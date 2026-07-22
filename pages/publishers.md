---
layout: page
title: Publishers
permalink: /publishers/
---

<h1 class="mb-3">{{ page.title }}</h1>

{%- assign all = site.data[site.metadata] -%}
{%- assign articles = all | where_exp: 'item', 'item.display_template == "compound_object"' -%}
{%- assign with_pub = articles | where_exp: 'item', 'item.publication != ""' -%}
{%- assign groups = with_pub | group_by: 'publication' | sort: 'name' -%}
{%- assign sn_data = site.data.article_sourcenotes -%}

{%- if groups.size == 0 -%}
<p><em>No publications found.</em></p>
{%- else -%}
<p class="text-muted mb-4">{{ groups.size }} publications &middot; {{ with_pub.size }} articles</p>

{%- comment -%}
  Manuscripts (identified by publication name) and other non-periodical items
  with no real publisher name are pulled out of the alphabetical scheme into
  their own section, rather than alphabetizing as "#" or hiding under "M".
{%- endcomment -%}
{%- assign alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" -%}
{%- assign special_names = "" -%}
{%- for g in groups -%}
{%- assign pn = g.name | strip -%}
{%- assign ltr = pn | upcase | slice: 0,1 -%}
{%- assign is_special = false -%}
{%- unless ltr != "" and alpha contains ltr -%}{%- assign is_special = true -%}{%- endunless -%}
{%- if pn contains "Manuscript" -%}{%- assign is_special = true -%}{%- endif -%}
{%- if is_special -%}{%- assign special_names = special_names | append: pn | append: "|||" -%}{%- endif -%}
{%- endfor -%}

<h2 id="pub-manuscripts" class="mt-5 border-bottom pb-1">Manuscripts and Non-Periodical Texts</h2>
<div class="accordion mb-2">
{%- for g in groups -%}
{%- assign pub_name = g.name | strip -%}
{%- assign _key = pub_name | append: "|||" -%}
{%- unless special_names contains _key -%}{%- continue -%}{%- endunless -%}
{%- include publisher-accordion-item.html group=g pub_name=pub_name sn_data=sn_data pid_prefix="ms" index=forloop.index -%}
{%- endfor -%}
</div>

<h2 class="mt-5 mb-3 text-uppercase text-muted" style="font-size:0.85em; letter-spacing:.05em;">Periodical Sources</h2>
{%- assign current_letter = "~unset~" -%}
{%- for g in groups -%}
{%- assign pub_name = g.name | strip -%}
{%- assign _key = pub_name | append: "|||" -%}
{%- if special_names contains _key -%}{%- continue -%}{%- endif -%}
{%- assign letter = pub_name | upcase | slice: 0,1 -%}
{%- unless letter != "" and alpha contains letter -%}{%- assign letter = "#" -%}{%- endunless -%}
{%- if letter != current_letter -%}
{% unless current_letter == "~unset~" %}
</div>
{% endunless %}
<h3 id="pub-{{ letter }}" class="mt-4 pb-1 border-bottom">{{ letter }}</h3>
<div class="accordion mb-2">
{%- assign current_letter = letter -%}
{%- endif -%}
{%- include publisher-accordion-item.html group=g pub_name=pub_name sn_data=sn_data pid_prefix="ps" index=forloop.index -%}
{%- endfor -%}
</div>
{%- endif -%}
