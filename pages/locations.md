---
layout: page
title: Locations
permalink: /locations.html
---

{%- assign all = site.data[site.metadata] -%}
{%- assign compounds = all | where: 'display_template', 'compound_object' | sort: 'publisher_location' -%}

<p class="text-muted mb-3">{{ compounds.size }} articles &middot; organized by country and region</p>

<div class="mb-5 small">
Jump to:
<a href="#australia">Australia</a> &middot;
<a href="#canada">Canada</a> &middot;
<a href="#france">France</a> &middot;
<a href="#germany">Germany</a> &middot;
<a href="#india">India</a> &middot;
<a href="#new-zealand">New Zealand</a> &middot;
<a href="#ussr">USSR</a> &middot;
<a href="#united-kingdom">United Kingdom and Ireland</a> &middot;
<a href="#united-states">United States</a> &middot;
<a href="#unpublished">Unpublished</a>
</div>

{%- comment %} ── Country arrays ──────────────────────────────────────────────── {%- endcomment %}
{%- assign australia_arts = compounds | where_exp: 'item', 'item.publisher_location contains ", Australia"' -%}
{%- assign canada_arts    = compounds | where_exp: 'item', 'item.publisher_location contains ", Canada"' -%}
{%- assign france_arts    = compounds | where_exp: 'item', 'item.publisher_location contains ", France"' -%}
{%- assign germany_arts   = compounds | where_exp: 'item', 'item.publisher_location contains ", Germany"' -%}
{%- assign india_arts     = compounds | where_exp: 'item', 'item.publisher_location contains "Maharashtra"' -%}
{%- assign nz_arts        = compounds | where_exp: 'item', 'item.publisher_location contains "New Zealand"' -%}
{%- assign ussr_arts      = compounds | where_exp: 'item', 'item.publisher_location contains "USSR"' -%}
{%- assign uk_arts        = compounds | where_exp: 'item', 'item.publisher_location contains "United Kingdom"' -%}
{%- assign unpub_arts     = compounds | where_exp: 'item', 'item.publisher_location == ""' -%}

{%- comment %} ── AUSTRALIA ────────────────────────────────────────────────────── {%- endcomment %}
<h2 id="australia" class="mt-5 border-bottom pb-1">Australia <span class="text-muted fw-normal fs-6">({{ australia_arts.size }})</span></h2>
{%- assign aus_states = ", New South Wales|, Queensland|, South Australia|, Tasmania|, Victoria|, Western Australia" | split: "|" -%}
{%- for sf in aus_states -%}
{%- assign sn = sf | remove_first: ", " -%}
{%- assign sc = 0 -%}
{%- for art in australia_arts -%}{%- if art.publisher_location contains sf -%}{%- assign sc = sc | plus: 1 -%}{%- endif -%}{%- endfor -%}
{%- if sc > 0 -%}
<h3 id="aus-{{ sn | slugify }}" class="h5 mt-4">{{ sn }}</h3>
<ul class="list-unstyled ps-3">
{%- for art in australia_arts -%}
{%- if art.publisher_location contains sf -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endif -%}
{%- endfor -%}
</ul>
{%- endif -%}
{%- endfor -%}

{%- comment %} ── CANADA ──────────────────────────────────────────────────────── {%- endcomment %}
<h2 id="canada" class="mt-5 border-bottom pb-1">Canada <span class="text-muted fw-normal fs-6">({{ canada_arts.size }})</span></h2>
{%- assign can_provs = ", Newfoundland|, Ontario|, Québec" | split: "|" -%}
{%- for sf in can_provs -%}
{%- assign sn = sf | remove_first: ", " -%}
{%- assign sc = 0 -%}
{%- for art in canada_arts -%}{%- if art.publisher_location contains sf -%}{%- assign sc = sc | plus: 1 -%}{%- endif -%}{%- endfor -%}
{%- if sc > 0 -%}
<h3 id="can-{{ sn | slugify }}" class="h5 mt-4">{{ sn }}</h3>
<ul class="list-unstyled ps-3">
{%- for art in canada_arts -%}
{%- if art.publisher_location contains sf -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endif -%}
{%- endfor -%}
</ul>
{%- endif -%}
{%- endfor -%}

{%- comment %} ── FRANCE ──────────────────────────────────────────────────────── {%- endcomment %}
<h2 id="france" class="mt-5 border-bottom pb-1">France <span class="text-muted fw-normal fs-6">({{ france_arts.size }})</span></h2>
<ul class="list-unstyled ps-3">
{%- for art in france_arts -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endfor -%}
</ul>

{%- comment %} ── GERMANY ─────────────────────────────────────────────────────── {%- endcomment %}
<h2 id="germany" class="mt-5 border-bottom pb-1">Germany <span class="text-muted fw-normal fs-6">({{ germany_arts.size }})</span></h2>
<ul class="list-unstyled ps-3">
{%- for art in germany_arts -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endfor -%}
</ul>

{%- comment %} ── INDIA ───────────────────────────────────────────────────────── {%- endcomment %}
<h2 id="india" class="mt-5 border-bottom pb-1">India <span class="text-muted fw-normal fs-6">({{ india_arts.size }})</span></h2>
<ul class="list-unstyled ps-3">
{%- for art in india_arts -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endfor -%}
</ul>

{%- comment %} ── NEW ZEALAND ─────────────────────────────────────────────────── {%- endcomment %}
<h2 id="new-zealand" class="mt-5 border-bottom pb-1">New Zealand <span class="text-muted fw-normal fs-6">({{ nz_arts.size }})</span></h2>
<ul class="list-unstyled ps-3">
{%- for art in nz_arts -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endfor -%}
</ul>

{%- comment %} ── USSR ────────────────────────────────────────────────────────── {%- endcomment %}
<h2 id="ussr" class="mt-5 border-bottom pb-1">USSR <span class="text-muted fw-normal fs-6">({{ ussr_arts.size }})</span></h2>
<ul class="list-unstyled ps-3">
{%- for art in ussr_arts -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endfor -%}
</ul>

{%- comment %} ── UNITED KINGDOM AND IRELAND ──────────────────────────────────── {%- endcomment %}
<h2 id="united-kingdom" class="mt-5 border-bottom pb-1">United Kingdom and Ireland <span class="text-muted fw-normal fs-6">({{ uk_arts.size }})</span></h2>
<ul class="list-unstyled ps-3">
{%- for art in uk_arts -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endfor -%}
</ul>

{%- comment %} ── UNITED STATES ────────────────────────────────────────────────── {%- endcomment %}
{%- assign intl_markers = ", Australia|, Canada|, France|, Germany|Maharashtra|New Zealand|USSR|United Kingdom" | split: "|" -%}
{%- assign us_count = 0 -%}
{%- for art in compounds -%}
{%- assign loc = art.publisher_location -%}
{%- unless loc == "" -%}
{%- assign is_intl = false -%}
{%- for marker in intl_markers -%}{%- if loc contains marker -%}{%- assign is_intl = true -%}{%- endif -%}{%- endfor -%}
{%- unless is_intl -%}{%- assign us_count = us_count | plus: 1 -%}{%- endunless -%}
{%- endunless -%}
{%- endfor -%}
<h2 id="united-states" class="mt-5 border-bottom pb-1">United States <span class="text-muted fw-normal fs-6">({{ us_count }})</span></h2>
{%- assign us_state_list = ", Arizona|, California|, Colorado|, Connecticut|, DC|, Georgia|, Hawaii|, Illinois|, Indiana|, Iowa|, Kansas|, Kentucky|, Louisiana|, Maine|, Maryland|, Massachusetts|, Michigan|, Minnesota|, Missouri|, Nebraska|, New Hampshire|, New Mexico|, New York|, North Carolina|, North Dakota|, Ohio|, Oklahoma|, Oregon|, Pennsylvania|, South Carolina|, Tennessee|, Texas|, Utah|, Vermont|, Virginia|, Washington|, Wisconsin" | split: "|" -%}
{%- for sf in us_state_list -%}
{%- assign sn = sf | remove_first: ", " -%}
{%- assign sc = 0 -%}
{%- for art in compounds -%}
{%- assign loc = art.publisher_location -%}
{%- unless loc == "" -%}
{%- assign is_intl = false -%}
{%- for marker in intl_markers -%}{%- if loc contains marker -%}{%- assign is_intl = true -%}{%- endif -%}{%- endfor -%}
{%- unless is_intl -%}{%- if loc contains sf -%}{%- assign sc = sc | plus: 1 -%}{%- endif -%}{%- endunless -%}
{%- endunless -%}
{%- endfor -%}
{%- if sc > 0 -%}
<h3 id="us-{{ sn | slugify }}" class="h5 mt-4">{{ sn }}</h3>
<ul class="list-unstyled ps-3">
{%- for art in compounds -%}
{%- assign loc = art.publisher_location -%}
{%- unless loc == "" -%}
{%- assign is_intl = false -%}
{%- for marker in intl_markers -%}{%- if loc contains marker -%}{%- assign is_intl = true -%}{%- endif -%}{%- endfor -%}
{%- unless is_intl -%}
{%- if loc contains sf -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.publisher_location != "" %}, {{ art.publisher_location }}{% endif %}{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endif -%}
{%- endunless -%}
{%- endfor -%}
</ul>
{%- endif -%}
{%- endfor -%}

{%- comment %} ── UNPUBLISHED ──────────────────────────────────────────────────── {%- endcomment %}
<h2 id="unpublished" class="mt-5 border-bottom pb-1">Unpublished <span class="text-muted fw-normal fs-6">({{ unpub_arts.size }})</span></h2>
<ul class="list-unstyled ps-3">
{%- for art in unpub_arts -%}
{%- assign art_url = '/items/' | append: art.objectid | downcase | append: '.html' | relative_url -%}
{%- if art.reprint_type contains "original" -%}{%- assign rtype = "Original" -%}{%- assign rbadge = "bg-primary" -%}
{%- elsif art.reprint_type contains "direct" -%}{%- assign rtype = "Direct" -%}{%- assign rbadge = "bg-success" -%}
{%- elsif art.reprint_type contains "truncated" -%}{%- assign rtype = "Truncated" -%}{%- assign rbadge = "bg-secondary" -%}
{%- else -%}{%- assign rtype = art.reprint_type | capitalize -%}{%- assign rbadge = "bg-info" -%}{%- endif -%}
<li class="mb-1"><span class="badge {{ rbadge }} me-1">{{ rtype }}</span><a href="{{ art_url }}">{{ art.publication }}</a>{% if art.date %} ({{ art.date | slice: 0,4 }}){% endif %}</li>
{%- endfor -%}
</ul>
