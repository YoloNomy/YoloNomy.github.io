---
layout: default
title: Grand canonical ensemble
parent: thermo
nav_order: 1
---

# Varying number of particles, grand canonical ensemble

So far, we only considered situations in which the number of particle was fixed. The Grand Canonical Ensemble (or Gibbs ensemble) describes an open system that can exchange both energy and particles with a reservoir. This is particularly useful for studying systems where the particle count is not fixed, such as chemical reactions or quantum gases.

## The discrete case

### Finding the partition function

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
p_i = \frac{1}{\Xi}e^{-\beta E_i -\gamma \mathcal{N}_i}
$$

where $\beta$ and $\gamma$ are the Lagrange multiplier associated to $E$ and $\mathcal{N}$ respectively. Their physical interpretation will be given in the next section.

$\Xi$ the grand canonical partition function defined as:

$$
\Xi = \sum_i e^{-\beta E_i -\gamma \mathcal{N}_i}
$$

<details>
  <summary><strong>Proof:</strong></summary>

We maximize the Gibbs entropy (with $k_B=1$)

$$
S = -\sum_i p_i \ln p_i
$$

under the constraints

$$
\sum_i p_i = 1,
$$

$$
\sum_i p_i E_i = U,
$$

$$
\sum_i p_i \mathcal N_i = \langle \mathcal N \rangle.
$$

Introduce Lagrange multipliers $\lambda_0, \lambda_1, \lambda_2$ and define

$$
\mathcal L =
-\sum_i p_i \ln p_i
-\lambda_0\left(\sum_i p_i -1\right)
-\lambda_1\left(\sum_i p_i E_i -U\right)
-\lambda_2\left(\sum_i p_i \mathcal N_i -\langle\mathcal N\rangle\right).
$$

Derivative with respect to $p_i$:

$$
\frac{\partial \mathcal L}{\partial p_i}
= -\ln p_i -1
-\lambda_0
-\lambda_1 E_i
-\lambda_2 \mathcal N_i = 0.
$$

Thus

$$
\ln p_i
= -1-\lambda_0-\lambda_1 E_i-\lambda_2 \mathcal N_i,
$$

$$
p_i
= e^{-1-\lambda_0}
e^{-\lambda_1 E_i-\lambda_2 \mathcal N_i}.
$$

Define (or simply rename):

$$
\beta=\lambda_1,
$$

$$
\gamma =\lambda_2,
$$

so that

$$
p_i
= e^{-1-\lambda_0}
e^{-\beta E_i-\gamma \mathcal{N}_i}.
$$

Normalization gives

$$
1=\sum_i p_i
= e^{-1-\lambda_0}
\sum_i e^{-\beta E_i-\gamma \mathcal{N}_i}.
$$

Define the grand partition function

$$
\Xi
= \sum_i e^{-\beta E_i-\gamma \mathcal{N}_i}.
$$

Hence

$$
e^{-1-\lambda_0}=\frac{1}{\Xi},
$$

</details>

We introduce now the **chemical potential**

$$\boxed{\mu = \frac{\partial U}{\partial N}\Bigg|_{S,V}}$$

which is the canonical conjugate of $N$ (see supplements [here](./canonical.md)). 
Using our understanding of the connection between statistical physics and classical thermodynamics aquired in [a previous lecture](./classical.md), we are able to infer the physical meaning of the Lagrange multipliers:

$$
\begin{aligned}
\begin{cases}
\beta &= 1/(k_B T)\\
\gamma &= -\mu\beta
\end{cases}
\end{aligned}
$$

<details markdown=1>
  <summary><strong>Proof:</strong></summary>

We recall that, from the normalisation condition $\sum_i \text{d}p_i=0$. Furthemore, in our case $\ln(p_i)=-\ln(\Xi)-\beta E_i - \gamma \mathcal{N}_i$. As such, the differential of the entropy is

$$
\begin{align}
\text{d}S&= - \sum_i \ln(p_i)\text{d}p_i\\
&= \beta \sum_i E_i \text{d}p_i + \gamma \sum_i \mathcal{N}_i \text{d}p_i
\end{align}
$$

Consider now the mean particle number

$$\mathcal{N}= \sum_i p_i \mathcal{N}_i$$

Its differential is hence:

$$\text{d}\mathcal{N} = \sum_i p_i \text{d}\mathcal{N}_i +  \sum_i \mathcal{N}_i \text{d} p_i = \sum_i \mathcal{N}_i \text{d} p_i$$

where we set $\text{d}\mathcal{N}_i=0$, as the number of particles associated to a given microstate is not something that is expected to change under a transformation.

As such, the entropy differential becomes:

$$
\text{d}S= \beta \sum_i E_i \text{d}p_i + \gamma \text{d}\langle\mathcal{N}\rangle
$$

Now, we should recall that mean energy is 

$$U= \sum_i p_i E_i$$

and its differential is hence:

$$\text{d}U = \sum_i p_i \text{d}E_i +  \sum_i E_i \text{d} p_i$$

which we used in [a previous lecture](./classical.md) to identify heat and work. We showed, an it is still true that

$$\delta W = \sum_i p_i \text{d}E_i = - P \text{d}V$$

The proof follows the exact same logic as in the canonical case, and varying particle number as no reason to change the value of the energy levels of the microstates $\text{d}E_i$.
Now, from the previously computed $\text{d}S$ we can extract:

$$\sum_i E_i \text{d}p_i= \frac{1}{\beta}\text{d}S - \frac{\gamma}{\beta} \text{d}\langle\mathcal{N}\rangle $$

Clearly, we see that something else than heat (varying entropy) also contribute to the first term of the differential $\text{d}U$. It is a change in the population (probability) of the energy levels due to changes in the mean number of particle $\text{d}\langle\mathcal{N}\rangle$. Indeed, one should understand all the microstates available to the system as a bunch of particle configurations, each associated to an energy $E_i$ and a particle number $\mathcal{N}_i$. Clearly, changing the mean number of particle $\langle\mathcal{N}\rangle$, will allow for microstates with more or less particle numbers to become more populated. Hence the probability distribution will shift.

Putting everything back in the expression of $\text{d}U$:

$$\boxed{\text{d}U = \frac{1}{\beta}\text{d}S - \frac{\gamma}{\beta} \text{d}\langle\mathcal{N}\rangle - P\text{d}V}$$

Now, from our definition of temperature

$$T = \frac{\partial U}{\partial S}\Bigg|_{V,\mathcal{N}},$$

we clearly identify, as in the canonical ensemble:

$$\boxed{T = 1/\beta}$$

from the first term of the differential. Furthermore, with  

$$\mu = \frac{\partial U}{\partial N}\Bigg|_{S,V}$$

we identify:

$$\boxed{\mu = -\frac{\gamma}{\beta}}$$

</details>


With these new relations we can write the probability distribution as:

$$
\boxed{p_i = \frac{1}{\Xi}e^{-\beta(E_i -\mu \mathcal{N}_i)}}
$$

and the grand canonical partition function:

$$
\boxed{\Xi = \sum_i e^{-\beta(E_i -\mu \mathcal{N}_i)}}
$$

### Finding back physical quantities


The entropy can be computed to be:

$$
\boxed{S = -\ln(\Xi) + \beta U -\beta\mu \langle \mathcal{N}\rangle}
$$


<details>
  <summary><strong>Proof:</strong></summary>
Using

$$
S=-\sum_i p_i\ln p_i
$$

and

$$
\ln p_i
= -\ln\Xi-\beta E_i+\beta\mu \mathcal N_i,
$$

we obtain

$$
S
= -\sum_i p_i
\left[-\ln\Xi-\beta E_i+\beta\mu N_i\right].
$$

Thus

$$
S
= \ln\Xi + \beta\sum_i p_i E_i 
- \beta\mu\sum_i p_i\mathcal N_i.
  $$

Hence

$$
S=\ln\Xi
+\beta U
-\beta\mu\langle\mathcal N\rangle.
$$

</details>

The mean particle number can be recovered from the partition function as

$$
\boxed{\langle\mathcal{N}\rangle = -\frac{\partial \ln(\Xi)}{\partial \gamma}}
$$

<details markdown=1>
  <summary><strong>Proof:</strong></summary>

Write

$$
\Xi=\sum_i e^{-\beta E_i -\gamma \mathcal N_i},
$$

Then

$$
\frac{\partial \Xi}{\partial \alpha}
=\sum_i \mathcal N_i
e^{-\beta E_i- \gamma \mathcal N_i}.
$$

Divide by $\Xi$:

$$
\frac1\Xi
\frac{\partial \Xi}{\partial \gamma}
=\sum_i \mathcal N_i
\frac{e^{-\beta E_i-\gamma\mathcal N_i}}{\Xi}
=\sum_i \mathcal N_i p_i.
$$

Thus

$$
\langle\mathcal N\rangle
=-\frac{\partial \ln\Xi}{\partial \gamma}.
$$

which we could have guessed immediately by understanding $\Xi$ as a generating function as discussed in [this lecture](./generating_function.md).

</details>

The mean energy:

$$
\boxed{U = -\frac{\partial \ln(\Xi)}{\partial \beta} + \mu \langle\mathcal{N}\rangle}
$$

allowing to understand $\mu$ as a mean energy per particle.

<details markdown=1>
  <summary><strong>Proof:</strong></summary>
Start from

$$
\ln\Xi
= \ln \sum_i e^{-\beta(E_i-\mu\mathcal N_i)}.
$$

Differentiate with respect to $\beta$ (at fixed $\mu$):

$$
\frac{\partial\ln\Xi}{\partial\beta}
= \frac1\Xi
\sum_i (-E_i+\mu\mathcal N_i)
e^{-\beta(E_i-\mu\mathcal N_i)}.
$$

Hence

$$
\frac{\partial\ln\Xi}{\partial\beta}
= -\sum_i p_i E_i + \mu\sum_i p_i \mathcal N_i.
  $$

Therefore

$$
U=\langle E\rangle
= -\frac{\partial\ln\Xi}{\partial\beta} + \mu\langle\mathcal N\rangle.
$$

Note here again that we could have guessed that $U = -\partial \ln(Xi)/\partial \beta$ from the fact that $\Xi$ is a generating function ([this class](./generating_function.md)). However, here the term $\mu \langle N\rangle$ might come as a surprise. It is simply an artifact from the fact that we expressed $\gamma= -\mu \beta$, and thus breaking the independence between the Lagrange multipliers from a physical argument.

</details>

The pressure remains 

$$P =\frac{1}{\beta}\frac{\partial \Xi}{\partial V} $$

<details>
  <summary><strong>Proof:</strong></summary>
Define the grand potential

$$
\Phi_G=-\frac1\beta\ln\Xi.
$$

Thermodynamics gives

$$
\Phi_G=U-TS-\mu N=-PV.
$$

Therefore

$$
P=-\frac{\Phi_G}{V}
=\frac1\beta
\frac{\partial\ln\Xi}{\partial V}.
$$

</details>


### The continuous case


