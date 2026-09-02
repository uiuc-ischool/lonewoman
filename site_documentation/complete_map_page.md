# Complete Map Page: All Articles by Place of Publication

The Complete Map page (`/map.html`) plots every article in the collection on a single world map, positioned by its place of publication. Unlike the [Document Groups](document_groups_page.md) reprint maps, which are scoped to one reprint family at a time and drawn on demand, this page loads all ~480 articles at once and reveals them over time with a play/slider control, clustering nearby points so dense cities (New York, Boston, San Francisco, etc.) don't overlap into an unreadable mess. Clicking a city cluster circle holds its article table open on screen, so its title/publisher/date metadata can be read and scrolled through at leisure instead of disappearing the moment the cursor moves.

**URL:** `/map.html`
**Page file:** `pages/map.md`

---

## What It Shows

- A full-page dark basemap with every geocoded article plotted as a dot at its `publisher_location`
- Nearby articles are merged into a single circle, sized by how many articles it contains — the more articles published in one place, the bigger the circle
- A play/pause button and time scrubber reveal articles in chronological order by `date`, plus a speed slider (0.2×–4×)
- **Hovering** a single-article dot shows its title/publisher/date; hovering a cluster shows a lightweight "N articles — click to view list" prompt
- **Clicking** any dot pins a detail panel in place (with a close button), so a cluster's full article list can actually be scrolled — see [Interaction model](#interaction-model-hover-vs-click-to-pin) below for why hover alone doesn't work for this

---

## Data Sources

| File | Role |
|---|---|
| `_data/article_map_locations.csv` | Provides geocoded `lat`/`lng` per article, keyed by `article_id` |
| `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv` | Master metadata — provides the canonical `title`, `publication`, `date`, and `publisher_location` shown in tooltips |
| `_data/geocode_cache.json` | Nominatim geocoding cache used by `metadata_notebooks/prepare_article_map_locations.py` to build `article_map_locations.csv` |

**Why two files for one dot:** `article_map_locations.csv` is a derived/cached file, regenerated only when someone reruns `prepare_article_map_locations.py` — it can drift out of sync with the master metadata if that sheet is edited afterward. To avoid displaying stale text next to correct coordinates (or vice versa), `_includes/all-articles-map-data.html` only pulls `lat`/`lng` from `article_map_locations.csv` and joins back to the master metadata by `article_id` for everything else the tooltip shows. This is also how a data-drift bug was caught and fixed directly: `NewhampshireSentinel1885` had a blank `article_map_locations.csv` row (title/publication/date/location all empty) even though the master sheet had a correct `publisher_location: Keene, New Hampshire` — the join by `article_id` is what makes that kind of staleness detectable and easy to patch by hand rather than requiring a full geocoder rerun.

**Coverage:** 494 rows in `article_map_locations.csv` → 481 unique articles → 474 with usable coordinates. The 7 missing are manuscripts/journal entries with no real "place of publication" to geocode (expected). Two were data gaps that got manually fixed directly in `article_map_locations.csv` and `geocode_cache.json`: `NewhampshireSentinel1885` (location was simply missing from the derived CSV) and `Pioneer1988` (location is `"Moscow, Russia, USSR"`, which Nominatim can't geocode since "USSR" isn't a country it recognizes — see the comment in `prepare_article_map_locations.py`).

---

## Page Structure (`pages/map.md`)

**Front matter:**
```yaml
layout: page
permalink: /map.html
use_all_articles_map: true
```

`use_all_articles_map: true` tells `_layouts/default.html` to load MapLibre GL, deck.gl, and `assets/js/all-articles-map.js`. It's a separate flag from `use_reprint_maps` (used by `pages/document-groups.md`) so the two pages' scripts stay independent — this page doesn't load `reprint-map.js`, and the Document Groups page doesn't load `all-articles-map.js`. If both flags happen to be set on the same page, `_layouts/default.html` still only loads the shared MapLibre/deck.gl CDN scripts once.

**Body:** just an intro paragraph plus one include:
```liquid
{% include all-articles-map-data.html %}
```

---

## Data Baking: `_includes/all-articles-map-data.html`

At build time this include:
1. Filters the master metadata to `display_template == "compound_object"` rows (one per article)
2. Filters `article_map_locations.csv` to rows with non-blank `lat`/`lng`, then groups by `article_id` (`group_by`) and takes the first row per group — this is the dedup step, since 13 articles appear more than once in that CSV as part of multiple reprint groups
3. For each unique geocoded `article_id`, looks up the matching `compound_object` row by `article_id` and pulls `title`/`publication`/`date`/`publisher_location` from there
4. Bakes the result into a plain JS array on `window._allArticlesMapData`

```js
window._allArticlesMapData = [
  { title: "...", publication: "...", date: "1885-06-10",
    publisher_location: "Keene, New Hampshire", lat: 42.93, lng: -72.28 },
  ...
];
```

Unlike the per-group reprint maps, there's only one map on this page, so the data isn't keyed/registered by container ID — it's read directly by `assets/js/all-articles-map.js` on `DOMContentLoaded`.

---

## The `AllArticlesMap` Widget (`assets/js/all-articles-map.js`)

Forked from `reprint-map.js`'s dark MapLibre + deck.gl foundation (same visual language: dark CartoDB basemap, indigo accent, bottom controls bar with play/pause/reset/scrubber/speed), but adapted for one big collection-wide view instead of many small per-group ones.

**What's different from `ReprintMap`:**
- No `ArcLayer` / origin coordinates — this page shows *where* articles were published, not reprint text movement, so it's a single `ScatterplotLayer` only
- Points are **clustered** (`ReprintMap` only "splays" exact duplicate coordinates apart; it never merges nearby-but-distinct ones)
- Not lazy-initialized behind a `<details>` toggle — it's the only thing on the page, so it initializes on `DOMContentLoaded`

### Clustering

`clusterPoints(points, zoom)` does a greedy single-link grouping: for each unvisited point, it collects every other unvisited point within `CLUSTER_PX = 30` screen pixels (converted to meters at the current latitude/zoom) and merges them into one cluster centered on their centroid. This runs fresh on every `render()` call — i.e. on every animation tick and every zoom change — so clusters grow as more articles appear over the timeline and re-split as the user zooms in. At collection scale (~480 points) this is cheap enough to redo every frame; it isn't a real clustering library (no Supercluster/quadtree), so it would need one if the collection grew much larger.

Circle radius scales with `Math.sqrt(cluster.items.length)`, clamped between `radiusMinPixels: 6` and `radiusMaxPixels: 46`.

### Interaction model: hover vs. click-to-pin

Hovering a cluster originally showed the same kind of scrollable table used for click, but that didn't work: the tooltip renders offset from the cursor, so reaching it means crossing a strip of empty canvas first — and deck.gl's `onHover` fires with `info.object == null` the instant the cursor leaves the dot, closing the tooltip before it can be reached. The fix, matching how most mapping libraries solve this:

- **Hover** (`handleHover`) is ephemeral and non-interactive (`pointer-events: none`): full detail for a single article, or just a `"N articles — click to view list"` prompt for a cluster.
- **Click** (`handleClick`) "pins" the tooltip: it stops following the mouse, gets `pointer-events: auto` and a `×` close button, and only closes when the user clicks it, clicks a different dot, or the underlying view changes (`closePinned()` is called from `play()`, `reset()`, the time-slider drag handler, and `map.on('zoom', ...)`, since a pinned cluster's membership can go stale once time or zoom changes). This also means single-article detail is now reachable by click too, which incidentally makes the map usable on touch devices that have no hover state at all.

### Cluster table layout

The pinned table uses a fixed `<colgroup>` (title 150px / publication 100px / date 90px) with `table-layout: fixed` and single-line ellipsis truncation on the title and publication cells. This was a deliberate fix for a real bug: with `table-layout: auto` and no column constraints, a long publication name (e.g. dense NYC/Boston/SF clusters) could push the date column past the tooltip's edge, where the container's `overflow: hidden` silently clipped it — so the year looked "missing" even though the data was correct. Fixed column widths guarantee the date column is always visible regardless of how long the other text is.

### Edge case guards (inherited from `ReprintMap`'s pattern)

- No geocoded data → shows a "No location data available" message instead of a blank map
- All points at one location → skips `fitBounds`, centers on that point at zoom 6 instead
- All points share one date → hides the controls bar; everything appears at once

---

## Styling

`.all-articles-map-container` in `_sass/_custom.scss` sets the container to `75vh` (capped between 480px and 780px, shrinking to `65vh`/380px on mobile) — taller than the Document Groups page's per-group `.reprint-map-container` (fixed 480px/300px), since this is the whole point of the page rather than one collapsible section among several.

---

## Navigation

`/map.html` is a flat top-level "Complete Map" link in the toolbar (`_data/config-nav.csv`) — there is no longer a "Map" dropdown. The dropdown previously also held three standalone "Map of Example Reprint Networks" pages (`pages/reprint-network.md`, `-2.md`, `-3.md`, each an iframe wrapper around a static file in `map_features/`); those were removed from the nav and disabled with `published: false` in their front matter rather than deleted, so they're fully intact and can be re-enabled (delete that one line, add their rows back to `config-nav.csv`) if needed later.

---

## Files NOT Used by This Page

`_layouts/map.html`, `_includes/js/map-js.html`, and `_data/config-map.csv` — the stock CollectionBuilder Leaflet-based map this page replaced — have been deleted from the repo entirely (not just disabled), since nothing else referenced them.

---

## File Summary

| File | Role |
|---|---|
| `pages/map.md` | Page file; sets `use_all_articles_map: true`; includes the data-baking include |
| `_includes/all-articles-map-data.html` | Jekyll include; dedups + joins `article_map_locations.csv` to master metadata; bakes `window._allArticlesMapData` |
| `assets/js/all-articles-map.js` | Defines `AllArticlesMap` (MapLibre + deck.gl); clustering, animation, hover/click-to-pin tooltips |
| `_layouts/default.html` | Loads MapLibre, deck.gl, and `all-articles-map.js` when `use_all_articles_map` is set |
| `_sass/_custom.scss` | `.all-articles-map-container` sizing |
| `_data/config-nav.csv` | "Complete Map" toolbar entry |
| `_data/article_map_locations.csv` | 494-row geocoded article dataset; source of `lat`/`lng` |
| `_data/geocode_cache.json` | Nominatim geocode cache backing `article_map_locations.csv` |
| `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv` | Master metadata; source of title/publication/date/location text |
| `metadata_notebooks/prepare_article_map_locations.py` | Script that (re)builds `article_map_locations.csv` from master metadata + Nominatim geocoding |
