# Tropes Page: Visualizations and Data

The Tropes page (`/subjects.html`) shows two D3-based charts that let readers explore how the 14 interpretive tropes are distributed across the archive's articles and across time. All data is baked into the page at Jekyll build time — no API calls or server-side requests at runtime, except for loading the D3 library from CDN.

**URL:** `/subjects.html`  
**Page file:** `pages/subjects.md`

---

## Data Sources

| File | Role |
|---|---|
| `_data/article_ids_only.csv` | One row per unique article (481 rows). Provides the `date`, `tropes`, and `publisher_location` fields used by both charts. |
| `_data/tropes.yml` | Ordered list of trope definitions: `id`, `label`, `color` (hex). Drives trope order, labels, and bar/sparkline colors. |

**Key columns used from `article_ids_only.csv`:**
- `date` — `YYYY-MM-DD`; year is sliced from the first 4 characters
- `tropes` — semicolon-separated trope labels (e.g. `Noble Savage; Discovery; Wonder`); articles with no tropes are excluded from the charts
- `publisher_location` — free-text string (e.g. `Albany, New York`); used by the regional bar chart logic (currently commented out)

**Tropes defined in `tropes.yml`:** 15 total. The "Captivity" trope (id 2) is excluded from both visualizations by an `unless trope.label == "Captivity"` guard, leaving **14 tropes** shown in the charts. There was no source data associated with the "Captivity" trope. 

---

## D3 Loading

`pages/subjects.md` injects a small inline script that defines a shared D3 loader:

```js
window._d3q = [];
window._whenD3 = function(fn) { ... };
```

D3 v7 is fetched once from CDN (`cdn.jsdelivr.net/npm/d3@7.9.0`). Both includes register their init functions via `_whenD3(fn)`, so the library loads only once regardless of include order.

---

## Sparklines (`_includes/trope-sparklines.html`)

A 2-column grid of filled area charts — one "Total Articles Published Across Time" overview, then one per trope (14 cards), for 15 cards total.

**Build-time (Liquid → JS):**  
Jekyll iterates `article_ids_only.csv` and bakes three JS arrays directly into the `<script>` block:

- `TROPES` — `[{ id, label, color }, ...]` from `tropes.yml`
- `ALL_YRS` — flat array of years (one integer per article) for the overview chart
- `RAW` — `[{ y: year, t: "trope label" }, ...]`, one entry per article-trope pair

**Runtime (D3):**  
1. Counts are aggregated: `tropeCounts[label][year]` and `allYmap[year]`
2. Year extent (min/max) is derived from `ALL_YRS` and shared across all sparklines so x-axes align
3. Each card renders a D3 area + line path with `d3.curveMonotoneX` smoothing
4. X-axis tick values are fixed: first year, 1900, 1950, last year
5. Hovering a card dims all other cards to 20% opacity
6. A tooltip (fixed-position `div`) shows `year — N articles` on mousemove

**SVG geometry:** 240 × 96 viewBox, left margin 28px for y-axis label, bottom margin 20px for x-axis.

---

## Bar Charts (`_includes/trope-barcharts.html`)

A single vertical bar chart showing total article count per trope across the full archive.

**Build-time (Liquid → JS):**  
Jekyll bakes two arrays into the script:

- `TROPES` — same as sparklines
- `ARTICLES` — `[{ loc: "publisher_location", tr: "tropes string" }, ...]` for articles that have at least one trope

**Runtime (D3):**  
1. Each article's `tr` string is split on `;` and trimmed; each trope label increments `overall[label]`
2. A D3 `scaleBand` places one bar per trope; a `scaleLinear` maps count to bar height
3. Bars are colored by `trope.color` from `tropes.yml`; bars with count 0 render at 15% opacity
4. X-axis labels are rotated −42° to fit; y-axis has 4 horizontal grid lines
5. Hovering a bar shows a tooltip: `Trope Label — N articles`

**Regional charts:** The code contains a full regional classifier and per-region count aggregation, but the regional grid (`<div id="bc-regional-grid">`) and the chart drawing calls are commented out. The classifier assigns articles to seven regions — US East Coast, US Midwest & South, US West Coast, Canada, Europe, Asia, Australia & New Zealand — using `publisher_location` string matching. This could be re-enabled by uncommenting the relevant blocks in `trope-barcharts.html`.

---

## File Summary

| File | Role |
|---|---|
| `pages/subjects.md` | Page front matter, D3 CDN loader, includes both chart includes |
| `_includes/trope-sparklines.html` | Sparkline grid: overview + one per trope, article frequency over time |
| `_includes/trope-barcharts.html` | Bar chart: total article count per trope (regional charts built but commented out) |
| `_data/tropes.yml` | Trope id, label, color — drives order and styling in both charts |
| `_data/article_ids_only.csv` | One row per article; `date` and `tropes` columns are the primary inputs |
