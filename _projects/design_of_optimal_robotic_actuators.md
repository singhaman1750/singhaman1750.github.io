---
layout: page
title: Design of Optimal Robotic Actuators
description: Computational design of planetary-gearbox actuators for legged robots
img: assets/img/publication_preview/AIR_2025_ESSPG_vs_ISSPG.png
importance: 1
category: ongoing research
related_publications: true

# Cards rendered by _includes/research_projects.liquid
projects:
  - title: "COMPAct: Computational Optimization and Automated Modular Design"
    img: assets/img/publication_preview/ICRA_26_graphical_abstract.png
    description: >
      TODO: ~45 words. COMPAct turns actuator design into a numerical optimization over gear
      ratio, stage topology, and motor selection, then emits the CAD automatically. Say what it
      optimizes for and what the automation buys you over hand design.
    links:
      arxiv: "2510.07197"
  - title: External vs. Internal Single-Stage Planetary Gearboxes
    img: assets/img/publication_preview/AIR_2025_ESSPG_vs_ISSPG.png
    description: >
      TODO: ~45 words. A like-for-like comparison of ESSPG and ISSPG actuator topologies at
      matched specifications. State the trade-off you found — torque density, backdrivability,
      efficiency, packaging — and which one a legged-robot designer should reach for.
    links:
      arxiv: "2506.16356"
  - title: "DTEA: Dual-Topology Elastic Actuator"
    img: assets/img/publication_preview/DTEA_Dual_Topology_Elastic_Actuator.png
    description: >
      TODO: ~45 words. An actuator that switches between series and parallel compliance in real
      time. Explain why a single fixed compliance topology is a compromise, and what switching
      between them unlocks for impact absorption and efficient jumping.
    links:
      arxiv: "2604.15865"
---

<a class="research-back" href="{{ '/projects/' | relative_url }}">&larr; Back to research themes</a>

<!-- TODO: one framing paragraph, ~60 words. What is this theme and why is it hard? -->

The actuator sets the ceiling on what a legged robot can do. Gear ratio, stage topology, and
motor choice together fix torque density, reflected inertia, and thermal headroom — yet these
are typically picked by hand from catalogue parts. This theme treats the actuator as a design
variable to be optimized numerically, and builds the tooling to fabricate and test the result.

## Representative Projects

{% include research_projects.liquid projects=page.projects %}
