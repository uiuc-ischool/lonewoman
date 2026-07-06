# Many-to-Many Relationships and ERD Documentation

This document covers two many-to-many relationships in the archive's data model — articles↔document groups and articles↔tropes — and describes the three ERD diagrams produced to visualize the data architecture.

---

## The 13 Articles in Multiple Document Groups

Most articles in the archive belong to exactly one document group (reprint network). However, 13 articles each belong to two document groups simultaneously. This is a product of the archive's sourcing methodology: some press accounts drew from two distinct source texts, making them valid members of both the group descending from the first source and the group descending from the second.

| article_id | Document Group 1 | Document Group 2 |
|---|---|---|
| CambriaFreeman1879 | SalemWeeklyReview1879_reprint | Stuart1878_reprint |
| SalemWeeklyReview1879 | SalemWeeklyReview1879_reprint | Stuart1878_reprint |
| ShipwreckedMariner1879 | SalemWeeklyReview1879_reprint | Stuart1878_reprint |
| TheGazette1879 | Stuart1878_reprint | TheGazette1879_reprint |
| TheNewfoundlander1879 | Stuart1878_reprint | TheGazette1879_reprint |
| ThePublicLedger1879 | Stuart1878_reprint | TheGazette1879_reprint |
| Taylor1860_12(11) | Russell1856_HCF_reprint | Taylor1860_12(11)_reprint |
| Taylor1860_13(16) | Russell1856_HCF_reprint | Taylor1860_12(11)_reprint |
| Warner1856_EB | Russell1856_HCF_reprint | Warner1856_LAS_reprint |
| Warner1856_LAS | Russell1856_HCF_reprint | Warner1856_LAS_reprint |
| Sheridan1925 | Sheridan1925_reprint | Terry1882_reprint |
| Sheridan1927_21(33) | Sheridan1925_reprint | Terry1882_reprint |
| Sheridan1927_21(34) | Sheridan1925_reprint | Terry1882_reprint |

All 13 cases involve paraphrase relationships, where a later article drew on two earlier texts rather than reprinting one directly. `Stuart1878_reprint` appears in 7 of the 13 cases, reflecting how widely George Nidever's 1878 memoir circulated as a secondary source alongside other 1879 reports.

The 13 dual-membership articles account for the discrepancy between the archive's 481 unique articles and the 494 compound-object rows in the master CSV — each dual-member article generates two compound-object rows, one per group.

### How this is computed

`metadata_notebooks/article_document_group_analysis.ipynb` identifies these articles by reading the master CollectionBuilder CSV and grouping on `article_id` across `compound_object` rows (which are one row per article per document group). Any `article_id` with more than one distinct `group_reprint_id` is flagged as a multi-group article.

The notebook saves results to `_data/multi_group_articles.csv` (three columns: `article_id`, `document_groups` as a semicolon-separated string, `num_groups`). This is a read-only analysis — it does not modify the master CSV.

---

## ObjectIDs: Compound Objects and Image Rows

Every row in the master CSV (`_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`) carries a unique `objectid`. There are two row types, and together they account for every objectid in the archive:

| Row type | Count | Description |
|---|---|---|
| `compound_object` (article parents) | 494 | One per article per document group — the parent record |
| `image` (digitized scan pages) | 3,934 | One per individual scanned page — children of a compound_object |
| **Total objectids** | **4,428** | Every row has a unique objectid |

A `compound_object` row is the parent that groups all the scanned page images for one article together. Each `image` row has an `image_parent_id` pointing back to its compound_object parent. CollectionBuilder uses this parent–child structure to build the image gallery on each article page.

The 494 compound_object rows (rather than 481) reflect the 13 dual-membership articles: each of those articles appears in two document groups and therefore has two compound_object rows — and two sets of image children. The image rows for dual-membership articles are duplicated once per group membership. The average article has **8.2 scanned pages**.

---

## Article Coverage Analyses

The analyses below are computed by `metadata_notebooks/article_document_group_analysis.ipynb` and characterise the full set of 481 unique articles across three dimensions. Run the notebook to reproduce.

### 1. Reprint Group Membership

Most articles in the archive are members of at least one reprint network, but a substantial minority stand alone.

| Category | Count | % of 481 |
|---|---|---|
| In at least one reprint group | 362 | 75.3% |
| Not in any reprint group (standalone) | 119 | 24.7% |
| **Total unique articles** | **481** | |

Standalone articles include books, monographs, manuscripts, and periodical articles that were collected as direct sources or contextual references rather than as participants in a text-reprinting chain. Examples include the Nidever and Dittman manuscripts (Bancroft Library), French-language editions, academic monographs, and a handful of newspaper articles that were sourced independently rather than traced through a reprint lineage.

### 2. Source Note Coverage

Source notes are publication-history descriptions that appear on the Publishers page. They were written exclusively for **periodical publications** (newspapers, magazines, journals). Books, manuscripts, theses, and government reports do not have source notes — this is intentional, not a data gap.

| Category | Count | % of 481 |
|---|---|---|
| Articles with a source note (periodical sources) | 422 | 87.7% |
| Articles without a source note (non-periodical sources) | 59 | 12.3% |
| **Total unique articles** | **481** | |

The 59 articles without source notes are the same category as the standalone non-periodicals described above: books (e.g., *Handbook of the Indians of California*, *Island of the Blue Dolphins*), French-language editions, theses, and government reports. These sources are vital to the archive's scholarly context but are not newspaper-type publications for which a publication history would be written.

Two of the 59 — George Nidever's *The Life and Adventures of a Pioneer of California Since 1834* (Manuscript C-D133) and Carl Dittman's *Narrative of a Seafaring Life on the Coast of California* (Manuscript C-D67) — are an exception on the Publishers page: because they have `document_intro` essays in the master CSV, those intro texts are displayed in place of a source note beneath their publication headings. All other non-periodical sources show no descriptive text on the Publishers page.

### 3. Articles with Document Introductions

Document introductions are substantial analytical essays — ranging from roughly 1,800 to 6,200 characters — written by Professor Schwebel about key source documents in the archive. Only five articles carry a `document_intro`:

| article_id | Publication | Document Group | Chars |
|---|---|---|---|
| TheBostonAtlas1847 | Boston Atlas | TheBostonAtlas1847_reprint | ~2,800 |
| DailyAltaCalifornia1853 | San Francisco Daily Alta California | DailyAltaCalifornia1853_reprint | ~1,900 |
| Hardacre1880_SM | Scribner's Monthly | Hardacre1880_SM_reprint | ~4,600 |
| Nidever1878 | Manuscript C-D133 | *(standalone)* | ~5,800 |
| Dittman1878 | Manuscript C-D67 | *(standalone)* | ~6,200 |

The three reprint-group intros (Boston Atlas, Daily Alta California, Hardacre/Scribner's Monthly) anchor three of the archive's most historically significant text-reprinting networks. They explain the cultural and journalistic context in which these founding documents circulated — why the Lone Woman's story spread so far and how it was transformed along the way. These three intros connect directly to the Literary Tropes essay, which traces how specific language and ideas moved through successive reprints.

The two manuscript intros (Nidever and Dittman) discuss the two key eyewitness sources that most shaped the historical record. George Nidever's 1878 dictation became the most-cited account of the Lone Woman's removal from San Nicolas Island; Carl Dittman's parallel narrative, long overshadowed by Nidever's, offers a contrasting perspective shaped by Dittman's status as a foreign-born, naturalized citizen. Both intros appear on the Publishers page beneath their respective manuscript entries.

Document intros appear on the Document Groups page beneath the interactive arc map for each group, and on the Publishers page beneath the publication heading. The 34 remaining document groups have no intro written for them.

---

## Many-to-Many: Articles and Document Groups

An article can belong to more than one document group, and a document group contains many articles. This is a true many-to-many (N:M) relationship.

In the master CSV (`_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`), this relationship is stored implicitly: each `compound_object` row for a multi-group article carries its `group_reprint_id` and `reprint_type` for that particular group membership. The article's image children are duplicated once per group as well. This is the CollectionBuilder-compatible flattened representation.

The underlying relational structure is:

```
Article ──(1:N)──> Article_Reprint <──(1:N)── Reprints (Document Group)
```

`Article_Reprint` is a junction table with a composite primary key of `(article_id, group_reprint_id)`. Each row represents one membership. The 13 dual-membership articles each contribute two rows; all other articles contribute one.

This is modeled in the enhanced ERD via the `Article_Reprint` entity. See [ERD: Overall Data Architecture](#erd-overall-data-architecture-lonewoman_erd_enhanced) below.

---

## Many-to-Many: Articles and Tropes

Each article can carry multiple interpretive tropes, and each trope appears across many articles. This is also an N:M relationship.

In the master CSV, tropes are stored as a semicolon-separated string in the `tropes` column on `compound_object` rows (e.g., `Indian Queen; Captivity; Noble Savage`). The relational structure underlying that flat encoding is:

```
Article ──(1:N)──> Article_Trope <──(1:N)── Trope
```

`Article_Trope` is a junction table with a composite PK of `(article_id, trope_id)`. Trope definitions (id, label, color) are stored separately in `_data/tropes.yml`.

This is modeled in the enhanced ERD alongside the article↔document group junction. The two junction tables (`Article_Reprint` and `Article_Trope`) follow the same structural pattern.

---

## ERD Diagrams

Three sets of ERD diagrams were produced using Python's `graphviz` library (Graphviz crow's foot notation, rendered with the `dot` layout engine).

### ERD: Individual Boston Atlas 1847 Articles (`ERD/ERD_output/`)

**Generator:** `ERD/generate_filled_erd.ipynb`

Individual article-level ERD diagrams were created for every article in the Boston Atlas 1847 document group — the largest and most historically central reprint network in the archive. Each diagram shows one article as a node connected to its images, publication, location, and document group, using actual data values from the master CSV rather than abstract column names.

The Boston Atlas 1847 group contains 15 articles, and one diagram exists for each:

| Article | File |
|---|---|
| TheBostonAtlas1847 (original) | `TheBostonAtlas1847_erd.png/svg` |
| ChristianAdvocateAndJournal1847 | `ChristianAdvocateAndJournal1847_erd.png/svg` |
| EdgefieldAdvertiser1847 | `EdgefieldAdvertiser1847_erd.png/svg` |
| LongIslander1848 | `LongIslander1848_erd.png/svg` |
| NewBedfordMercury1847 | `NewBedfordMercury1847_erd.png/svg` |
| NewYorkDailyTribune1847 | `NewYorkDailyTribune1847_erd.png/svg` |
| NewYorkEveningExpress1847 | `NewYorkEveningExpress1847_erd.png/svg` |
| PublicLedger1847 | `PublicLedger1847_erd.png/svg` |
| SpiritOfTheTimes1847 | `SpiritOfTheTimes1847_erd.png/svg` |
| TheFriend1847 | `TheFriend1847_erd.png/svg` |
| TheLivingAge1847 | `TheLivingAge1847_erd.png/svg` |
| ThePolynesian1847 | `ThePolynesian1847_erd.png/svg` |
| TheVermontJournal1847 | `TheVermontJournal1847_erd.png/svg` |
| WisconsinHerald1847 | `WisconsinHerald1847_erd.png/svg` |

All output files are in `ERD/ERD_output/`.

---

### ERD: CambriaFreeman1879 Multi-Group Example (`ERD/ERD_output/`)

**Generator:** Final code cell in `ERD/generate_filled_erd.ipynb`

A dedicated diagram showing `CambriaFreeman1879` connected to two document groups simultaneously — the clearest illustration of the N:M article↔document group relationship with real data. This article is a March 1879 issue of the Cambria (PA) Freeman that drew from both the Salem Weekly Review (direct reprint) and the Stuart 1878 memoir (paraphrase).

The diagram uses two separate amber-shaded nodes for the two document groups, with edge labels indicating the relationship type (`belongs to (direct)` and `belongs to (paraphrase)`):

- `ERD/ERD_output/CambriaFreeman1879_multigroup_erd.png`
- `ERD/ERD_output/CambriaFreeman1879_multigroup_erd_svg.svg`

---

### ERD: Overall Data Architecture (`ERD/`)

**Generator:** `ERD/generate_erd_enhanced.py`

A schema-level ERD showing all entities and their relationships across the full archive. Uses crow's foot notation (arrowhead = many, flat line = one). Entities included:

| Entity | Description |
|---|---|
| Article | Core article record (481 unique articles) |
| Publication | Newspaper or journal title |
| Location | Publisher city/location |
| Images | Digitized scan pages (image child rows) |
| Reprints | Document groups (reprint networks) |
| Article_Reprint | Junction table for Article↔Reprints N:M |
| Trope | Interpretive trope definitions |
| Article_Trope | Junction table for Article↔Trope N:M |

Key design decisions:
- `Article_Reprint` and `Article_Trope` are explicit junction entities, each with a composite PK of both FK columns, representing the N:M relationships correctly rather than as FK columns on Article.
- The diagram is generated from `generate_erd_enhanced.py` (not a notebook), which reads the master CSV for statistics but generates the schema statically.

Output files (at project root `ERD/`, not in `ERD_output/`):
- `ERD/lonewoman_erd_enhanced.png`
- `ERD/lonewoman_erd_enhanced_svg.svg`

---

## File Summary

| File | Role |
|---|---|
| `_data/multi_group_articles.csv` | 13 dual-membership articles with their group pairs |
| `metadata_notebooks/article_document_group_analysis.ipynb` | Read-only analysis that produces `multi_group_articles.csv` |
| `ERD/generate_filled_erd.ipynb` | Generates individual Boston Atlas 1847 article ERDs + CambriaFreeman1879 multi-group ERD |
| `ERD/generate_erd_enhanced.py` | Generates the overall schema ERD with all entities and junction tables |
| `ERD/ERD_output/` | All individual and example ERD output files (PNG + SVG) |
| `ERD/lonewoman_erd_enhanced.png` | Overall data architecture ERD (PNG) |
| `ERD/lonewoman_erd_enhanced_svg.svg` | Overall data architecture ERD (SVG) |
