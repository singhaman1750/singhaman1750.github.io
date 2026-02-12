---
layout: page
permalink: /repositories/
title: repositories
description: This page contains my GitHub repositories.
nav: true
nav_order: 4
---

<style>
  .publications ol.bibliography li.repo-item {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
  }

  .publications ol.bibliography li.repo-item .preview {
    width: 120px;
    height: 120px;
    object-fit: cover;
    flex-shrink: 0;
    border-radius: 8px;
  }

  .publications ol.bibliography li.repo-item .repo-item__content {
    min-width: 0;
  }

  .publications ol.bibliography li.repo-item .title {
    font-size: 1rem;
  }

  .publications ol.bibliography li.repo-item .repo-desc {
    font-size: 0.9rem;
    color: var(--global-text-color-light);
    margin: 0.35rem 0 0.6rem;
  }

  @media (max-width: 768px) {
    .publications ol.bibliography li.repo-item {
      flex-direction: column;
    }

    .publications ol.bibliography li.repo-item .preview {
      width: 160px;
      height: 160px;
    }
  }
</style>

<div class="publications">

  {% if site.data.repositories.github_users %}
  <h2>GitHub users</h2>
  <ol class="bibliography">
    {% for user in site.data.repositories.github_users %}
      <li class="repo-item">
        {% assign user_image = user.image | default: '/assets/img/repository-placeholder.svg' %}
        <img class="preview z-depth-1 rounded" src="{{ user_image | relative_url }}" alt="{{ user.name }} placeholder">
        <div class="repo-item__content">
          <div class="title">
            <a href="https://github.com/{{ user.name }}">{{ user.name }}</a>
          </div>
          <div class="author">GitHub profile</div>
          {% if user.description %}
            <div class="repo-desc">{{ user.description }}</div>
          {% endif %}
          <div class="links">
            <a href="https://github.com/{{ user.name }}" class="btn btn-sm z-depth-0" role="button">Profile</a>
          </div>
        </div>
      </li>
    {% endfor %}
  </ol>
  {% endif %}

  {% if site.data.repositories.github_repos %}
  <h2 class="bibliography">GitHub Repositories</h2>
  <ol class="bibliography">
    {% for repo in site.data.repositories.github_repos %}
      <li class="repo-item">
        {% assign repo_image = repo.image | default: '/assets/img/repository-placeholder.svg' %}
        <img class="preview z-depth-1 rounded" src="{{ repo_image | relative_url }}" alt="{{ repo.name }} placeholder">
        <div class="repo-item__content">
          <div class="title">
            <a href="https://github.com/{{ repo.name }}">{{ repo.name }}</a>
          </div>
          <div class="author">GitHub repository</div>
          {% if repo.description %}
            <div class="repo-desc">{{ repo.description }}</div>
          {% endif %}
          <div class="links">
            <a href="https://github.com/{{ repo.name }}" class="btn btn-sm z-depth-0" role="button">Repo</a>
          </div>
        </div>
      </li>
    {% endfor %}
  </ol>
  {% endif %}

</div>
