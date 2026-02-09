---
layout: default
title: System
parent: thermo
nav_order: 1
---

# Studying a system

## State variables and state functions

In thermodynamics (and in physics in general), a **system** is the object we want to study. It could be a box of gas, a star, a thermal engine ...
What will interest us is how this system evolves and possibly interact with what surrounds it. For the specifics of thermodynamics, our main interest will be to understand and quantify how some properties of the system (like its temperature, or volume) can change under specific conditions.

The surrounding of a system is called the **exterior** or the **environment**.

Depending on how they interact with the exterior, we can distinguish three types of system:

- **Open systems**: which can exchange particles and energy with the exterior. For exemple a lake or a bathtub that can be filled or emptied.
- **Closed systems**: which can exchange only energy with the exterior. For example a mug of coffee which cools down or a star exchanging energy only by radiating into space.
- **Isolated systems**: which can not exchange anything with the exterior. As such they are idealisations and can not truely exist in nature, except perhaps for the Universe as a whole! 

In classical thermodynamics, a system is caracterized by the mesurable quantities called **state variables**. These are the physical properties of interest that characterize the system. The more common states variables are:

- The **pressure** $P$, which is the force exerted by the system on it's surface. 
- The **temperature** $T$, which matches the intuition you have, and that can be measured with a thermometer!
- The **volume** $V$ of the system, which is also exactly what you think!
- The **quantity of matter** $n$ (in moles) or equivalently the number of particles $\mathcal{N}=nN_A$, where $N_A= 6.022 \times 10^{23}$ is the Avogadro number (the number of particles in one mole).

As we will further discuss, for the typical case of a gas in a box, pressure can be interpreted as the transfer of momentum when particles hit the walls and temperature as the kinetic energy of the particles. However, thermodyanmics intend to be able to treat very general systems, far beyond the simple examples of gases. It was also develloped historically before the understanding of gases as made of atoms and molecules and as such does not require any interpretation of this kind. 

The set of all the state variables at a given time, is simply called the **state** of the system. For now, unless otherwise stated, we will assume that the system we consider is described entierly by a single temperature and a single pressure. Clearly, this is a simplifying assumption, as extended objects can have different temperature/pressure at different point. We'll discuss that point in more details when we will define [thermal equilibrium](../equilibrium) and leave the discussion of more complex scenarios for later.

The whole goal of thermodynamics is then to predict the evolution of the state variables and understand how they are related to one another. This understanding can lead to a wide range of applications and can be used to build machines as motors or fridges aswell as estimating the temperature inside of the Sun!

State variables can be ranked in two categories: the **extensive** ones and the **intensive** ones.
 
- **Extensive variables** describe the system as a whole and they can be summed when you add two systems (i.e. when you consider a new larger system composed of two separate subsystems). Basic examples are the volume and the quantity of matter. If you consider for exemple two boxes of gas with volumes $V_1$ and $V_2$ and you consider the system made by the two boxes, the total volume will be $V=V_1+V_2$.
- **Intensive variables** are given at every point of the system (we say that they are *local*) and they can not be summed when you add two system. Basic examples are the temperature and the pressure. Temperature is defined at every point of a system, some regions can be colder or hotter. If you consider two cup of coffees at temperatures $T_1$ and $T_2$, it would be absurd to say that the temperature of the two cups is the sum of them, hence $T\neq T_1+T_2$.

Once you have found state variables to describe your system, it is possible to combine them to create mathematical functions with them, called **state functions**. Such functions can be very useful if you can give them a physical interpretation and/or in order to simplify complicated problems.

For example, we will see in the next class that the energy of a system, noted $U$, is a state function $U(n,T,V,P)$ which can be expressed in term of the other **state variables**.

![image](../images/sun.png){: width="80%"}

*The sun as an open system, which can exchange both matter and energy with the exterior (space). It is characterized by its state variables and the state functions one can build from them.*

## Equation of state

Equation of states are equations that relates all the state variables of the system together. They are sort of "rules" that dictates the behavior of a given system. They can be derived experimentally, by quantifying how changing a state variable correspondingly change the values of the others. As such, equations of state play a major role in thermodynamics. 

A typical exemple of equation of state, that you will see over and over again, is called the ideal gas equation:

$$ PV = n\mathcal{R}T $$

where $P,V,n,T$ are respectively the pressure, volume, quantity of matter and temperature of the gas and $\mathcal{R}$ is a constant called the ideal gas constant.

As we will see, this equation describes with a great accuracy the behavior of gases under reasonable assumptions.


