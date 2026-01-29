---
layout: post
title: How to calculate the gear ratio of a planetary gearbox
date: 2026-01-28 13:32:20 +0300
description: 
thumbnail: assets/img/how-to-write-intro-of-a-research-paper.jpeg # Add image post (optional)
tags: [research, research-paper, writing]
categories: sample-posts
---

Planetary gearboxes are one of the most widely used gearbox designs in mechanical engineering. 
It is widely used in the field of robotics especially in development of joint actuators humanoid, quadruped and other legged robots. 
The reason for its widespread popularity is its low-gearbox-inertia and high efficiency, which are ideal for robotic joints. 
Apart from robotics, planetary gear systems are widely used in automotive industry to make automatic transmissions. 
The versatile nature of the planetary gearboxes can be seen by the fact that it is used in transmissions of mechanical systems as big as airplane and helicopters and also in the 
mechanical systems as small as hand drills. 

This blog piece helps in deriving the gear-ratio or the gear reduction of the planetary gear system. 

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/Planetary_gear_set.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Planetary gear system
</div>

## Body
1. Explaining the planetary gearbox design
    1.1 Input
    1.2 Output
    1.3 Ring fixed
The Planetary gearbox design consists of mainly 4 different parts in total. The sun gear, the planet gear, the ring gear and the carrier.
In this blog piec

3. Module, Diameter and number of teeth relation

$$
m = \frac{PCD}{N} = \frac{2R}{N}
$$

$$
\frac{m}{2} N = R
$$

where $m$ is the module of a gear, $PCD$ is the Pitch circle diameter of the gear, and $N$ is the number of teeth of the gear.

4. Geometric relation of a planetary gearbox

$$
R_{s} + 2 R_{p} = R_{r}
$$
$$
\frac{m}{2} N_{s} + 2 \frac{m}{2} N_{p} = \frac{m}{2} N_{r}
$$
$$
N_{s} + 2 N_{p} = N_{r}
$$

5. Calculate the gear ratio of the planetary gearbox
4.0 Diagram of a planetary gearbox
   
4.1 velocity of the center of the planet gear:

$$
V_{c} = \omega_{c} R_c = \omega_{c} (R_{s} + R_{p})
$$

4.1 Equate the velocity at the sun to planet interaction

$$
(-V_{c}) + \omega_{p} R_{p} = \omega_{s} R_{s}
$$

\begin{equation}
\label{eq:velocity_balance_bw_sun_and_planet}
\omega_{p} R_{p} - \omega_{c} (R_{s} + R_{p}) = \omega_{s} R_{s}
\end{equation}

4.2 Equate the velocity of the planet to the ring gear

$$
(-V_{c}) - \omega_{p} R_{p} = \omega_{r} R_{r} = 0
$$

\begin{equation}
\label{eq:velocity_balance_bw_planet_and_ring}
\omega_{c} (R_{s} + R_{p}) + \omega_{p} R_{p} = 0
\end{equation}

4.3 Solve the equation and write the expression of gear-ratio

7. Analyse the gear-ratio

## Conclusion
1. Explain what this blog did
2. Further reading
3. References



