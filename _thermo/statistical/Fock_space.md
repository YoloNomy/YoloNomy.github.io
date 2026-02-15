---
layout: default
title: Fock space
parent: thermo
nav_order: 1
---

$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

## Microstate for multiple particles 

In the [previous lecture](./quantumstat.md), on Hilbert space, we saw that the statistical properties of a quantum system are encoded in the object $\ket{\phi}$ or $\hat{\rho}$. We must now understand how such an object can describe the systems associated to multiple particles, possibly interacting, as $\Gamma$ was in classical mechanics. How to built such a Hilbert space in a consistent way?

First, what should be our microstates? A crucial and irreconcible difference between classical and quantum mechanics is that, in classical mechanics, microstates $\Gamma$ were associated to unique, tangible physical realities (particle configurations). Finding $\rho(\Gamma)$ was looking for a statistical description of these possible realities. In quantum mechanics, the intrinsic and atomic describtion we use for the system is already intrinsically a probabilistic quantity $\ket{\phi}$ or $\hat{\rho}$.

A naive idea would be to assume that each classical microstate $\Gamma$ should be associated with a possible pure state $\ket{\Gamma}$ such that the quantum state of the total system $\ket{\psi}$ is a linear combination of classical microstates.
However, this can not be the right approach as due to the uncertainty principle ($[q_i,p_i]=i\hbar \delta_{ij}$), it is impossible to know both position and momentum perfectly. Thus the classical microstates can not be associated directly to quantum states $\ket{q_1,...q_\mathcal{N},p_1,...,p_\mathcal{N}}$. Furthemore, the transformation from classical phase space to Hilbert space, that is the replacement of the Poisson bracket with the commutator and of functions by operators change the structure of the theory in a deep and non trivial way. In short: there is a profound incompatibility between the classical geometry and the quantum geometry preventing us to do any simple transition from one to another. Finding this link is the topic of geometric quantization. As said in introduction, we will not further explore this direction here but instead build "from scratch" our quantum microstates for multiparticle systems.

In quantum mechanics, if a system is described by a wave-vector/density operator in a Hilbert space $\mathcal{H}_1$, the composition of $\mathcal{N}$ such systems is described by a wave-vector/density operator living on the tensor-product space of each individual subsystem, that is:

$$\mathcal{H}_{\mathcal{N}} = \mathcal{H}_1 \otimes \mathcal{H}_2 ... \otimes \mathcal{H}_{\mathcal{N}} $$

This tensor product is at the heart of quantum collective behaviour, at origin notably of the puzzling **quantum intrication**. Indeed, in such context, particles are not treated as separate, independent entities (and it is possible to do so only in specific conditions).
As a reminder (and illustration), imagine that $\mathcal{H}_1$ is a two dimensional Hilbert space, which could for exemple describing the spin of a particle. A basis of  $\mathcal{H}_1$ is given by two orthogonal vectors $(\ket{\phi_1}=\ket{\uparrow}$, $\ket{\phi_2}=\ket{\downarrow})$. A general $\phi \in \mathcal{H}_1$ is thus written:

$$\ket{\phi} = \alpha\ket{\phi_1} + \alpha_2\ket{\phi_2}$$

Where $\alpha_i$ quantify the probability for the particle to be observed as up or down ($\alpha_1\alpha_1^* +\alpha_1\alpha_2^*=1$). The Hilbert space of two identical particle treated together is $\mathcal{H}_2= \mathcal{H}_1 \otimes \mathcal{H}_1$. A basis for this space is $\lbrace \ket{\phi_1\phi_1}, \ket{\phi_1\phi_2}, \ket{\phi_2\phi_1}, \ket{\phi_2\phi_2} \rbrace$, where we used the shortcut notation
$\ket{\phi_i}\otimes \ket{\phi_j} = \ket{\phi_i \phi_j}$, and as a reminder, the first slot is associated to the first particle and the second slot to the second particle. A general vector $\psi\in  \mathcal{H}_2$ can be written as:

$$\ket{\psi} = \alpha_{11} \ket{\phi_1 \phi_1} + \alpha_{12} \ket{\phi_1 \phi_2} + \alpha_{21} \ket{ \phi_2 \phi_1} + \alpha_{22} \ket{ \phi_2 \phi_2 } $$

where we see clearly that the two particles are not treated separately. The $\alpha_i$ treat together the probability to observe the couple in a given state.

Tensor product of individual Hilbert space is a good candidate to be the space in which we can do statistical quantum physics. However, such an account can not be quite what we need for two critical features of statistical systems:

- **Varying particle numbers:** in nature we observe that the number of particles can change. For example, a light bulb emits photons (creating them). Even more strikingly, electrons can disapear when meeting a positron to transform into photons. This is a key feature of quantum field theory that can not be captured by elementary quantum mechanics.
- **Indistinguishability of particles:** quantum particles have very specific behaviour that can not be captured so trivially when they are exchanged. This behaviour related to the spin of the particles, and lead to a distinction between fermions and bosons. 

## Thinking in Fock space

To address the physical reality of varying particle numbers—where particles can be created or annihilated—we transition from a fixed-particle Hilbert space to the (non-symmetrised) **Fock space**: 

$$\tilde{\mathcal{F}}= \bigoplus^{\infty}_{i=0} \mathcal{H}_i$$

with $H_0=\mathbb{C}$ (representing the vacuum state, containing zero particles).
A general $\ket{\Phi}\in \tilde{\mathcal{F}}$ can be written as:

$$\ket{\Phi}= \alpha_0 \ket{0} + \alpha_1 \ket{\phi} + \alpha_2 \ket{\psi} + ... $$

where $\ket{\phi}\in \mathcal{H}_1$, $\ket{\psi}\in \mathcal{H}_2$ ... can be decomposed on a basis of $\mathcal{H}_1$ ($\ket{\phi_i}$) as described in the previous section. $\ket{\Phi}$ is thus an entangled sum of states with zero particle, a state with one particle etc. As such, $\tilde{\mathcal{F}}$ is a relevant space to allow for the change in particle numbers, as $\ket{\Phi}$ encompass different possibilities for $\mathcal{N}$ and while $\ket{\Phi}$ evolve with time from states with more or less particles, it changes the probability that the state with more or less particles are occupied. 

Let again $\ket{\phi_i}$ be a orthonormal basis of $\mathcal{H}_1$. In the case of spin it could be the two dimensional basis $\lbrace \ket{\phi_1}=\ket{\uparrow}$, $\ket{\phi_2}=\ket{\downarrow}\rbrace$, in the case of a quantum point particle it could be the infinite dimensional position eigenvectors $\ket{x}$. Staying in the case of $N$ discrete basis vectors, a basis of $\tilde{\mathcal{F}}$ is made of all the possible combination $$\ket{\phi_1}\otimes\ket{\phi_2} \otimes ...\ket{\phi_N}$$.
We can rewrite $\ket{\Phi}$ explicitely as

$$\ket{\Phi} = \sum_{\mathcal{N},i_1...i_\mathcal{N}}^{\infty} \alpha_{i_1,i_2... i_{\mathcal{N}}} \ket{\phi_{i_1}\phi_{i_2}...\phi_{i_{\mathcal{N}}}} $$

where the sum takes into account all possible permutations of the $i_i$ and goes over all possible particle number $\mathcal{N}$ up to infinity.

To be explicit and sure to understand what we mean by the previous expression, in the case where two basis state ($\ket{\phi_1},\ket{\phi_2}$) are accessible for the system. In such a case, a general state in $\tilde{\mathcal{F}}$ is written:

$$
\begin{aligned}
\ket{\Phi} &= 
\underbrace{\alpha_0 \ket{0}}_{\substack{\mathcal{N}=0}} \\
&+ \underbrace{\alpha_1 \ket{\phi_1} + \alpha_2 \ket{\phi_2}}_{\substack{\mathcal{N}=1}} \\
&+ \underbrace{
\alpha_{11}\ket{\phi_1\phi_1} + \alpha_{12}\ket{\phi_1\phi_2} + \alpha_{21}\ket{\phi_2\phi_1} + \alpha_{22}\ket{\phi_2\phi_2}
}_{\substack{\mathcal{N}=2}} \\
&+ \underbrace{
\alpha_{111}\ket{\phi_1\phi_1\phi_1} + \alpha_{112}\ket{\phi_1\phi_1\phi_2} + \alpha_{121}\ket{\phi_1\phi_2\phi_1} + \alpha_{122}\ket{\phi_1\phi_2\phi_2} \\
+ \alpha_{211}\ket{\phi_2\phi_1\phi_1} + \alpha_{212}\ket{\phi_2\phi_1\phi_2} + \alpha_{221}\ket{\phi_2\phi_2\phi_1} + \alpha_{222}\ket{\phi_2\phi_2\phi_2}
}_{\substack{\mathcal{N=3}}} \\
&+ \dots
\end{aligned}
$$

Now, there must be a way to simplify such expressions. A key feature we must use is **indistinguishability** and it's quantum generalisation. Indeed, terms as $\ket{\phi_2\phi_1}$ and $\ket{\phi_1\phi_2}$ are the same states in which particle 1 as been replaced by particle 2. But are they equal?

## Bosons and fermions

At the fundamental level, elementary particles are described by quantum fields. These abstract fields, are discussed in the associated [class](../../_quantum/quantum.md). The mathematical form that these fields can have is not purely arbitrary, but is deeply dictated by symmetry principle. In particular, the structure and symmetries of our space-time impose the fields to be associated with a number, the spin $s$, which can be either an integer or a half-integer. The value of $s$ is rather mysterious and dictates how the field transform under rotations and change of reference frame in space-time. Discussing it further is way beyond the scope of this class.
However, $s$ as a very important impact for statistical physics, as it divide the elementary particles into two distinct types:

- **fermions**: which are particles associated with fields of half-integer spins. We know that most particles forming matter: electrons, protons and quarks are fermions of spin $s=1/2$. This is also the case of every atomic nuclei with a odd number of nucleons.
- **bosons**: which are particles associated with fields of integer spins. Particles associated to fundamental forces of natures are bosons. This is the case for photons, gluons and $W$ and $Z$ bosons with $s=1$ and the Higgs boson with $s=0$. Atomic nuclei with an even number of nucleons also behave as bosons.

The link between the spins of particles and their statistical properties is a very subtle one, given by the so-called **spin-statistics** theorem which is notably difficult to prove.

In particular, the wavefunctions of bosons will remain unchanged if you operate a rotation in space by $360^{\circ}$ or if you swap two identical particles. However, the wavefunctions of fermions will get a minus sign under such operations. This strange fact has deep consequences on the cohesion of matter itself.

## Fock spaces for bosons and fermions

### Bosons

We will now construct the proper **Fock spaces**, on which we apply symmetry principles which account for the properties of bosons and fermions.

Bosons are truely **indistinguishable**, meaning that:

$$\ket{\phi_1\phi_2} = \ket{\phi_2\phi_1} $$

and similarly for any combination $\ket{\phi_1\phi_2\phi_1}=\ket{\phi_2\phi_1\phi_1}$. Hence, this simplify our expression for vectors in unsymmetrised Fock-space. For example, in the case of the two state system, we obtain: 

$$
\begin{aligned}
\ket{\Phi} &= 
\underbrace{\alpha_0 \ket{0}}_{\substack{\mathcal{N}=0}} \\
&+ \underbrace{\alpha_1 \ket{\phi_1} + \alpha_2 \ket{\phi_2}}_{\substack{\mathcal{N}=1}} \\
&+ \underbrace{
\alpha_{11}\ket{\phi_1\phi_1} + (\alpha_{12}+\alpha_{21})\ket{\phi_1\phi_2} + \alpha_{22}\ket{\phi_2\phi_2}
}_{\substack{\mathcal{N}=2}} \\
&+ \underbrace{
\alpha_{111}\ket{\phi_1\phi_1\phi_1} + (\alpha_{112}+ \alpha_{121}+ \alpha_{211})\ket{\phi_1\phi_1\phi_2}\\ 
+(\alpha_{122}+ \alpha_{221}+ \alpha_{212})\ket{\phi_1\phi_2\phi_2} 
+
\alpha_{222}\ket{\phi_2\phi_2\phi_2}
}_{\substack{\mathcal{N=3}}} \\
&+ \dots
\end{aligned}
$$

As such, the relevant information becomes the number of particles in a given state $\ket{\phi_i}$. We can rewrite:

$$
\begin{aligned}
\ket{\Phi} &= 
\underbrace{\alpha_{0,0} \ket{0,0}}_{\substack{\mathcal{N}=0}} \\
&+ \underbrace{\alpha_{1,0} \ket{1,0} + \alpha_{0,1} \ket{0,1}}_{\substack{\mathcal{N}=1}} \\
&+ \underbrace{
\alpha_{2,0}\ket{2,0} + \alpha_{1,1}\ket{1,1} + \alpha_{0,2}\ket{0,2}
}_{\substack{\mathcal{N}=2}} \\
&+ \underbrace{
\alpha_{3,0}\ket{3,0} + \alpha_{1,2}\ket{1,2} 
+\alpha_{2,1}\ket{2,1} +
\alpha_{0,3}\ket{0,3}
}_{\substack{\mathcal{N=3}}} \\
&+ \dots
\end{aligned}
$$

where we identified $\ket{0,0}=\ket{0}$, $\ket{\phi_1}=\ket{1,0}$, $\ket{\phi_2}=\ket{0,1}$, as well as $\alpha_{0,0}=\alpha_0$, $\alpha_{1,0}=\alpha_1$ ... and so on!
Here, we changed our perspective and the two slots in $\ket{a,b}$ do not represent particle one and particle two anymore, but instead the number of particles in state $\phi_1$ and the number of particles in state $\phi_2$.

Generalising for a case with $N$ accessible quantum states instead of two, we write a general bosonic vector-state as:

$$\ket{\Phi} = \sum_{n_i,n_j...,n_N}\alpha_{n_i,n_j ...}\ket{n_i,n_j ...,n_{N}} $$

### Fermions

For fermions, things are a bit more complicated. Particles are no more fully indistinguishable, as swapping two of them gives a minus sign to the wave function. For example:

$$\ket{\phi_1\phi_2} = -\ket{\phi_2\phi_1} $$

We can not justify this here, and this would require a fully dedicated class. A quick and "hand-wavy" explanation goes as follows: spin is related to how the wavefunction transform under a rotation of the system. More precisely, if a system of $s=1/2$ fermions described by a wavefunction $\ket{\psi}$ is rotated by an angle $\theta$, the wavefunction will transform as $e^{s\theta}\ket{\psi}= e^{\theta/2}\ket{\psi}$. Swapping two particles is equivalent to rotate the system by $180^{\circ}=\pi$. The wave function after swapping/rotating then becomes $e^{\pi/2}\ket{\psi}= -1\ket{\psi}$.

Now, there is a very profound consequence of this assymetry. Consider a state made of two particles in the same quantum state. Then, we should have:

$$\ket{\phi_1\phi_1}=-\ket{\phi_1\phi_1}$$
 
The only mathematical object which is the opposite of itself is zero. That is, the only way for the above equation to be satisfied is $\ket{\phi_1\phi_1}=0$. Similar consideration applies to any state with repeated state as $\ket{\phi_1\phi1\phi_2}$ and $\ket{\phi_1\phi2\phi_2}$. This is the so-called
**Pauli's exclusion principle** stating that two fermions can not be in the exact same quantum state. It has profound consequences on the structure itself of matter, as it is the reason why you are not going through the floor right now.

With this in mind, a two state wavefunction in Fock space for fermions is:

$$
\begin{aligned}
\ket{\Phi} &= 
\underbrace{\alpha_0 \ket{0}}_{\substack{\mathcal{N}=0}} \\
&+ \underbrace{\alpha_1 \ket{\phi_1} + \alpha_2 \ket{\phi_2}}_{\substack{\mathcal{N}=1}} \\
&+ \underbrace{
(\alpha_{12}-\alpha_{21})\ket{\phi_1\phi_2}
}_{\substack{\mathcal{N}=2}} \\
&+ \underbrace{0}_{\substack{\mathcal{N=3}}} \\
&+ \dots
\end{aligned}
$$

This is much simpler than for bosons! We see that all the 3 fermions states are excluded by our symmetry principle, as they would necessarly imply two particles in the same quantum state for a two state system.


$$
\begin{aligned}
\ket{\Phi} &= 
\underbrace{\alpha_{0,0} \ket{0,0}}_{\substack{\mathcal{N}=0}} \\
&+ \underbrace{\alpha_{1,0} \ket{1,0} + \alpha_{0,1} \ket{0,1}}_{\substack{\mathcal{N}=1}} \\
&+ \underbrace{
 \alpha_{1,1}\ket{1,1}
}_{\substack{\mathcal{N}=2}} \\
&+ \dots
\end{aligned}
$$

Generalising for a case with $N$ accessible quantum states instead of two, we write a general fermionic vector-state as:

$$\ket{\Phi} = \sum_{n_i,n_j...,n_N}\alpha_{n_i,n_j ...}\ket{n_i,n_j ...,n_{N}} $$

where $n_i = 0,1$.

## General approach to build Fock spaces

We glossed over some subtelties in the above presentation, namely the formal process of **symmetrisation** of Fock space. The proper space in which bosons and fermions leave is the not the "non symmetrized" fock space $\tilde{\mathcal{F}}$ presented first, but rather

$$\mathcal{F}= \mathcal{S}\left( \tilde{\mathcal{F}}\right)=\bigoplus^{\mathcal{N}}_{i=0} \mathcal{S}\left(\mathcal{H}_i\right)$$

where $S$ is a symmetrisation operator which allow to account for the boson or fermion statistical properties. In the previous section, we slopily made some identifications as $\ket{\phi_1\phi_2}= \pm \ket{\phi_2\phi_1}$ on the unsymmetrised Fock space and look at the consequences. The proper way to do so is to make the following identifications

- **Bosons:** $$(\mathcal{S}(\ket{\psi}) = \frac{1}{\sqrt{N!}} \sum_{\sigma} \ket{\psi_\sigma})$$
- **Fermions:** $$(\mathcal{S}(\ket{\psi}) = \frac{1}{\sqrt{N!}} \sum_{\sigma} \text{sign}(\sigma) \ket{\psi_\sigma})$$

In the case of a two state system, $\ket{0}$, $\ket{\phi_1}$ and $\ket{\phi_2}$ remain untouched by $\mathcal{S}$ while:

$$\mathcal{S}_{\text{boson}}(\ket{\phi_1\phi_2})= \frac{1}{2}\left(\ket{\phi_1\phi_2} + \ket{\phi_2\phi_1} \right) $$

and

$$\mathcal{S}_{\text{fermions}}(\ket{\phi_1\phi_2})= \frac{1}{2}\left(\ket{\phi_1\phi_2} - \ket{\phi_2\phi_1} \right) = \frac{1}{\sqrt{2}}\phi_1 \wedge \phi_2$$

Where $a\wedge b = a\otimes b - b\otimes a$ is the **exterior product** which plays a deep role in [advanced algebra](../../_maths/maths.md). Pauli's exclusion principle for two fermions naturally follows from the product properties as $$\ket{\phi_1}\wedge \ket{\phi_1}=0$$. Applying this symmetrisation correctly to $\tilde{\mathcal{F}}$ lead to the same conclusion as above. A general state in $\mathcal{F}$ can be written in term of its occupation numbers as

$$\ket{\Phi} = \sum_{n_i,n_j...,n_N}\alpha_{n_i,n_j ...}\ket{n_i,n_j ...,n_{N}} $$

## Statistical mechanics on Fock space

The shift we did from $\ket{\phi}_i$ to $\ket{n_1,n_2...n_N}$ is sometimes refered to as the **second quantization**.
When considering position of particles as the quantity of interest ($\ket{\phi_i}=\ket{x}$), we end up defining such a Fock space at each point of space(-time), and counting the number of particles present for the states at a given location. This leads precisely the notion of "field" in quantum field. We will leave a detailed discussion of this particularity for later.

Since Fock space itself is an Hilbert space, all the previous notions (entropy, density operator, time evolution) applies identically. Put more bluntly: all of the previous equations can be used now replacing $\ket{\phi(t)}$ by $\ket{\Phi(t)}$. One can construct $\hat{\rho}$ with states as $\ket{\Phi}$ and obtain from it 

$$\hat{\rho}= \frac{1}{\Xi}e^{-\beta\left(\hat{H}- \mu \hat{N}\right)}$$

Where $\hat{N}$ and $\hat{H}$ are the number and Hamiltonian operators in Fock space. 

$$ \hat{N}\ket{n_1,n_2...n_N}= \sum_i^{N}n_i\ket{n_1,n_2...n_N}$$

$$ \hat{H}\ket{n_1,n_2...n_N}= \sum_i^{N}n_i\epsilon_i\ket{n_1,n_2...n_N}$$

Note the close proximity with the quantum harmonic oscillator. Creation and anhilation operators can be defined in Fock space. But we will leave this topic for the quantum field theory class.

