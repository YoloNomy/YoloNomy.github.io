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


# Quantum statistics

Many (if not most of) the collective phenomenon can't be explained with classical statistics. In fact, beyond simple dilute gas, the explanatory power of classical statistics fail. Actually, we often tend to consider quantum mechanics as an abstract topic, far from our daily life, which concern only very specific phenomenon, as the ones for which there is so few interactions that decoherence can be avoided. In a sense, statistical mechanics disprove this assertion by demonstrating that, without the intrinsic quantum nature governing microphysics, it would be impossible to interpret most of the daily life phenomenon around us from a statistical perspective.

In particular, we absolutely need quantum statistics in order to describe:

- Systems with **high densities**, like solids or cristals.
- To describe **radiation**, like light, as the well known UV catastrophe illustrates.

We will assume here some prior knowledge of quantum mechanics and we warmly advise the reader to first have a look at the [quantum mechanics](../../_quantum/quantum.md) class before reading further.

## Microstates: Wave-vectors, density operator and entropy

A quantum system is described by a **wave-vector** $\ket{\phi}$, element of a complex Hilbert space $\mathcal{H}$ equipped with an Hermitian product $\braket{.}{.}: \mathcal{H}\times\mathcal{H}\to \mathbb{C}$. As such, the wave-vector describing the system is the **microstate** of the system in a quantum mechanical context.
**Observables** are described by Hermitian operators $\hat{f}$ on this Hilbert space, that is object that act on wave-vector to give another wave-vector $\hat{f}: \mathcal{H}\to\mathcal{H}$. The wavevector describing the system can be written as a linear decomposition on the basis of the eigenvectors $\ket{f_i}$ of an operator $\hat{f}$ as:

$$
\ket{\phi} = \sum_i \alpha_i \ket{f_i}
$$


Where the coefficients $\alpha_i= \braket{\phi}{f_i}$ are complex coefficients, the **probability amplitudes** and, by definition of the eigenvectors:

$$
\hat{f}\ket{f_i} = f_i \ket{f_i}
$$

The probability for the system to be observed in the state $\ket{f_i}$ with the measured value $f_i$ for the observable $\hat{f}$ is then given by $p(f_i) = \alpha_i^* \alpha_i$ (and so $\sum_i \alpha_i^* \alpha_i = 1$) and the average value of $\hat{f}$ is given by $\langle f \rangle = \bra{\phi}\hat{f}\ket{\phi}$. In this sense, $\ket{\phi}$ contains all the quantum informations about the system.

The **density operator** $\hat{\rho}$, generalizes the wavevector to take into account for more general states, called mixed states $\ket{\psi}$ that are statistical mixtures of pure states $\ket{\phi_i}$.

$$
\hat{\rho}:= \ket{\psi(t)}\bra{\psi(t)} = \sum_i \mathcal{P}_i \ket{\phi_i(t)}\bra{\phi_i(t)}
$$

Where $\mathcal{P}_i$ are the classical probabilities -- which can also be time dependent -- associated to the pure state $\ket{\phi_i}$.

This operator is necessary in statistical physics where the system is composed of a big number of independant quantum sub-systems, all described by pure states. Despite the quantum nature of all the subsystems, the mixture behaves stochasticly with classical probabilities. 
It can also be used when the system considered is the sub-part of a quantum entangled system (for example considering a single electron in an intriqued "EPR" electron-positron pair). In such a situation, we can show that this sub-part behaves as a classical statistical variable. As such, the best and more general tool to describe a **microstate** in the quantum context is given by $\hat{\rho}$.

The mean value of an observable $\hat{f}$ is obtained from $\rho$ using the trace:

$$\langle \hat{f}\rangle = {\rm Tr}(\hat{\rho}\hat{f}) $$

<details>
  <summary><strong>Complement:</strong> More informations on the density operator</summary>

</details>

Out of the density operator, one can build the **Von Neumann entropy**:

$$
\boxed{S = Tr(\hat{\rho} \ln(\hat{\rho}))}
$$

which is equivalent to the classical entropy.  Due to its concavity, extremalization is maximization. Using the Lagrange multiplier technique we find the expression for $\hat{\rho}$ maximizing $S$.

The constraints for maximizing $S$ are normalization of all probabilities and the mean value of an observable $\hat{X}$, which takes the form:

$$
\begin{aligned}
\begin{cases}
\text{Tr}{\hat{\rho}}&=1\\
\text{Tr}{\hat{\rho}\hat{X_i}}&= \langle X_i \rangle
\end{cases}
\end{aligned}
$$


Grand canonical ensemble: system can exchange both particles and energy with the surrounding medium at equilibrium. We ask for the conditions of normalisation and mean value with $\hat{X}_i= \{\hat{H},\hat{N}\}$. We get the quantum generalisation of the Grand canonical ensemble:

$$
\boxed{\hat{\rho}= \frac{1}{\Xi}e^{-\beta(\hat{H} - \mu \hat{N})}}
$$

With $\Xi$ is the quantum partition function: 

$$
\Xi = \text{Tr}(e^{-\beta(\hat{H} - \mu \hat{N})}) 
$$

Similarly, the microcanonical and canonical distribution keep identical structures as the ones in the classical case.

## Quantum phase-space: time evolution and Ehrenfest theorem

The classical phase space of classical mechanics is replaced by the Hilbert space $\mathcal{H}$ in a quantum context. As discussed above, observables $\hat{f}$ are not functions like in classical mechanics but operators $\hat{f}:\mathcal{H}\to\mathcal{H}$. Just like in classical mechanics, a special observable, the Hamiltonian $\hat{H}$ governs the time evolution of microstates, through the
**Schrödinger equation**:

$$i\hbar \frac{\text{d}}{\text{d}t}\ket{\phi} = \hat{H}\ket{\phi}$$

which solution gives the time evolution of the wave-vector from a time $t_0$ to a time $t$ as

$$\ket{\phi(t)}= U(t-t_0)\ket{\phi(t_0)}$$

with the time evolution operator:

$$U(t-t_0)=e^{\frac{-i \hat{H}t}{\hbar}}$$


<!-- $$\hat{f}(t)=U(t-t_0)\hat{f}(t_0)U(t-t_0)$$ -->

As in classical mechanics, the commutator with $\hat{H}$ allows to infer the time evolution of the mean value of observables through the **Erhenfest theorem**, which follows from the Schrödinger equation: 

$$\frac{\text{d}}{\text{d}t} \langle \hat{f} \rangle= \frac{1}{i\hbar}\langle [\hat{H},\hat{f}] \rangle +\langle \frac{\partial \hat{f}}{\partial t}\rangle$$

<details>
  <summary><strong>Proof:</strong></summary>

</details>

The geometry of the Hilbert space is encoded in the operator commutator $[.,.]$, which is the quantum equivalent to the classical Poisson bracket: 

$$[\hat{f},\hat{g}]= \hat{f}\hat{g} -\hat{g}\hat{f}$$

It disctates the time evolution of $\hat{\rho}$ (which is time depend through $\mathcal{P}_i(t)$ and $\ket{\phi_i(t)}$):

$$\frac{\text{d}\hat{\rho}}{\text{d}t}= \frac{1}{i\hbar} [\hat{H},\hat{\rho}] $$

which follows and generalizes the  Schrödinger equation.

<details>
  <summary><strong>Proof:</strong></summary>

</details>

The probability distribution is independant of time if $\hat{H}$ commutes with $\hat{\rho}$: $[\hat{H},\hat{\rho}]=0$. This condition is satisfied for any function of the Hamlitonian: $\hat{\rho}=f(\hat{H})$, which are characteristic of **thermal equilibrium**.

