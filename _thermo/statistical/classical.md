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

### Putting back units

So far, we implicitely assumed $k_B = 1$. 

$$k_B = 1.3806490\times 10^{-23} $$ J/K

allows to translate temperature into energy through:
$$E_{th} \propto k_B T$$

And also allows to associate units to entropy,

$$S_{\rm th}  = k_B S$$

in order to match the defintion of the second principle $\text{d}S=\delta Q /T$.

Another way to re-introduce units is through the Lagrange multiplier $\beta$:

$$\beta=\frac{1}{k_B T}$$

## Zeroth principle and equilibrium

## Energy conservation and the first principle 

$$ U = \langle E \rangle = \sum_i p_i E_i $$ 

$$\text{d} U = \sum_i E_i\text{d}p_i + \sum_i p_i \text{d}E_i $$

$$\boxed{\delta Q = \sum_i E_i\text{d}p_i }$$

$$\boxed{\delta W =  \sum_i p_i \text{d}E_i}$$

