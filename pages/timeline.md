---
title: Timeline
layout: page
permalink: /timeline.html
---

<h1 class="mb-3">{{ page.title }}</h1>
<p class="mb-4">This page organizes every article in the archive chronologically by publication date, grouped by year.</p>

{%- assign all = site.data[site.metadata] -%}
{%- assign compounds = all | where: 'display_template', 'compound_object' -%}
{%- assign dated = compounds | where_exp: 'item', 'item.date and item.date != ""' | sort: 'date' -%}
{%- assign undated = compounds | where_exp: 'item', 'item.date == nil or item.date == ""' -%}

{%- assign year_list = "" -%}
{%- for it in dated -%}
{%- assign y = it.date | slice: 0,4 -%}
{%- unless year_list contains y -%}{%- assign year_list = year_list | append: y | append: ';' -%}{%- endunless -%}
{%- endfor -%}
{%- assign uniqueYears = year_list | split: ';' -%}

<p class="text-muted mb-3">{{ compounds.size }} articles &middot; {{ uniqueYears | first }}&ndash;{{ uniqueYears | last }}</p>

<div class="mb-5 small">
Jump to:
{%- for y in uniqueYears %} <a href="#y{{ y }}">{{ y }}</a>{% unless forloop.last %} &middot;{% endunless %}{% endfor -%}
{%- if undated.size > 0 %} &middot; <a href="#undated">Undated</a>{% endif %}
</div>

{%- for y in uniqueYears -%}
<h2 id="y{{ y }}" class="mt-5 border-bottom pb-1">{{ y }}</h2>
<div class="row g-3 mb-4">
{%- assign inYear = dated | where_exp: 'item', 'item.date contains y' -%}
{%- for it in inYear -%}
{%- include timeline-card.html item=it -%}
{%- endfor -%}
</div>
{%- endfor -%}

{%- if undated.size > 0 -%}
<h2 id="undated" class="mt-5 border-bottom pb-1">Undated</h2>
<div class="row g-3 mb-4">
{%- for it in undated -%}
{%- include timeline-card.html item=it -%}
{%- endfor -%}
</div>
{%- endif -%}
