---
layout: post
title: Planetary Gearbox -- Calculation of Gear-ratio
date: 2026-01-28 13:32:20 +0300
description: 
thumbnail: assets/img/how-to-write-intro-of-a-research-paper.jpeg # Add image post (optional)
tags: [gears, planetary_gear, actuators]
categories: sample-posts
---

# Introduction

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
    Fig 1: Planetary gear system
</div>

# Design of Planetary Gearbox
    1.1 Input
    1.2 Output
    1.3 Ring fixed
The Planetary gearbox design consists of mainly 4 different parts in total. The sun gear, the planet gear, the ring gear and the carrier.
In this blog piece

# Gear ratio calculation

## Module

The module of a spur gear is calculated by dividing the Pitch circle diameter with the number of teeth of the gear. 
In a planetary gearbox, the module of the sun, the ring and the planet gear should be same in order to get proper meshing of the gears. 
The mathematical relation of the module, the diameter and the number of teeth of the gear is given as:

$$
m = \frac{PCD}{N} = \frac{2R}{N}
$$

where $m$ is the module of a gear, $PCD$ is the Pitch circle diameter of the gear, $R$ is the radius of the gear, and $N$ is the number of teeth of the gear.
The above expression be re-written as follows after some rearrangement:

\begin{equation}
\label{eq:module_relation}
\frac{m}{2} N = R
\end{equation}

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/Planetary_gear_set_geometric_and_velocity_diagrams.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Fig 2: Planetary Gear System, (a) Geometric relation, (b) Velocity diagram
</div>

## Geometric relation

The geometry of the sun, planet and ring gear follow a relationship, see Fig 2 (a). The radius of the ring gear is equal to the sun of radius of sun gear and twice the radius of planet gear. 
This relation can be mathematically represented as follows:

$$
R_{s} + 2 R_{p} = R_{r}
$$

where $R_{s}$, $R_{p}$, and $R_{r}$ are the radii of the sun, planet and ring gears, respectively. 

From Eq.$\eqref{eq:module_relation}$, we can see that the Number of teeth of each gear is directly proportional to the radius of the gear. The constant $m/2$ has to be same for all the three (sun, planet and ring) gear,
to ensure proper meshing. So, we can write that:

\begin{equation}
\label{eq:geometric_relation}
N_{s} + 2 N_{p} = N_{r}
\end{equation}

where  $N_{s}$, $N_{p}$, and $N_{r}$ are the Number of teeth of sun, planet and ring gears, respectively. 

## Velocity Equations
To calculate the gear ratio we will have to write the relation between the angular velocities of the sun gear, planet gear, and the carrier. To do that let's look and the gear interaction points $A$, $B$ and $C$, see Fig 2(b). At point $A$ sun and planet gear are meshed together and at point $B$ planet and ring gear are meshed together. At point $C$, the carrier and planet gear are attached through a revolute joint.

Meshing together can be looked as if the sun and planet gear move without slipping at point $A$, and planet gear moves without slipping (wrt fixed ring) at point $A$.

Let's assume that sun, planet, ring and carrier are rotating with angular velocities $\omega_{s}$, $\omega_{p}$, $\omega_{r}$, and $\omega_{c}$ in counter-clockwise (CCW) direction. Also, let the velocity of the geometrical centre of the planet gears be $V_{c}$. The velocity of the centre of the planet gear, i.e. point $C$ in Fig. 2(b) can be given as follows:

$$
V_{c} = - \omega_{c} R_c = - \omega_{c} (R_{s} + R_{p})
$$

The negative sign shows that the velocity is in negative (left) direction. 
 
The velocity of sun gear particles at point $A$ is $\omega_{s} R_{s}$ and that of planet gear particles is $( - \omega_{c} (R_{s} + R_{p})+ \omega_{p} R_{p} ) $. 

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



