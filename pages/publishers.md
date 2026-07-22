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
{%- assign current_letter = "~unset~" -%}
{%- for g in groups -%}
{%- assign pub_name = g.name | strip -%}
{%- assign letter = pub_name | upcase | slice: 0,1 -%}
{%- assign alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" -%}
{%- unless letter != "" and alpha contains letter -%}{%- assign letter = "#" -%}{%- endunless -%}
{%- if letter != current_letter -%}
{% unless current_letter == "~unset~" %}
</div>
{% endunless %}
<h2 id="pub-{{ letter }}" class="mt-5 border-bottom pb-1">{{ letter }}</h2>
<div class="accordion mb-2">
{%- assign current_letter = letter -%}
{%- endif -%}
{%- assign first_item = g.items | first -%}
{%- assign sn_entry = sn_data | where: 'article_id', first_item.article_id | first -%}
{%- if sn_entry == nil or sn_entry.source_note == "" -%}
{%- assign sn_entry = sn_data | where: 'publication', pub_name | first -%}
{%- endif -%}
{%- assign desc_text = "" -%}
{%- if sn_entry.source_note and sn_entry.source_note != "" -%}
{%- assign desc_text = sn_entry.source_note -%}
{%- elsif first_item.document_intro and first_item.document_intro != "" -%}
{%- assign desc_text = first_item.document_intro -%}
{%- endif -%}
{%- assign pid = pub_name | slugify | append: '-' | append: forloop.index -%}
<div class="accordion-item">
<h3 class="accordion-header h5" id="heading-{{ pid }}">
<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{{ pid }}" aria-expanded="false" aria-controls="collapse-{{ pid }}">
{{ pub_name }} <span class="text-muted fw-normal small ms-2">({{ g.items | size }} article{% if g.items.size != 1 %}s{% endif %})</span>
</button>
</h3>
<div id="collapse-{{ pid }}" class="accordion-collapse collapse" aria-labelledby="heading-{{ pid }}">
<div class="accordion-body">
<ul class="list-group list-group-flush mb-0">
{%- assign sorted = g.items | sort: 'date' -%}
{%- for it in sorted -%}
{%- assign item_url = '/items/' | append: it.objectid | downcase | append: '.html' | relative_url -%}
{%- assign _t = it.title -%}
{%- assign _t_last = _t | slice: -1 -%}

{%- assign _loc = it.publisher_location | default: "" | strip -%}
{%- assign _yr = "" -%}
{%- if it.date and it.date != "" -%}{%- assign _yr = it.date | slice: 0,4 -%}{%- endif -%}

{%- assign _meta = "" -%}
{%- if pub_name != "" -%}{%- assign _meta = _meta | append: pub_name -%}{%- endif -%}
{%- if _loc != "" -%}
  {%- if _meta != "" -%}{%- assign _meta = _meta | append: ", " -%}{%- endif -%}
  {%- assign _meta = _meta | append: _loc -%}
{%- endif -%}
{%- if _yr != "" -%}
  {%- if _meta != "" -%}{%- assign _meta = _meta | append: ", " -%}{%- endif -%}
  {%- assign _meta = _meta | append: _yr -%}
{%- endif -%}

{%- if _t_last == '"' or _t_last == '"' -%}
  {%- assign _tlen_m1 = _t.size | minus: 1 -%}
  {%- assign _t_body = _t | slice: 0, _tlen_m1 -%}
  {%- if _meta != "" -%}
<li class="list-group-item px-0"><a href="{{ item_url }}">{{ _t_body }}</a>,{{ _t_last }} {{ _meta }}</li>
  {%- else -%}
<li class="list-group-item px-0"><a href="{{ item_url }}">{{ _t_body }}</a>{{ _t_last }}</li>
  {%- endif -%}
{%- else -%}
  {%- if _meta != "" -%}
<li class="list-group-item px-0"><a href="{{ item_url }}">{{ _t }}</a>, {{ _meta }}</li>
  {%- else -%}
<li class="list-group-item px-0"><a href="{{ item_url }}">{{ _t }}</a></li>
  {%- endif -%}
{%- endif -%}
{%- endfor -%}
</ul>
{%- if desc_text != "" -%}
<div class="mt-3 pt-3 border-top" style="font-size:0.95em; line-height:1.6; color:#495057;">
<h4 class="text-uppercase text-muted mb-1" style="font-size:0.75em; letter-spacing:.04em;">Source Note</h4>
{{ desc_text | replace: "End Notes", "<strong>End Notes</strong>" | paragraphize: "mb-2" }}
</div>
{%- endif -%}
</div>
</div>
</div>
{%- endfor -%}
</div>
{%- endif -%}
