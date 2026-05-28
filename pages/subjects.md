---
layout: page
title: Tropes
permalink: /subjects.html
---

{%- assign all = site.data[site.metadata] -%}
{%- assign compounds = all | where: 'display_template', 'compound_object' -%}
{%- assign sorted_compounds = compounds | sort: 'date' -%}

<p class="text-muted mb-3">14 tropes across {{ compounds.size }} articles. Jump to a trope section below.</p>

<script>
/* Single D3 loader — both includes call _whenD3(fn) to register callbacks */
window._d3q = [];
window._whenD3 = function(fn) {
  if (typeof d3 !== 'undefined') { fn(); return; }
  window._d3q.push(fn);
  if (!window._d3loading) {
    window._d3loading = true;
    var s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js';
    s.onload = function() {
      window._d3q.forEach(function(f) { f(); });
      window._d3q = [];
    };
    document.head.appendChild(s);
  }
};
</script>

{% include trope-sparklines.html %}

{% include trope-barcharts.html %}

{%- for trope in site.data.tropes -%}
{%- unless trope.label == "Captivity" -%}
{%- assign trope_label = trope.label -%}
{%- assign trope_slug = trope.label | slugify -%}
{%- assign trope_count = 0 -%}
{%- for item in compounds -%}
{%- if item.tropes contains trope_label -%}
{%- assign trope_count = trope_count | plus: 1 -%}
{%- endif -%}
{%- endfor -%}
<section id="trope-{{ trope_slug }}" class="mb-5">
<h2 class="h4 border-bottom pb-1 mt-4">{{ trope.label }} <span class="text-muted fw-normal fs-6">({{ trope_count }} article{% if trope_count != 1 %}s{% endif %})</span></h2>
<ul class="list-unstyled ps-2 mb-1">
{%- for item in sorted_compounds -%}
{%- if item.tropes contains trope_label -%}
{%- assign item_url = '/items/' | append: item.objectid | downcase | append: '.html' | relative_url -%}
<li class="mb-1"><a href="{{ item_url }}">{{ item.title }}</a> &mdash; {{ item.publication }}{% if item.date %}, {{ item.date | slice: 0,4 }}{% endif %}</li>
{%- endif -%}
{%- endfor -%}
</ul>
<p class="small mb-0"><a href="#" class="text-muted">↑ Back to top</a></p>
</section>
{%- endunless -%}
{%- endfor -%}
