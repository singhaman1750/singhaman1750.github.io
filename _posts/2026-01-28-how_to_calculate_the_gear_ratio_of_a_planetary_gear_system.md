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

Planetary gearboxes are one of the most widely used gearbox designs in mechanical engineering. They are extensively used in robotics, especially in the development of joint actuators for humanoid, quadruped, and other legged robots. The primary reasons for their widespread popularity are their low gearbox inertia and high efficiency, which make them ideal for robotic joint applications.

Beyond robotics, planetary gear systems are widely used in the automotive industry, particularly in automatic transmissions. The versatility of planetary gearboxes is evident from the fact that they are used in mechanical systems ranging from large-scale applications such as airplanes and helicopters to compact devices like hand drills.

The aim of this blog post is to derive the mathematical expression for the gear ratio (or gear reduction) of a planetary gear system as a function of key gear parameters such as the number of teeth and the module.

# Design of Planetary Gearbox
A planetary gearbox design mainly consists of four different parts, as shown in Fig. 1: the sun gear, the planet gear, the ring gear, and the carrier. The sun gear, ring gear, and carrier share a common fixed axis of rotation. The sun and planet gears are external gears, while the ring gear is an internal gear. Each planet gear meshes with the sun gear on one side and with the ring gear on the diametrically opposite side. The carrier is a link that connects the center of the sun gear to the center of the planet gear, and it has revolute joints at the centers of both the sun and planet gears.

In a particular configuration, one of the sun gear, ring gear, or carrier is fixed with respect to the ground, one of the remaining components acts as the input, and the third acts as the output. For example, the sun gear can be fixed, the carrier can serve as the input, and the ring gear can be the output. However, the most commonly used configuration fixes the ring gear, applies the input at the sun gear, and takes the output from the carrier. This configuration is widely used because it provides the highest gear ratio (output torque to input torque ratio) for a given set of gear teeth. In this blog post, we derive the gear ratio for this specific configuration only.

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

We can see that $N_{s} < (N_{s} + N_{r})$, which means $\omega_{c} < \omega_{s}$. So, the output angular velocity is less than the input velocity. This is why it called a gear "reducer".

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
\tau_{c} = \large(1 + \frac{N_{r}}{N_{s}}\large) \tau_{s}
\end{equation}

We can observe the following points:

- We can see that as $N_{r} > N_{s}$ the output torque is higher than the input torque. 
- We can also see that the gear-ratio is independent of the module of the gears, it only depends on the number of teeth.

## Conclusion
In this blog post we derived the gear-reduction ratio of the planetary gear system. We saw that the final gear ratio is independent of the module of the gears and only depends on the number of teeth of ring and sun gear. 

