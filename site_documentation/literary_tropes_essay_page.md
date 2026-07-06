# Literary Tropes Essay Page

The Literary Tropes page (`/literary-tropes/`) presents a scholarly essay by project editor Professor Sara Schwebel (2016) analyzing the 14 interpretive tropes used in press accounts of the Lone Woman. The text and images were ported directly from the previous version of the site. For the current archive, the essay was wired into the data infrastructure: named people, places, organizations, and ships in the prose are linked to entity descriptions from the archive's entity CSVs, and citations to specific archival documents open a floating image-gallery panel tied to the archive's digitized scans.

**URL:** `/literary-tropes/`  
**Page file:** `pages/literary-tropes.md`

---

## Page Structure

`pages/literary-tropes.md` is minimal — it just includes three components in order:

```
{% include entity-panel.html %}
{% include doc-panel.html %}
{% include literary-tropes-essay.html %}
```

No special front matter flags are needed beyond `layout: page`.

---

## Essay Content (`_includes/literary-tropes-essay.html`)

The essay HTML was taken from the old website and reformatted for Jekyll. It contains:

- Introductory prose contextualizing the archive's interpretive approach
- 14 trope sections (some archive-specific, some universal settler-colonial tropes)
- Floated figures with images from `assets/img/literary-tropes/`
- Superscript footnote references linking to an endnotes section
- A byline (Sara L. Schwebel, PhD, February 1, 2016) and acknowledgment

**Two types of interactive annotations were added when porting the essay to this site:**

### Entity links

Named people, places, organizations, and ships in the essay text are wrapped in:

```html
<span class="entity-link" data-entity-key="gni" data-entity-type="person">George Nidever</span>
```

For group annotations (multiple entities sharing the same text):
```html
<span class="entity-link" data-entity-keys='["gni","cdi","col","cook","msh","poli","nsk","hva"]'>the hunting party</span>
```

A click listener at the bottom of the essay file routes these to the entity panel:

```js
essay.addEventListener('click', function (e) {
  var link = e.target.closest('.entity-link');
  if (link.dataset.entityKeys) {
    window.openGroupPanel(JSON.parse(link.dataset.entityKeys));
  } else {
    window.openEntityPanel(link.dataset.entityKey, link.dataset.entityType || '');
  }
});
```

Entity data comes from the same pipeline used on article pages: entity CSVs → `utilities/build_entities_json.py` → `_data/entities.json` → `assets/js/entity-data.js` (Jekyll-processed, sets `window.ENTITY_DATA`). See `site_documentation/article_page_transcripts_tropes_entities.md` for the full entity data pipeline.

### Document links

Citations to specific archival documents in the essay are marked as:

```html
<a href="{{ '/items/thebostonatlas1847__...' | relative_url }}" class="doc-link"
   data-doc-id="thebostonatlas1847__thebostonatlas1847_reprint__original">
  <em>Boston Atlas</em>
</a>
```

Clicking a `.doc-link` intercepts the navigation and opens the document preview panel instead.

---

## Entity Panel (`_includes/entity-panel.html`)

The same entity panel used on article pages is included here. On this page it is styled as `position: sticky; top: 1rem` (defined in `literary-tropes-essay.html`'s CSS block) so it appears inline below the navigation bar rather than overlaying a two-column layout. The panel logic and data source are identical to the article page version — see `site_documentation/article_page_transcripts_tropes_entities.md`.

---

## Document Preview Panel (`_includes/doc-panel.html`)

A floating panel that appears when a `.doc-link` in the essay is clicked. It shows article metadata and a navigable image gallery of the digitized scans, with a link to the full article page in the archive.

**What it shows:**
- Publication name, date, and author
- Article title
- Image gallery (the digitized scan pages, with previous/next navigation and a page counter)
- "Open full article →" link to `/items/<objectid>.html`

**How it works:**

A hardcoded `DOCS` registry in the panel's `<script>` block maps each lowercase `objectid` to its metadata and image paths:

```js
var DOCS = {
  'thebostonatlas1847__thebostonatlas1847_reprint__original': {
    title: '"A Female Crusoe"',
    pub: 'Boston Atlas',
    date: 'January 7, 1847',
    url: BASE + '/items/thebostonatlas1847__...',
    images: [
      'objects/TheBostonAtlas1847/TheBostonAtlas1847_DigSur_1.png',
      ...
    ]
  },
  ...
};
```

**The 8 documents registered** are those cited directly in the essay:
- *Boston Atlas* (1847) — the original "jump overboard" article
- 6 direct reprints of the Boston Atlas article: *Littell's Living Age*, New York Evening Express, Philadelphia Public Ledger, Edgefield (SC) Advertiser, Wisconsin Herald, Honolulu Polynesian (all 1847)
- George Nidever's *Life and Adventures* memoir (1878, Bancroft Library)

`window.openDocPanel(docId)` is a global function that populates and shows the panel. It is called by the `.doc-link` click handler.

**Keyboard support:** Escape closes the panel; left/right arrow keys navigate images.  
**Mobile:** panel slides up from the bottom of the screen as a full-width sheet.

**Important note:** The `DOCS` registry is hardcoded, not generated from the metadata CSV. If new document links are added to the essay in future, each referenced document must also be added manually to the `DOCS` object in `doc-panel.html`, including the correct image file paths.

---

## File Summary

| File | Role |
|---|---|
| `pages/literary-tropes.md` | Page stub; includes the three components below |
| `_includes/literary-tropes-essay.html` | Essay text and images (ported from old site); entity links and doc links wired in |
| `_includes/entity-panel.html` | Entity description panel, shared with article pages |
| `_includes/doc-panel.html` | Document preview panel with hardcoded registry of 8 cited articles |
| `assets/js/entity-data.js` | Jekyll-processed bridge that sets `window.ENTITY_DATA` from `_data/entities.json` |
| `assets/js/entity-panel.js` | Panel logic for `openEntityPanel()` and `openGroupPanel()` |
| `assets/img/literary-tropes/` | Images used as figures in the essay (ported from old site) |
| `_data/entities.json` | Entity lookup built by `utilities/build_entities_json.py` from entity CSVs |
