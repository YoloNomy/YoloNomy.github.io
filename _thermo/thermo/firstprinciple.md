---
layout: default
title: First law of thermodynamics
parent: thermo
nav_order: 1
---

# First law of thermodynamics: energy

## The law

In physics, "laws" or "principles" are comparable to "axioms" in mathematics. They are "rules" which seems to describe the world around us and from which a theory can be built by deriving their consequences and confront them with experiments. There are now way to derive the laws from more fundamental principles with a theory, but if an observational consequence of a law is not verified, then the theory is simply wrong, or out of its domain of validity. 

The thermodynamic theory that we will study here, is built on three such laws. 

Consider for now a closed system, which can only exchange energy with the exterior.
The first law of thermodynamics state that, there exist a state function called the *internal energy* $U$ that can be associated to this system. Under a transformation from a state $A$ to $B$, $U$ can change only through two processes as

$$\boxed{\Delta U = U_B-U_A= Q+ W}$$

where $Q$ is called a *heat transfer* and $W$ is called the *work*. 

This law can be expressed using the differential of the state function $U$ as

$$\boxed{\text{d}U = \delta Q + \delta W}$$

where

$$ Q= \int \delta Q$$

and 

$$ W = \int \delta W$$

## The difference between $d$ and $\delta$

You might have noted that we used the symbol $\delta$ to describe the small variations of $Q$ and $W$ while we reserved the symbol $\text{d}$ for $U$. 

$Q$ and $W$ are not state functions from which you can take the differential!

The bank account analogy: 

## Work

$$\delta W = -P {\rm d}V$$


$$ \delta W = \vec{F}\cdot\text{d}\vec{\ell}$$

<details>
  <summary>Correspondance with mechanics</summary>

$$P=-\frac{F}{S}=\frac{F \text{d}x}{\text{d}x\text{d}y\text{d}z}= $$

$$ {\rm d}V= {\text{d}x\text{d}y\text{d}z $$

hence 
$$ \delta W = \vec{F}\cdot\text{d}\vec{x}$$

as in mechanics.
</details>

- volume increase --> $\text{d}U =\delta W<0$, loss of energy
- volume decrease --> $\text{d}U =\delta W>0$ gain of energy

## Heat
