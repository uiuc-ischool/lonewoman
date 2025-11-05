---
layout: page
title: Document Groups
permalink: /groups/
---

{%- comment -%}
Lists each document group, ordering items:
Original → Direct Reprint → Truncated Reprint → (others)
Requires CSV fields: objectid, title, group_id, version_type, creator
{%- endcomment -%}

{%- assign items = site.data[site.metadata] | where_exp: 'r','r.group_id' -%}
{%- if items.size == 0 -%}
<p><em>No document groups found yet.</em></p>
{%- else -%}
  {%- assign group_ids = items | map: 'group_id' | uniq | sort -%}

  <p class="mb-4">This index lists document groups comprised of an Original and its reprints.</p>

  <div class="cb-group-list">
  {%- for gid in group_ids -%}
    {%- assign group = items | where: "group_id", gid -%}
    {%- assign originals = group | where: "version_type", "Original" -%}
    {%- assign original = originals | first -%}
    {%- assign group_heading = original.title | default: gid -%}

    <section class="mb-4 pb-3 border-bottom">
      <h3 class="h5">{{ group_heading }}</h3>
      <p class="text-muted small mb-2">
        <strong>Group ID:</strong> {{ gid }} • <strong>Total:</strong> {{ group.size }}
      </p>

      <ul class="mb-0">
        {%- assign order = "Original|Direct Reprint|Truncated Reprint" | split: "|" -%}

        {%- comment -%} preferred order passes {%- endcomment -%}
        {%- for t in order -%}
          {%- for it in group -%}
            {%- if it.version_type == t -%}
              <li>
                {{ it.version_type }}:
                <a href="{{ '/items/' | append: it.objectid | append: '.html' | relative_url }}">"{{ it.title}},"</a>
                {%- if it.creator %} {{ it.creator }}{%- endif -%}
              </li>
            {%- endif -%}
          {%- endfor -%}
        {%- endfor -%}

        {%- comment -%} anything not in the preferred list {%- endcomment -%}
        {%- for it in group -%}
          {%- unless order contains it.version_type -%}
            <li>
              {{ it.version_type | default: 'Related' }}:
              <a href="{{ '/items/' | append: it.objectid | append: '.html' | relative_url }}">"{{ it.title}},"</a>
              {%- if it.creator %} {{ it.creator }}{%- endif -%}
            </li>
          {%- endunless -%}
        {%- endfor -%}
      </ul>
    </section>
  {%- endfor -%}
  </div>
{%- endif -%}
