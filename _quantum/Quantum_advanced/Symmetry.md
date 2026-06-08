---
layout: default
title: Operators from symmetry
parent: thermo
nav_order: 1
---

$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

## Lie groups and Lie algebra for physicists

## Representation of groups

## Stone theorem

## Expression for classical quantum operators 

On $\mathcal{H}$, $\ket{\psi}$ is a vector and $\hat{X}$, $\hat{V}$, $\hat{P}$ are linear operators $\mathcal{H}\to \mathcal{H}$.

We write $\ket{x}$ the eigenvectors of $\hat{X}$, which form a complete orthogonal basis of $\mathcal{H}$: $\braket{x}{x'}= \delta(x-x')$, $\int \ket{x}\bra{x}\text{d}x=1$. Furthermore, we will assume the fundamental commutation relations $\[\hat{X},\hat{P}\]=i\hbar$, inherited from the Poisson braket in classical mechanics.

### The Hamiltonian

$\hat{H}$ is defined to be the generator of time translations of $\ket{\psi}$, that is, for any time interval $\text{d}t$:

$$\ket{\psi(t+\text{d}t)} = e^{-\frac{i}{\hbar}\hat{H}\text{d}t}\ket{\psi(t)}$$

where the factor $-\frac{i}{\hbar}$ is pure convention.
Taking the limit $\text{d}t \to 0$:

$$\ket{\psi(t+\text{d}t)} \simeq_{\text{d}t\to 0} (1-\frac{i}{\hbar}\hat{H}\text{d}t)\ket{\psi(t)}$$

$$ \lim_{\text{d}t\to 0} \frac{\ket{\psi(t+\text{d}t)}- \ket{\psi}(t)}{\text{d}{t}} = -\frac{i}{\hbar}\hat{H} \ket{\psi}(t) $$

and hence

$$\frac{\text{d}\ket{\psi}}{\text{d}t} = -\frac{i}{\hbar}\hat{H}\ket{\psi} $$

### The momentum

### The potential

If $\hat{V}$ can only be expressed in term of the operator $\hat{X}$, which we will assume, from classical mechanics, $\hat{V}$ is self-adjoint and eigenvectors of $\hat{X}$ are also eigenvectors of $\hat{V}$:

$$\hat{V}\ket{x} = V(x)\ket{x}$$

Hence:

$$\bra{x}\hat{V}\ket{\psi} = (\hat{V}\ket{x})^{\dagger}\ket{\psi} = V(x)\braket{x}{\psi}= V(x)\psi(x)$$


## Uncertainty relations and Fourier transform

Consider an operator $\hat{O}$ with eigenvectors $\ket{o_i}$ and eigenvalues $o_i$.

$$\hat{O} = -i\hbar\partial_y $$

The eigenvalue equation thus leads:

$$o_i\ket{o_i} = -i\hbar\partial_y \ket{o_i}$$

which general solutions are of the form:

$$\ket{o_i} \propto e^{i \frac{o_i y }{\hbar}}$$

Furthermore, if $\ket{o_i}$ forms a basis of $\mathcal{H}$, any vector can be written as

$$\ket{\psi} = \sum \alpha_i \ket{o_i} $$

(or integral for continuous cases).

Thus 

$$\ket{\psi} = \sum \alpha_i e^{i \frac{o_i y }{\hbar}}\ket{o_i} $$

Hence the famous relation:

$$\Delta p \Delta x \geq \hbar/2$$

$$\Delta E \Delta t \geq \hbar/2$$

Even though there is **no** time observable.

Similarly we would have:

$$\Delta L \Delta \theta \geq \hbar/2$$

and for gauge:

$$\Delta Q \Delta \varphi \geq \hbar/2$$

where $Q$ is the electric charge and $\varphi$ the phase of the wavefunction. Superselection rules + Josephson effect 

## Bonus: spherical harmonics
