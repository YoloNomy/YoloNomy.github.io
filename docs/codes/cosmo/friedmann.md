---
layout: default
title: Universe evolution and Friedmann equations
parent: codes
nav_order: 3
---

# The building blocks of cosmology

Cosmology is the science that study the universe as a whole. Promoting cosmology as a branch of natural sciences has been made possible only very recently with the discovery of the universe expansion, showing that it was a dynamical entity (hence it becomes possible to predict and postdict its behavior) and the discovery of its very first light with the cosmic microwave background (cmb), implying that it history might have had a beggining.

The three building blocks of modern cosmology are the following:

- A) Cosmological principle: the universe is homogeneous (invariant under translation) and isotropic (invariant under rotations) on large scales.

- B) Content: the content of the universe is given by the various species of particle physics and an additional unknown component called cold dark matter (cdm). The species can all be sorted in two broad categories depending on their mass: matter (heavy and cold) and radiation (light and hot).

- C) Gravity: the theory of gravity is given by general relativity (see [here]({% link docs/codes/cosmo/black-holes.md %}))) with a non zero cosmological constant $\Lambda$, responsible for the accelerated expansion of the universe.

# The FLRW metric

The assumption A) gives strong constraints on the possible geometry of the universe. 
Let's consider a *comoving frame* $(t,r,\theta,\varphi)$.
The most general metric $g$ satisfying the constraints of being homogeneous and isotropic is given by the *Friedmann-Lemaître-Robertson-Walker (FLRW) metric*:

$$
\text{d}s^2 = -c^2\text{d}t^2 + a(t)^2\left( \frac{\text{d}r^2}{1 - kr^2}  + r^2\text{d}\Omega^2\right) 
$$

- $a(t)$ is the *scale factor*. a(t=t_0)=1, a(t=0)=0 (singularity).
- $k$ *spatial curvature*.

We introduce the famous *Hubble parameter*
$$
H := \frac{\dot{a}}{a}
$$

Quantifying the whole evolution of the universe.

Hubble law:

$$v\sim H_0d$$

# Universe content and perfect fluids

A) also gives strong constraints on the possible behavior of the content in the universe. Since no overall prefered direction should exist, the fluids/matter distribution in the universe must iself be homogeneous without any resulting velocity. We talk about a perfect fluid. The general form of their stress-energy tensor is given by:

$$ T_{\mu \nu}=\rho u_\mu u_\nu + p (g_{\mu\,\nu}+ u_\mu u_\nu)= {\rm diag}(\rho,p,p,p)
$$
More simply, such a fluid should obey the equation of state:
$$
p=w\rho
$$
One could think about an ideal gaz where $w = k_B T$. (see ideal gas ?)
We will assume that:

- All heavy elements are slow and have a null pressure. $w=0$. This includes matter and dark matter.
- All light and relativistic elements (photons and neutrinos) have $w=1/3$. (see statistical physics)
- The existence of a cosmological constant is equivalent to a energy vaccum of negative pressure with $w=-1$.

The continuity equation
$$
\nabla_\mu T^{\mu \nu} = 0
$$
equivalent to fluid mechanics (mass) conservation/continuity equation:

$$ \frac{\partial \rho}{\partial t}= - \vec{\nabla}\cdot\vec{j}$$

In the the FLRW metric, the continuity equation can be written as:
$$
\frac{\partial\rho}{\partial t} + 3 H(1 + w)\rho =0
$$
Integrating this, we obtain the evolution of the density (i.e. the dilution of a given species) through the evolution of the universe:
$$
\rho(a) =  rho_0 a^{-3(1+w)}
$$

So one gets:
- $\rho^r(a) =  \rho^r_0 a^{-4}$ for radiation
- $\rho^M(a) =   \rho^M_0 a^{-3}$ for matter
- $\rho^\Lambda(a) = \rho^\Lambda_0 $ for cosmological constant.

# The Friedmann equation(s)

We now use our last assumption C). The fundamental equation of General relativity is Einstein's equation, that can be rewritten as:

$$     R^{\mu \nu} = 8 \pi G \left( T^{\mu \nu} - \frac{1}{2}g^{\mu \nu} T_{\ \sigma}^{\sigma}\right) $$

Inserting FLRW for $g$ and perfect fluids for $T$, one gets the *Friedmann-Lemaître* equation

$$ \frac{H^2}{H_0^2} = \frac{8\pi G}{3}\rho - \frac{k}{a^2} -\frac{\Lambda}{8 \pi G} $$

and the Raychaudaury or acceleration equation

$$
\frac{\ddot{a}}{a} = H^2 + \dot{H} = \frac{4 \pi G}{3}(\rho+3p).
$$

Those are the fundamental equations of cosmology. If you know what the content of the universe $\rho$ is and its geometry $k$, you are fully able to predict its evolution.

Introducing the critical density

$$
\rho_c := \frac{3 H_0^2}{8 \pi G}
$$

one can consider the density parameters

$$
\Omega_{i} := \frac{\rho^i_0}{\rho_c} \qquad i\in\{m,r,DE,\kappa\}
$$

allowing to rewrite the Friedmann equation as:

$$ \frac{H^2}{H_0^2} = \sum_i \Omega_i a^{-3(1+w_i)}$$

$$     \left(\frac{H}{H_0}\right)^2 = \frac{\Omega_r}{a^4} +\frac{\Omega_m}{a^3} + \frac{\Omega_k}{a^2}+ \Omega_\Lambda $$

Looking at $t=t_0$, we get the closure equation:

$$\Omega_k + \Omega_\Lambda + \Omega_m + \Omega_r = 1 $$

Allowing to interpret the $\Omega$ as fractions.

# Various evolutions and the Big-Bang model



