---
layout: default
title: System
parent: thermo
nav_order: 1
---

# Thermodynamics: why should you care?

# Studying a system

## State variables and state functions

We call a *system* any general object of study in thermodynamics. It could be a box of gas, a star, a thermal engine ...
What will interest us is how this system evolves and possibly interact with what surrounds it. The surrounding of a system is called the *exterior* or the *environment*.

Isolated system.

In classical thermodynamics, a system is caracterized by the mesurable quantities called *state variables*. The more common states variables are:

- The *pressure* $P$, which is the force exerted by the system on it's surface. 
- The *temperature* $T$, which matches the intuition you have, and that can measure with a thermometer!
- The *volume* $V$ of the system, which is also exactly what you think!
- The *quantity of matter* $n$ (in moles) or equivalently the number of particles $N=nN_A$, where $N_A= 6.022 \times 10^{23}$ is the Avogadro number (the number of particles in one mole).

As we will further discuss later, for the typical case of a gas in a box, pressure can be interpreted as the transfer of momentum when particles hit the walls, temperature as the kinetic energy of the particles. However, thermodyanmics intend to be able to treat very general systems, far beyond the simple examples of gases.

The whole goal of thermodynamics is then to predict the evolution of these variables and understand how they are related to one another. The consequences can be gigantic, especially regarding applications, as this understanding can be used to build machines as motors or fridges!

State variables can be ranked in two categories: the *extensive* ones and the *intensive* ones.
 
- Extensive variables describe the system as a whole and they can be summed when you add two systems. Basic examples are the volume and the quantity of matter. If you consider for exemple two boxes of gas with volumes $V_1$ and $V_2$ and you consider the system made by the two boxes, the total volume will be $V=V_1+V_2$.
- Intensive variables are given at every point of the system and they can not be summed when you add two system. Basic examples are the temperature and the pressure. Temperature is defined at every point of a system, some regions can be colder or hotter. If you consider two cup of coffees at temperatures $T_1$ and $T_2$, it would be absurd to say that the temperature of the two cups is the sum of them, hence $T\neq T_1+T_2$.

Once you have find state variables to describe your system, it is possible to create functions from them, called *state functions*.

For example, we will see in the next class that the energy of a system, noted $U$, is a state function $U(n,T,V,P)$ which can be expressed in term of the other *state variables*.

## Equation of state

The equation you will see over and over again, called the ideal gas equation, relates all the state variables of the system as

$$ PV = n\mathcal{R}T $$

