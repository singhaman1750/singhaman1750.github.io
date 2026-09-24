---
layout: page
title: Robot Platforms and Locomotion
description: Building quadrupeds and the control that makes them robust in hardware
img: assets/img/publication_preview/stoch_3_diag.png
importance: 3
category: completed research
related_publications: true

# Cards rendered by _includes/research_projects.liquid
projects:
  - title: A Chain-Driven, Sandwich-Legged Quadruped Robot
    img: assets/img/publication_preview/stoch_3_diag.png
    description: >
      TODO: ~45 words. The design and experimental analysis of Stoch 3. Say what the chain drive
      and sandwich leg structure buy you — inertia, robustness, serviceability — and what the
      hardware experiments demonstrated.
    links:
      paper: https://dl.acm.org/doi/10.1145/3787370.3787373
      arxiv: "2503.14255"
      website: https://aman-singh.in/stoch3-design/
  - title: "Force Control for Robust Quadruped Locomotion"
    img: assets/img/publication_preview/ICRA_2023_Force_control_linear_policy_stoch3.JPG
    description: >
      TODO: ~45 words. A linear policy approach to force control for quadruped locomotion.
      Explain why a linear policy is worth preferring here, and what robustness it bought on
      hardware compared to the alternatives.
    links:
      paper: https://doi.org/10.1109/ICRA48891.2023.10161080
  - title: Dynamic Mirror Descent MPC for Accelerating Robot Learning
    img: assets/img/publication_preview/ICRA_2022.png
    description: >
      TODO: ~45 words. Model predictive control built on dynamic mirror descent to speed up
      robot learning. State the sample-efficiency problem it attacks and the gain it delivered.
    links:
      paper: https://doi.org/10.1109/ICRA46639.2022.9812089
---

<a class="research-back" href="{{ '/projects/' | relative_url }}">&larr; Back to research themes</a>

<!-- TODO: one framing paragraph, ~60 words. What is this theme and why is it hard? -->

Design and co-design claims only mean something once a robot survives contact with the floor.
This theme covers the platforms built to test them — quadrupeds designed for serviceability and
repeatable experiments — together with the locomotion controllers that run on them. The
recurring question is which modelling and control choices still hold up once real actuators,
real compliance, and real impacts are in the loop.

## Representative Projects

{% include research_projects.liquid projects=page.projects %}
