# Metadata Pipeline Overview

This folder contains the notebooks and scripts that build the CollectionBuilder master metadata CSV from raw image files, article metadata, TEI XML annotations, and reprint/document-group data. Run them in the order listed below.

---

## 1. `image_metadata_maker.ipynb`

Walks every article folder inside `objects/` and generates one parent row (`compound_object`) and one child row per image file (`image`) for each article. Also standardizes image filenames (converts `(N)` suffix notation to `_N`).

**Input:** `../objects/` (image folders at project root)
**Output:** `image_metadata_full.csv` (this folder)

Columns produced: `object_id`, `article_id`, `image_display_template`, `image_parent_id`, `image_file`, `image_object_location`

---

## 2. `metadata_merger.ipynb`

LEFT JOINs the image rows from Step 1 with the article-level metadata spreadsheet so that every image row carries the full article context (title, date, publication, author, etc.) repeated across it.

**Input:** `image_metadata_full.csv` (this folder), `article_metadata_starter.csv` (this folder)
**Output:** `images_with_article_metadata.csv` (this folder)

---

## 3. `trope_transc_metadata_adder.ipynb`

Two passes in one notebook:

1. **Tropes** — reads each article's TEI XML file (`objects/<article_id>/m_<article_id>_TEI.xml`) and extracts `<span type="trope" n="X">` tags, mapping them to human-readable labels (e.g. `Indian Queen`, `Captivity`, `Noble Savage`). Adds a semicolon-separated `tropes` column.
2. **Transcripts** — reads each article's initial transcript file (`objects/<article_id>/<article_id>_InitTransc.txt`), handling multiple encodings. Adds a `transcripts` column to `compound_object` rows only.

**Input:** `images_with_article_metadata.csv` (this folder), `../objects/` (TEI XML files + `_InitTransc.txt` files)
**Output:** `metadata_with_tropes.csv` → `metadata_with_tropes_transcripts.csv` (both in this folder)

> After this step, `metadata_with_tropes_transcripts.csv` must be combined with reprint data manually (or via a separate step) to produce `complete_metadata_images_tropes_reprints_transcripts.csv` in this folder before the next notebook can run.

---

## 4. `reprint_metadata_maker.ipynb`

Two cells in sequence:

1. **Build long-form reprint table** — reads the wide-format `document_groups.csv` (one row per group, reprints spread across columns) and pivots it into a long table with columns `article_id`, `group_reprint_id` (e.g. `Stuart1878_reprint`), and `reprint_type` (`original`, `direct`, `truncated`, or `paraphrase`). Saves this as `document_groups_labeled.csv`.
2. **Merge into master CSV** — LEFT JOINs the long reprint table onto the master CSV by `article_id`, adding `group_reprint_id` and `reprint_type` columns. Overwrites the master CSV in place.

**Input:** `document_groups.csv` (this folder), `complete_metadata_images_tropes_reprints_transcripts.csv` (this folder)
**Output:** `document_groups_labeled.csv` (this folder), `complete_metadata_images_tropes_reprints_transcripts.csv` (updated in place)

---

## 5. `prepare_cb_metadata_objectids.ipynb`

Makes the fully-merged CSV CollectionBuilder-compatible, with a focus on correctly resolving `objectid` uniqueness for articles that appear in multiple reprint groups:

- Rebuilds `objectid` values from `article_id` + `group_reprint_id` + `reprint_type` to eliminate duplicate IDs
- Derives `filename` from `image_object_location` (strips leading `objects/`)
- Adds `object_location` column (prefixes each filename with `/objects/`)
- Adds `display_template` column (copy of `image_display_template`)
- Sets `format` column (`image` for image rows, `multiple` for compound_object rows)
- Renames `object_id` to `article_image_tag`

**Input:** `complete_metadata_images_tropes_reprints_transcripts.csv` (this folder)
**Output:** `../_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv` — **the master CollectionBuilder CSV**

---

## 6. `article_document_group_analysis.ipynb`

Read-only analysis notebook — does not modify any CSV. Identifies the many-to-many relationship between articles and document groups: which articles appear in more than one reprint group and which groups they belong to. Run this anytime to verify data integrity or to inspect the cross-group structure.

Reads only `compound_object` rows (one per article per document group), groups by `article_id`, and flags any article with more than one distinct `group_reprint_id`. The 13 articles identified account for the difference between 481 unique articles and 494 compound-object rows in the master CSV — each dual-member article appears once per group.

**Input:** `../_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`
**Output:** `../_data/multi_group_articles.csv` — the 13 articles belonging to more than one document group, with their group memberships as a semicolon-separated string and a `num_groups` count column

See `site_documentation/many_to_many_relationships_erd.md` for the full list of the 13 articles and an explanation of why dual membership occurs.

---

## 7. `prepare_article_map_locations.py`

Standalone script (not a notebook) that produces a CSV for geographic arc visualization of reprint travel. Not part of the master CSV pipeline — reads from the already-finished master.

For each article in a reprint group, it records the article's own publication location and the original publication's location as arc endpoints. Geocodes all `publisher_location` values via Nominatim (OpenStreetMap), caching results in `geocode_cache.json` to avoid redundant API calls on reruns. Filters to `compound_object` rows only (one row per article, no image children). Articles appearing in multiple document groups will have one row per group (494 rows total vs 481 unique articles).

**Input:** `../_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`
**Output:** `../_data/article_map_locations.csv`

---

## Reference: `_data/article_ids_only.csv`

Not generated by any notebook in this folder — this is a manually created export containing exactly one row per unique article (481 rows), with no duplicates from multi-group articles and no image child rows. Columns are identical to `article_map_locations.csv`. It exists as a clean, flat reference for quickly understanding the total set of discrete articles and their locations, and is used directly by the trope bar charts and sparklines on the site.

---

## Pipeline at a glance

```
objects/        article_metadata_starter.csv
    │                       │
    ▼                       │
image_metadata_maker ───────┘
    │ image_metadata_full.csv
    ▼
metadata_merger
    │ images_with_article_metadata.csv
    ▼
trope_transc_metadata_adder  ← TEI XMLs + _InitTransc.txt files
    │ metadata_with_tropes_transcripts.csv
    │   [manual: merge into complete_metadata_... CSV]
    ▼
reprint_metadata_maker  ← document_groups.csv
    │ complete_metadata_images_tropes_reprints_transcripts.csv (updated in place)
    ▼
prepare_cb_metadata_objectids
    │
    ▼
_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv  ← MASTER
    │                   │
    ▼                   ▼
prepare_article_map_locations.py    article_document_group_analysis  (read-only, run anytime)
    │                                   │
    ▼                                   ▼
_data/article_map_locations.csv     _data/multi_group_articles.csv
```
