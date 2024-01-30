---
layout: default
title: Quantum statistics
parent: thermo
nav_order: 1
---


$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

# Quantum statistics: bosons, fermions and blackbody

A quantum system is described by a *wave-vector* $\ket{\phi}$, element of a complex Hilbert space. *Observables* are described by Hermitian operators $\hat{X}$ on this Hilbert space. The wavevector can always be written as a linear decomposition on the basis of the eigenvectors $\ket{x_i}$ of $\hat{X}$ as:

$$
\ket{\phi} = \sum_i \alpha_i \ket{x_i}
$$


Where $\alpha$ are complex coefficients, the probability amplitudes and

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