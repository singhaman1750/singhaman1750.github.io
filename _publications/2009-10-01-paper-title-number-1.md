---
title: "Force control for robust quadrupedal locomotion: A Linear Policy approach"
collection: publications
permalink: /publication/17-01-2023-force-lp-ICRA-2023
excerpt: #'This paper is about the number 1. The number 2 is left for future work.'
date: 17-01-2023
venue: 'International Conference on Robotics and Automation (ICRA)'
paperurl: #'https://www.stochlab.com/papers/force_lp_ICRA_2023.pdf'
citation: #'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---

**Authors**: Aditya Shirwatkar\*, Vamshi Kumar Kurva\*, Devaraju Vinoda, **Aman Singh**, Aditya Sagi, Himanshu Lodha, Bhavya Giri Goswami, Shivam Sood, Ketan Nehete, Shishir Kolathaya

**Abstract**: This work presents a simple linear policy for direct force control for quadrupedal robot locomotion. The motivation
is that force control is essential for highly dynamic and agile motions. We learn a linear policy to generate end-foot trajectory
parameters and a centroidal wrench, which is then distributed among the legs based on the foot contact information using a
quadratic program (QP) to get the desired ground reaction forces. Unlike the majority of the existing works that use
complex nonlinear function approximators to represent the RL policy or model predictive control (MPC) methods with many
optimization variables in the order of hundred, our controller uses a simple linear function approximator to represent policy
along with only a twelve variable QP for the force distribution. A centroidal dynamics-based MPC method is used to generate
reference trajectory data, and then the linear policy is trained using imitation learning to minimize the deviations from the
reference trajectory. We demonstrate this compute-efficient controller on our robot Stoch3 in simulation and real-world
experiments on indoor and outdoor terrains with push recovery.

**Links**: [Paper](https://www.stochlab.com/papers/force_lp_ICRA_2023.pdf) / [Video](https://www.youtube.com/watch?v=k89QdImcqdo)