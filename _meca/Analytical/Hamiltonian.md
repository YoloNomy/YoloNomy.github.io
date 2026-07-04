---
layout: default
title: Hamiltonian mechanics
parent: Analytical 
nav_order: 2
---


## Hamiltonian 

**canonical momentum**

$$p = \frac{\partial \mathcal{L}}{\partial \dot{q}}$$

$$H(p,q) = \sum_i p_i\dot{q}_i - L(q,\dot{q})$$

$$\frac{\text{d}q^i}{\text{d}t}=\frac{\partial H}{\partial p_i}$$

$$\frac{\text{d}p_i}{\text{d}t}=-\frac{\partial H}{\partial q^i} $$

An **observable** is a general function $f(q,p,t)$ on phase space. It's total change with time can be obtained with the chain rule as

$$\frac{\text{d}f}{\text{d} t} = \frac{\partial f}{\partial t} + \sum_i \frac{\partial f}{\partial q^i}\frac{\partial q^i}{\partial t} + \sum_i\frac{\partial f }{\partial p_i}\frac{\partial p_i}{\partial t}$$

If we want to see how the function changes along the evolution of the system, we can insert back Hamilton's equations such that 

$$\frac{\text{d}f}{\text{d} t} = \frac{\partial f}{\partial t} + \sum_i \frac{\partial f}{\partial q^i}\frac{\partial H}{\partial p_i} - \sum_i\frac{\partial f }{\partial p_i}\frac{\partial H}{\partial q^i}$$

This motivates the introduction of the so-called Poisson brackets

$$\{f,g\} = \sum_i^{3\mathcal{N}} \left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} -  \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right) $$

Such that the time evolution of any observable $f$ becomes

$$\frac{\text{d}f}{\text{d} t} = \lbrace f, H\rbrace + \frac{\partial f}{\partial t}  $$

While this definition might seem a bit abstract and fancy, the Poisson bracket is of very high importance in the geometry of phase space as discussed in [this lecture](../../_maths/geodiff/Hamiltonian.md).