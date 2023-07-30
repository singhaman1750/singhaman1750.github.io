---
title: "Dynamic Mirror Descent based Model Predictive Control for Accelerating Robot Learning"
collection: publications
permalink: /publication/17-01-2023-DMD-MPC-ICRA-2022
excerpt: #'This paper is about the number 1. The number 2 is left for future work.'
date: 2022-01-01
venue: 'International Conference on Robotics and Automation (ICRA)'
paperurl: #'https://www.stochlab.com/papers/force_lp_ICRA_2023.pdf'
citation: #'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---

**Authors**: Utkarsh A. Mishra, Soumya R. Samineni, Prakhar Goel, Chandravaran Kunjeti, Himanshu Lodha, **Aman Singh**, Aditya Sagi, Shalabh Bhatnagar, Shishir Kolathaya

**Abstract**: Recent works in Reinforcement Learning (RL) combine model-free (Mf)-RL algorithms with model-based (Mb)-RL approaches to get the best from both: asymptotic performance of Mf-RL and high sample-efficiency of Mb-RL. Inspired by these works, we propose a hierarchical framework that integrates online learning for the Mb-trajectory optimization with off-policy methods for the Mf-RL. In particular, two loops are proposed, where the Dynamic Mirror Descent based Model Predictive Control (DMD-MPC) is used as the inner loop Mb-RL to obtain an optimal sequence of actions. These actions are in turn used to significantly accelerate the outer loop Mf-RL. We show that our formulation is generic for a broad class of MPC based policies and objectives, and includes some of the well-known Mb-Mf approaches. We finally introduce a new algorithm: Mirror-Descent Model Predictive RL (M-DeMoRL), which uses Cross-Entropy Method (CEM) with elite fractions for the inner loop. Our experiments show faster convergence of the proposed hierarchical approach on benchmark MuJoCo tasks. We also demonstrate hardware training for trajectory tracking in a 2R leg, and hardware transfer for robust walking in a quadruped. We show that the inner-loop Mb-RL significantly decreases the number of training iterations required in the hardware setting, thereby validating the proposed approach.

**Links**: [Paper](https://arxiv.org/pdf/2112.02999.pdf)