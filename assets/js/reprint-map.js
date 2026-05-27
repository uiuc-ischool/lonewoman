/**
 * reprint-map.js
 * Reusable animated reprint-network map widget.
 *
 * Depends on (loaded by the page, not this file):
 *   MapLibre GL  3.6.2  — https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.js
 *   deck.gl      8.9.35 — https://unpkg.com/deck.gl@8.9.35/dist.min.js
 *
 * Usage:
 *   const rm = new ReprintMap('my-container', reprints, { autoplay: true, height: '320px' });
 *   rm.play();  rm.pause();  rm.reset();
 */
(function () {
  'use strict';

  // ── Constants ──────────────────────────────────────────────────────────────
  const SPLAY_PX    = 12;   // pixel radius for co-located splay circle
  const BASE_FRAMES = 140;  // frames for full timeline at speed 1×
  const CTRL_H      = 52;   // px height of the controls bar
  const MONTHS      = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

  const TYPE_COLORS = {
    original:   [209, 213, 219],  // gray   #d1d5db
    direct:     [ 59, 130, 246],  // blue   #3b82f6
    truncated:  [249, 115,  22],  // orange #f97316
    paraphrase: [ 34, 197,  94],  // green  #22c55e
  };

  const TYPE_BADGE_STYLE = {
    original:   'background:rgba(200,200,200,0.20);color:#d1d5db',
    direct:     'background:rgba(59,130,246,0.25);color:#93c5fd',
    truncated:  'background:rgba(249,115,22,0.25);color:#fdba74',
    paraphrase: 'background:rgba(34,197,94,0.20);color:#86efac',
  };

  // ── Helpers ────────────────────────────────────────────────────────────────
  function getColor(d) { return TYPE_COLORS[d.reprint_type] || [200, 200, 200]; }

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
    if (parts.length === 1) return parts[0];                            // "1847"
    if (parts.length === 2) return MONTHS[+parts[1] - 1] + ' ' + parts[0]; // "Jan 1847"
    return MONTHS[+parts[1] - 1] + ' ' + (+parts[2]) + ', ' + parts[0];
  }

  /** Unix-ms timestamp → "Jan 7, 1847" (UTC) */
  function tsToDisplayDate(ts) {
    const d = new Date(ts);
    return `${MONTHS[d.getUTCMonth()]} ${d.getUTCDate()}, ${d.getUTCFullYear()}`;
  }

  /**
   * Returns [lng, lat] with a pixel-stable circular offset for co-located points.
   * Groups of size 1 are returned unchanged.
   */
  function getSplayedPos(d, zoom) {
    if (d._n === 1) return [d.lng, d.lat];
    const metersPerPx =
      (40075016.686 / (256 * Math.pow(2, zoom))) *
      Math.cos((d.lat * Math.PI) / 180);
    const offsetM = SPLAY_PX * metersPerPx;
    const latOff  = offsetM / 111320;
    const lngOff  = offsetM / (111320 * Math.cos((d.lat * Math.PI) / 180));
    const angle   = (2 * Math.PI * d._i) / d._n - Math.PI / 2;
    return [d.lng + Math.cos(angle) * lngOff, d.lat + Math.sin(angle) * latOff];
  }

  /** Thin helper: create a DOM element with inline CSS and optional innerHTML. */
  function el(tag, css, html) {
    const e = document.createElement(tag);
    if (css)  e.style.cssText = css;
    if (html != null) e.innerHTML = html;
    return e;
  }

  // ── Constructor ────────────────────────────────────────────────────────────
  window.ReprintMap = function ReprintMap(containerId, data, options) {
    options = options || {};

    const container = document.getElementById(containerId);
    if (!container) throw new Error('ReprintMap: no element with id "' + containerId + '"');

    // Scope container
    container.style.position = 'relative';
    container.style.overflow = 'hidden';
    container.style.background = '#0f111e';
    if (options.height) container.style.height = options.height;

    // ── Guard 1: no geocoded rows ─────────────────────────────────────────
    if (!data || data.length === 0) {
      container.appendChild(el(
        'p',
        'position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);' +
        'color:#6b7280;font-size:13px;text-align:center;padding:1rem;margin:0;' +
        'font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;',
        'No location data available for this group.'
      ));
      return { play: function () {}, pause: function () {}, reset: function () {} };
    }

    // Unique prefix so multiple instances on the same page don't clash
    const uid = 'rm_' + containerId;

    // ── Process data ─────────────────────────────────────────────────────
    const RAW = data.map(function (d) { return Object.assign({}, d); });
    RAW.forEach(function (d) {
      // Guard 4: handle year-only ("1847") and year-month ("1847-03") date strings
      d.ts = new Date(normalizeDate(d.date) + 'T12:00:00Z').getTime();
    });
    RAW.sort(function (a, b) { return a.ts - b.ts; });

    const MIN_TS = RAW[0].ts;
    const MAX_TS = RAW[RAW.length - 1].ts;
    const RANGE  = MAX_TS - MIN_TS || 1;

    // Guard 5: all rows share the same timestamp → skip animation entirely
    const isSingleDate = MIN_TS === MAX_TS;

    // Build splay index from ALL points so positions are stable as animation plays
    const _locGroups = {};
    RAW.forEach(function (d) {
      const key = d.lat + ',' + d.lng;
      if (!_locGroups[key]) _locGroups[key] = [];
      _locGroups[key].push(d);
    });
    RAW.forEach(function (d) {
      const key  = d.lat + ',' + d.lng;
      const grp  = _locGroups[key];
      d._n = grp.length;
      d._i = grp.indexOf(d);
    });

    // Guard 2: all destination points share the same location → skip arcs
    const isSingleLocation = Object.keys(_locGroups).length === 1;

    // ── DOM: map canvas area ─────────────────────────────────────────────
    const mapDiv = el('div', 'position:absolute;top:0;left:0;right:0;bottom:' + CTRL_H + 'px;');
    mapDiv.id = uid + '_map';
    container.appendChild(mapDiv);

    // ── DOM: legend ──────────────────────────────────────────────────────
    const legend = el(
      'div',
      'position:absolute;top:8px;left:8px;z-index:100;' +
      'background:rgba(10,12,24,0.85);border:1px solid #1e2340;border-radius:8px;' +
      'padding:10px 12px;font-size:12px;color:#9ca3af;' +
      'font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;',
      '<div style="color:#e2e8f0;font-weight:600;font-size:10px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px">Reprint Type</div>' +
      '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px"><div style="width:9px;height:9px;border-radius:50%;background:#d1d5db;flex-shrink:0"></div><span>Original</span></div>' +
      '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px"><div style="width:9px;height:9px;border-radius:50%;background:#3b82f6;flex-shrink:0"></div><span>Direct</span></div>' +
      '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px"><div style="width:9px;height:9px;border-radius:50%;background:#f97316;flex-shrink:0"></div><span>Truncated</span></div>' +
      '<div style="display:flex;align-items:center;gap:8px"><div style="width:9px;height:9px;border-radius:50%;background:#22c55e;flex-shrink:0"></div><span>Paraphrase</span></div>'
    );
    container.appendChild(legend);

    // ── DOM: tooltip ─────────────────────────────────────────────────────
    const tooltipEl = el(
      'div',
      'position:absolute;z-index:200;pointer-events:none;display:none;' +
      'background:rgba(10,12,24,0.93);border:1px solid #374151;border-radius:7px;' +
      'padding:10px 13px;font-size:12px;color:#9ca3af;max-width:230px;line-height:1.6;' +
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

    // Play button
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

    // Reset button
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

    // Divider
    const div1 = el('div', 'width:1px;height:28px;background:#1e2340;flex-shrink:0;');

    // Current-date label
    const dateLabel = el(
      'span',
      'color:#e2e8f0;font-size:12px;font-weight:600;min-width:100px;white-space:nowrap;flex-shrink:0;'
    );
    dateLabel.textContent = fmtDate(RAW[0].date);

    // Time scrubber
    const timeSlider = el('input', 'flex:1;accent-color:#6366f1;cursor:pointer;min-width:60px;');
    timeSlider.type  = 'range';
    timeSlider.min   = '0';
    timeSlider.max   = '1000';
    timeSlider.value = '0';
    timeSlider.step  = '1';

    // End-date label
    const dateEnd = el(
      'span',
      'color:#6b7280;font-size:11px;white-space:nowrap;flex-shrink:0;'
    );
    dateEnd.textContent = fmtDate(RAW[RAW.length - 1].date);

    // Divider
    const div2 = el('div', 'width:1px;height:28px;background:#1e2340;flex-shrink:0;');

    // Speed label
    const speedLabel = el(
      'span',
      'font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:#4b5563;flex-shrink:0;',
      'Speed'
    );

    // Speed slider (0.2× – 4×)
    const speedSlider = el('input', 'width:80px;accent-color:#818cf8;cursor:pointer;flex-shrink:0;');
    speedSlider.type  = 'range';
    speedSlider.min   = '0.2';
    speedSlider.max   = '4';
    speedSlider.step  = '0.2';
    speedSlider.value = '1';

    // Speed readout
    const speedVal = el(
      'span',
      'color:#a5b4fc;font-weight:700;min-width:30px;flex-shrink:0;',
      '1.0×'
    );

    [playBtn, resetBtn, div1, dateLabel, timeSlider, dateEnd, div2, speedLabel, speedSlider, speedVal]
      .forEach(function (n) { ctrlBar.appendChild(n); });

    // Guard 5: single unique date → hide controls bar, map fills full container
    if (isSingleDate) {
      ctrlBar.style.display = 'none';
      mapDiv.style.bottom   = '0';
    }

    // ── Animation state ───────────────────────────────────────────────────
    // Guard 5: start at MAX_TS so all points are visible immediately
    var currentTs = isSingleDate ? MAX_TS : MIN_TS;
    var isPlaying  = false;
    var animTimer  = null;
    var speed      = 1;

    // ── MapLibre basemap ──────────────────────────────────────────────────
    var map = new maplibregl.Map({
      container: mapDiv.id,
      style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
      center: [-88, 39],
      zoom: 4,
      attributionControl: true
    });

    // ── deck.gl overlay ───────────────────────────────────────────────────
    var overlay = new deck.MapboxOverlay({ interleaved: false, layers: [] });
    map.addControl(overlay);

    // ── Render ────────────────────────────────────────────────────────────
    function render() {
      var zoom    = map.getZoom();
      var visible = RAW.filter(function (d) { return d.ts <= currentTs; });

      var layers = [];

      // Guard 2: skip arcs when all points share one location (zero-length arcs
      // look like noise; ScatterplotLayer alone is cleaner)
      if (!isSingleLocation) {
        var arcData = visible.filter(function (d) { return d.reprint_type !== 'original'; });
        layers.push(new deck.ArcLayer({
          id: uid + '_arcs',
          data: arcData,
          // Guard 3: fall back to destination coords when origin is missing/zero
          getSourcePosition: function (d) {
            var oLat = (d.origin_lat && d.origin_lat !== 0) ? d.origin_lat : d.lat;
            var oLng = (d.origin_lng && d.origin_lng !== 0) ? d.origin_lng : d.lng;
            return [oLng, oLat];
          },
          getTargetPosition: function (d) { return getSplayedPos(d, zoom); },
          getSourceColor:    function (d) { return getColor(d); },
          getTargetColor:    function (d) { return getColor(d); },
          getWidth: 2.5,
          widthMinPixels: 1.5,
          opacity: 0.82,
          pickable: true,
          onHover: handleHover,
          updateTriggers: { getTargetPosition: [currentTs, zoom] }
        }));
      }

      layers.push(new deck.ScatterplotLayer({
        id: uid + '_points',
        data: visible,
        getPosition:  function (d) { return getSplayedPos(d, zoom); },
        getFillColor: function (d) { return getColor(d); },
        getRadius:    function (d) { return d.reprint_type === 'original' ? 55000 : 32000; },
        radiusMinPixels: 5,
        radiusMaxPixels: 18,
        opacity: 0.95,
        stroked: true,
        getLineColor: [255, 255, 255, 160],
        lineWidthMinPixels: 1,
        pickable: true,
        onHover: handleHover,
        updateTriggers: { getPosition: [currentTs, zoom] }
      }));

      overlay.setProps({ layers: layers, getTooltip: null });
    }

    // ── Tooltip ───────────────────────────────────────────────────────────
    function handleHover(info) {
      var object = info.object, x = info.x, y = info.y;
      if (!object) { tooltipEl.style.display = 'none'; return; }
      var d = object;
      var bStyle = TYPE_BADGE_STYLE[d.reprint_type] || 'background:rgba(150,150,150,0.2);color:#ccc';
      tooltipEl.innerHTML =
        '<div style="color:#e2e8f0;font-weight:600;margin-bottom:2px;font-size:13px">' + d.publication + '</div>' +
        '<div>' + d.publisher_location + '</div>' +
        '<div>' + fmtDate(d.date) + '</div>' +
        '<span style="display:inline-block;margin-top:5px;padding:1px 7px;border-radius:4px;' +
        'font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;' + bStyle + '">' +
        d.reprint_type + '</span>';

      // Keep inside container bounds
      var cw = container.offsetWidth;
      var ch = container.offsetHeight;
      var tw = 240, th = 110;
      tooltipEl.style.left = (x + 14 + tw > cw ? x - tw - 14 : x + 14) + 'px';
      tooltipEl.style.top  = (y + 14 + th > ch ? y - th - 14 : y + 14) + 'px';
      tooltipEl.style.display = 'block';
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
      pause();
      currentTs = MIN_TS;
      syncUI();
      render();
    }

    // ── Control listeners ─────────────────────────────────────────────────
    playBtn.addEventListener('click', function () { if (isPlaying) pause(); else play(); });
    resetBtn.addEventListener('click', reset);

    timeSlider.addEventListener('input', function () {
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
      // Guard 2: single location → center on that point at zoom 6 instead of fitBounds
      if (isSingleLocation) {
        map.setCenter([RAW[0].lng, RAW[0].lat]);
        map.setZoom(6);
      } else {
        var minLng =  Infinity, maxLng = -Infinity;
        var minLat =  Infinity, maxLat = -Infinity;
        RAW.forEach(function (d) {
          if (d.lng < minLng) minLng = d.lng;
          if (d.lng > maxLng) maxLng = d.lng;
          if (d.lat < minLat) minLat = d.lat;
          if (d.lat > maxLat) maxLat = d.lat;
        });
        map.fitBounds([[minLng, minLat], [maxLng, maxLat]], { padding: 40, duration: 0 });
      }

      render();

      // Guard 5: don't autoplay when there's nothing to animate
      if (!isSingleDate && options.autoplay) play();
    });

    // Re-render on zoom so splay radius stays pixel-stable
    map.on('zoom', function () { render(); });

    // ── Public API ─────────────────────────────────────────────────────────
    return { play: play, pause: pause, reset: reset };
  };

}());

// ── Global registry for lazy initialization ────────────────────────────────
// _includes/reprint-map.html stores each group's data array here, keyed by
// container id.  The toggle listener below reads from it on first open.
window._reprintMapRegistry = window._reprintMapRegistry || {};

// ── Lazy initializer ───────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('details.map-group').forEach(function (det) {
    det.addEventListener('toggle', function () {
      if (!det.open) return;
      var container = det.querySelector('.reprint-map-container');
      if (!container || container.dataset.initialized) return;
      var data = window._reprintMapRegistry[container.id];
      if (!data || typeof ReprintMap === 'undefined') return;

      // Mark immediately to prevent double-init if the user rapidly toggles.
      container.dataset.initialized = 'true';

      // Defer one frame so the browser reflows the container (it just transitioned
      // from display:none → visible via CSS).  Without this, MapLibre reads
      // clientWidth/clientHeight = 0 and creates a zero-size canvas.
      requestAnimationFrame(function () {
        new ReprintMap(container.id, data, { autoplay: true });
      });
    });
  });
});
