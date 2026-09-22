---
layout: page
title: Co-Design of Legged Robots
description: Optimizing morphology and actuation jointly against a target behaviour
img: assets/img/publication_preview/Humanoids_2025_method_diag.png
importance: 2
category: ongoing research
giscus_comments: false
related_publications: true

# Cards rendered by _includes/research_projects.liquid
projects:
  - title: Energy-Aware Monoped Jumping with Detailed Actuator Modeling
    img: assets/img/publication_preview/Humanoids_2025_method_diag.png
    description: >
      TODO: ~45 words. A co-design framework that optimizes jumping performance while modelling
      the actuator in detail — gearbox losses, thermal limits, electrical constraints. Say what
      a naive point-mass actuator model gets wrong, and what changes once you model it properly.
    links:
      paper: https://doi.org/10.1109/Humanoids65713.2025.11203144
  - title: High-Performance Jumping of a Five-Bar Monoped
    img: assets/img/publication_preview/Aim_main_diag.png
    description: >
      TODO: ~45 words. Co-design of a five-bar linkage monoped with actuator optimization in the
      loop. Explain what the five-bar topology offers, and how jointly tuning linkage geometry
      and actuator parameters beats tuning either one alone.
    links:
      arxiv: "2604.06025"
---

<a class="research-back" href="{{ '/projects/' | relative_url }}">&larr; Back to research themes</a>

<!-- TODO: one framing paragraph, ~60 words. What is this theme and why is it hard? -->

Designing the robot and designing its controller are usually separate jobs, done in that order.
That ordering quietly discards performance: a morphology fixed before the behaviour is known is
rarely the morphology that behaviour wanted. This theme optimizes structure and actuation jointly
against a target task, with actuator models detailed enough that the resulting design is
buildable rather than merely optimal on paper.

## Representative Projects

{% include research_projects.liquid projects=page.projects %}
