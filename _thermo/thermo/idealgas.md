---
layout: default
title: Ideal gas
parent: thermo
nav_order: 1
---

# Ideal gas

## The fundamental equations

An ideal gas is a gas which satisfies the state equation:

$$\boxed{PV = n\mathcal{R}T}$$

where $\mathcal{R}=8.314$  J/mol/K is the so-called universal gas constant. This state's equation is motivated from experiments made on gases. An ideal gas also follows the second's Joule's law, which states that it's internal energy only depends on the quantity of matter $n$ and the temperature $T$:

$$\boxed{U=U(n,T)}$$

All these equations should be understood as verified experimental relationships that intruiged physicist which where trying to understand the behavior of gases. They can however be retrieved by assuming that the gas is made of point particles bouncing randomly and not interacting between them. As such, the ideal gas assumption breaks when considering high pressures, when particles are able to interact between one another, or when some quantum effects come into play.

<details  markdown="1">
  <summary>Exercice: Temperature of a room</summary>

</details>

<details  markdown="1">
  <summary>Exercice: Temperature of a molecular gas</summary>

Can be used to model roughly stars and interstellar clouds in which they form. For more, see Jean's mass in the [astrophysics lectures](../../../cosmo/cosmo/stars-form/).

</details>

## A word on constants


$$ \mathcal{R} = k_B N_A $$

$$ \boxed{PV = N k_B T}$$

## Laplace law

An ideal gas satisfies the relation

$$ \boxed{PV^\gamma=\text{cst}}$$

during an adiabatic ($Q=0$) transformation at constant $n$.
Here $\gamma=C_P/C_V$ is called the adiabatic index. This relation is known as the Laplace law.

<details>
  <summary>Exercice: proove it!</summary>

</details>

Depending on why you need it, this law can be re-expressed as

$$TV^{\gamma-1}=\text{cst}\qquad\text{or}\qquad T^\gamma P^{1-\gamma}=\text{cst}$$

<details>
  <summary>Proof</summary>

Starting from Laplace's law 
$PV^\gamma= \text{cst}$ and using the ideal gas law $P=\frac{n\mathcal{R}T}{V}$, one finds

$$ n\mathcal{R}T\frac{V^\gamma}{V} = n\mathcal{R}T V^{\gamma-1} = \text{cst}$$

as $n\mathcal{R}=\text{cst}$, 

$$T V^{\gamma-1} = \text{cst}$$

Now, we can use again the ideal gas law in this expression to replace $P$ and obtain

$$
\begin{aligned}
&T \left(\frac{n\mathcal{R}T}{P}\right)^{\gamma-1} = \text{cst}\\
&TT^{\gamma-1}(n\mathcal{R})^{\gamma-1} \frac{1}{P^{\gamma-1}} = \text{cst}\\
&T^{\gamma}P^{-(\gamma-1)} =\text{cst}\\
&T^{\gamma}P^{1-\gamma} =\text{cst}
\end{aligned}
$$

</details>

Hence in an adiabatic transformation, the work becomes

$$\boxed{W = -n c_V \Delta T}$$

but also

$$\boxed{W = \frac{n\mathcal{R}\kappa}{\gamma-1}\Delta V^{\gamma-1}}$$

### Applications


## Microscopic model

Note that all the laws about the ideal gas stated above where derived experimentally, without the need to understand gas as made up of subparticles. However, it is amazing that all these laws can be demonstrated simply by assuming that the gas is made of non interacting particles obeing Newton mechanics! The proper derivation will be done in the statistical mechanics lectures, but let us give an introduction here, to have a feeling.

Let us assume that the gas can be understood microscopically as follows: 
Consider a square box filled with free particles moving randomly and constantly bouncing off the walls. We assume particles are not interacting with one another and that they bounce elastically with the walls meaning that they do not loose energy when bouncing. As such, the [total momentum](../../../meca/Newton/laws/) and [energy](../../../meca/Newton/energy/) is conserved. All these approximations are valid, at least at low pressure and intermediate temperatures, as the gas particles are extremely small and separated from one another by gigantic distances. 

In this framework, the pressure that the gas exert on the walls, can be expressed as

$$\boxed{P = \frac{Nm}{3V} \langle v^2\rangle,}$$

where $\langle v^2\rangle$ is the mean velocity squared of the particles in the box.

<details>
  <summary>Proof</summary>

When particles bounce on the walls, the collisions are supposed to be elastic, which mean that they do not loose energy and hence the length of their velocity vector remains the same. However, they direction of their velocity changes.

To get to the pressure, which is the force exerted by the particle over the wall's surface $(P=\|\vec{F}\|/S)$, we need to express the linear momentum they transfer to the walls as $\vec{F}=d\vec{p}/dt$.

The problem can be treated in full generality, which is a bit more complicated, so let us simplify it maximally in order to get an intuition of what is happening. A full satisfying treatment will be delayed to the statistical mechanics class. Consider then a single particle of velocity $\vec{v}=v_x \vec{u}_x$ bouncing back and forth between two walls of surface $S=L\times L$ in the $(y,z)$ plane, while the particle is moving in the single dimension $x$.

When it bounce of the wall, the length of the velocity will not change, but it's derection will, such that it goes from $\vec{v}$ before the collision, to $-\vec{v}$ after the collision. The total change of linear momentum is thus $\Delta \vec{p} = m\Delta \vec{v}= m(\vec{v}-(-\vec{v}))=2mv_x\vec{u}_x$ (you can convince yourself that this is true in general, even if the particle moves with a general velocity vector).

Let's assume that the particle is moving in a cubic box of length $L$, then the typical time between two collision is given by the time for the particle to go back and forth between two opposite walls. It will move a total distance of $2L$ at a velocity $v$, such that $v_x=2L/\Delta t \Rightarrow \Delta t=2L/v_x$.

The total force it will exert on a single wall, will hence be

$$\|\vec{F}\|=\frac{\| \Delta \vec{p}\|}{\Delta t} = \frac{2mv_x}{2L/v_x}= \frac{mv_x^2}{L}$$

Now, the pressure exerted by this single particle on the wall is

$$P_x= \frac{\|\vec{F}\|}{S}=\frac{mv_x^2}{L^3}=\frac{mv_x^2}{V}$$

Now assume we have a big number $N$ of particles doing the same thing in the 3 dimensions of space and in all random directions. Hence, each particle will exert a pressure $p$ on each wall, with mean velocity distributed along the 3 directions of space. As there is no reason why the particles should move faster in a direction than another, we have $\langle v_x^2 \rangle=\langle v_y^2\rangle=\langle v_z^2\rangle$. The length of the mean total velocity should then be $\langle v\rangle=(\langle v_x^2\rangle+\langle v_y^2\rangle+\langle v_z^2\rangle)=3\langle v_x^2\rangle$. Hence, $\langle v_x^2\rangle=\langle v^2\rangle/3$ and the total pressure $P$ exerted by all the particles on the wall is given by

$$P= N\langle p\rangle=\frac{N m\langle v_x^2\rangle}{V}=\frac{N m\langle v^2\rangle}{3V}$$

</details>

Now, we will assume that the law of ideal gas is true. We can think of it as an experimental verified fact. We will re-demonstrate it from first principles in the statistical mechanics class.

Using it and our expression for the pressure, we can derive that the total energy of the particles (and hence the gas) is

$$\boxed{U = \frac{3}{2}n\mathcal{R}T=\frac{3}{2}Nk_BT},$$

Such that the average kinetic energy per particle is directly related to the temperature as

$$\boxed{\frac{1}{2}m\langle v^2\rangle = \frac{3}{2}k_B T}$$

<details>
  <summary>Proof</summary>
  
The total mean kinetic energy is 

$$U=E_C =  \frac{N}{2}m \langle v^2\rangle$$

Multiplying the expression we obtained above for $P$ by the volume $V$, we have

$$PV =  \frac{N}{3} m \langle v^2\rangle$$

$$ PV = \frac{2}{3} \left(\frac{N}{2}m\langle v^2\rangle\right) = \frac{2}{3} U$$

Adding the ideal gas law

$$\frac{3}{2} n\mathcal{R}T = U$$

</details>

Hence, when you feel that something is warm, it is nothing else but the "kinetic energy" of the microscoping particles bouncing on your hand! We can even use this expression to estimate the mean velocity of a particle in a room to be $v\sim$ 500 m/s = 1836 km/h!

<details>
  <summary>Exercice: estimate the mean velocity for the air in a room </summary>
  
Isolating $v$ in the above equation, and ussiming extremely grossly that $\langle v\rangle ~ \sqrt{\langle v^2\rangle}$, we obtain:

$$ \langle v \rangle \sim \sqrt{\frac{3k_BT}{m}}$$

Using $k_B=1,380649\times 10^{−23} J/K$, $T=27^{\circ}= 300$ K and finding the density of the typical density for air to be 28,96 g/mol, we obtain

$$ \langle v \rangle = 510 m/s$$

</details>

The above expression also demonstrates Joule's second law, stating that $U$ depends solely of $n$ and $T$ for an ideal gas.

## Beyond the ideal gas