---
layout: default
title: Fock space
parent: QFT
nav_order: 1
---

$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

## Fock space

We saw in the first part that a general solution of the Schrödinger equation can be written as

$$\boxed{\ket{\psi} = \sum_n \alpha_n(t)\ket{\varphi_n}(x)}$$

where $n$ label the different eigenstates of the Hamiltonian $\hat{H}$ and can eventually be a tuple in the case of degeneracies (in which case, the sum goes over each element of the tuple). In the simplest case of a time independent Hamiltonian with discrete spectra:

$$\alpha_n(t)  = c_n e^{\frac{-iE_n t}{\hbar}}$$

and for particle in a box:

$$\ket{\varphi_n} = \frac{1}{\sqrt{V}}e^{i\vec{k}\cdot \vec{x}}\ket{\vec{k}}$$

giving back a plane wave for $\psi(x)=\braket{\bra{x}}{\psi}$.

We already encountered such decompositions on a basis of the Hilbert space in the case of Fock spaces in the [statistical mechanics class](../../_thermo/statistical/Fock_space.md).

We saw that it was possible to describe a system of $\mathcal{N}$ particles equivalently on the basis

$$ \ket{n_1,n_2,n_3,...,n_{\infty}}$$

where $n_i$ describes the number of particles amongst the $\mathcal{N}$ which are in the state of energy $i$. For $\mathcal{N}$ particles, $\sum_i n_i = \mathcal{N}$.

$\ket{0}=\ket{0,0,0,...,0}$ is the vacuum. A single particle wave function will be described on the basis $\ket{1,0,0,...,0}=\ket{\varphi_0}$, $\ket{0,1,0,...,0}=\ket{\varphi_1}$, $\ket{0,0,1,...,0}=\ket{\varphi_2}$ and so on.

$$\ket{\psi} = \sum_n \alpha_n(t)\ket{\varphi_n}(x) =  \alpha_0 \ket{1,0...} + \alpha_1 \ket{0,1,...} + ...$$ 

Recall that the wavefunction description is obtained by sandwiching all these expressions on the left by $\bra{x}$. 
In the case of a plane wave, $n_i$ is the number of particles with wavevector $k_i$ and thus momentum $p_i$.

Now, of course, the whole purpose of this formalism is to describe systems for which the particle number is greater than one.

$$\ket{\psi} = \sum_{n_i} \alpha_{n_i,n_j,n_k...} \alpha_{n_i,n_j,n_k ...}\ket{n_i,n_j,n_k...}$$

Where the sum goes over all possible particle configurations.
For example, a general state for three particles for bosons would be:

$$\ket{\psi} = \alpha_{3,0,0 ...}\ket{3,0,0 ...} + \alpha_{0,3,0,...}\ket{0,3,0,...} + \alpha_{0,0,3,...}\ket{0,0,3,...}  + \alpha_{2,1,0,...}\ket{2,1,0,...}+ \alpha_{1,1,1,...}\ket{1,1,1,...} + ...$$

Hence, a general state is a superposition of all possible energy distribution of the three particles amongst the accessible energy levels (and, say, $\alpha_{3,0,0}$, is the probability amplitude to find the three particles in the ground state). For  fermions, we recall that there can not be more than one particle in the same state, hence, the $n_i$ can be only 0 or 1, and a general state is of the form:

$$\ket{\psi} = \alpha_{1,1,1 ...}\ket{1,1,1 ...} + \alpha_{0,1,1,1,..}\ket{0,1,1,1,...} +\alpha_{1,0,1,1,..}\ket{1,0,1,1,...} + ...$$

## Introducing creation and destruction operators on Fock space

So far, our description had only a constant number of particles $\mathcal{N}$, such that the sum over all occupation numbers is $\sum_i n_i = \mathcal{N}$.

How about conservations?

Introducing creation and destruction operators for bosons and fermions.

[quantum harmonic oscillator](../../_quantum/quantum/QHO.md).

$$\hat{\mathcal{N}}= \sum_i a_ia_i^{\dagger}$$

$$\hat{H}= \sum_i E_i a_ia_i^{\dagger}$$

$$[\hat{\mathcal{N}},\hat{H}]=0$$

and hence

$$\frac{\text{d}\mathcal{N}}{\text{d}t}=0$$

with $\mathcal{N}=\bra{\psi}\hat{\mathcal{N}}\ket{\psi}$.

## Your first quantum field

$$ \Psi(x) = \sum_k \psi_k(x) a_k$$

$$ \Psi^{\dagger}(x) = \sum_k \psi_k^{\dagger}(x) a_k^{\dagger}$$

## The Schrödinger field equation

