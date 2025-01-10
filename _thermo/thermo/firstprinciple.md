---
layout: default
title: First law of thermodynamics
parent: thermo
nav_order: 1
---

# First law of thermodynamics: energy

## The law

In physics, "laws" or "principles" are comparable to "axioms" in mathematics. They are "rules" which seem to describe the world around us and from which a theory can be built by deriving their consequences and confront them with experiments. There are no way to derive the laws from more fundamental principles with a theory, but if an observational consequence of a law is not verified, then the theory is simply wrong, or out of its domain of validity. 

The thermodynamic theory that we will study here, is built on three such laws. 

Consider for now a closed system, which can only exchange energy with the exterior.
The first law of thermodynamics state that, there exist a state function called the *internal energy* $U$ that can be associated to this system. Under a transformation from a state $A$ to a state $B$, $U$ can change only through two processes as

$$\boxed{\Delta U = U_B-U_A= Q+ W}$$

where $Q$ is called a *heat transfer* and $W$ is called the *work*. $Q$ can be understood as the variations of energy due to the random motion of the particles within the body, as the cool down of a cup of coffee. $W$ is to be understood as a mechanical change of energy, as a system which would be squeezed.

This law can be expressed using the differential of the state function $U$ as

$$\boxed{\text{d}U = \delta Q + \delta W}$$

where $W$ and $Q$ can then be computed by integration (sum) of the small $\delta Q$ and $\delta W$ between the states $A$ and $B$, that is

$$ Q= \int_A^B \delta Q$$

and 

$$ W = \int_A^B \delta W$$

## The difference between $\text{d}$ and $\delta$

You might have noted that we used the symbol $\delta$ to describe the small variations of $Q$ and $W$ while we reserved the symbol $\text{d}$ for $U$. 

Let us try to explain intuitively why we make such a distinction here. A more rigourous mathematical explanation can be found in any good textbook.

As a general rule, the differential $\text{d}$ *can only be computed for state functions*. As they represent exchanges, $Q$ and $W$ are not state functions from which you can take the differential.

A useful analogy, is to compare the energy of a system with your bank account: 

- $U$ is the total money on your account. It can be defined at any time. If I am indiscrete, I can ask you "How much is your $U$ right now?" It makes sense to ask how much did it change over a period of time $\Delta U$ or consider very small amount of time given by the differential $\text{d}U$.
- $Q$ and $W$, being energy exchanges with the exterior, would be two different forms of bank transfers. They can change the amount of $U$ but it makes no sense to ask you what is the value of your bank transfer right now and how much did it change in the last minutes. $\delta Q$ and $\delta W$ correspond to bank transfers associated with the small change of total money $\text{d}U$.

# Various types of transformations

The internal energy $U$ of a system can change during various types of transformations. Let us here define some of them in order to introduce some of the thermodynamical jargon you might encounter everywhere:

- *(de)compression*: the volume of the system is changed.
- *reversible/quasi-static transformation*: a transformation is performed very slowly on the state of the system.
- *isobaric transformation*: transformation at constant pressure.
- *adiabatic transformation*: transformation for which $\delta Q=0$.
- *isochore transformation*: transformation at constant volume.
- *isothermal transformation*: transformation at constant temperature.

## Work

Work is the energy exchanged by the system when a constant mechanical force is exerted on it. 

$$\delta W = -P {\rm d}V$$


We will encounter the work again in [mechanics](../../../meca/Newton/energy), where it is again deeply linked with energy. The definition will be a bit different and we explain below to the curious reader why they are the same.

<details>
  <summary>Correspondance with mechanics</summary>

In mechanics, the infinitesimal work $\delta W$ of a force $\vec{F}$ associated to the infinitesimal displacement $\text{d}\vec{\ell}$ of a body is defined as

$$ \delta W = \vec{F}\cdot\text{d}\vec{\ell}$$

where $\cdot$ is the dot product.
Furthermore, the pressure is defined as the force exerted over a surface. For a constant force $\vec{F}$ applied uniformly on a surface $S$, we have:

$$P = -\frac{\vec{F}}{S}\cdot \vec{n}$$

Where $\vec{n}$ is the normal to the surface.
The minus sign is a convention allowing to define that a positive pressure pushes a surface while a negative pressure pulls a surface.
Consider now an infinitesimal volume element $\text{d}x, \text{d}y, \text{d}z$. Apply a constant force $F\vec{e}_x$ along the $x$ direction on the surface $\text{d}x\text{d}y$ of normal $\vec{e}_x$. This would "pull out" the surface, as the pressure of a gas would push outward on the walls of its container.
 
The pressure in that case becomes 

$$P=-\frac{F}{\text{d}y\text{d}z}= \frac{F \text{d}x}{\text{d}x\text{d}y\text{d}z} = -\frac{\delta W}{\text{d} V} $$

where we recognize the infinitesimal volume
$$ {\rm d}V= \text{d}x\text{d}y\text{d}z $$ and the work of the force on the infinitesimal surface. Hence pressure is not only a force per unit of surface, it is also an energy per unit of volume!
</details>

- If the volume increased by the force, then $\text{d}V>0$ and hence $\text{d}U =\delta W<0$. Thus the system losses energy when it expends.
- If the volume decrease $\text{d}V<0$ and hence $\text{d}U =\delta W>0$. Thus the system gain energy when it contracts.


**Exercice: Consider an ideal gas, thus obeying the relation $PV=nRT$. Show that, if its volume is changed from $V_A$ to $V_B$, the corresponding work is $W= n\mathcal{R}\ln\left(\frac{V_B}{V_A}\right)$.**

<details>
  <summary>Solution</summary>

$$ \begin{aligned}
W &= -\int_A^B P \text{d}V\qquad \qquad && \text{definition of work}\\
&= -\int_A^B \frac{nRT}{V} \text{d}V && \text{ideal gas law}\\
&= - nRT\int_A^B \frac{1}{V} \text{d}V && \text{isothermal transformation}\\
&= - nRT [\ln(V)]^B_A && \text{integral of $1/x$}\\
&= - nRT\left(\ln(V_B)-\ln(V_A)\right)\\
&= nRT\left(\ln(V_A)-\ln(V_B)\right)\\
&= nRT \ln\left(\frac{V_B}{V_A}\right) && \text{property of log: $\ln(a)-\ln(b)=\ln(a/b)$}
\end{aligned}
$$

</details>


## Heat

Three types of heat transfers

- *Conduction*
- *Convection*
- *Radiation*

$P,V,T$ are related by an equation of state so it's enough to know the heat induced by a change in two of them.

In a reversible transformation, the heat transformation can be decomposed in three different equivalent ways as

$$\begin{cases}
\begin{aligned}
\delta Q &= C_p \text{d} T + h \text{d}P\\
\delta Q &=C_v \text{d} T + \ell \text{d}V\\
\delta Q &=\mu \text{d} V + \lambda \text{d}P
\end{aligned}
\end{cases}
$$

### Application: heat for an ideal gas

