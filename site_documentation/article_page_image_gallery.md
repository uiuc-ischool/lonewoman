# Article Page: Compound Object Layout and Image Gallery

Each article in the archive is a **compound object** in CollectionBuilder terms: one parent record representing the article, plus one child record per scanned image page. This document explains how those records are assembled and displayed as a side-by-side image gallery and transcript viewer.

---

## Data: How Parent and Child Records Are Structured

The master metadata CSV (`_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`) contains two types of rows per article:

- **Parent row** — `image_display_template: compound_object`. One row per article. Holds article-level metadata (title, date, publication, tropes, transcript, etc.). Its `objectid` is the unique article identifier (e.g. `AlbanyEveningJournal1853__Goliah1853_DPT_reprint__direct`).
- **Child rows** — `image_display_template: image`. One row per scanned page image. Each has `image_parent_id` set to the parent's `objectid`, and `filename` pointing to the image file (e.g. `AlbanyEveningJournal1853/AlbanyEveningJournal1853_DigSur_1.png`).

Image files themselves live at: `objects/<article_id>/<filename>`

---

## Layout: The Two-Column Article Viewer

**Layout file:** `_layouts/item/compound_object.html`

The page renders a two-column flex layout:

```
┌────────────────────────┬─────────────────────────────┐
│  LEFT (48%)            │  RIGHT (flex: 1)             │
│  Image gallery         │  Transcript                  │
│   — or —              │  (with trope highlights       │
│  Interpretive panel    │   and entity links)          │
│   — or —              │                              │
│  Entity panel          │                              │
└────────────────────────┴─────────────────────────────┘
```

At the top of the layout, Jekyll queries the metadata to find child image records:

```liquid
{%- assign all = site.data[site.metadata] -%}
{%- assign children = all | where: "image_parent_id", page.objectid -%}
```

Those child rows are passed to the gallery include.

---

## Gallery Include

**Include file:** `_includes/item/compound-gallery.html`

Receives the `children` array and renders the scanned page images as a clickable, navigable gallery. Images are served as static files from `objects/`.

---

## Left Column View Modes

The left column can show three different things, toggled by buttons beneath it:

| View | When active | How triggered |
|---|---|---|
| **Image gallery** | Default | Always on load |
| **Interpretive panel** | When "Interpretive Mode" is active | "Interpretive Mode" button |
| **Entity panel** | When a named entity is clicked in the transcript | Click on underlined entity text |

JavaScript in `compound_object.html` manages swapping between views using `d-none` class toggling. The "Interpretive Mode" button is wired to show/hide `#gallery-view` and `#panel-view`. The entity panel logic (in `assets/js/entity-panel.js`) hides whichever view is currently shown and restores it on close.

---

## Controls

Two buttons sit beneath the left column:

- **Interpretive Mode** — hides the gallery and shows the trope checklist panel (see `_includes/interpretive-panel.html` and the transcript/trope documentation).
- **Expand Document** — hides the entire left column, letting the transcript fill the full page width. Toggling again restores the two-column view.

On mobile (≤767px), the columns stack vertically.

---

## File Summary

| File | Role |
|---|---|
| `_layouts/item/compound_object.html` | Main page layout; queries children, renders two-column view, wires buttons |
| `_includes/item/compound-gallery.html` | Renders the child image records as a clickable gallery |
| `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv` | Master metadata; parent and child rows that define the compound object structure |
| `objects/<article_id>/<filename>.png` | Scanned page images served as static files |
