---
layout: post
title: "Universe evolution and Friedmann equations"
---

# The building blocks of cosmology

Cosmology is the science that study the universe as a whole. Promoting cosmology as a branch of natural sciences has been made possible only very recently with the discovery of the universe expansion, showing that it was a dynamical entity (hence it becomes possible to predict and postdict its behavior) and the discovery of its very first light with the cosmic microwave background (cmb), implying that it history might have had a beggining.

The three building blocks of modern cosmology are the following:

- A) Cosmological principle: the universe is homogeneous (invariant under translation) and isotropic (invariant under rotations) on large scales.

- B) Content: the content of the universe is given by the various species of particle physics and an additional unknown component called cold dark matter (cdm). The species can all be sorted in two broad categories depending on their mass: matter (heavy and cold) and radiation (light and hot).

- C) Gravity: the theory of gravity is given by general relativity (see [here]({% link codes/cosmo/black-holes.md %}))) with a non zero cosmological constant $\Lambda$, responsible for the accelerated expansion of the universe.

# The FLRW metric

The assumption A) gives strong constraints on the possible geometry of the universe. 

$$ 
\text{d}s^2 = -c^2\text{d}t^2 + a(t)^2\left( \frac{\text{d}r^2}{1 - kr^2}  + r^2\text{d}\Omega^2\right) 
$$

# Universe content and perfect fluids

A) also gives strong constraints on the possible behavior of the content in the universe.

$$ T_{\mu \nu}=\rho u_\mu u_\nu + p (g_{\mu\,\nu}+ u_\mu u_\nu)= {\rm diag}(\rho,p,p,p)
$$

$$
p=w\rho
$$

The continuity equation
$$
\nabla_\mu T^{\mu \nu} = 0
$$
equivalent to fluid mechanics

$$
\frac{\partial\rho}{\partial t} + 3 H(1 + w)\rho =0
$$

$$
H := \frac{\dot{a}}{a}
$$

$$
\rho(a) =  a^{-3(1+w)}
$$

# The Friedmann equation(s)

We now use our last assumption C). General relativity 

$$     R^{\mu \nu} = 8 \pi G \left( T^{\mu \nu} - \frac{1}{2}g^{\mu \nu} T_{\ \sigma}^{\sigma}\right) $$ 

$$ \frac{H^2}{H_0^2} = \frac{8\pi G}{3}\rho - \frac{k}{a^2} -\frac{\Lambda}{8 \pi G} $$

$$
\frac{\ddot{a}}{a} = H^2 + \dot{H} = \frac{4 \pi G}{3}(\rho+3p)
$$

$$
\rho_c := \frac{3 H_0^2}{8 \pi G}
$$

$$
\Omega_{i} := \frac{\rho^i_0}{\rho_c} \qquad i\in\{m,r,DE,\kappa\}
$$

$$ \frac{H^2}{H_0^2} = \sum_i \Omega_i a^{-3(1+w_i)}$$

# Various evolutions and the Big-Bang model