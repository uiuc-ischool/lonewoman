---
layout: page
title: Document Groups
permalink: /groups/
use_reprint_maps: true
---

{%- assign all = site.data[site.metadata] -%}
{%- assign compounds = all | where: 'display_template', 'compound_object' -%}
{%- assign originals = compounds | where_exp: 'item', 'item.reprint_type contains "original"' | sort: 'date' -%}

{%- if originals.size == 0 -%}
<p><em>No document groups found.</em></p>
{%- else -%}
<p class="text-muted mb-4">{{ originals.size }} document groups &middot; each Original followed by its Reprints</p>
{%- assign current_year = "" -%}
{%- for orig in originals -%}
{%- assign year = orig.date | slice: 0,4 -%}
{%- if year != current_year -%}
<h2 id="year-{{ year }}" class="mt-5 border-bottom pb-1">{{ year }}</h2>
{%- assign current_year = year -%}
{%- endif -%}
{%- assign gid = orig.group_reprint_id -%}
{%- assign group_items = compounds | where: 'group_reprint_id', gid | sort: 'date' -%}
{%- assign reprint_count = group_items.size | minus: 1 -%}
{%- assign orig_url = '/items/' | append: orig.objectid | downcase | append: '.html' | relative_url -%}
<details class="map-group mb-4" id="group-{{ orig.objectid | downcase }}">
<summary>
<h3 class="h5 mb-1 d-inline">
<a href="{{ orig_url }}">{{ orig.title }}</a>
<span class="text-muted fw-normal small">
({{ reprint_count }} reprint{% if reprint_count != 1 %}s{% endif %})
</span>
</h3>
<span class="map-toggle-icon">▶</span>
</summary>
<p class="text-muted small mb-2">
{{ orig.publication }}{% if orig.publisher_location != "" %}, {{ orig.publisher_location }}{% endif %}
{% if orig.date %} &middot; {{ orig.date | slice: 0,4 }}{% endif %}
{% if orig.author != "" %} &mdash; {{ orig.author }}{% endif %}
</p>
{% if reprint_count > 0 %}
<ul class="list-unstyled ps-3 mb-2">
{% for it in group_items %}
{% unless it.reprint_type contains "original" %}
{%- assign item_url = '/items/' | append: it.objectid | downcase | append: '.html' | relative_url -%}
{%- if it.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}
{%- elsif it.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}
{%- else -%}{%- assign rtype = it.reprint_type | capitalize -%}{%- endif -%}
<li class="mb-1">
<span class="badge bg-secondary me-1">{{ rtype }}</span>
<a href="{{ item_url }}">{{ it.publication }}</a>
{% if it.publisher_location != "" %}, {{ it.publisher_location }}{% endif %}
{% if it.date %} ({{ it.date | slice: 0,4 }}){% endif %}
</li>
{% endunless %}
{% endfor %}
</ul>
{% endif %}
{% include reprint-map.html group_id=orig.group_reprint_id %}
</details>
{%- endfor -%}
{%- endif -%}
