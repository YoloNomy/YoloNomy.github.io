---
layout: default
title: Classical thermo
parent: thermo
nav_order: 1
---

# Seeing classical thermodynamics emerging from the statistics

We made a lot of progress in the previous lectures, by understanding how the maximisation of entropy can help us finding the probability distribution. However, this first part of the lectures might seems very abstract and for a good reason: it is! Statistical mechanics is not an easy subject.
Let us now try to reconnect, gradually, with the language of classical thermodynamics and emmerge out of abstraction.

### A little summary of where we are

As it does not hurt to repeat oneself, let's start with a big picture summary of where we stand. We considered a system like a box containing many particles as moving through time between different configurations of energy $E_i$ and with probability $p_i$. For now we assumed that these possibilities (microstates) were discrete. As such, the system can be thought as a die being rolled over and over again and showing randomly one face or another.

We convinced ourselves that a good way to evaluate the $p_i$ of each microstate (particle configuration) was to maximize the entropy function

$$S=-\sum_i p_i\ln(p_i)$$

quantifying our ignorance about the details of the system. Doing so can be done under some constraints. For example we can ask that the mean energy of the system is forced by a thermostat to have a value of $\langle E \rangle$. Adding these constraints is similar to looking for the probabilities of a biased die, which have a specific mean value for the number it displays.
The maximisation of entropy under the constraints of mean energy leads to 

$$p_i = \frac{1}{Z}e^{- \frac{E_i}{T}}$$

where $Z=\sum_i e^{E_i/T}$ is the partition function and
where the temperature $T$ tells us how much the mean energy has to change if we want to increase the entropy of the $p_i$ distribution.

We found that $Z$ plays a crucial role in recovering the physical quantities that one can observe about the system, for example:

$$\langle E \rangle = -\frac{\partial \ln(Z)}{\partial \beta}  $$

and

$$P = \frac{1}{\beta}\frac{\partial \ln(Z)}{\partial V}\Bigg|_T$$

In reading all this, one should keep in mind that:

- Entropy maximisation here is not yet related to 2nd principle. It is a way to derive $p_i$, coming from information theory. If you are skeptical about this, we will look much later at at other ways to derive $p_i$ without using $S$.
- We assumed a discrete set of accessible energy level which is of course a simplification. We will gradually go beyond this simplification in the next lectures. However, the logic and the formula we derive above will remain extremely important.
- In this class, we are now exclusively concerned with systems in thermal equilibrium. This is translated here by the fact that the probability distribution $p_i$ does not change with time. The system moves around its microstates, but the probability of each microstate always remain the same. After a long enough time, it will have explored all of it's accessible microstates.

### Restoring physical units

Up to this point, we have deliberately ignored physical units. This implicitly corresponds to working in natural units where the Boltzmann constant is set to unity, $k_B = 1$.

The Boltzmann constant is defined as
$$
k_B = 1.380\,649 \times 10^{-23}\ \mathrm{J\,K^{-1}},
$$
and acts as a conversion factor between temperature, measured in kelvin, and energy, measured in joules. Thermal energies (per particle and degree of freedom)are therefore typically written as (see our classical thermodynamics class on [ideal gas](../thermo/idealgas.md))
$$
E_{\mathrm{th}} \sim k_B T.
$$
Because $k_B$ is numerically very small, the energy associated with thermal excitation is usually a small quantity when expressed in joules.

The constant $k_B$ also fixes the physical units of entropy. In statistical mechanics, entropy is first introduced as a dimensionless quantity derived from a probability distribution,

$$
S = - \sum_i p_i \ln p_i
$$

The corresponding thermodynamic entropy is obtained by

$$
S_{\mathrm{th}} = k_B\, S,
$$

which has units of $\mathrm{J\,K^{-1}}$. This is the entropy that appears in classical thermodynamics, for instance in the second law written (for reversible processes) as

$$
\mathrm{d}S_{\mathrm{th}} = \frac{\delta Q_{\mathrm{rev}}}{T}.
$$

Another ubiquitous appearance of $k_B$ is in the Lagrange multiplier $\beta$ associated with the energy constraint in equilibrium statistical mechanics:

$$\beta = \frac{1}{k_B T}.$$

In what follows, we will freely alternate between expressions written in thermodynamic units and those written in units where $k_B = 1$. With the relations summarized above, it should always be straightforward to reinstate physical units when needed.

## Zeroth principle and equilibrium

## Energy conservation and the first principle 

The mean energy $\langle E \rangle$ of the system, is nothing else than the internal energy $U$ in the context of classical thermodynamics. As such, and from now on, we will use the two notations interchangably. As a reminder:

$$ U = \langle E \rangle = \sum_i p_i E_i $$ 

Now, it is instructive to look at the differential of $U$:

$$\text{d} U = \sum_i E_i\text{d}p_i + \sum_i p_i \text{d}E_i $$

We see a first term corresponding to how the mean energy change if the probability associated to each microstate were to change, keeping each energy level fixed. This correspond to what we define as a heat injection:

$$\boxed{\delta Q = \sum_i E_i\text{d}p_i }$$

and a second term corresponding to how the mean energy change if the energy level associated to each microstate were to change, keeping the probabilities fixed. This correspond to what we define as work:


$$\boxed{\delta W =  \sum_i p_i \text{d}E_i}$$
