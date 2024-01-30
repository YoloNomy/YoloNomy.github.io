---
layout: default
title: Phase space
parent: thermo
nav_order: 1
---

## Varying number of particles, grand canonical ensemble

Consider a system with accessible microstates caracterised by an energy $E_i$ and a number of particle $N_i$. Then maximizing the entropy $S$ of the system in the grand cononcial ensemble, letting the system exchange energy and particles with the exterior and asking for the constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i N_i = \langle N \rangle\\
&\sum_i p_i E_i = \langle E \rangle \\
& \sum_i p_i  = 1
\label{eq:constraintsGrandCano}
\end{aligned}
\end{cases}
$$

leads to:

$$
p_i = \frac{1}{Z}e^{-\beta E_i + \mu N_i}
$$

With $\beta=1/T$ and $Z$ the partition function defined as:

$$
\boxed{Z = \sum_i e^{-\beta E_i + \mu N_i}}
$$

<details>
  <summary>Proof</summary>
  
</details>

$$
\boxed{\langle N\rangle = \frac{\partial Z}{\partial \alpha}}
$$

with $\alpha=\mu\beta$.

Note that allowing other constraints as Eq.\ref{eq:constraintsGrandCano} would add new lagrange multipliers appearing in the exponential of the expression of $p_i$.

## Volumes in phase space

The probability $d\mathcal{P}$ of a given element of the phase space is given by:

$$
\text{d}\mathcal{P}= \rho \text{d}\Gamma
$$

### Ideal gas, again



