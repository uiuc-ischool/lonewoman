---
layout: page
title: Tropes
permalink: /subjects.html
---

{%- assign all = site.data[site.metadata] -%}
{%- assign compounds = all | where: 'display_template', 'compound_object' -%}
{%- assign sorted_compounds = compounds | sort: 'date' -%}
{%- assign troped = compounds | where_exp: 'item', 'item.tropes != ""' -%}
{%- assign trope_string = troped | map: 'tropes' | join: "; " -%}
{%- assign all_tropes = trope_string | split: "; " | uniq | sort -%}

<p class="text-muted mb-3">{{ all_tropes.size }} tropes across {{ compounds.size }} articles. Jump to a trope section below.</p>

{% include trope-barcharts.html %}

{% include trope-sparklines.html %}

{%- for trope in all_tropes -%}
{%- assign trope_slug = trope | slugify -%}
{%- assign trope_count = 0 -%}
{%- for item in compounds -%}
{%- if item.tropes contains trope -%}
{%- assign trope_count = trope_count | plus: 1 -%}
{%- endif -%}
{%- endfor -%}
<section id="trope-{{ trope_slug }}" class="mb-5">
<h2 class="h4 border-bottom pb-1 mt-4">{{ trope }} <span class="text-muted fw-normal fs-6">({{ trope_count }} article{% if trope_count != 1 %}s{% endif %})</span></h2>
<ul class="list-unstyled ps-2 mb-1">
{%- for item in sorted_compounds -%}
{%- if item.tropes contains trope -%}
{%- assign item_url = '/items/' | append: item.objectid | downcase | append: '.html' | relative_url -%}
<li class="mb-1"><a href="{{ item_url }}">{{ item.title }}</a> &mdash; {{ item.publication }}{% if item.date %}, {{ item.date | slice: 0,4 }}{% endif %}</li>
{%- endif -%}
{%- endfor -%}
</ul>
<p class="small mb-0"><a href="#trope-cloud" class="text-muted">↑ Back to cloud</a></p>
</section>
{%- endfor -%}
