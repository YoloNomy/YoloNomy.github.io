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

$$ \hat{\rho}= \frac{1}{\Xi}e^{-\beta\left( \hat{H} - \mu \hat{\mathcal{N}}\right)}$$

$$
\begin{aligned}
&U=\langle \hat{H}\rangle = \sum_\lambda n_\lambda \epsilon_\lambda \\
&\langle \mathcal{N} \rangle= \langle \hat{\mathcal{N}}\rangle=\sum_\lambda n_\lambda
\end{aligned}
$$


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

## Partition functions and occupation number


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

PLOTS