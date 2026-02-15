---
layout: default
title: Grand canonical ensemble
parent: thermo
nav_order: 1
---

## Varying number of particles, grand canonical ensemble

So far, we only considered situation in which the number of particle was fixed.

The Grand Canonical Ensemble (or Gibbs ensemble) describes an open system that can exchange both energy and particles with a reservoir. This is particularly useful for studying systems where the particle count is not fixed, such as chemical reactions or quantum gases.

### The discrete case

In order to introduce the grand canonical ensemble, let us first go back on the discrete case, which already allowed us to derive very powerful results without having to deal with the complexity of phase space.

Consider a system with accessible microstates caracterised by an energy $E_i$ and a number of particle $\mathcal{N}_i$. This would be typically the case of an open system in contact with a large reservoir, in which particle are free to enter and leave freely. The reservoir still impose the system to have a mean energy $\langle E \rangle=U$ and a mean particle number $\langle N \rangle$.
Maximizing the entropy $S$ of the system in this context, means asking for the constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i \mathcal{N}_i = \langle\mathcal{N}\rangle\\
&\sum_i p_i E_i = \langle E \rangle \\
& \sum_i p_i  = 1
\label{eq:constraintsGrandCano}
\end{aligned}
\end{cases}
$$

Doing so leads to:

$$
\boxed{p_i = \frac{1}{\Xi}e^{-\beta \left( E_i + \mu \mathcal{N}_i\right)}}
$$

with $\beta=1/T$ and $\Xi$ the grand canonical partition function defined as:

$$
\boxed{\Xi = \sum_i e^{-\beta \left( E_i - \mu \mathcal{N}_i\right)}}
$$

<details>
  <summary><strong>Proof:</strong></summary>

We write: 

$$
\begin{align}
\mathcal{L} &=  S(p_i) - \lambda_1 C_1(p_i)- \lambda_2 C_2(p_i)- \lambda_3 C_3(p_i)\\
&= -\sum^N_i p_i \ln(p_i) - \lambda_1 (\sum^N_i E_i p_i - \langle E \rangle)  - \lambda_2 (\sum^6_i p_i -1) - \lambda_3 (\sum^N_i \mathcal{N}_i p_i - \langle \mathcal{N} \rangle)
\end{align}
$$

Now the derivatives are:

$$
\begin{align}
&\frac{\partial \mathcal{L}}{\partial p_i} = - \ln(p_i) - 1 - \lambda_1 E_i - \lambda_2 \mathcal{N}_i   \\
&\frac{\partial \mathcal{L}}{\partial \lambda_1} =  -(\sum^6_i i p_i - \langle i \rangle)
&\frac{\partial \mathcal{L}}{\partial \lambda_2} =  -(\sum^6_i p_i -1) 
\end{align}
$$

Setting the first equation to 0, we get

$$
\begin{align}
&- \ln(p_i) - 1 - \lambda_1 i - \lambda_2 =0 \\
&p_i= e^{- 1 - \lambda_1 i - \lambda_2} \\
&p_i = e^{- 1 - \lambda_2}e^{-\lambda_1 i}
\end{align}
$$

The sum of probabilities equal to one leads to 

$$
\begin{align}
&\sum_i^6 e^{- 1 - \lambda_2}e^{-\lambda_1 i}=1 \\
&e^{- 1 - \lambda_2} = \frac{1}{\sum_i e^{-\lambda_1 i}}
\end{align}
$$

Re-injecting in the expression of $p_i$, we get

$$p_i = \frac{1}{\sum_i^6 e^{-\lambda_1 i}}e^{-\lambda_1 i} $$


</details>

The mean particle number can be recovered from the partition function as

$$
\boxed{\langle\mathcal{N}\rangle = \frac{\partial \Xi}{\partial \alpha}}
$$

with $\alpha=\mu\beta$.

<details>
  <summary><strong>Proof:</strong></summary>

</details>

$$
\boxed{U = -\frac{\partial \ln(\Xi)}{\partial \beta} + \mu \langle\mathcal{N}\rangle}
$$

<details>
  <summary><strong>Proof:</strong></summary>

</details>

$$
\boxed{S = -\ln(\Xi) + \beta U - \beta\mu \langle \mathcal{N}\rangle}
$$

<details>
  <summary><strong>Proof:</strong></summary>

</details>

The pressure remains 

$$P =\frac{1}{\beta}\frac{\partial \Xi}{\partial V} $$

<details>
  <summary><strong>Proof:</strong></summary>

</details>

Link with first principle:

$$U = \sum_i p_i E_i$$

$$\text{d}U = p_i \text{d}E_i + E_i\text{d}p_i $$

$$... \mu \text{d}\mathcal{N}$$

### The continuous case


