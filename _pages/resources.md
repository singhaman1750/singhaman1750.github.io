---
layout: page
title: resources
permalink: /resources/
description: A curated library of papers, videos, tools and references for legged robotics.
nav: true
nav_order: 6
---

<!-- pages/resources.md -- the index is generated into _data/resources.yml by
     bin/sync_resources.py from the README of the Legged-Robots repo. -->

{% assign res = site.data.resources %}

{% if res.entries == nil or res.entries == empty %}

  <p>
    This page is built from the
    <a href="https://github.com/singhaman1750/Legged-Robots">Legged-Robots</a>
    repository. Run <code>python bin/sync_resources.py</code> before serving the
    site locally to generate it.
  </p>

{% else %}

<style type="text/css">
  .resource-index h2 {
    margin-top: 2.5rem;
  }
  .resource-index h3,
  .resource-index h4 {
    margin-top: 1.75rem;
  }
  .resource-index .card {
    height: 100%;
    transition: transform 0.2s ease-in-out;
  }
  .resource-index a.resource-link {
    text-decoration: none;
    color: inherit;
  }
  .resource-index a.resource-link:hover .card {
    transform: translateY(-2px);
    border-color: var(--global-theme-color);
  }
  .resource-index .card-title {
    font-size: 1rem;
    margin-bottom: 0.25rem;
    color: var(--global-theme-color);
  }
  .resource-index .card-text {
    font-size: 0.85rem;
    margin-bottom: 0;
    color: var(--global-text-color-light);
  }
  .resource-meta {
    font-size: 0.85rem;
    color: var(--global-text-color-light);
  }
</style>

<div class="resource-index">

  <p>{{ res.intro }}</p>

  <p class="resource-meta">
    Maintained in the
    <a href="{{ res.repo_url }}" target="_blank" rel="noopener noreferrer">Legged-Robots</a>
    repository &middot; last synced {{ res.generated }}
  </p>

  {% for entry in res.entries %}
    {% if entry.kind == 'heading' %}
      {% if entry.level == 2 %}
        <h2>{{ entry.title }}</h2>
      {% elsif entry.level == 3 %}
        <h3>{{ entry.title }}</h3>
      {% else %}
        <h4>{{ entry.title }}</h4>
      {% endif %}
    {% else %}
      <div class="row row-cols-1 row-cols-md-2 g-3 mt-1">
        {% for item in entry.items %}
          <div class="col">
            <a class="resource-link" href="{{ item.url | relative_url }}">
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">{{ item.title }}</h5>
                  {% if item.description != '' %}
                    <p class="card-text">{{ item.description }}</p>
                  {% endif %}
                </div>
              </div>
            </a>
          </div>
        {% endfor %}
      </div>
    {% endif %}
  {% endfor %}

</div>

{% endif %}
