---
layout: default
title: Phase space
parent: thermo
nav_order: 1
---

## Continuous variables in phase space

Now that we understood carefully the case of a system with discrete energy levels that are accessed randomly (like a die being continuously drawn), we are ready to move towards a more realistic statistical description of a physical system.

The complete description of a classical system, like a box of gas, is given by a single point in phase space. Before going further, you might want to first have a look at the [analytical mechanics](../../_meca/meca.md) class, which will be indispensable from now on. This lecture is significantly more advanced than the previous ones, you can try to follow it as much as possible and gloss over the details you do not understand and try to reconnect with the next lectures, where only the key formula and concepts will be needed.

Phase space is the space made of the positions $q_i$ and momentum $p_i$ of classical particles. For a single particle moving in three dimensions, it is thus a space of six dimension. A point $\Gamma$ in phase space is a sixtuplet $(q_1,q_2,q_3,p_1,p_2,p_3)$. In simple Cartesian coordinates $q_1=x,q_2=y,q_3=z$. The evolution of a particle moving through time will be given by a trajectory $\Gamma(t)$ in this space. For $\mathcal{N}$ particles moving in three dimensions, this space is of dimension $6\mathcal{N}$. A point would be labelled by the huge set of numbers:

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

We say that $H$ is the **generator** of time translations (similarly $p_i$ would generate space translations and angular momentum $L_i$ would generate rotations). 
From this equation, one can infer the evolution of a microstate through time ($q_i$ and $p_i$ are coordinates of $\Pi$ and are as such time independent observables), giving the **Hamilton equations**:

$$ \begin{cases}
\begin{align}
\frac{\text{d}q_i}{\text{d}t}&= \{q_i,H\}= -\frac{\partial H}{\partial p_i}\\
\frac{\text{d}p_i}{\text{d}t}&=\{p_i,H\}= \frac{\partial H}{\partial q_i}
\end{align}
\end{cases}
$$

An observable is conserved if it does not depend explicitely on time and if it commutes with the Hamiltonian $\lbrace f, H\rbrace=0$.
As such, energy is concerved through the time evolution of the system, as long as the Hamiltonian is not a function of time $t$, since $\lbrace H,H\rbrace =0$.

For general systems, the probability density must also be a function of time $\rho(\Gamma,t)$. As such, $\rho$ will also evolve according to

$$ \frac{\text{d}\rho}{\text{d}t}= \{\rho,H\} + \frac{\partial \rho}{\partial t}$$

**Liouville theorem** states that volumes in phase space are conserved through time evolution, which is equivalent to require a conservation of the probability along the flows in phase space. This condition lead to:

$$\boxed{\frac{\text{d}\rho}{\text{d}t}= 0.}$$ 

<details markdown="1">
  <summary><strong>Proof:</strong> </summary>

$\rho$ is a probability distribution of the microstate to be at a point $\Gamma$ of phase space. Probability must be conserved locally, the system can not disapear! If probability density change at a point, it should be "transferred" in another region of phase space. This implies that $\rho$ must satisfy a continuity equation over the $6\mathcal{N}$ dimensional phase-space

$$\frac{\partial \rho}{\partial t} = \vec{\nabla}_{q,p}\cdot(\rho\vec{v})$$

where 

$$\vec{\nabla}_{q,p}= \left(\frac{\partial}{\partial q_1},...,\frac{\partial}{\partial q_{3\mathcal{N}}},\frac{\partial}{\partial p_1}...,\frac{\partial}{\partial p_{3\mathcal{N}}}\right)$$

is the divergence over phase space and 

$$\vec{v}= \left(\frac{d q_1}{\text{d}t},...,\frac{d q_{3\mathcal{N}}}{\text{d}t},\frac{d p_1}{\text{d}t},...,\frac{d p_{3\mathcal{N}}}{\text{d}t}\right)$$

is the velocity of the microstate in phase space.
This is perfectly analogous to continuituy equation in fluid mechanics. It state that if probability density is not created out of nowhere, if the value of $\rho$ decrease at one point of phase space, it must "go out of it", and if it increases some probability must "go in".

The divergence is:

$$
\begin{align}
\vec{\nabla}_{q,p}\cdot(\rho\vec{v})= \vec{\nabla}_{q,p}(\rho)\cdot\vec{v} + \rho\vec{\nabla}_{q,p}\cdot\vec{v}
\end{align}
$$

such that the continuity equation becomes:

$$ \frac{\partial \rho}{\partial t} + \vec{\nabla}_{q,p}(\rho)\cdot\vec{v} = - \rho\vec{\nabla}_{q,p}\cdot\vec{v} $$

the left hand side is:

$$ \frac{\partial \rho}{\partial t} + \vec{\nabla}_{q,p}(\rho)\cdot\vec{v} = \frac{\partial \rho}{\partial t} + \sum_i \frac{\partial\rho}{\partial q_i}\frac{\partial q_i}{\partial t} + \sum_i \frac{\partial\rho}{\partial p_i}\frac{\partial p_i}{\partial t}  = \frac{\text{d}\rho}{\text{d}t}$$

the right hand side is:

$$
\begin{align}
- \rho\vec{\nabla}_{q,p}\cdot(\vec{v})&= - \rho\sum_i \left( \frac{\partial}{\partial q_i}\frac{\partial q_i}{\partial t} + \frac{\partial}{\partial p_i}\frac{\partial p_i}{\partial t} \right)\\
&= - \rho \sum_i\left(\frac{\partial^2 H}{\partial q_i \partial p_i} -\frac{\partial^2 H}{\partial p_i \partial q_i}  \right)\\
&=0
\end{align}
$$

where we re-injected Hamilton's equations and used the fact that second order derivative of a function commutes.
Hence:

$$\frac{\text{d}\rho}{\text{d}t}= 0$$

</details>

From this, we can write:

$$  \frac{\partial \rho}{\partial t}=\{H,\rho\} $$

**Thermal equilibrium** can be understood as $\rho(\Gamma)$ that is $ \frac{\partial \rho}{\partial t}=0$. In this case $\lbrace H,\rho\rbrace=0$ which is true only for functions $\rho(H)$.
Condition for which ergodicity can be assumed to be valid. Furthermore, most of the high dimensional systems display **chaotic** evolution, meaning that very nearby initial conditions in phase space ends up diverging and exploring very different regions of phase space. This property quickly spread probability distributions over $\Pi$, easing the ergodicity and leading to thermal equilbrium. 

## Entropy in phase space

For continuous cases, the entropy takes the form

$$\boxed{S = -\int_{\Pi} \rho(\Gamma)\ln(\rho(\Gamma)) \text{d}\Gamma}$$

which is the straightforward generalisation of our previous expression for the discrete case.

We can, as for the discrete case, looking for probability densities over phase space $\rho(\Gamma)$, which maximizes $S$ under some constraints. Again, the justification for doing so is to look for $\rho$ that reflect our knowledge of the system, maximizing our ignorance in order to avoid adding extra assumptions.

We will see that doing so gives back identical formula than the ones found in the discrete case, replacing sum over the energy states by integrals over phase space. As such, our understanding of the discrete case will translate directly here.

If nothing is known except the normalisation of probabilities, we find the probability distribution for the **microcanonical ensemble**:

$$\boxed{\rho(\Gamma) = \frac{1}{\Omega}}$$

where $\Omega = \int_\Pi \text{d}\Gamma$ is the total phase space-volume. All microstates are **equiprobable**. This is sometimes taken to be the **fundamental postulate** of statistical mechanics. Indeed, assuming this, it is possible to derive the expression for the other ensembles without invoking the maximisation of entropy, as discussed in [this lecture](./generating_function.md).
If we were to focus on specific regions of phase space with a given value of energy, we would find $\rho(E)=1/\Omega(E)$, which is equivalent to the discrete case with degeneracies $g$. The probability density is thus proportional to the volume occupied in phase space by the energy value. 

<details markdown="1">
  <summary><strong>Proof:</strong> </summary>

The proof is similar to the discrete case. We want to maximize $S$, under the two following constraints:

$$ \int_\Pi \rho(\Gamma)\text{d}\Gamma=1$$

Using the Lagrange multiplier methods exactly as before, we obtain

$$ \mathcal{L} = -\int_{\Pi} \rho(\Gamma)\ln(\rho(\Gamma)) \text{d}\Gamma - \alpha(\int_\Pi \rho(\Gamma)\text{d}\Gamma-1)$$

Now, analoguously to what is done to obtain Euler-Lagrange equations in mechanics (where $\mathcal{L}$ here plays the role of an action $\mathcal{S}$), we should set

$$\delta \mathcal{L} = \int_{\Pi}\frac{\delta \mathcal{L}}{\delta \rho}\delta \rho \text{d}\Gamma=0 \, ,\ \forall \delta \rho \leftrightarrow \frac{\delta \mathcal{L}}{\delta \rho} = 0$$

Hence:

$$ \delta \mathcal{L} = -\int_{\Pi} \delta\rho(1+\ln(\rho)) \text{d}\Gamma - \alpha \int_{\Pi}\delta \rho \text{d}\Gamma = -\int_{\Pi} \delta \rho \left(1+\ln(\rho)+\alpha\right)\text{d}\Gamma=0$$

which means

$$-(1+\ln(\rho)+\alpha)=0$$

and hence

$$\rho = e^{-1-\alpha}$$

$\alpha$ is fixed from the condition on the normalisation of probabilities

$$\int_{\Pi} \rho \text{d}\Gamma = \int_{\Pi}\text{d}\Gamma e^{-1-\alpha}=1$$

leading to:

$$ \alpha = \ln(\Omega)-1$$

where we fixed $\Omega= \int_{\Pi} \text{d}\Gamma$.

Hence:

$$\rho = \frac{1}{\Omega} $$

</details>

If we re-inject this formula in the entropy, and re-inject the Boltzmann constant to consider the thermodynamic entropy, we find that 

$$\boxed{S_{\rm th} = k_B\ln(\Omega)}$$

The entropy is the logarithm of the volume occupied by the microstates of interest in phase space. This is the formula that is written on Ludwig Boltzmann's grave! As we will discuss below, it is indeed important to understand the second principle and irreversibility in a statistical context.

If the mean value of $H$ is "forced" by a thermostat to take a mean value $U$, we obtain instead:

$$\boxed{\rho(\Gamma)= \frac{1}{Z}\int e^{-\beta H} \text{d}\Gamma}$$

with the partition function being:

$$ Z = \int_{\Pi} e^{-\beta H(\Gamma)} \text{d}\Gamma$$

We see that these expressions are a straightforward generalisation of the discrete case considered in the previous lectures ($p_i = e^{-\beta E_i}/Z$ and $Z= \sum_i e^{-\beta E_i}$), replacing the sum over each microstate by an integral over phase-space. This is probability density for the **canonical ensemble**.

<details markdown="1">
  <summary><strong>Proof:</strong> </summary>

We want to maximize $S$, under the two following constraints

$$ \int_\Pi \rho(\Gamma)\text{d}\Gamma=1$$

and

$$\int_\Pi \rho(\Gamma)H(\Gamma) \text{d}\Gamma= \langle E \rangle$$

The second equation means that our microstates are "forced" to follow trajectories in phase space for which the mean value of the Hamiltonian is $\langle E \rangle$.

Using the Lagrange multiplier methods exactly as before, we obtain

$$ \mathcal{L} = -\int_{\Pi} \rho(\Gamma)\ln(\rho(\Gamma)) \text{d}\Gamma - \alpha(\int_\Pi \rho(\Gamma)\text{d}\Gamma-1) - \beta(\int_\Pi \rho(\Gamma)H(\Gamma) \text{d}\Gamma- \langle E \rangle)$$

$$ \delta \mathcal{L} = -\int_{\Pi} \delta\rho(1+\ln(\rho)) \text{d}\Gamma - \alpha \int_{\Pi}\delta \rho \text{d}\Gamma = -\int_{\Pi} \delta \rho \left(1+\ln(\rho)+\alpha + \beta H\right)\text{d}\Gamma=0$$

$$-(1+\ln(\rho)+\alpha+\beta H)=0$$ 

and hence 

$$\rho = e^{-1-\alpha - \beta H} = \frac{1}{Z}e^{-\beta H}$$

$Z= e^{1+\alpha}$ is fixed using the normalisation of probabilities:

$$\int_{\Pi} \rho \text{d}\Gamma = \int_{\Pi}\frac{1}{Z}e^{- \beta H}\text{d}\Gamma =1 $$

and then:

$$Z= \int_{\Pi} e^{-\beta H}\text{d}\Gamma$$

</details>

## The second principle of thermodynamics in phase space

Due to chaotic behaviour, two points with close initial conditions will spread. Volume in coarse grained phase space increases.
The system will occupy all of its available volume in phase space.

Fundamental laws of nature are revesible. But most of macroscopic phenomenon seems irreversible. How to solve this paradox?
On large scales, reversibility is not impossible, it's just extremely unlikely.

Consider a large room completely empty. Consider taking a small box with $\mathcal{N}$ particle of gas bouncing. If you open the small box and let the particles enter in the room, they will occupy all of phase space. Entropy will increase as the probability density will start to be non zero in the room (2nd principle) The chances that all particles return in the small box is extremely small (irreversibility).

This has some links with the unidirectionality of the **flow of time** in a very complicated and yet partialy understood fashion.

## Integrating over phase space: a measure problem

We saw in the previous lectures that the partition function $Z$ is a key function in order to rederive physical quantities of interest. The challenge in order to apply this to concrete problems will then be to compute explicitely the integral over phase-space. To do so, we must clarify what is this $\text{d}\Gamma$ that we integrate over.

Considering a system made of $\mathcal{N}$ classical point particles, then the integral over phase space is naturally expected to be of the form

$$\text{d}\Gamma = \text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p  $$

which gives the value of an infinitessimal $6\mathcal{N}$ dimensional volume of phase space. This is the so-called **Liouville measure** over phase space.
It is easy to get fooled by simplifying notations, and sometimes, we gain to be painfuly explicit. So, just to be clear, this should be understood as 

$$
\begin{align}
\text{d}\Gamma & = \text{d}^{3\mathcal{N}}q \, \text{d}^{3\mathcal{N}}p\\
& = \text{d}q_1...\text{d}q_{3\mathcal{N}}\text{d}p_1...\text{d}p_{3\mathcal{N}}
\end{align}
$$

However here, a very subtle point comes into play. A crucial point is whether or not the particles are **distinguishable** or not. This might look like a silly question, but we will see later on that it has a huge impact in the case of quantum physics.
If particles are distinguishable, you could imagine giving them a name, or a color, such that, at any time, you are able to locate "bob" or "paul". As such, each of the possible particle configuration (microstate) is truely and funamentaly different.
If particles are indistinguishable, you could imagine interchanging them which would not change anything at all. As such every "swap" of the particles would give the same microstate.
If so, we should divide by the number of possible rearangement that give the same microstate when counting the states, which is $\mathcal{N}!$. In classical physics, we usually consider that particles are indistiguishable, which we make explicit by correcting the extra counting in the integrals over phase space, by considering the alternative measure:

$$\text{d}\Gamma = \frac{\text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p}{\mathcal{N}!}  $$

One last issue must be addressed: as introduced above, the phase-space measure $\mathrm{d}\Gamma$ is not dimensionless, but carries units of
$(\text{length} \times \text{momentum})^{3\mathcal{N}},$
i.e. units of an action raised to the power $3\mathcal{N}$. As a consequence, the phase-space density $\rho(\Gamma)$ cannot be dimensionless, as a probability density should be, but must instead carry units of $(\text{action})^{-3\mathcal{N}}$ in order to satisfy the normalization condition
$
\int \rho(\Gamma)\,\mathrm{d}\Gamma = 1.
$ This reflects the fact that classical mechanics does not provide a natural, dimensionless measure on phase space. In order to define a dimensionless probability density, one must therefore normalize the phase-space volume element by a reference action scale raised to the power $3\mathcal{N}$. Equivalently, this amounts to introducing an elementary cell of finite volume in phase space.

The physically well-motivated way to fix this scale is obtained by considering the classical limit of quantum mechanics, which naturally introduces a fundamental unit of action given by Planck’s constant $h$. It is possible to show (and we will not show it now!) that this leads to the well motivated phase-space measure

$$
\mathrm{d}\Gamma = \frac{\mathrm{d}^{3\mathcal{N}}q\,\mathrm{d}^{3\mathcal{N}}p}{\mathcal{N}!\,h^{3\mathcal{N}}},
$$

In the following, and until the discussion of quantum statistics, we will adopt units in which $h = 1$ for simplicity, with the understanding that the appropriate powers of $h$ can be restored when required.


### Pressure, temperature and so on

You can convince yourself that all the formula we derived in the previous lecture for the canonical ensemble (constrained mean energy) remain all valid in this continuous case. 
The expressions for $T$ and $P$ as derivatives of energy where definitions, and they have no reason to change in this continuous context.

The expressions which express relevant quantities in term of $Z$ are:

$$U = \frac{\partial \ln(Z)}{\partial \beta}$$

$$S = \beta U + \ln(Z)$$

$$P = \frac{1}{\beta}\frac{\partial \ln(Z)}{\partial V}\Bigg|_{T}$$ 

All of them can be prooved identically as in the discrete case, simply by carefully replacing sums by integrals. It is a good exercice to see if you can remember how the proof went in the discrete case.

<details markdown="1">
  <summary><strong>Proof:</strong> </summary>

Starting with the mean energy, we have 

$$U = \langle H \rangle = \int \rho(\Gamma) H(\Gamma) \text{d}\Gamma$$

replacing the expression for the probability density, we find

$$U =  \int \frac{e^{-\beta H(\Gamma)} H(\Gamma)}{Z} \text{d}\Gamma$$

Now, on the other hand we have

$$\frac{\text{d}Z}{\text{d}\beta} = \int -H(\Gamma)e^{-\beta H(\Gamma)} \text{d}\Gamma $$

So, by identifying the two expressions, we conclude that (remember that $Z$ is just a number once the integral is done):

$$U = -\frac{1}{Z}\frac{\text{d}Z}{\text{d}\beta}= -\frac{\partial \ln(Z)}{\partial \beta} $$

Looking now at the expression for $S$:

$$
\begin{align}
S&=- \int \rho(\Gamma)\ln(\rho(\Gamma))\text{d}\Gamma\\
&=- \int \frac{e^{-\beta H(\Gamma)}}{Z} \left(-\beta H(\Gamma) -\ln(Z)\right) \text{d}\Gamma \\
&= \int \frac{e^{-\beta H(\Gamma)}}{Z} \left(\beta H(\Gamma) +\ln(Z)\right) \text{d}\Gamma \\
&=  \beta\int \frac{e^{-\beta H(\Gamma)}}{Z}\text{d}\Gamma  + \ln(Z) \frac{1}{Z}\int e^{-\beta H(\Gamma)}\text{d}\Gamma\\
&= \beta U + \ln(Z)
\end{align}
$$

Now, the proof of the expression for $P$ presented in the discrete case was totally independent of the discretness of the microstates. You can copy it identically to obtain

$$P = \frac{1}{\beta}\frac{\partial \ln(Z)}{\partial V}\Bigg|_{T}$$ 


</details>

