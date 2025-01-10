---
layout: default
title: System
parent: thermo
nav_order: 1
---

# Studying a system

## State variables and state functions


We call a *system* any general object of study in thermodynamics. It could be a box of gas, a star, a thermal engine ...
What will interest us is how this system evolves and possibly interact with what surrounds it. The surrounding of a system is called the *exterior* or the *environment*.

Depending on how they interact with the exterior, we can distinguish three types of system:

- *Open systems*: which can exchange particles and energy with the exterior. For exemple a lake or a bathtub that can be filled or emptied.
- *Closed systems*: which can exchange only energy with the exterior. For example a mug of coffee which cools down or a star exchanging energy only by radiating into space.
- *Isolated systems*: which can not exchange anything with the exterior. As such they are idealisations and can not truely exist in nature, except perhaps for the Universe as a whole! 

In classical thermodynamics, a system is caracterized by the mesurable quantities called *state variables*. The more common states variables are:

- The *pressure* $P$, which is the force exerted by the system on it's surface. 
- The *temperature* $T$, which matches the intuition you have, and that can measure with a thermometer!
- The *volume* $V$ of the system, which is also exactly what you think!
- The *quantity of matter* $n$ (in moles) or equivalently the number of particles $N=nN_A$, where $N_A= 6.022 \times 10^{23}$ is the Avogadro number (the number of particles in one mole).

As we will further discuss later, for the typical case of a gas in a box, pressure can be interpreted as the transfer of momentum when particles hit the walls, temperature as the kinetic energy of the particles. However, thermodyanmics intend to be able to treat very general systems, far beyond the simple examples of gases.

The data of all these variables at a given time, is simply called the *state* of the system. For now, we will assume that the system we consider is described entierly by a single temperature (thermal equilibrium) and a single pressure.

The whole goal of thermodynamics is then to predict the evolution of these variables and understand how they are related to one another. This understanding can lead to a wide range of applications and can be used to build machines as motors or fridges aswell as finding the temperature inside of the Sun!

State variables can be ranked in two categories: the *extensive* ones and the *intensive* ones.
 
- Extensive variables describe the system as a whole and they can be summed when you add two systems. Basic examples are the volume and the quantity of matter. If you consider for exemple two boxes of gas with volumes $V_1$ and $V_2$ and you consider the system made by the two boxes, the total volume will be $V=V_1+V_2$.
- Intensive variables are given at every point of the system and they can not be summed when you add two system. Basic examples are the temperature and the pressure. Temperature is defined at every point of a system, some regions can be colder or hotter. If you consider two cup of coffees at temperatures $T_1$ and $T_2$, it would be absurd to say that the temperature of the two cups is the sum of them, hence $T\neq T_1+T_2$.

Once you have find state variables to describe your system, it is possible to create functions from them, called *state functions*.

For example, we will see in the next class that the energy of a system, noted $U$, is a state function $U(n,T,V,P)$ which can be expressed in term of the other *state variables*.

![image](../images/sun.png){: width="80%"}

*The sun as an open system, which can exchange both matter and energy with the exterior (space). It is characterized by its state variables and the state functions one can build from them.*

## Equation of state

Equation of states are equations that relates all the state variables of the system together. They are sort of "rules" that dictates the behavior of a given system. They can be derived experimentally, by quantifying how changing a state variable correspondingly change the values of the others.

A typical exemple of equation of state, that you will see over and over again, is called the ideal gas equation:

$$ PV = n\mathcal{R}T $$

As we will see, this equation describes with a great accuracy the behavior of gases as we can find them on earth.


