---
layout: default
title: Phase space
parent: thermo
nav_order: 1
---

## Continuous variables in phase space

Now that we understood carefully the case of a system with discrete energy levels that are accessed randomly (like a die being continuously drawn), we are ready to move towards a more realistic statistical description of a physical system.

The complete description of a classical system, like a box of gas, is given by a single point in phase space. Before going further, you might want to first have a look at the [analytical mechanics](../../_meca/meca.md) class, which will be indispensable from now on.

As a reminder, phase space is the space made of the positions $q_i$ and momentum $p_i$. For a single particle moving in three dimensions, it is thus a space of six dimension. A point $\Gamma$ in phase space is a sixtuplet $(q_1,q_2,q_3,p_1,p_2,p_3)$. In simple Cartesian coordinates $q_1=x,q_2=y,q_3=z$. The evolution of a particle moving through time will be given by a trajectory $\Gamma(t)$ in this space. For $\mathcal{N}$ particles moving in three dimensions, this space is of dimension $6\mathcal{N}$. A point would be labelled by the huge set of numbers:

$$\Gamma=(q_1^{(1)}, q_2^{(1)},q_3^{(1)}, ... q_1^{(\mathcal{N})}, q_2^{(\mathcal{N})},q_3^{(\mathcal{N})}..., p_1^{(1)}, p_2^{(1)},p_3^{(1)}, ... p_1^{(\mathcal{N})}, p_2^{(\mathcal{N})},p_3^{(\mathcal{N})})
$$

where the upper index in parenthesis label the particle and the lower index label the different coordinates.

Such a point $\Gamma$ label a specific particle configuration. If $\Gamma$ describes the actual state of a system at a given time, it will then evolve with time to give a trajectory over phase space, $\Gamma(t)$, following Euler-Lagrange equations, or equivalently Hamilton equations or the flow of the Hamilton vector in the context of sympectic geometry depending on the theoretical framework under consideration.

We easily understand how complicated it would be to solve such equations in the case of an extemely large number of particles, as the ones contained within a box of gas.
Instead of treating this problem exactly -- which is in practice impossible -- we will treat it statistically, by considering some probability that the system is located within a given volume of phase space.
To do so, let's first start with some reminder regarding continuous probability distributions.

## Continuous probability distributions

In the previous classes, we considered variables which could take values only within a discrete set of possibilities, labelled by an index $i$, to which was associated a probability $p_i$ (recall the case of the die with $i\in \{1,2,3,4,5,6\}$ and $p_i=1/6$, $\forall i$).

We now want to generalize this concept for continuous variable, that can take any values within the real numbers. Consider for example the probability that a particle is located at position $x$. In such a situation, we replace the concept of probability, by the one of **probability density function** $\rho(x)$. This function is such that the probability that the particle is located between a position $a$ and $b$ is given by the integral

$$p(a<x<b) = \int_a^b \rho(x) \text{d}x$$

or, another way to put it is that the infinitesimal probability $\text{d}p$ that $x$ can be found in the infinetismal interval $\[x-\text{d}x,x+\text{d}x\]$ around the point $x$ is

$$\text{d}p = \rho(x) \text{d}x$$

The normalisation of probability ($\sum_i p_i=1$) then takes the form in the continuous case:

$$ \int_{\mathbb{R}} \rho(x) \text{d}x = 1 $$

and the mean of a function $f(x)$ becomes

$$ \langle f \rangle = \int_{\mathbb{R}} \rho(x)f(x) \text{d}x $$

What will interest us, is the density probability associated to $x$ where $x$ is a position in phase space for the system, that is, for example, a complete configuration of all the positions and velocities/momentum of all the particles contained in a box of gas. To do so, we will consider the $6\mathcal{N}$ dimensional probability distribution, labelled by $\Gamma$ instead of $x$.

## Probability density in phase space

Let us now label by $\Gamma$ the position of a point in phase space, i.e. the whole set of positions $q^{(1)}_1,q^{(1)}_2...$ and momentums $p_1^{(1)},p_2^{(1)}...$ for each particle. A **microstate**, discussed in previous lectures, is corresponding exactly to a given value of $\Gamma$. Noting the phase space $\Pi$ (or quite pretentiously as $\Pi=TQ^{\*}$ for reasons that will only be clear in the differential geometry classes), then $\Gamma \in \Pi$.

To alleviate the notations and emphasize on the $6\mathcal{N}$ dimensional aspect of phase space, we will now label the $q$ and the $p$ between $1$ and $3\mathcal{N}$, going over all the particles, that is:


$$

\begin{cases}
q_1,q_2,q_3,q_4,q_5,q_6 ... q_{3\mathcal{N}} &= q^{(1)}_1,q^{(1)}_2,q^{(1)}_3, q^{(2)}_1,q^{(2)}_2,q^{(2)}_3..., q^{(\mathcal{N})}_3 \\

p_1,p_2,p_3,p_4,p_5,p_6 ... p_{3\mathcal{N}} &= p^{(1)}_1,p^{(1)}_2,p^{(1)}_3, p^{(2)}_1,p^{(2)}_2,p^{(2)}_3..., p^{(\mathcal{N})}_3 
\end{cases}
$$

Hence phase space really has to be thought of as a large $6\mathcal{N}$ dimensional space (similarly to how space time is a 4 dimensional one) which can be coordinized with $3\mathcal{N}$ coordinates of $q$ and $3\mathcal{N}$ coordinates of $p$ (just as space-time can be coordinized with 3 $x$ "space" coordinates and 1 $t$ "time" coordinate). This will make our discussion a bit more abstract, but much simpler. You should always try to keep in mind what is the meaning of these coordinates, and come back here in case of need.

Our system will then evolve in time, following a trajectory $\Gamma(t)$ in phase space, dictated by the Hamiltonian/Lagrangian. Formally, $\Gamma(t)$ is a curve in phase space $\mathbb{R}\to \Pi$.

An **observable** $f$, is a function on phase space, which associate to each $\Gamma$ a real number (that is $f: \Pi \to \mathbb{R}$). Examples of observable is for example, the energy $E(\Gamma)$ associated with the microstate $\Gamma$.

We can associate to each $\Gamma \in \Pi$ a probability density $\rho(\Gamma)$ which takes values in the real numbers is an observable as defined above. The value of $\rho(\Gamma)$ over the whole phase space is what represent the **macrostate** of the system.

The time (empirical) average value of an observable $f(\Gamma)$ along the curve, after a duration $\mathcal{T}$, is given by  

$$ \overline{f} = \frac{1}{\mathcal{T}}\int_0^\mathcal{T} f(\Gamma(t)) \text{d}t,$$

which generalizes the discrete expression introduced in the supplement of the [first lecture](.//entropy.md). When the period over which the measurement is done is very large ($\mathcal{T}\to \infty$), the empirical average is expected to reflect the statistical mean, that is:

$$\overline{f}= \langle f \rangle.$$

where

$$ \langle f \rangle = \int_{P} \rho(\Gamma)f(\Gamma) \text{d}\Gamma $$

If so, the empirical mean reflects the properties of the underlying theoretical probability density $\rho$. It assumes that, through its time evolution, the system will explore the whole phase space, with more time spent in regions where $\rho(\Gamma)$ has a larger value.
Such a property is called **ergodicity**, which is characteristic of system at thermal equilibrium. Indeed, for systems with a fast evolution, $\rho$ might change with time, such that this property is not satisfied. A similar problem happens for systems with very few interactions betweens its constituents, in which the whole phase space can not be explored.

## Liouville's theorem and equilibrium

One way to consider the time evolution of microstates, is that it is dictated by a very special observable, the Hamiltonian $H$. $H(\Gamma)$ can be identified with what was called $E_i$ in the discrete case. It is the total energy of a microstate, and hence of a particle configuration.

As discussed in the analytical mechanics class, Hamiltonian defines the time evolution of any observable. It is done through the very important concept of Poisson bracket $\lbrace.,.\rbrace$, which encodes a lot about the geometry and symmetries of phase space.

The Poisson bracket $\lbrace f,g\rbrace$ between two observables $f$ and $g$ is the new observable:

$$\{f,g\} = \sum_i^{3\mathcal{N}} \left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} -  \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right) $$

The time evolution of any observable $f$ is given by:

$$\frac{\text{d}f}{\text{d}t}=\{f,H\} + \frac{\partial f}{\partial t}$$

For general systems, the probability density must also be a function of time $\rho(\Gamma,t)$. As such, $\rho$ is expected to change as

$$ \frac{\text{d}\rho}{\text{d}t}= \{\rho,H\} + \frac{\partial \rho}{\partial t}$$


**Liouville theorem** volumes in phase space are conserved leading to $\frac{\text{d}\rho}{\text{d}t}= 0$.

$$  \frac{\partial \rho}{\partial t}=\{H,\rho\} $$

**Thermal equilibrium** can be understood as $\rho(\Gamma)$ that is $ \frac{\partial \rho}{\partial t}=0$. In this case $\lbrace H,\rho\rbrace=0$ which is true only for functions $\rho(H)$.
Condition for which ergodicity can be assumed to be valid.


## Entropy in phase space

For continuous cases, the entropy takes the form

$$\boxed{S = -\int_{\Pi} \rho(\Gamma)\ln(\rho(\Gamma)) \text{d}\Gamma}$$

which is the straightforward generalisation of our previous expression for the discrete case.

We can, as for the discrete case, looking for probability densities over phase space $\rho(\Gamma)$, which maximizes $S$ under some constraints. Again, the justification for doing so is to look for $\rho$ that reflect our knowledge of the system, maximizing our ignorance in order to avoid adding extra assumptions.

We will see that doing so gives back identical formula than the ones found in the discrete case, replacing sum over the energy states by integrals over phase space. As such, our understanding of the discrete case will translate directly here.

If nothing is known, we find the **microcanonical ensemble**:

$$\rho(\Gamma) = \frac{1}{\Omega(E)}$$

<details markdown="1">
  <summary><strong>Proof:</strong> </summary>

The proof is very similar to the discrete case.

We want to maximize $S$, under the two following constraints

$$ \int_\Pi \rho(\Gamma)\text{d}\Gamma=1$$
The second equation means that our microstates are "forced" to follow trajectories in phase space for which the mean value of the Hamiltonian is $\langle E \rangle$.

Using the Lagrange multiplier methods exactly as before, we obtain

$$ \mathcal{L} = -\int_{\Pi} \rho(\Gamma)\ln(\rho(\Gamma)) \text{d}\Gamma - \alpha(\int_\Pi \rho(\Gamma)\text{d}\Gamma-1) - \beta(\int_\Pi \rho(\Gamma)H(\Gamma) \text{d}\Gamma- \langle E \rangle)$$


</details>

If the mean value of $H$ is "forced" by a thermostat to take a mean value:

$$\rho(\Gamma)= \frac{1}{Z}\int e^{-\beta H} \text{d}\Gamma$$

where $Z$ is further discussed in the next section.

<details markdown="1">
  <summary><strong>Proof:</strong> </summary>

We want to maximize $S$, under the two following constraints

$$ \int_\Pi \rho(\Gamma)\text{d}\Gamma=1$$

and

$$\int_\Pi \rho(\Gamma)H(\Gamma) \text{d}\Gamma= \langle E \rangle$$

The second equation means that our microstates are "forced" to follow trajectories in phase space for which the mean value of the Hamiltonian is $\langle E \rangle$.

Using the Lagrange multiplier methods exactly as before, we obtain

$$ \mathcal{L} = -\int_{\Pi} \rho(\Gamma)\ln(\rho(\Gamma)) \text{d}\Gamma - \alpha(\int_\Pi \rho(\Gamma)\text{d}\Gamma-1) - \beta(\int_\Pi \rho(\Gamma)H(\Gamma) \text{d}\Gamma- \langle E \rangle)$$


</details>


## Integrating over phase space: a measure problem

In the last classes, we saw that a critically important concept was the one of partition function $Z$, defined as

$$Z= \sum_i e^{-\beta E_i}$$

where $E$ are all the energy level associated to each possible microstates $i$ (if several microstates are associated with the same energy, we introduced the concept of degeneracy $g$).

It's generalisation to the continous case is simply

$$ Z = \int_{\Pi} e^{-\beta H(\Gamma)} \text{d}\Gamma$$

replacing the sum over each microstate by an integral over phase-space. This is indeed the expression of $Z$ we found above when maximizing the entropy to obtain $\rho(\Gamma)$.

Considering a system made of $\mathcal{N}$ classical point particles, then the integral over phase space is of the form

$$\text{d}\Gamma = \text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p  $$

which gives the value of an infinitessimal $6\mathcal{N}$ dimensional volume of phase space. This is the so-called **Liouville measure** over phase space.
It is easy to get fooled by simplifying notations, and sometimes, we gain to be painfuly explicit. So, just to be clear, this should be understood as 

$$
\begin{align}
\text{d}\Gamma & = \text{d}^{3\mathcal{N}}q \, \text{d}^{3\mathcal{N}}p\\
& = \text{d}q_1...\text{d}q_{3\mathcal{N}}\text{d}p_1...\text{d}p_{3\mathcal{N}}
\end{align}
$$

In the next classes, we will have to compute explicitely integrals over phase space. For example, we will have to compute integrals of the form:

$$\int \text{d}^{3\mathcal{N}}q$$

For a single particle, contained (and thus forced to move) within a container of gas of volume $V$, we expect:

$$\int_{\Pi} \text{d}^{3}q = \iiint\text{d}q_1\text{d}q_2\text{d}q_3 = V$$

For $\mathcal{N}$ particles, we have 

$$
\begin{align}
\int_{\Pi} \text{d}^{3\mathcal{N}}q &= \iiint \text{d}q_1\text{d}q_2\text{d}q_3\text{d}q_4\text{d}q_5\text{d}q_6 ... \text{d}q_{3\mathcal{N}-2}\text{d}q_{3\mathcal{N}-1}\text{d}q_{3\mathcal{N}}\\
 &=\iiint \text{d}q_1\text{d}q_2\text{d}q_3\iiint\text{d}q_4\text{d}q_5\text{d}q_6 ...\iiint \text{d}q_{3\mathcal{N}-2}\text{d}q_{3\mathcal{N}-1}\text{d}q_{3\mathcal{N}}
\end{align}
$$

where we should keep in mind that $q_1,q_2,q_3$ are the three coordinates of the first particle, $q_4,q_5,q_6$ are the three coordinates of the second particle and so on until the particle $\mathcal{N}$. As such, each of these integral will give again $V$, such that we will obtain $\mathcal{N}$ products of $V$. As such, we obtain

$$ \int_{\Pi} \text{d}^{3\mathcal{N}}q= V^{\mathcal{N}}$$

However here, a very subtle point comes into play. A crucial point is whether or not the particles are **distinguishable** or not. This might look like a silly question, but we will see later on that it has a huge impact in the case of quantum physics.
If particles are distinguishable, you could imagine giving them a name, or a color, such that, at any time, you are able to locate "bob" or "paul". As such, each of the possible particle configuration (microstate) is truely and funamentaly different.
If particles are indistinguishable, you could imagine interchanging them which would not change anything at all. As such every "swap" of the particles would give the same microstate.
If so, we should divide by the number of possible rearangement that give the same microstate when counting the states, which is $\mathcal{N}!$. In classical physics, we usually consider that particles are indistiguishable, which we make explicit by correcting the extra counting in the integrals over phase space, by considering the alternative measure:

$$\text{d}\Gamma = \frac{\text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p}{\mathcal{N}!}  $$

The integral over volumes can absorbe this extra factor to become:

$$\int_{\Pi} \frac{\text{d}^{3\mathcal{N}}q}{\mathcal{N}!}= \frac{V^{\mathcal{N}}}{\mathcal{N}!} $$


### Pressure, temperature and so on

You can convince yourself that all the formula we derived in the previous lecture for $T$, $S$, $U$, $P$ etc remain all valid in this continuous case. 