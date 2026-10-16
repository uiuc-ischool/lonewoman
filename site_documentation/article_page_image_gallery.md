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

Receives the `children` array and renders one big preview image plus a row of thumbnail buttons below it. Clicking a thumbnail swaps the big preview's `src` in place (plain JS, no page reload) — this is separate from, and doesn't trigger, the full-screen viewer described next.

```
┌──────────────────────────┐
│                          │
│   big preview image      │  ← <a class="spotlight"> wrapping <img id="cbCompoundMain">
│                          │     (click → opens full-screen viewer)
├──────────────────────────┤
│ [thumb][thumb][thumb]... │  ← <button data-src="..."> (click → swaps preview above only)
└──────────────────────────┘
```

Images are served as static files from `objects/`.

---

## Full-Screen Viewer (Spotlight) and In-Article Image Navigation

Clicking the big preview image opens a full-screen lightbox, powered by `assets/lib/spotlight.bundle.js` (loaded whenever a layout sets `gallery: true`, per `_includes/foot.html`). Inside that viewer, next/prev arrows let the reader flip through **every image in that same article** — without ever leaving the article or jumping to a different one. This is a distinct feature from the chronological `«`/`»` arrows described below, which move between articles; these move between pages of the *same* article's scan.

**How the grouping works:** Spotlight has no Liquid/Jekyll awareness — it's a plain client-side library that scans the DOM for elements with class `.spotlight` and treats them as one navigable set. Reading the minified bundle directly shows the exact mechanism: on click, it looks for the closest ancestor with class `.spotlight-group`; if found, the gallery set is every `.spotlight` element *inside* that container (otherwise it falls back to every `.spotlight` on the whole page).

`_includes/item/compound-gallery.html` wraps its markup in a `.spotlight-group` container and gives every image in `children` its own `.spotlight` link — but only the first (the big preview) is actually visible:

```html
<div class="card mb-4 text-center spotlight-group">
  <a class="spotlight" href="...image_1...">            <!-- visible: the big preview -->
    <img id="cbCompoundMain" ...>
  </a>

  <!-- one per remaining image, invisible — exists only so Spotlight knows about it -->
  <a class="spotlight" href="...image_2..." style="display:none;" aria-hidden="true" tabindex="-1"></a>
  <a class="spotlight" href="...image_3..." style="display:none;" aria-hidden="true" tabindex="-1"></a>
  ...

  <!-- visible thumbnail strip: unrelated <button> elements, just swap the preview above -->
</div>
```

These hidden links exist purely to register the rest of the article's images with Spotlight's internal scan — they're not part of the visible thumbnail strip and aren't reachable by keyboard/tab (`tabindex="-1"`, `aria-hidden="true"`) since they're decorative plumbing, not a second UI. `getElementsByClassName` (what Spotlight uses internally) returns elements in document order, so the gallery set always matches the article's actual image sequence 1→N, same order as the thumbnail strip and the default preview.

This mirrors a pattern already used elsewhere in the template for different display types — `_layouts/item/multiple.html` and `_includes/item/image-gallery.html` both make every image a visible `.spotlight` link, relying on the same document-wide fallback grouping since there's only one gallery per page. The compound-gallery case is the odd one out only because its visible UI (one big preview + a thumbnail picker) doesn't show every image as its own link — the explicit `.spotlight-group` plus hidden links reproduce the same grouping without changing that UI.

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

## Article-to-Article Navigation (`«` / `»` Arrows)

Separate from the in-article image navigation above, every item page also has `«`/`»` arrow buttons (`_includes/item/browse-buttons.html`) that move to a **different article entirely** — previous/next in the collection, not previous/next page of the current scan. These are easy to mix up since they look similar (and the modal/full-screen viewer reuses the same left/right-arrow-key convention), so it's worth being explicit about what each one actually does:

| | Moves between | Triggered by |
|---|---|---|
| Full-screen viewer next/prev (see above) | Images *within* the current article | Spotlight's own UI; left/right arrow keys while the full-screen viewer is open |
| `«`/`»` buttons (this section) | *Different articles* | `#prev-page-button`/`#next-page-button`; left/right arrow keys when no modal/viewer is open |

**Where `previous_item`/`next_item` come from:** these aren't metadata fields — they're computed and injected onto every item page at build time by `_plugins/cb_page_gen.rb`, the same Jekyll plugin that generates the item pages themselves. The logic is simple and has nothing to do with date, title, or how the reader browsed to the page: it walks the master metadata CSV (`_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`) top to bottom, filtered (via `_config.yml`'s `page_gen.filter_condition: '!record["image_parent_id"]'`) down to the 494 top-level article rows — child scan-image rows are excluded from this sequence entirely. Whichever row sits physically one line above/below in the CSV becomes that article's "previous"/"next," and it wraps around at the ends (the last article's "next" loops back to the first, and vice versa).

**Because of that, row order in the CSV *is* browse order.** The CSV is kept sorted chronologically by each article's `date` for exactly this reason — so the arrows walk the collection from earliest (1841) to latest (2013) rather than in whatever order rows happened to be entered. Each article's own child image rows stay grouped directly beneath it in the file (matched by `image_parent_id`, not by position) purely for human readability when browsing the CSV directly; the plugin's filter already excludes them from the ordering regardless of where they sit.

**Keyboard shortcuts:** `browse-buttons.html` also wires left/right arrow keys to the `«`/`»` article navigation — but only when nothing else is open. It checks for the compound-item modal gallery first and clicks `.prev-child-button`/`.next-child-button` instead if it's open, and it deliberately does *nothing* if the full-screen Spotlight viewer is open (`isSpotlightModalShown()` guards that case with an empty branch). That's not a gap — Spotlight's own bundle registers its own `keydown` listener on `window` for the same arrow keys (confirmed directly in `assets/lib/spotlight.bundle.js`), so it already flips between this article's images on its own; the empty branch exists specifically to stop `browse-buttons.html` from *also* reacting to the same keypress and navigating to a different article underneath the open viewer.

---

## File Summary

| File | Role |
|---|---|
| `_layouts/item/compound_object.html` | Main page layout; queries children, renders two-column view, wires buttons |
| `_includes/item/compound-gallery.html` | Renders the child image records as a clickable gallery; wraps them in `.spotlight-group` with hidden links so the full-screen viewer can navigate between them |
| `assets/lib/spotlight.bundle.js` | Third-party full-screen lightbox library; groups `.spotlight` elements inside the closest `.spotlight-group` ancestor; has its own arrow-key navigation |
| `_includes/item/browse-buttons.html` | Renders the `«`/`»` article-to-article buttons; wires arrow keys, deferring to the full-screen viewer or modal gallery when either is open |
| `_plugins/cb_page_gen.rb` | Jekyll plugin; computes each item's `previous_item`/`next_item` from its position in the filtered metadata CSV |
| `_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv` | Master metadata; parent and child rows that define the compound object structure, kept sorted chronologically by article `date` so row order drives `«`/`»` browse order |
| `objects/<article_id>/<filename>.png` | Scanned page images served as static files |
