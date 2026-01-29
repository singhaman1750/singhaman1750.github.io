---
layout: post
title: Planetary Gearbox - How to Calculate Gear-ratio?
date: 2026-01-28 13:32:20 +0300
description: 
thumbnail: assets/img/Planetary_gear_set_stylized.png # Add image post (optional)
tags: [gears, planetary_gear, actuators]
categories: sample-posts
---

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/Planetary_gear_set.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Fig 1: Planetary gear system
</div>

# Introduction

Planetary gearboxes are one of the most widely used gearbox designs in mechanical engineering. 
It is widely used in the field of robotics especially in development of joint actuators humanoid, quadruped and other legged robots. 
The reason for its widespread popularity is its low-gearbox-inertia and high efficiency, which are ideal for robotic joints. 
Apart from robotics, planetary gear systems are widely used in automotive industry to make automatic transmissions. 
The versatile nature of the planetary gearboxes can be seen by the fact that it is used in transmissions of mechanical systems as big as aeroplane and helicopters and also in the 
mechanical systems as small as hand drills. 

The aim of this blog post is to derive the mathematical expression of the gear-ratio or the gear reduction of the planetary gear system as a function the gear parameters like number of teeth, and module. 

# Design of Planetary Gearbox
The Planetary gearbox design consists of mainly 4 different parts in total, see Fig 1. The sun gear, the planet gear, the ring gear and the carrier. The sun, ring and carrier have a common fixed axis of rotation. The sun and planet gears are external gears and the ring gear is an internal gear. The planet gear is meshed with the sun gear and ring gear on the diametrically opposite side. The carrier is a link joining the centre of the sun and the planet gear, it has a revolute joint to the centre of the planet as well as the sun gear. 

In a particular configuration one of the sun, ring or carrier is fixed wrt to ground, one of the three parts is an input link and the third one is the output link. For eg. it is possible that we fix the sun gear, make the carrier as input link and ring gear as the output link. However, the most common configurtion that is used is fixing the ring gear, sending the input in the sun gear and taking the output from the carrier. This configuration is most commonly used because it gives highest value of gear ratio (output torque to input torque ratio) for the same number of teeth of the planet gears. In this blog, post we are going to find the gear ratio of this particular configuration only. 

# Gear ratio calculation

## Module

The module of a spur gear is calculated by dividing the Pitch circle diameter with the number of teeth of the gear. 
In a planetary gearbox, the module of the sun, the ring and the planet gear should be same in order to get proper meshing of the gears. 
The mathematical relation of the module, the diameter and the number of teeth of the gear is given as:

$$
m = \frac{PCD}{N} = \frac{2R}{N}
$$

Rearranging the above equation results in:

\begin{equation}
\label{eq:module_relation}
\frac{m}{2} N = R
\end{equation}

where $m$ is the module of a gear, $PCD$ is the Pitch circle diameter of the gear, $R$ is the radius of the gear, and $N$ is the number of teeth of the gear.



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

Let's assume that sun, planet, ring and carrier are rotating with angular velocities $\omega_{s}$, $\omega_{p}$, $\omega_{r}$, and $\omega_{c}$ in counter-clockwise (CCW) direction. Please note, $\omega_r = 0$ as ring gear is fixed. Also, let the velocity of the points $A$, $B$ and $C$ in Fig 2(b) be $V_{a}$, $V_{b}$ and $V_{c}$. The velocity of the centre of the planet gear, i.e. point $C$ in Fig. 2(b) can be given as follows:

$$
V_{c} = - \omega_{c} R_c = - \omega_{c} (R_{s} + R_{p})
$$

The negative sign shows that the velocity is in negative (left) direction. 
 
The velocity of sun gear particles at point $A$ is $V_{a}^{sun} = - \omega_{s} R_{s}$ and that of planet gear particles is $V_{a}^{planet} = V_{c} + \omega_{p} R_{p}$. Because, the sun and planet are meshed at $A$ these velocities should be equal. So, we get the following equation:

\begin{equation}
\label{eq:velocity_balance_bw_sun_and_planet}
(-\omega_{c} (R_{s} + R_{p})) + \omega_{p} R_{p} = - \omega_{s} R_{s}
\end{equation}

A similar thing can be done at point $B$. The velocity of planet gear particles at point $B$ is  $V_{b}^{planet} = V_{c} - \omega_{p} R_{p}$ and that of ring gear particles is $V_{b}^{ring} = \omega_r R_{r} = 0$ as ring is fixed. Equating these two, we get:

\begin{equation}
\label{eq:velocity_balance_bw_planet_and_ring}
(- \omega_{c} (R_{s} + R_{p}) - \omega_{p} R_{p}) = 0
\end{equation}

## Solving the Velocity equations
In the Eq.$\eqref{eq:velocity_balance_bw_sun_and_planet}$ and Eq.$\eqref{eq:velocity_balance_bw_planet_and_ring}$, $\omega_s$ (input velocity) and the radiis are the known values. The $\omega_{p}$ and $\omega_{c}$ are unknown values. We have a system of 2 equations with 2 variables. To solve the equations you can just add Eq.$\eqref{eq:velocity_balance_bw_sun_and_planet}$ and Eq.$\eqref{eq:velocity_balance_bw_planet_and_ring}$ to get the value of $\omega_{c}$ and subtract them to get $\omega_{p}$. The solution of the equations should look like the following:

$$
\omega_{c} = \frac{R_{s}}{2(R_{s} + R_{p})} \omega_{s}
$$

$$
\omega_{p} = \frac{R_{s}}{2R_{p}} \omega_{s} 
$$

Using the Eq.$\eqref{eq:module_relation}$ we can write the following:

$$
\omega_{c} = \frac{N_{s}}{2(N_{s} + N_{p})} \omega_{s}
$$

$$
\omega_{p} = \frac{N_{s}}{2N_{p}} \omega_{s} 
$$

Using the Eq.$\eqref{eq:geometric_relation}$ we can say that $2(N_{s} + N_{p}) = N_{s} + N_{r}$ and $2N_{p} = N_{r}-N_{s}$. Hence:

$$
\omega_{c} = \frac{N_{s}}{(N_{s} + N_{r})} \omega_{s}
$$

$$
\omega_{p} = \frac{N_{s}}{(N_{r}-N_{s})} \omega_{s} 
$$

The gear reduction can be given as:
\begin{equation}
\label{eq:gear_reduction}
\frac{\omega_{c}}{\omega_{s}} = \frac{N_{s}}{(N_{s} + N_{r})}
\end{equation}

We can see that $N_{s} \leq (N_{s} + N_{r})$, which means $\omega_{c} \leq \omega_{s}$. So, the output angular velocity is less than the input velocity. This is why it called a gear "reducer".

## Torque Relation
In ideal no energy loss condition the input power to the gearbox should be equal to the output power. So:

$$
\tau_{in} \omega_{in} = \tau_{out} \omega_{out}
$$

$$
\tau_{s} \omega_{s} = \tau_{c} \omega_{c}
$$

where $\tau_{s}$ and $\tau_{c}$ are torque input in sun and torque output from the carrier. The above equation can be written as:

$$
\frac{\tau_{s}}{\tau_{c}} =  \frac{\omega_{c}}{\omega_{s}} = \frac{N_{s}}{(N_{s} + N_{r})}
$$

The gear-ratio can now be given as:

\begin{equation}
\label{eq:gear_ratio}
\frac{\tau_{c}}{\tau_{s}} =  \frac{(N_{s} + N_{r})}{N_{s}} = 1 + \frac{N_{r}}{N_{s}} 
\end{equation}

The output torque value can be given as follows:

\begin{equation}
\label{eq:output_torque_relation}
\frac{\tau_{c}} = \large(1 + \frac{N_{r}}{N_{s}}\large) \tau_{s}
\end{equation}

We can observe the following points:

- We can see that as $N_{r} \geq N_{s}$ the output torque is higher than the input torque. 
- We can also see that the gear-ratio is independent of the module of the gears, it only depends on the number of teeth.

## Conclusion
In this blog post we derived the gear-reduction ratio of the planetary gear system. We saw that the final gear ratio is independent of the module of the gears and only depends on the number of teeth of ring and sun gear. 

