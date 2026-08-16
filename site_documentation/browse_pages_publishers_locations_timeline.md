# Browse Pages: Publishers, Locations, and Timeline

These three pages appear in the site toolbar and give readers different ways to browse the full set of articles. All three read directly from the master metadata CSV at build time via Jekyll Liquid — no JavaScript or client-side fetching is involved. Each page filters to `compound_object` rows only (one row per article; image child rows are excluded).

**Data source for all three:** `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`

---

## Browse (`pages/browse.md`)

**URL:** `/browse.html`

Unlike Publishers, Locations, and Timeline below — which render entirely server-side via Liquid — the Browse page is built from client-side JS app: Jekyll only emits a JSON array of every article into the page, and `_includes/js/browse-js.html` handles filtering, faceting, sorting, and card rendering in the browser after load.

**What it shows:**
- A search/filter bar: field-select dropdown (desktop select + mobile dropdown), free-text filter box, date-range inputs, and (if `advanced-search` is enabled in `_data/theme.yml`) an Advanced Search modal for building multi-field AND/OR/NOT queries
- A "Sort by" dropdown (Random by default, plus Title and any field with a `sort_name` set in `config-browse.csv`)
- A responsive grid of article cards — thumbnail, title, and whichever fields from `config-browse.csv` aren't marked `hidden`
- Active filter indicators and a running result count

**Thumbnail construction (per card):**
1. Default thumbnail is the article's own `object_location` field — its first scanned image
2. If the article is *not* a manuscript (`arhival_holding` is empty) and has 3 or more child images (matched via `image_parent_id == objectid`), the thumbnail is swapped to the **third** image instead — typically a closer, more legible crop of the article text rather than a full front-page scan
3. Manuscripts (`arhival_holding` set) and articles with fewer than 3 images always use the first image
4. Thumbnails are lazy-loaded (`lazysizes`), so only cards actually scrolled into view get downloaded
5. Displayed at a fixed `aspect-ratio: 4/3` with `object-fit: cover; object-position: top`, so cards line up at a consistent height and any cropping trims from the bottom rather than the masthead/headline at the top of the scan

**Filterable vs. visible fields:** `_data/config-browse.csv` controls both, independently. Every row becomes a filter/sort/facet option regardless of its `hidden` value; only rows where `hidden` is not `true` are actually printed on the card. This lets a field (e.g. `document_intro`) stay searchable without cluttering the card grid.

**How it works:**
1. `_includes/js/browse-js.html` builds a `var items = [...]` JS array server-side: one object per `compound_object` row, with the fields listed in `config-browse.csv` plus `img`, `title`, `id`, and `parent`
2. Field values, the field-select dropdown, sort options, and the Advanced Search modal's field list are all generated from `_data/config-browse.csv` — adding a row there both makes a field filterable and (unless `hidden`) visible on cards
3. All actual filtering/sorting/rendering happens client-side in the browser after page load (see `_includes/js/browse-js.html`, or `_includes/js/browse-simple-js.html` if both `faceted-search` and `advanced-search` are disabled in `_data/theme.yml`)

---

## Publishers (`pages/publishers.md`)

**URL:** `/publishers/`

Groups all articles alphabetically by the `publication` field (the newspaper or magazine name). Articles with no publication are excluded.

**What it shows:**
- A count of total publications and articles at the top
- A "Manuscripts and Non-Periodical Texts" section at the very top, outside the A–Z scheme — covers archival manuscripts (grouped by publication names starting with "Manuscript") and any item with no real publisher name (labeled "Unattributed", with a location fallback if available)
- A small "Periodical Sources" label, then the normal A–Z letter headings as section anchors resume for everything else
- Each publication is a Bootstrap accordion item, collapsed by default; expanding it reveals its articles and, if one exists, a source note
- Under each publication: a list of its articles sorted by `date`, each linking to the article's item page (`/items/<objectid>.html`)
- Each list entry: article title, publication name, `publisher_location` (if present), and year
- Below the article list, a "Source Note" (from `_data/article_sourcenotes.csv`, falling back to the first article's `document_intro`) describing the publication itself, set apart from the article list by a divider and small label

**How it works:**
1. Filters metadata to `compound_object` rows → `articles`
2. Filters out rows where `publication` is empty → `with_pub`
3. Groups by `publication`, sorts groups alphabetically → `groups`
4. A first pass flags "special" groups — publication name starts with "Manuscript", or its first letter isn't A–Z (blank/odd names) — and collects their names into a delimited string
5. Special groups render first, under "Manuscripts and Non-Periodical Texts," via a shared include (`_includes/publisher-accordion-item.html`)
6. Remaining groups render under "Periodical Sources," resuming the normal per-letter A–Z headings, tracking first letter to insert each one
7. Within each group, sorts articles by `date` before listing

---

## Locations (`pages/locations.md`)

**URL:** `/locations.html`

Groups articles by the country and region of their `publisher_location`, with sub-sections for states/provinces where applicable. Includes a jump-to nav at the top of the page.

**Regions covered:** Australia, Canada, France, Germany, India, New Zealand, USSR, United Kingdom and Ireland, United States, Unpublished

**What it shows:**
- Total article count at top
- Each article listed with a color-coded reprint type badge, publication name (linked to item page), location, and year
- Australia and Canada are sub-divided by state/province
- United States is sub-divided by state

**Reprint type badges:**

| Badge color | Reprint type |
|---|---|
| Blue (`bg-primary`) | Original |
| Green (`bg-success`) | Direct |
| Grey (`bg-secondary`) | Truncated |
| Teal (`bg-info`) | Paraphrased (or any other type) |

**How it works:**
1. Filters metadata to `display_template == "compound_object"`, sorts by `publisher_location`
2. Assigns articles to country buckets using `publisher_location contains "…"` string matching (e.g. `contains ", Australia"`, `contains "United Kingdom"`, `contains "Maharashtra"` for India)
3. United States is everything that doesn't match any international marker and has a non-empty location
4. For Australia and Canada, a hardcoded list of states/provinces is iterated and articles are sub-filtered by state string
5. For the US, a hardcoded list of state suffixes (`, California`, `, New York`, etc.) is iterated similarly
6. Unpublished = articles where `publisher_location` is empty

Country and state detection is purely string-based matching on `publisher_location`, so the accuracy depends on consistent formatting of that field in the metadata CSV.

---

## Timeline (`pages/timeline.md`)

**URL:** `/timeline.html`

Groups all articles by year, in the same style as Publishers/Locations (plain Liquid, no client-side JS). Articles with no `date` are shown in a separate "Undated" section rather than being dropped.

**What it shows:**
- Total article count and year range at the top, plus a "Jump to" year nav (and "Undated" link, if applicable)
- One heading per year; under each, a responsive grid of article cards (thumbnail, title, publication), each linking to the article's item page
- An "Undated" section at the end for any article with a blank `date`

**How it works:**
1. Filters metadata to `compound_object` rows, splits into `dated` and `undated` (guarding against Jekyll's `nil` for blank CSV cells, not just `""`)
2. Sorts `dated` by `date` and derives the unique year list from the first 4 characters of each
3. For each year, filters articles whose `date contains` that year and renders a card per article via a shared include (`_includes/timeline-card.html`)
4. The card include builds the thumbnail `src` from `object_location`, falling back to `filename` then `image_object_location` — the same fallback chain used by `_includes/item/compound-gallery.html`

This replaced the stock CollectionBuilder `_layouts/timeline.html`, which assumed a `parentid` field this project's data doesn't have (it uses `image_parent_id`) — that mismatch let individual scanned-page images appear as their own timeline entries, linking to item pages that don't exist for child images. `_layouts/timeline.html` is no longer used by any page but is left in place as an unused vendor file (see `site_documentation/collectionbuilder_template_documentation/`).

---

## File Summary

| File | Role |
|---|---|
| `pages/browse.md` | Browse page — thin wrapper; layout + JS do the real work |
| `_layouts/browse.html` | Browse page layout — filter bar, sort menu, Advanced Search modal trigger |
| `_includes/js/browse-js.html` | Builds the `items` JSON array server-side and all client-side filter/sort/render/thumbnail logic |
| `_includes/js/browse-simple-js.html` | Fallback browse JS used when `faceted-search` and `advanced-search` are both disabled |
| `_includes/advanced-search-modal.html` | Advanced Search modal markup, field list generated from `config-browse.csv` |
| `_data/config-browse.csv` | Controls which fields are filterable/sortable/faceted and which are visible on cards |
| `pages/publishers.md` | Publishers browse page — groups into the special/periodical split, then loops per group |
| `_includes/publisher-accordion-item.html` | Renders one accordion item (article list + source note); shared by both the manuscripts/non-periodical loop and the periodical loop |
| `pages/locations.md` | Locations browse page — full Liquid logic inline |
| `pages/timeline.md` | Timeline browse page — groups articles by year |
| `_includes/timeline-card.html` | Renders one article thumbnail card; shared across all year sections (and "Undated") |
| `_layouts/timeline.html` | Unused vendor CollectionBuilder layout — no longer referenced by any page |
| `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv` | Source data for all pages on this file |

---

## Search

**URL:** `/search/` (page); toolbar box lives in `_includes/nav-search-lunr.html`

Full-text search across the whole collection, powered by Lunr.js — a separate mechanism from Browse's field filtering above.

**What user search terms connect to:** only the fields marked `index: true` in `_data/config-search.csv` are searchable — currently `title`, `date`, `author`, `publication`, `publisher_location`, `tropes`, and `document_intro`. A search for "Boston" matches because `publisher_location` (e.g. "Boston, Massachusetts") and `publication` (e.g. "Boston Evening Transcript") are indexed; a term that only appears in a non-indexed field (e.g. the full OCR transcript text, deliberately excluded to keep the client-side index small) won't return anything.

**How it works:**
1. The toolbar search box (`_includes/nav-search-lunr.html`) is a plain redirect — it URL-encodes whatever's typed and sends the browser to `/search/?q=...`
2. `assets/js/lunr-store.js` is a Jekyll-templated JS file: at build time it loops over the metadata (child images included if `search-child-objects` is `true` in `_data/theme.yml`) and, for each `index: true` field in `config-search.csv`, copies that field's value into a JS `store` object keyed by item id
3. `_includes/js/lunr-js.html` builds the actual Lunr index client-side from `store` on page load, reads `?q=` from the URL, and runs the search
4. Lunr's query syntax works directly in the search box: `field:term` (scoped search), trailing `*` wildcards, `~N` fuzzy matching, `^N` term boosting — documented for users in the "Search Options" modal on the search page
5. Each result links to `/items/<id>.html`, with `id` lowercased to match the actual generated filenames (item pages are slugified/lowercased by `_plugins/cb_page_gen.rb`)

**Which fields display in results:** controlled by the `display: true` column in `config-search.csv`. The first CSV row (must be `title`) becomes the clickable result heading; subsequent `display: true` rows are printed underneath it.
