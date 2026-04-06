---
layout: page
title: Publishers
permalink: /publishers/
---

{%- assign all = site.data[site.metadata] -%}

{%- comment -%}
  Build the article list manually with strip+downcase comparison to avoid
  missed matches from whitespace in the CSV's image_display_template field.
{%- endcomment -%}
{%- assign articles = "" | split: "" -%}
{%- for item in all -%}
  {%- assign tmpl = item.image_display_template | strip | downcase -%}
  {%- assign pub = item.publication | strip -%}
  {%- if tmpl == "compound_object" and pub != "" -%}
    {%- assign articles = articles | push: item -%}
  {%- endif -%}
{%- endfor -%}

{%- assign groups = articles | group_by: 'publication' | sort: 'name' -%}

{%- if groups.size == 0 -%}
<p><em>No publications found.</em></p>
{%- else -%}

  <p class="text-muted mb-1">{{ groups.size }} publications &middot; {{ articles.size }} articles</p>

  {%- comment -%} A–Z jump links {%- endcomment -%}
  <p class="small mb-4">
    Jump to:&nbsp;
    {%- assign seen = "" -%}
    {%- for g in groups -%}
      {%- assign letter = g.name | strip | upcase | slice: 0,1 -%}
      {%- unless seen contains letter -%}
        <a href="#pub-{{ letter }}">{{ letter }}</a>{% unless forloop.last %} &middot; {% endunless %}
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
      <ul class="list-unstyled ps-3 mb-0">
        {%- assign sorted_items = g.items | sort: 'date' -%}
        {%- for it in sorted_items -%}
          {%- comment -%} Jekyll slugify (pretty mode) lowercases the objectid for the filename {%- endcomment -%}
          {%- assign item_url = '/items/' | append: it.objectid | downcase | append: '.html' | relative_url -%}
          <li class="mb-1">
            {%- if it.author and it.author != "" -%}{{ it.author }}, {%- endif -%}
            <a href="{{ item_url }}">{{ it.title }}</a>,
            {{ pub_name }}{% if it.date %}, {{ it.date | slice: 0,4 }}{% endif %}
          </li>
        {%- endfor -%}
      </ul>
    </section>
  {%- endfor -%}

{%- endif -%}
