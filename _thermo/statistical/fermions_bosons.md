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

## Bosons and fermions

At the fundamental level, elementary particles are described by quantum fields. These abstract fields, are discussed in the associated [class](../../_quantum/quantum.md). The mathematical form that these fields can have is not purely arbitrary, but is deeply dictated by symmetry principle. In particular, the structure and symmetries of our space-time impose the fields to be associated with a number, the spin $s$, which can be either an integer or a half-integer. The value of $s$ is rather mysterious and dictates how the field transform under rotations and change of reference frame in space-time. Discussing it further is way beyond the scope of this class.
However, $s$ as a very important impact for statistical physics, as it divide the elementary particles into two distinct types:

- **fermions**: which are particles associated with fields of half-integer spins. We know that most particles forming matter: electrons, protons and quarks are fermions of spin $s=1/2$. This is also the case of every atomic nuclei with a odd number of nucleons.
- **bosons**: which are particles associated with fields of integer spins. Particles associated to fundamental forces of natures are bosons. This is the case for photons, gluons and $W$ and $Z$ bosons with $s=1$ and the Higgs boson with $s=0$. Atomic nuclei with an even number of nucleons also behave as bosons.

The link between the spins of particles and their statistical properties is a very subtle one, given by the so-called **spin-statistics** theorem which is notably difficult to prove.

## Fock spaces for bosons and fermions

## Factorisation of the partition functions


## Partition functions and occupation number

To describe multiparticle states, we work in Fock space, that is, tensorial product of single particle Hilbert spaces. The basis wavevector describing the states of the systems are given by the eigenvector of several commuting observables $\ket{n_1,n_2, \cdots, n_M}$. Where $1\cdots M$ represents the (potentialy infinite) $M$ possible quantum states accessible to a particle and $n_\lambda$ are the occupation number of each quantum states i.e. the number $n_\lambda$ of particles observed in the quantum state $\ket{\lambda}$. The wavevector $\ket{\Phi}$ describing the multiparticle system can then be decomposed in the basis:

$$
\ket{\Phi}= \sum_i \alpha_{n_1,n_2, \cdots, n_M} \ket{n_1,n_2, \cdots, n_M}
$$

$$
\begin{aligned}
&U=\sum_\lambda n_\lambda \epsilon_\lambda \\
&N=\sum_\lambda n_\lambda
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
\langle n_{\lambda} \rangle = \frac{\partial \ln(\xi_\lambda)}{\partial \alpha}
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