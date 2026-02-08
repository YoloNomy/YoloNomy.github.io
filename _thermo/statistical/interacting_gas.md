---
layout: default
title: Interacting gas
parent: thermo
nav_order: 1
---

### Writting the partition function

Now that we understood well the ideal gas, we can study many different cases, simply by changing the microphysics of the particle, and hence the Hamiltonian function. We could for exemple consider a gas made of particles of different masses etc. A useful example is the case of interacting particles within the gas, which will be a more accurate model than the ideal gas when pressures are high enough or temperatures low enough.

$$H(\Gamma) = \frac{1}{2m}\sum^{3\mathcal{N}} p_i^2 + \sum_{n>m} U(|q^{(n)}-q^{(m)}|)$$

To simplify notations, we write $\Delta q_{nm}= |q^{(n)}-q^{(m)}|$.
Such that the partition function becomes:

$$Z= \int e^{-\beta \frac{1}{2m}\sum^{3\mathcal{N}} p_i^2 - \beta\sum_{n>m} U(\Delta q_{nm})}\text{d}\Gamma $$

which can be split in the product of two integrals, one over momenta, which is the ideal gas partition function, and one over space:

$$Z= \int e^{-\frac{\beta}{2m} \sum_i p_i^2} \text{d}^{3\mathcal{N}}p\int e^{-\beta\sum_{n>m} U(\Delta q_{nm})}  \frac{\text{d}^{3\mathcal{N}}q}{\mathcal{N}!}$$

Assuming that the gas is weakly interacting, we can assume that the potential is small and expand the exponential. Doing so allow us to simplify $Z$ and get the simple expression:

$$\boxed{Z\simeq Z^{ideal}\times \left(1 - \frac{\beta\mathcal{N}^2}{2V} U_0\right) }$$

with $U_0= \int U(\|q\|)\text{d}q$ for a single particle.

<details>
  <summary><strong>Proof</strong></summary>
  
</details>

### Physical quantities

From the expression of $Z$, it becomes possible to express, as before, the physical quantities of interest:

$$\boxed{ U = \frac{3}{2}\mathcal{N}k_B T + \frac{\mathcal{N}\rho}{2}U_0}$$

$$\boxed{P =  \rho k_B T + \frac{\rho^2}{2}U_0}$$

We see that we get the ideal gas formula plus some corrections due to the interactions proportional to the density of particles $\rho$ (and hence, at very low densities $\rho \to 0$, we recover the ideal gas).


<details>
  <summary><strong>Proof</strong></summary>
  
</details>

### Finding back Van der Waals equation of state

We almost found back the properties of the **van der Waals** gas studied in classical thermodynamics class.



## Going further: recommended readings and watching

- [Statistical mechanics, theoretical minimum lectures - L. Susskind (2013)](https://theoreticalminimum.com/courses/statistical-mechanics/2013/spring)