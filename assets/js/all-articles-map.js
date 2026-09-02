/**
 * all-articles-map.js
 * Full-collection map: every article plotted at its place of publication,
 * revealed over time with a play/slider control. Nearby articles are
 * clustered into a single circle (sized by count); hovering a point shows a
 * lightweight preview, clicking it pins a detail panel — a scrollable table
 * of every article in it, for a cluster — that stays open until closed.
 *
 * Depends on (loaded by the page, not this file):
 *   MapLibre GL  3.6.2  — https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.js
 *   deck.gl      8.9.35 — https://unpkg.com/deck.gl@8.9.35/dist.min.js
 *
 * Usage:
 *   const m = new AllArticlesMap('all-articles-map', data, { autoplay: false });
 */
(function () {
  'use strict';

  // ── Constants ──────────────────────────────────────────────────────────────
  const BASE_FRAMES = 220;  // frames for full timeline at speed 1×
  const CTRL_H      = 52;   // px height of the controls bar
  const CLUSTER_PX  = 30;   // clustering radius, in screen pixels, at current zoom
  const DOT_COLOR   = [99, 102, 241]; // indigo #6366f1
  const MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

  // ── Helpers ────────────────────────────────────────────────────────────────
  /**
   * Normalize partial date strings so Date() parsing is always safe.
   *   "1847"       → "1847-01-01"
   *   "1847-03"    → "1847-03-01"
   *   "1847-03-15" → unchanged
   */
  function normalizeDate(dateStr) {
    if (!dateStr) return '1970-01-01';
    var parts = dateStr.split('-');
    if (parts.length === 1) return dateStr + '-01-01';
    if (parts.length === 2) return dateStr + '-01';
    return dateStr;
  }

  /** "1847-01-07" → "Jan 7, 1847" (handles year-only and year-month strings too) */
  function fmtDate(dateStr) {
    if (!dateStr) return '';
    var parts = dateStr.split('-');
    if (parts.length === 1) return parts[0];
    if (parts.length === 2) return MONTHS[+parts[1] - 1] + ' ' + parts[0];
    return MONTHS[+parts[1] - 1] + ' ' + (+parts[2]) + ', ' + parts[0];
  }

  /** Unix-ms timestamp → "Jan 7, 1847" (UTC) */
  function tsToDisplayDate(ts) {
    const d = new Date(ts);
    return `${MONTHS[d.getUTCMonth()]} ${d.getUTCDate()}, ${d.getUTCFullYear()}`;
  }

  /** Thin helper: create a DOM element with inline CSS and optional innerHTML. */
  function el(tag, css, html) {
    const e = document.createElement(tag);
    if (css)  e.style.cssText = css;
    if (html != null) e.innerHTML = html;
    return e;
  }

  /** Escape text dropped into tooltip HTML. */
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>]/g, function (c) {
      return c === '&' ? '&amp;' : c === '<' ? '&lt;' : '&gt;';
    });
  }

  /**
   * Greedy single-link clustering: groups points within CLUSTER_PX screen
   * pixels of each other at the given zoom. Good enough at collection scale
   * (a few hundred points) — recomputed every render, so clusters grow and
   * shrink as points appear over the timeline and as the user zooms.
   */
  function clusterPoints(points, zoom) {
    const metersPerPxBase = 40075016.686 / (256 * Math.pow(2, zoom));
    const used = new Array(points.length).fill(false);
    const clusters = [];
    for (let i = 0; i < points.length; i++) {
      if (used[i]) continue;
      const group = [points[i]];
      used[i] = true;
      const mpp = metersPerPxBase * Math.cos(points[i].lat * Math.PI / 180) || metersPerPxBase;
      for (let j = i + 1; j < points.length; j++) {
        if (used[j]) continue;
        const dLat = (points[j].lat - points[i].lat) * 110574;
        const dLng = (points[j].lng - points[i].lng) * 111320 * Math.cos(points[i].lat * Math.PI / 180);
        const distPx = Math.sqrt(dLat * dLat + dLng * dLng) / mpp;
        if (distPx < CLUSTER_PX) { group.push(points[j]); used[j] = true; }
      }
      let sumLat = 0, sumLng = 0;
      group.forEach(function (p) { sumLat += p.lat; sumLng += p.lng; });
      clusters.push({ lat: sumLat / group.length, lng: sumLng / group.length, items: group });
    }
    return clusters;
  }

  // ── Constructor ────────────────────────────────────────────────────────────
  window.AllArticlesMap = function AllArticlesMap(containerId, data, options) {
    options = options || {};

    const container = document.getElementById(containerId);
    if (!container) throw new Error('AllArticlesMap: no element with id "' + containerId + '"');

    container.style.position = 'relative';
    container.style.overflow = 'hidden';
    container.style.background = '#0f111e';

    // ── Guard: no geocoded rows ────────────────────────────────────────────
    if (!data || data.length === 0) {
      container.appendChild(el(
        'p',
        'position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);' +
        'color:#6b7280;font-size:13px;text-align:center;padding:1rem;margin:0;' +
        'font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;',
        'No location data available.'
      ));
      return { play: function () {}, pause: function () {}, reset: function () {} };
    }

    const uid = 'aam_' + containerId;

    // ── Process data ─────────────────────────────────────────────────────
    const RAW = data.map(function (d) { return Object.assign({}, d); });
    RAW.forEach(function (d) { d.ts = new Date(normalizeDate(d.date) + 'T12:00:00Z').getTime(); });
    RAW.sort(function (a, b) { return a.ts - b.ts; });

    const MIN_TS = RAW[0].ts;
    const MAX_TS = RAW[RAW.length - 1].ts;
    const RANGE  = MAX_TS - MIN_TS || 1;
    const isSingleDate = MIN_TS === MAX_TS;

    // ── DOM: map canvas area ─────────────────────────────────────────────
    const mapDiv = el('div', 'position:absolute;top:0;left:0;right:0;bottom:' + CTRL_H + 'px;');
    mapDiv.id = uid + '_map';
    container.appendChild(mapDiv);

    // ── DOM: legend ──────────────────────────────────────────────────────
    const legend = el(
      'div',
      'position:absolute;top:8px;left:8px;z-index:100;' +
      'background:rgba(10,12,24,0.85);border:1px solid #1e2340;border-radius:8px;' +
      'padding:10px 12px;font-size:12px;color:#9ca3af;max-width:200px;' +
      'font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;',
      '<div style="color:#6366f1;font-weight:700;font-size:10px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;padding-bottom:5px;border-bottom:1px solid #1e2340">' +
      RAW.length + ' Articles</div>' +
      '<div style="display:flex;align-items:center;gap:8px;">' +
      '<div style="width:8px;height:8px;border-radius:50%;background:#6366f1;flex-shrink:0"></div>' +
      '<span>One article</span></div>' +
      '<div style="display:flex;align-items:center;gap:8px;margin-top:4px;">' +
      '<div style="width:16px;height:16px;border-radius:50%;background:#6366f1;flex-shrink:0"></div>' +
      '<span>Cluster &mdash; hover for list and click to hold table</span></div>'
    );
    container.appendChild(legend);

    // ── DOM: tooltip ─────────────────────────────────────────────────────
    const tooltipEl = el(
      'div',
      'position:absolute;z-index:200;pointer-events:none;display:none;' +
      'background:rgba(10,12,24,0.95);border:1px solid #374151;border-radius:7px;' +
      'padding:10px 13px;font-size:12px;color:#9ca3af;line-height:1.5;' +
      'font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;'
    );
    container.appendChild(tooltipEl);

    // ── DOM: controls bar ─────────────────────────────────────────────────
    const ctrlBar = el(
      'div',
      'position:absolute;bottom:0;left:0;right:0;height:' + CTRL_H + 'px;' +
      'background:rgba(10,12,24,0.92);border-top:1px solid #1e2340;' +
      'display:flex;align-items:center;padding:0 14px;gap:10px;' +
      'font-size:12px;color:#9ca3af;z-index:100;box-sizing:border-box;' +
      'font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;'
    );
    container.appendChild(ctrlBar);

    const playBtn = el(
      'button',
      'width:30px;height:30px;border-radius:50%;background:#6366f1;border:none;' +
      'color:white;cursor:pointer;font-size:13px;display:flex;align-items:center;' +
      'justify-content:center;flex-shrink:0;transition:background 0.15s;',
      '▶'
    );
    playBtn.title = 'Play / Pause';
    playBtn.addEventListener('mouseover', function () { playBtn.style.background = '#4f46e5'; });
    playBtn.addEventListener('mouseout',  function () { playBtn.style.background = isPlaying ? '#4f46e5' : '#6366f1'; });

    const resetBtn = el(
      'button',
      'padding:4px 10px;border-radius:5px;background:transparent;' +
      'border:1px solid #374151;color:#9ca3af;cursor:pointer;font-size:11px;' +
      'flex-shrink:0;transition:border-color 0.15s;',
      '↺'
    );
    resetBtn.title = 'Reset';
    resetBtn.addEventListener('mouseover', function () { resetBtn.style.borderColor='#6b7280'; resetBtn.style.color='#e2e8f0'; });
    resetBtn.addEventListener('mouseout',  function () { resetBtn.style.borderColor='#374151'; resetBtn.style.color='#9ca3af'; });

    const div1 = el('div', 'width:1px;height:28px;background:#1e2340;flex-shrink:0;');

    const dateLabel = el(
      'span',
      'color:#e2e8f0;font-size:12px;font-weight:600;min-width:100px;white-space:nowrap;flex-shrink:0;'
    );
    dateLabel.textContent = fmtDate(RAW[0].date);

    const timeSlider = el('input', 'flex:1;accent-color:#6366f1;cursor:pointer;min-width:60px;');
    timeSlider.type  = 'range';
    timeSlider.min   = '0';
    timeSlider.max   = '1000';
    timeSlider.value = '0';
    timeSlider.step  = '1';

    const dateEnd = el(
      'span',
      'color:#6b7280;font-size:11px;white-space:nowrap;flex-shrink:0;'
    );
    dateEnd.textContent = fmtDate(RAW[RAW.length - 1].date);

    const div2 = el('div', 'width:1px;height:28px;background:#1e2340;flex-shrink:0;');

    const speedLabel = el(
      'span',
      'font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:#4b5563;flex-shrink:0;',
      'Speed'
    );

    const speedSlider = el('input', 'width:80px;accent-color:#818cf8;cursor:pointer;flex-shrink:0;');
    speedSlider.type  = 'range';
    speedSlider.min   = '0.2';
    speedSlider.max   = '4';
    speedSlider.step  = '0.2';
    speedSlider.value = '1';

    const speedVal = el(
      'span',
      'color:#a5b4fc;font-weight:700;min-width:30px;flex-shrink:0;',
      '1.0×'
    );

    [playBtn, resetBtn, div1, dateLabel, timeSlider, dateEnd, div2, speedLabel, speedSlider, speedVal]
      .forEach(function (n) { ctrlBar.appendChild(n); });

    if (isSingleDate) {
      ctrlBar.style.display = 'none';
      mapDiv.style.bottom   = '0';
    }

    // ── Animation state ───────────────────────────────────────────────────
    var currentTs = isSingleDate ? MAX_TS : MIN_TS;
    var isPlaying  = false;
    var animTimer  = null;
    var speed      = 1;

    // ── MapLibre basemap ──────────────────────────────────────────────────
    var minLng =  Infinity, maxLng = -Infinity, minLat =  Infinity, maxLat = -Infinity;
    RAW.forEach(function (d) {
      if (d.lng < minLng) minLng = d.lng;
      if (d.lng > maxLng) maxLng = d.lng;
      if (d.lat < minLat) minLat = d.lat;
      if (d.lat > maxLat) maxLat = d.lat;
    });
    const isSingleLocation = (minLng === maxLng && minLat === maxLat);

    var map = new maplibregl.Map({
      container: mapDiv.id,
      style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
      center: isSingleLocation ? [minLng, minLat] : [(minLng + maxLng) / 2, (minLat + maxLat) / 2],
      zoom: isSingleLocation ? 6 : 1.5,
      attributionControl: true
    });

    var overlay = new deck.MapboxOverlay({ interleaved: false, layers: [] });
    map.addControl(overlay);

    // ── Render ────────────────────────────────────────────────────────────
    function render() {
      var zoom    = map.getZoom();
      var visible = RAW.filter(function (d) { return d.ts <= currentTs; });
      var clusters = clusterPoints(visible, zoom);

      var layer = new deck.ScatterplotLayer({
        id: uid + '_points',
        data: clusters,
        getPosition:  function (d) { return [d.lng, d.lat]; },
        getFillColor: DOT_COLOR,
        getRadius:    function (d) { return 18000 + Math.sqrt(d.items.length) * 16000; },
        radiusMinPixels: 6,
        radiusMaxPixels: 46,
        opacity: 0.82,
        stroked: true,
        getLineColor: [255, 255, 255, 160],
        lineWidthMinPixels: 1,
        pickable: true,
        onHover: handleHover,
        onClick: handleClick,
        updateTriggers: { getPosition: [currentTs, zoom], getRadius: [currentTs, zoom] }
      });

      overlay.setProps({ layers: [layer], getTooltip: null });
    }

    // ── Tooltip ───────────────────────────────────────────────────────────
    // Hover gives a lightweight, ephemeral preview (full detail for a single
    // article; just a count + prompt for a cluster, since a hover tooltip
    // can never be scrolled — the pointer has to cross empty canvas to reach
    // it, which cancels the hover before it gets there). Clicking a point
    // "pins" the tooltip instead: it stops following the mouse and gets a
    // close button, so a multi-article cluster's table can actually be
    // scrolled.
    var pinned = null;

    function singleItemHtml(a) {
      var loc = a.publisher_location ? esc(a.publisher_location) : '';
      return '<div style="color:#e2e8f0;font-weight:600;margin-bottom:2px;font-size:13px">' + esc(a.title) + '</div>' +
        '<div>' + esc(a.publication) + (loc ? ', ' + loc : '') + '</div>' +
        '<div>' + fmtDate(a.date) + '</div>';
    }

    function clusterTableHtml(d) {
      var sorted = d.items.slice().sort(function (p, q) { return p.ts - q.ts; });
      var rows = sorted.map(function (a) {
        return '<tr>' +
          '<td style="padding:2px 6px 2px 0;color:#e2e8f0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">' + esc(a.title) + '</td>' +
          '<td style="padding:2px 6px 2px 0;color:#9ca3af;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">' + esc(a.publication) + '</td>' +
          '<td style="padding:2px 0;color:#6b7280;white-space:nowrap;">' + fmtDate(a.date) + '</td>' +
          '</tr>';
      }).join('');
      return '<div style="color:#e2e8f0;font-weight:600;margin-bottom:5px;font-size:12px">' +
        d.items.length + ' articles' +
        (sorted[0].publisher_location ? ' &middot; ' + esc(sorted[0].publisher_location) : '') +
        '</div>' +
        '<div style="max-height:190px;overflow-y:auto;overflow-x:hidden;">' +
        '<table style="border-collapse:collapse;table-layout:fixed;width:340px;font-size:11px;">' +
        '<colgroup><col style="width:150px"><col style="width:100px"><col style="width:90px"></colgroup>' +
        rows + '</table></div>';
    }

    function positionTooltip(x, y, tw, th) {
      var cw = container.offsetWidth;
      var ch = container.offsetHeight;
      tooltipEl.style.maxWidth = tw + 'px';
      tooltipEl.style.left = (x + 14 + tw > cw ? x - tw - 14 : x + 14) + 'px';
      tooltipEl.style.top  = (y + 14 + th > ch ? y - th - 14 : y + 14) + 'px';
      tooltipEl.style.display = 'block';
    }

    function handleHover(info) {
      if (pinned) return; // frozen while a pinned tooltip is open
      var d = info.object;
      if (!d) { hideTooltip(); return; }

      if (d.items.length === 1) {
        tooltipEl.style.pointerEvents = 'none';
        tooltipEl.innerHTML = singleItemHtml(d.items[0]);
        positionTooltip(info.x, info.y, 240, 90);
      } else {
        tooltipEl.style.pointerEvents = 'none';
        tooltipEl.innerHTML =
          '<div style="color:#e2e8f0;font-weight:600;font-size:12px">' + d.items.length + ' articles' +
          (d.items[0].publisher_location ? ' &middot; ' + esc(d.items[0].publisher_location) : '') + '</div>' +
          '<div style="color:#6b7280;margin-top:3px;">Click to view list</div>';
        positionTooltip(info.x, info.y, 220, 60);
      }
    }

    function handleClick(info) {
      var d = info.object;
      if (!d) return;
      pinned = d;

      var closeBtn = '<button class="' + uid + '_close" style="position:absolute;top:6px;right:8px;background:none;' +
        'border:none;color:#9ca3af;font-size:15px;line-height:1;cursor:pointer;padding:2px 4px;">&times;</button>';

      var tw, th;
      if (d.items.length === 1) {
        tooltipEl.innerHTML = closeBtn + '<div style="padding-right:16px;">' + singleItemHtml(d.items[0]) + '</div>';
        tw = 240; th = 100;
      } else {
        tooltipEl.innerHTML = closeBtn + '<div style="padding-right:16px;">' + clusterTableHtml(d) + '</div>';
        tw = 370; th = 220;
      }

      tooltipEl.style.pointerEvents = 'auto';
      positionTooltip(info.x, info.y, tw, th);

      var btn = tooltipEl.querySelector('.' + uid + '_close');
      if (btn) btn.addEventListener('click', closePinned);
    }

    function closePinned() {
      pinned = null;
      hideTooltip();
    }

    function hideTooltip() {
      tooltipEl.style.display = 'none';
      tooltipEl.style.pointerEvents = 'none';
    }

    // ── Animation helpers ─────────────────────────────────────────────────
    function syncUI() {
      var pct = (currentTs - MIN_TS) / RANGE;
      timeSlider.value    = Math.round(pct * 1000);
      dateLabel.textContent = tsToDisplayDate(currentTs);
    }

    function tick() {
      var inc = (RANGE / BASE_FRAMES) * speed;
      currentTs = Math.min(currentTs + inc, MAX_TS);
      syncUI();
      render();
      if (currentTs >= MAX_TS) pause();
    }

    function play() {
      closePinned(); // clusters shift as new points appear — a pinned table would go stale
      if (currentTs >= MAX_TS) currentTs = MIN_TS;
      isPlaying = true;
      playBtn.innerHTML = '⏸';
      animTimer = setInterval(tick, 100);
    }

    function pause() {
      isPlaying = false;
      clearInterval(animTimer);
      animTimer = null;
      playBtn.innerHTML = '▶';
    }

    function reset() {
      closePinned();
      pause();
      currentTs = MIN_TS;
      syncUI();
      render();
    }

    // ── Control listeners ─────────────────────────────────────────────────
    playBtn.addEventListener('click', function () { if (isPlaying) pause(); else play(); });
    resetBtn.addEventListener('click', reset);

    timeSlider.addEventListener('input', function () {
      closePinned();
      pause();
      currentTs = MIN_TS + RANGE * (this.value / 1000);
      dateLabel.textContent = tsToDisplayDate(currentTs);
      render();
    });

    speedSlider.addEventListener('input', function () {
      speed = parseFloat(this.value);
      speedVal.textContent = speed.toFixed(1) + '×';
    });

    // ── Map ready ─────────────────────────────────────────────────────────
    map.on('load', function () {
      if (!isSingleLocation) {
        map.fitBounds([[minLng, minLat], [maxLng, maxLat]], { padding: 40, duration: 0 });
      }
      render();
      if (!isSingleDate && options.autoplay) play();
    });

    map.on('zoom', function () { closePinned(); render(); });

    // ── Public API ─────────────────────────────────────────────────────────
    return { play: play, pause: pause, reset: reset };
  };

}());

// ── Auto-init ────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
  var container = document.getElementById('all-articles-map');
  if (!container || typeof AllArticlesMap === 'undefined') return;
  var data = window._allArticlesMapData || [];
  requestAnimationFrame(function () {
    window._allArticlesMapInstance = new AllArticlesMap('all-articles-map', data, { autoplay: false });
  });
});
