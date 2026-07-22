---
title: Tropes Interpretive Essay
layout: page
permalink: /literary-tropes/
---

<h1 class="mb-3">{{ page.title }}</h1>

{% comment %}
  On this page (unlike the two-column article-page layout entity-panel.html
  was originally built for) there's no side column to put the entity panel
  in — it's a plain full-width block, so opening it pushes the whole essay
  down and can bury the reader's place. Override it here, page-scoped only,
  to float the same way doc-panel.html already does (fixed position, side
  of the viewport, mobile bottom-sheet fallback) rather than editing the
  shared include and risking the two-column article-page behavior.
{% endcomment %}
<style>
  .lw-tropes-page #entity-panel {
    position: fixed;
    top: 72px;
    left: 1.5rem;
    width: 290px;
    max-height: calc(100vh - 100px);
    overflow-y: auto;
    z-index: 1050;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18);
  }

  @media (max-width: 767px) {
    .lw-tropes-page #entity-panel {
      top: auto;
      bottom: 0;
      left: 0;
      right: 0;
      width: 100%;
      max-height: 70vh;
      border-radius: 8px 8px 0 0;
      box-shadow: 0 -4px 20px rgba(0,0,0,0.2);
    }
  }
</style>

<div class="lw-tropes-page">
{% include entity-panel.html %}

{% include doc-panel.html %}

{% include literary-tropes-essay.html %}
</div>
