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

In the previous lectures, we described the right mathematical space, Fock space, in which to consider a system made of a varying number of quantum particles. 
We will now focus on the special case of a system made of $\mathcal{N}$ **identical** and **non-interacting** quantum particles. The single particle Hilbert space has $N$ accessible states, each having an energy $\epsilon_\lambda$.
On Fock space, the density matrix which maximize the entropy under (grand canonical) constraints is the operator: 

$$ \hat{\rho}= \frac{1}{\Xi}e^{-\beta\left( \hat{H} - \mu \hat{\mathcal{N}}\right)}$$

with

$$
\Xi = \text{Tr}(e^{-\beta(\hat{H} - \mu \hat{\mathcal{N}})}) 
$$

If the system is made of a varying $\mathcal{N}$ number of identical particles,

$$
\boxed{\Xi = \prod_\lambda \xi_\lambda}
$$

With the partition function for a single particle being:

$$
\boxed{\xi_\lambda = \sum_{n_\lambda=0}^\infty e^{-\beta n_\lambda (\epsilon_\lambda - \mu)}}
$$

<details>
  <summary><strong>Proof:</strong> </summary>

$$
\begin{align}
\Xi &= \text{Tr}(e^{-\beta(\hat{H} - \mu \hat{\mathcal{N}})}) \\
     &=\sum_{n_\lambda} \bra{n_1,n_2,...,n_N} e^{-\beta(\hat{H} - \mu \hat{\mathcal{N}})}\ket{n_1,n_2,...,n_N} \\
     &= \sum_{\lambda=0} e^{-\beta\sum_\lambda n_\lambda(\epsilon_\lambda -\mu)}\\
     &= \prod_\lambda\left( \sum_{n_\lambda} e^{-\beta n_\lambda(\epsilon_\lambda -\mu)}\right)\\
     &= \prod_\lambda \xi_\lambda
\end{align}
$$

</details>

The average number of particle occuping a quantum state is given by:

$$
\boxed{\langle n_{\lambda} \rangle = \frac{\partial \ln(\xi_\lambda)}{\partial \alpha}}
$$

with $\alpha := \beta \mu$

<details>
  <summary><strong>Proof:</strong> </summary>


</details>

## Partition functions and occupation number

### Bosons

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

### Fermions


For fermions, **Fermi-Dirac** (FD) statistics: 

$$
\xi^{FD}_\lambda = \sum_{n_\lambda=0}^1 \left(e^{-\beta n_\lambda (\epsilon_\lambda - \mu)}\right) = 1 + e^{-\beta (\epsilon_\lambda - \mu)}
$$


$$
\boxed{\langle n^{FD}_\lambda \rangle = \frac{1}{e^{\beta(\epsilon_\lambda - \mu)}+1}}
$$

PLOTS