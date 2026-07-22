# Article Page: Transcripts, Trope Highlighting, and Entity Panels

This document explains the full pipeline — from TEI XML source files to the interactive transcript on the article page — including how trope underlining and entity description panels are wired up.

---

## Overview

The transcript system has two offline build steps that produce static files, and then a fully client-side runtime that renders the transcript interactively without any server-side processing.

```
TEI XML  ──→  xml_to_json.py  ──→  *_transcript.json  ──→  [browser fetch + render]
                                                                    ↑
entity CSVs  ──→  build_entities_json.py  ──→  entities.json  ──→  entity-data.js
```

---

## Step 1: TEI XML Source Files

**Location:** `objects/<article_id>/m_<article_id>_TEI.xml`

Each article has a hand-encoded TEI XML file containing the transcript text with inline annotations:

- **Trope spans:** `<span type="trope" n="3">` — marks a passage as belonging to trope #3. Trope numbers map to labels via `_data/tropes.yml`.
- **Entity annotations:** `<persName key="#fremontcpt">`, `<placeName key="#ci_aca">`, `<orgName key="#natam_aleuts">`, `<name type="ship" key="#sh_active">` — links text to a named entity by key. A span can carry multiple keys separated by semicolons for group annotations.
- **Struck-through text:** `<del rend="strikethrough">` — appears only in the small set of manuscript-source articles (dictated interviews and personal narratives, as opposed to periodical clippings). Marks text the original writer or transcriber crossed out. See [`data_relationships_erd_explainer.md`](data_relationships_erd_explainer.md#manuscript-articles-struck-through-text) for which articles these are and why they're unique in the archive.

---

## Step 2: `utilities/xml_to_json.py` — Produce Transcript JSON

**Run:** `python utilities/xml_to_json.py` (all articles) or `python utilities/xml_to_json.py AlbanyEveningJournal1853` (one article)

**Input:** `objects/<article_id>/m_<article_id>_TEI.xml`
**Output:** `objects/<article_id>/<article_id>_transcript.json`

Walks the XML body, collecting `<p>` paragraphs and splitting each into **segments** — the smallest unit of annotated text. Each segment is one of:

- Plain text: `{ "text": "She had lived alone..." }`
- Troped text: `{ "text": "Wild Woman", "tropes": [3, 8] }` (multiple tropes can overlap)
- Entity text: `{ "text": "George Nidever", "entity_key": "nidever", "entity_type": "person" }`
- Both: `{ "text": "the Island", "tropes": [6], "entity_key": "ci_sni", "entity_type": "place" }`
- Group annotation (multiple entities on same text): uses `entity_keys` (array) instead of `entity_key`
- Struck-through text: adds `"deleted": true` to whatever segment it would otherwise be, e.g. `{ "text": "Colorado", "deleted": true }` or, if the crossed-out text was itself entity-tagged, `{ "text": "i", "entity_key": "lw", "entity_type": "person", "deleted": true }`. A `del_depth` counter in `extract_segments()` tracks nesting so text is flagged correctly even when a `<del>` wraps a nested entity tag.

The output JSON structure:
```json
{
  "article_id": "AlbanyEveningJournal1853",
  "paragraphs": [
    [ { "text": "..." }, { "text": "...", "tropes": [1] }, ... ],
    [ ... ]
  ]
}
```

**Must be re-run whenever TEI XML files are updated.**

---

## Step 3: `utilities/build_entities_json.py` — Build Entity Lookup

**Run:** `python utilities/build_entities_json.py`

**Input:** Five entity CSVs in `_data/`:
- `persons_entities.csv`
- `places_entities.csv`
- `groups_entities.csv`
- `orgs_entities.csv`
- `ships_entities.csv`

Each CSV has columns: `key`, `name`, `write_up` (and `latitude`/`longitude` for places).

**Output:** `_data/entities.json` — a flat key-to-entry lookup:

```json
{
  "fremontcpt": {
    "name": "A. M. Burns",
    "description": "A. M. Burns: employee of the Pacific Mail Steamers...",
    "type": "person"
  },
  "ci_aca": {
    "name": "Acapulco",
    "description": "Acapulco: a port city on the Pacific coast of Mexico...",
    "type": "place",
    "lat": 16.8636,
    "lng": -99.8825
  }
}
```

**Must be re-run whenever entity CSVs are updated.**

---

## Step 4: `assets/js/entity-data.js` — Jekyll-Processed Entity Data Bridge

This file has Jekyll front matter (`---`) so Jekyll processes it as a Liquid template at build time:

```js
window.ENTITY_DATA = {{ site.data.entities | jsonify }};
```

At build time, Jekyll serializes the entire `_data/entities.json` into the JS file as a global variable. This makes entity data available in the browser without any API call. Loaded by `_includes/entity-panel.html` via a `<script src>` tag.

---

## Runtime: Transcript Rendering

**Rendering logic lives in one place:** `_includes/transcript-viewer.html`
**Included by:** `_layouts/item/compound_object.html` (right column of the article page), via `{% include transcript-viewer.html document_id=page.article_id %}`


The transcript `<div>` is rendered with a `data-src` attribute pointing to the JSON file:

```html
<div id="transcript-AlbanyEveningJournal1853"
     class="transcript-viewer"
     data-src="/objects/AlbanyEveningJournal1853/AlbanyEveningJournal1853_transcript.json">
```

An inline `fetch()` loads the JSON at runtime and calls `buildSegmentNode()` on each segment to construct DOM nodes:

| Segment type | DOM output |
|---|---|
| Plain text | `TextNode` |
| Troped text | `<mark class="trope-mark trope-3" data-tropes="3">` |
| Entity text | `<span class="entity-link" data-entity-key="..." data-entity-type="...">` |
| Both (trope + entity) | `<mark>` wrapping a `<span>` |
| Group entity | `<span class="entity-link" data-entity-keys='["key1","key2"]'>` |
| Struck-through (`deleted: true`) | Whatever node the segment would otherwise be, wrapped in `<del class="transcript-deletion" title="Struck through in the original manuscript">` |

The `.transcript-deletion` rule (injected into `<head>` alongside the trope color variables — see the `trope_css` capture block near the top of the include) renders it with `text-decoration: line-through` and reduced opacity, so it's still fully readable but visually distinct from the surrounding text. Because the wrap happens last in `buildSegmentNode()`, a struck-through entity is still a clickable `.entity-link` inside the `<del>` — the entity panel behaves normally even for crossed-out names.

---

## Trope Highlighting

**Panel include:** `_includes/interpretive-panel.html`
**Color/label config:** `_data/tropes.yml`

Trope colors are defined in `_data/tropes.yml` (id, label, color hex). At page load, the layout injects CSS variables into `<head>`:

```css
:root {
  --trope-1-color: #hex;
  --trope-3-color: #hex;
  ...
}
```

The interpretive panel (shown when "Interpretive Mode" is active) lists only the tropes **present in the current document** — pulled from `page.tropes` (the semicolon-separated tropes field in the metadata CSV). Each trope gets a colored checkbox.

When a checkbox is checked, `recalculateStripes()` runs and applies `box-shadow` underlines to all matching `<mark data-tropes>` elements. Multiple active tropes produce stacked underlines in each trope's color:

```js
// e.g. tropes 1 and 3 both active on a span:
boxShadow: "0 3px 0 0 #color1, 0 6px 0 0 #color3"
```

Unchecking a trope removes its stripe. Exiting Interpretive Mode unchecks all boxes and clears all highlights.

---

## Entity Panels

**Panel HTML:** `_includes/entity-panel.html`
**Panel logic:** `assets/js/entity-panel.js`
**Data:** `window.ENTITY_DATA` (set by `assets/js/entity-data.js`)

Clicking any underlined entity text in the transcript triggers a click listener on the `.transcript-viewer` div:

- If the span has `data-entity-key` (single entity) → calls `window.openEntityPanel(key, type)`
- If the span has `data-entity-keys` (group) → calls `window.openGroupPanel(keysArray)`

**Single entity panel:** looks up the key in `window.ENTITY_DATA`, populates `#ep-title` and `#ep-description`, hides the gallery (or interpretive panel, tracking which was active), and shows `#entity-panel`.

**Group panel:** renders a list of clickable entity names. Clicking one drills into that entity's panel and shows a back button to return to the group list.

**Closing** the entity panel restores whichever left-column view was active before (gallery or interpretive panel).

---

## File Summary

| File | Role |
|---|---|
| `objects/<id>/m_<id>_TEI.xml` | Source: hand-encoded TEI XML with trope and entity annotations |
| `utilities/xml_to_json.py` | Build script: converts TEI XML → `*_transcript.json` per article |
| `objects/<id>/<id>_transcript.json` | Output of xml_to_json.py; fetched by the browser at runtime |
| `_data/{persons,places,groups,orgs,ships}_entities.csv` | Source: entity name, key, and write-up data |
| `utilities/build_entities_json.py` | Build script: merges entity CSVs → `_data/entities.json` |
| `_data/entities.json` | Flat entity lookup keyed by ID |
| `assets/js/entity-data.js` | Jekyll-processed bridge: serializes `entities.json` into `window.ENTITY_DATA` |
| `assets/js/entity-panel.js` | Runtime: panel logic, `openEntityPanel()`, `openGroupPanel()` |
| `_data/tropes.yml` | Trope id / label / color definitions |
| `_includes/interpretive-panel.html` | Trope checklist panel; triggers `recalculateStripes()` |
| `_includes/entity-panel.html` | Entity panel DOM and script loader |
| `_includes/transcript-viewer.html` | The transcript renderer: trope CSS, `fetch()`, `buildSegmentNode()`, entity-link click handling, strikethrough wrapping |
| `_layouts/item/compound_object.html` | Main article page layout; includes `transcript-viewer.html` and wires up the gallery/interpretive-panel/entity-panel views around it |

---

## When to Re-run Build Scripts

| Change made | Script to re-run |
|---|---|
| Edited a TEI XML file | `python utilities/xml_to_json.py <article_id>` |
| Added or updated any entity CSV | `python utilities/build_entities_json.py` |
| Both | Run both scripts, then rebuild the Jekyll site |
