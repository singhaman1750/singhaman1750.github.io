---
layout: page
title: research
permalink: /projects/
description:
nav: true
nav_order: 2
horizontal: false
---

<!-- pages/projects.md -->

<div class="research-intro" markdown="1">

<!-- TODO: rewrite these three paragraphs in your own words. The pattern is:
     (1) the problem landscape, (2) what you do about it, (3) a one-line
     handoff into the themes below. -->

Legged robots are expected to run, jump, and carry loads in the real world, but their
performance is bounded long before the controller runs — by the actuators, gearboxes, and
linkages chosen at design time. Torque density, reflected inertia, gear ratio, and thermal
limits decide what behaviours are physically reachable, and these choices are usually fixed
by hand, early, and in isolation from the control problem they constrain.

My research treats hardware design as an optimization problem in its own right, and couples it
to the locomotion behaviours it has to support. I work on computational design and optimization
of planetary-gearbox actuators, co-design frameworks that tune morphology and actuation against
a target task, and the robot platforms needed to validate that any of it survives contact with
reality. The emphasis throughout is on practical, reproducible systems: automated CAD, open
tooling, and hardware experiments rather than simulation alone.

The work is organized around three themes.

</div>

<div class="projects">
  {% assign sorted_projects = site.projects | sort: "importance" %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
