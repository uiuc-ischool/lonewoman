# Browse Pages: Publishers, Locations, and Timeline

These three pages appear in the site toolbar and give readers different ways to browse the full set of articles. All three read directly from the master metadata CSV at build time via Jekyll Liquid — no JavaScript or client-side fetching is involved. Each page filters to `compound_object` rows only (one row per article; image child rows are excluded).

**Data source for all three:** `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`

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

## Timeline (`pages/timeline.md` + `_layouts/timeline.html`)

**URL:** `/timeline.html`

A standard CollectionBuilder timeline layout. Displays all articles organized by year in a table, with thumbnail images linking to each article page.

**What it shows:**
- A year-range header (first year → last year in the collection)
- An optional year-jump dropdown (configured in `_data/theme.yml` via `year-navigation` or `year-nav-increment`)
- A striped table with one row per year; each year row contains a responsive grid of article thumbnails
- Clicking a thumbnail goes to the article's item page

**How it works:**
1. Reads items from the metadata CSV; excludes child objects (rows with a `parentid`) so only top-level article records appear
2. Sorts by the `date` field (configurable via `site.data.theme.timeline-field`; defaults to `"date"`)
3. Extracts years from the date field (handles `YYYY-MM-DD`, `MM/DD/YYYY`, and bare year formats)
4. Deduplicates and sorts years, then groups articles by year for table rendering
5. For each article, shows `image_thumb` if available, or a fallback card with the title and a format icon

The timeline page file (`pages/timeline.md`) contains only front matter and a heading — all the logic lives in `_layouts/timeline.html`, which is part of the CollectionBuilder template (see `site_documentation/collectionbuilder_template_documentation/`).

---

## File Summary

| File | Role |
|---|---|
| `pages/publishers.md` | Publishers browse page — groups into the special/periodical split, then loops per group |
| `_includes/publisher-accordion-item.html` | Renders one accordion item (article list + source note); shared by both the manuscripts/non-periodical loop and the periodical loop |
| `pages/locations.md` | Locations browse page — full Liquid logic inline |
| `pages/timeline.md` | Timeline page stub — just front matter and a heading |
| `_layouts/timeline.html` | CollectionBuilder timeline layout with all rendering logic |
| `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv` | Source data for all three pages |
