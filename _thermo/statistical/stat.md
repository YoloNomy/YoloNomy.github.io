---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---

$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

# Statistical physics in general

## Statistical physics, microstates and macrostates

The idea laying behind statistical mechanics will be to explain the observed behavior of large systems as the result of underlying microscopic subsystem. For exemple, we will be able to retrieve quite easily the ideal gas law by decomposing it as made of a gigantic number of free bouncing microscopic particles.

All of statistical mechanics lies on the distinction between macrostates and microstates:

- The *macrostate* of a system correspond to the state as described in classical thermodynamics. It is what you will measure about the system here and now: its temperature, pressure, volume etc

- The *microstate* of a system is the complete description of the system in term of its microscopic constituents.

As such, **several *microstates* can correspond to the same *macrostate***: you can think of an infinite amount of different ways to put particles of gas in a box which will give you the same measured pressure, temperature and volume.

Each microstate $i$ can be associated with a probability of occuring $p_i$. The entierty of statistical mechanics lies on the following statistical law: **The macrostate you will observe will be the more probable** that is the the macrostate which is associated with the highest number of probable microstates.

A way to quantify the likelihood of a macrostate is given by the *entropy*. The higher the entropy of a macrostate, the more microstates with high probabilities are associated with it, and hence the higher are the chances you will observe it.

<details>
  <summary>Basic probability theory</summary>
   

The sum of all probabilities 
$$\sum p_i=1$$

The average of the quantity $X$ is

$$\langle X \rangle = \sum_i p_i X_i$$
</details>

## Maximizing the entropy

Let $i$ label a discrete number of $N$ possible microstates associated with a macrostate of a system. Let $p_i$ be the probability for the system to be in the microstate $i$, such that $\sum_i p_i = 1$. We define the entropy of the macrostate $S$ as:

$$
\boxed{
S = -\sum_i p_i\ln{p_i} = \langle \ln(p_i)\rangle}
$$

For a system where all states are equiprobable, $p_i=1/N$ and:

$$
S = -\frac{1}{N}\sum_i^N\ln\left(\frac{1}{N}\right)= \ln(N)
$$

As such, if there is a single microstate $N=1$ explaining the whole macrostate, then the system is perfectly known and correspondingly the entropy is $S=0$. The more microstates $N$ associated to a macrostate, the bigger the entropy, as desired. The entropy hence quantifies how probable a macrostate is in term of its microstates. The observed macrostate of a system will be the one which maximizes $S$.

# Classical statistics up to the ideal gas

### Derivation of the probabilities of maximal entropy in the canonical ensemble ($N$ fixed).

Let's now traduce this idea in term of the familiar problem of particles in a box. Consider then a system, like a gas, with mean energy $\langle E\rangle$ (its macrostate). Assume that there exist $N$ distinguishable possible ways to re-arange the particles inside the box to give the same mean energy ($N$ possible microstate associated with the macrostate).

Let's label by $i$ the possible microstates, that is the possible particle configurations giving back the mean energy $\langle E\rangle$. To each microstate is associated an energy $E_i$. Some can be very weird, as e.g. all the particles being located in one corner of the box, or half having very high energies and the other half having very low energies. However, the great majority of these microstates are made of particles being distributed everywhere in the box with average temperatures. As such, these states will contribute much more to the entropy calculation and will be incredibly more probable.

For simplicity, we now assume that the accessible energy levels of the microstates $E_i$ are discrete. It will be straightforward to generalize this to the continuous case by replacing sums with integrals and taking limits toward infinity. Let $n_i$ be the occupation number that is the number of possible microstates (particle configurations) associated with the energy $E_i$. We have:

$$
\sum_i n_i = N
$$

The probability of a particle to be in the state $i$ is then simply:

$$
p_i = \frac{n_i}{N}
$$

Leading naturally from the above equation to

$$
\sum_i p_i = \sum_i \frac{n_i}{N} = 1
$$


The average energy of the macrostate is then expressed in term of the microstates as:

$$
\langle E \rangle  = \sum_i p_i E_i = \sum_i \frac{n_i}{N} E_i
$$

The number of possible ways to rearange the $N$ microstates into the possible allowed energy states with occupation numbers $n_i$ is given by:

$$
C^n_N = \frac{N!}{\prod_i n_i!}
$$

Maximizing $C^n_N$ will give us the most probable configuration of the $n_i$. It can be shown that this maximum is very sharp, making other configurations almost impossible.

If $N$ and $n_i \to \infty$, which is clearly the case here, we can use the *Stirling approximation*:

$$ N! \sim N^N e^{-N} $$

<details>
  <summary>Proof</summary>
  
$$
\begin{aligned}
\ln(N!) &= \sum_{x=1}^N \ln(x)
\\ &\sim \int_1^N dx \ln(x) \qquad (N\to \infty)\\
&= [x \ln(x)-x ]_1^N \\
&= N\ln N -N
\end{aligned}
$$

(One can verify easily that $\frac{d}{dx}(x\ln(x)-x=\ln(x)$). And then:

$$
N! \sim e^{N\ln N -N} = e^{\ln(N^N)}e^{-N} = N^N e^{-N}
$$

</details>

This approximation allows us to bring the entropy as:

$$ 
\ln(C^n_N)= NS
$$

<details>
  <summary>Proof</summary>

$$
\begin{aligned}
\ln(C)&= N\ln(N)- \sum_i n_i \ln(n_i)\\
&= Nln(N) - \sum_i p_i N \ln(p_iN)\\
& =  Nln(N) - \sum_i p_i N(\ln(p_i)+ \ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i)+ \sum_i N p_i\ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i)+ - N\ln(N))\\
& = N S
\end{aligned}
$$
</details>

Maximizing $C^n_N$ is thus equivalent to maximizing $S$. This will give us the most probable particle configurations within the box associated to the most probable $n_i$ combinations amongst the $N$ possible macrostates. As all this is very abstract, let us rephrase again exactly what we are doing here. You are having a gas and say that you are measuring one way or another that its mean energy is $\langle E\rangle$. Then you are thinking of the gas as made of particles, and you consider what are the most probable ways that these particles are arranged within the box. Particle configurations are classified by their energy $E_i$ and a number of corresponding configurations $n_i$ leading to this energy. If you could know it perfectly, the probability $p_i$ for the microstate of your particle box to be associate with the exact energy $E_i$ can be found by maximizing the entropy.

We will now do the entropy maximization using the so-called *Lagrange multipliers* and asking for the following constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i E_i &= \langle E \rangle \\
& \sum_i p_i  &= 1
\end{aligned}
\end{cases}
$$

asking respectively for the mean energy of a particle to be given by $\langle E \rangle$ and the sum of probabilities to be conserved.

<details>
  <summary>Lagrange multipliers</summary>
  
</details>

Once $S$ is maximized, we can obtain the probability for a single particle to be in the state of energy $E_i$:

$$
\boxed{p_i = \frac{1}{Z}e^{-\beta E_i}}
$$

With $Z$ the *partition function*:

$$
Z := e^{1+\alpha}
$$

and $\alpha$ and $\beta$ are the two Lagrange multipliers associated to our two constraints.

$Z$ can be simplified by re-inserting it again in the normalization of probabilities:

$$
\sum_i p_i = \sum_i \frac{1}{Z}e^{-\beta E_i} =1 
$$

Leading to:

$$
\boxed{Z = \sum_ie^{-\beta E_i}}
$$

The mean energy of the particle can then be re-expressed from $Z$ as

$$
\boxed{\langle E \rangle = -\frac{1}{Z}\frac{\partial Z}{\partial \beta} = -\frac{\partial{\ln Z}}{\partial \beta}}
\label{eq:E-of-Z}
$$

<details>
  <summary>Proof</summary>
 
Using the second constraints, we can relate $\langle E \rangle$ to $Z$ as:

$$
\sum_i p_i E_i = \sum_i \frac{1}{Z}e^{-\beta E_i}E_i= \langle E \rangle
$$

Seeing that:

$$
-\frac{1}{Z}\frac{\partial Z}{\partial\beta}= \sum_i \frac{E_i}{Z}e^{-\beta E_i}
$$

and so:

$$
\langle E \rangle = -\frac{1}{Z}\frac{\partial Z}{\partial \beta} = -\frac{\partial{\ln Z}}{\partial \beta}
$$
</details>

The entropy $S$ can also be rederived in terms of $Z$ as:

$$
\boxed{S = \beta \langle E \rangle + \ln Z}
$$

<details>
  <summary>Proof</summary>
 
$$
\begin{aligned}
S &= -\sum_i p_i \ln(p_i) \\
&= \sum_i\frac{1}{Z}e^{-\beta E_i}\left[ \beta E_i + \ln (Z)\right]\\
&= \beta \langle E \rangle + \ln (Z)\sum_i e^{-\beta E_i}
\end{aligned}
$$

And so:

$$
S = \beta \langle E \rangle + \ln Z
$$
</details>

While we got rid of $\alpha$, the second Lagrange multiplier $\beta$ can be expressed with respect to the temperature. To do so, we define the temperature as the change of energy associated with a change of entropy:

$$
\boxed{T := \frac{\partial \langle E \rangle}{\partial S}} 
\label{eq:defTemp}
$$

The next section will discuss why this definition is deep and connects with the intuitions you might have about temperature. With this definition

$$
\boxed{\beta = \frac{1}{T}}
$$

<details>
  <summary>Proof</summary>
 

$$
dS = \beta d\langle E\rangle + \langle E\rangle d\beta + \frac{\partial \ln Z}{\partial \beta}d\beta
$$

(using Eq.\ref{eq:entropy-of-E} and the fact that $Z$ is a function of only one independant variable $\beta$ or $\langle E \rangle$ since both are not independant because of Eq.\ref{eq:E-of-Z}. Now using Eq.\ref{eq:E-of-Z}, we can see that the two last terms cancels out to give simply: $dS = \beta d\langle E\rangle$. With the definition of $T$:

$$
T = \frac{\partial \langle E \rangle}{\partial S}
$$

Whe have $dS = \frac{1}{T}d\langle E\rangle$, allowing us to conclude that:

$$
\beta = \frac{1}{T}
$$
</details>


### On the definition of temperature

The temperature is defined above by Eq.\ref{eq:defTemp}.

Why is it a good definition:
- direction of heatflows
- broadening of $p(E)$ with increasing $\langle E \rangle$

### Defining Pressure

Pressure is not only a force over a surface but also a energy per unit of volume!

$$ P = -\frac{\partial{E}}{\partial{V}}\Bigg|_S$$

This is equivalent (but more convinient) that the the usual definition. Indeed, to convince yourself, imagine a small infinitessimal box of size $\text{d}x$,$\text{d}y$ and $\text{d}z$. The pressure exerted on the surface $\mathcal{S}=\text{d}y\text{d}z$ is 

$$P=\frac{\text{d} \vec{F}\cdot \vec{n}}{\text{d} \mathcal{S}}= \frac{\text{d} \vec{F}\cdot \vec{n}}{\text{d} \mathcal{S}}=\frac{\text{d}\vec{F}\cdot \vec{n}}{ \text{d}y\text{d}z}= \frac{\text{d} \vec{F}\cdot \text{d}\vec{x}}{ \text{d}y\text{d}z\text{d}x}=\frac{\text{d} \vec{F}\cdot\text{d}\vec{x}}{\text{d}V} $$

. On the other hand, the energy transfered to a wall of the box due to the kinetic motion of the particle within the box, can be written $\text{d} E= - \delta W=-\vec{F}\cdot\text{d}\vec{x}$.

From which 

$$ P = \frac{\text{d} \vec{F}\text{d}\vec{x}}{\text{d}V} =-\frac{\partial{E}}{\partial{V}}\Bigg|_S$$

Hence, knowing only the expression of the energy $E_i$ of each microstate, we are able to derive all the thermodynamically relevant quantities (the pressure $P$, the temperature $T$, the mean energy $E$, the entropy $S$...) through the partition function $Z$, simply by asking for the maximization of the entropy.

# Classical ideal gas.

## The equation of states and energy

Let us now apply the above equations to rederive the ideal gas properties. Consider a box filled with $\mathcal{N}$ particles. These particles are free and non interacting, hence their energy is given by $\vec{p}^2/2m$. The energy of a microstate, i.e. a particle configuration in the box is given by

$$E(i)=\frac{1}{2m}\sum_i^{3\mathcal{N}}{p_n}^2$$

where we sum over all $\mathcal{N}$ particles and the 3 configurations of space.

The partition function associated to the maximisation of enetropy is hence  

$$Z=\int e^{-\frac{\beta}{2m}\sum_n p_n^2} d^{3\mathcal{N}}x d^{3\mathcal{N}}p$$

Where we replaced the sums over the $N$ possible microstates associated to the macrostate by continuous integrals over momentum and space.

Develloping this integral simply gives

$$ \boxed{Z=\left(\frac{e}{\rho}\right)^\mathcal{N}\left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}}$$

<details>
  <summary>Proof</summary>
 
The integral over space gives

$$\int dx^{3\mathcal{N}}=\frac{V^\mathcal{N}}{\mathcal{N}!}$$

where the $\mathcal{N}!$ is here to traduce the fact that particles are distinguishable and avoid double conting same particle configurations with different labeling.

$$Z=\frac{V}{\mathcal{N}!}\left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}$$
</details>

From $Z$, one can find back the mean energy of the macrostate under consideration to be

$$ \boxed{E = -\frac{\partial \ln(Z)}{\partial \beta} = \frac{3}{2}\mathcal{N}k_B T}$$

<details>
 <summary>Proof</summary>

$$\begin{aligned}
\ln(Z)&=\ln\left(\left(\frac{e}{\rho}\right)^N\left(\frac{2m\pi}{\beta}\right)^{\frac{3N}{2}}\right) \\
&= N\ln\left(\frac{e}{\rho}\right)+\frac{3N}{2}\left(\ln(2m\pi)-\ln(\beta)\right)\\
\end{aligned}
$$

$$\begin{aligned}
-\frac{\partial \ln(Z)}{\partial \beta}&= -\frac{3\mathcal{N}}{2}\frac{\partial}{\partial \beta}\left(-\ln(\beta)\right) \\
&= \frac{3\mathcal{N}}{2} \frac{1}{\beta}\\
&= \frac{3\mathcal{N}}{2} k_B T
\end{aligned}
$$

</details>

Similarly, we can compute the pressure of the macrostate to be

$$ P = \frac{\partial{E}}{\partial{V}}\Bigg|_S= \rho k_B T$$

that is, we derived back the ideal gas law

$$ \boxed{P =\frac{n\mathcal{R}T}{V}}$$

and thus, only by assuming that particles were not interacting $E=E_c$, and asking for the entropy to be maximal! 

<details>
  <summary>Proof</summary>
As

$$P= -\frac{\partial E}{\partial V}\Bigg|_{S}$$

and 

$$ E= \frac{3N}{2} k_B T= \frac{3\mathcal{N}}{2}k_B $$

</details>

### The Maxwell-Boltzmann speed distribution

We can use the partition function to associate a probability to a given microstate

$$p_i = \frac{1}{Z}e^{-\beta E_i} $$

## Varying number of particles, grand canonical ensemble

Consider a system with accessible microstates caracterised by an energy $E_i$ and a number of particle $N_i$. Then maximizing the entropy $S$ of the system in the grand cononcial ensemble, letting the system exchange energy and particles with the exterior and asking for the constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i N_i = \langle N \rangle\\
&\sum_i p_i E_i = \langle E \rangle \\
& \sum_i p_i  = 1
\label{eq:constraintsGrandCano}
\end{aligned}
\end{cases}
$$

leads to:

$$
p_i = \frac{1}{Z}e^{-\beta E_i + \mu N_i}
$$

With $\beta=1/T$ and $Z$ the partition function defined as:

$$
\boxed{Z = \sum_i e^{-\beta E_i + \mu N_i}}
$$

<details>
  <summary>Proof</summary>
  
</details>


Note that allowing other constraints as Eq.\ref{eq:constraintsGrandCano} would add new lagrange multipliers appearing in the exponential of the expression of $p_i$.

### Volumes in phase space

The probability $dP$ of a given element of the phase space is given by:

$$
dP= \rho d\Gamma
$$

# Quantum statistics: boson, fermions and blackbody

A quantum system is described by a *wave-vector* $\ket{\phi}$, element of a complex Hilbert space. *Observables* are described by Hermitian operators $\hat{X}$ on this Hilbert space. The wavevector can always be written as a linear decomposition on the basis of the eigenvectors $\ket{x_i}$ of $\hat{X}$ as:

$$
\ket{\phi} = \sum_i \alpha_i \ket{x_i}
$$


Where $\alpha$ are complex coefficients and

$$
\hat{X}\ket{x_i} = x_i \ket{x_i}
$$

The probability for the system to be oberved in the state $\ket{x_i}$ with the measured value $x_i$ for the observable $\hat{X}$ is then given by $p(x_i) = \alpha_i^* \alpha_i$ (and so $\sum_i \alpha_i^* \alpha_i = 1$) and the average value of $\hat{X}$ is given by $\langle X \rangle = \bra{\phi}\hat{X}\ket{\phi}$. In this sense, $\ket{\phi}$ contains all the quantum informations about the system.

The *density operator* $\hat{\rho}$, generalizes the wavevector to take into account for more general states, called mixed states $\ket{\psi}$ that are statistical mixtures of pure states $\ket{\phi_i}$.

$$
\hat{\rho}:= \ket{\psi(t)}\bra{\psi(t)} = \sum_i \mathcal{P}_i \ket{\phi_i(t)}\bra{\phi_i(t)}
$$


Where $\mathcal{P}_i$ are the classical probabilities associated to the pure state $\ket{\phi_i}$.

This operator is necessary in statistical physics where the system is composed of a big number of independant quantum sub-systems, all described by pure states. Despite the quantum nature of all the subsystems, the mixture behaves stochasticly with classical probabilities. 
It can also be used when the system considered is the sub-part of a quantum entangled system (for example considering a single electron in an intriqued "EPR" electron-positron pair). In such a cituation, we can show that this sub-part behaves as a classical statistical variable.

The normalization of all probabilities and the mean value of an observable $\hat{X}$ are given by:

$$
\begin{aligned}
&\text{Tr}{\hat{\rho}}=1\\
&\text{Tr}{\hat{\rho}\hat{X_i}}= \langle X_i \rangle
\end{aligned}
\label{eq:densitymatrixproperties}
$$

Out of the density operator, one can build the *Von Neumann entropy*:

$$
S = Tr(\hat{\rho} \ln(\hat{\rho})) 
$$


which is equivalent to the classical entropy.  Due to its Concavity, extremalization is maximization. Using the Lagrange multiplier technique we find the expression for $\hat{\rho}$ maximizing $S$. Grand canonical ensemble: system can exchange both particles and energy with the surrounding medium at equilibrium. We ask for the conditions in Eq.~\ref{eq:densitymatrixproperties} with $\hat{X}_i= \{\hat{H},\hat{N}\}$. We get:

$$
\hat{\rho}= \frac{1}{\Xi}e^{-\beta(\hat{H} - \mu \hat{N})}
$$


The lagrange multiplier can be showned to be equal to $\beta= (k_\text{B} T)^{-1}$ and $\mu$ the chemical potential. $\Xi$ is the partition function: 

$$
\Xi = \text{Tr}(e^{-\beta(\hat{H} - \mu \hat{N})}) 
$$


## Quantum statistics

To describe multiparticle states, we work in Fock space, that is, tensorial product of single particle Hilbert spaces. The basis wavevector describing the states of the systems are given by the eigenvector of several commuting observables $\ket{n_1,n_2, \cdots, n_M}$. Where $1\cdots M$ represents the (potentialy infinite) $M$ possible quantum states accessible to a particle and $n_\lambda$ are the occupation number of each quantum states i.e. the number $n_\lambda$ of particles observed in the quantum state $\ket{\lambda}$. The wavevector $\ket{\Phi}$ describing the multiparticle system can then be decomposed in the basis:

$$
\ket{\Phi}= \sum_i \alpha_{n_1,n_2, \cdots, n_M} \ket{n_1,n_2, \cdots, n_M}
$$

$$
\begin{aligned}
&E=\sum_\lambda n_\lambda \epsilon_\lambda \\
&N=\sum_\lambda n_\lambda
\end{aligned}
$$

One can show that the total partition function can be written as the product of the partition function associated to each individual quantum state:

$$
\Xi = \prod_\lambda \xi_\lambda
$$


With:

$$
\xi_\lambda = \sum_{n_\lambda=0}^\infty e^{-\beta n_\lambda (\epsilon_\lambda - \mu)}
$$


The average number of particle occuping a quantum state is given by:

$$
\langle n_{\lambda} \rangle = \frac{\partial \ln(\xi_\lambda)}{\partial \alpha}
$$

with $\alpha := \beta \mu$

Due to spin-statistics theorem, Bosons have no limits on their occupation number, each state can be populate infinitly. They follow the *Bose-Einstein* (BE) statistics:

$$
\xi^{BE}_\lambda = \sum_{n_\lambda=0}^\infty \left(e^{-\beta (\epsilon_\lambda - \mu)}\right)^{n_\lambda} = \frac{1}{1-e^{-\beta(\epsilon_\lambda - \mu)}}
$$


Remembering the expression for an infinite geometric sum:

$$
\sum_{k=0}^\infty q^k = \frac{1}{1-q}
$$


We then get:

$$
\langle n^{BE}_\lambda \rangle = \frac{1}{e^{\beta(\epsilon_\lambda - \mu)}-1}
$$


For fermions, 

$$
\xi^{FD}_\lambda = \sum_{n_\lambda=0}^1 \left(e^{-\beta n_\lambda (\epsilon_\lambda - \mu)}\right) = 1 + e^{-\beta (\epsilon_\lambda - \mu)}
$$


$$
\langle n^{FD}_\lambda \rangle = \frac{1}{e^{\beta(\epsilon_\lambda - \mu)}+1}
$$

## Quantum ideal gas


## Radiation pressure and the black-body

Let's consider now a closed box of volume $V$containing a photon gaz at equilibrium at temperature $T$. The gaz is thermalized by the constant interactions with the electrons of the atoms of the walls and has a continus spectrum. (this spectrum would then be emitted by the gaz if a hole was open in it).
Photons are continuiously created and absorbed and it's impossible to fix their average value $N$ when minimizing the entropy (since they have no mass, one can get any state of energy $E$ with N photons of energy $\hbar \omega$ or 2N photons of energy $\hbar \frac{\omega}{2}$ $\cdots$). The number of photons $N$ has no impact on the macrostate which is then fully determined by $E$. One must then fix $\mu=0$.


$$
\langle \epsilon_\lambda\rangle = \langle n_\lambda\rangle\epsilon_\lambda =  \langle n_\omega \rangle \hbar \omega
$$


$$
g(\omega)= \frac{V}{\pi^2 c^3}\omega^2
$$

$$
u(\omega)= \frac{1}{V}\frac{dE}{d\omega}=\frac{1}{\pi^2c^3}\frac{\hbar \omega^3}{e^{\beta \hbar \omega}-1}
$$

$$
B_\nu(T)= u(\omega)\frac{d\omega}{d\nu}
$$

$$
w=\frac{1}{3}
$$
