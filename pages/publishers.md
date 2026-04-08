---
layout: page
title: Publishers
permalink: /publishers/
---

{%- assign all = site.data[site.metadata] -%}
{%- assign articles = all | where_exp: 'item', 'item.image_display_template contains "compound_object"' -%}
{%- assign with_pub = articles | where_exp: 'item', 'item.publication != ""' -%}
{%- assign groups = with_pub | group_by: 'publication' | sort: 'name' -%}

{%- if groups.size == 0 -%}
<p><em>No publications found.</em></p>
{%- else -%}
<p class="text-muted mb-4">{{ groups.size }} publications &middot; {{ with_pub.size }} articles</p>
{%- assign current_letter = "" -%}
{%- for g in groups -%}
{%- assign pub_name = g.name | strip -%}
{%- assign letter = pub_name | upcase | slice: 0,1 -%}
{%- assign alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" -%}
{%- unless alpha contains letter -%}{%- assign letter = "#" -%}{%- endunless -%}
{%- if letter != current_letter -%}
<h2 id="pub-{{ letter }}" class="mt-5 border-bottom pb-1">{{ letter }}</h2>
{%- assign current_letter = letter -%}
{%- endif -%}
<section class="mb-4">
<h3 class="h5 mb-1">{{ pub_name }} <span class="text-muted fw-normal">({{ g.items | size }} article{% if g.items.size != 1 %}s{% endif %})</span></h3>
<ul class="list-unstyled ps-3 mb-0">
{%- assign sorted = g.items | sort: 'date' -%}
{%- for it in sorted -%}
{%- assign item_url = '/items/' | append: it.objectid | downcase | append: '.html' | relative_url -%}
<li class="mb-1"><a href="{{ item_url }}">{{ it.title }}</a>, {{ pub_name }}{% if it.publisher_location != "" %}, {{ it.publisher_location }}{% endif %}{% if it.date %}, {{ it.date | slice: 0,4 }}{% endif %}</li>
{%- endfor -%}
</ul>
</section>
{%- endfor -%}
{%- endif -%}
