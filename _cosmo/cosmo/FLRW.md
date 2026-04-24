---
layout: default
title: The FLRW metric
parent: cosmo
---

## In a spatially flat Universe

Recall that, in General relativity, the geometry of space-time is characterized by a metric $g$ which allows to define the vector product (and thus define lengths and angles) at each point of space-time. $g$ can be expressed locally in specific coordinate frames. In particular, $g$ allows to define a small space-time interval $\text{d}s$.
In cosmology, we use **comoving frames**, that is frames "dragged along" by the expansion of the Universe. Let's introduce the comoving frame $t,x,y,z$.

If the Universe is spatially flat:

$$
\text{d}s^2 = -c^2\text{d}t^2 + a(t)^2(\text{d}x^2 +\text{d}y^2 + \text{d}z^2) 
$$

Or, as a matrix 

$$
g_{\mu\nu} =
\begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & a^2(t) & 0 & 0 \\
0 & 0 & a^2(t) & 0 \\
0 & 0 & 0 & a^2(t)
\end{pmatrix}
$$

We see that the FLRW metric is nothing more than a flat Minkowski metric with time dependent spatial metric components.
The function $a(t)$, called the **scale factor** changes between 0 and 1 as the Universe expands.
$\sqrt{\text{d}x^2 +\text{d}y^2 + \text{d}z^2}$ is sometimes noted $r$ or $\chi$. If two objects are simply dragged along by the expansion of the Universe, $\chi$ remain constant between them. In other word, if $\chi$ between two objects changed, it can only be due to proper motions. $\chi$ is called **the comoving distance**. $a(t)\chi$ is better understood as a physical distance, as it also accounts for the expansion. It is called the **proper distance**. We will see in [the next lecture](../distances), that it is not obvious to define distances in an expanding Universe, and that it can be done in several different ways. 

### Connection and geodesic equation

The four-momentum of a freely moving particle in the expanding Universe follows the **geodesic equation**:

$$
p^\mu \nabla_\mu p_\nu = 0
$$

This is a direct consequence of general relativity and is true both for massive and massless particles. Despite its geometrical meaning of particles following geodesics (shortest-length paths) in space-time, this equation can be derived from the continuity equation for a point-like particle.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

In coordinate form

$$\partial_\mu p_\nu + \Gamma^{\lambda}_{\,\,\mu \nu}p_\lambda=0$$

The connection coefficients can be expressed from the metric as:

$$
\Gamma^\lambda_{\ \mu\nu}
= \frac{1}{2} g^{\lambda \rho}
\left(
\partial_\mu g_{\nu\rho}
+ \partial_\nu g_{\mu\rho}
- \partial_\rho g_{\mu\nu}
\right)
$$

For the flat FLRW metric, we obtain:

$$
\begin{aligned}
&\Gamma^{0}_{00}=\Gamma^{0}_{0i} = \Gamma^{0}_{i0} = 0, \\
&\Gamma^{0}_{ij} = a \dot{a}\,\delta_{ij}, \\
&\Gamma^{i}_{0j} = \Gamma^{i}_{j0} = \frac{\dot{a}}{a}\,\delta^{i}_{j}.
\end{aligned}
$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

Hence, we can find that both energy and momentum of a free particle moving in space-time obey the equation:

$$\frac{\text{d}p_i}{\text{d}t} + \frac{\dot{a}}{a}p_i =0.$$

From this we can find that both the value of the physical energy and momentum decreases with the expansion as

$$ p_i \propto 1/a $$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

$$\begin{aligned}
&\partial_0 p_i + \Gamma^{\lambda}_{\,\,0 i}p_\lambda=0\\
& \frac{\partial p_i}{\partial t} + \Gamma^{0}_{\,\,0 i}p_0 + \Gamma^{j}_{\,\,0 i}p_j =0\\
&\frac{\partial p_i}{\partial t} + \frac{\dot{a}}{a} \delta^{i}_{j} p_j =0\\
& \frac{\partial p_i}{\partial t} + \frac{\dot{a}}{a} p_i =0
\end{aligned}
$$

</details>

For light, $p\propto \lambda$ and $E \propto \nu$, such that the wavelength of a photon, as well as its energy, is stretched by $1/a$ during the expansion.

## Adding spatial curvature

