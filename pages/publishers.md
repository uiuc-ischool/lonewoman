---
layout: page
title: Publishers
permalink: /publishers/
---

{%- comment -%}
Browse articles grouped by publication, A→Z.
Uses the `publication` field from the metadata CSV.
Only shows compound_object (article-level) records — not individual image sub-items.
{%- endcomment -%}

{%- assign all = site.data[site.metadata] -%}

{%- comment -%} Keep only article-level compound objects that have a publication name {%- endcomment -%}
{%- assign articles = all | where: "display_template", "compound_object" -%}
{%- assign with_pub = articles | where_exp: 'r', 'r.publication and r.publication != ""' -%}

{%- comment -%} Group by publication and sort groups alphabetically {%- endcomment -%}
{%- assign groups = with_pub | group_by: 'publication' | sort: 'name' -%}

{%- if groups.size == 0 -%}
<p><em>No publications found.</em></p>
{%- else -%}

  <p class="text-muted mb-1">{{ groups.size }} publications, {{ with_pub.size }} articles total</p>

  {%- comment -%} A–Z jump links {%- endcomment -%}
  <p class="small mb-4">
    Jump to:&nbsp;
    {%- assign seen = "" -%}
    {%- for g in groups -%}
      {%- assign letter = g.name | strip | upcase | slice: 0,1 -%}
      {%- unless seen contains letter -%}
        <a href="#pub-{{ letter }}">{{ letter }}</a>{% unless forloop.last %} · {% endunless %}
        {%- assign seen = seen | append: letter -%}
      {%- endunless -%}
    {%- endfor -%}
  </p>

  {%- assign current_letter = "" -%}
  {%- for g in groups -%}
    {%- assign pub_name = g.name | strip -%}
    {%- assign letter = pub_name | upcase | slice: 0,1 -%}

    {%- if letter != current_letter -%}
      <h2 id="pub-{{ letter }}" class="mt-5 border-bottom pb-1">{{ letter }}</h2>
      {%- assign current_letter = letter -%}
    {%- endif -%}

    <section class="mb-4">
      <h3 class="h5 mb-1">
        {{ pub_name }}
        <span class="text-muted fw-normal">({{ g.items | size }} article{% if g.items.size != 1 %}s{% endif %})</span>
      </h3>
      <ul class="mb-0">
        {%- assign sorted_items = g.items | sort: 'date' -%}
        {%- for it in sorted_items -%}
          {%- assign item_url = '/items/' | append: it.objectid | downcase | append: '.html' | relative_url -%}
          <li>
            <a href="{{ item_url }}">{{ it.title }}</a>
            {%- if it.date %} <span class="text-muted">({{ it.date | slice: 0,4 }})</span>{% endif -%}
            {%- if it.author and it.author != "" %} — <em>{{ it.author }}</em>{% endif -%}
          </li>
        {%- endfor -%}
      </ul>
    </section>
  {%- endfor -%}

{%- endif -%}
