---
layout: default
title: Varying constants
parent: cosmo
---

# Empirical validation of general relativity II: fundamental constants

Fundamental constants play a crucial (and perhaps surprising role) in the empirical tests of general relativity and the quest for modified gravity theories. Indeed, as we will discuss here:

- A space and/or time variation of the non-gravitational constants would be in direct **violation with the Einstein Equivalence Principle (EEP)**. This would imply that gravitation can not be described by a **metric theory of gravity** and/or that a **fifth fundamental interaction** is required to describe fundamental physics.
- A space and/or time variation of the gravitational constant would be in direct **violation with the Strong Equivalence Principle (SEP)**. This would imply that gravitation can not be described by a **general relativity** and that effectively a **different metric** would be required to describe the matter sector and the gravitational sector.

## Fundamental constants: an overview

Inspired by the discussion of [Uzan (2025)](https://link.springer.com/article/10.1007/s41114-025-00059-y), we can define the fundamental constants as the set of **necessary** parameters that **cannot be explained** by **a theory**, only **measured**. This definition covers several aspects:

- **necessary:** Fundamental constants are required, there is no way to get rid of them. They play key roles in a theory which can be different depending on the constant considered. 
- **cannot be explained/measured**: The theory in which the constant appear cannot explain or derive their value anyhow. These values can only be measured. As such, the constant set clearly a theoretical limit of the theory. 
- **a theory**: The number of fundamental constants depends of a given theory. As theories evolve, they can redefine the status and number of constants. One can hope that this number reduces with time, signature that the theory can more and more explanatory power.

Our standard model of particle physics together with general relativity requires 19 fundamental constants, listed in the table below. Ultimately, this number is expected to be even larger as the standard model does not account for observed phenomena such as the mass of neutrinos or dark matter. 

![image](../pictures/constants_table.png){: width="80%"} 

*List of the fundamental constants for the standard model of particle physics and general relativity. Taken from [Uzan (2025)](https://link.springer.com/article/10.1007/s41114-025-00059-y).*


As a general matter of fact, we prefer to consider dimensionless parameters (as the fine-structure constant $\alpha$), instead of constants with dimensions (such as $c$ and $\hbar$). The reason for this is that constants with dimensions can be interpreted as unit conversion factor instead of fundamental quantities. Dimensionless ratios, on the other hand, quantifies relationships between fundamental quantities. Indeed, it is always possible to fix $\hbar=c=1$ without changing the physics. Setting $\alpha=1$ would however give a theory in which the physics of the Universe is completely changed. Today, dimensional constants as $c$ are even fixed by convention in order to define unit systems (see again [Uzan (2025)](https://link.springer.com/article/10.1007/s41114-025-00059-y) for a more detailed discussion).

Dimensionless constants of the standard models are of four broad types:

- **Gauge couplings $g_i$**, which quantify the relative strength of fundamental interactions. They can be also quantified through the **fine structure constants** defined as $\alpha_i = g_i^2/(4\pi)$ in natural units, which can be easier to measure.
- **Yukawa couplings $h_i$** which quantify the masses of each particles (and are ultimately couplings of fermions with the Higgs boson). They can be measured directly by looking at mass ratios $m_i/m_j = h_i/h_j$. 
- **Symmetry breaking angles $\theta_i, \delta_{\rm CKM}$**: which quantifies the breaking of symmetries as the terms of the CKM matrix and the strong vacuum phase, associated to the CP violations of the weak and strong forces respectively.
- **Higgs Potential** parameters, $\hat{\mu}$ and $\lambda$ defining the shape of the Higgs potential through the data of the mass of the Higgs boson and its quartic coupling respectively. 

## Non-gravitational constants and the EEP

We use the term "non-gravitational constants" here to describe broadly any fundamental constant that is not the Newton constant $G$ and that is not anyhow related to it. 

A variation of the non-gravitational fundamental constants would lead to a direct violation of the local position invariance (LPI), which is one of the three building block of the EEP and that we defined in our [previous class](./foundations-GR.md).
Indeed, in such a case, the results of non-gravitational experimental tests would clearly depend on the region of space and time in which they are performed.

Furthermore, a space-time variation of the non-gravitational fundamental constants would lead to a violation of the weak equivalence principle (WEP) stating that all bodies must fall identically.

<details markdown="1">
  <summary><strong>Violation of WEP from varying constants</strong></summary>

**The Newtonian version**


**In General relativity**

</details>

### The fine structure constant 

![image](../pictures/QSO_summary.png){: width="80%"} 

*Measurement from QSO of varying constants. Data taken from [Uzan (2025)](https://link.springer.com/article/10.1007/s41114-025-00059-y).*

In S.I. units:

$$\boxed{\alpha = \frac{e^2}{4\pi \hbar c\varepsilon_0}}$$

$\alpha =7.297 352 5643 (11) \times 10^{-3} \simeq 1/137$ (from [CODATA](https://physics.nist.gov/cgi-bin/cuu/Value?alph))

Varying $\alpha$ --> violation of EEP.

Oklo $z=0.14$, 2 Gyr ago:

$$\frac{\Delta \alpha}{\alpha_0} = (0.005 ±0.061)\times 10^{-6}$$

$$\frac{\dot{\alpha}}{\alpha_0} = (1.8 \pm 2.5)\times 10^{-19} \, {\rm yr^{-1}}$$


### The electron to proton mass ratio

$$\mu = \frac{m_e}{m_p}$$

$$\overline{\mu}= \mu^{-1} = \frac{m_p}{m_e}$$

$\overline{\mu}=1836.152 673 426(32)$ from [CODATA](https://physics.nist.gov/cgi-bin/cuu/Value?mpsme).

Varying $m_e$ --> violation of EEP.

$$\frac{\dot{\mu}}{\mu_0} = (3.09 \pm 1.42)\times 10^{-17} \, {\rm yr^{-1}}$$

## Gravitational constant and the SEP

### Why is the gravitational force so weak? 

We recall from our first lecture that $G=6.674300(15) \times 10^{-11}$ m$^{3}$kg$^{−1}$⋅s$^{−2}$ (Value from [Codata 2022](https://physics.nist.gov/cgi-bin/cuu/Value?bg)).

Dirac's numerology. 
(See also Feynman's lecture on gravitation)

Paleontolgy, stellar physics, BBN

### Varying gravitational constant

Varying $G$ --> violation of SEP.

$\alpha_G$

<details markdown="1">
  <summary><strong>Why a varying $G$ implies a violation of the SEP</strong></summary>

$$G = G_0 f(x,t)$$

$$\mathcal{L}=  \sqrt{-|g|}\frac{1}{16\pi G_0 f(x,t)}(R-2\Lambda) + \mathcal{L}_m(\psi)$$

We will discuss later how to produce self consistent models of modified gravity for which $G$ becomes a function of space-time.

</details>

Is equivalent to vary all masses identically together

## A sidenote: EEP violation and fifth force

Duality field/geometry.

## Further reading

- [J.P. Uzan - Fundamental constants: from measurement to the universe, a window on gravitation and cosmology - Living Rev Relativ 28, 6 (2025)](https://link.springer.com/article/10.1007/s41114-025-00059-y)
- [C.J.A.P. Martins - The status of varying constants: a review of the physics, searches and implications - Rep. Prog. Phys. 80 126902](https://iopscience.iop.org/article/10.1088/1361-6633/aa860e)
