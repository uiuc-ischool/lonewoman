---
layout: page
title: Publishers
permalink: /publishers/
---

{%- assign all = site.data[site.metadata] -%}
{%- assign articles = all | where_exp: 'item', 'item.display_template == "compound_object"' -%}
{%- assign with_pub = articles | where_exp: 'item', 'item.publication != ""' -%}
{%- assign groups = with_pub | group_by: 'publication' | sort: 'name' -%}
{%- assign sn_data = site.data.article_sourcenotes -%}

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
{%- assign first_item = g.items | first -%}
{%- assign sn_entry = sn_data | where: 'article_id', first_item.article_id | first -%}
{%- if sn_entry == nil or sn_entry.source_note == "" -%}
{%- assign sn_entry = sn_data | where: 'publication', pub_name | first -%}
{%- endif -%}
<section class="mb-4">
<h3 class="h5 mb-1">{{ pub_name }} <span class="text-muted fw-normal">({{ g.items | size }} article{% if g.items.size != 1 %}s{% endif %})</span></h3>
{%- if sn_entry.source_note and sn_entry.source_note != "" -%}
<p class="text-muted mb-2" style="font-size:0.82em; line-height:1.5;">{{ sn_entry.source_note }}</p>
{%- endif -%}
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
