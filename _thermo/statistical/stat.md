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

## Maximizing the entropy

Let $i$ label a discrete number of $N$ possible states for a system. Let $p_i$ be the probability for the system to be in the state $i$, such that $\sum_i p_i = 1$. We define the entropy of the system $S$ as:

$$
\boxed{
S = -\sum_i p_i\ln{p_i} = \langle \ln(p_i)\rangle}
$$

For a system where all states are equiprobable, $p_i=1/N$ and:

$$
S = -\frac{1}{N}\sum_i^N\ln\left(\frac{1}{N}\right)= \ln(N)
$$

If there is a single state that is perfectly known, the entropy is then $N=1$ and $S=0$.


# Classical statistics up to the ideal gas

### Derivation of the probabilities of maximal entropy in the canonical ensemble ($N$ fixed).

Let's consider a system of $N$ distinguishable interacting particles in thermal equilibrium with a eat bath. Let's label by $i$ the possible energy states that a subsystem can be in. To each state is associated a energy $E_i$. Let $n_i$ be the occupation number that is the number of particles that can be with energy $E_i$ at a given time. In the large $N$ limit, we have:

$$
\sum_i n_i = N
$$

The probability of the system to be in the state $i$ is:

$$
p_i = \frac{n_i}{N}
$$

Leading naturally from the above equation to

$$
\sum_i p_i = \sum_i \frac{n_i}{N} = 1
$$


The average energy of a particle is:

$$
\langle E \rangle  = \sum_i p_i E_i = \sum_i \frac{n_i}{N} E_i
$$


The number of ways to rearange the $N$ particles into the possible energy states with occupation numbers $n_i$ is given by:

$$
C = \frac{N!}{\prod_i n_i!}
$$

Maximizing $C$ will give us the most probable configuration of the $n_i$. It can be shown that this maximum is very sharp, making other configurations almost impossible.

If $N$ and $n_i \to \infty$, we can use the *Stirling approximation*:

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

This approximation allows us to calculate:

$$ 
\ln(C)= NS
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

Maximizing $C$ is equivalent to maximizing $S$ with the following constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i E_i &= \langle E \rangle \\
& \sum_i p_i  &= 1
\end{aligned}
\end{cases}
$$

<details>
  <summary>Lagrange multipliers</summary>
  
</details>

Maximizing $S$... Lagrange multipliers
giving us the probability for a single particle to be in the state of energy $E_i$:

$$
\boxed{p_i = \frac{1}{Z}e^{-\beta E_i}}
$$

With $Z$ the *partition function*:

$$
Z := e^{1+\alpha}
$$

It can be expressed by asking for the normalization of probabilities:

$$
\sum_i p_i = \sum_i \frac{1}{Z}e^{-\beta E_i} =1 
$$

Leading to:

$$
\boxed{Z = \sum_ie^{-\beta E_i}}
$$

The energy of the system can then be re-expressed from $Z$ as

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

We can now express $\beta$ with respect to the temperature. First noticing that: 

$$
dS = \beta d\langle E\rangle + \langle E\rangle d\beta + \frac{\partial \ln Z}{\partial \beta}d\beta
$$

(using Eq.\ref{eq:entropy-of-E} and the fact that $Z$ is a function of only one independant variable $\beta$ or $\langle E \rangle$ since both are not independant because of Eq.\ref{eq:E-of-Z}. Now using Eq.\ref{eq:E-of-Z}, we can see that the two last terms cancels out to give simply: $dS = \beta d\langle E\rangle$. We now define the temperature $T$ as (more on this definition later):

$$
\boxed{T := \frac{\partial \langle E \rangle}{\partial S}} 
\label{eq:defTemp}
$$


Which leads to $dS = \frac{1}{T}d\langle E\rangle$, allowing us to conclude that:

$$
\boxed{\beta = \frac{1}{T}}
$$


### On the definition of temperature

The temperature is above by Eq.\ref{eq:defTemp}.

Why is it a good definition:
- direction of heatflows
- broadening of $p(E)$ with increasing $\langle E \rangle$

### Pressure

Pressure is not only a force over a surface but also a energy per unit of volume!

$$ P = \frac{\partial{E}}{\partial{V}}\Bigg|_S$$

### Classical ideal gas.

What has been calculated previously to look at the states of a single particle can be generalized to the states of the entire box of particles.

$$E=\frac{1}{2m}\sum_i^{3N}{p_n}^2$$

$$Z=\int e^{-\frac{\beta}{2m}\sum_n p_n^2} d^{3N}x d^{3N}p$$


$$ \boxed{Z=\left(\frac{e}{\rho}\right)^N\left(\frac{2m\pi}{\beta}\right)^{\frac{3N}{2}}}$$

<details>
  <summary>Proof</summary>
 
$$\int dx^{3N}=\frac{V^N}{N!}$$

$$Z=\frac{V}{N!}\left(\frac{2m\pi}{\beta}\right)^{\frac{3N}{2}}$$
</details>

$$ \boxed{E = -\frac{\partial \ln(Z)}{\partial \beta} = \frac{3}{2}Nk_B T}$$

<details>
 <summary>Proof</summary>

$$\begin{aligned}
\ln(Z)&=\ln\left(\left(\frac{e}{\rho}\right)^N\left(\frac{2m\pi}{\beta}\right)^{\frac{3N}{2}}\right) \\
&= N\ln\left(\frac{e}{\rho}\right)+\frac{3N}{2}\left(\ln(2m\pi)-\ln(\beta)\right)\\
\end{aligned}
$$

$$\begin{aligned}
-\frac{\partial \ln(Z)}{\partial \beta}&= -\frac{3N}{2}\frac{\partial}{\partial \beta}\left(-\ln(\beta)\right) \\
&= \frac{3N}{2} \frac{1}{\beta}\\
&= \frac{3N}{2} k_B T
\end{aligned}
$$

</details>

$$ P = \frac{\partial{E}}{\partial{V}}\Bigg|_S= \rho k_B T$$

that is, we derived back the ideal gas law

$$ \boxed{P =\frac{n\mathcal{R}T}{V}}$$

and thus, only by assuming that particles were not interacting $E=E_c$, and asking for the entropy to be maximal! 

<details>
  <summary>Proof</summary>

</details>

### Varying number of particles, grand canonical ensemble

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
Z = \sum_i e^{-\beta E_i + \mu N_i}
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
&{\rm Tr}{\hat{\rho}}=1\\
&{\rm Tr}{\hat{\rho}\hat{X_i}}= \langle X_i \rangle
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


The lagrange multiplier can be showned to be equal to $\beta= (k_{\rm B} T)^{-1}$ and $\mu$ the chemical potential. $\Xi$ is the partition function: 

$$
\Xi = {\rm Tr}(e^{-\beta(\hat{H} - \mu \hat{N})}) 
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

$$$
u(\omega)= \frac{1}{V}\frac{dE}{d\omega}=\frac{1}{\pi^2c^3}\frac{\hbar \omega^3}{e^{\beta \hbar \omega}-1}
$$

$$
B_\nu(T)= u(\omega)\frac{d\omega}{d\nu}
$$

$$
w=\frac{1}{3}
$$
