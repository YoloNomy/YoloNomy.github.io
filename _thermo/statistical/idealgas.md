---
layout: default
title: Ideal gas II
parent: thermo
nav_order: 1
---

# Classical ideal gas

## The equation of states and energy

Let us now apply the above equations to rederive the ideal gas properties. Consider a box filled with $\mathcal{N}$ particles. These particles are free and non interacting. Treating them classicaly in the context of Newtonian mechanics, we can write the energy of each particle as $\vec{p}^2/2m$ (See the [classical mechanics](../../_meca/Newton/Energy.md) lecture on this topic). As such, the energy of a microstate, i.e. a particle configuration in the box is given by

$$E(i)=\frac{1}{2m}\sum_n^{\mathcal{N}}{\vec{p}_n}^2$$

where we sum over all $\mathcal{N}$ independent particles.

The partition function associated to the maximisation of enetropy is hence  

$$Z=\int e^{-\frac{\beta}{2m}\sum_n p_n^2} d^{3\mathcal{N}}x d^{3\mathcal{N}}p$$

Where we replaced the sums over the $N$ possible microstates associated to the macrostate by continuous integrals over momentum and space, as discussed in the previous lecture.

Develloping this integral simply gives

$$ \boxed{Z=\left(\frac{e}{\rho}\right)^\mathcal{N}\left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}}$$

<details>
  <summary>Proof</summary>
 
The integral over space gives

$$\int dx^{3\mathcal{N}}=\frac{V^\mathcal{N}}{\mathcal{N}!}$$

where the $\mathcal{N}!$ is here to traduce the fact that particles are distinguishable and avoid double conting same particle configurations with different labeling.

$$Z=\frac{V}{\mathcal{N}!}\left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}$$
</details>

From $Z$, one can find back the mean energy of the macrostate under consideration to be

$$ \boxed{E = -\frac{\partial \ln(Z)}{\partial \beta} = \frac{3}{2}\mathcal{N}k_B T}$$

<details>
 <summary>Proof</summary>

$$\begin{aligned}
\ln(Z)&=\ln\left(\left(\frac{e}{\rho}\right)^N\left(\frac{2m\pi}{\beta}\right)^{\frac{3N}{2}}\right) \\
&= N\ln\left(\frac{e}{\rho}\right)+\frac{3N}{2}\left(\ln(2m\pi)-\ln(\beta)\right)\\
\end{aligned}
$$

$$\begin{aligned}
-\frac{\partial \ln(Z)}{\partial \beta}&= -\frac{3\mathcal{N}}{2}\frac{\partial}{\partial \beta}\left(-\ln(\beta)\right) \\
&= \frac{3\mathcal{N}}{2} \frac{1}{\beta}\\
&= \frac{3\mathcal{N}}{2} k_B T
\end{aligned}
$$

</details>

Similarly, we can compute the pressure of the macrostate to be

$$ P = \frac{\partial{E}}{\partial{V}}\Bigg|_S= \rho k_B T$$

that is, we derived back the ideal gas law

$$ \boxed{P =\frac{n\mathcal{R}T}{V}}$$

and thus, only by assuming that particles were not interacting $E=E_c$, and asking for the entropy to be maximal! 

<details>
  <summary>Proof</summary>
As

$$P= -\frac{\partial E}{\partial V}\Bigg|_{S}$$

and 

$$ E= \frac{3N}{2} k_B T= \frac{3\mathcal{N}}{2}k_B $$

</details>

### The Maxwell-Boltzmann speed distribution

We can use the partition function to associate a probability to a given microstate

$$p_i = \frac{1}{Z}e^{-\beta E_i}$$

$$p(E)\text{d}E = \frac{1}{Z}e^{-\beta E_i} $$

Single particle 