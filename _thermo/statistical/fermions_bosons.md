---
layout: default
title: Bosons and fermions
parent: thermo
nav_order: 1
---

$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

## Factorisation of the partition functions


## Partition functions and occupation number

To describe multiparticle states, we work in Fock space, that is, tensorial product of single particle Hilbert spaces. The basis wavevector describing the states of the systems are given by the eigenvector of several commuting observables $\ket{n_1,n_2, \cdots, n_M}$. Where $1\cdots M$ represents the (potentialy infinite) $M$ possible quantum states accessible to a particle and $n_\lambda$ are the occupation number of each quantum states i.e. the number $n_\lambda$ of particles observed in the quantum state $\ket{\lambda}$. The wavevector $\ket{\Phi}$ describing the multiparticle system can then be decomposed in the basis:

$$
\ket{\Phi}= \sum_i \alpha_{n_1,n_2, \cdots, n_M} \ket{n_1,n_2, \cdots, n_M}
$$

$$
\begin{aligned}
&U=\langle \hat{H}\rangle = \sum_\lambda n_\lambda \epsilon_\lambda \\
&N= \langle \hat{N}\rangle=\sum_\lambda n_\lambda
\end{aligned}
$$

As discussed above, the total partition function can be written as the product of the partition function associated to each individual quantum state:

$$
\Xi = \prod_\lambda \xi_\lambda
$$

With:

$$
\xi_\lambda = \sum_{n_\lambda=0}^\infty e^{-\beta n_\lambda (\epsilon_\lambda - \mu)}
$$


The average number of particle occuping a quantum state is given by:

$$
\boxed{\langle n_{\lambda} \rangle = \frac{\partial \ln(\xi_\lambda)}{\partial \alpha}}
$$

with $\alpha := \beta \mu$

Due to spin-statistics theorem, Bosons have no limits on their occupation number, each state can be populate infinitly. They follow the **Bose-Einstein** (BE) statistics:

$$
\xi^{BE}_\lambda = \sum_{n_\lambda=0}^\infty \left(e^{-\beta (\epsilon_\lambda - \mu)}\right)^{n_\lambda} = \frac{1}{1-e^{-\beta(\epsilon_\lambda - \mu)}}
$$


Remembering the expression for an infinite geometric sum:

$$
\sum_{k=0}^\infty q^k = \frac{1}{1-q}
$$

We then get:

$$
\boxed{\langle n^{BE}_\lambda \rangle = \frac{1}{e^{\beta(\epsilon_\lambda - \mu)}-1}}
$$


For fermions, **Fermi-Dirac** statistics: 

$$
\xi^{FD}_\lambda = \sum_{n_\lambda=0}^1 \left(e^{-\beta n_\lambda (\epsilon_\lambda - \mu)}\right) = 1 + e^{-\beta (\epsilon_\lambda - \mu)}
$$


$$
\boxed{\langle n^{FD}_\lambda \rangle = \frac{1}{e^{\beta(\epsilon_\lambda - \mu)}+1}}
$$
