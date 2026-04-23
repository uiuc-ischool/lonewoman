#!/usr/bin/env python3
"""Generate three reprint network interactive map HTML files."""

import csv
import json
import time
import re
import os

# ── Coordinate cache ────────────────────────────────────────────────────────
COORD_CACHE = {
    "New York, New York":                       (40.7128,  -74.0060),
    "Edgefield, South Carolina":                (33.7893,  -81.9293),
    "Huntington, New York":                     (40.8676,  -73.4257),
    "Bedford, Massachusetts":                   (41.6362,  -70.9342),
    "Philadelphia, Pennsylvania":               (39.9526,  -75.1652),
    "Batavia, New York":                        (42.9980,  -78.1876),
    "Boston, Massachusetts":                    (42.3601,  -71.0589),
    "Ithaca, New York":                         (42.4440,  -76.5022),
    "Honolulu, Hawaii":                         (21.3069, -157.8583),
    "Windsor, Vermont":                         (43.4799,  -72.3866),
    "Lancaster, Wisconsin":                     (42.8477,  -90.7102),
    "Belvidere, Illinois":                      (42.2639,  -88.8441),
    "Savannah, Georgia":                        (32.0809,  -81.0912),
    "Washington, DC":                           (38.9072,  -77.0369),
    "Fayetteville, North Carolina":             (35.0527,  -78.8784),
    "Franklin, Louisiana":                      (29.7960,  -91.5012),
    "Ironton, Ohio":                            (38.5363,  -82.6824),
    "Gettysburg, Pennsylvania":                 (39.8309,  -77.2311),
    "New-Lisbon, Ohio":                         (40.7720,  -80.9865),
    "Newburyport, Massachusetts":               (42.8137,  -70.8753),
    "Stroudsburg, Pennsylvania":                (40.9862,  -75.1968),
    "Salem, North Carolina":                    (36.0999,  -80.2442),
    "Millersburg, Ohio":                        (40.5545,  -81.9179),
    "San Francisco, California":                (37.7749, -122.4194),
    "Lowell, Massachusetts":                    (42.6334,  -71.3162),
    "New Orleans, Louisiana":                   (29.9511,  -90.0715),
    "Sacramento, California":                   (38.5816, -121.4944),
    "Santa Barbara, California":                (34.4208, -119.6982),
    "Fort Atkinson, Wisconsin":                 (42.9288,  -88.8371),
    "Chicago, Illinois":                        (41.8781,  -87.6298),
    "Melbourne, Victoria, Australia":           (-37.8136, 144.9631),
    "Goulburn, New South Wales, Australia":     (-34.7523, 149.7194),
    "Memphis, Tennessee":                       (35.1495,  -90.0490),
    "Los Angeles, California":                  (34.0522, -118.2437),
    "Charlotte, North Carolina":                (35.2271,  -80.8431),
    "Wilmington, North Carolina":               (34.2257,  -77.9447),
    # Map 2 new locations
    "Katanning, Western Australia, Australia":  (-33.6908, 117.5556),
    "Maryborough, Queensland, Australia":       (-25.5377, 152.7021),
    "Oamaru, North Otago, New Zealand":         (-45.0971, 170.9714),
    "Tokomairiro, Otago, New Zealand":          (-46.1169, 169.9623),
    "Rockhampton, Queensland, Australia":       (-23.3782, 150.5094),
    "Saint Paul, Minnesota":                    (44.9537,  -93.0900),
    "Brisbane, Queensland, Australia":          (-27.4698, 153.0251),
    "Dublin, Ireland, United Kingdom":          (53.3498,   -6.2603),
    "Albany, New York":                         (42.6526,  -73.7562),
    "Burlington, Vermont":                      (44.4759,  -73.2121),
    "Ebensburg, Pennsylvania":                  (40.4855,  -78.7252),
    "Launceston, Tasmania, Australia":          (-41.4332, 147.1441),
    "Decatur, Illinois":                        (39.8403,  -88.9548),
    "Newcastle, New South Wales, Australia":    (-32.9283, 151.7817),
    "Reading, Pennsylvania":                    (40.3356,  -75.9269),
    "Rochester, New York":                      (43.1566,  -77.6088),
    "Salem, New York":                          (43.1731,  -73.3349),
    "London, England, United Kingdom":          (51.5074,   -0.1278),
    "Canton, New York":                         (44.5956,  -75.1688),
    "Bath, New York":                           (42.3384,  -77.3170),
    "Winona, Minnesota":                        (43.9995,  -91.6416),
    "Cincinnati, Ohio":                         (39.1031,  -84.5120),
    "Thames, North Island, New Zealand":        (-37.1378, 175.5356),
    "Morganton, North Carolina":                (35.7457,  -81.6849),
    "Mount Gambier, South Australia, Australia":(-37.8269, 140.7832),
    "Council Grove, Kansas":                    (38.6611,  -96.4911),
    "Montreal, Québec, Canada":                 (45.5017,  -73.5673),
    "Kapunda, South Australia, Australia":      (-34.3358, 138.9146),
    "Kiama, New South Wales, Australia":        (-34.6711, 150.8545),
    "Maitland, New South Wales, Australia":     (-32.7315, 151.5581),
    "Millheim, Pennsylvania":                   (40.8942,  -77.4849),
    "New Bern, North Carolina":                 (35.1085,  -77.0441),
    "St. John's, Newfoundland, Canada":         (47.5615,  -52.7126),
    "Newtown, New York":                        (40.7282,  -73.8898),
    "Clare, South Australia, Australia":        (-33.8355, 138.6147),
    "Lismore, New South Wales, Australia":      (-28.8140, 153.2773),
    "Dunedin, South Island, New Zealand":       (-45.8788, 170.5028),
    "Rockingham, North Carolina":               (34.9390,  -79.7717),
    "San Jose, California":                     (37.3382, -121.8863),
    "Queanbeyan, New South Wales, Australia":   (-35.3533, 149.2343),
    "Ipswich, Queensland, Australia":           (-27.6173, 152.7610),
    "Webster, Nebraska":                        (40.0853,  -98.5214),
    "Adelaide, South Australia, Australia":     (-34.9285, 138.6007),
    "Christchurch, South Island, New Zealand":  (-43.5321, 172.6362),
    "Mumbai, Maharashtra, India":               (19.0760,   72.8777),
    "Wagga Wagga, New South Wales, Australia":  (-35.1082, 147.3598),
    "Warwick, Queensland, Australia":           (-28.2131, 152.0333),
    "Tiffin, Ohio":                             (41.1142,  -83.1774),
    "Utica, New York":                          (43.1009,  -75.2327),
    "Watkins Glen, New York":                   (42.3786,  -76.8719),
    "Arkansas City, Kansas":                    (37.0642,  -97.0281),
    "Bismarck, North Dakota":                   (46.8083, -100.7837),
    "Liverpool, England, United Kingdom":       (53.4084,   -2.9916),
    "Queenstown, South Island, New Zealand":    (-45.0302, 168.6626),
    "Laporte, Pennsylvania":                    (41.4248,  -76.4971),
    "Omaha, Nebraska":                          (41.2565,  -95.9345),
    "Smithfield, North Carolina":               (35.5093,  -78.3361),
    "Timaru, Canterbury, New Zealand":          (-44.3960, 171.2553),
    "Algona, Iowa":                             (43.0694,  -94.2350),
    "Barcaldine, Queensland, Australia":        (-23.5531, 145.2892),
    "Wichita, Kansas":                          (37.6872,  -97.3301),
    # Map 3 new locations
    "Corsicana, Texas":                         (32.0957,  -96.4689),
    "Cortland, New York":                       (42.6006,  -76.1797),
    "Hamburg, New York":                        (42.7164,  -78.8301),
    "Galena, Kansas":                           (37.0717,  -94.6388),
    "Geneva, New York":                         (42.8687,  -76.9777),
    "Follett, Texas":                           (36.4337, -100.1376),
    "Mount Carmel, Pennsylvania":               (40.7951,  -76.4135),
    "Skaneateles, New York":                    (42.9471,  -76.4293),
    "Graham, North Carolina":                   (36.0766,  -79.4036),
    "Beloit, Kansas":                           (39.4681,  -98.1112),
    "Bemidji, Minnesota":                       (47.4736,  -94.8811),
    "Chanute, Kansas":                          (37.6792,  -95.4571),
    "McKinney, Texas":                          (33.1972,  -96.6397),
    "East Hampton, New York":                   (40.9632,  -72.1851),
    "Port Jervis, New York":                    (41.3748,  -74.6927),
    "North Tonawanda, New York":                (43.0342,  -78.8645),
    "Fayetteville, New York":                   (43.0275,  -76.0041),
    "Oswego, New York":                         (43.4553,  -76.5105),
    "Las Cruces, New Mexico":                   (32.3199, -106.7637),
    "Sayville, New York":                       (40.7418,  -73.0849),
    "Friendship, New York":                     (42.2014,  -78.1397),
    "Clyde, New York":                          (43.0842,  -76.8694),
    "Ottawa, Ontario, Canada":                  (45.4215,  -75.6919),
    "Littleton, North Carolina":                (36.4274,  -77.9119),
    "Lake Providence, Louisiana":               (32.8065,  -91.1719),
    "Corning, Iowa":                            (40.9886,  -94.7363),
    "Baltimore, Maryland":                      (39.2904,  -76.6122),
    "Brooklyn, New York":                       (40.6782,  -73.9442),
    "Brownsville, Texas":                       (25.9017,  -97.4975),
    "Salem, Oregon":                            (44.9429, -123.0351),
    "Kansas City, Missouri":                    (39.0997,  -94.5786),
    "Nemaha, Nebraska":                         (40.3408,  -95.6794),
    "Pittsboro, North Carolina":                (35.7190,  -79.1785),
    "Fort Wayne, Indiana":                      (41.0793,  -85.1394),
    "Indiana, Pennsylvania":                    (40.6215,  -79.1528),
    "St. Louis, Missouri":                      (38.6270,  -90.1994),
    "Salt Lake City, Utah":                     (40.7608, -111.8910),
    "Topeka, Kansas":                           (39.0489,  -95.6780),
    "Alexandria, Indiana":                      (40.2631,  -85.6786),
    "Canonsburg, Pennsylvania":                 (40.2630,  -80.1864),
    "Sydney, New South Wales, Australia":       (-33.8688, 151.2093),
}

# ── Nominatim fallback ───────────────────────────────────────────────────────
def geocode_fallback(location_str):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="lonewoman_map_gen/1.0")
    try:
        loc = geolocator.geocode(location_str, timeout=10)
        time.sleep(1.1)
        if loc:
            print(f"  Geocoded: {location_str} → ({loc.latitude:.4f}, {loc.longitude:.4f})")
            return (loc.latitude, loc.longitude)
    except Exception as e:
        print(f"  Geocode failed: {location_str}: {e}")
    return None

def get_coords(location_str):
    if location_str in COORD_CACHE:
        return COORD_CACHE[location_str]
    # Try Nominatim
    coords = geocode_fallback(location_str)
    if coords:
        COORD_CACHE[location_str] = coords
        return coords
    # Jitter to avoid overlap for unknown
    print(f"  WARNING: could not geocode '{location_str}', using fallback")
    return (0.0, 0.0)

# ── CSV loading ──────────────────────────────────────────────────────────────
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "_data",
                        "cb_complete_metadata_images_tropes_reprints_transcripts.csv")

def load_articles(groups):
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return [r for r in rows
            if r['display_template'] == 'compound_object'
            and r['group_reprint_id'] in groups]

# ── Reprint-type → line style ─────────────────────────────────────────────
def line_style(rtype):
    if 'direct' in rtype:
        return 'solid'
    elif 'truncated' in rtype:
        return 'dash'
    else:  # paraphrase, etc.
        return 'dot'

# ── 8-band colour scheme ─────────────────────────────────────────────────────
BAND_STARTS = [1825, 1850, 1875, 1900, 1925, 1950, 1975, 2000]

def get_color_value(year):
    for b, start in enumerate(BAND_STARTS):
        if start <= year < start + 25:
            return (b + 1) + (year - start) / 25.0
    return 1.0 if year < 1825 else 9.0

NEW_COLORSCALE = [
    [0.0000, "rgb(198,219,239)"],
    [0.1249, "rgb(8,48,107)"],
    [0.1250, "rgb(199,233,192)"],
    [0.2499, "rgb(0,68,27)"],
    [0.2500, "rgb(253,208,162)"],
    [0.3749, "rgb(166,54,3)"],
    [0.3750, "rgb(252,174,145)"],
    [0.4999, "rgb(103,0,13)"],
    [0.5000, "rgb(218,218,235)"],
    [0.6249, "rgb(63,0,125)"],
    [0.6250, "rgb(178,226,226)"],
    [0.7499, "rgb(0,88,88)"],
    [0.7500, "rgb(255,247,188)"],
    [0.8749, "rgb(179,88,6)"],
    [0.8750, "rgb(253,205,228)"],
    [1.0000, "rgb(197,27,125)"],
]

BAND_LABELS = ["1825–1849","1850–1874","1875–1899","1900–1924",
               "1925–1949","1950–1974","1975–1999","2000–2024"]
TICK_VALS   = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]

# ── Build Plotly traces ──────────────────────────────────────────────────────
def build_traces(articles):
    """Return (traces, article_to_group, group_to_articles, edge_mapping, article_years, article_tropes)"""
    import plotly.graph_objects as go

    # Find originals per group
    originals = {}
    for art in articles:
        if 'original' in art['reprint_type']:
            originals[art['group_reprint_id']] = art

    # Group membership
    group_to_articles = {}
    article_to_group  = {}
    for art in articles:
        gid = art['group_reprint_id']
        aid = art['article_id']
        group_to_articles.setdefault(gid, []).append(aid)
        article_to_group[aid] = gid

    # Article years and tropes
    article_years  = {}
    article_tropes = {}
    for art in articles:
        aid = art['article_id']
        year = int(art['date'][:4]) if art['date'] else 1900
        article_years[aid] = year
        tropes_raw = art.get('tropes', '')
        article_tropes[aid] = tropes_raw.replace('; ', ', ').replace(';', ', ')

    import math

    # Coordinates
    coords = {}
    for art in articles:
        loc = art['publisher_location']
        if loc not in coords:
            coords[loc] = get_coords(loc)

    # ── Per-article spread coordinates ──────────────────────────────────────
    # Group all article IDs (originals + reprints) by location, then assign
    # small circular offsets so overlapping nodes are distinct.
    loc_to_aids = {}
    for art in articles:
        loc = art['publisher_location']
        loc_to_aids.setdefault(loc, []).append(art['article_id'])

    SPREAD_RADIUS = 0.55   # degrees – big enough to separate, small enough to look local
    SPREAD_SCALE  = 1.25   # grow radius a bit more when there are many nodes

    article_spread = {}
    for loc, aids in loc_to_aids.items():
        n = len(aids)
        base_lat, base_lon = coords.get(loc, (0, 0))
        if n == 1:
            article_spread[aids[0]] = (base_lat, base_lon)
        else:
            # Scale radius with sqrt(n) so larger clusters spread more
            r = SPREAD_RADIUS * (1 + SPREAD_SCALE * math.log(n) / 4)
            for i, aid in enumerate(aids):
                angle = 2 * math.pi * i / n - math.pi / 2  # start at top
                dlat = r * math.sin(angle)
                # longitude degrees are smaller near the poles – correct for that
                cos_lat = math.cos(math.radians(base_lat)) or 0.01
                dlon = r * math.cos(angle) / cos_lat
                article_spread[aid] = (base_lat + dlat, base_lon + dlon)

    # Build edge traces (one per edge)
    traces = []
    edge_mapping = []
    edge_idx = 0
    for art in articles:
        if 'original' in art['reprint_type']:
            continue
        gid = art['group_reprint_id']
        orig = originals.get(gid)
        if not orig:
            continue
        olat, olon = article_spread.get(orig['article_id'], coords.get(orig['publisher_location'], (0, 0)))
        rlat, rlon = article_spread.get(art['article_id'],  coords.get(art['publisher_location'],  (0, 0)))
        traces.append(go.Scattergeo(
            lat=[olat, rlat],
            lon=[olon, rlon],
            mode='lines',
            line=dict(color='rgba(100, 100, 100, 0.4)', width=2, dash=line_style(art['reprint_type'])),
            hoverinfo='skip',
            showlegend=False,
        ))
        edge_mapping.append({'index': edge_idx, 'source': orig['article_id'],
                             'target': art['article_id'], 'group': gid})
        edge_idx += 1

    num_edge_traces = len(traces)

    # Originals marker trace
    orig_lats, orig_lons, orig_cdata, orig_htext, orig_text = [], [], [], [], []
    for gid, orig in sorted(originals.items()):
        loc = orig['publisher_location']
        aid = orig['article_id']
        lat, lon = article_spread.get(aid, coords.get(loc, (0, 0)))
        orig_lats.append(lat)
        orig_lons.append(lon)
        orig_cdata.append(aid)
        year = article_years.get(aid, 1900)
        title_short = orig['title'][:60] + '...' if len(orig['title']) > 60 else orig['title']
        tropes = article_tropes.get(aid, '')
        tropes_str = f'<br>Tropes: {tropes}' if tropes else ''
        orig_htext.append(
            f'<b>{title_short}</b><br>'
            f'Publication: {orig["publication"]}<br>'
            f'Location: {loc}<br>'
            f'Date: {orig["date"]}<br>'
            f'Type: {orig["reprint_type"]}'
            f'{tropes_str}<br>'
            f'Group: {gid}'
        )
        orig_text.append(f'{title_short[:30]}...<br>{orig["publication"][:20]}')

    orig_colors = [get_color_value(article_years.get(aid, 1900)) for aid in orig_cdata]
    traces.append(go.Scattergeo(
        lat=orig_lats, lon=orig_lons,
        mode='markers+text',
        name='Original',
        customdata=orig_cdata,
        hoverinfo='text',
        hovertext=orig_htext,
        text=orig_text,
        textposition='top center',
        textfont=dict(size=10, color='black', family='Arial Black'),
        marker=dict(
            size=20, symbol='star',
            color=orig_colors,
            colorscale=NEW_COLORSCALE,
            cmin=1, cmax=9,
            colorbar=dict(
                ticktext=BAND_LABELS, tickvals=TICK_VALS,
                title=dict(text='25-Year Period')
            ),
            line=dict(color='black', width=3),
        ),
    ))

    # Reprints marker trace
    rep_lats, rep_lons, rep_cdata, rep_htext, rep_text = [], [], [], [], []
    for art in articles:
        if 'original' in art['reprint_type']:
            continue
        loc = art['publisher_location']
        aid = art['article_id']
        lat, lon = article_spread.get(aid, coords.get(loc, (0, 0)))
        rep_lats.append(lat)
        rep_lons.append(lon)
        rep_cdata.append(aid)
        year = article_years.get(aid, 1900)
        title_short = art['title'][:60] + '...' if len(art['title']) > 60 else art['title']
        tropes = article_tropes.get(aid, '')
        tropes_str = f'<br>Tropes: {tropes}' if tropes else ''
        gid = art['group_reprint_id']
        rep_htext.append(
            f'<b>{title_short}</b><br>'
            f'Publication: {art["publication"]}<br>'
            f'Location: {loc}<br>'
            f'Date: {art["date"]}<br>'
            f'Type: {art["reprint_type"]}'
            f'{tropes_str}<br>'
            f'Group: {gid}'
        )
        rep_text.append(f'{title_short[:30]}...<br>{art["publication"][:20]}')

    rep_colors = [get_color_value(article_years.get(aid, 1900)) for aid in rep_cdata]
    traces.append(go.Scattergeo(
        lat=rep_lats, lon=rep_lons,
        mode='markers+text',
        name='Reprints',
        customdata=rep_cdata,
        hoverinfo='text',
        hovertext=rep_htext,
        text=rep_text,
        textposition='top center',
        textfont=dict(size=9, color='black'),
        marker=dict(
            size=12, symbol='circle',
            color=rep_colors,
            colorscale=NEW_COLORSCALE,
            cmin=1, cmax=9,
            showscale=False,
            line=dict(color='white', width=2),
        ),
    ))

    return (traces, num_edge_traces, article_to_group, group_to_articles,
            edge_mapping, article_years, article_tropes)


# ── JS injection block ───────────────────────────────────────────────────────
def build_js_block(num_edge_traces, article_to_group, group_to_articles,
                   edge_mapping, article_years, article_tropes):
    return f"""
<script>
(function() {{
    'use strict';

    var articleToGroup = {json.dumps(article_to_group)};
    var groupToArticles = {json.dumps(group_to_articles)};
    var edgeMapping = {json.dumps(edge_mapping)};
    var numEdgeTraces = {num_edge_traces};
    var currentlyHighlighted = null;
    var myPlot = null;
    var originalEdgeStyles = [];

    function findPlotElement() {{
        return document.querySelector('.js-plotly-plot') ||
               document.querySelector('.plotly-graph-div');
    }}

    function initClickHandler() {{
        myPlot = findPlotElement();
        if (!myPlot) {{ setTimeout(initClickHandler, 500); return; }}
        if (!myPlot.data || !myPlot._fullLayout) {{ setTimeout(initClickHandler, 500); return; }}

        for (var i = 0; i < numEdgeTraces; i++) {{
            var trace = myPlot.data[i];
            if (trace.line) {{
                originalEdgeStyles.push({{
                    color: trace.line.color, width: trace.line.width, dash: trace.line.dash
                }});
            }}
        }}

        myPlot.on('plotly_click', handleClick);
        myPlot.on('plotly_doubleclick', function() {{ resetView(); }});

        myPlot.on('plotly_legendclick', function(eventData) {{
            var clicked = eventData.curveNumber;
            for (var i = numEdgeTraces; i < myPlot.data.length; i++) {{
                if (i !== clicked && myPlot.data[i].customdata) {{
                    var cur = myPlot.data[i].visible;
                    Plotly.restyle(myPlot, {{'visible': cur === false ? true : false}}, [i]);
                }}
            }}
            return false;
        }});

        myPlot.on('plotly_legenddoubleclick', function() {{
            for (var i = numEdgeTraces; i < myPlot.data.length; i++) {{
                if (myPlot.data[i].customdata) {{
                    Plotly.restyle(myPlot, {{'visible': true}}, [i]);
                }}
            }}
            return false;
        }});

        Plotly.relayout(myPlot, {{
            'autosize': true,
            'width': null,
            'legend.x': 0.01,
            'legend.y': 0.98,
            'legend.xanchor': 'left',
            'legend.yanchor': 'top',
            'legend.bgcolor': 'rgba(255,255,255,0.88)',
            'legend.bordercolor': '#bbb',
            'legend.borderwidth': 1,
            'legend.font': {{size: 13}}
        }});
    }}

    function handleClick(eventData) {{
        var point = eventData.points[0];
        var clickedArticleId = point.customdata;
        if (!clickedArticleId) return;

        var reprintGroup = articleToGroup[clickedArticleId];
        if (!reprintGroup) return;

        if (currentlyHighlighted === reprintGroup) {{ resetView(); return; }}
        currentlyHighlighted = reprintGroup;
        var articlesInGroup = groupToArticles[reprintGroup];

        for (var i = 0; i < numEdgeTraces; i++) {{
            var inGroup = false;
            for (var j = 0; j < edgeMapping.length; j++) {{
                if (edgeMapping[j].index === i && edgeMapping[j].group === reprintGroup) {{
                    inGroup = true; break;
                }}
            }}
            if (inGroup) {{
                Plotly.restyle(myPlot, {{'line.color': 'rgba(255, 100, 0, 0.9)', 'line.width': 4}}, [i]);
            }} else {{
                Plotly.restyle(myPlot, {{'line.color': 'rgba(200, 200, 200, 0.08)', 'line.width': 0.5}}, [i]);
            }}
        }}

        for (var i = numEdgeTraces; i < myPlot.data.length; i++) {{
            var trace = myPlot.data[i];
            if (!trace.customdata) continue;
            var opacities = [], sizes = [], blacks = [];
            var baseSize = (trace.name === 'Original') ? 20 : 12;
            for (var j = 0; j < trace.customdata.length; j++) {{
                var aid = trace.customdata[j];
                var inG = articlesInGroup.indexOf(aid) !== -1;
                opacities.push(inG ? 1.0 : 0.12);
                sizes.push(inG ? baseSize * 1.4 : baseSize * 0.6);
                blacks.push(inG ? 'black' : 'rgba(0,0,0,0.08)');
            }}
            Plotly.restyle(myPlot, {{
                'marker.opacity': [opacities],
                'marker.size': [sizes],
                'textfont.color': [blacks]
            }}, [i]);
        }}

        showInfoBox(reprintGroup, articlesInGroup.length);
    }}

    function resetView() {{
        currentlyHighlighted = null;
        for (var i = 0; i < numEdgeTraces; i++) {{
            if (originalEdgeStyles[i]) {{
                Plotly.restyle(myPlot, {{
                    'line.color': originalEdgeStyles[i].color,
                    'line.width': originalEdgeStyles[i].width
                }}, [i]);
            }}
        }}
        for (var i = numEdgeTraces; i < myPlot.data.length; i++) {{
            var trace = myPlot.data[i];
            if (!trace.customdata) continue;
            var baseSize = (trace.name === 'Original') ? 20 : 12;
            var ones = [], sizes = [], blacks = [];
            for (var j = 0; j < trace.customdata.length; j++) {{
                ones.push(1.0); sizes.push(baseSize); blacks.push('black');
            }}
            Plotly.restyle(myPlot, {{'marker.opacity': [ones], 'marker.size': [sizes], 'textfont.color': [blacks]}}, [i]);
        }}
        var infoDiv = document.getElementById('group-info');
        if (infoDiv) infoDiv.remove();
    }}

    function showInfoBox(groupName, numArticles) {{
        var infoDiv = document.getElementById('group-info');
        if (!infoDiv) {{
            infoDiv = document.createElement('div');
            infoDiv.id = 'group-info';
            infoDiv.style.cssText = 'position:fixed;top:120px;right:30px;background:rgba(255,255,255,0.95);border:3px solid #ff6600;border-radius:10px;padding:20px;z-index:10000;font-family:Arial,sans-serif;box-shadow:0 6px 12px rgba(0,0,0,0.3);min-width:250px;';
            document.body.appendChild(infoDiv);
        }}
        var plural = numArticles > 1 ? 's' : '';
        infoDiv.innerHTML = '<div style="font-size:16px;font-weight:bold;color:#ff6600;margin-bottom:10px;">Highlighted Group</div>' +
            '<div style="font-size:14px;margin-bottom:5px;"><strong>' + groupName + '</strong></div>' +
            '<div style="font-size:13px;color:#666;margin-bottom:15px;">' + numArticles + ' article' + plural + ' in this lineage</div>' +
            '<div style="font-size:11px;color:#999;font-style:italic;border-top:1px solid #ddd;padding-top:10px;">Click another node to switch groups<br>Double-click map to reset view</div>';
    }}

    if (document.readyState === 'complete') {{
        setTimeout(initClickHandler, 300);
    }} else {{
        window.addEventListener('load', function() {{ setTimeout(initClickHandler, 300); }});
    }}
}})();
</script>
"""


# ── Generate one map HTML ─────────────────────────────────────────────────────
def generate_map(map_title, nav_title, groups, output_filename):
    import plotly.graph_objects as go

    print(f"\n=== Generating {output_filename} ===")
    articles = load_articles(groups)
    print(f"  Loaded {len(articles)} articles across groups: {groups}")

    (traces, num_edge_traces, article_to_group, group_to_articles,
     edge_mapping, article_years, article_tropes) = build_traces(articles)

    print(f"  Built {num_edge_traces} edge traces + 2 marker traces")

    subtitle = ("Node color = 25-year period (lighter → earlier, darker → later) | "
                "⭐=Original, ⚫=Reprint | Lines: solid=direct, dashed=truncated, dotted=paraphrase")

    fig = go.Figure(data=traces, layout=go.Layout(
        title=dict(
            text=f"{map_title}<br><sub>{subtitle}</sub>",
            x=0.5, xanchor='center'
        ),
        geo=dict(
            projection=dict(type='mercator'),
            lataxis=dict(range=[-60, 75]),
            lonaxis=dict(range=[-180, 180]),
            showland=True,
            landcolor='rgb(243, 243, 243)',
            coastlinecolor='rgb(204, 204, 204)',
            showlakes=True,
            lakecolor='rgb(230, 245, 255)',
            showcountries=True,
            countrycolor='rgb(204, 204, 204)',
            showocean=True,
            oceancolor='rgb(230, 245, 255)',
        ),
        margin=dict(l=0, r=0, t=80, b=0),
        height=900,
        legend=dict(x=0.01, y=0.98, xanchor='left', yanchor='top',
                    bgcolor='rgba(255,255,255,0.88)',
                    bordercolor='#bbb', borderwidth=1,
                    font=dict(size=13)),
    ))

    html_str = fig.to_html(
        full_html=True,
        include_plotlyjs='cdn',
        config={'responsive': True},
    )

    js_block = build_js_block(
        num_edge_traces, article_to_group, group_to_articles,
        edge_mapping, article_years, article_tropes
    )

    # Inject JS before </body>
    html_str = html_str.replace('</body>', js_block + '\n</body>')

    out_path = os.path.join(os.path.dirname(__file__), output_filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_str)
    print(f"  Saved: {out_path}")


# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    generate_map(
        map_title="Reprint Network: Boston Atlas (1847), Newburyport Daily Herald (1853), Hutchings' California Illustrated Magazine (1856)",
        nav_title="Map of Reprint Network Examples 1840–1875",
        groups=['TheBostonAtlas1847_reprint', 'TheDailyHerald1853_reprint', 'Russell1856_HCF_reprint'],
        output_filename='map1_1840_1875.html',
    )

    generate_map(
        map_title="Reprint Network: Winona Daily Republican (1878), San Francisco Examiner (1892), New York Herald (1896)",
        nav_title="Map of Reprint Network 1875–1900",
        groups=['Stuart1878_reprint', 'SanFranciscoExaminer1892_reprint', 'NewYorkHerald1896_reprint'],
        output_filename='map2_1875_1900.html',
    )

    generate_map(
        map_title="Reprint Network: Los Angeles Saturday Post (1901), New York Field and Stream (1905), Corsicana Daily Sun (1921)",
        nav_title="Map of Reprint Network 1900–1925",
        groups=['FHDudley1901_reprint', 'Gassaway1905_reprint', 'CorsicanaDailySun1921_reprint'],
        output_filename='map3_1900_1925.html',
    )

    print("\nAll maps generated successfully.")
