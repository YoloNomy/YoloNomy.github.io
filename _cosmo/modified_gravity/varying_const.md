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

Furthermore, a space-time variation of the non-gravitational fundamental constants would lead to a violation of the weak equivalence principle (WEP) stating that all bodies must fall identically. This boils down to the fact that, if non-gravitational constants become dependent on space and time, so are the masses of the atoms and objects.

As we discussed in the previous lecture, the validity of the WEP is quantified by the value of the Eotvos parameter

$$\eta = 2\,\frac{|\vec{a}_1-\vec{a}_2|}{|\vec{a}_1+\vec{a}_2|}$$

If we introduce the so-called **sensitivity coefficient** 

$$f_i = \frac{\partial \ln(m_i)}{\partial \alpha}$$

which quantifies how the mass $m_i$ of particle $i$ depends on a change of a non-gravitational constant $\alpha$.

It is then possible to show that, in a constant gravitational field $g$,

$$\boxed{\eta \simeq \frac{c^{2}}{g}\,|f_1-f_2|\,\big|\vec{\nabla}\alpha\big|}$$

Thus measurements of the UFF also constraint varying non-gravitational constant models, and on the other hand, the variation of non-gravitational constant indeed induces a violation of the EEP. 

The proof of this expression both in a Newtonian and in a general relativistic context can be found in the following bonus session. 

<details markdown="1">
  <summary><strong>Violation of WEP from varying constants</strong></summary>

Consider any non-gravitational constant which we note $\alpha$. The mass of any composite body (e.g. an atom) depends on this constant, both through the masses of its constituents (yukawa couplings and Higgs potential) and through its internal binding energies (electromagnetic, strong, weak): $m = m(\alpha)$. If $\alpha$ becomes a function of space and time, $\alpha \to \alpha(x,t)$, this leads to a violation of the weak equivalence principle (WEP), i.e. of the universality of free fall. We show this first in Newtonian mechanics to build some intuition and then in general relativity.

**The Newtonian version**

Consider a particle of mass $m(\alpha)$ free-falling in the constant gravitational field $g$ of earth. We consider a Cartesian frame with unit vectors $\hat{x},\hat{y},\hat{z}=\hat{x_i}$. The particle is assumed to fall along the vertical $z$ axis, which is zero on the ground and pointing upward.

We start from the Lagrangian $L = T - V$ as the most fundamental quantity. In this context:

$$L = \frac{1}{2}m(\alpha)v^2 - m(\alpha)gz $$

Here remember that $\alpha$ is a function of space and time and thus $m=m(\alpha(\vec{x},t))$.
The [Euler–Lagrange](../../_meca/Analytical/Lagrangian.md) equations for each generalized coordinate $x_i$ are:

$$\frac{\text{d}}{\text{d}t}\frac{\partial L}{\partial \dot{x}_i}= \frac{\partial L}{\partial x_i}$$

and in our context, only the one along the $z$ axis is non-trivial and gives:

$$\frac{\text{d}}{\text{d} t}\Big(m(\alpha)\,\dot{z}\Big) = \frac{\partial}{\partial z}\Big(\frac{1}{2}m(\alpha)\dot{z}^2 - m(\alpha)\,g z\Big),$$

where the partial derivative is taken at fixed $\dot{z}$ and $t$. Expanding both sides and using the product rule we get:

$$\frac{\text{d} m}{\text{d} t}\dot{z} + m \ddot{z} =  \frac{\partial m}{\partial z}\left(\frac{\dot{z}^2}{2} -gz\right) - mg$$ 

where dotted quantities denote time derivatives (and $\text{d}m/\text{d}t = \partial_t m + \dot{z}\,\partial_z m$ is the total derivative along the trajectory). We thus notice additional terms that lead to a clear violation of the WEP. Indeed, if we rearrange the equation, we get:

$$\ddot{z}+g = -\frac{\text{d} \ln(m)}{\text{d} t}\dot{z} + \frac{\partial\ln(m)}{\partial z}\left(\frac{\dot{z}^2}{2} -gz\right)$$

which should be strictly zero in standard Newtonian mechanics, for which $\ddot{z}=-g$ in agreement with WEP.

We can further develop this expression using the chain rule (recall that $m$ depends
on $z$ and $t$ only through $\alpha$, with no explicit dependence):

$$\frac{\text{d}\ln(m)}{\text{d}t} = \frac{\partial \ln(m)}{\partial \alpha}\,\dot{\alpha}, \qquad \frac{\partial\ln(m)}{\partial z} = \frac{\partial \ln(m)}{\partial \alpha}\frac{\partial \alpha}{\partial z} $$

where $\dot{\alpha} \equiv \text{d}\alpha/\text{d}t = \partial_t\alpha + \dot{z}\,\partial_z\alpha$
is the total derivative along the trajectory. We introduce the **sensitivity coefficient**:

$$f = \frac{\partial \ln(m)}{\partial \alpha}$$

The important aspect is that $f$ will be different depending on the particle under consideration. For example different atoms will have different number of protons and electrons and thus will depend differently on the non-gravitational constants, like the fine-structure constant. The general expression to get the mass of an atom in terms of the mass of its constituants and their interactions is known as the **Bethe-Weizsäcker formula**.

Now, it is quite straightforward to generalize the previous expression to vector form:

$$\vec{a}-\vec{g}= -f\dot{\alpha}\,\vec{v}+ f\vec{\nabla}\alpha\left(\frac{v^2}{2}- \Phi\right)$$

where $\Phi = gz$ is the gravitational potential. If we add the rest-mass term
$L_0 = -mc^2$ to the Lagrangian (the leading term of the non-relativistic expansion
$-mc^2\sqrt{1-v^2/c^2}\approx -mc^2 + \frac{1}{2}mv^2$), we obtain the final expression:

$$\boxed{\vec{a}-\vec{g}= -f\dot{\alpha}\,\vec{v}+ f\vec{\nabla}\alpha\left(-c^2+\frac{v^2}{2}- \Phi\right)}$$

Now consider two particles with masses $m_1$ and $m_2$ and sensitivity coefficients
$f_1$ and $f_2$, compared at the same point with the same velocity $\vec{v}$. They fall
differently, leading to a non-zero value of the so-called Eötvös parameter

$$\eta = 2\,\frac{|\vec{a}_1-\vec{a}_2|}{|\vec{a}_1+\vec{a}_2|}$$

From the formula above, using $\vert\vec{a}_1+\vec{a}_2\vert \approx 2g$, $\vec{v}_1 \simeq \vec{v}_2$ and $\alpha_1 \simeq \alpha_2$, we get directly

$$\eta \simeq \frac{|f_1-f_2|}{g}\left|\,\dot{\alpha}\,\vec{v} + \vec{\nabla}\alpha\left(c^{2}-\frac{v^{2}}{2}+\Phi\right)\right|$$

and hence

$$\boxed{\eta \simeq \frac{c^{2}}{g}\,|f_1-f_2|\,\big|\vec{\nabla}\alpha\big|}$$

since the rest-mass contribution dominates by a factor $\sim c^2/v^2$.

**In General relativity**

In General relativity, the action of a point-like particle with a $\alpha$ dependent mass is given by

$$S = -\int m(\alpha)c \sqrt{-g_{\mu\nu}u^\mu u^\nu} $$

This action leads to the geodesic equation $u^\nu\nabla_\nu u^\mu =0$ when extremalized if $m$ is constant. If $m$ varies, we obtain

$$\boxed{u^\nu\nabla_\nu u^\mu = -f \partial_\beta \alpha \left(g^{\beta\mu} + u^{\beta}u^\mu\right)}$$

Hence, the space-time variation of $\alpha$ will deviate geodesics in a component dependent way (as $f$ is different depending on the atom under consideration).

This can be proved as follows:



**A sidenote: EEP violation and fifth force**

Duality field/geometry.

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

## Further reading

- [J.P. Uzan - Fundamental constants: from measurement to the universe, a window on gravitation and cosmology - Living Rev Relativ 28, 6 (2025)](https://link.springer.com/article/10.1007/s41114-025-00059-y)
- [C.J.A.P. Martins - The status of varying constants: a review of the physics, searches and implications - Rep. Prog. Phys. 80 126902](https://iopscience.iop.org/article/10.1088/1361-6633/aa860e)
