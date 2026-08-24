---
layout: default
title: General relativity, field theory or geometry?
parent: cosmo
---


As discussed in the [first lecture](./foundations-GR.md), GR is largely interpreted as geometry of space and time. However, the other theories of modern physics — as Yang-Mills gauge theories of particle physics — are not usually understood this way, and more often presented as "field theories", in which various fields evolve and interact[^1]. This raises the natural question: is GR a field theory, and in what sense? Or, in other words, can we forget everything about geometry when talking about GR, and instead present it purely as a field theory? We will see that GR can be interpreted either as a theory describing a field propagating on a flat space-time background, or as a geometrical theory. These are two faces of the same coin, and both aspects will become important when looking for extensions of GR.

[^1]: Note however that Yang-Mills theory also has a deep and often overlooked geometrical interpretation: a gauge field is a connection on a principal bundle, and its field strength is the curvature of that connection. For more on this topic, see e.g. [Baez & Muniain (1994)](https://pages.jh.edu/rrynasi1/PhysicalPrinciples/literature/Baez+Muniain1994GaugeFieldsKnots+Gravity.pdf) or [Frankel (1997)](https://api.pageplace.de/preview/DT0400.9781139154147_A23866698/preview-9781139154147_A23866698.pdf). The dichotomy "geometry vs. field theory" is therefore a false one from the start — the real question is which geometry, and how much of it is dynamical.

## GR as a field theory

### What is a field theory?

A field $\hat{\phi}(x,y,z,t)=\hat{\phi}(x^\mu)$ is an object[^2] that associates a mathematical quantity to each point of space-time $M$. This quantity can be, for example, a number (scalar), a vector, a spinor, or a tensor. In that sense, we already encountered several fields in our [first lecture](./foundations-GR.md), such as the stress-energy tensor field $T$, or the matter fields $\psi$. The metric $g$ is arguably a tensor field, but a very special one, as it is the object defining the geometry in every tangent space of space-time. The central question for us now is to understand whether GR can be seen as a field theory for the field $g$ on the flat space-time of special-relativity, and what is meant by that.

[^2]: More accurately, a field is to be understood as a section of a specific bundle over space-time $M$.

A field theory describes the evolution of a field $\hat{\phi}$ and is given by the data of a Lagrangian of the form:

$$\boxed{\mathcal{L} = \mathcal{L}_{\rm kin}(\hat{\phi}) - V(\hat{\phi}) + \mathcal{L}_{\rm int}(\hat{\phi},J) + \mathcal{L}_m(\psi)}$$

where $\mathcal{L}_{\rm kin}$ is the kinetic Lagrangian for the field, describing its energy due to its self-motion, and $V(\hat{\phi})$ is the field potential, describing its possible self-interactions. $\mathcal{L}_m(\psi)$ is the Lagrangian of the other fields that can exist in the Universe. $J$ is some form of **current**, expressed in terms of all the other possible fields $\psi$ the field can be coupled to. It takes the general form:

$$\mathcal{L}_{\rm int}(\hat{\phi},J) = \kappa \langle J\hat{\phi}\rangle$$

where $\kappa$ is the charge (coupling constant) of the interaction and $$\langle ...\rangle$$ is a specific procedure combining $J$ and $\hat{\phi}$ to create a scalar.

If the field evolves in a flat space-time with rigid metric $\eta$, the field evolution is obtained by extremizing $S=\int \mathcal{L}\, \text{d}^4x$, and is given by the Euler-Lagrange equations:

$$\frac{\partial \mathcal{L}}{\partial \hat{\phi}} = \partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \hat{\phi})}\right)$$

The proof of this equation is really similar to the proof of D2 in [our first lecture](./foundations-GR.md), with $g=\eta$ and $\sqrt{-g}=1$.

The standard textbook example of a field theory is the case of a scalar field $\phi$ with a potential (from now on, we will use $\phi$ exclusively for scalars). Scalar fields are very important in cosmology, and we shall discuss them a lot in these lectures. For more on them, see also our future class [dedicated to it](./Brans-Dicke.md). Such a field has

$$\mathcal{L}_{\rm kin}= -\frac{1}{2}\partial_\mu\phi\partial^\mu\phi= -\frac{1}{2}\eta^{\mu\nu}\partial_\mu\phi \partial_\nu \phi$$

where the minus sign comes from our choice of signature $(-,+,+,+)$ — unfamiliar to the particle physicist, but common in gravity theory. This kinetic Lagrangian can be justified in different ways, either as the continuous limit of some interconnected springs (See e.g. [Zee (2010)](http://www.stat.ucla.edu/~ywu/Zee.pdf)), as the relativistic generalisation of Schrödinger equation, or from first principles using space-time symmetries (see e.g. [Schwichtenberg (2018)](https://pierre.ag.gerard.web.ulb.be/textbooks/books/Physics_from_Symmetry.pdf)). The total Lagrangian is thus:

$$\mathcal{L}= -\frac{1}{2}\partial_\mu\phi\partial^\mu\phi - V(\phi)$$

leading to the equation of motion:

$$\Box \phi \equiv \partial_\mu \partial^\mu \phi = \frac{\partial V}{\partial \phi}$$

where we introduced the **d'Alembertian** $\Box \equiv \eta^{\mu\nu}\partial_\mu\partial_\nu = -\partial_t^2 + \nabla^2$. Beware of the sign: with signature $(-,+,+,+)$, $\Box = -\partial_t^2 + \partial_x^2+\partial_y^2+\partial_z^2$, *not* the other way around.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

The Euler-Lagrange equation extremizing the action for fields in **flat** space-time is:

$$\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\right) = \frac{\partial \mathcal{L}}{\partial \phi}$$

(In curved space-time, $\partial_\mu$ would be replaced by $\frac{1}{\sqrt{-g}}\partial_\mu\left(\sqrt{-g}\;\cdot\;\right)$; as discussed in [this class](../cosmo/scalar_fields.md)).

Now, in our case, we have for the left-hand side:

$$
\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\right) = -\frac{1}{2}\partial_\mu \left(\frac{\partial( \partial_\nu \phi \partial^\nu \phi)}{\partial (\partial_\mu \phi)}\right)
$$

where we renamed the dummy summation index $\nu$ to distinguish it from the derivative index $\mu$. Now, the product rule gives:

$$
\frac{\partial(\partial_\nu \phi \partial^\nu \phi)}{\partial (\partial_\mu \phi)} = \frac{\partial (\partial_\nu \phi)}{\partial (\partial_\mu \phi)}\partial^\nu \phi + \partial_\nu \phi \frac{\partial(\partial^\nu \phi)}{\partial (\partial_\mu \phi)}
$$

We can then use the metric to rewrite $\partial^\nu \phi = \eta^{\nu \sigma}\partial_\sigma\phi$, and use that the derivative of a variable with respect to itself is the Kronecker delta, $\frac{\partial(\partial_\nu\phi)}{\partial(\partial_\mu\phi)} = \delta^\mu_{\ \nu}$ (note the *mixed* index placement: one up, one down — this is the only index structure that makes sense here, since the two derivatives carry indices in opposite positions). We get:

$$
\begin{align}
&\frac{\partial(\partial_\nu \phi)}{\partial (\partial_\mu \phi)}\partial^\nu \phi + \partial_\nu \phi \frac{\partial(\partial^\nu \phi)}{\partial (\partial_\mu \phi)}  \\
&=\frac{\partial(\partial_\nu \phi)}{\partial (\partial_\mu \phi)}\partial^\nu \phi + \partial_\nu \phi\, \eta^{\nu \sigma}\frac{\partial( \partial_\sigma\phi)}{\partial (\partial_\mu \phi)}  \\
&=  \delta^\mu_{\ \nu} \partial^\nu \phi + \partial_\nu\phi\, \eta^{\nu \sigma} \delta^\mu_{\ \sigma} \\
&= \partial^\mu \phi + \partial^\mu\phi\\
&= 2 \partial^\mu \phi
\end{align}
$$

Putting this back in our original expression for the left-hand side of the Euler-Lagrange equation, we get:

$$
\begin{align}
\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\right) &= -\frac{1}{2}\partial_\mu (2\partial^\mu \phi) \\
&= -\partial_\mu \partial^\mu \phi = -\Box\phi
\end{align}
$$

Now, the right-hand side is simply:

$$\frac{\partial \mathcal{L}}{\partial \phi} = -\frac{\partial V}{\partial \phi}$$

as $V$ is the only part of $\mathcal{L}$ that depends on $\phi$ itself. Equating both sides in the Euler-Lagrange equation, we get:

$$
\begin{align}
\Box \phi = \partial_\mu\partial^\mu \phi = \frac{\partial V}{\partial \phi}
\end{align}
$$

</details>

The **mass** of a field is generally defined as the curvature (second derivative) of the potential around its minimum $\hat{\phi}_0$:

$$\boxed{m_{\hat{\phi}}^2 = \left.\frac{\partial^2 V}{\partial \hat{\phi}^2}\right|_{\hat{\phi}_0}}$$

The archetype being the quadratic potential $V(\phi)=\frac12 m^2\phi^2$ for a scalar field, for which the equation of motion becomes the **Klein-Gordon equation**

$$(\Box - m^2)\phi = 0 $$

whose plane-wave solutions $\phi \propto e^{i(k\cdot x - \omega t)}$ obey the relativistic dispersion relation $\omega^2 = k^2+m^2$. 

Now the interaction term of a scalar field with other fields $$\mathcal{L}_{\rm int}(\hat{\phi},J)$$ can take different forms, depending on which kind of force it mediates and which kind of field it interacts with. The key is that the interaction Lagrangian should be a scalar. As a general matter of fact, one can think of making either a scalar current $J$ out of the other fields or a vector current field $J^\mu$ (like in electromagnetism), such that we can propose simply:

$$\mathcal{L}_{\rm int,scalar}(\phi,J)= \kappa \phi J \qquad \mathcal{L}_{\rm int,vector}(\phi,J) = \kappa \partial_\mu \phi J^\mu$$

Both have very different phenomenology. Perhaps the simplest scalar interaction term that one can think of for a scalar field interacting with fermionic matter is of the form $\mathcal{L}_{\rm int}(\phi,J)= \kappa \bar{\psi}\phi\psi$, where $J=\bar{\psi}\psi$ and $\bar{\psi}=\psi^\dagger \gamma^0$. Such a term is called a **Yukawa coupling** and is exactly how the Higgs boson couples to matter particles to give their masses. Now, can we find some such coupling able to explain the gravitational force?

## What can gravity be coupled to?

We now try to fit GR into the boxed template above. We saw that the Einstein-Hilbert action is

$$\mathcal{L}_{\rm EH} = \frac{1}{16\pi G} \sqrt{-g}\,(R-2\Lambda) + \mathcal{L}_m[g,\psi]$$

and at first sight this looks nothing like $$\mathcal{L}_{\rm kin} - V + \mathcal{L}_{\rm int}$$ and we thus see that GR does not seem to follow the simple Lagrangian structure that we proposed above, seriously threatening our chances to understand it as a field theory. However, not all hope is lost, as we will see. Instead of starting from $\mathcal{L}_{\rm EH}$ and trying to identify a field theory, we will try to build a field theory of gravity from scratch and see whether we can re-obtain general relativity.

So, we are looking for a field $\hat{\phi}$, mediator of gravity, that might allow us to describe gravitation as a field theory. We call this field the **graviton**. Note however that this does not mean that the graviton is a quantum field or a particle or any of the sort. We are talking exclusively about classical fields here. The graviton is characterized by its spin, that is, how it transforms under a rotation. It could be a scalar field of spin 0, $\phi$, a vector field of spin 1, $A_\mu$, or a tensor field of some rank, e.g. $h_{\mu\nu}$ or $Z_{\mu\nu\sigma}$. If the tensor is symmetric and the field massless, it is possible to show that the spin of the field corresponds to the rank of the tensor. Hence, a rank-two symmetric tensor $h_{\mu\nu}$ would be a spin-2 object.

<details markdown="1">
  <summary><strong>Spin and tensors</strong></summary>

The spin of a field tells us how its components mix under a spatial rotation[^spin]. A scalar $\phi$ has a single component, and it does not change at all under rotations: it is spin 0. A vector $A_\mu$: its transverse components $(A_x,A_y)$ rotate into each other like an ordinary arrow, and the pattern returns to itself after a full turn $2\pi$: it is a spin 1 field. A symmetric tensor $h_{\mu\nu}$ carries *two* vector indices, each of which picks up one rotation matrix — schematically $h \to R\,R\,h$ — so a rotation by $\theta$ acts "twice", and the pattern returns to itself after only $\pi$: it is a spin 2 ield. This is directly visible in a gravitational wave: the "$+$" polarisation (stretch along $x$, squeeze along $y$) is mapped to *minus itself* by a $90°$ rotation, back to itself after $180°$, and is mapped onto the "$\times$" polarisation by a $45°$ rotation. That $45°$ angle between the two polarisations is the experimental fingerprint of spin 2 (for a photon, the two linear polarisations are at $90°$).

[^spin]: more formally, spin labels the irreducible representation of the Lorentz group under which the field transforms. As such, it quantifies both the transformation properties of the fields under spatial rotations and boosts. All the infinite dimensional irreducible representations of the Lorentz group can be labelled by two half integer number $j_1$ and $j_2$, and their sum $s=j_1+j_2$ is what we usually call spin.

A symmetric $4\times 4$ tensor has 10 independent components. Under spatial rotations, these organise as: $h_{00}$ (1 component, a scalar), $h_{0i}$ (3 components, a vector), and the symmetric $3\times3$ block $h_{ij}$ (6 components), which splits further into its trace (1 component, a scalar) and its symmetric **traceless** part (5 components). Now, a spin-$s$ representation of the rotation group has exactly $2s+1$ components; since $5 = 2\times 2+1$, the traceless part of $h_{ij}$ is a spin-2 object — the highest spin contained in a symmetric rank-2 tensor. (This is why we insist on *symmetric*: a general rank-2 tensor also contains an antisymmetric part, 6 components which organise as two spatial vectors — think of $E_i = F_{0i}$ and $B_i = \frac12\epsilon_{ijk}F_{jk}$ for the electromagnetic field strength — i.e. spin-1 content, not spin 2.)

For a *massless* field, gauge invariance (which we will meet in the Fierz-Pauli section below) removes all the lower-spin pieces: of the 10 components of $h_{\mu\nu}$, only the two helicity $\pm 2$ modes actually propagate. This is the exact analogue of the photon: $A_\mu$ has 4 components, but only the 2 transverse polarisations are physical. The general rule for a massless symmetric rank-$s$ tensor is: 2 propagating modes, of helicity $\pm s$. Hence the statement in the main text: *massless symmetric rank 2 $\Rightarrow$ spin 2*. (A *massive* spin-2 field, by contrast, keeps all $2s+1=5$ modes — a fact that will come back to haunt us in the massive-gravity case).

</details>

Now, let us ask ourselves: **what would be the current $J$ that the graviton should couple to?** Here, the equivalence principle gives us the answer almost for free. More precisely, we saw that the incredible precision at which the UFF is verified led us to propose the **weak equivalence principle** (WEP) as a principle of GR. It states that all bodies fall in the same way in a gravitational field, whatever their composition. In field-theory language: the coupling of the gravitational field to matter must be **universal** — the same coupling constant for electrons, photons, kinetic energy, binding energy, everything. The current $J$ must therefore be built out of a quantity that *every* form of matter carries in proportion to how much it gravitates. It could be the mass density $\rho$, but we know that within GR energy and pressure also gravitate, so the object we are looking for should also account for this. 
Furthermore, $J$ should be an object that can combine with the graviton to make a scalar, and hence it should itself be an object that transforms correctly (scalar, vector, tensor, etc.).
There is exactly one such object in relativistic physics: the **stress-energy tensor** $$T_{\mu\nu}$$.

Now, we know that the interaction term $$\mathcal{L}_{\text{int}}$$ must be a scalar (invariant under coordinate transformations) in order to be a proper Lagrangian, and thus the gravitational field must couple to $T$ in order to make a scalar. That is: $T_{\mu\nu}$ has two free indices that must be properly contracted with something in order to make a scalar. 
That something can be the gravitational field itself if it happens to be a vector $A_\mu$ or a tensor $h_{\mu\nu}$.

First of all, a scalar can be built directly from $T$, its trace:

$$\mathcal{T} \equiv g^{\mu\nu}T_{\mu\nu} = T^\mu_{\ \mu}$$

For a perfect fluid, we saw that $T_{\mu\nu}=(\rho+p)u_\mu u_\nu + p\, g_{\mu\nu}$ with $u^\mu u_\mu = -1$, and thus

$$\mathcal{T} = -\rho+3p.$$

### The target: a Newtonian potential

Ok now, our challenge is to reproduce at least the Newtonian potential energy of two masses at distance $r$

$$\boxed{V_{\text{int}}(r) = -\frac{G m_1 m_2}{r}}$$

— note the **minus sign**: gravity is *attractive*, so the potential energy is negative and decreases as the masses approach. This should be done starting from a coupling $$\mathcal{L}_{\rm int} = \kappa \langle J\phi\rangle$$ in which $J$ is a current built from the stress energy tensor of matter $$T_{\mu\nu}$$.

### Coupling term for a scalar graviton 

If the gravitational field is a scalar field $\phi$, we could think simply of 

$$\boxed{\mathcal{L}_{\text{int}}= \kappa \mathcal{T}\phi.}$$ 

Other reasonable terms might come to mind, as $\kappa \phi T_{\mu\nu}T^{\mu\nu}$ or $\kappa T_{\mu\nu} \partial^\mu \phi \partial^\nu\phi$. Each of these terms is interesting to look at in detail, but none of them ends up being a good candidate to describe gravity. 

- **The coupling to matter must be linear in $T_{\mu\nu}$.** The stress-energy tensor is additive: if two matter types coexist at a space-time point, the total source is $$T_{\mu\nu}=T^{(1)}_{\mu\nu}+ T^{(2)}_{\mu\nu}$$ (energy and momentum simply add up). A linear coupling $\kappa\phi\mathcal{T}$ respects this: the gravitational pull of a mixture is the sum of the pulls of its components, and each species couples to $\phi$ the same way whether it is alone or not. A quadratic term such as $\kappa \phi T_{\mu\nu}T^{\mu\nu}$ does not: it expands into $$\phi\, T^{(1)}_{\mu\nu}T^{(1)\mu\nu } + \phi\, T^{(2)}_{\mu\nu}T^{(2)\mu\nu} + 2\phi\, T^{(1)}_{\mu\nu}T^{(2)\mu\nu}$$ The **cross term** is the problem: how strongly matter type 1 gravitates now depends on what other matter happens to sit at the same point. Gravitational "charge" is no longer additive — two bodies brought together would not weigh the sum of their weights — and the strength of the coupling becomes composition-dependent, violating the universality demanded by the WEP.
- **The coupling to matter must be also be linear in the gravitational field.** A term like $\kappa T_{\mu\nu} \partial^\mu \phi \partial^\nu\phi$ is called a **disformal coupling**. This would generate a gravitational interaction that depends on the direction in which the scalar field evolves. While such a term is interesting to study extensions of General relativity, it is possible to show that this term alone can not reproduce the desired attraction law, and are instead corrections to the kinetic term of the scalar field due to the presence of matter, modifying its propagation. Some other terms as $\kappa\phi^2\mathcal{T}$ would lead to similar issues and the problem is easier to understand. If we go a bit ahead of ourselves, such terms when inserted in the Euler Lagrange equation would lead to an equation of motion like $\partial_\mu\partial^\mu \phi = - 2\kappa \mathcal{T}\phi$. We can see that $\phi=0$ is a possible solution of this equation. Hence it is possible to have a case where matter is present ($\mathcal{T}\neq0$) and the field is not ($\phi=0$). This is bad, as such a coupling does not make matter a **source** of the field and we would like that whenever matter is present, it generates a gravitational field.

Similar arguments can be pursued for any other kind of interactions one can propose, leading us to reject them as candidate for a scalar theory of gravitation. As a general rule, a coupling term allowing to reproduce an inverse square law force must be linear in both the gravitational field and the source (matter energy tensor).

### Coupling term for a vector graviton 

If the graviton is a vector field $A_\mu$, we need to build a *vector* out of the matter content for it to couple to. The model here is electromagnetism, where the coupling is $$\mathcal{L}_{\rm int} = -j^\mu A_\mu$$, with $j^\mu = \rho_e u^\mu$ the electric four-current (charge density in motion). For gravity, the role of the "charge" is played by energy-momentum, and the natural rank-1 object built from the stress-energy tensor is the four-momentum density:

$$P^\mu = T^{0\mu} = (\rho, \vec{\pi})$$

suggesting the coupling 

$$\boxed{\mathcal{L}_{\text{int}}=\kappa A_\mu P^\mu}$$

A warning signs appear already at this stage. The fixed index $0$ refers to the time direction of one particular observer, so a coupling built from it is not Lorentz invariant: the strength of gravity would depend on the observer's frame, in conflict with the equivalence principle. Second, as we will see below, even setting this aside, a vector mediator produces a force of the *wrong sign* between like charges. Both problems are fatal; we nevertheless record the candidate coupling for the systematic comparison to come.

Other non-linear coupling terms such as $T_{\mu\nu}A^\mu A^\nu$ or $\mathcal{T}A_\mu A^\mu$ might come to your mind. However, such terms can not be understood as propoer coupling between $A$ and $T$ generating gravity. Instead, they are understood as "mass terms" (see the definition of mass above) for the vector field $A$. As such, they would induce a mass to the vector field in the presence of matter, modifying its propagation. Again, just like the $\kappa T_{\mu\nu}\partial^\mu \phi \partial^\nu\phi$ such term are perfectly legitimate and interesting extensions for modified theories of gravity, but they do not allow to reproduce the inverse square law force of gravity.

### Coupling term for a tensor graviton 

If the graviton is a symmetric rank-2 tensor $h_{\mu\nu}$, no manipulation of the source is needed at all: the two free indices of the field contract exactly with the two free indices of the stress-energy tensor,

$$\boxed{\mathcal{L}_{\text{int}}=\kappa\, h^{\mu\nu}T_{\mu\nu}}$$

This is the only candidate in which the *entire* stress-energy tensor — energy density, momentum flux, pressure, shear stresses, everything we expect to gravitate — sources the field, linearly, locally and covariantly. Universality comes for free: every matter field, whatever its nature, possesses a stress-energy tensor, so every form of matter couples to $h_{\mu\nu}$ with the same strength $\kappa$, exactly as the WEP demands.

We now go through the full field theory for each of the proposed couplings. We will see that only spin 2 survives, and that it provides a field theory for gravity equivalent to GR. This is precisely what is meant when one says that "the graviton is a spin-2 field".

## What should be the spin of the graviton?

### Why must gravity be mediated by an integer-spin field?

Before comparing spins, let us discuss the half-integer ones. Recall from the supplement above that a field of spin $s$ returns to itself after a rotation by $2\pi/s$. Take this at face value for $s=\tfrac12$: the field returns to itself only after a rotation by $4\pi$ — after an ordinary full turn of $2\pi$, it comes back as *minus* itself. Such objects are perfectly consistent mathematically: they are called **spinors**, and they are the fields describing electrons and neutrinos. While deeply counter-intuitive, they are actually extremely deep: the are the most basic building blocks for fields in space-time, such that any field can be build from them.

The gravitational field should be a *directly measurable* classical field: an accelerometer reads it off at every point, like a voltmeter reads the electric field. Now rotate your measurement apparatus by $360°$: this is no operation at all, so every needle must return to its original reading. Any directly measurable classical field must therefore be **unchanged** under a $2\pi$ rotation. A spinor field flips sign, so it can never itself be a classical observable — only quantities *quadratic* in it (bilinears such as $\bar\psi\psi$, which pick up $(-1)^2=1$) are single-valued. This is why you have never seen a "classical electron field" the way you see a classical electric field. A field that mediates a macroscopic force must be observable through that force; a spinor cannot be. Hence, a field carrying a classical force should be an **integer spin**.

Suppose we tried nonetheless. To make matter source a spinor field $\psi_\alpha$ linearly, we would need an interaction $$\mathcal{L}_{\rm int}=\kappa\langle J\psi\rangle$$ where the matter current $J$ is itself a spinor, to contract the spinor index. But every current that macroscopic matter provides — energy density, momentum, stress, all packaged in $T_{\mu\nu}$ — is a *tensor*, single-valued under rotations: there is simply no classical spinor current to write down.[^susy] The only scalar couplings available are then quadratic in $\psi$, of the form $\mathcal{T}\,\bar\psi\psi$ — and we know from our previous discussions that a coupling quadratic in the mediator cannot source it: $\psi=0$ remains an exact solution in the presence of matter, and no classical force is generated at all. Further arguments can be brought in the context of quantum mechanics, as the fact that in order to preserve angular momentum, the exchange of fermions must be done by *pairs* which would indeed generate a residual force, but it falls as $1/r^5$ for massless fermions, far too weak and too short-ranged to be gravity. For a deeper discussion of this point using quantum field theoretic arguments see the great Feynman's lecture on gravitation. From all the above arguments, we thus conclude that the mediator has spin $s\in\{0,1,2,3,\dots\}$.


[^susy]: There is one loophole, and nature may even use it: *supersymmetric* theories possess a conserved spinor current, the supercurrent, and the associated spin-$\tfrac32$ gauge field is the **gravitino** of supergravity. But consistently with our argument, the gravitino does not mediate a classical long-range force; it is the partner of the graviton, not a substitute for it.

### Can gravity be mediated by a spin-0 field? Nordström's theory

This is the historically first relativistic theory of gravity, **Nordström's theory** (1912-1913) — a genuine competitor to GR at the time, and the only other theory known to satisfy the *strong* equivalence principle (for its geometrized version below, see also [Deruelle 2011](https://arxiv.org/abs/1104.4608)). It would be described by the field theory with the scalar coupling to the trace $\mathcal{T}$ that we identified above:

$$\boxed{\mathcal{L} = -\frac{1}{2}\partial_\mu \phi\,\partial^\mu \phi + \kappa\,\phi\, \mathcal{T} + \mathcal{L}_m}$$

which leads to the equation of motion:

$$\partial_\mu \partial^\mu\phi = -\kappa\, \mathcal{T}$$

the solution for static masses being:

$$V_{\text{int}}(r)= -\frac{\kappa^2}{4\pi} \frac{m_1m_2}{r}$$

Identifying with Newton's law leads us to define:

$$G \equiv \frac{\kappa^2}{4\pi}$$

such that $\kappa$ can be understood as the gravitational charge, and $G$ plays a role analogous to a fine-structure constant of gravity. That's fantastic: we managed to reproduce Newtonian gravity from a simple (relativistic) field theory. This is actually even better than Newtonian theory of gravity, as this theory reproduces special relativity when gravity is turned off and thus is a fully legitimate theory of gravity according to the criteria we gave in [our first class](./foundations-GR.md). And even better: it is much simpler than GR!

<details markdown="1">
  <summary><strong>Proof of the above equations</strong></summary>

Consider

$$ \mathcal{L} = -\frac{1}{2}\partial_\mu \phi\partial^\mu \phi  + \kappa\phi\, \mathcal{T} + \mathcal{L}_m$$

The Euler-Lagrange equations of motion associated to the extremization of the action for a variation of $\phi$ are ($\mathcal{L}_m$ does not depend on $\phi$):

$$\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\right) = \frac{\partial \mathcal{L}}{\partial \phi} $$

The left-hand side gives $-\Box\phi$, exactly as computed in the proof above (and in our [class on scalar fields in cosmology](../cosmo/scalar_fields.md)). The right-hand side is $\kappa \mathcal{T}$, since $\mathcal{T}$ is built from the matter fields and does not depend on $\phi$. Hence

$$-\Box\phi = \kappa T \qquad\Longleftrightarrow\qquad \Box\phi = -\kappa \mathcal{T}.$$

For a static configuration $\partial_t\phi = 0$, so $\Box\to\nabla^2$. For non-relativistic dust ($p\ll\rho$) the trace is $\mathcal{T}=-\rho$, hence

$$\nabla^2\phi = \kappa\rho$$

which is exactly Poisson's equation under the identification $G= \kappa^2/(4\pi)$. We can thus identify $\phi$ with the gravitational potential $\Phi$ of the Newtonian limit of GR defined in the [first lecture](./foundations-GR.md). Hence, the scalar field really **is** the gravitational potential.
We can solve this equation exactly as for the Newtonian limit of GR, the solution for a point mass $m_1$ at the origin is

$$\phi(r) = -\frac{\kappa m_1}{4\pi r}$$

The interaction energy of a second static mass $m_2$ is $-\int \mathcal{L}_{\rm int}\text{d}^3x = -\kappa\phi\int \mathcal{T}\,\text{d}^3x = +\kappa\, \phi\, m_2$, giving

$$V_{\text{int}}(r) = -\frac{\kappa^2}{4\pi}\frac{m_1m_2}{r}$$

Note that since $$G=\kappa^2/(4\pi)$$, in order for $\phi$ to be directly identified with Newtonian potential, one would have to consider the redefinition $$\Phi= \kappa\phi$$ with Lagrangian $$-\frac{1}{2\kappa^2}\partial_\mu \Phi\partial^\mu  \Phi + \Phi \mathcal{T}$$ or equivalently:

$$\boxed{-\frac{1}{8\pi G}\partial_\mu \Phi\partial^\mu  \Phi + \Phi \mathcal{T}}$$

</details>

So far, so good: **a massless scalar reproduces Newtonian gravity exactly**. This is not an accident of gravity. The same structure — massless mediator, static source, Poisson equation — is what produces *every* long-range $1/r^2$ force in nature.

#### Nordström's theory with a potential

To build a fully general field theory, a potential $V$ could be added to the scalar field. 

$$\boxed{\mathcal{L} = -\frac{1}{2}\partial_\mu \phi\,\partial^\mu \phi - V(\phi) + \kappa\,\phi\, \mathcal{T} + \mathcal{L}_m}$$

We see quickly that such additional term would lead to a modification to Newton's square law and would thus become more a modified gravity theory candidate than a reproduction of Einstein's theory. In particular, one could consider adding a mass to the graviton $V(\phi)= m_\phi^2 \phi^2/2$, leading to the equation of motion:

$$(\partial_\mu \partial^\mu\phi - m^2_\phi\phi) = -\kappa\, \mathcal{T}$$

Doing so leads to the potential

$$V_{\text{int}}(r) =  -\frac{\kappa^2}{4\pi}\frac{m_1m_2}{r}e^{-m_\phi r}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

In the static limit for a point source, the equation of motion is:

$$(\nabla^2-m^2_\phi)\phi(r) = \kappa m\delta(r)$$

This equation is again not trivial to solve and would require the use of Green functions. We will again assume here that the solution of $$(\nabla^2-a^2) f = \kappa m_1\delta(r)$$ is $$f = -e^{-ar}/(4\pi r)$$, which is a standard result of Green function theory. You can easily verify its validity by differentiating $f$.

Hence, we get the solution

$$\phi =  -\frac{\kappa}{4\pi}\frac{m_1}{r}e^{-m_\phi r}$$

From which we get the Yukawa potential for $V_{\rm int}(r)$ given above.

</details>

known as the **Yukawa potential**, which reduces to the $1/r$ potential in the limit $m_\phi \to 0$. The effect of the field is exponentially damped by the mass. This explains for example, why the weak force is so short ranged, as the $W$ and $Z$ bosons are massive. As gravity is long-ranged, we really don't want such kind of suppression. As a general rule here for our attempt to rewrite GR as a field theory, we will thus ask for the graviton to be massless in all scenarios. However, we will see that looking for the possible effect of a massive but light graviton is an active topic in modified gravity, through the theories of [massive gravity](./massive-gravity.md).

#### Why Nordström's theory fails

Now, you can take a moment and wonder why Nordström's theory fails over General relativity, while it appear to be so simple and elegant.  We can find three independent problems, in increasing order of severity:

1. **No light bending.** For the electromagnetic field (or any relativistic, conformally invariant matter), $\rho = 3p$, so the trace vanishes: $\mathcal{T} = -\rho + 3p = 0$. Light therefore does not source the scalar field, *and does not respond to it*. Nordström's theory predicts **exactly zero** deflection of light by the Sun. Eddington's 1919 expedition, and every measurement since, sees a non-zero deflection consistent with GR to $\sim 10^{-4}$ ([Will 2014, *Living Rev. Rel.*](https://link.springer.com/article/10.12942/lrr-2014-4)). In the PPN language, Nordström's theory has $\gamma=-1$, while $\gamma=1$ in GR and $\vert\gamma - 1\vert < 2.3\times 10^{-5}$ from the Cassini experiment.

2. **The perihelion precession has the wrong sign.** Nordström's theory has PPN parameters $\gamma=-1$, $\beta=1/2$. The perihelion advance per orbit is $\Delta\varpi = \frac{6\pi GM}{a(1-e^2)}\cdot\frac{2+2\gamma-\beta}{3}$, so the theory predicts $-1/6$ of the Einstein value: about $-7''$ per century for Mercury, i.e. a *regression*, whereas the observed anomaly is $+43''$ per century.

3. **It cannot accommodate cosmology.** Since $\mathcal{T}=0$ for radiation, the early radiation-dominated Universe would not gravitate at all (hence not enter in the Friedmann equation, more on this in the [previous lecture](./cosmology.md) dedicated on cosmology).

4. **It would not produce the proper gravitational waves**. But we will not enter into these details here as the three points above are already enough!

Trying to patch these points by adding some additional terms, as a coupling of the field to electromagnetism (like $\kappa\phi F_{\mu\nu}F^{\mu\nu}$) would make things worse. Actually, such a coupling would lead to a variation of the fine structure constant $\alpha$, and directly violate the EEP. For more on this point, see the the expandable box below and our lecture on the [fundamental constants](./varying_const.md). Furthermore it would not fix the perihelion prediction (nothing would), such that there really is no hope for Nordström theory.

#### Nordström (second) theory is a geometric theory!

However, Nordström's theory is *not* a counterexample to the geometrical reading of gravity. Indeed, you can easily convince yourself that this theory encompasses the EEP, and as discussed in our [first lecture](./foundations-GR.md), it must thus allow for a geometric reading. In Einstein & Fokker (1914) showed that (a slightly generalised version of) Nordström theory can be rewritten *exactly* as a geometric theory with the following metric

$$g_{\mu\nu} = (1+\kappa\phi)^2\,\eta_{\mu\nu}$$

We talk about a **conformally flat** metric, as it can be rescaled everywhere by a function (here $(1+\kappa\phi)^2$) to give back $\eta$. Then free particles follow geodesics of $g$, and the field equation becomes the manifestly covariant statement

$$\boxed{R = 24\pi G\,\mathcal{T}_{(g)}}$$

where $R$ is the Ricci scalar and $$\mathcal{T}_{(g)}$$ is the trace of the stress energy tensor of matter expressed in the metric $g$ (see box below). So the *first* relativistic theory of gravity was already a "flat-space field theory" and a "curved-space geometric theory" simultaneously. **The dichotomy in the title of this lecture was already false in 1914.** And notice why light is not deflected: it is possible to show that null geodesics remain the same under a conformal transformation of the metric $$g_{\mu\nu}\to (1+\kappa\phi)^2\eta_{\mu\nu}$$, so a conformally flat metric bends no light (discussed in the second box below). 

<details markdown="1">
  <summary><strong> The geometrical (Einstein-Fokker) rewriting of Nordström theory</strong></summary>

We introduce the short-hand notation $\varphi = 1+ \kappa\phi$. From our remark in a previous derivation, recall that we can identify $\kappa\Phi$ with the Newtonian potential in standard Nordström theory. Consider the metric $g_{\mu\nu}=\varphi^2\eta_{\mu\nu}$, hence $g^{\mu\nu}=\varphi^{-2}\eta^{\mu\nu}$. Compute the Christoffel symbols:

$$
\begin{align}
\Gamma^\lambda{}_{\mu\nu}&= \tfrac{1}{2}g^{\lambda\sigma}\left(\partial_\mu g_{\sigma \nu} + \partial_\nu g_{\sigma \mu} - \partial_\sigma g_{\mu\nu}\right) \\
&= \tfrac{1}{2}\varphi^{-2}\eta^{\lambda\sigma}\left(\partial_\mu(\varphi^2)\, \eta_{\sigma\nu} + \partial_\nu(\varphi^2)\,\eta_{\sigma\mu} - \partial_\sigma(\varphi^2)\, \eta_{\mu\nu}\right)\\
&= \tfrac{1}{2}\varphi^{-2}\eta^{\lambda\sigma}\left(2\varphi\,\partial_\mu\varphi\, \eta_{\sigma\nu} + 2\varphi\,\partial_\nu\varphi\,\eta_{\sigma\mu} - 2\varphi\,\partial_\sigma\varphi\, \eta_{\mu\nu}\right)\\
&= \frac{1}{\varphi}\left(\eta^{\lambda\sigma}\eta_{\sigma\nu}\partial_\mu\varphi + \eta^{\lambda\sigma}\eta_{\sigma\mu}\partial_\nu\varphi - \eta^{\lambda\sigma}\eta_{\mu\nu}\partial_\sigma \varphi \right)\\
&= \frac{1}{\varphi}\left(\delta^{\lambda}_\nu\partial_\mu\varphi + \delta^\lambda_\mu \partial_\nu\varphi - \eta_{\mu\nu}\partial^\lambda \varphi\right)
\end{align}
$$

We now introduce the shortcut notation:

$$
A_\mu \equiv \partial_\mu\ln\varphi = \frac{\partial_\mu\varphi}{\varphi},
\qquad A^\lambda\equiv\eta^{\lambda\sigma}A_\sigma,
\qquad A^2\equiv \eta^{\mu\nu}A_\mu A_\nu ,
$$

so that

$$\Gamma^\lambda{}_{\mu\nu} = \delta^\lambda_\nu A_\mu + \delta^\lambda_\mu A_\nu - \eta_{\mu\nu}A^\lambda .$$

Note $A_\mu$ is a **gradient**, hence $\partial_\mu A_\nu=\partial_\nu A_\mu$. This is used repeatedly.

We now compute the Riemann tensor. Start with the two derivatives:

$$
\begin{align}
\partial_\nu\Gamma^\lambda{}_{\mu\rho}-\partial_\rho\Gamma^\lambda{}_{\mu\nu}
&= \left(\delta^\lambda_\rho\partial_\nu A_\mu + \delta^\lambda_\mu\partial_\nu A_\rho - \eta_{\mu\rho}\partial_\nu A^\lambda\right)
 - \left(\delta^\lambda_\nu\partial_\rho A_\mu + \delta^\lambda_\mu\partial_\rho A_\nu - \eta_{\mu\nu}\partial_\rho A^\lambda\right)\\[4pt]
&= \delta^\lambda_\rho\,\partial_\nu A_\mu - \delta^\lambda_\nu\,\partial_\rho A_\mu
 \;+\;\underbrace{\delta^\lambda_\mu\left(\partial_\nu A_\rho-\partial_\rho A_\nu\right)}_{=\,0\ \text{($A$ is a gradient)}}
 \;-\;\eta_{\mu\rho}\,\partial_\nu A^\lambda + \eta_{\mu\nu}\,\partial_\rho A^\lambda
\end{align}
$$

Expanding the nine products and contracting on $\sigma$:

$$
\Gamma^\lambda{}_{\nu\sigma}\Gamma^\sigma{}_{\mu\rho}
= \delta^\lambda_\rho A_\mu A_\nu + \delta^\lambda_\mu A_\nu A_\rho + 2\delta^\lambda_\nu A_\mu A_\rho
- \delta^\lambda_\nu\eta_{\mu\rho}A^2 - \eta_{\nu\rho}A^\lambda A_\mu - \eta_{\mu\nu}A^\lambda A_\rho
$$

(two terms, $-\eta_{\mu\rho}A_\nu A^\lambda$ and $+\eta_{\mu\rho}A^\lambda A_\nu$, cancelled). Antisymmetrising in $\nu\leftrightarrow\rho$, the $\delta^\lambda_\mu$ and $\eta_{\nu\rho}$ pieces drop out and

$$
\Gamma^\lambda{}_{\nu\sigma}\Gamma^\sigma{}_{\mu\rho}-\Gamma^\lambda{}_{\rho\sigma}\Gamma^\sigma{}_{\mu\nu}
= -\delta^\lambda_\rho A_\mu A_\nu + \delta^\lambda_\nu A_\mu A_\rho
+ \delta^\lambda_\rho\eta_{\mu\nu}A^2 - \delta^\lambda_\nu\eta_{\mu\rho}A^2
+ \eta_{\mu\rho}A^\lambda A_\nu - \eta_{\mu\nu}A^\lambda A_\rho
$$

Define the symmetric tensor

$$
K_{\mu\nu}\;\equiv\;\partial_\mu A_\nu - A_\mu A_\nu \;=\; -\,\varphi\,\partial_\mu\partial_\nu\!\left(\frac{1}{\varphi}\right),
\qquad K\equiv\eta^{\mu\nu}K_{\mu\nu}
$$

Adding Steps 1 and 2, every term organises into $K$:

$$
\boxed{\;R^\lambda{}_{\mu\nu\rho}
= \delta^\lambda_\rho\left(K_{\nu\mu}+\eta_{\mu\nu}A^2\right)
- \delta^\lambda_\nu\left(K_{\rho\mu}+\eta_{\mu\rho}A^2\right)
- \eta_{\mu\rho}\,K_\nu{}^{\lambda} + \eta_{\mu\nu}\,K_\rho{}^{\lambda}\;}
$$

Now for the Ricci tensor. Contract $\lambda=\nu$ and sum, using $\delta^\lambda_\lambda=4$:

$$
\begin{align}
R_{\mu\rho}=R^\lambda{}_{\mu\lambda\rho}
&= \underbrace{K_{\rho\mu}+\eta_{\mu\rho}A^2}_{\delta^\lambda_\rho\ \text{term}}
\;-\;\underbrace{4\left(K_{\rho\mu}+\eta_{\mu\rho}A^2\right)}_{\delta^\lambda_\lambda\ \text{term}}
\;-\;\underbrace{\eta_{\mu\rho}K}_{K_\lambda{}^\lambda}
\;+\;\underbrace{K_{\rho\mu}}_{\eta_{\mu\lambda}K_\rho{}^\lambda}\\[4pt]
&= -2 K_{\mu\rho}\;-\;\eta_{\mu\rho}K -3\,\eta_{\mu\rho}A^2
\end{align}
$$

And thus:

$$\boxed{\;R_{\mu\nu} = -2K_{\mu\nu} - \eta_{\mu\nu}\left(K+3A^2\right)\;}$$


Finally, the Ricci scalar: Trace with $g^{\mu\nu}=\varphi^{-2}\eta^{\mu\nu}$ (note $\eta^{\mu\nu}\eta_{\mu\nu}=4$):

$$
R = \varphi^{-2}\,\eta^{\mu\nu}R_{\mu\nu}
= \varphi^{-2}\Big[-2K - 4K -12 A^2\Big]
= \varphi^{-2}\Big[-6K -12 A^2\Big]
$$

Now return to $\varphi$. Since $A_\mu=\partial_\mu\varphi/\varphi$,

$$
A^2=\frac{(\partial\varphi)^2}{\varphi^2},
\qquad
K=\eta^{\mu\nu}\!\left(\partial_\mu A_\nu-A_\mu A_\nu\right)=\frac{\Box_\eta\varphi}{\varphi}-\frac{2(\partial\varphi)^2}{\varphi^{2}}
$$

Substituting and collecting the two independent structures:

$$
\boxed{\;R=\,-\frac{6\,\Box_\eta\varphi}{\varphi^{3}}}
$$

Now we face a subtlety in order to confront this geometry with the scalar field theory we started from. First, express the Nordström Lagrangian in terms of $\varphi$ by substituting $\phi = (\varphi-1)/\kappa$:

$$\mathcal{L} = -\frac{1}{2\kappa^{2}}\,\partial_\mu \varphi\,\partial^\mu \varphi
\;+\; (\varphi-1)\,\mathcal{T} \;+\; \mathcal{L}_m$$

Note that the coupling constant has simply migrated from the vertex into the kinetic term — this is a change of variable, nothing more. You can check that the equation of motion is unchanged (the constant shift drops out of $\partial_\mu\varphi$):

$$\Box_\eta\varphi = -\kappa^{2}\,\mathcal{T} = -4\pi G\,\mathcal{T}$$

Second — and this is the key step — recognise what the coupling $(\varphi-1)\mathcal{T}$
actually *is*. For a point particle of mass $m$ following a worldline $z^\mu(s_\eta)$, the
flat-space stress tensor is

$$T^{\mu\nu}(x) = m\!\int\! ds_\eta\;\frac{dz^\mu}{ds_\eta}\frac{dz^\nu}{ds_\eta}\;\delta^4(x-z)$$

Its trace follows from the normalisation of the four-velocity,
$\eta_{\mu\nu}\,\frac{dz^\mu}{ds_\eta}\frac{dz^\nu}{ds_\eta} = -1$:

$$\mathcal{T} \;\equiv\; \eta_{\mu\nu}T^{\mu\nu} \;=\; -\,m\!\int\! ds_\eta\;\delta^4(x-z)$$

The free and interaction terms of the matter Lagrangian then combine into

$$-m\!\int\! ds_\eta \;-\; m\!\int\!(\varphi-1)\,ds_\eta \;=\; -m\!\int\!\varphi\,ds_\eta
\;=\; -m\!\int\! ds_g$$

which is just the *free* matter action written with the metric
$g_{\mu\nu}=\varphi^{2}\eta_{\mu\nu}$, since $ds_g = \varphi\,ds_\eta$. The whole matter
sector is therefore $S_m[g]$, and the theory can be written with **no explicit coupling to the stress-energy tensor at all**:

$$\boxed{\;\mathcal{L} = -\frac{1}{2\kappa^{2}}\,\partial_\mu \varphi\,\partial^\mu \varphi
\;+\; \mathcal{L}_m\!\left[\varphi^{2}\eta\right]\;}$$

All the $\varphi$-dependence now hides inside $g_{\mu\nu}$. This formulation of the field Lagrangian can be called the **second Nordström theory**. This is what lets us bring in
the stress-energy tensor of matter *in the curved geometry defined by $\varphi$*,

$$T^{(g)}_{\mu\nu} = -\frac{2}{\sqrt{-g}}\,\frac{\delta S_m}{\delta g^{\mu\nu}}\ ,
\qquad \mathcal{T}_{(g)} \equiv g^{\mu\nu}T^{(g)}_{\mu\nu}$$

Varying with respect to $\varphi$ by the chain rule, and using
$\partial g^{\mu\nu}/\partial\varphi = -2\varphi^{-3}\eta^{\mu\nu} = -\tfrac{2}{\varphi}g^{\mu\nu}$
together with $\sqrt{-g}=\varphi^4$:

$$\frac{\delta S_m}{\delta\varphi}
= \left(-\frac{\sqrt{-g}}{2}T^{(g)}_{\mu\nu}\right)\!\left(-\frac{2}{\varphi}g^{\mu\nu}\right)
= \frac{\sqrt{-g}}{\varphi}\,\mathcal{T}_{(g)} = \varphi^{3}\,\mathcal{T}_{(g)}$$

so that the equation of motion reads

$$\Box_\eta\varphi = -\kappa^2\varphi^{3}\,\mathcal{T}_{(g)} = -4\pi G\,\varphi^{3}\,\mathcal{T}_{(g)}$$

**Why is this the same equation as $\Box_\eta\varphi = -4\pi G\,\mathcal{T}$?** Because
$\mathcal{T}$ and $$\mathcal{T}_{(g)}$$ are not the same object: they are the trace of the
same physical matter, but measured against different volumes. Compute
$$\mathcal{T}_{(g)}$$ for the point particle above, using $d\tau = ds_g = \varphi\,ds_\eta$
for the proper time in $g$, and $\sqrt{-g}=\varphi^{4}$:

$$\mathcal{T}_{(g)} = -\frac{m}{\sqrt{-g}}\!\int\! d\tau\;\delta^4(x-z)
= -\frac{m\,\varphi}{\varphi^{4}}\!\int\! ds_\eta\;\delta^4(x-z)
= \frac{1}{\varphi^{3}}\;\mathcal{T}$$

Hence $$\mathcal{T}=\varphi^{3}\mathcal{T}_{(g)}$$, and the two field equations are literally
identical. The factor $\varphi^{3}$ records that $\mathcal{T}$ counts mass per unit
**coordinate** volume while $$\mathcal{T}_{(g)}$$ counts it per unit **proper** volume, the
two being related by the 3-volume Jacobian $\sqrt{\det g_{ij}} = \varphi^{3}$.

<!-- As a word of caution: the relation between flat and curved stress energy tensor ($$\mathcal{T}=\varphi^{3}\mathcal{T}_{(g)}$$) is true only for the motion of massive particles. For more general fluid, this is not true and the $\kappa \mathcal{T}$ theory can be understood as a first order linearisation of the more complete and non-linear second Nordström theory. -->

Finally, insert the curvature identity obtained above:

$$R = -\frac{6\,\Box_\eta\varphi}{\varphi^{3}}
= -\frac{6}{\varphi^{3}}\left(-4\pi G\,\varphi^{3}\,\mathcal{T}_{(g)}\right)$$

$$\boxed{\;R = 24\pi G\,\mathcal{T}_{(g)}\;}$$

The $\varphi^{-3}$ carried by the curvature and the $\varphi^{+3}$ carried by the source
cancel **exactly**, leaving an equation in which no trace of the background $\eta_{\mu\nu}$
survives. That cancellation *is* the geometrisation: it is what allows a theory built on
flat spacetime to be restated as a statement about curvature alone.

</details>


<details markdown="1">
  <summary><strong> Why Nordström theory does not affect light from a geometric point of view</strong></summary>

We saw above that Nordström theory could not affect light as it couples to $\mathcal{T}=0$ for radiation. We  also saw in the previous box that Nordström theory has a geometric interpretation. Let us understand why it does not affect light either as a geometric theory. 

The Maxwell Lagrangian in flat space-time is:

$$-\frac{1}{4}F^{\mu\nu}F_{\mu\nu} =  -\frac{1}{4}\eta^{\rho\mu}\eta^{\sigma \nu}F_{\rho\sigma}F^{\mu\nu}$$

Reframing it in a conformally curved space-time with $$g=\varphi^2\eta$$, we have:

$$\begin{align}
&-\frac{1}{4}\sqrt{-\vert g\vert}g^{\rho\mu}g^{\sigma \nu}F_{\rho\sigma}F^{\mu\nu}\\
&=-\frac{1}{4}\sqrt{-\vert \varphi^2\eta\vert}\varphi^{-4}\eta^{\rho\mu}\eta^{\sigma \nu}F_{\rho\sigma}F^{\mu\nu}\\
&=-\frac{1}{4}\varphi^4\varphi^{-4}\eta^{\rho\mu}\eta^{\sigma \nu}F_{\rho\sigma}F^{\mu\nu}\\
&= -\frac{1}{4}\eta^{\rho\mu}\eta^{\sigma \nu}F_{\rho\sigma}F^{\mu\nu}
\end{align}
$$

Remembering that the determinant of a diagonal metric is the product of all its terms and $g_{\mu\nu}=\varphi^2\eta_{\mu\nu}= {\rm diag}(-\varphi^2,\varphi^2,\varphi^2,\varphi^2)$, such that $$\vert g \vert = -\varphi^8$$. Hence light is **blind** to conformal transformations (the same argument applies for any metric transformations $$g \to A^2g$$, which would for example be the case of varying $G$ theory as discussed in [our previous lecture](./varying_const.md)) and null geodesics will not be affected at all. This is a lucky coincidence that is **only true in four dimensions**.

</details>

<details markdown="1">
  <summary><strong> Bootstrap and SEP in Nordstrom theory</strong></summary>

We have been a bit sloppy in the previous geometric derivation in the way we justify the form of Nordström's second theory. Actually all of our reasoning works fine for a point particle but gets wrong when considering more general matter form.

The cleanest way to obtain Nordström second theory from the first linear one is to use a gravitational bootstrap very similar to the one we will use later for the spin-2 field.

The motivation is the following: the field $\phi$ must also gravitate if we want the SEP to be satisfied. So in the coupling $$\kappa \phi\mathcal{T} $$
in the Lagrangian, the trace should also contain the field's own stress energy tensor contribution $$\mathcal{T} = \mathcal{T}_m + \mathcal{T}_\phi$$.

We know the stress-energy tensor for the field is obtained, as for matter, by varying with respect to the metric and then setting it back to $\eta$:

$$T^\phi_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta \left(\sqrt{-g}\,\mathcal{L}_\phi\right)}{\delta g^{\mu\nu}}\Bigg\vert_{g=\eta} = -2\frac{\partial \mathcal{L}_\phi}{\partial \eta^{\mu\nu}} + \eta_{\mu\nu}\mathcal{L}_\phi
= \partial_\mu\phi\,\partial_\nu\phi - \frac{1}{2}\eta_{\mu\nu}\,\partial_\alpha\phi\,\partial^\alpha\phi$$

So its trace is, writing $(\partial\phi)^2\equiv \partial_\alpha\phi\,\partial^\alpha\phi$ and using $\eta^{\mu\nu}\eta_{\mu\nu}=4$:

$$\mathcal{T}_\phi = \eta^{\mu\nu}T^\phi_{\mu\nu} = (\partial\phi)^2 - 2(\partial\phi)^2 = -\,(\partial\phi)^2 .$$

But adding this to the Lagrangian further adds a term

$$\kappa\,\phi\,\mathcal{T}_\phi = -\,\kappa\,\phi\,(\partial\phi)^2$$

which has an impact on the stress energy tensor: this cubic term is itself a piece of the Lagrangian, so it carries energy, and its own trace must be fed back into the source as well. Applying the same recipe to it gives $\mathcal{T}\left[-\kappa\phi(\partial\phi)^2\right] = -2\kappa\phi(\partial\phi)^2$, so we must add $-2\kappa^2\phi^2(\partial\phi)^2$, whose trace is $-4\kappa^2\phi^2(\partial\phi)^2$, and so on.

We end up with the infinite loop:

$$\mathcal{L}_\phi = -\frac{1}{2}(\partial\phi)^2\Big[\,1 \;+\; 2\kappa\phi \;+\; 4\kappa^2\phi^2 \;+\; 8\kappa^3\phi^3 \;+\;\dots\Big]$$

and, worse, **the matter side loops too**: the interaction term $\kappa\phi\,\mathcal{T}_m$ is part of the matter Lagrangian, so it has its own stress-energy tensor, whose trace generates a term $\propto\kappa^2\phi^2$, which generates a term $\propto \kappa^3\phi^3$, and so on. The two loops feed each other, and there is no obvious reason for either of them to stop.

*The story is that accounting for these loops allows to give back exactly Nortdstrom second theory! (in prep)*

**Bootstrap here**

</details>

### Can gravity be mediated by a spin-1 field?

From the previous discussion, we saw convincingly that gravity cannot be mediated by a scalar field. How about a vector field?

The most general Lorentz-invariant kinetic term with two derivatives for a vector field is a combination of $\partial_\mu A_\nu\partial^\mu A^\nu$, $\partial_\mu A_\nu\partial^\nu A^\mu$ and $(\partial_\mu A^\mu)^2$. Requiring that none of the four components of $A_\mu$ carries negative kinetic energy (no **ghost** — we come back to this crucial notion below) forces a unique combination:

$$\mathcal{L}_{\rm kin}= -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}, \qquad F_{\mu\nu}=\partial_\mu A_\nu - \partial_\nu A_\mu$$

which is precisely the combination invariant under the gauge transformation $$A_\mu \to A_\mu + \partial_\mu\alpha$$. This is exactly the Lagrangian leading to Maxwell's equations without charges, with $A^\mu = (\Phi, \vec{A})$ the four-potential (beware the index position: with our signature, $A_0 = -\Phi$). Hence, a spin-1 theory of gravity would have a gravitational field evolving in vacuum exactly like the electromagnetic field. This does not sound bad at all: the Coulomb force between static charges falls as $1/r^2$, just like Newton's. To generate Coulomb's law, the electromagnetic coupling must be $$\mathcal{L}_{\rm int}= j^\mu A_\mu$$, with $$j^\mu = (\rho_e,\vec\jmath_e)$$ the charge-current density (note: $+j^\mu A_\mu$ in our signature $(-,+,+,+)$; the familiar $$-j^\mu A_\mu$$ belongs to $$(+,-,-,-)$$). However, this force is **repulsive** between identical charges, and we need the opposite for gravity.

Let us then propose the Lagrangian of a spin-1 gravity theory:

$$\mathcal{L}= -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + (-1)^\sigma \kappa\, P^\mu A_\mu$$

where $\sigma\in\{0,1\}$ lets us keep track of both possible signs of the coupling at once, and $P^\mu \equiv T^{0\mu} = (\rho, \vec\pi)$ is the local energy-momentum current density — the local version of the four-momentum $P^\mu$ proposed earlier (the suspicious fixed index $0$ will come back to bite us at the end of this section).

Let's now take the static limit and keep only $\Phi$ and $\rho$, which are the only time-independent terms. The field strength has only $F_{0i} = -\partial_i A_0 = \partial_i\Phi$, so $F_{\mu\nu}F^{\mu\nu} = 2F_{0i}F^{0i} = -2(\nabla\Phi)^2$ (the raised $0$ brings one $\eta^{00}=-1$), while the coupling gives $P^\mu A_\mu \to \rho A_0 = -\rho\Phi$. The Lagrangian reduces to

$$\mathcal{L} \;\to\; \frac12(\nabla\Phi)^2 - (-1)^\sigma \kappa\rho\,\Phi$$

We thus recover an effective scalar theory for the potential $\Phi$ — but note the crucial difference with the spin-0 case: the kinetic term now comes with a positive sign.

The Euler-Lagrange equation of this static Lagrangian is

$$\nabla^2\Phi = -(-1)^\sigma \kappa\rho \qquad\Longrightarrow\qquad \Phi(r) = (-1)^\sigma\frac{\kappa M_1}{4\pi r}$$

for a point mass $M_1$ at the origin. The interaction energy of a second mass, $V_{\rm int} = -\int\mathcal{L}_{\rm int}\,\text{d}^3x = (-1)^\sigma \kappa M_2\,\Phi(r)$, is then:

$$V_{\rm int}(r) = (-1)^{2\sigma}\frac{\kappa^2 M_1M_2}{4\pi r} = +\frac{\kappa^2 M_1M_2}{4\pi r}$$

The sign $\sigma$ of the coupling has dropped out completely: $(-1)^{2\sigma}=+1$ always. Whatever sign we choose, the potential energy is positive and grows as the masses approach: the force is **repulsive** between like charges — correct for electrostatics, fatal for gravity.

The $\sigma$ disappeared because the coupling enters the interaction energy *twice*: once when the source creates the field (the field equation), once when the probe feels it (in $V_{\rm int}$). Flipping the coupling flips both, and the two flips cancel. Indeed, flipping the coupling is nothing but the field redefinition $A_\mu \to -A_\mu$, which cannot change any observable. In general, $V_{\rm int}\propto (\text{coupling})^2\times(\text{sign fixed by the kinetic term})$. Opposite electric charges attract only because $q_1q_2<0$ is available; gravitational charge (energy) comes with a single sign, so that escape is closed.

Then why not flip the sign of the kinetic term instead? This is the right question, since the sign of $V_{\rm int}$ is inherited from there: taking $+\frac14 F^2$ would flip the static gradient term to $-\frac12(\nabla\Phi)^2$ — the scalar's sign — and like masses would attract. But the kinetic sign, unlike the coupling sign, is *not* a matter of convention: it fixes the sign of the field's **energy**. Flip it, and every propagating mode of the field carries negative energy — the energy density of a wave becomes $-\frac12(\vec E^2+\vec B^2)<0$. Such a field is called a **ghost**, and a ghost coupled to ordinary matter destroys the theory: energy conservation then *allows* the vacuum to decay into positive-energy matter plus negative-energy radiation at zero total cost, so empty space is unstable, and orbits are anti-damped by radiation (runaway solutions) instead of slowly decaying. And one cannot flip the sign "only for the static part": Lorentz invariance ties the static sector to the radiative one — the very same $\eta^{00}$ that fixes the sign of the $(\nabla\Phi)^2$ term also fixes the (positive) energy of the transverse waves. Within a Lorentz-invariant, stable theory, *attraction with healthy radiation is simply not on the menu for spin 1*. This is why "no ghosts" (unitarity) appears among the assumptions of the uniqueness theorems at the end of this lecture: the sign rule holds only — but always — for fields of positive energy.

Compare with the scalar case worked out above, and (as a preview) with the spin-2 case constructed later:

| | static Lagrangian | field equation | point-source solution | $V_{\rm int}(r)$ | verdict |
|---|---|---|---|---|---|
| spin 0 | $-\frac12(\nabla\phi)^2 - \kappa\rho\,\phi$ | $\nabla^2\phi = +\kappa\rho$ | $\phi = -\dfrac{\kappa M_1}{4\pi r}$ | $-\dfrac{\kappa^2M_1M_2}{4\pi r}$ | attracts |
| spin 1 | $+\frac12(\nabla\Phi)^2 - \kappa\rho\,\Phi$ | $\nabla^2\Phi = -\kappa\rho$ | $\Phi = +\dfrac{\kappa M_1}{4\pi r}$ | $+\dfrac{\kappa^2M_1M_2}{4\pi r}$ | repels |
| spin 2 *(preview)* | $-\frac12(\nabla h_{00})^2 + \dots + \frac{\kappa}{2}\rho\, h_{00}$ | $\nabla^2\bar h_{00} = -16\pi G\rho$ | $\bar h_{00} = +\dfrac{4GM_1}{r}$ | $-\dfrac{GM_1M_2}{r}$ | attracts |

(the spin-2 kinetic term is schematic — the full Fierz-Pauli structure comes later; the spin-2 row is derived in the "static limit of the spin-2 theory" box below.)

Follow the time indices. The scalar's static kinetic term is $-\frac12(\nabla\phi)^2$. The vector's surviving component $A_0$ carries one *lower time index*; building the Lorentz invariant requires raising it once, which brings exactly one factor of $\eta^{00}=-1$: hence $+\frac12(\nabla A_0)^2$, the opposite sign. That single relative sign then propagates mechanically down the row of the table: into the field equation (same source, opposite-sign response), into the solution, into $V_{\rm int}$. For a rank-2 field, the surviving component $h_{00}$ carries *two* time indices, hence *two* factors of $\eta^{00}$: $(-1)^2=+1$, and we are back to the scalar's sign — attraction. The pattern generalizes: a rank-$s$ field contracted with a static source contributes $(\eta^{00})^s = (-1)^s$, so **even spin attracts like charges, odd spin repels them**.

A caution to avoid a classic confusion: the negative sign in front of the scalar's gradient term does *not* mean the scalar field carries negative energy. The field energy density is positive in both healthy theories ($\frac12(\nabla\phi)^2$ and $\frac12 \vec E^{\,2}$ respectively) — a Lagrangian is not an energy, and the $\eta^{00}$ bookkeeping surfaces in the sign of the *force between sources*, not in the sign of the field's own energy. (The ghost discussion above is precisely about theories where this ceases to be true.)

Hence in the static, non-relativistic limit, spin-0, spin-1 and spin-2 massless theories *all* collapse onto the same Poisson equation, differing only by an overall sign and by which piece of the source appears (the trace $\mathcal{T}$ for spin 0, the energy density for spin 1, the full $T^{00}$ for spin 2). This is why "reproducing Newton" is a very weak test of a theory of gravity — and why the discriminating observations are all *relativistic* ones (light bending, perihelion precession, gravitational waves).

Finally, one can also see the obstruction from the source side, as anticipated: the current $P^\mu = T^{0\mu}$ carries a fixed index $0$ referring to one particular observer — it is not a Lorentz-covariant object — so the strength of gravity would depend on the observer's frame, in violation of the equivalence principle.

This is not to say vector gravity is useless: the *linearised* $g_{0\mu}$ sector of GR does behave like a Maxwell field (**gravitomagnetism**), producing frame-dragging, measured by Gravity Probe B and LAGEOS. But it is a *part* of a spin-2 theory, not a theory in itself.

### Can gravity be mediated by a spin $\geq 3$ field?

Ok, so spin zero and one failed, and our whole discussion so far really wants us to explore the spin-2 case! But before this, let us also see that gravity cannot be mediated by a field of spin greater or equal to three. The obstruction here is purely theoretical, and it rests on an entirely classical chain of reasoning. Before diving in, let us state the strategy in plain words. We will first show that a massless field of spin $s\geq 1$ cannot couple to just any source: consistency of its field equations demands that the source be a *conserved* current with $s$ indices. We will then translate this requirement on the current into a requirement on matter itself: matter must carry a certain conserved total quantity, a "charge". Next, we will ask what this charge can possibly look like when matter is made of particles, and find that the answer is essentially unique at each rank. Finally, we will test whether such a charge can survive the most ordinary physical process there is — a collision — and discover that the test is passed trivially at spin 1, passed at spin 2 at the price of a remarkable condition (which turns out to be the equivalence principle), and failed irrecoverably at spin 3 and beyond. This section is a bit more technical than the other ones, so feel free to skip it, keeping only in mind that gravity can not be mediated by a field with a spin greater than 2!

Let us begin with the first claim: a massless field demands a conserved source. We can see it concretely in the theory we know best, electromagnetism. Maxwell's equations read $\partial_\mu F^{\mu\nu} = -j^\nu$. Apply the divergence $\partial_\nu$ to both sides. On the left we obtain $\partial_\nu\partial_\mu F^{\mu\nu}$, which vanishes identically for *any* field configuration whatsoever. The reason is a purely algebraic clash of symmetries: the pair of derivatives $\partial_\nu\partial_\mu$ is symmetric under the exchange of $\mu$ and $\nu$ (derivatives commute), while $F^{\mu\nu}$ is antisymmetric under the same exchange; contracting a symmetric object with an antisymmetric one always gives zero. (To see it explicitly: $\partial_\nu\partial_\mu F^{\mu\nu} = -\partial_\nu\partial_\mu F^{\nu\mu}$ by antisymmetry, and relabelling the dummy indices $\mu\leftrightarrow\nu$ turns the right-hand side back into $-\partial_\nu\partial_\mu F^{\mu\nu}$; a quantity equal to minus itself vanishes.) This is even more profound than it seems: we will not enter into the details here but this is a geometric relationship similar to Bianchi identity (from the definition of the exterior derivative $\text{d}F=\text{d}^2A=0$).
The left-hand side being identically zero, the divergence of the right-hand side must vanish too: $\partial_\nu j^\nu = 0$. It is **not** a property we imposed, it is a property the field equations *force upon the source*. If we tried to couple the electromagnetic field to a non-conserved current, the equations would admit no solution at all — the theory would be empty, not merely inaccurate. We saw the very same mechanism at play with Einstein's equation (D1) in our [first lecture](./foundations-GR.md), where the Bianchi identity $\nabla_\mu G^{\mu\nu}\equiv 0$ forces $\nabla_\mu T^{\mu\nu}=0$, and we will meet it once more in the Fierz-Pauli construction below. The lesson generalizes to any massless field of spin $s \geq 1$: such a field couples to a current carrying $s$ indices, $J^{\mu_1\dots\mu_s}$, and the consistency of its field equations forces $\partial_\mu J^{\mu\nu\dots} = 0$. This ultimately has to do with Noether's second theorem and gauge invariance, and the detail is discussed in the following supplement. One remark before moving on: this constraint genuinely starts at spin 1. A scalar field carries no index, its field equation $\Box\phi = -\kappa J$ has no identity hidden in its left-hand side, and therefore demands nothing of $J$ — indeed Nordström's source, the trace $\mathcal{T}$, is not a conserved quantity, and the theory remains perfectly consistent. This is why spin 0 had to be eliminated by experiment, whereas spin $\geq 3$ will now be eliminated by pure thought. So for now we conclude that **a massless spin $\geq 1$ mediator must couple to a conserved current*.

<details markdown="1">
  <summary><strong>Supplement: equations of motion, gauge invariance and conserved charge (Noether's second theorem)</strong></summary>

The vanishing of $\partial_\nu\partial_\mu F^{\mu\nu}$ looks like an algebraic accident of antisymmetry. It is not. It is the visible trace of a deep and completely general mechanism, which we now unfold.

In a field theory, say that the Lagrangian is given by the general Lagrangian:

$$S = \int \text{d}^4x \;\Big[\mathcal{L}_\phi(\hat{\phi}) + \kappa \langle \hat{\phi}, J \rangle + \mathcal{L}_{m}(\psi)\Big]$$

Recall that $\hat{\phi}$ could be of any spin, and that $J$ is a current constructed from the matter fields.

Now, all this has ultimately to do with **gauge invariance**. Gauge invariance is an extremely subtle concept underlying all of modern physics and we will not be able to give you a clear explanation of it here. We will instead consider a very practical meaning to it. In a field theory, a massless field carries one physical degree of freedom for a scalar and only **two** for higher spins, their **polarisations**. 

The reason is, roughly, as follows: In order to find the number of physical degrees of freedom of a field, one usually goes into its rest frame and look for the group of transformations that leaves $p^\mu$ unchanged, the so-called **little group**.
For a *massive* particle, this frame would be $(m,\vec{0})$, which would be unchanged by any spatial rotation. The little group is $\mathrm{SO}(3)$ and one finds $2s+1$ physical states associated with the particle.
For a massless particle, there is no rest frame. One can instead consider the frame where the particle propagates along the $z$ axis and for which $p^\mu=(E,0,0,E)$. The only Lorentz transformations preserving its momentum are rotations *about* the direction of motion, and that group, $\mathrm{SO}(2)$, is **abelian**. All its representations are therefore one-dimensional, labelled by the **helicity** $h=\vec J\cdot\hat p$. As $p$ can be aligned or anti-aligned with $J$, we get two possible states $\{+h,-h\}$. Hence two, whatever the spin.  For scalar fields $\vec{J}=0$ and hence $h=0$: a single physical state.

However, the original covariant fields used to describe the theory and appearing in the Lagrangians have $1$, $4$ or $10$ components for $s=0,1,2$ respectiely. From $s\ge1$ onward the mismatch is the sign of a redundancy. It should be possible to apply transformations to the field, the **gauge transformations**, depending on an **arbitrary function** $\epsilon(x)$ that changes $\hat\phi$ without changing anything physical, simply by reshuffling the extra unphysical degrees of freedom. Spin $0$ has no mismatch, and therefore no such transformation. This is why scalars are unaffected by the whole discussion we will have now. For gravitation, these transformations are associated to arbitrary coordinate transformations, or their active counterparts, the **diffeomorphisms**. For particle physics and gauge forces, these transformations are understood as "internal" frame transformations, associated to geometric transformations of the bundle. 

**So**: for massless fields of $s \geq 1$, there must exist transformations built from an arbitrary function $\epsilon(x)$, the **gauge transformations** $\hat{\phi} \to \hat{\phi} + \delta_\epsilon\hat{\phi}$, which leave the physics invariant. They go together with a transformation of the matter components $\hat{\psi} \to \hat{\psi} + \delta_\epsilon\hat{\psi}$ in order to preserve the physics of the interaction. These transformations only shuffle the unphysical components, leaving the two physical polarisations untouched.

Now, this invariance should translate at the Lagrangian level. We will write the variations of the field using a first order Taylor expansion possibly using differential operators acting on $\epsilon$. Note here that $\epsilon$ is not a standard function but must have as many components as $\hat{\phi}$. We will simply assume here that infinitesimal gauge transformations can always be written as such. The total Lagrangian must be invariant under the infinitesimal joint transformation of $\psi$ and $\phi$ as

$$\delta_\epsilon \phi = \mathcal{R}(\epsilon), \qquad \delta_\epsilon \psi = \mathcal{M}(\epsilon),$$

where $\mathcal{R}$ and $\mathcal{M}$ are infinitesimal **linear differential operators** acting on the arbitrary function $\epsilon(x)$. Concretely, for spin 1 and 2, the operators $\mathcal{R}$ and $\mathcal{M}$ leaving the Lagrangian invariant are:

| spin | field | gauge parameter | $\mathcal{R}(\epsilon)$ | $\mathcal{M}(\epsilon)$ |
|---|---|---|---|---|
| 1 | $A_\mu$ | scalar $\epsilon$ | $\partial_\mu\epsilon$ | $i\,\epsilon\,\psi$ |
| 2 | $g_{\mu\nu}$ | vector $\xi^\mu$ | $\nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu$ | $\mathcal{L}_\xi\,\psi$ |

(For spin 1 the finite form of the matter transformation is the familiar phase rotation $\psi\to e^{i\epsilon}\psi$; for spin 2 it is the Lie derivative (see [next lecture](./altform_GR.md)), i.e. matter is simply dragged along by the coordinate change.)

Introducing the Euler–Lagrange derivative $$\dfrac{\Delta S}{\Delta\hat\phi} = \dfrac{\partial \mathcal{L}}{\partial\hat\phi} - \partial_\mu\dfrac{\partial \mathcal{L}}{\partial(\partial_\mu\hat\phi)} + \dots$$, any variation reads
$$\delta S = \int\sqrt{-|g|}\,\text{d}^4x\left[\frac{\Delta S}{\Delta\hat\phi}\,\delta\hat\phi + \frac{\Delta S}{\Delta\psi}\,\delta\psi\right]$$ (the Euler–Lagrange derivative simply absorbs the variations of the action with respect to $\delta (\partial_\mu \hat{\phi})$, integrate by part and use vanishing on the boundary, as we did multiple times explicitly already).

For the particular variation given above, invariance gives

$$0 \;=\; \int \,\text{d}^4x\left[\frac{\Delta S}{\Delta\hat\phi}\,\mathcal{R}(\epsilon) \;+\; \frac{\Delta S}{\Delta\psi}\,\mathcal{M}(\epsilon)\right].$$

Note that, we are not extremlizing the action here, as we do usually for Euler-Lagrange equations. We are simply stating that the transformations $\mathcal{R}$ and $\mathcal{M}$ are not changing anything about the physics, since they are just a reshuffling of the physical degrees of freedom. Hence this $\delta S=0$ is true all the time.
Every derivative acting on $\epsilon$ can be integrated by parts, each one costing a sign. This defines the **adjoint operator** $\mathcal{R}^\dagger$:

$$\int \,\text{d}^4x \;\;\frac{\delta S}{\delta\hat\phi}\,\mathcal{R}(\epsilon) \;=\; \int \,\text{d}^4x\;\; \mathcal{R}^\dagger(\frac{\delta S}{\delta\hat\phi})\,\epsilon.$$

For our two cases, one integration by parts gives $\mathcal{R}^\dagger = -D_\mu$ for spin 1 and $\mathcal{R}^\dagger = -2\nabla^\mu$ for spin 2. So

$$0 \;=\; \int \,\text{d}^4x\;\;\epsilon\left[\mathcal{R}^\dagger\!\left(\frac{\Delta S}{\Delta\hat\phi}\right) + \mathcal{M}^\dagger\!\left(\frac{\Delta S}{\Delta\psi}\right)\right].$$

Now, use that $\epsilon$ is arbitrary. This is the crux, and the only place the *locality* of the symmetry is used. An integral that vanishes against **every** test function has a vanishing integrand:

$$\boxed{\;\mathcal{R}^\dagger\!\left(\frac{\Delta S}{\Delta\hat\phi}\right) + \mathcal{M}^\dagger\!\left(\frac{\Delta S}{\Delta\psi}\right) = 0\;}$$

This is **Noether's second theorem**. These equations hold *identically*, for any field configuration, even when Lagrange equations are not satisfied (so called **off shell**). If you know about it, this contrast with Noether first theorem, where a *global* symmetry (constant $\epsilon$) yields a conserved current only *on* shell. Arbitrary functions buy you an identity; constants buy you a conservation law.

Now split the field equation. If the coupling of the field to matter is simple and linear (which is often the case and is always true at linear order), $$ \mathcal{L}_{\rm int} = \kappa \hat{\phi}J$$ and then $$\dfrac{\Delta S}{\Delta\hat\phi} = \dfrac{\Delta\mathcal{L}_\phi}{\Delta\hat\phi} + \kappa J$$, so

$$\underbrace{\mathcal{R}^\dagger\!\left(\frac{\Delta\mathcal{L}_\phi}{\Delta\hat\phi}\right)}_{\text{(a)}} \;+\; \kappa\,\underbrace{\mathcal{R}^\dagger(J)}_{\text{(b)}} \;+\; \underbrace{\mathcal{M}^\dagger\!\left(\frac{\Delta S}{\Delta\psi}\right)}_{\text{(c)}} \;\equiv\; 0 .$$

Term (a) vanishes by itself. The free Lagrangian $$\mathcal{L}_\phi$$ and thus the equation of motion of the free field are gauge invariant *on their own* — that is what it means for the theory to have this redundancy. Running Steps 2–4 with $$\mathcal{L}_\phi$$ alone therefore gives

$$\mathcal{R}^\dagger\!\left(\frac{\Delta\mathcal{L}_\phi}{\Delta\hat\phi}\right) \;\equiv\; 0 .$$

**This is the generalised Bianchi identity**, and it is the answer to the question we opened with. For spin 1, $$\delta\mathcal{L}_\phi/\delta A_\mu = \partial_\nu F^{\nu\mu}$$ and the identity reads $$\partial_\mu\partial_\nu F^{\nu\mu}\equiv0$$. The antisymmetry of $F$ is the *mechanism*; gauge invariance is the *reason*. It could not have come out any other way.

If we now go on the matter shell. Term (c) is proportional to the matter field equations, so it vanishes whenever the matter obeys its own dynamics. What survives is

$$\boxed{\;\mathcal{R}^\dagger(J) \;=\; 0\;}$$

**The current coupled to a gauge field must be conserved.** Explicitly:

$$\text{spin }1:\quad \nabla_\mu J^\mu = 0, \qquad\qquad \text{spin }2:\quad \nabla_\mu T^{\mu\nu} = 0 .$$

For a scalar there is no mismatch between components and degrees of freedom, hence no $R$, hence no identity, hence **no constraint whatsoever on $J$**. A scalar may couple to the trace $\mathcal{T}$ or to anything at all. This single fact is why scalar–tensor theories form such a vast landscape while massless spin 2 is rigid, and why a scalar fifth force must be *screened* rather than forbidden.

</details>

The second step translates this statement about currents into a statement about matter. What does it mean, physically, for a current to be conserved? Take the familiar case $\partial_\mu j^\mu = 0$, and define the total charge as the integral of the time component over all of space, $Q = \int j^0\,\text{d}^3x$. Its time derivative is $\dot Q = \int \partial_0 j^0\,\text{d}^3x = -\int \nabla\cdot\vec\jmath\;\text{d}^3x$, where we used the conservation equation to trade the time derivative for a spatial divergence; by the divergence theorem this is a flux through a surface at infinity, which vanishes for any localised distribution of matter. Hence $Q$ is constant in time: a conserved current means matter carries a conserved total charge. The same reasoning applies to the stress-energy tensor: $\partial_\mu T^{\mu\nu}=0$ is really four conservation equations (one for each value of $\nu$), and the four associated conserved quantities are the components of the total four-momentum, $\mathcal{P}^\nu = \int T^{0\nu}\,\text{d}^3x$ — precisely the integral of the object we introduced when constructing the vector coupling earlier in this lecture. Notice the index bookkeeping in these two examples: the current $j^\mu$ has one index and its charge $Q$ has none; the current $T^{\mu\nu}$ has two indices and its charge $P^\nu$ has one. Integrating over space consumes the time index, so a conserved current of rank $s$ endows matter with a conserved total charge of rank $s-1$. We can now restate the requirement of the first step in terms of matter alone: a spin-1 mediator requires matter to carry a conserved scalar $Q$; a spin-2 mediator, a conserved vector $Q^\mu$; and a spin-3 mediator, a conserved two-index quantity $Q^{\mu\nu}$.

The third step asks what these charges can possibly be. Think of matter as a collection of particles. What quantities does a structureless point particle carry, out of which a charge could be built? Exactly two: a number $g_i$, its coupling strength to the force in question (this is what "electric charge" is for electromagnetism), and a single four-vector, its momentum $p_i^\mu$ (its position cannot appear in a total, integrated charge). Charges must moreover be additive over the particles, as we argued when discussing the linearity of the coupling. With only these ingredients, the possible conserved charges at each rank are essentially unique: at rank zero the only candidate is $Q = \sum_i g_i$; at rank one, the only vector in town being the momentum, it must be $Q^\mu = \sum_i g_i\, p_i^\mu$; and at rank two, the only symmetric two-index object a particle can offer is the product of its momentum with itself, giving $Q^{\mu\nu} = \sum_i g_i\, p_i^\mu p_i^\nu$. One factor of momentum per index, because nothing else is available.

Now comes the decisive fourth step. A conservation law admits no exceptions: the charge must remain constant through every physical process, and in particular through the most mundane one, an elastic collision between two particles — a process in which, by definition, the total momentum is conserved while the individual momenta change direction. Let us subject each rank to this test.

At rank zero (i.e. spin-1 field), the charge $Q = \sum_i g_i$ contains no momenta at all, so a collision, which only reshuffles momenta, cannot possibly change it. Conservation is automatic, whatever the values of the $g_i$ — they may differ freely from one particle species to the next, as electric charge indeed does (electron $-1$, proton $+1$, neutron $0$). The test imposes no constraint, and this is why a spin-1 force like electromagnetism can and do exist (electromagnetism, weak and strong force). For gravity, however, we saw that the vector option was already dead twice over: wrong sign of the force, frame-dependent current.

At rank one (i.e. spin-2 field), the charge $Q^\mu = \sum_i g_i\, p_i^\mu$ does contain the momenta, and the test begins to bite. Consider a collision in which particle 1 transfers some four-momentum $q^\mu$ to particle 2; momentum conservation is the statement that what one loses the other gains, $\Delta p_1^\mu = -q^\mu$ and $\Delta p_2^\mu = +q^\mu$. The change of our candidate charge is then $\Delta Q^\mu = g_1\,\Delta p_1^\mu + g_2\,\Delta p_2^\mu = (g_2 - g_1)\,q^\mu$, and demanding that this vanish for an arbitrary momentum transfer leaves a single possibility: $g_1 = g_2$. Any two particles capable of exchanging momentum — that is, any two particles that interact at all — must couple to the spin-2 field with exactly the same strength. Pause on what has just happened: universality of the coupling was not assumed anywhere; it fell out of the conservation law. The equivalence principle, which we took as an experimental input at the beginning of this lecture, is here *derived*. And once all the $g_i$ are equal, we may absorb the common value into the coupling constant $\kappa$, and the rank-2 current of matter becomes unique: it is the stress-energy tensor $T^{\mu\nu}$ itself. Earlier we selected $T_{\mu\nu}$ as the source of the tensor coupling $\kappa\, h^{\mu\nu}T_{\mu\nu}$ by invoking the WEP; we now see there was never any freedom in that choice.

At rank two (i.e. spin-3 field), the charge $Q^{\mu\nu} = \sum_i g_i\, p_i^\mu p_i^\nu$ contains the momenta twice, and this is one time too many. To see it, place ourselves in the centre-of-mass frame of an elastic two-body collision, the frame in which the two momenta are opposite, $\vec p_2 = -\vec p_1 \equiv -\vec p$. In this frame an elastic collision does one simple thing: it rotates the pair of momenta by the deflection angle $\theta$ while preserving their common magnitude. Compute the spatial components of the charge before the collision: $Q^{ij} = g\left(p^i p^j + (-p)^i(-p)^j\right) = 2g\, p^i p^j$, the two minus signs of the second particle cancelling because the momentum enters twice — this is precisely where the "one time too many" strikes. After the collision the same computation gives $2g\, p'^i p'^j$, with $\vec p'$ the rotated momentum. Conservation requires $p'^i p'^j = p^i p^j$ for all pairs of indices, and since $\vec p'$ has the same length as $\vec p$, this forces $\vec p' = \pm\vec p$: either $\theta = 0$, meaning nothing happened, or $\theta = \pi$, the degenerate case of an exact head-on rebound. Every intermediate deflection angle — every graze, every scattering at an angle, every curved orbit — is forbidden by the conservation of $Q^{\mu\nu}$. Matter carrying such a conserved charge is matter that can never be deflected. A natural objection at this point: is angular momentum, $M^{\lambda\mu\nu} = x^\mu T^{\nu\lambda}-x^\nu T^{\mu\lambda}$, not a conserved three-index current? It is, but it is antisymmetric in two of its indices and built out of $T$ itself, whereas a spin-3 field needs an independent, *symmetric* current; the objection does not go through.

The verdict follows. A spin-3 (or higher) field could only couple to matter whose trajectories nothing can alter; but altering trajectories is the very definition of what a force does, and gravity in particular must pull on everything. Such a field would therefore destroy, through its own action, the conservation law its consistency depends on. The only way out is for the coupling to vanish identically for any matter that interacts: massless fields of spin $\geq 3$ may exist in isolation, but they can generate no macroscopic long-range force. 
s
This classical argument is the skeleton of two celebrated theorems of quantum field theory, which make it rigorous. Weinberg's soft theorem ([Weinberg (1964)](https://link.aps.org/doi/10.1103/PhysRev.135.B1049)) derives exactly the chain above — charge conservation at $s=1$, the equivalence principle at $s=2$, no long-range force for $s\geq 3$ — from Lorentz invariance alone. The Weinberg-Witten theorem ([Weinberg and Witten (1980)](https://doi.org/10.1016/0370-2693(80)90212-9)) forbids massless particles of spin $>2$ in any theory possessing a Lorentz-covariant conserved stress tensor. One caveat, since these theorems are often over-quoted: they assume flat asymptotic space-time and Lorentz-covariant currents. Interacting higher-spin theories do exist on anti-de Sitter backgrounds (Vasiliev theory), and the graviton itself evades Weinberg-Witten precisely because the gravitational stress tensor is not a Lorentz-covariant tensor (it is a *pseudo-tensor*) — the field-theoretic shadow of the fact that gravitational energy cannot be localised.

Hence, we conclude that the mediator of gravity must certainly be a massless spin-2 field. Every thread of the lecture now converges on the coupling proposed at the start: $$\mathcal{L}_{\rm int} = \kappa\, h^{\mu\nu}T_{\mu\nu}$$ with $T_{\mu\nu}$ not merely a convenient choice but the unique conserved rank-2 current that interacting matter can possess, coupled with the universal strength that the conservation law itself enforces. Now, is it possible to build such a theory, and is it equivalent to GR?

### Gravity as a spin-2 field: The Fierz-Pauli approach

We now build the theory. A massless spin-2 field is described by a symmetric rank-2 tensor $h_{\mu\nu}=h_{\nu\mu}$ (10 components). It is possible to show that the unique **Lorentz-invariant, two-derivative, ghost-free kinetic term** is the **Fierz-Pauli Lagrangian** ([Fierz & Pauli (1939)](https://doi.org/10.1098/rspa.1939.0140)):

$$\boxed{\mathcal{L}_{\rm FP} = -\frac{1}{2}\partial_\kappa h_{\mu\nu}\partial^\kappa h^{\mu\nu} + \partial_\mu h_{\nu\kappa}\partial^\nu h^{\mu\kappa} - \partial_\mu h^{\mu\nu}\partial_\nu h + \frac{1}{2}\partial_\kappa h\,\partial^\kappa h}$$

where $h\equiv \eta^{\mu\nu}h_{\mu\nu}$ is the trace. The interaction with matter, following our rule that a rank-2 field couples to a rank-2 current, is

$$\mathcal{L}_{\rm int} = \frac{\kappa}{2} h_{\mu\nu}T^{\mu\nu}$$

with an additional factor of $1/2$ simply to match conventions in the litterature. Varying $$\mathcal{L}_{\rm FP}+\mathcal{L}_{\rm int}$$ gives the linearised Einstein equations that we already encountered when talking about [gravitational waves](./validation_GR.md), now sourced by the *full* $T_{\mu\nu}$ — not just its trace. 

<details markdown="1">
  <summary><strong>Proof: the equation of motions</strong></summary>

We recall from our [previous class](./validation_GR.md) that the linearized Einstein equations are

$$G^{(1)}_{\mu\nu} = \tfrac12\Big(\partial_\alpha\partial_\mu h^{\alpha}{}_{\nu} + \partial_\alpha\partial_\nu h^{\alpha}{}_{\mu} - \Box h_{\mu\nu} - \partial_\mu\partial_\nu h - \eta_{\mu\nu}\,\partial_\alpha\partial_\beta h^{\alpha\beta} + \eta_{\mu\nu}\,\Box h\Big) = 8\pi G\, T_{\mu\nu},$$

before we use multiple tricks to fix a gauge and suppress as many terms as possible.

**Second: Fierz Pauli equations of motion**

Now we use Euler-Lagrange equation directly:

$$\frac{\partial \mathcal{L}}{\partial h_{\alpha\beta}} = \partial_\sigma\left(\frac{\partial \mathcal{L}}{\partial(\partial_\sigma h_{\alpha\beta})}\right) $$

The left-hand side is simply coming from the interaction term:

$$ \frac{\partial \mathcal{L}}{\partial h_{\alpha\beta}} = \frac{\kappa}{2}T^{\alpha\beta}$$

The right-hand side is the sum of the derivative of the four terms in the kinetic Lagrangian.

Now, we must extensively use the fact that the symmetry of $h_{\mu\nu}$ imposes:

$$\frac{\partial(\partial_\rho h_{\mu\nu})}{\partial(\partial_\sigma h_{\alpha\beta})}=\delta^{\sigma}_{\rho}\,\delta^{(\alpha}_{\mu}\delta^{\beta)}_{\nu}\equiv\delta^{\sigma}_{\rho}\,\tfrac12\big(\delta^{\alpha}_{\mu}\delta^{\beta}_{\nu}+\delta^{\beta}_{\mu}\delta^{\alpha}_{\nu}\big)$$

this is a easy to miss trick in order to account for the fact that symmetric terms, say $h_{01}$ and $h_{10}$ are the same, so the derivative of one with respect to the other must be $1$ and not 0. The $1/2$ factor is here to avoid double counting such terms in sums.

The **first term** is exactly as for a scalar field kinetic term:

$$
\begin{align}
\frac{\partial }{\partial(\partial_\sigma h_{\alpha\beta})}\Big(-\tfrac{1}{2}\partial_\kappa h_{\mu\nu}\partial^\kappa h^{\mu\nu}\Big) = -\,\partial^\sigma h^{\alpha\beta}\\
\partial_\sigma\Big(-\partial^\sigma h^{\alpha\beta}\Big)= -\,\Box h^{\alpha\beta}
\end{align}
$$

**The second term** $\partial_\mu h_{\nu\kappa}\partial^\nu h^{\mu\kappa}$ can be written with all indices down as

$$\partial_\mu h_{\nu\kappa}\partial^\nu h^{\mu\kappa}=\eta^{\nu\lambda}\eta^{\mu\rho}\eta^{\kappa\tau}\,\partial_\mu h_{\nu\kappa}\,\partial_\lambda h_{\rho\tau}$$

Unlike the first term the two factors are *different*, so the product rule genuinely produces two distinct contributions. The derivative with respect to $\partial_\sigma h_{\alpha\beta}$ becomes:

$$
\begin{aligned}
&\eta^{\nu\lambda}\eta^{\mu\rho}\eta^{\kappa\tau}\,\Bigg( \frac{\partial(\partial_\mu h_{\nu\kappa})}{\partial(\partial_\sigma h_{\alpha \beta})} \,\partial_\lambda h_{\rho\tau} + \partial_\mu h_{\nu\kappa}\, \frac{\partial(\partial_\lambda h_{\rho\tau})}{\partial(\partial_\sigma h_{\alpha \beta})}\Bigg)\\[6pt]
&= \eta^{\nu\lambda}\eta^{\mu\rho}\eta^{\kappa\tau}\Bigg(\delta^{\sigma}_{\mu}\,\delta^{(\alpha}_{\nu}\delta^{\beta)}_{\kappa}\ \partial_\lambda h_{\rho\tau} \;+\; \partial_\mu h_{\nu\kappa}\ \delta^{\sigma}_{\lambda}\,\delta^{(\alpha}_{\rho}\delta^{\beta)}_{\tau}\Bigg)\\[6pt]
&= \tfrac12\Big(\eta^{\alpha\lambda}\eta^{\sigma\rho}\eta^{\beta\tau}+\eta^{\beta\lambda}\eta^{\sigma\rho}\eta^{\alpha\tau}\Big)\partial_\lambda h_{\rho\tau}
\;+\;\tfrac12\Big(\eta^{\nu\sigma}\eta^{\mu\alpha}\eta^{\kappa\beta}+\eta^{\nu\sigma}\eta^{\mu\beta}\eta^{\kappa\alpha}\Big)\partial_\mu h_{\nu\kappa}\\[6pt]
&= \tfrac12\Big(\partial^\alpha h^{\sigma\beta}+\partial^\beta h^{\sigma\alpha}\Big)\;+\;\tfrac12\Big(\partial^\alpha h^{\sigma\beta}+\partial^\beta h^{\sigma\alpha}\Big)\\[6pt]
&= \partial^\alpha h^{\sigma\beta}+\partial^\beta h^{\sigma\alpha}
\end{aligned}
$$

Such that the final Euler-Lagrange right-hand side term is:

$$\begin{aligned}
\partial_\sigma\Big(\partial^\alpha h^{\sigma\beta}+\partial^\beta h^{\sigma\alpha}\Big)&=\partial^\alpha\partial_\sigma h^{\sigma\beta}+\partial^\beta\partial_\sigma h^{\sigma\alpha}
\end{aligned}
$$

**The third term** $$-\partial_\mu h^{\mu\nu}\partial_\nu h$$ is computed again with the product rule, keeping in mind that the trace is $$h= h^{\lambda}{}_{\lambda}=\eta^{\lambda\pi}h_{\lambda\pi}$$. We write it with all indices down as $$-\partial_\mu h^{\mu\nu}\partial_\nu h= -\,\eta^{\mu\rho}\eta^{\nu\tau}\eta^{\lambda\pi}\,\partial_\mu h_{\rho\tau}\,\partial_\nu h_{\lambda\pi}$$

Here the two factors are of two *different* shapes — one is a divergence, the other a trace — so the two pieces of the product rule will **not** be equal, unlike for the second term and hence the derivative with respect to $\partial_\sigma h_{\alpha\beta}$ becomes:

$$
\begin{aligned}
&-\eta^{\mu\rho}\eta^{\nu\tau}\eta^{\lambda\pi}\Bigg(\frac{\partial(\partial_\mu h_{\rho\tau})}{\partial(\partial_\sigma h_{\alpha\beta})}\,\partial_\nu h_{\lambda\pi}+\partial_\mu h_{\rho\tau}\,\frac{\partial(\partial_\nu h_{\lambda\pi})}{\partial(\partial_\sigma h_{\alpha\beta})}\Bigg)\\[4pt]
&=-\eta^{\mu\rho}\eta^{\nu\tau}\eta^{\lambda\pi}\Bigg(\delta^{\sigma}_{\mu}\delta^{(\alpha}_{\rho}\delta^{\beta)}_{\tau}\,\partial_\nu h_{\lambda\pi}+\partial_\mu h_{\rho\tau}\,\delta^{\sigma}_{\nu}\delta^{(\alpha}_{\lambda}\delta^{\beta)}_{\pi}\Bigg)\\[4pt]
&=-\tfrac12\big(\eta^{\sigma\alpha}\,\partial^{\beta}h+\eta^{\sigma\beta}\,\partial^{\alpha}h\big)\;-\;\eta^{\alpha\beta}\,\partial_\mu h^{\mu\sigma}
\end{aligned}
$$

In the first piece $$\delta^{\sigma}_{\mu}\delta^{(\alpha}_{\rho}\delta^{\beta)}_{\tau}$$ eats the *divergence* factor, leaving behind the trace $$\eta^{\lambda\pi}\partial_\nu h_{\lambda\pi}=\partial_\nu h$$ with $$\eta^{\nu\tau}\delta^{\beta}_{\tau}$$ raising its index; in the second piece $$\delta^{\sigma}_{\nu}\delta^{(\alpha}_{\lambda}\delta^{\beta)}_{\pi}$$ eats the *trace* factor and its two free indices close onto each other to give the metric $\eta^{\alpha\beta}$, leaving the divergence untouched.

Such that the final Euler-Lagrange term is:

$$\begin{aligned}
\partial_\sigma\Big(-\tfrac12\big(\eta^{\sigma\alpha}\partial^{\beta}h+\eta^{\sigma\beta}\partial^{\alpha}h\big)-\eta^{\alpha\beta}\partial_\mu h^{\mu\sigma}\Big)&= -\,\partial^\alpha\partial^\beta h\;-\;\eta^{\alpha\beta}\,\partial_\mu\partial_\nu h^{\mu\nu}
\end{aligned}
$$

where in the last step $\partial_\sigma\big(\eta^{\sigma\alpha}\partial^\beta h\big)=\partial^\alpha\partial^\beta h$ and the two symmetrised halves recombine, since partial derivatives commute.

**and the fourth term** $$\tfrac12\partial_\kappa h\,\partial^\kappa h$$ is again of "scalar" type, with the trace $h$ playing the role of the scalar. With all indices down: $$\tfrac12\partial_\kappa h\,\partial^\kappa h=\tfrac12\,\eta^{\kappa\rho}\eta^{\mu\nu}\eta^{\lambda\pi}\,\partial_\kappa h_{\mu\nu}\,\partial_\rho h_{\lambda\pi}$$

The two factors are now identical, so — exactly as for the first term — the product rule gives twice the same contribution and the factor $2$ cancels the $\tfrac12$:

$$
\begin{aligned}
&\tfrac12\,\eta^{\kappa\rho}\eta^{\mu\nu}\eta^{\lambda\pi}\Bigg(\frac{\partial(\partial_\kappa h_{\mu\nu})}{\partial(\partial_\sigma h_{\alpha\beta})}\,\partial_\rho h_{\lambda\pi}+\partial_\kappa h_{\mu\nu}\,\frac{\partial(\partial_\rho h_{\lambda\pi})}{\partial(\partial_\sigma h_{\alpha\beta})}\Bigg)\\[4pt]
&=\tfrac12\,\eta^{\kappa\rho}\eta^{\mu\nu}\eta^{\lambda\pi}\Bigg(\delta^{\sigma}_{\kappa}\delta^{(\alpha}_{\mu}\delta^{\beta)}_{\nu}\,\partial_\rho h_{\lambda\pi}+\partial_\kappa h_{\mu\nu}\,\delta^{\sigma}_{\rho}\delta^{(\alpha}_{\lambda}\delta^{\beta)}_{\pi}\Bigg)\\[4pt]
&=\tfrac12\Big(\eta^{\alpha \beta}\,\partial^{\sigma}h+\eta^{\alpha\beta}\,\partial^{\sigma}h\Big)\;=\;\eta^{\alpha\beta}\,\partial^{\sigma}h
\end{aligned}
$$

the only new ingredient being $$\eta^{\mu\nu}\delta^{(\alpha}_{\mu}\delta^{\beta)}_{\nu}=\eta^{\alpha\beta}$$, i.e. $$\partial h/\partial h_{\alpha\beta}=\eta^{\alpha\beta}$$.

Such that the final Euler-Lagrange term is:

$$\begin{aligned}
\partial_\sigma\Big(\eta^{\alpha\beta}\,\partial^{\sigma}h\Big)&=+\,\eta^{\alpha\beta}\,\Box h
\end{aligned}
$$

Note the $+$ sign here, opposite to the $-\Box h^{\alpha\beta}$ of the first term: the two "scalar-type" terms enter the Lagrangian with opposite signs, $-\tfrac12$ and $+\tfrac12$.

Summing them all together, we find $2$ times the left-hand side of the linearized Einstein equations:

$$ \partial_\sigma\left(\frac{\partial \mathcal{L}}{\partial(\partial_\sigma h_{\alpha\beta})}\right) = 2\times\tfrac12\Big(\partial^\alpha\partial_\sigma h^{\sigma\beta} + \partial^\beta\partial_\sigma h^{\sigma\alpha} - \Box h^{\alpha\beta} - \partial^\alpha\partial^\beta h - \eta^{\alpha\beta}\,\partial_\mu\partial_\nu h^{\mu\nu} + \eta^{\alpha\beta}\,\Box h\Big)=2\,G^{(1)\alpha\beta}[h]$$

Thus, equating both sides,

$$\frac{\kappa}{2}\,T^{\alpha\beta}=2\,G^{(1)\alpha\beta}[h]
\qquad\Longleftrightarrow\qquad
\boxed{\;G^{(1)}_{\mu\nu}[h]=\frac{\kappa}{4}\,T_{\mu\nu}\;}$$

we really get the linearized Einstein equations. Now we should be extremely careful for once. The $h_{\mu\nu}$ from the previous class, defined as a small perturbation of the metric $g_{\mu\nu} = \eta_{\mu\nu}+ h_{\mu\nu}$ in GR, can not be identified directly with our spin-2 field appearing in the Fierz Pauli Lagrangian. The reason is dimensions! A perturbation of the metric has dimension of length to the four while a field in the Lagrangian has a dimension of mass. In order to fix it, we define the following correspondance:

$$h^{\rm GR}_{\mu\nu}=\kappa\,h^{FP}_{\mu\nu}$$

Under this redefinition of the field, we get that:

$$\boxed{\;\kappa=\sqrt{32\pi G}\;}$$

</details>

We studied already what we can get out of the linearized Einstein equations: an appropriate gauge choice gives us gravitational waves and  the static limit reproduces Newton inverse square law exactly. Because the photon's stress-energy tensor is traceless but *non-zero*, light now both gravitates and is deflected: the predicted deflection of a ray grazing the Sun at impact parameter $b$ is $$\delta\theta = \frac{4GM}{c^2 b}$$ as desired. This is a **fantastic success**!

However, this is only the first order Einstein equation and we do not have the post-Newtonian terms. Hence, we can not for example, predict a shift of the perihelion of mercury. This is not so great. This was close, but this theory is **not general relativity**.

More problems are ahead of us. The kinetic part of $$\mathcal{L}_{\rm FP}$$ is invariant under the transformation:

$$h_{\mu\nu} \;\longrightarrow\; h_{\mu\nu} + \partial_\mu\xi_\nu + \partial_\nu\xi_\mu$$

for any vector $\xi^\mu(x)$. This is a form of **gauge invariance** for this theory. This is the spin-2 analogue of $A_\mu\to A_\mu+\partial_\mu\alpha$ in electromagnetism, and it is *required*: it removes $10 - 4 - 4 = 2$ components, leaving exactly the 2 polarisations of a massless spin-2 particle (the "+" and "$\times$" of gravitational waves). We did not put this symmetry in by hand — it is forced when writting the Lagrangian when demanding no ghosts.

<details markdown="1">
  <summary><strong>Proof and discussion: gauge invariance for Fierz-Pauli Lagrangian</strong></summary>

We prove this by brute force. Nothing enters but three ingredients: the **product rule**, **integration by parts**, and the fact that **partial derivatives commute**. No geometry, no Lie derivatives, no assumption that this Lagrangian came from anywhere — which is important, since the whole point of this section is to *arrive* at general relativity rather than presuppose it.
The Lagrangian will *not* be left literally unchanged — that is too much to ask, and it is not what is needed. What must be invariant is the **action**, so what we must prove is that $\delta_\xi\mathcal{L}_{\rm FP}$ is a **total derivative**,

$$\delta_\xi\mathcal{L}_{\rm FP}=\partial_\sigma K^\sigma\qquad\Longrightarrow\qquad \delta_\xi S_{\rm FP}=\int\mathrm{d}^4x\;\partial_\sigma K^\sigma=\oint K^\sigma\mathrm{d}\Sigma_\sigma=0$$

for fields decaying at infinity. We will exhibit $K^\sigma$ explicitly at the end. Throughout, the symbol $\simeq$ means **"equal up to a total derivative"**, i.e. equal after discarding terms that integrate to a boundary. Write the transformation and its trace as

$$\delta_\xi h_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,\qquad
\delta_\xi h=\eta^{\mu\nu}\big(\partial_\mu\xi_\nu+\partial_\nu\xi_\mu\big)=2\,\partial^\lambda\xi_\lambda\equiv 2\,(\partial\!\cdot\!\xi)$$

**One simplification before we start.** $\mathcal{L}_{\rm FP}$ is exactly quadratic in $h$, so for any shift $h\to h+\psi$,

$$\mathcal{L}_{\rm FP}[h+\psi]=\mathcal{L}_{\rm FP}[h]+\underbrace{2B[h,\psi]}_{\text{cross term}}+\;\mathcal{L}_{\rm FP}[\psi]$$

where $B$ is the symmetric bilinear form with $$B[h,h]=\mathcal{L}_{\rm FP}[h]$$. It is enough to show the **cross term** is a total derivative for every $h$: if it is, then choosing $h=\psi$ gives $$2\mathcal{L}_{\rm FP}[\psi]\simeq0$$, so the last piece is a total derivative too. So from here on we compute only the part of $\delta\mathcal{L}_{\rm FP}$ that is linear in $\xi$ *and* linear in $h$.

**Now vary the four terms, one at a time**

**Term 1.** $$\;T_1=-\tfrac12\,\partial_\kappa h_{\mu\nu}\,\partial^\kappa h^{\mu\nu}$$.

Both factors are the same field, so the product rule gives twice the same contribution and the factor $\tfrac12$ is cancelled:

$$\delta T_1=-\,\partial_\kappa h^{\mu\nu}\;\partial^\kappa\big(\delta h_{\mu\nu}\big)
=-\,\partial_\kappa h^{\mu\nu}\;\partial^\kappa\big(\partial_\mu\xi_\nu+\partial_\nu\xi_\mu\big)$$

Because $h^{\mu\nu}$ is symmetric, the two pieces in the bracket give the same thing (relabel $\mu\leftrightarrow\nu$ in the second), so

$$\boxed{\;\delta T_1=-\,2\,\partial_\kappa h^{\mu\nu}\;\partial^\kappa\partial_\mu\xi_\nu\;}$$

**Term 2.** $$\;T_2=+\,\partial_\mu h_{\nu\kappa}\,\partial^\nu h^{\mu\kappa}$$.

Here the two factors carry their indices *differently*, so in principle we must vary each and the two results need not agree. In fact they do. Varying the second factor gives $\partial_\mu h_{\nu\kappa}\,\partial^\nu\delta h^{\mu\kappa}$; renaming the dummy pair $\mu\leftrightarrow\nu$ and using the symmetry of $h$ and of $\delta h$ turns this into $\partial_\mu\delta h_{\nu\kappa}\,\partial^\nu h^{\mu\kappa}$, which is what varying the first factor gives. So again we get twice one contribution:

$$
\begin{aligned}
\delta T_2&=2\,\partial_\mu\big(\delta h_{\nu\kappa}\big)\,\partial^\nu h^{\mu\kappa}
=2\,\partial_\mu\big(\partial_\nu\xi_\kappa+\partial_\kappa\xi_\nu\big)\,\partial^\nu h^{\mu\kappa}\\[4pt]
&=\boxed{\;2\,\partial^\nu h^{\mu\kappa}\,\partial_\mu\partial_\nu\xi_\kappa\;+\;2\,\partial^\nu h^{\mu\kappa}\,\partial_\mu\partial_\kappa\xi_\nu\;}
\end{aligned}
$$

Note that this time the two pieces are genuinely different: in the first, both derivatives on $\xi$ are contracted with the *derivative* index and one *tensor* index of $h$; in the second, they are contracted with the two tensor indices. Keep them apart, they will end up in different pairings.

**Term 3.** $$\;T_3=-\,\partial_\mu h^{\mu\nu}\,\partial_\nu h$$.

The two factors now have *different shapes* — one is a divergence, the other a trace — so the product rule gives two genuinely distinct contributions, and there is no factor of $2$. We need both variations separately:

$$\delta\big(\partial_\mu h^{\mu\nu}\big)=\partial_\mu\big(\partial^\mu\xi^\nu+\partial^\nu\xi^\mu\big)=\Box\xi^\nu+\partial^\nu(\partial\!\cdot\!\xi),
\qquad
\delta\big(\partial_\nu h\big)=2\,\partial_\nu(\partial\!\cdot\!\xi)$$

so that

$$\boxed{\;\delta T_3=-\,\big(\partial_\nu h\big)\,\Box\xi^\nu\;-\;\big(\partial^\nu h\big)\,\partial_\nu(\partial\!\cdot\!\xi)\;-\;2\,\big(\partial_\mu h^{\mu\nu}\big)\,\partial_\nu(\partial\!\cdot\!\xi)\;}$$

where in the middle term we raised the index on $\partial_\nu h$ against the $\partial^\nu(\partial\!\cdot\!\xi)$ it multiplies.

**Term 4.** $$\;T_4=+\tfrac12\,\partial_\kappa h\,\partial^\kappa h$$.

Same field twice again, so the $\tfrac12$ is cancelled:

$$\boxed{\;\delta T_4=\partial_\kappa h\,\partial^\kappa\big(\delta h\big)=2\,\big(\partial^\nu h\big)\,\partial_\nu(\partial\!\cdot\!\xi)\;}$$


Now, collect, and relabel to a common set of index names. Adding the four boxed results gives seven pieces. Rename dummy indices so that everything is written with the free structure "(two derivatives of $\xi_\beta$) $\times$ (one derivative of $h$)":

$$
\begin{array}{llll}
\text{from }T_1: & (a) & -2\,\partial^\lambda h^{\alpha\beta}\;\partial_\lambda\partial_\alpha\xi_\beta &\\[3pt]
\text{from }T_2: & (b) & +2\,\partial^\lambda h^{\alpha\beta}\;\partial_\alpha\partial_\lambda\xi_\beta &\\
                 & (c) & +2\,\partial^\beta h^{\alpha\lambda}\;\partial_\alpha\partial_\lambda\xi_\beta &\\[3pt]
\text{from }T_3: & (d) & -\big(\partial_\nu h\big)\,\Box\xi^\nu &\\
                 & (e) & -\big(\partial^\nu h\big)\,\partial_\nu(\partial\!\cdot\!\xi) &\\
                 & (f) & -2\big(\partial_\mu h^{\mu\nu}\big)\,\partial_\nu(\partial\!\cdot\!\xi) &\\[3pt]
\text{from }T_4: & (g) & +2\big(\partial^\nu h\big)\,\partial_\nu(\partial\!\cdot\!\xi) &
\end{array}
$$

and these seven cancel in **three pairs**. Two of the pairs need an integration by parts; one does not.

**first pair — $(a)+(b)$, no work required**

Look at them side by side:

$$(a)+(b)=-2\,\partial^\lambda h^{\alpha\beta}\,\partial_\lambda\partial_\alpha\xi_\beta\;+\;2\,\partial^\lambda h^{\alpha\beta}\,\partial_\alpha\partial_\lambda\xi_\beta\;=\;0$$

They differ *only* in the order of the two derivatives acting on $\xi_\beta$, and partial derivatives commute. This is the first term of $\mathcal{L}_{\rm FP}$ annihilating half of the second, and it fixes the relative coefficient $-\tfrac12$ versus $+1$ between them.

**second pair — the trace terms $(d)+(e)+(g)$**

First combine $(e)$ and $(g)$, which are the same object with coefficients $-1$ and $+2$:

$$(e)+(g)=+\big(\partial^\nu h\big)\,\partial_\nu(\partial\!\cdot\!\xi)$$

Now integrate both surviving terms by parts twice, moving every derivative off $\xi$.

For $(d)=-\big(\partial_\nu h\big)\partial^\lambda\partial_\lambda\xi^\nu$:

$$
\begin{aligned}
(d)&=\underbrace{-\,\partial^\lambda\Big[\big(\partial_\nu h\big)\partial_\lambda\xi^\nu\Big]}_{\text{total derivative}}+\big(\partial^\lambda\partial_\nu h\big)\,\partial_\lambda\xi^\nu\\[4pt]
&\simeq\underbrace{+\,\partial_\lambda\Big[\big(\partial^\lambda\partial_\nu h\big)\xi^\nu\Big]}_{\text{total derivative}}-\big(\Box\,\partial_\nu h\big)\,\xi^\nu
\;\;\simeq\;\;-\,\big(\Box\,\partial^\beta h\big)\,\xi_\beta
\end{aligned}
$$

For $(e)+(g)=\big(\partial^\nu h\big)\partial_\nu\partial^\lambda\xi_\lambda$, the same two steps:

$$
\begin{aligned}
(e)+(g)&=\partial_\nu\Big[\big(\partial^\nu h\big)\partial^\lambda\xi_\lambda\Big]-\big(\Box h\big)\,\partial^\lambda\xi_\lambda\\[4pt]
&\simeq-\,\partial^\lambda\Big[\big(\Box h\big)\xi_\lambda\Big]+\big(\partial^\lambda\Box h\big)\,\xi_\lambda
\;\;\simeq\;\;+\,\big(\partial^\beta\Box h\big)\,\xi_\beta
\end{aligned}
$$

Adding them,

$$(d)+(e)+(g)\;\simeq\;-\big(\Box\partial^\beta h\big)\xi_\beta+\big(\partial^\beta\Box h\big)\xi_\beta\;=\;0$$

again because derivatives commute. This is the third term of $\mathcal{L}_{\rm FP}$ against the fourth, and it is what fixes the coefficients $-1$ and $+\tfrac12$.

**third pair — $(c)+(f)$**

For $(c)=2\,\partial^\beta h^{\alpha\lambda}\,\partial_\alpha\partial_\lambda\xi_\beta$, integrate by parts on $\partial_\alpha$, then on $\partial_\lambda$:

$$
\begin{aligned}
(c)&=\partial_\alpha\Big[2\,\partial^\beta h^{\alpha\lambda}\,\partial_\lambda\xi_\beta\Big]-2\big(\partial_\alpha\partial^\beta h^{\alpha\lambda}\big)\,\partial_\lambda\xi_\beta\\[4pt]
&\simeq-\,\partial_\lambda\Big[2\big(\partial_\alpha\partial^\beta h^{\alpha\lambda}\big)\xi_\beta\Big]+2\big(\partial_\lambda\partial_\alpha\partial^\beta h^{\alpha\lambda}\big)\,\xi_\beta
\;\;\simeq\;\;+2\,\partial^\beta\big(\partial_\alpha\partial_\lambda h^{\alpha\lambda}\big)\,\xi_\beta
\end{aligned}
$$

For $(f)=-2\big(\partial_\mu h^{\mu\nu}\big)\partial_\nu\partial^\lambda\xi_\lambda$, write $A^\nu\equiv\partial_\mu h^{\mu\nu}$ and do the same:

$$
\begin{aligned}
(f)&=-2\,\partial_\nu\Big[A^\nu\,\partial^\lambda\xi_\lambda\Big]+2\big(\partial_\nu A^\nu\big)\,\partial^\lambda\xi_\lambda\\[4pt]
&\simeq+2\,\partial^\lambda\Big[\big(\partial_\nu A^\nu\big)\xi_\lambda\Big]-2\big(\partial^\lambda\partial_\nu A^\nu\big)\,\xi_\lambda
\;\;\simeq\;\;-2\,\partial^\beta\big(\partial_\nu\partial_\mu h^{\mu\nu}\big)\,\xi_\beta
\end{aligned}
$$

The two surviving pieces are the *same scalar* $\partial_\alpha\partial_\lambda h^{\alpha\lambda}=\partial_\mu\partial_\nu h^{\mu\nu}$ — only the names of the dummy indices differ — so

$$(c)+(f)\;\simeq\;0$$

This is the *other* half of the second term of $\mathcal{L}_{\rm FP}$ against the third.

So finally we conclude:  All seven pieces are accounted for and $$\delta_\xi\mathcal{L}_{\rm FP}\simeq0$$: the Fierz-Pauli action is invariant under $$h_{\mu\nu}\to h_{\mu\nu}+\partial_\mu\xi_\nu+\partial_\nu\xi_\mu$$. 

Collecting every total derivative we discarded along the way gives the current explicitly,

$$
\begin{aligned}
K^\sigma=\;&2\,\partial^\beta h^{\sigma\lambda}\,\partial_\lambda\xi_\beta\;-\;2\big(\partial_\alpha\partial^\beta h^{\alpha\sigma}\big)\xi_\beta\\
&-\big(\partial_\nu h\big)\partial^\sigma\xi^\nu\;+\;\big(\partial^\sigma\partial_\nu h\big)\xi^\nu\\
&+\big(\partial^\sigma h\big)\partial^\lambda\xi_\lambda\;-\;\big(\Box h\big)\xi^\sigma\\
&-2\big(\partial_\mu h^{\mu\sigma}\big)\partial^\lambda\xi_\lambda\;+\;2\big(\partial_\nu\partial_\mu h^{\mu\nu}\big)\xi^\sigma
\end{aligned}
\qquad\text{with}\qquad
\delta_\xi\mathcal{L}_{\rm FP}=\partial_\sigma K^\sigma
$$

so that $\delta_\xi\mathcal{L}_{\rm FP}$ is a perfectly ordinary non-vanishing function of $x$ — it is only its integral that is zero.

**What the computation is really telling us**

Every one of the four terms in $\mathcal{L}_{\rm FP}$ was used, and each cancellation used a specific pair of *relative coefficients*:

| pair | terms involved | coefficients it fixes |
|---|---|---|
| $(a)+(b)$ | 1st against half of 2nd | $-\tfrac12$ vs $+1$ |
| $(c)+(f)$ | other half of 2nd against 3rd | $+1$ vs $-1$ |
| $(d)+(e)+(g)$ | 3rd against 4th | $-1$ vs $+\tfrac12$ |

Detune any one coefficient and the corresponding pair no longer cancels. This is a second, independent route to the claim made in the main text that the Fierz-Pauli tuning is forced: the coefficients $\big(-\tfrac12,\,1,\,-1,\,\tfrac12\big)$ are precisely and uniquely the ones for which these three cancellations happen, so **demanding gauge invariance alone reproduces $\mathcal{L}_{\rm FP}$**, up to overall normalisation, without ever mentioning ghosts. The two requirements — "no ghosts" and "gauge invariant" — cut out the same unique Lagrangian.

</details>

As discussed above regarding Noether's second theorem, this gauge symmetry demands a conserved source. Under the gauge transformation, $$\mathcal{L}_{\rm int}$$ shifts by $$- \kappa\, \xi_\nu \partial_\mu T^{\mu\nu}$$. Dropping the total derivative, the full Lagrangian is really gauge invariant **if and only if**

$$\partial_\mu T^{\mu\nu}=0$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Here $T^{\mu\nu}$ is a *fixed external* source: the gauge transformation acts on $h_{\mu\nu}$ and on nothing else, so $\delta_\xi T^{\mu\nu}=0$. Then, using the symmetry of $T^{\mu\nu}$ to relabel the dummy indices of the second piece,

$$\delta_\xi\mathcal{L}_{\rm int}=\frac{\kappa}{2}\big(\partial_\mu\xi_\nu+\partial_\nu\xi_\mu\big)T^{\mu\nu}=\kappa\,T^{\mu\nu}\partial_\mu\xi_\nu$$

Applying the product rule backwards splits this into a total derivative and a remainder:

$$\boxed{\;\delta_\xi\mathcal{L}_{\rm int}=\underbrace{\kappa\,\partial_\mu\big(T^{\mu\nu}\xi_\nu\big)}_{\text{total derivative}}\;-\;\kappa\,\xi_\nu\,\partial_\mu T^{\mu\nu}\;}$$

which is the shift quoted in the main text. The **"if"** direction is now immediate: if $\partial_\mu T^{\mu\nu}=0$ only the total derivative survives and the action does not change.

The **"only if"** direction is where the *locality* of $\xi$ does the work. Suppose the action is invariant for every $\xi$. Then

$$0=\delta_\xi S_{\rm int}=-\kappa\int\mathrm{d}^4x\;\xi_\nu(x)\,\partial_\mu T^{\mu\nu}(x)\qquad\text{for all }\xi_\nu$$

and by the fundamental lemma of the calculus of variations — if $\int f_\nu\xi^\nu=0$ for every smooth compactly supported $\xi^\nu$ then $f_\nu\equiv0$ — we conclude $\partial_\mu T^{\mu\nu}=0$ at every point. 

Note that a *global* symmetry (constant $\xi$, i.e. a translation) would only have given the much weaker statement that the total four-momentum $P^\nu=\int\mathrm{d}^3x\,T^{0\nu}$ is conserved. A local symmetry gives a local conservation law.

There is a blunter way to see the same thing, which never mentions the action. Take the divergence of the field equation $G^{(1)\mu\nu}=\tfrac{\kappa}{4}T^{\mu\nu}$. The left-hand side vanishes *identically* by the linearised Bianchi identity proved above, for any $h$ whatsoever. So $\partial_\mu T^{\mu\nu}=0$ is not merely a symmetry requirement but an **integrability condition**: hand the theory a non-conserved source and the field equation has no solution at all. This is the same phenomenon as $\partial_\mu F^{\mu\nu}=J^\nu$ being unsolvable unless $\partial_\nu J^\nu=0$.

</details>

**HOWEVER, the source is *not* conserved, and this destroys the theory.** Once matter feels the gravitational field, it exchanges energy and momentum with it, so $\partial_\mu T^{\mu\nu}_{\rm matter}\neq 0$. 

<details markdown="1">
  <summary><strong>Proof</strong></summary>

We show this on the simplest possible piece of matter, a point particle of mass $m$ on a worldline $z^\mu(\tau)$, where every step is explicit. Nothing depends on that choice.

**The divergence of $T^{\mu\nu}$ is the force density.** For a point particle,

$$T^{\mu\nu}(x)=m\int\mathrm{d}\tau\;\dot z^\mu\dot z^\nu\;\delta^{(4)}\big(x-z(\tau)\big)$$

Smear against an arbitrary smooth test field $\psi_\nu$ and integrate by parts twice — once in $x$, once in $\tau$:

$$
\begin{aligned}
\int\!\mathrm{d}^4x\;\psi_\nu\,\partial_\mu T^{\mu\nu}
&=-\int\!\mathrm{d}^4x\;\big(\partial_\mu\psi_\nu\big)T^{\mu\nu}
=-m\int\!\mathrm{d}\tau\;\dot z^\mu\dot z^\nu\,\partial_\mu\psi_\nu(z)\\[4pt]
&=-m\int\!\mathrm{d}\tau\;\dot z^\nu\,\frac{\mathrm{d}}{\mathrm{d}\tau}\Big[\psi_\nu\big(z(\tau)\big)\Big]
=+m\int\!\mathrm{d}\tau\;\ddot z^\nu\,\psi_\nu\big(z(\tau)\big)
\end{aligned}
$$

(the third step is just the chain rule, $\dot z^\mu\partial_\mu=\mathrm{d}/\mathrm{d}\tau$). Since $\psi_\nu$ was arbitrary,

$$\partial_\mu T^{\mu\nu}_{\rm matter}(x)=m\int\mathrm{d}\tau\;\ddot z^\nu\;\delta^{(4)}\big(x-z(\tau)\big)$$

A free particle has $\ddot z^\nu=0$ and its stress-energy is conserved. **An accelerating particle does not**, because momentum is flowing into it from whatever pushes it.

**Our own theory makes the particle accelerate.** That is the entire purpose of $\mathcal{L}_{\rm int}$. Feeding the point-particle $T^{\mu\nu}$ into the coupling gives the worldline action

$$S=\frac{m}{2}\int\mathrm{d}\tau\;\big(\eta_{\mu\nu}+\kappa\,h_{\mu\nu}(z)\big)\dot z^\mu\dot z^\nu$$

and varying with respect to $z^\alpha$ gives, to first order in $\kappa$,

$$\ddot z_\alpha=-\,\frac{\kappa}{2}\Big(\partial_\mu h_{\alpha\nu}+\partial_\nu h_{\alpha\mu}-\partial_\alpha h_{\mu\nu}\Big)\dot z^\mu\dot z^\nu\;\equiv\;-\,\Gamma^{(1)}_{\alpha\mu\nu}\,\dot z^\mu\dot z^\nu\;\neq\;0$$

**Now combine.** Substituting into Step 1 and using the delta function to evaluate $\Gamma^{(1)}$ at $x$,

$$\boxed{\;\partial_\mu T^{\mu\nu}_{\rm matter}=-\,\Gamma^{(1)\nu}{}_{\mu\rho}\,T^{\mu\rho}=\mathcal{O}(\kappa)\;\neq\;0\;}$$

in flat contradiction with the requirement of the previous box. 

In the Newtonian limit, with $$\kappa h_{00}=-2\Phi$$ one has $\Gamma^{(1)i}{}_{00}=\partial_i\Phi$, so for dust of density $\rho$ the spatial components read $$\partial_\mu T^{\mu i}\simeq-\rho\,\partial_i\phi$$. The right-hand side is just the gravitational force per unit volume: the "non-conservation" is the wholly banal fact that when an apple falls its momentum increases.

Two things are worth noticing. First, $$\Gamma^{(1)}_{\alpha\mu\nu}$$ is precisely the Christoffel symbol of $$g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}$$ to first order — our flat-space field theory has handed us a piece of Riemannian geometry we never asked for. Second, the violation is $\mathcal{O}(\kappa)$, which is exactly the order at which the field equation $$G^{(1)}=\tfrac{\kappa}{4}T$$ lives. There is therefore no regime in which the theory is both non-trivial and consistent: switch off the coupling and matter moves freely but gravity does nothing; switch it on and the source stops being conserved.

</details>

So, the linear theory is inconsistent with its own predictions. The only way out is to account for the fact that **gravity gravitates**, i.e. that gravitational field energy is itself a source of gravity — the *strong* equivalence principle. The only way out is to add to the source the stress-energy of the gravitational field itself:

$$\mathcal{L}_{\rm int} = \frac{\kappa}{2}h_{\mu\nu}\left(T^{\mu\nu}_{\rm matter} + T^{\mu\nu}_{(h)}\right)$$

But $$T^{\mu\nu}_{(h)}$$ is quadratic in $h$, so this new cubic term modifies $$T^{\mu\nu}_{(h)}$$ itself, requiring a quartic term, and so on — an infinite tower of corrections. Remarkably, **the series can be summed in closed form, and its sum is exactly the Einstein-Hilbert action** with

$$g_{\mu\nu} = \eta_{\mu\nu} + \kappa\, h_{\mu\nu}$$

This is the **graviton bootstrap**, first attempted by [Gupta (1954)](https://doi.org/10.1103/PhysRev.96.1683) and [Kraichnan (1955)](https://doi.org/10.1103/PhysRev.98.1118), given its most elegant treatment by [Deser (1970)](https://arxiv.org/abs/gr-qc/0411023). Feynman independently reconstructed the argument in his Lectures on Gravitation.

<details markdown="1">
  <summary><strong>More on bootstrap</strong></summary>

**The iteration, concretely.** Start from $$\mathcal{L}^{(2)}=\mathcal{L}_{\rm FP}+\tfrac{\kappa}{2}h_{\mu\nu}T^{\mu\nu}_{\rm matter}$$. Compute the stress-energy tensor $$T^{\mu\nu}_{(h,2)}$$ of the field $h$ itself from this Lagrangian: it is **quadratic** in $h$. Adding it to the source produces a new term $$\tfrac{\kappa}{2}h_{\mu\nu}T^{\mu\nu}_{(h,2)}$$, which is **cubic** in $h$. But changing the Lagrangian changes the stress-energy tensor, so the new $$T^{\mu\nu}_{(h,3)}$$ has a cubic piece, which demands a **quartic** term, and so on:

$$\mathcal{L}=\underbrace{\mathcal{L}^{(2)}}_{\mathcal{O}(h^2)}+\underbrace{\kappa\,\mathcal{L}^{(3)}}_{\mathcal{O}(h^3)}+\underbrace{\kappa^2\mathcal{L}^{(4)}}_{\mathcal{O}(h^4)}+\cdots$$

Each order is fixed by the requirement that the source be conserved at the previous order. The claim is that this infinite series resums to

$$S=\frac{1}{2\kappa^2}\int\mathrm{d}^4x\;\sqrt{-g}\,R[g]\;+\;S_{\rm matter}[g,\psi],\qquad g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}$$

**Deser's shortcut.** Written this way the argument is a nightmare of index algebra, and it was originally carried out order by order by Gupta and Kraichnan. Deser's insight was to change variables first: work in the **first-order (Palatini) formalism**, where the metric density $$\mathfrak{g}^{\mu\nu}=\sqrt{-g}g^{\mu\nu}$$ and the connection $$\Gamma^{\rho}{}_{\mu\nu}$$ are varied independently. In those variables the Einstein-Hilbert action is only *quadratic* in the connection, the iteration **terminates after a single step**, and the whole infinite tower collapses to one correction. That is why his paper is three pages long and the earlier ones are not. This is the same Palatini formulation discussed in the [alternative formulations class](./altform_GR.md).

What survives all of this is the weaker but still remarkable statement: *a self-consistent interacting theory of a massless spin-2 field must have a nonlinearly realised gauge symmetry, and general relativity is the simplest theory that does.* That is the content of the Weinberg-Deser theorem.

</details>

**And notice what happened to the gauge symmetry.** The linear symmetry $$h_{\mu\nu}\to h_{\mu\nu}+2\partial_{(\mu}\xi_{\nu)}$$ is nothing but the infinitesimal version of a coordinate change $$x^\mu \to x^\mu - \kappa\,\xi^\mu$$ acting on $$g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}$$. At the nonlinear level it becomes the full **diffeomorphism invariance** of GR. So: Diffeomorphism invariance is not an extra geometric postulate. It is the gauge symmetry that any consistent interacting massless spin-2 field theory is forced to have. It thus works in both directions: start from geometry and you *derive* that the graviton is spin 2; start from spin 2 and you *derive* geometry.

This leads us to introduce the so-called **Weinberg uniqueness theorem** or the **Weinberg-Deser** theorem: GR is the unique consistent (no-ghost) field theory for a massless spin two field on a flat four dimensional space-time. This is an extremely strong statement and we see that GR is really not a random theory to describe gravity, it is a natural one to reach when coming from the field theory angle. We will rediscuss it [later](./Lovelock_thm.md) in the context of modified gravity.

Now, where did the flat background go? This is the crucial conceptual point, and the answer to the question posed in the introduction. We *started* with a flat background $\eta_{\mu\nu}$ and a field $h_{\mu\nu}$ living on it. But the bootstrap told us that every matter field couples not to $\eta$ but to the combination $g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}$. **Rods, clocks, light rays, and every experiment we can perform therefore measure $g$, never $\eta$.** The flat background is *unobservable in principle*: it is pure gauge, a scaffolding we erected and can now remove. This is why the two descriptions are two faces of one coin — not two theories that happen to agree, but one theory in two sets of variables.

That said, the split is not entirely innocent, and it might break down:

- **Topology and global structure are lost.** Writing $g=\eta+\kappa h$ presupposes $M \simeq \mathbb{R}^4$. The field-theory formulation cannot describe a spatially closed universe, the interior of a black hole, or a space-time with non-trivial topology. Every result that depends on *global* structure — the singularity theorems of Penrose and Hawking, the causal structure of horizons, black hole thermodynamics, the Gauss-Bonnet theorem — is invisible in the perturbative language.
- **The expansion may not converge.** $\kappa h$ is not small near a horizon or a singularity.
- **The choice of $T_{\mu\nu}^{(h)}$ is not unique**, and different choices give different-looking "gravitational energy" — this is known as the pseudo-tensor problem.

So the correct statement is: **the field-theoretic and geometric formulations agree on everything local and perturbative, and the geometric one is strictly more general globally.** Thus GR is not "just" a spin-2 field theory; but this perturbative approach is where gravitational waves, gravitons, quantum corrections, and entire groups of modified-gravity theories come from. More than anything, the Fierz-Pauli action will be of first interest when considering [massive gravity](./massive-gravity.md), because it is the proper framework in order to "give a mass to the graviton".

## Newton-Cartan: even Newtonian gravity is about curved space-time

Now that we saw that GR can be seen somehow as a theory of fields, we wrap up this lecture by discovering that 
**Newtonian gravity can be written, exactly and without approximation, as a geometric theory of curved space-time.** This is the *Newton-Cartan* formulation (See for example [Schwartz (2023)](https://www.pschwartz.de/Newton--Cartan_gravity.pdf), ch. 4 of [Malament (2012)](https://press.uchicago.edu/ucp/books/book/chicago/T/bo12893557.html) or the [dedicated video class](https://www.youtube.com/watch?v=IBlCu1zgD4Y&list=PLmsIjFudc1l2wDQ_ekx6iLtqcWJQQvOsw&index=15) from F.P. Schuller).

In order to get a geometric version of Newtonian theory, one must clearly curve space-time (and mostly time), not space alone. We already had a hint for this from the Newtonian limit of General relativity in which the Newtonian potential is the time component of the metric. The geometrization of Newtonian gravity allows to understand the usefulness of Newton's first law (which does not reduce trivially to Newton second law with no force) and define what "straight line" means: gravity is not a force, it's a straight line in a curved space-time. While the trajectory of a body attracted by gravity appears as straight in space, it accelerates, and it is thus curved in space-time.

<details markdown="1">
  <summary><strong>Newtonian gravity as geodesic motion</strong></summary>

This is inspired from [Schuller (2015)](https://www.youtube.com/watch?v=IBlCu1zgD4Y) (see the associated [lecture notes](https://docs.wixstatic.com/ugd/6b203f_dc24fe06fbe14a71ae32a1ad031e1928.pdf?index=true)). The basic idea is to take the Newtonian limit of GR, already discussed in our [first lecture](./foundations-GR.md), and look at it the other way around.

Consider a three dimensional manifold with a chart $x^i$. Newton's second law is then

$$F^i = m\,\ddot{x}^i .$$

If we now consider the force of gravitation $F^i = m\,g^i$, Newton's law becomes $\ddot{x}^i - g^i = 0$. There is no way to read this as a geodesic equation. The obstruction is worth spelling out, because it tells us exactly what is missing: a geodesic equation reads $$\ddot{x}^i + \Gamma^{i}{}_{jk}\,\dot{x}^j\dot{x}^k = 0$$, whose inhomogeneous term is **quadratic in the velocity**, whereas $g^i$ is velocity-independent. No choice of $$\Gamma^{i}{}_{jk}(x)$$ can reproduce $$\ddot{x}^i = g^i$$ for *all* initial velocities. We are missing a "velocity" that is always equal to $1$.

We now move to a four dimensional space-time with chart $x^\alpha = (t,x,y,z)$, and we parametrise worldlines by $t$ itself. This immediately gives us the missing ingredient: the fourth component $x^0 = t$ satisfies $\dot{x}^0 = 1$ and $\ddot{x}^0 = 0$ identically.[^param] We can now rewrite Newton's second law for gravity as a genuine geodesic equation,

$$\ddot{x}^\alpha + \Gamma^{\alpha}{}_{\beta\gamma}\,\dot{x}^{\beta}\dot{x}^{\gamma} = 0 ,$$

with

$$\Gamma^{i}{}_{00} = -\,g^i$$

and all other components chosen to vanish. Indeed the $\alpha = i$ equation becomes

$$\ddot{x}^i + \Gamma^{i}{}_{00}\,\dot{x}^{0}\dot{x}^{0} = \ddot{x}^i - g^i = 0 ,$$

while the $\alpha = 0$ equation is the identity $\ddot{x}^0 = 0$. So adding a time dimension to space allows us to interpret gravity as geodesic motion. We can therefore stop thinking of gravity as a force, and think of it instead as a probe of space-time curvature, defining the **straight lines** and thus the inertial motion of a body on which no force acts.

Computing the Riemann tensor associated with this choice of Christoffel symbols gives

$$R^{j}{}_{0i0} = -\,\partial_i g^j ,$$

all other independent components vanishing. Three comments, in increasing order of importance:

1. The fact that the Riemann tensor is **not zero** shows that this is not a coordinate artefact that could be removed by an appropriate choice of chart (remember that $\Gamma$ is not a tensor, while $R$ is). Gravity is *really* curvature, not a bookkeeping trick.
2. $R$ here is the spatial derivative of the gravitational field, so it quantifies **tidal forces**, exactly as it does in GR. And indeed only tidal forces are chart-independent: a uniform $g^i$ gives $R = 0$ and can be transformed away — this is the equivalence principle, visible in one line.
3. Every non-vanishing component carries the index $0$ at least twice. **The curvature is purely temporal**; the purely spatial components $R^{i}{}_{jkl}$ all vanish, which is the precise sense in which "one curves time, not space".

One last bonus. Contracting to get the Ricci tensor, $R_{\mu\nu} = R^{\lambda}{}_{\mu\lambda\nu}$, the only surviving component is

$$R_{00} = R^{j}{}_{0j0} = -\,\partial_j g^j = -\,\vec\nabla\cdot\vec{g} .$$

But Newton's law of gravitation says precisely $\vec\nabla\cdot\vec{g} = -4\pi G\rho$ (equivalently $\Delta\phi = 4\pi G\rho$ with $\vec g = -\vec\nabla\phi$). So $R_{00} = 4\pi G\rho$. Keep this result in a corner of your mind: we will meet it again below, promoted to a covariant field equation.

</details>

A **Newtonian space-time** or **Galilean manifold**[^gal]  is a four dimensional smooth manifold $M$, just like in GR, but equipped with different structures. As a reminder, the structure of GR requires solely the doublet ($M,g$), and the connection $\nabla$ is entirely defined by $g$. Newton geometry needs additional structure in order to define the **absolute space** and **time**. In a sense this is another way to see why GR is background independent or lacking absolute/rigid geometrical structures, while Newtonian gravity isn't. 

So, a Newtonian space-time is the given of a four dimensional smooth manifold $M$[^3], a connection $\nabla$ and a specific function $t$ called **the absolute time**. **Absolute space** is then simply the set of all the manifold point having the same value for the $t$ function. A metric $k^{\mu\nu}$ is further introduced to measure distances on slices of absolute space only.
From the function $t$ one can build everywhere the one-form $\tau = \text{d}t$ called the **clock form**.[^clock] If you are uneasy with the concept of one-form, simply understand $\tau$ as a special covector $\tau_\alpha= \frac{\partial t}{\partial x^\alpha}$ defined everywhere by the function $t$ in space-time. $k^{\mu\nu}$ satisfies the orthogonality condition $$k(\tau)=k^{\mu\nu}\tau_\nu=0$$, such that in the special chart $(t,x,y,z)$ where the $x^0$ component matches with the function $t$, $\tau_\alpha=(1,0,0,0)$ and $k^{\mu\nu}=\text{diag}(0,1,1,1)$. The one-form $\tau$ defines the time orientation on $M$. For a vector $X$ in $T_pM$, if $\tau(X)=\tau_\alpha X^\alpha >0$, $X$ is said to be future directed, if $\tau(X)=0$ it is said to be spatial, and if $\tau(X)<0$ past directed. 

Now, a Newtonian space-time must satisfy:

- $\tau \neq 0$ everywhere in $M$. This makes sure that "time never stops", and that the absolute spaces are genuine three dimensional hypersurfaces which foliate $M$: every event belongs to one and only one absolute space.
- $\nabla \tau = 0$ everywhere in $M$, i.e. $$\nabla_\mu \tau_\alpha = \partial_\mu\tau_\alpha - \Gamma^{\lambda}{}_{\mu\alpha}\tau_\lambda = 0$$. This ensures that "time always flows at the same pace": parallel transport does not change the duration $\tau(X)$ assigned to a vector.
- $\nabla k = 0$ everywhere in $M$, i.e. $$\nabla_\mu k^{\alpha\beta} = \partial_\mu k^{\alpha\beta} + \Gamma^{\alpha}{}_{\mu\lambda}k^{\lambda\beta} + \Gamma^{\beta}{}_{\mu\lambda}k^{\alpha\lambda} = 0$$. The connection is metric compatible in space: the Euclidean length of a parallel-transported spatial vector is conserved.
- $\nabla$ is torsion-free (its coefficients in a coordinate basis satisfy $$\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$$).

These are the equivalent of the "S" axioms we introduced for GR, describing the structure of Newton-Cartan theory. Note that while GR has $(M,g)$ as a structure, Newton-Cartan requires the quadruplet ($M, t/\tau, k, \nabla$). $\nabla$ was entierly fixed by $g$ in GR, it is not in Newton-Cartan theory where $\nabla$ is a free field (dynamical degree of freedom) of the theory. 

Newton's two laws, which would be the "D" kind of axioms, are then:

- A free particle follows a geodesic of $\nabla$: the tangent vector $v$ to its trajectory obeys $\nabla_v(v)=0$ and the velocity is future directed $\tau(v)>0$.
- If a particle deviates from this trajectory, it is subject to a force $F$ vector field, such that $$\nabla_v(v)=F/m$$ and $F$ is a spatial vector $\tau(F)=0$.

As promised, Newton first and second law are now completely distinct statements in Newton-Cartan theory. As in GR, gravity is not a force, it is what defines inertial motion. We note that this dynamics is exactly what we would get in GR with the continuity equation for a point particle subject to some external forces, except for the requirements set by the additional structure $\tau$ which does not exist in GR. In fact these two Newton laws can be reduced to 

$$R_{\mu\nu}= 4\pi G \rho \tau_\mu \tau_\nu $$

the **geometrized Poisson equation**, with $\rho$ the mass density. The source is thus a single scalar, projected on the time direction by $\tau_\mu\tau_\nu$. In Newtonian gravity, *mass* gravitates, not energy.[^trautman] Newton-Cartan theory closes cleany the loop started when exploring the Newtonian limit of GR. It provides a fully complete geometric theory of gravity which can be obtained as a limit of GR (we refer again to [Malament (2012)](https://press.uchicago.edu/ucp/books/book/chicago/T/bo12893557.html) for proper prooves of all these claims).

<details markdown="1">
  <summary><strong>Newton-Cartan equations in a special chart</strong></summary>

Let us now check all of this explicitly, in the special chart $(t,x,y,z)$ where $\tau_\alpha = (1,0,0,0)$.

Since $\tau_\alpha$ is constant, $\partial_\mu\tau_\alpha = 0$ and the condition $\nabla\tau = 0$ becomes simply

$$-\,\Gamma^{0}{}_{\mu\alpha} = 0 ,$$

i.e. **no Christoffel symbol with an upper time index survives**. Similarly, $\nabla k= 0$ with $k^{\mu\nu} = \mathrm{diag}(0,1,1,1)$ forces (lowering spatial indices with $\delta$)

$$\Gamma^{i}{}_{\mu j} + \Gamma_{j}{}_{\mu i} = 0 ,$$

i.e. antisymmetry in the two *spatial* indices. Combined with torsion-freeness this kills $\Gamma_{i}{}_{jk}$ outright — it would have to be symmetric in $(jk)$ and antisymmetric in $(ij)$ at once, which forces it to vanish — and leaves $\Gamma^i_{0j} = -\Gamma^j_{0i}$ free. That surviving antisymmetric piece is nothing but the **Coriolis term** and setting it to zero is the choice of a **non-rotating** frame. Hence **fictitious forces** of Newtonian theory are part of the connection terms appearing in the geodesic equation.
What is then left completely unconstrained is exactly $$\Gamma^{i}{}_{00}$$, which we may always write as $$\Gamma^{i}{}_{00} = g^i = \delta^{ij}\partial_j\Phi$$ for some function $\Phi$ — called the **Newtonian potential**, appearing here as the *only* free degree of freedom of the geometry.

The first Newton law $\nabla_v v = 0$ splits into a time component and a space component. The time component is

$$\ddot{x}^0 + \Gamma^{0}{}_{\mu\nu}\dot{x}^\mu\dot{x}^\nu = \ddot{t} = 0 ,$$

which is *not* an equation of motion but a statement about the parameter: absolute time is automatically an affine parameter along every geodesic. This is the geometric content of "$t$ is absolute". The space component is

$$\ddot{x}^i + \Gamma^{i}{}_{00}\,\dot{t}^{\,2} = \ddot{x}^i + \delta^{ij}\partial_j\Phi = 0 \qquad \Longleftrightarrow \qquad \ddot{\vec{x}} = -\vec\nabla\Phi ,$$

which is free fall in the potential $\Phi$. The second Newton law $\nabla_v v = F/m$ adds the source term back on the right,

$$\ddot{x}^i = -\,\delta^{ij}\partial_j\Phi + \frac{F^i}{m} ,$$

and the condition $\tau(F) = 0$, i.e. $F^0 = 0$, is what guarantees that the time equation $\ddot{t} = 0$ is left alone: no force can ever change the flow of absolute time. In GR, by contrast, a force *does* affect the relation between coordinate time and proper time — this single line is where the two theories part ways.

Finally, with only $\Gamma^{i}{}_{00}$ non-zero, all quadratic $\Gamma\Gamma$ terms in the Riemann tensor drop out and

$$R_{00} = \partial_\mu\Gamma^{\mu}{}_{00} - \partial_0\Gamma^{\mu}{}_{\mu 0} = \partial_i\left(\delta^{ij}\partial_j\phi\right) = \Delta\Phi ,$$

every other component vanishing. Since $\tau_\mu\tau_\nu$ has $1$ as its only non-zero component, the covariant field equation collapses to the single scalar statement

$$\Delta\Phi = 4\pi G\rho ,$$

which is Poisson's equation. The circle is closed: Newton-Cartan is Newtonian gravity, exactly, written in a language where gravity is curvature.

</details>

[^gal]: As expected, Galilean transformation will play a special role in such manifold, as they do in classical mechanics. We will not enter in the details here. See again [Schwartz (2023)](https://www.pschwartz.de/Newton--Cartan_gravity.pdf) or ch. 4 of [Malament (2012)](https://press.uchicago.edu/ucp/books/book/chicago/T/bo12893557.html).

[^param]: This is not an innocent choice of parameter but the whole trick. In three dimensions there is no coordinate that automatically advances at unit rate; promoting $t$ from parameter to coordinate is what supplies the "$\dot{x}^0\dot{x}^0 = 1$" that turns a velocity-independent force into a velocity-quadratic geodesic term.

[^3]: In this class and the other we neglected to mention that $M$ comes equipped with a topology $\mathcal{O}$ and atlas $\mathcal{A}$ as Schuller does. This is always implicitely assumed to be true.

[^clock]: $\tau$ is arguably more fundamental than the function $t$ as it can be defined globally and is often used as the building block of Newton-Cartan theory.

[^trautman]: Strictly speaking this equation is necessary but not sufficient: it only constrains the Ricci part of the curvature. Trautman showed that one must add two conditions on the full Riemann tensor — spatial flatness $R^{\mu\nu}{}_{\rho\sigma} = 0$ and the symmetry $$R^{\mu}{}_{\nu}{}^{\rho}{}_{\sigma} = R^{\rho}{}_{\sigma}{}^{\mu}{}_{\nu}$$ (indices raised with $k$) — for the theory to be *equivalent* to Newtonian gravity rather than merely to contain it. See e.g. ch. 4 of [Malament (2012)](https://press.uchicago.edu/ucp/books/book/chicago/T/bo12893557.html).

## Conclusion: fields or geometry?

We saw that modern physical theories often have multiple faces, associated with different formalisms. These multiple faces allow us to interpret and understand them differently and some may be preferred for some specific practical applications. In particular, all **contemporary theories**, that is general relativity and gauge theories, can be seen either as field theories, or geometrical theories talking about motions in curved spaces. This is very relevant for our class, as when we will explore new theories beyond general relativity to be proposed as alternatives, we might want to start from its field formulation instead of its geometric one.

Of course, you may think that the details of these preliminary are a bit long and not absolutely needed for a course in modified gravity. I however believe that understanding deeply this class and the previous ones will give you a deep understanding of gravity that nothing else would.

All modern physics theories admit a geometric formulation, which is often very abstract at first and then extremely enlightening. For example:

- Thermodynamics and contact geometry
- Classical mechanics and symplectic geometry
- Quantum mechanics and Hilbert spaces, Berry phases and geometric quantizations
- Modern gauge theories and associated fiber bundles (and jets bundles)
- ...

All these topics are very difficult and honestly more targeted for mathematicians than physicists. However, understanding all these faces is the only way to become a real expert of a field. I am myself profoundly interested by the geometrical aspects of gauge theories and the parallels that can be done with general relativity. On this topic, you can have a look at the first version of my [mémoire](https://leovacher.github.io/files/memoire_new.pdf). 

## Further reading and watching

- R. P. Feynman, *Lectures on Gravitation* - 1962-63 - Addison-Wesley (1995).
- S. Weinberg, The quantum theory of fields Vol. 1 to 3. - 1995 - Cambridge University Press (2005). 
- N. Deruelle, [*Nordström's scalar theory of gravity and the equivalence principle*, Gen. Rel. Grav. **43** (2011) 3337](https://arxiv.org/abs/1104.4608).
- [Modified gravity — Rachel Rosen - Youtube lectures](https://www.youtube.com/watch?v=1THLppx96T8).
- [The WE-Heraeus International Winter School on Gravity and Light - F.P. Schuller - Youtube lectures](https://www.youtube.com/watch?v=IBlCu1zgD4Y&list=PLmsIjFudc1l2wDQ_ekx6iLtqcWJQQvOsw&index=1).
