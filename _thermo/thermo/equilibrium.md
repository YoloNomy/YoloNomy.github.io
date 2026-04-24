---
layout: default
title: Thermal equilibrium and energy exchanges
parent: thermo
nav_order: 1
---

## Defining equilibrium

A system is said to be at thermal equilibrium with another if they do not exchange [heat](../firstprinciple), that is $\delta Q=0$.

As such, a system which is described by a single temperature $T$ is by definition at thermal equilibrium with itself that is each "subpart" of it is at equilbrium with another.

## The principle zero of thermodynamics

What is sometimes considered as the zeroth principle of thermodynamics states that thermal equilbrium is **contagious**, or more formally **transitive**. 

That is: consider three systems $A$, $B$ and $C$. If $A$ is in thermal equilibrium with $B$ and $A$ is in thermal equilibrium with $C$, then $B$ is in thermal equilibrium with $C$.

Often considered as a consequence of a combination of the first and the second principle (we'll rediscuss this later).

## Temperature and thermal equilbrium 

Temperature is a state variable that is not like the others. If it is the same between two systems, both are necessarily in thermal equilibrium between one another.

In the case of a difference of temperature $\Delta T$ between two systems, a flow of heat will occur until:

$$T_A=T_B$$,

$A$ and $B$ are in thermal equilibrium.

## Mechanical equilbrium

In the case of a difference of pressure $\Delta P$ between two objects, an adjustement of volumes will occur until:

$P_A=P_B$

This is mechanical equilibrium.

## Diffusive equilbrium 

In case of a difference of chemical potential between two systems, a flow of particles will occur until:

$\mu_A=\mu_B$

## Conjugate variables

We do not have yet all the tools to discuss in detail the subtle notion of conjugate variables.

- $T$ and $Q$, and more precisely, the entropy $S$ that we will introduce later.
- $P$ and $V$.
- $\mu$ an $\mathcal{N}$.

We will see that 

$$\text{d}U = T\text{d}S - P\text{d}V + \mu \mathcal{d}\mathcal{N}$$