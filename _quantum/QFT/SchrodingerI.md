---
layout: default
title: Schrodinger solutions
parent: QFT
nav_order: 1
---

$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

## Introduction

Standard quantum mechanics faces two major difficulties which do not make it compatible with experiments at high energies. 

- Dealing with varying number of particles: particles are destroyed and created continuously in physics experiments. This happens during interaction between different types of particles. For example, a bulb of light emits photons or collisions in colliders are able to generate new particles. Standard quantum mechanics can not describe such processes, as the Schrödinger equation does not allow for such transformations. The first part of this class will address how to go beyond this assumption using quantum fields instead of wave-functions in a process known as second quantization. 
- Being compatible with special relativity: space and time are treated asymmetrically in quantum mechanics: $t$ is a linear parameter and $x$ is an operator. Furthermore, Schrödinger equation is not covariant and is not preserved under a Lorentz boost. We will focus on this problem in the second part of this class, by considering relativistic fields.

As we will see in this class, facing these difficulties will lead us to quantum field theory (QFT). QFT is a very hard and rich topic, both conceptually and mathematically.

## Solutions of the Schrödinger equation for a single particle

### Schrödinger equation and its solutions

In quantum mechanics, the state of a system is described by a vector $\ket{\psi}$ in a complex Hilbert space $\mathcal{H}$. This vector depends solely on a given parameter, the time $t$. All other physical quantities like positions are  observables described by operator on $\mathcal{H}$. As such, we see already how time and space are treated asymmetrically in standard quantum mechanics: there is a single Hilbert space, and its object evolve as time passes (in the Schrödinger picture, the vectors evolve and the operators remain fixed). The time evolution of state vectors is given by the Schrödinger equation:

$$\hat{H}\ket{\psi(t)} = i\hbar\,\frac{d}{dt}\ket{\psi(t)},$$

which expresses the fact that $\hat{H}$, the **Hamiltonian operator**, is the generator of time translations (see class on symmetries). $\hat{H}$ is also the observable associated with the energy: its eigenvalues $E_n$ — which may form a discrete set, a continuous set, or a mixture — are the possible outcomes of an energy measurement, and (modulo subtleties for degenerate or continuous spectra) its eigenstates $\ket{\varphi_n}$ are the states in which the system is found after such a measurement.

The index $n$ may be discrete (e.g., bound states in a confined system) or continuous (e.g., free particles), and is typically a combination of both. Throughout, we write $\sum_n$ to denote a sum over discrete labels (which generalizes to integrals over continuous ones as we will discuss later), and $\delta_{n\beta}$ for the corresponding Kronecker delta. For time-translation-invariant ("isolated") systems, $\hat{H}$ has no explicit time dependence, so $E_n$ and $\ket{\varphi_n}$ are themselves time-independent. The eigenstates form an orthonormal basis of $\mathcal{H}$:

$$\braket{\varphi_n}{\psi_\beta} = \delta_{n\beta}, \qquad \sum_n \ket{\varphi_n}\bra{\varphi_n} = \mathbb{1},$$

and any state, at any time, can be expanded as $\ket{\phi} = \sum_n c_n \ket{\varphi_n}$ with $c_n = \braket{\varphi_n}{\phi}$. Proving this -- known as the spectral theorem -- carefully would require heavy mathematical machinery, which we leave for a dedicated class.

As mentioned previously, we glossed over the fact that energy eigenvalues are generically degenerate: different linearly independent eigenstates can share the same energy. Energy alone is therefore insufficient as a label for eigenstates. To resolve this, one introduces additional commuting observables, forming a **complete set of commuting observables** (CSCO), whose joint eigenvalues form a tuple $n$ of **quantum numbers** uniquely labeling each basis state. We write $\hat{H}\ket{\varphi_n} = E_n \ket{\varphi_n}$ with the understanding that $n$ is generally a tuple, and that distinct $n$'s can give the same $E_n$ (degeneracy).

Generally, using the correspondence principle, the Hamiltonian operator for a non-relativistic system is of the form:

$$\hat{H}= \frac{\hat{P}^2}{2m} + \hat{V}$$

We introduce the wave-function $\psi(x,t)= \braket{x}{\psi}$, which quantifies the probability amplitude for the particle to be measured at position $x=(x,y,z)$ and time $t$.
Because the linear momentum is the generator of spatial translations, we have $\bra{x}\hat{P}\ket{\psi} = -i \hbar \vec{\nabla}\psi$. Furthermore, assuming that the potential is just a function of the position, we have $\bra{x}\hat{V}\ket{\psi}=V(x)$ (for a derivation of the operator expressions, see [here](../Quantum_advanced/Symmetry.md)). As such, Schrödinger equation becomes: 

$$ i\hbar \frac{\partial \psi}{\partial t} = \left(-\frac{\hbar^2}{2m} \vec{\nabla}^2 + V\right)\psi$$

Solutions $\psi$ of this equation depends on the specific form of $V$ as well as the region of interest (i.e. if the system we consider is confined in a box, on a circle, or in an infinite space). 

It is both easier and mathematically cleaner to restrict our analysis to compact system, which is what we will often do by considering particles restricted to move in a box of fixed volume $\mathcal{V}$. The case of a particle free to move in the entierty of space can easily be found by taking the limit $\mathcal{V}\to \infty$ in our expressions.

If the system is contained within a compact region, general solutions of the Schrödinger equations are of the form:

$$\boxed{\psi(x,t) = \sum_n \alpha_n(t) \varphi_n(x)}$$

with $\varphi_n=\braket{x}{\varphi_n}$ and $\alpha_n(t)$ are complex coefficients quantifying how much each eigenstate contributes at different times i.e. what is the probability to observe the energy state $E_n$ at time $t$. If energy levels are degenerated, they are just repeated in the sum with different quantum numbers and $\alpha_n$ is the probability to observe the state with all the quantum numbers $n$. This result simply comes from the fact that the $\ket{\varphi_n}$ vectors forms a basis of $\mathcal{H}$.

In general, the time evolution is given by:

$$\boxed{\alpha_n(t) = \alpha_{n,0}e^{-i(E_n t)/\hbar}}$$

with $\alpha_{n,0}=\alpha_n(t=0)$ being the initial value of the probability amplitudes at $t=0$.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

We assume that the $\ket{\varphi_n}$ forms an orthonormal basis of the Hilbert space (which is a standard result of quantum mechanics if the system is well-behaved). We also assume that $H_n$ is discrete. $n$ could be degenerated, as such sums over $n$ would simply range over all the quantum numbers. 
The initial state can be decomposed on this basis as

$$\ket{\psi}(t=0) = \sum_n \alpha_n \ket{\varphi_n}$$

where $\alpha_n = \braket{\varphi_n }{\psi(t=0)}$ are the coefficients of this decomposition.

Now assume that the time evolution is of the form

$$\ket{\psi}(t) = \sum_n \alpha_{n,0} c_n(t)\ket{\varphi_n} $$

with $c_n(t=0)=1$. Inserting this solution in Schrödinger equation, we obtain

$$ i\hbar \dot{c_n} = E_n c_n $$

Which is solved by 

$$ c_n(t) = e^{-iE_nt/\hbar} $$

Thus, the proposed solution is indeed a solution of Schrödinger equation. 
Furthermore, using self-adjointness of $\hat{H}$ and the properties of the hermitian product, it is possible to prove that this solution is unique.

</details>

### Spinless free particle in a box

The form of $\varphi_n$ depends on the choice of boundary conditions and the exact problem at stake. For this class, we will often consider the case of a free particle in a cubic box of finite volume $\mathcal{V}$ and length $L$. Different expression for the solution will depend on the choice made to fix the boundary conditions. For this class, this choice does not matter much, as we will be ultimately interested in the limit where $\mathcal{V}\to \infty$, and this limit should obviously not depend on our choice of boundary condition. The most convenient choice for our matters is the so-called periodic boundary conditions asking that the wave-function repeats itself in the box: $\psi(0)=\psi(L)$ and $\psi'(0)=\psi'(L)$. In such scenario, we obtain:

If the particle has no spin, the label $n$ is really an index labelling discrete, infinite and non-degenerate energy levels.

It is possible to show that:

$$\varphi_n(x)= \frac{1}{\sqrt{L}}e^{ i \vec{p}_n\cdot \vec{x}}$$

with momentum and energy taking only discrete quantized values $p_n = \frac{2\pi n}{L\hbar}$ and $E_n= \frac{\hbar^2 k_n^2}{2m}= \frac{2\pi^2\hbar^2n^2}{mL^2}$. Under the De-Broglie identification $E_n = \hbar \omega_n$ and $\vec{p}_n= \hbar \vec{k}_n$, general solutions are thus given by a superposition of plane waves:

$$\boxed{\psi(x,t) = \frac{1}{\sqrt{L}}\sum_n \alpha_{n,0} e^{i \vec{k}_n\cdot\vec{x}-\omega_n t}}$$


<details markdown="1">
  <summary><strong>Proof</strong></summary>

Looking for the eigenvalues of $\hat{H}$:

$$\hat{H}\ket{\varphi_n}= E_n \ket{\varphi_n} $$

for a free particle (in position representation):

$$-\frac{\hbar^2}{2m} \vec{\nabla}^2\varphi_n = E_n \varphi_n$$

$$\vec{\nabla}^2\varphi_n = \frac{2m E_n}{\hbar}\varphi_n $$

The general solution is of the form 

$$\varphi_n = A e^{i\sqrt{\frac{2m E_n}{\hbar}}t} + Be^{-i\sqrt{\frac{2m E_n}{\hbar}}t}$$

</details>

As stated above, we will be interested in the general solution of the Schrödinger equation describing a single free particle being able to move through space. To do so, we take the infinite volume limit, that is $L \to \infty$, we find: 

$$\boxed{\psi(x) = \int \tilde{\psi}(k)e^{ - i\omega t} \text{d}\vec{k} = \int \alpha_0(k) e^{ - i\omega t -i\vec{k}\cdot \vec{x}} \text{d}\vec{k}}$$

with $\psi_n \to \tilde{\psi}(k)$. We find back that the momentum states are the **Fourier transform** of the position states.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

## How system couple? The case of two particles

## Classical physics and the cartesian product

Let's now ask a simple question which has a difficult answer: how do multiple quantum system combine and interact?

First, let's look at the classical case. Take a system, say a particle. It is fully described by its position $q_1$ and momentum $p_1$, (both being triplets in three dimension) and thus evolves in a (six dimensional) phase space $\Pi_1$. The time evolution in phase space is dictated by a Hamiltonian function $H_1(q_1,p_1)$, through Hamilton's equations:

$$\frac{\text{d} q_1}{\text{d} t} = \frac{\partial H_1}{\partial p_1 },  \qquad \frac{\text{d} p_1}{\text{d} t} = -\frac{\partial H_1}{\partial q_1 }$$

which result both from the rich symplectic structure of phase space and the fact that $H$ is the generator of time translations. See our dedicated notes for more on this point.
Consider now a second system, described by the pair $q_2, p_2$ and living in phase space $\Pi_2$ equipped with Hamiltonian $H_2(q_2,p_2)$. 
Our classical intuition tells us that the description of the two systems together will simply be given by the four numbers $q_1,p_1,q_2$ and $p_2$ and this is indeed the case.
The phase-space describing the two particles is simply the Cartesian product space $\Pi=\Pi_1 \times \Pi_2$ of dimension ${\rm dim}(\Pi_1) + {\rm dim}(\Pi_2)=12$ and whose point is a quadruplet of three dimensional vectors: $(q_1,p_1,q_2,p_2)$. Hence, the Cartesian product simply adds the two descriptions, without mixing them anyhow. In that sense, it is really similar to adding a new dimension (for example, the $xy$ plane is described by the Cartesian product $\mathbb{R}\times \mathbb{R}$).

The Hamiltonian function generating evolution is given by the function

$$\boxed{H = H_1(q_1,p_1) + H_2(q_2,p_2) + H_{\rm int}(q_1,q_2,p_1,p_2)}$$

which guides completely the time evolution of the quadruplet $(q_1,p_1,q_2,p_2)$ in the phase space $\Pi$ through the Hamilton equations

$$\frac{\text{d} q_i}{\text{d} t} = \frac{\partial H}{\partial p_i} = \frac{\partial H_1}{\partial p_i} + \frac{\partial H_2}{\partial p_i} +  \frac{\partial H_{\rm int}}{\partial p_i}$$

$$\frac{\text{d} p_i}{\text{d} t} = -\frac{\partial H}{\partial q_i} = - \frac{\partial H_1}{\partial q_i} - \frac{\partial H_2}{\partial q_i} -  \frac{\partial H_{\rm int}}{\partial q_i}$$

Where $i$ is either $1$ or $2$. First, since $H_1$ does not depend on $q_2$ and $p_2$ and neither does $H_2$ on $q_1$ and $p_1$, we get:

$$\frac{\text{d} q_i}{\text{d} t} =  \frac{\partial H_i}{\partial p_i} +  \frac{\partial H_{\rm int}}{\partial p_i}$$

$$\frac{\text{d} p_i}{\text{d} t} = - \frac{\partial H_i}{\partial q_i} -  \frac{\partial H_{\rm int}}{\partial q_i}$$

We see that if $H_{\rm int}=0$, the two systems evolve separately, and we obtain the two independent original Hamilton equations, as desired. In a sense, this is a justification of why the energy of the two individual system must be added in the total energy. 
$H_{\rm int}$ allows particles to influence one another, which is really what we expect for an interaction.
If $H_{\rm int}$ contains terms involving only $q_i$, $p_i$, they can be reabsorbed as a potential in the $H_i$, and thus will not produce any interaction. As such, only terms containing both variables of particle 1 and particle 2 coupled together can generate interactions in $H_{\rm int}$. As such, $H_{\rm int}$ has to include product terms that mix variables from both subsystems as $q_1q_2$ or $p_1p_2$, $q_1p_2$ for the derivative with respect to $q_1$ or $p_1$ to lead terms depending on $q_2$ or $p_2$ and vice-versa, such that variables of one particle can influence the dynamics of the variables of the second. The classical example being a term which is a nonlinear function of the distance between the two particles $|q_1-q_2|$. Looking at Hamilton equations, we see that such term would induce a time variation of both momenta $p_1$ and $p_2$ depending on the other particle's position $q_2$ and $q_1$ respectively. A term function of $|q_1-q_2|$ will thus be an interaction **potential energy** generating a **force** in the sense of Newtonian mechanics, which is symmetric (satisfying also Newton third law). Classical examples are squared like the restorative force of a spring in $(q_2-q_1)^2$ or the inverse of the distance $1/(|q_2-q_1|)$, like a central force.
Interaction terms function of $p_1$ and $p_2$ would generate more complicate behaviour and impact velocities instead of accelerations. Such functions occur for example in the context of relativistic physics and we will not discuss them further here.

## Quantum physics and the tensor product

Now, let's see how this generalizes to the quantum case. Consider a first system, like a particle, described by a Hilbert space $$\mathcal{H}_{(1)}$$. Its time evolution is described by a Hamiltonian $$\hat{H}_1$$ with eigenfunction $$\ket{\varphi_{n}}$$.
Consider now a second system, described by another Hilbert space $$\mathcal{H}_{(2)}$$ with Hamiltonian $$\hat{H}_2$$ of eigenfunctions $$\ket{\varphi_{m}}$$.

Quantum mechanics tells us that the right structure to describe the two systems together is given by the tensor product space 
$$\mathcal{H} = \mathcal{H}_{(1)} \otimes \mathcal{H}_{(2)}$$, which is the Hilbert space describing the two systems at once. If $\ket{\varphi_{n}}$ and $\ket{\phi_{m}}$ are complete basis of $$\mathcal{H}_{(1)}$$ and $$\mathcal{H}_{(2)}$$, then $\ket{\varphi}_n \otimes \ket{\phi}_m$ is a basis of $\mathcal{H}$. General states $\ket{\Phi}$ are thus linear combination of the two particles being in different states, allowing for entangled states.

<details markdown="1">
  <summary><strong>Reminder on tensor product</strong></summary>

</details>

Indeed, the tensor product $\otimes$ is very different than the Cartesian product of classical mechanics. Instead of combining simply the two pairs of the into a quadruplet $(q_1,q_2,p_1,p_2)$, the tensor product mixes the coordinates and momentum of both systems such that they are no more independent of one another. For simplicity, let's consider that particles are allowed to move only in one spatial dimension, and thus living in a two dimensional phase space, such that $q_1,q_2,p_1,p_2$ simply are functions on $\mathbb{R}$ instead of vectors. We write $e_{q}^{(1)}$ and $e_{q}^{(2)}$ the basis vector of positions for particles $1$ and $2$ and $e_{p}^{(1)}$ and $e_{p}^{(2)}$ the basis vectors for momenta of each particle.

As discussed previously, a general element of $\Pi_1 \times \Pi_2$ is the four dimensional vector:

$$C = c_{q_1} e_q^{(1)} +  c_{q_2} e_q^{(2)} + c_{p_1} e_p^{(1)} +  c_{p_2} e_p^{(2)}$$

As a shortcut, we write $c_{q_1} = q_1$, $c_{q_2}=q_2$, $c_{p_1}=p_1$ and $c_{p_2} = p_2$.

$\Pi_1\otimes\Pi_2$ would be a strange space instead. A general element of $\Pi_1\otimes\Pi_2$ is a real linear combination of these four basis vectors:

$$T = c_{q_1q_2}\,e_q^{(1)}\otimes e_q^{(2)} + c_{q_1p_2}\,e_q^{(1)}\otimes e_p^{(2)} + c_{p_1q_2}\,e_p^{(1)}\otimes e_q^{(2)} + c_{p_1p_2}\,e_p^{(1)}\otimes e_p^{(2)},$$

with four free real coefficients $c_{qq}, c_{qp}, c_{pq}, c_{pp} \in \mathbb{R}$.
The replacement of $\times$ by $\otimes$ is, in a real sense, the source of entanglement — and through it, of much of what makes quantum mechanics genuinely strange.

The Hamiltonian of the combined system takes the general form:

$$\boxed{\hat{H}=\hat{H}_1 \otimes \mathbb{I}_2 + \mathbb{I}_1 \otimes \hat{H}_2 + \hat{H}_{\text{int}}}$$ 

If $$\hat{H}_{\text{int}}=0$$, then $$\hat{H}$$ has eigenfunctions $\ket{\varphi}_n \otimes \ket{\phi}_m$. Otherwise, in the case of interactions, the eigenvectors and the energy levels of the combined interacting system are not the ones of the individual systems and the time-evolution of both field is not independent: the two subsystem get entangled as time passes.

In the case of no-interactions, we can get by combining the individual solutions of the Schrödinger equation:

$$\ket{\psi_{12}} = \ket{\psi_1}\otimes\ket{\psi_2} = \sum_{n,m} \alpha_{n}(t)\alpha_{m}(t) \ket{\varphi_{n}}\otimes \ket{\phi_{m}}$$

which in wavefunction space gives

$$\psi_{12}(x_1,x_2) = \sum_{n,m} \alpha_{n,m}(t) \varphi_{n}(x_1)\phi_{m}(x_2)$$

with

$$\alpha_{n}(t)\alpha_{m}(t) = \alpha_{0,n}\alpha_{0,m}e^{-i(E_n + E_m)t/\hbar}$$

Thus, the basis are "product states" which are not entangled, but a general state is entangled.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

Now, how about if the two systems are identical?

### $\mathcal{N}$  Bosons and fermions in a box

