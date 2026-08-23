---
layout: default
title: Foundations of general relativity
parent: cosmo
---

# What to modify? Foundations of general relativity

If we want to study modified gravity, we must first understand what is there to modify. Our best description of gravity so far is given by general relativity (GR). As we will further see, GR is at the heart of modern cosmology. From its formulation in 1915 to the first direct detection of gravitational waves a century later, it has proven to be a remarkably successful theory, with applications ranging from solar system dynamics to the large-scale structure of the universe. At its core lies a beautiful geometric picture: spacetime curvature governs the motion of matter, and matter in turn shapes the curvature of spacetime.
As we will see however, despite its beauty, GR is only one of many possible theories of gravity, and some alternatives might be preferred either from theoretical grounds, or forced on us by future experiments. 
Let us try to unpack the conceptual foundations of GR and try to identify a minimal set of axioms at its base. These axioms will be the natural candidates to drop if we want to look for alternative theories of gravitation beyond general relativity. 

## Some conceptual motivations for GR

Before stating a list of fundamental axioms of general relativity, we must first review some of the conceptual and experimental motivations for this theory that lead to the geometrisation of space-time. 

### What to ask of a gravity theory?

Before getting too technical, let's first list some simple and intuitive requirements that we should ask to a theory that pretend to describe gravity. These are inspired from the so-called "Dicke framework" discussed in [Will (2018)](https://www.cambridge.org/core/books/theory-and-experiment-in-gravitational-physics/8A5923C93E43FAFDEC17C3E0FD01A623).
Let's then say that gravitation, at minimum, should be described in our theory as:

- A **long range** force.
- It should act between **masses**.
- It should be **attractive**.
- It should reproduce **Newton law of gravitation** under some suitable limits:

  $$\boxed{V_{\rm int}(r) = -\frac{G m_1m_2}{r}}$$

  where $G$ is the so-called **Newton gravitational constant**, measured to be $G=6.67430(15) \times 10^{-11}$ m$^{3}\,$.kg$^{−1}\,$⋅s$^{−2}$ (Value from [Codata 2022](https://physics.nist.gov/cgi-bin/cuu/Value?bg)).
- it should reproduce **special relativity** when turned off (as special relativity has been tested and never contradicted up to an extremely high precision, more on this later). 
- It should be **self-consistent** (one should not lead to two contradictory statements or predictions from the same principles) and as **complete** as possible (able to describe as many experimental phenomena as possible).

Newtonian mechanics does not fulfill all these criteria, simply because it does not reproduce special relativity when gravitation is turned off (which in this context clearly means that the gravitational force $\vec{F}_G$ is absent in the sum of forces applying to an object).
GR is one of the theories that satisfy all these criteria, but as we will see, it is not the only one.

### The Einstein equivalence principle

On top of the previous requirements, we can ask that gravity should not only act between masses, but that it should act **universally** between them, that is, it should induce a motion on all massive objects, independently of the value of their mass. Such an additional constraint is forced on us by experiment, and can be promoted to a principle as we will discuss now. Actually, at least three different principles can be built out of this universality statement, known as "equivalence principles".

An equivalence principle is a building block of a theory (principle are like "axioms" in mathematics, they can not be proven and the whole theory is built on them) stating the equivalence between two apparently different concepts or physical situations. They play a very important role in the study of gravitation and multiple different such principles can be proposed (for a review see e.g. [Di Casola et al (2015)](https://arxiv.org/abs/1310.7426)). In this class, we will focus on three of them which are arguably the most important: the weak, the Einstein and the strong equivalence principles. 

First, let's start with a well known experimental fact, which represent the main motivation for the introduction of equivalence principles:

- **Universality of free-fall (UFF)**: as far as our measurements can go, we witness that all free test bodies fall identically in a gravitational field, independently of their shape, state or composition. 

Every word is important in this statement:
By **test particle** here, we mean a particle small and light enough such that its own gravitational field can be neglected, as well as tidal forces which could be applied to it. By **free** we mean that no other force than gravity is applied on the test body. By **state** here, we mean any possible self-motion, like spinning on itself or properties as electric charge.  We will discuss in [a following lecture](../modified_gravity/validation_GR.md) how this empirical fact can be verified up to a very high accuracy using a great variety of experiments. If we accept that the UFF is exactly true, and we decide to make it a principle to construct a theory, we introduce the

- **Weak equivalence principle (WEP):** UFF is always satisfied.

While UFF and WEP are sometimes conflated, we make here a distinction between the UFF as an experimental fact, and the WEP as a principle.

If we consider the WEP in the context of Newtonian theory of point mechanics, we can assert the equivalence between the inertial mass (appearing in $\sum_i\vec{F}=m_i\vec{a}$) and the gravitational mass (appearing in the weight $\vec{P}=m_g\vec{g}$) . This equivalence of concept translates into a mathematical equality $m_i=m_g$, such that the second law for a free-falling body gives exactly $\vec{a}=\vec{g}$ for any body, no matter its composition.

The WEP can be extended with other principles in order to build the so-called **Einstein equivalence principle (EEP)**, which is a useful extension for relativistic theories. The EEP is composed of three different assertions:

1. **Weak equivalence principle (WEP)** is valid.
2. **Local position invariance (LPI):** the outcome of any local non-gravitational experiment is independent of where and when in the Universe it is performed. As such, there is no "preferred" event in space-time in which laws of physics would be different.
2. **Local Lorentz invariance (LLI):** the outcome of any local non-gravitational experiment (i.e. any "small scale" experiment in an inertial/free falling frame) is independent of the velocity of the reference frame in which it is performed. Thus, inertial frames are all equivalent. 

It can be shown that the EEP implies the local equivalence of an accelerated frame upward and a frame at rest in a gravitational field. Furthermore, it implies the local equivalence of a free-fall frame with an inertial frame of special relativity. This is one of the well known intuition that lead Einstein to formulate general relativity, by asserting that gravity is some kind of "inertial force".

The emphasis on "local non-gravitational experiment" in the definition of LPI and LLI might seem cumbersome, but it is actually necessary. Dropping it would lead to a stronger principle, known as the strong equivalence principle (which we will discuss below).

The three "sub-principles" of the EEP are related through **Schiff's conjecture** which is the hypothesis that any self-consistent theory of gravity that embodies WEP necessarily embodies LPI and LLI and thus the full EEP (See [Schiff 1960](https://einstein.stanford.edu/content/sci_papers/papers/Schiff-Expt_Tests_GR-AJP-1960.pdf) and [Coley 1982](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.49.853)). The study of Schiff's conjecture and its domain of validity was and is of great importance on the debates on the foundations of gravitational physics. While it seems to be valid in generic cases, some counter-examples have been found. As a general principle: if one explore a specific modified theory of gravity in which one of the three sub-principle is violated, it is almost certain that the other two are equally violated in a related way. As such, one must use the bundle of data constraining each sub-principle (which we discuss in the next lectures) in order to derive complete and consistent constraints of a given theory. For a discussion of Schiff's conjecture, see also section 2.4 of [Will (2018)](https://www.cambridge.org/core/books/theory-and-experiment-in-gravitational-physics/8A5923C93E43FAFDEC17C3E0FD01A623) and [Ni 2015](https://arxiv.org/abs/1512.08426).

### General covariance, diffeomorphisms and relativity principle

One of the motivation often invoked for general relativity, is the desire to generalize the results of special relativity not only to inertial frames, but to any possible frames, and especially to accelerated frames. 

At the heart of relativity is the so-called:

- **Relativity principle**: The laws of physics should be independent of the frames in which they are formulated.

The ambition of special relativity was arguably to apply the relativity principle to inertial frames, that is to treat all inertial frames, that is all frames related to one another by linear motion at constant velocity, as equivalent. The relativity principle applied to inertial frames lead to the conclusion that the speed of light must be the same in all frames, such that it is impossible to say whether or not one is in **absolute motion**. Furthermore, it lead to a first geometrical conclusion that space and time should be merged into a single realm: space-time equipped with an invariant length given by the rigid Minkowski metric $\eta$ (a Lorentzian metric, in the sense introduced below, that happens to be constant everywhere) which allows to compute the length of any four dimensional vector $v$ as $$\eta(v,v)= -(v^0)^2 + \sum_i (v^i)^2.$$

The big revelation leading to general relativity is then the EEP's assertion that a gravitational field is *locally indistinguishable* from an accelerated frame: gravity can always be transformed away at a
point by going to free fall, and free-falling frames are identified with the inertial frames of special relativity. This suggests that gravity is not a force propagating on spacetime, but part of the inertial structure of spacetime itself — a property of geometry. Historically, Einstein phrased this as the demand to "extend the relativity principle to
accelerated frames". Taken literally this is misleading: special relativity describes accelerated observers perfectly well (e.g. Rindler coordinates for uniform acceleration,
see [the physics FAQ](https://math.ucr.edu/home/baez/physics/Relativity/SR/acceleration.html)), and even in general relativity acceleration remains absolutely detectable — an accelerometer in free fall reads zero, an accelerated one does not. What the heuristic actually led to,
as we discuss below, is something deeper: the removal of any fixed background structure (like the rigid $\eta$ of special relativity) singling out the inertial frames a priori —
in GR they are determined by the dynamical field $g$ itself.

The generalisation of the relativity principle, embodied through the so-called principle of **general covariance** takes a very practical meaning:

- The relevant physical quantities should be expressed by special quantities (known as scalars and tensors which we will define below), such that the relations between such quantities remain valid in any arbitrary frame or coordinatization of space-time.

While general covariance was a powerful guide in the historical building of GR, its status of a foundational block is largely contested. Indeed, Erich Kretschmann in 1917 objected, already at the time, that any physical theory can be rewritten in a generally covariant, tensorial form by suitable (if sometimes cumbersome) mathematical reformulation, without changing any of its observable content -- making general covariance, by itself, an empty physical requirement. For more discussion on the topic of general covariance, see for example [Norton 1993](https://sites.pitt.edu/~jdnorton/papers/decades.pdf) and [Ryckman 2024](https://plato.stanford.edu/entries/genrel-early/).

General covariance should not be confused with the closely related concept of **diffeomorphism invariance**, which is itself a deep feature of general relativity. We haven't yet set all the stage to discuss it in detail, but we give some extra details here for the curious reader. A **diffeomorphism** is a smooth, bijective map with smooth inverse -- that is an *active* relabelling of the points of space-time itself, as opposed to general covariance, which is merely a *passive* relabelling of coordinates at fixed points. Any diffeomorphism $$f$$ drags tensor fields along with it, producing new fields say $$\tilde{\psi}$$. Diffeomorphism invariance is the statement that if $(g,\psi)$ solves the fundamental equations of the theory (D1-D2 below), then so does $$(\tilde{g},\tilde{\phi})$$, for *any* diffeomorphism $f$. Unlike general covariance, this is not automatic for an arbitrary theory: it requires the complete absence of any fixed, non-dynamical background geometric structure that would fail to transform along with everything else -- exactly what is achieved by making $g$ itself fully dynamical, as a solution of the Einstein equation or Einstein-Hilbert action as we introduced below. This property of general relativity is known as **background independence**. 

## From motivations to axioms

Now, if EEP is true and added on top of our basic requirements for a theory of gravitation, it is possible to show that we become able to interpret gravitation as the motion of bodies on a curved space-time. While encompassing the EEP, this interpretation naturally extends the rigid geometric reading proposed by special relativity, as well as extending the relativity principle and the desire for relevant quantities to be tensorial objects.

This geometric interpretation can be encoded theoretically as follows:

- Space-time is endowed with a symmetric metric $g$, that is, at every point there exist a way to compute (four dimensional) "length" of any vectors as well as angles between vectors. As such $g$ defines a **geometry** at each point of space-time. Furthermore, $g$ is a **tensor** and thus has the right transformation properties for general covariance.
- According to the **WEP**, all bodies should fall identically. This can be interpreted geometrically if all trajectories of freely falling test bodies are geodesics of the unique metric $g$, that is they are the curves that minimizes (or maximize) the length given by $g$. Such curves are a property of the geometry itself and thus do not depend on the specific particle considered. 
- According to **LPI** and **LLI**, the non-gravitational experiments should be independent of the space-time location and velocity of the frame in which it is performed. This can be encoded geometrically as follows: in local freely falling reference frames, which are identified with the **inertial frames** of special-relativity, gravity becomes "invisible" and the non-gravitational laws of physics are those of special relativity. Only in such frames that the outcome of a non-gravitational experiment is guaranteed to reproduce exactly the predictions of special relativity. In these frames the metric $g$ must be $\eta$ and it should be possible to find such frame at every point of space-time. 

For a discussion of why the EEP is encoding this description, see Section 2.2 of [Will (2018)](https://www.cambridge.org/core/books/theory-and-experiment-in-gravitational-physics/8A5923C93E43FAFDEC17C3E0FD01A623). 
Every theory of gravity, which satisfy EEP and which can thus be interpreted geometrically as such, are called the
**metric theories of gravity**. As we will see, GR is only one of many metric theories of gravity. 

## A set of axioms for general relativity

### Structure:

So, if GR is only one possible theory of gravity, and even more, one of the restricted classes of **metric theory** of gravity, what makes it so special? Let us try to introduce a list of "axioms" which would be sufficient to uniquely define general relativity.

First, we can define some axioms about the need theoretical structure (S) used to define GR:

- (S1): Space-time is a smooth **four dimensional manifold** $M$.
- (S2): $M$ is equipped with a **Lorentzian metric tensor** $g$ at each point, allowing to define length and angles of tangent vectors. $g$ **is the unique dynamical quantity** of the theory associated with gravitation, which space-time evolution must be found.
- (S3): $M$ is equipped with a **connection** $\nabla$ defining parallel transport of tangent vectors. $\nabla$ is assumed to be **metric compatible** or **preserving** (S3a) and **torsion free** (S3b). It can be proved that such a choice leads to a **unique Levi-Civita connection**, which can be fully expressed in terms of the metric $g$ and its coordinate derivatives. All geometrical objects on space-time (tensors, spinors etc which could be associated to matter fields, see S4) are also transported through generalizations of $\nabla$.

These three items wrap up the geometrical project that we motivated in the previous section. We will further discuss later how these hypothesis are encoding the EEP. 
On top of that, we could add a fourth structural axiom, of a very different type: 

- (S4): Space-time contains matter. This matter is described by fields, the **matter fields** $\psi$, living on the curved space-time (which are locally irreducible representations of the Lorentz-group i.e. scalars, spinors, vectors, tensors etc). Collectively, their local energy density, momentum density, and stress at every point of space-time, are encoded in a symmetric $(0,2)$-tensor $T_{\mu\nu}$, called the **stress-energy tensor**.

<details markdown="1">
  <summary><strong>Complements: useful definitions and reminders</strong></summary>

General relativity is best understood using the abstract but beautiful language of differential geometry. For a first approach of these topics, we refer for example to [Baez & Muniain (1994)](https://pages.jh.edu/rrynasi1/PhysicalPrinciples/literature/Baez+Muniain1994GaugeFieldsKnots+Gravity.pdf), [Coqueraux (2016)](https://www.cpt.univ-mrs.fr/~coque/EspacesFibresCoquereaux.pdf) (for french speakers) and [Nakahara (2003)](http://www.stat.ucla.edu/~ywu/GTP.pdf). Here is a condensed review of the key concepts that you will encounter over and over again when studying GR:

- A smooth **manifold** $M$ of dimension $n$ (here $n=4$): a space that locally "looks like" $\mathbb{R}^n$, in the sense that around every point $p\in M$ one can find an open neighborhood mapped bijectively, through a **chart** (a local coordinate system $x^\mu$, $\mu=0,1,2,3$), onto an open subset of $\mathbb{R}^4$, in such a way that the transition between any two overlapping charts is smooth ($C^\infty$). This is the minimal structure needed to talk about differentiable functions, curves, and tangent vectors on space-time without assuming it sits inside some larger, "flat" ambient space.

- A map $f:M\to \mathbb{R}$ is called a **function** on $M$. It associates a real number $f(p)$ to each point $p$ of the manifold. The space of all smooth functions on $M$ is denoted $C^\infty(M)$.

- A map $\gamma: I\to M$, where $I\subseteq\mathbb{R}$ is an interval, is called a **curve** on $M$. It associates to each parameter value $\lambda\in I$ a point $\gamma(\lambda)$ on $M$; in a chart it is described by $n$ functions $x^\mu(\lambda)$.

- At each point $p\in M$, the set of all **tangent vectors** to all possible curves passing through $p$ form a real vector space of dimension $n$, the **tangent space** $T_pM$. A tangent vector $\gamma'$ to a curve $\gamma$, parametrized by the parameter $\tau$, at a point $p$ can be defined abstractly using the derivation operation as the map acting on a function $f$ as:
$$\gamma'(p)(f) := \frac{\text{d}}{\text{d}\tau}(f\circ\gamma)(p)$$.
Choosing a specific vector at each point of $M$ defines a **vector field**, understood as a section of the **tangent bundle**, $TM=\bigsqcup_{p\in M}T_pM$. $TM$ is itself a manifold of dimension $2n$. We write $\mathfrak{X}(M)$ the space of all possible vector fields. A vector field $v\in\mathfrak{X}(M)$ acts on a function $f\in C^\infty(M)$ to produce another function $v(f)\in C^\infty(M)$: in a chart $x^\mu$, the partial derivatives $\partial_\mu$ form a basis of $T_pM$ at every point, so $v=v^\mu\partial_\mu$ and $v(f)=v^\mu\partial_\mu f$. The tangent vector to a curve $\gamma$ of components $x^\mu(\tau)$ is
$$\gamma'(\tau) = \frac{\text{d}x^\mu}{\text{d}\tau}\,\partial_\mu.$$

- The dual vector space of $T_pM$ is the **cotangent space** $T_p^{\*}M$; its elements, called **covectors** (or **one-forms**), are linear maps $\omega:T_pM\to\mathbb{R}$. Collecting $T_p^{\*}M$ at every point gives the **cotangent bundle** $T^{\*}M=\bigsqcup_{p\in M}T_p^{\*}M$, and a smooth choice of covector at each point is a **one-form field** $\omega$. In a chart $x^\mu$, the differentials $\text{d} x^\mu$, defined by $dx^\mu(\partial_\nu)=\delta^\mu_\nu$, form the basis dual to $\partial_\mu$, so that $\omega=\omega_\mu\, dx^\mu$ and $\omega(v)=\omega_\mu v^\mu$. The differential of a function $f\in C^\infty(M)$, $df=\partial_\mu f\,dx^\mu$, is the simplest example of a one-form.

- A **tensor** of type $(r,s)$ at $p$ is a multilinear map taking $r$ covectors and $s$ vectors to a real number, i.e. it is a map  $$\underbrace{T^*_pM\otimes\cdots\otimes T^*_pM}_{r}\otimes\underbrace{T_pM\otimes\cdots\otimes T_pM}_{s}\to \mathbb{R}$$. We write it as an element of $$\underbrace{T_pM\otimes\cdots\otimes T_pM}_{r}\otimes\underbrace{T_p^{*}M\otimes\cdots\otimes T_p^{*}M}_{s}$$. A smooth assignment of such a tensor at every point of $M$ is a **tensor field**. In a chart it is written $$T=T^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s}\,\partial_{\mu_1}\otimes\cdots\otimes\partial_{\mu_r}\otimes dx^{\nu_1}\otimes\cdots\otimes dx^{\nu_s}$$. Vectors are $(1,0)$-tensors, one-forms are $(0,1)$-tensors, and the metric $g$ (introduced below) is an example of a $(0,2)$-tensor.

- A **metric tensor** $g$: a symmetric, non-degenerate $(0,2)$-tensor field, i.e. at every point $p$ a bilinear symmetric form $g_p$ acting on pairs of vectors of the **tangent space** $T_pM$ (the vector space of all vectors "tangent to $M$" at $p$, e.g. velocities of curves through $p$). In a coordinate basis $e_\mu$ of the tangent space, it is represented by a symmetric matrix $g_{\mu\nu}(x)$ such that $g= g_{\mu\nu} e^\mu \otimes e^\nu$, with $e^\mu$ being the corresponding basis of $TM^{\star}$ such that $e^\nu(e_\mu)=\delta^\nu_\mu$. In a natural chart $e_\mu = \partial_\mu$ and $e^\mu = \text{d}x^\mu$. 
The inverse of the matrix $g_{\mu\nu}$ is $g^{\mu\nu}$ satisfying $g^{\mu\rho}g_{\rho\nu}=\delta^\mu_\nu$ (used to raise and lower indices). For two tangent vectors $u^\mu,v^\mu$, $g(u,v)=g_{\mu\nu}u^\mu v^\nu$ (Einstein summation convention: repeated up/down indices are summed) defines their scalar product, from which one recovers the "length" $g(v,v)$ of $v$ and the angle $\cos(\widehat{u,v})=g(u,v)/\sqrt{g(u,u)g(v,v)}$ between $u$ and $v$.

- A **Lorentzian metric**: a metric tensor whose signature (the numbers of positive and negative eigenvalues of $g_{\mu\nu}$ once diagonalized at a point) is $(-,+,+,+)$, as opposed to a **Riemannian** metric, of signature $(+,+,+,+)$, which only encodes distances. It is always possible to find locally (at each point of space-time), a frame (i.e. a basis for $TM$) in which $g$ is diagonal and equal to the Minkowski metric $\eta$. These frames are called inertial or free-falling frames. The Lorentzian signature is precisely what allows one to separate tangent vectors into **timelike** ($g(v,v)<0$), **spacelike** ($g(v,v)>0$) and **null/lightlike** ($g(v,v)=0$) vectors at every point, reproducing locally the light-cone structure and causal order of Minkowski space-time.

- A **connection** $\nabla$ provides a canonical way to differentiate a vector field along another vector field. The naive difference quotient $\big(v(\gamma(\lambda))-v(p)\big)/\lambda$ is not well defined: $v(\gamma(\lambda))\in T_{\gamma(\lambda)}M$ and $v(p)\in T_pM$ live in different vector spaces and cannot be subtracted directly, since a priori there is no way to compare vectors at different points of $M$. This is exactly what a connection supplies, through **parallel transport**: given a curve $\gamma$ with $\gamma(0)=p$, $\nabla$ defines a linear isomorphism $\Pi_{\gamma(\lambda)\to p}:T_{\gamma(\lambda)}M\to T_pM$ bringing a vector at $\gamma(\lambda)$ back into $T_pM$ before comparing it to $v(p)$. This gives a well-defined derivative of $v$ along $u=\gamma'(0)$ at $p$:
$$\nabla_u v\big|_p = \lim_{\lambda\to 0}\frac{\Pi_{\gamma(\lambda)\to p}\,v(\gamma(\lambda)) - v(p)}{\lambda}.$$
In a chart this reduces to the familiar $\nabla_uv=u^\mu\left(\partial_\mu v^\nu+\Gamma^\nu_{\mu\rho}v^\rho\right)\partial_\nu$, consistent with $\nabla_\mu v^\rho=\partial_\mu v^\rho+\Gamma^\rho_{\mu\nu}v^\nu$, where we introduced the **Christoffel symbols**, being the covariant derivative of the basis vector in a given chart $$\Gamma^{\lambda}_{\mu\nu}\partial_\lambda = \nabla_\mu \partial_\nu$$. 

  The connection is a very general and important concept; we present here only the special case relevant to general relativity, the so-called **affine connection**. For a fully general presentation, see our [lecture on connections](../../_maths/gauge/connections.md). Axiomatically, it is an $\mathbb{R}$-bilinear map $\nabla:\mathfrak{X}(M)\times\mathfrak{X}(M)\to\mathfrak{X}(M)$, $(u,v)\mapsto\nabla_uv$, such that for all $u,v\in\mathfrak{X}(M)$ and $f\in C^\infty(M)$:

  (i) $\nabla_{fu}v = f\,\nabla_uv$ ($C^\infty(M)$-linear, i.e. tensorial, in the direction $u$);

  (ii) $\nabla_u(fv) = u(f)\,v + f\,\nabla_uv$ (Leibniz rule in $v$, making it a derivative).

  Axiom (i) means $(\nabla_uv)(p)$ depends on $u$ only through $u_p\in T_pM$ — consistent with $u$ being merely a "direction" at $p$ — while (ii) shows $\nabla_uv$ genuinely differentiates $v$, so it depends on $v$ in a whole neighborhood of $p$, not just its value there.

- **Metric compatibility** (S3a): the connection is **metric compatible** when, for all vector fields $u,v,w\in\mathfrak{X}(M)$,
$$u\big(g(v,w)\big) = g(\nabla_u v,w)+g(v,\nabla_u w),$$. In components, this condition is also written $$\nabla_\rho g_{\mu\nu}=0$$, where the action of $\nabla$ on a tensor is defined in another bullet point below. It guarantees that parallel transport preserves scalar products: if $u^\mu,v^\mu$ are parallel transported along a curve, $g(u,v)$ is constant along that curve. Without it, physical rulers and clocks carried along space-time would not stay consistent with the metric's own notion of length and duration.

- **Torsion free** (S3b): the **torsion tensor** of the connection is defined, without reference to any chart, as
$$T(u,v) \equiv \nabla_uv-\nabla_vu-[u,v],$$
where $[u,v]$ is the **Lie bracket** of two vector fields — itself a vector field, defined by its action on functions, $$[u,v](f)=u(v(f))-v(u(f))$$. The connection is **torsion free** when $T\equiv0$, i.e. $\nabla_uv-\nabla_vu=[u,v]$ for all $u,v\in\mathfrak{X}(M)$. In a coordinate basis, $[\partial_\mu,\partial_\nu]=0$ (partial derivatives commute), so evaluating $T$ on $u=\partial_\mu$, $v=\partial_\nu$ gives $$T^\rho{}_{\mu\nu}\,\partial_\rho=\nabla_{\partial_\mu}\partial_\nu-\nabla_{\partial_\nu}\partial_\mu=\big(\Gamma^{\rho}{}_{\mu\nu}-\Gamma^{\rho}{}_{\nu\mu}\big)\partial_\rho$$: torsion-freeness is thus equivalent to the symmetry of the connection coefficients in their lower indices,
$$\Gamma^{\rho}{}_{\mu\nu}=\Gamma^{\rho}{}_{\nu\mu},$$
i.e. to the vanishing of
$$T^{\rho}{}_{\mu\nu}\equiv \Gamma^{\rho}{}_{\mu\nu}-\Gamma^{\rho}{}_{\nu\mu}.$$
Geometrically, torsion measures the failure of an infinitesimal parallelogram, built by transporting one small displacement along another, to close.

Metric compatibility and torsion-freeness together (S3a+S3b) are precisely the two conditions of the **fundamental theorem of Riemannian (here Lorentzian) geometry**: they fix $\Gamma$ uniquely in terms of $g$ and its first coordinate derivatives, through 

$$\boxed{\Gamma^{\rho}{}_{\mu\nu} = \frac{1}{2}g^{\rho\sigma}\left(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\right)},$$

the **Levi-Civita connection**. This theorem is proven in this [class](../../_maths/gauge/connections.md). We thus see that, once (S1)-(S3) are assumed, no independent geometric degree of freedom is left besides $g$ itself: the connection (and hence curvature) is entirely determined by the metric.

- **action of $\nabla$ on tensors**: The action of the connection on a type $(r,s)$ tensor is give by asking that, for every $u\in\mathfrak{X}(M)$: (a) $\nabla_u f = u(f)$ on scalars $f\in C^\infty(M)$; (b) the **Leibniz rule** on tensor products, $\nabla_u(S\otimes T)=(\nabla_uS)\otimes T + S\otimes(\nabla_uT)$; and (c) that $\nabla_u$ commutes with every **contraction** (the pairing of an upper index against a lower one). Together with the original action on vector fields, these three requirements fix $\nabla_uT$ uniquely for any tensor field $T$. As a first consequence, take a one-form $\omega$ and a vector field $v$: $\omega(v)$ is exactly the contraction of $\omega\otimes v$, hence a scalar, so (a)-(c) give
  $$u\big(\omega(v)\big) = (\nabla_u\omega)(v) + \omega(\nabla_uv) \quad\Longrightarrow\quad (\nabla_u\omega)(v) = u(\omega(v)) - \omega(\nabla_uv).$$
  Writing this out in a chart with $u=\partial_\mu$, $v=\partial_\nu$, and comparing coefficients of $v^\nu$ using $\nabla_\mu v^\nu=\partial_\mu v^\nu+\Gamma^\nu_{\mu\lambda}v^\lambda$, gives
  $$\nabla_\mu\omega_\nu = \partial_\mu\omega_\nu - \Gamma^\lambda_{\mu\nu}\omega_\lambda:$$
  a **minus** sign for the lower (covariant) index, as opposed to the **plus** sign for the upper (contravariant) index of a vector.

  More generally, for a tensor field of type $(r,s)$, one $+\Gamma$ term appears for every upper index and one $-\Gamma$ term for every lower index:

  $$\nabla_\rho T^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s} = \partial_\rho T^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s} + \sum_{i=1}^r \Gamma^{\mu_i}_{\rho\lambda}\,T^{\mu_1\cdots\lambda\cdots\mu_r}{}_{\nu_1\cdots\nu_s} - \sum_{j=1}^s \Gamma^{\lambda}_{\rho\nu_j}\,T^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\lambda\cdots\nu_s}$$

  (the $i$-th upper or $j$-th lower index replaced by the dummy $\lambda$ in each summand).

</details>

### Dynamics:

Now that the structure is set, we introduce dynamical principles (D) encoding how this structure evolve through space-time:


- (D1): Energy is related to geometry, through the **Einstein equation**:
   
    $$\boxed{R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu} - \Lambda g_{\mu\nu}}$$

  where $\Lambda$ is a constant called the **cosmological constant**, which we will discuss in later classes. The **Ricci tensor** $R_{\mu\nu}$ is the contraction of the Riemann tensor on its first and third indices,

  $$R_{\mu\nu} = R^{\rho}{}_{\mu\rho\nu},$$

  and the **Ricci scalar** is its trace with respect to the metric,

  $$R = g^{\mu\nu} R_{\mu\nu}.$$

  The **Riemann curvature tensor** $R^{\rho}{}_{\sigma\mu\nu}$ associated to the connection $\Gamma$ is defined by

  $$R^{\rho}{}_{\sigma\mu\nu} = \partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} + \Gamma^{\rho}{}_{\mu\lambda}\Gamma^{\lambda}{}_{\nu\sigma} - \Gamma^{\rho}{}_{\nu\lambda}\Gamma^{\lambda}{}_{\mu\sigma}.$$

  $R^{\rho}{}_{\sigma\mu\nu}$ is really understood as a geometrical curvature, quantifying how much a vector rotates if it is parallel transported back to its point around a loop with the connection $\nabla$. The presence of its contractions in the Einstein equation further favours the literal geometrical interpretation that the presence of energy/matter curve space-time. For further discussion, it is also convenient to define the left-hand side of the Einstein equation (D1) as the **Einstein tensor**,

  $$G_{\mu\nu} = R_{\mu\nu} - \tfrac{1}{2} R\, g_{\mu\nu}.$$

- (D2): Matter fields obey their special-relativistic field equations in any local inertial free-falling frame. A simple and general way to satisfy this demand is to leave the special-relativistic expressions untouched in other general frames with the replacement $\eta \to g$ and $\partial_\mu \to \nabla_\mu$. This prescription, is sometimes known as **minimal coupling** or **universal coupling**, translating that all fields of matter couple to a unique metric $g$ (universal) and its uniquely defined Levi-Civita connection defining their parallel transport (minimal). Note however that such prescription is not always perfectly unambiguous and can be problematic in specific situations. For example, while partial derivative commutes, covariant derivative do not, and their ordering can thus be ambiguous (in a way, this problem is similar for the prescriptions regarding quantification of classical systems).

D1 and D2 can also be recovered together through extremalization of the **Einstein-Hilbert action**:

$$\boxed{S_{EH} = \int\sqrt{-|g|}\left(\frac{c^4}{16 \pi G}(R - 2\Lambda) + \mathcal{L}_m(\psi)\right) \text{d}^4x}$$

where $$\vert g \vert$$ is the determinant of the metric $g$ allowing to define the volume form $\sqrt{-\vert g\vert}\text{d}^4x$. This action encodes both Einstein equations (D1) when varying with respect to $g$ and the equation of matter of fields (D2) when varying with respect to $\psi$. In practice, the minimal coupling rule (D2) is generally implemented by taking the $\mathcal{L}_m$ to be the special relativistic matter Lagrangian, where the metric $\eta$ is replaced by $g$ and the standard derivatives are replaced by the connection $\nabla$.

Note that multiple approach have been proposed to justify the equation D1 taking different routes. We will not cover them all here. For a review, see for example Box 17.2 (p. 417) of [Misner, Thorne and Wheeler (1973)](https://physicsgg.me/wp-content/uploads/2023/05/misner_thorne_wheeler_gravitation_freema.pdf) which list six different ways to demonstrate D1 from first principles. Multiple other angles have been proposed since then, as approaches stressing some deep link between the Einstein equations and the principles of thermodynamics ([Jacobson 1995](https://arxiv.org/abs/gr-qc/9504004)).

<details markdown="1">
  <summary><strong>Deriving D1 from the Lagrangian</strong></summary>

The way to obtain the equation of motions from the action is a direct generalisation in four dimension of the standard approach used to derive the [Euler-Lagrange equation](../../_meca/Analytical/Lagrangian.md).

We consider a region of space-time $\Omega$, and vary the action within that region. We consider variations of the action induced by small changes of  the metric in that volume, which is the only dynamical variable of our theory of gravity. We consider small variations of the inverse metric $\delta g^{\mu\nu}$ instead of the metric ($\delta g_{\mu\nu}$) by convention, it allows to recover more immediately the D1 expression. Variations should cancel on the boundary $\partial \Omega$.

The action is stationary when $\delta S_{EH}=0$. That is, we ask for:

$$\delta S_{EH} = \int \left[\frac{c^4}{16\pi G}\,\delta\big(\sqrt{-|g|}(R-2\Lambda)\big) + \delta\big(\sqrt{-|g|}\mathcal{L}_m\big)\right]\text{d}^4x = 0.$$

where $\delta$ indicates a variation when $g^{\mu\nu}$ is varied along the space-time trajectory. 

From this, using the product rule one obtains:

$$
\begin{align}
\delta S_{EH} = \int \left(\frac{c^4}{16\pi G}\left(\frac{\delta R}{\delta g^{\mu\nu}}+ \frac{R}{\sqrt{-|g|}}\frac{\delta \sqrt{-|g|}}{\delta g^{\mu\nu}} - \frac{2\Lambda}{\sqrt{-|g|}}\frac{\delta \sqrt{-|g|}}{\delta g^{\mu\nu}} \right) + \frac{1}{\sqrt{-|g|}}\frac{\delta (\sqrt{-|g|}\,\mathcal{L}_m)}{\delta g^{\mu\nu}} \right)\sqrt{-|g|}\;\delta g^{\mu\nu}\ \text{d}^4x = 0
\end{align}
$$

Since this should hold for every $\delta g^{\mu\nu}$, and $\sqrt{-\vert g\vert}\neq0$, we obtain

$$\frac{c^4}{16\pi G}\left(\frac{\delta R}{\delta g^{\mu\nu}}+ \frac{R}{\sqrt{-|g|}}\frac{\delta \sqrt{-|g|}}{\delta g^{\mu\nu}} - \frac{2\Lambda}{\sqrt{-|g|}}\frac{\delta \sqrt{-|g|}}{\delta g^{\mu\nu}} \right) + \frac{1}{\sqrt{-|g|}}\frac{\delta (\sqrt{-|g|}\,\mathcal{L}_m)}{\delta g^{\mu\nu}}=0$$

Let's now look at each term.

**A useful formula first** 

Let us first find useful relations in order to switch freely from variations of the metric $\delta g_{\mu\nu}$ to variations of its inverse $\delta g^{\mu\nu}$, which we will need multiple times. The metric and its inverse obey the relation $g^{\mu\rho}g_{\rho\nu}=\delta^\mu_\nu$. Taking the variation of both side using the product rule, we get

$$\begin{align}
&\delta g^{\mu\rho}g_{\rho\nu} + g^{\mu\rho}\delta g_{\rho\nu} = 0\\
& \delta g^{\mu\rho}g_{\rho\nu} = -g^{\mu\rho}\delta g_{\rho\nu} \\
&  \delta g^{\mu\rho}g^{\alpha \rho}g_{\rho\nu} = -g^{\alpha \rho}g^{\mu\rho}\delta g_{\rho\nu}\\
& \delta g^{\mu\rho}\delta^{\alpha}_\nu = -g^{\alpha \rho}g^{\mu\rho}\delta g_{\rho\nu}
\end{align}
$$

Relabelling summation indices, we get:

$$\boxed{\delta g^{\mu\nu} = -g^{\mu\alpha}g^{\nu\beta}\delta g_{\alpha\beta}}$$

hence, going from the metric to its inverse raise/lowers the indices and adds a minus sign.

**Variation of the volume element** 

Here, we will assume the formula for the differential of the metric determinant, also known as Jacobi formula, giving:

$$\delta|g| = |g|\,g^{\mu\nu}\delta g_{\mu\nu}$$

We will not attempt at proving it, and more details can be found in most standard general relativity textbook. From this, we obtain

$$\delta\sqrt{-|g|} = \frac{-1}{2\sqrt{-|g|}} \delta|g|= \tfrac12\sqrt{-|g|}\,g^{\mu\nu}\delta g_{\mu\nu}.$$

In term of the inverse metric, this gives:

$$\delta\sqrt{-|g|} = -\tfrac12\sqrt{-|g|}\,g_{\mu\nu}\delta g^{\mu\nu}. $$

and hence

$$\boxed{\frac{1}{\sqrt{-|g|}}\frac{\delta \sqrt{-|g|}}{\delta g^{\mu\nu}}= \frac{-g_{\mu\nu}}{2}}$$

**Another useful formula**

From the expression of $\Gamma^{\rho}_{\,\,\mu\nu}$ in terms of the metric and its derivative (found in the "complement" session above), we can easily derive the expression for its upper and lower index contraction:

$$\begin{align}
\Gamma^\rho_{\,\,\mu\rho}&=\tfrac12g^{\rho\sigma}\partial_\mu g_{\rho\sigma} +\tfrac12g^{\rho\sigma}\partial_\rho g_{\sigma \mu} - \tfrac12g^{\rho\sigma}\partial_{\sigma}g_{\mu\rho} \\
&=\tfrac12g^{\rho\sigma}\partial_\mu g_{\rho\sigma}
\end{align}
$$

Recalling the formula $\delta f/f=\delta(\ln(f))$, for a general function $f$, we found in the previous section on the volume element that:

$$\delta(\ln(\sqrt{-|g|})) = -\frac{1}{2}g_{\mu\nu}\delta g^{\mu\nu} = \frac{1}{2}g^{\mu\nu}\delta g_{\mu\nu} $$

where we used the first useful formula to lower the indices in the second step. Focusing on variations of the metric induced by a change in position $\delta(...) = \partial_\mu(...) \delta x^\mu$, we obtain:

$$\begin{align}
\Gamma^\rho_{\,\,\mu\rho}= \frac{1}{\sqrt{-|g|}}\partial_\mu(\sqrt{-|g|})
\end{align}
$$

Now, from the expression of the covariant derivative of a vector we have 

$$\begin{align}
\nabla_\rho v^\rho &= \partial_\rho v^\rho  + \Gamma^\rho_{\,\,\rho \lambda}v^\lambda\\
&= \partial_\rho v^\rho  + \frac{1}{\sqrt{-|g|}}\partial_\lambda(\sqrt{-|g|}) v^\lambda
\end{align}
$$

From which, using the product rule, we infer another very useful formula, which we will call the **divergence formula**:

$$\boxed{\nabla_\rho v^\rho = \frac{1}{\sqrt{-|g|}}\partial_\rho(\sqrt{-|g|}v^\rho)}$$

For any vector $v$.

**The Riemann curvature term** 

Since $R=g^{\mu\nu}R_{\mu\nu}$, the product rule gives:

$$\delta R = R_{\mu\nu}\,\delta g^{\mu\nu} + g^{\mu\nu}\delta R_{\mu\nu} = -R^{\mu\nu}\delta g_{\mu\nu} + g^{\mu\nu}\delta R_{\mu\nu}.$$

We now assume what is known as **the Palatini identity**:

$$\delta R_{\mu\nu} = \nabla_\rho(\delta\Gamma^\rho_{\nu\mu}) - \nabla_\nu(\delta\Gamma^\rho_{\rho\mu}).$$

which can be proven by looking at the full expression of the Riemann tensor in term of $\Gamma$ and its derivatives, and looking at $\delta R^{\rho}_{\,\,\sigma \mu \nu}$. See for example [here](https://en.wikipedia.org/wiki/Palatini_identity).

Contracting with $g^{\mu\nu}$, which commutes freely with $\nabla$ by metric compatibility (S3a),

$$g^{\mu\nu}\delta R_{\mu\nu} = \nabla_\rho v^\rho,$$

where we introduced $$v^\rho \equiv g^{\mu\nu}\delta\Gamma^\rho_{\mu\nu}-g^{\mu\rho}\delta\Gamma^\lambda_{\lambda\mu}$$.

Hence, using the divergence formula, and Stoke's theorem we find:

$$\int_\Omega \sqrt{-|g|}\,g^{\mu\nu}\delta R_{\mu\nu}\;\text{d}^4x = \oint_{\partial \Omega}\sqrt{-|g|}\,v^\rho\,\text{d}S_\rho$$

This term is thus a boundary term, which vanishes once $\delta g_{\mu\nu}$ is fixed (or compactly supported) on $\partial \Omega$. The cancellation of boundary terms is a subtle topic that we just gloss over here. For more, see e.g. [York (2009)](https://arxiv.org/abs/0809.4033). 

Deleting this boundary term, we simply obtain:

$$\boxed{\frac{\delta R}{\delta g^{\mu\nu}}=R_{\mu\nu}}$$

**Stress energy tensor** 

We assert that the stress-energy tensor of matter, introduced in S4, is defined such that:

$$\boxed{T_{\mu\nu} = -\frac{2}{\sqrt{-|g|}}\frac{\delta \sqrt{-|g|} \mathcal{L}_m}{\delta g^{\mu\nu}}}$$

A discussion of this choice and of the physical meaning of this quantity is given in one of the following complement.

**Putting in all together**:

By replacing each term one by one with the first expression we derived for $\delta S_{EH}$, we obtain immediately  Einstein Equation (D1):

$$R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu} - \Lambda g_{\mu\nu}$$

</details>

<details markdown="1">
  <summary><strong>Deriving D2 from the Lagrangian</strong></summary>

To prove D2, we must look at variations of $S_{EH}$ with respect to $\psi$. This is much easier, as the whole gravitational term does not depend on $\psi$: only $\mathcal{L}_m$ does.

First, make the replacement $$\mathcal{L}_m(\psi,\partial\psi,\eta)\to \mathcal{L}_m(\psi,\nabla\psi,g)$$ required by the minimal coupling rule. Then, starting from  $$S_m=\int\sqrt{-\vert g\vert}\,\mathcal{L}_m(\psi,\nabla\psi,g)\,\text{d}^4x$$, vary $$\psi\to\psi+\delta\psi$$ at *fixed* $g$ (so $\Gamma$ is fixed too -- unlike the metric variation, there is no subtlety here about $\delta\Gamma$). Since $\nabla_\mu\psi$ is linear in $\psi$ for fixed $\Gamma$ (whatever the type of field, the derivative will be a sum of $\Gamma\psi$ contraction terms),

$$\delta(\nabla_\mu\psi) = \nabla_\mu(\delta\psi).$$

Hence

$$\delta S_m = \int\sqrt{-|g|}\left[\frac{\partial\mathcal{L}_m}{\partial\psi}\,\delta\psi + \frac{\partial\mathcal{L}_m}{\partial(\nabla_\mu\psi)}\,\nabla_\mu(\delta\psi)\right]\text{d}^4x,$$

where, if $\psi$ carries indices, a sum over all its components is implied. Integrate the second term by parts using the Leibniz rule for $\nabla$:

$$\frac{\partial\mathcal{L}_m}{\partial(\nabla_\mu\psi)}\,\nabla_\mu(\delta\psi) = \nabla_\mu\!\left(\frac{\partial\mathcal{L}_m}{\partial(\nabla_\mu\psi)}\,\delta\psi\right) - \nabla_\mu\!\left(\frac{\partial\mathcal{L}_m}{\partial(\nabla_\mu\psi)}\right)\delta\psi.$$

In the first piece, all the indices of $\psi$ are contracted, leaving a genuine vector field $$v^\mu \equiv \frac{\partial\mathcal{L}_m}{\partial(\nabla_\mu\psi)}\,\delta\psi$$; by the divergence formula, $$\sqrt{-\vert g\vert}\,\nabla_\mu v^\mu = \partial_\mu(\sqrt{-\vert g\vert}\,v^\mu)$$ is a total derivative, which drops for $\delta\psi$ vanishing on $\partial\Omega$. So

$$\delta S_m = \int\sqrt{-\vert g\vert}\left[\frac{\partial\mathcal{L}_m}{\partial\psi}-\nabla_\mu\!\left(\frac{\partial\mathcal{L}_m}{\partial(\nabla_\mu\psi)}\right)\right]\delta\psi\;\text{d}^4x = 0$$

for arbitrary $\delta\psi$, giving the **covariant Euler-Lagrange equation** for matter:

$$\boxed{\frac{\partial \mathcal{L}_m}{\partial \psi}=  \nabla_\mu \left(\frac{\partial \mathcal{L}_m}{\partial(\nabla_\mu \psi)}\right)}$$

Two remarks on how to read it: (i) $$\partial\mathcal{L}_m/\partial\psi$$ is taken at fixed $\nabla\psi$; (ii) if $\psi$ carries tensor indices, so does $$\partial\mathcal{L}_m/\partial(\nabla_\mu\psi)$$, and $\nabla_\mu$ acts on *all* of them.

One can instead treat the Lagrangian *density* $$\sqrt{-\vert g\vert}\,\mathcal{L}_m$$ as a function of the components of $\psi$ and their partial derivatives $\partial_\mu\psi$ (re-expressing $\nabla\psi=\partial\psi+\Gamma\,\psi$). The variational principle then yields the standard Euler-Lagrange equation, valid for any field:

$$\frac{\partial(\sqrt{-\vert g\vert}\,\mathcal{L}_m)}{\partial\psi} = \partial_\mu\!\left(\frac{\partial(\sqrt{-\vert g\vert}\,\mathcal{L}_m)}{\partial(\partial_\mu\psi)}\right).$$

This form is arguably the most fundamental, as it treats each component of $\psi$ as an independent dynamical variable and makes no reference to its tensorial nature. It is strictly equivalent to the boxed equation: the $\Gamma$ terms hidden in $$\partial(\sqrt{-\vert g \vert}\mathcal{L}_m)/\partial\psi$$ (through the $\psi$-dependence of $\nabla\psi$) exactly reproduce those generated by $\nabla_\mu$ acting on the indices of $$\partial\mathcal{L}_m/\partial(\nabla_\mu\psi)$$. Beware of the tempting hybrid $$\frac{1}{\sqrt{-\vert g \vert}}\partial_\mu\big(\sqrt{-\vert g\vert}\,\partial\mathcal{L}_m/\partial(\nabla_\mu\psi)\big) = \partial\mathcal{L}_m/\partial\psi$$: it is correct only for scalar $\psi$, for which $\nabla\psi=\partial\psi$ and the two forms coincide via the divergence formula.

Finally, in a local inertial frame, $g\to\eta$ and $\nabla\to\partial$, so the boxed equation reduces to the standard special-relativistic Euler-Lagrange equation: matter fields locally obey their special-relativistic dynamics, which is exactly the content of D2.

</details>

<details markdown="1">
  <summary><strong>A sidenote on the stress-energy tensor</strong></summary>

In the derivation of D1 from the Lagrangian, we connected the **stress-energy tensor** (introduced in S4) to the matter Lagrangian $\mathcal{L}_m$ through:

$$T_{\mu\nu} = -\frac{2}{\sqrt{-|g|}}\frac{\delta \big(\sqrt{-|g|}\, \mathcal{L}_m\big)}{\delta g^{\mu\nu}}.$$

Expanding the variation with the product rule and using the formula for the variation of the metric determinant established before,

$$\delta\sqrt{-|g|} = -\tfrac12\sqrt{-|g|}\; g_{\mu\nu}\,\delta g^{\mu\nu},$$

we find

$$\frac{\delta \big(\sqrt{-|g|}\,\mathcal{L}_m\big)}{\delta g^{\mu\nu}} = \sqrt{-|g|}\,\frac{\delta \mathcal{L}_m}{\delta g^{\mu\nu}} - \tfrac12\sqrt{-|g|}\,g_{\mu\nu}\,\mathcal{L}_m,$$

so that, whenever $$\mathcal{L}_m$$ depends on the metric but **not on its derivatives** (which is the case for all standard matter fields, since $$\partial_\mu g_{\alpha\beta}$$ only enters through covariant derivatives of the *metric itself*, which vanish), the functional derivative reduces to an ordinary partial derivative and:

$$\boxed{\;T_{\mu\nu} = -2\,\frac{\partial \mathcal{L}_m}{\partial g^{\mu\nu}} + g_{\mu\nu}\,\mathcal{L}_m.\;}$$

This is often the quickest way to compute $T_{\mu\nu}$ in practice, without having to vary the full action $S_m$.

Physically, $T_{\mu\nu}$ collects the densities and fluxes of energy and momentum: $T^{00}$ is the energy density, $T^{0i}$ the momentum density (equivalently the energy flux), and the spatial block $T^{ij}$ contains the stresses — pressure on the diagonal, shear off the diagonal.

In flat-spacetime classical field theory, the stress-energy tensor arises instead as the **Noether current** associated with invariance under spacetime translations (the corresponding conserved *charges* are the total energy and momentum, $P^\nu = \int T^{0\nu}\,\mathrm{d}^3x$). For a field theory with Lagrangian $$\mathcal{L}_m(\psi, \partial_\mu\psi)$$, it reads:

$$T^{\mu}{}_{\nu} = -\frac{\partial \mathcal{L}_m}{\partial (\partial_\mu\psi)}\,\partial_\nu \psi + \delta^{\mu}_{\nu}\,\mathcal{L}_m.$$

(The overall sign is a convention; this choice matches $T^0{}_0 = -\rho$ below. Many quantum field theory textbooks use the opposite sign.)
This definition is the one familiar to particle physicists. The two definitions — the "metric" one and the canonical one — agree for simple models as scalar fields (discussed later in this class), but not always in general: the canonical tensor need not be symmetric (e.g. for the electromagnetic field). It can, however, always be brought to agree with the metric definition by adding suitable total-derivative terms that change neither the conservation law nor the total charges (the *Belinfante–Rosenfeld* procedure). In this sense the metric definition is the more fundamental one.

For a single point particle of rest mass $m$, the action is simply (minus) the mass times the proper time elapsed along its worldline: $S_m = -m\int \mathrm{d}\tau$. **Dust** is a cloud of many such particles, described by a rest-mass density $\rho$ and a common 4-velocity field $u^\mu$, normalized so that $g(u,u) \equiv g_{\mu\nu}u^\mu u^\nu = -1$. The corresponding Lagrangian density is

$$\mathcal{L}_m = -\rho\,\sqrt{-g(u,u)}.$$

One word of caution: a naive application of the boxed formula, holding $\rho$ and $u^\mu$ fixed while varying the metric, gives a wrong extra term. The density $\rho$ itself responds to a change of metric, because the number of particles in a volume is conserved; taking this constraint into account, one obtains

$$T^\mu{}_{\nu} = \rho\, u^\mu u_\nu,$$

which in the local rest frame is simply $\mathrm{diag}(-\rho, 0, 0, 0)$: energy density and nothing else — dust carries no pressure.

For a perfect fluid with energy density $\rho$ and isotropic pressure $P$ (both measured in the local rest frame):

$$T^\mu{}_{\nu} = (\rho + P)\,u^\mu u_\nu + P\,\delta^{\mu}_{\nu},$$

which in the local rest frame reads $\mathrm{diag}(-\rho, P, P, P)$. Dust is recovered as the special case $P = 0$.

Its conservation law $\nabla_\mu T^{\mu\nu}=0$ reduces, in the non-relativistic limit, to the continuity equation and the (inviscid) **Euler equation** of fluid dynamics — not Navier–Stokes, since a *perfect* fluid has no viscosity by construction; the viscous stress term needed for Navier–Stokes simply is not part of this $T^{\mu\nu}$.

The boxed formula pays off immediately for the simplest possible Lagrangian, a constant: $$\mathcal{L}_m = -\rho_\Lambda$$. Then $$\partial\mathcal{L}_m/\partial g^{\mu\nu} = 0$$ and

$$T_{\mu\nu} = -\rho_\Lambda\, g_{\mu\nu},$$

which is exactly a perfect fluid with $\rho = \rho_\Lambda$ and $P = -\rho_\Lambda$. A constant vacuum energy behaves as a fluid with *negative pressure* $P = -\rho$ — the equation of state of the cosmological constant.

</details>

The EEP is also encoded in these axioms as we further discuss in the next section. 

As natural consequences of D1 and D2, we can find two very important equations:

- The **continuity equation**: $$\nabla_\mu T^{\mu\nu}=0$$, which comes from the reunion of Einstein equations with the Bianchi identity $\nabla_\mu G^{\mu\nu}=0$. It encodes the local conservation of energy-momentum for matter.
- The **geodesic equation** for a point like particle $u^\mu\nabla_\mu u^\nu=0$. This equation is a special case of the continuity equation for a free massive particle with energy momentum $T^{\mu\nu}=\rho u^\mu u^\nu$ (the generalisation to massless particles/photons is straightforward and will be discussed later). It states that point-like particles follow the path that extremize the total (space-time) length between two points, known as geodesics. This equation is thus absolutely key for the geometrical understanding of gravity.

<details markdown="1">
  <summary><strong>Discussion of the continuity equation</strong></summary>

Working with the expression of $G_{\mu\nu}$, it is possible to show that:

$$\nabla^\mu G_{\mu\nu} \equiv \nabla^\mu\left(R_{\mu\nu}-\frac12 R g_{\mu\nu}\right)=0.$$ 

This is a contracted form of the so-called **Bianchi identity**, which is a purely geometric identity, valid for the Riemann tensor of *any* torsion-free, metric-compatible connection, and reads
It holds identically, independently of the field equations: it is a property of geometry alone, valid for any metric $g$. It even has a geometric interpretation related to the concept of "holonomies", which will not discuss further here (see e.g. [Baez & Muniain (1994)](https://pages.jh.edu/rrynasi1/PhysicalPrinciples/literature/Baez+Muniain1994GaugeFieldsKnots+Gravity.pdf)). 
Now, taking the covariant divergence $\nabla^\mu$ of both sides of the Einstein equation (D1), the geometric side vanishes by the Bianchi identity, and since $\nabla^\mu(\Lambda g_{\mu\nu})=0$ by metric compatibility ($\nabla g = 0$) and constancy of $\Lambda$, we are left with
$$\nabla^\mu T_{\mu\nu}=0.$$ This equation can be understood as the local conservation of energy-momentum of matter, and is as we saw, deeply encoded in the relationship between matter and geometry (D1). 

</details>

<details markdown="1">
  <summary><strong>Discussion of the geodesic equation</strong></summary>

Consider a pressureless fluid of free point particles ("dust"), of stress-energy tensor $T^{\mu\nu}=\rho\, u^\mu u^\nu$, where $\rho$ is the rest-mass density measured in the local rest frame and $u^\mu$ the 4-velocity field, normalized as $u^\mu u_\mu = -c^2 = -1$ (using the signature convention introduced above). Plugging into the continuity equation:

$$\nabla_\mu(\rho u^\mu u^\nu) = u^\nu\nabla_\mu(\rho u^\mu) + \rho\, u^\mu\nabla_\mu u^\nu = 0.$$

Contracting this equation with $u_\nu$, and using that $u^\nu u_\nu=-1$, we obtain $$-\nabla_\mu(\rho u^\mu) + \rho u^\mu u_\nu \nabla_\mu u^\nu=0$$. Now, the second terms disapears by noticing that $$\nabla_\mu(u_\nu u^\nu) =\nabla_\mu(-1)=0$$ and that, on the other hand, by the product rule $$\nabla_\mu(u_\nu u^\nu) = u_\nu \nabla_\mu u^\nu + u^\nu \nabla_\mu(u_\nu) = u_\nu \nabla_\mu u^\nu + u^\nu \nabla_\mu(g_{\nu \alpha}u^\alpha) = u_\nu \nabla_\mu u^\nu + u^\nu g_{\nu \alpha}\nabla_\mu(u^\alpha) = 2 u_\nu \nabla_\mu u^\nu $$ (using metricity condition $\nabla g=0$ and relabelling summation indices). We are thus left with:

$$-\nabla_\mu(\rho u^\mu) = 0,$$

i.e. rest mass is conserved along the flow, the curved-spacetime analogue of the continuity equation of fluid mechanics. Substituting this back into the first expression we had for $\nabla_\mu(\rho u^\mu u^\nu)$,  and since $\rho\neq0$ for a physical fluid, we are left with

$$u^\mu\nabla_\mu u^\nu = 0,$$

the **geodesic equation**. Notice that this equation contains no reference whatsoever to the mass, composition, or internal structure of the particle: any free test body, regardless of what it is made of, follows the same worldline once its initial position and 4-velocity are fixed. This mass-independence is exactly the mathematical translation of the UFF, and we will use it again below to show how (S1)-(S3)+(D2) encode the EEP.

The geodesic equation can also be recovered from a least-action principle when looking for the curve $\gamma(\tau)$ extremizing the total space-time length of the particle, that is:

$$S = -m\int \text{d}s = -m\int\sqrt{-g_{\mu\nu}(x)\,\dot x^\mu\dot x^\nu}\;\text{d}\tau, \qquad \dot x^\mu \equiv \frac{\text{d}x^\mu}{\text{d}\tau},$$

where $\tau$ is, for now, an arbitrary parameter along the curve (the action is invariant under reparametrization $\tau\to\tau'(\tau)$, so no particular choice of $\tau$ is assumed yet). Writing $-\vert u \vert^2 \equiv -g_{\alpha\beta}\dot x^\alpha\dot x^\beta$, the Lagrangian is $L=-m\sqrt{-\vert u \vert^2}$, and since this is an ordinary mechanics-type action (one independent variable $\tau$, first derivatives only), the standard Euler-Lagrange equation applies directly:

$$\frac{\text{d}}{\text{d}\tau}\left(\frac{\partial L}{\partial \dot x^\beta}\right) - \frac{\partial L}{\partial x^\beta} = 0.$$

Computing the two derivatives gives:

$$
\begin{align}
&\frac{\partial L}{\partial \dot x^\beta} =-m\frac{\partial}{\partial \dot x^\beta}(\sqrt{-g_{\mu\nu}(x)\,\dot x^\mu\dot x^\nu}) \\
&= -\frac{1}{2\sqrt{-g_{\mu\nu}(x)\,\dot x^\mu\dot x^\nu}} \frac{\partial}{\partial \dot x^\beta}(-g_{\mu\nu}(x)\,\dot x^\mu\dot x^\nu)\\
&= \frac{m}{2\sqrt{-\vert u \vert^2}}(g_{\mu\nu}\delta^{\mu}_{\,\beta} \dot x^\nu + g_{\mu\nu}x^\mu \delta^{\nu}_{\,\beta})\\
&=\frac{m}{\sqrt{-\vert u \vert^2}}\,g_{\beta\alpha}\dot x^\alpha
\end{align}
$$

and:

$$
\begin{align}
\frac{\partial L}{\partial x^\beta} = \frac{m}{2\sqrt{-\vert u \vert^2}}\,\partial_\beta(g_{\mu\nu})\,\dot x^\mu\dot x^\nu,
\end{align}
$$

such that the Euler-Lagrange equation is

$$\frac{\text{d}}{\text{d}\tau}\left(\frac{m}{\sqrt{-\vert u \vert^2}}g_{\beta\alpha}\dot x^\alpha\right) - \frac{m}{2\sqrt{-\vert u \vert^2}}\partial_\beta g_{\mu\nu}\dot x^\mu\dot x^\nu = 0.$$

Reparametrization invariance means we are free to now specialize to **proper time**, i.e. the parametrization for which $(\sqrt{-\vert u \vert^2})^2=1$ is constant along the curve (equivalently $u^\mu u_\mu=-1$, with $u^\mu\equiv\dot x^\mu$); this simplifies the equation without loss of generality, since any solution curve can always be reparametrized this way after the fact. With $\vert u \vert^2=-1$ constant, $\text{d}\mathcal{\sqrt{-\vert u \vert^2}}/\text{d}\tau=0$, and the equation becomes, after dividing through by the (now manifestly cancelling) mass $m$ -- a first, direct illustration of the UFF/WEP already discussed above --

$$\frac{\text{d}}{\text{d}\tau}\big(g_{\beta\alpha}u^\alpha\big) - \tfrac12\partial_\beta g_{\mu\nu}\,u^\mu u^\nu = 0.$$

We shall not forget that $g$ depends also on $\tau$ as the particle evolves through space time and hence we can use the chain rule as:

$$\dfrac{\text{d}}{\text{d}\tau}g_{\beta\alpha}(x(\tau)) = \frac{\partial x^\lambda}{\partial \tau}\frac{\partial}{\partial x^\lambda}g_{\beta\alpha} = \partial_\lambda g_{\beta\alpha}\,u^\lambda$$

Such that the total equation becomes:

$$g_{\beta\alpha}\dot u^\alpha + \partial_\lambda g_{\beta\alpha}\,u^\lambda u^\alpha - \tfrac12\partial_\beta g_{\mu\nu}\,u^\mu u^\nu = 0.$$

Since $$\partial_\lambda g_{\beta\alpha}\,u^\lambda u^\alpha$$ is contracted with the symmetric object $u^\lambda u^\alpha$, it may be symmetrized in $\lambda,\alpha$ at no cost, giving

$$g_{\beta\alpha}\dot u^\alpha + \tfrac12\big(\partial_\lambda g_{\beta\alpha}+\partial_\alpha g_{\beta\lambda}-\partial_\beta g_{\mu\nu}\big)u^\mu u^\nu = 0.$$

The bracketed combination is exactly $$g_{\beta\lambda}\Gamma^\lambda{}_{\mu\nu}$$, from the boxed Levi-Civita formula given above. So

$$g_{\beta\alpha}\dot u^\alpha + g_{\beta\lambda}\Gamma^{\lambda}{}_{\mu\nu}\,u^\mu u^\nu = 0.$$

That is, raising the free index:

$$\boxed{\frac{\text{d}u^\beta}{\text{d}\tau} + \Gamma^{\beta}{}_{\mu\nu}\,u^\mu u^\nu = 0,}$$

which is precisely $u^\lambda\nabla_\lambda u^\beta=0$, since 

$$u^\mu\nabla_\mu u^\beta = u^\mu(\partial_\mu u^\beta + \Gamma^\beta{}_{\mu\nu} u^\nu) = \dfrac{\text{d}u^\beta}{\text{d}\tau}+\Gamma^\beta{}_{\mu\nu}u^\mu u^\nu$$

This is exactly the **geodesic equation**, matching the derivation obtained above from the continuity equation.

</details>


## Requierements for a theory of gravity, EEP and GR

After all this theoretical display, we find thanksfully that, in the context of general relativity, gravity is as desired, a long range attractive force between masses with $$V(r)=-Gm_1m_2/r$$ in the limit of small velocities. We find back special relativity when gravity is turned off, and it can be shown to be self-consistent. As such all the basic requierements we asked for at the beggining of this class are satisfied by GR! Indeed:

### Newtonian limit

As discussed in the supplement to this section, considering general relativity near the flat space-time limit, considering a weak and static field, as well as slow motions. In this context, the metric can be written $g_{\mu\nu}= \eta_{\mu\nu} + h_{\mu\nu}$, where $h_{\mu\nu}$ is a small perturbation, and writing $g_{00}=-(1+2\Phi/c^2)$, we can show that the geodesic equation, in the small velocity limit gives:

$$\boxed{\frac{\text{d}^2 x^i}{\text{d}t^2} = -\partial^i \Phi}$$

On the other hand, in such a limit, Einstein equations reduce to the so-called **Poisson equation**:
  
$$\boxed{\nabla^2\Phi = 4\pi G \rho,}$$

For a point mass, the solution is the familiar $\Phi(r)=-Gm_1/r$, giving the interaction energy $V_{\rm int}(r)=-Gm_1m_2/r$: Newton's law, exactly as demanded in our initial wish-list. 
As such, Newtonian gravity is as desired a limit of GR, making gravity an attractive and long-range force between masses. Note however, that GR does even more, as not only masses, but also energy and pressure gravitates! But this is a supplement, not a contradiction to our initial demand. 

<details markdown="1">
  <summary><strong>Derivation of the equations for the Newtonian limit</strong></summary>

The Newtonian regime is defined by three independent assumptions,
which we will invoke by name:

1. **Weak field:** We assume that the metric can be written as a small correction to Minkowski: $g_{\mu\nu}=\eta_{\mu\nu}+\epsilon h_{\mu\nu}$ with $$\epsilon \in \mathbb{R}$$ and $$\vert\epsilon\vert\ll1$$. Every term in $\epsilon^2$ will be considered as null.
2. **Static field:** all time derivatives of the metric vanish, $\partial_0 h_{\mu\nu}=0$.
3. **Slow motion:** the test particle and the source move with $v\ll c$.

We use Cartesian coordinates $x^0=ct,x^1=x,x^2=y,x^3=z$. Let $\tau$ be the proper time of a test particle. In such a frame, the four velocity $u^\mu= \text{d}x^\mu/\text{d}\tau = (c\text{d}t/\text{d}\tau, \text{d}x^i/\text{d}\tau)$. 

**i) geodesic equation**

The geodesic equation is 

$$\frac{\text{d}^2 x^\lambda}{\text{d}\tau^2} = -\Gamma^{\lambda}_{\mu\nu}\frac{\text{d} x^\mu}{\text{d}\tau}\frac{\text{d} x^\nu}{\text{d}\tau}$$

with the Christoffel symbols:

$$\Gamma^{\lambda}{}_{\mu\nu} = \frac{1}{2}g^{\lambda\sigma}\left(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\right)$$

Using the small velocity approximation $u^0 = c\text{d}t/\text{d}\tau \gg u^i = \text{d} x^i/\text{d}\tau$, because of the factor of $c$.
 
Simplifying all the terms in $\text{d}x^i/\text{d}\tau$, one gets simply:

$$\frac{\text{d}^2 x^\lambda}{\text{d}\tau^2} = -c^2\Gamma^{\lambda}{}_{00}\left(\frac{\text{d} t}{\text{d}\tau}\right)^2$$

From the expression of the christoffel symbol, we have 

$$\Gamma^{\lambda}{}_{00} = \frac{1}{2}g^{\lambda\sigma}\left(\partial_0 g_{\sigma 0}+\partial_0 g_{\sigma 0}-\partial_\sigma g_{00}\right) = -\frac{1}{2}g^{\lambda\sigma} \partial_\sigma g_{00}=  -\frac{1}{2}\epsilon \eta^{\lambda\sigma} \partial_\sigma h_{00}$$

where we simplified the time derivatives (because of the static field approximation) and then cancelled all the terms in $\epsilon^2$ (weak field assumption). 

For $\lambda=0$, we get $$\Gamma^{0}{}_{00}=1(\eta^{00}\partial_0h_{00} - \eta^{0i}\partial_i h_00)/2=0$$ (because of static field and $$\eta^{0i}=0$$ is diagonal). The zeroth component of the geodesic equation thus becomes simply $$c^2 \text{d}^2 t/ \text{d}\tau^2 =0$$ and hence $$\text{d}t/\text{d}\tau = {\rm cst}$$.

For $\lambda=i$, using the chain rule $$\frac{\text{d}x}{\text{d}t} = \frac{\text{d}x}{\text{d}\tau}\frac{\text{d}\tau}{\text{d}t}$$, we get:

$$\frac{\text{d}^2x^i}{\text{d}t^2}=\frac{1}{2}c^2\epsilon\partial^i h_{00}$$

Now, since we know that in Newtonian mechanics

$$\boxed{\frac{\text{d}^2x^i}{\text{d}t} = -\partial^i \Phi}$$

where $\Phi$ is the gravitational potential, we introduce the suggestive notation:

$$\Phi = -\frac{c^2\epsilon h_{00}}{2} = \frac{c^2}{2}(g_{00}-\eta_{00})$$

So far we can simply consider this as a definition or a renaming. We will see in the second part that $\Phi$ can really be identified with the Newtonian potential through Einstein equations giving the Poisson equation for $\Phi$ in the Newtonian limit.

Using the time signature $\eta_{00}=-1$, we can then write the metric component in term of the Newtonian gravitational potential:

$$\boxed{g_{00}= - 1 - \frac{2 \Phi}{c^2}}$$

Hence, Newtonian gravitation is the limit of general relativity in which only the geometry of time matters (hence clocks ticks at different rates in a gravitational field) and the geometry of space can be neglected. 

**i) Einstein equation**

Taking the Einstein equation (D1) and contracting with $g^{\mu\nu}$ on both sides one obtains:

$$R = -\frac{8\pi G}{c^4} \mathcal{T} + 4\Lambda $$

where we used: $g^{\mu\nu}g_{\mu\nu}=4$ and $\mathcal{T}= g^{\mu\nu}T_{\mu\nu}$. Re-inserting back this expression of the Ricci scalar $R$ in the original Einstein equation, we get:

$$R_{\mu\nu} = \frac{8\pi G}{c^4}(T_{\mu\nu}-\frac{1}{2}\mathcal{T}g_{\mu\nu}) + \Lambda g_{\mu\nu}$$

Now, let's compute the left-hand side. Using the expression of the Riemann tensor in term of $\Gamma$, we have:

$$R_{\mu\nu}= R^{\rho}{}_{\mu \rho \nu}=  \partial_\rho \Gamma^{\rho}{}_{\nu\mu} - \partial_\nu \Gamma^{\rho}{}_{\rho\mu} + \Gamma^{\rho}{}_{\rho\lambda}\Gamma^{\lambda}{}_{\nu\mu} - \Gamma^{\rho}{}_{\nu\lambda}\Gamma^{\lambda}{}_{\rho\mu}$$

all the $\Gamma\Gamma$ term are second order (they will give $\epsilon^2$ terms only), and they can thus be neglected. We are then left with $$ R_{\mu\nu}=  \partial_\rho \Gamma^{\rho}{}_{\nu\mu} - \partial_\nu \Gamma^{\rho}{}_{\rho\mu} $$. Focusing on the $\mu=\nu=0$ component $$R_{00} = \partial_\rho \Gamma^{\rho}{}_{00} - \partial_0 \Gamma^{\rho}{}_{00}$$. Using the static approximation, $$R_{00} = \partial_\rho \Gamma^{\rho}{}_{00}$$ and using our expression for $$\Gamma^{\rho}{}_{00}$$ obtained above: 

$$R_{00} = - \frac{1}{2}\epsilon\partial_\rho(\eta^{\lambda \sigma}\partial_\sigma h_{00})$$

Now, since only the spatial derivative are non-vanishing (static approximation), and using the expression for $\Phi$ in term of $h_{00}$, we simply get:

$$R_{00}= \frac{1}{c^2}\nabla^2\Phi$$

where we introduced the notation $$\nabla^2=\partial_i\partial^i$$.

Now, we are ready to put everything back in our Einstein Equation ! Considering a fluid of mass density $\rho$, the stress energy tensor has an only non negligable component: $T_{00}=\rho c^2$. The trace is $\mathcal{T}\simeq \eta^{00}T_{00}=-\rho c^2$. For a solar system type solution, we can easily neglect the cosmological constant $\Lambda \simeq 0$. 
Hence $$T_{00}-\frac{1}{2}\mathcal{T}g_{00} = \rho c^2 - \rho c^2/2 = \rho c^2/2$$ and the zero-zero component of the Einstein equation is:

$$\frac{1}{c^2}\nabla^2\Phi =  \frac{8\pi G}{c^4} \rho c^2/2  $$

that is, the Poisson equation:

$$\boxed{\nabla^2\Phi =  4\pi G \rho}$$

Confirming that the $\Phi$ field driving the motion in the limit of the geodesic equation really corresponds to the Newtonian potential.

Consider a single point mass $m_1$ sitting at the origin. Its mass density is a
*distribution*, not a function:

$$\rho(\vec{x}) = m_1\,\delta^3(\vec{x}), \qquad \delta^3(\vec{x}) \equiv \delta(x)\delta(y)\delta(z)$$

where $\delta$ is the Dirac delta. The Poisson equation becomes

$$\nabla^2 \Phi = 4\pi G m_1 \delta^3(\vec{x})$$

In order to solve this equation, we can use the divergence theorem that tells us that the integral of the divergence of a vector field in a volume is equal to the integral of that vector over its surface. Considering a sphere of volume $V$, and surface $S$ surounding the point mass: 

$$\iint \vec{\nabla}(\vec{\nabla}\phi) \text{d}V = \oint\oint \vec{\nabla} \phi \text{d}\vec{S}$$
 
inserting Poisson equation on the left and integrating

$$4\pi G m_1 = 4\pi r^2 \frac{\partial}{\partial r}\Phi(r)$$
 
which we can integrate again to get:

$$\boxed{\Phi(r) = -Gm_1/r}$$

Rather than solving this by brute force, we could also have called on a friendly mathematician, who tells us that

$$\nabla^2 f = \delta^3(\vec{x}) \quad \text{is solved by} \quad f(\vec{x}) = -\frac{1}{4\pi r}, \qquad r \equiv |\vec{x}|$$

where $f$ is called the **Green function** of the operator $\nabla^2$: the response of the
field to a unit point (Dirac) source. Equivalently, $\nabla^2 (1/r) = -4\pi\delta^3(\vec{x})$. Green functions are a general tool which can help us solving this equation with general $\rho$ or more complicated derivation operators (which we will encounter later): once we know the response to a point source, linearity gives the response to *any* source $\rho$ by superposition, $\Phi(\vec{x}) = 4\pi G \int f(\vec{x}-\vec{x}\,')\,\rho(\vec{x}\,')\,d^3x'$. We will use green functions again.

From Newtonian physics, if a second mass $m_2$ is placed at distance $r$ and couples
to this field, the **interaction potential energy** of the pair is

$$\boxed{V_{\rm int}(r) = m_2 \Phi(r) = -\frac{G m_1 m_2}{r}}$$

</details>

### Special-relativistic limit

Our wish-list also demanded that GR give back special relativity when gravity is switched off -- but "switching gravity off" is more delicate than it sounds. However, the satisfaction of this demand is encoded through our axiom D2, and the fact that gravity can always be locally switched off in free-falling frames, as implied by the EEP.

### Self-consistency and completeness 

We further asked that our theory must be self-consistent and as complete as possible.
Multiple example can be found within GR of experimental predictions that can be derived from different theoretical directions and gives the same results, as for example the prediction of the deviation of light rays, which can be computed both by taking the $m\to 0$ limit of the geodesic equations or by considering the ray optic limit of Maxwell equations in a curved space-time. As far as everyone tried, it is impossible to find two contradicting conclusions from different routes using the axioms of GR proposed above. 

GR is also "as complete as possible", as if one uses the standard model Lagrangian containing all of the known particle physics fields for $\mathcal{L}_m$, one is able to recover all the experimental predictions of this theory in the limit $g\to\eta$. This formulation of GR can even be used as such to study the limiting case of quantum theory in curved space-time where both the quantum behaviour of standard model fields and gravity emmerging from the geometry of space-time are both relevant (see e.g. [Wald (1994)](https://press.uchicago.edu/ucp/books/book/chicago/Q/bo3684008.html)). However, the possible quantum aspects of gravity are not accounted for within GR, in which gravitation gravity is described entierly by classical objects. As you are surely aware, extending and going beyond GR to make it "even more complete" and include such phenomena is one of the biggest challenging of contemporary physics. 

### Validity of the EEP

Taking the three last sections together: long range, attractive for ordinary matter, universal, Newtonian limit, special-relativistic limit, self-consistent -- every item of our initial wish-list is checked. Furthermore, the EEP is carefully encoded in the axioms we used to build GR, and it is, as already discussed before encoded in our geometric formulation. This is thus true of all metric theory of gravity, but we can check the three components of the EEP again in the context of GR, just for the pleasure.

**WEP.** As shown in the discussion of the geodesic equation above, the trajectory of any free test body is a solution of $u^\mu\nabla_\mu u^\nu=0$, an equation that contains no reference to the mass, composition, or internal state of the body. Hence, for a fixed initial position and velocity, all free test bodies follow the *same* worldline in a geometry $g$: this is exactly the UFF, and by construction the WEP. This is a consequence of all the axioms taken together. 

**LPI and LLI.** These both follow from a standard theorem of Lorentzian geometry (a consequence of (S1)-(S3), i.e. of $g$ being a smooth Lorentzian metric equipped with its (unique, by S3a-b) Levi-Civita connection): at *any* point $p\in M$, there exists a coordinate system -- a **local inertial frame**, or Riemann normal coordinates at $p$ -- in which
$$g_{\mu\nu}(p) = \eta_{\mu\nu}$$ and $$\Gamma^{\rho}{}_{\mu\nu}(p) = 0.$$ This is known as **Sylvester's law of inertia**.
Combined with (D2) -- matter fields obey their special-relativistic equations whenever $g=\eta$ and $\Gamma=0$, i.e. $\nabla=\partial$ -- this means that at $p$, in that frame, any non-gravitational experiment obeys exactly the equations of special relativity. Since this construction works at *every* point $p$ of $M$, irrespective of where or when $p$ is located, the outcome of a local non-gravitational experiment cannot depend on where/when it is performed: this is **LPI**. At a given point $p$, the freedom to choose *which* local inertial frame to use is exactly the freedom to apply a Lorentz transformation of the tangent space $T_pM$ (the set of frames in which $g(p)=\eta$ is precisely the orbit of the Lorentz group, since Lorentz transformations are, by definition, the linear maps preserving $\eta$). Since (D2) holds in *any* such frame, the outcome of a local non-gravitational experiment cannot depend on the velocity of the (local inertial) frame in which it is performed: this is **LLI**.

Hence (S1)-(S4) together with (D1) and (D2) reproduce all three components of the EEP (WEP, LPI, LLI), confirming that GR is, as claimed earlier, a **metric theory of gravity**.

## Strong equivalence principle 

A stronger equivalence principle than the EEP is also satisfied by GR. It can be formualted identically to the EEP but includes also gravitational effects. To do so, WEP is generalised to include also self-gravitating objects, and one has to remove the "non gravitational experiment" line in the bullet points for LPI and LLI. The understanding of this principle is that "gravity gravitates" and it also gravitates universally, identically to matter. In other word: take two bodies with largely different masses (like the moon and the earth), such that they have a different binding-energy due to their self gravity. This difference in purely gravitational energy should not impact how they fall/move in another gravitational field, as the one of the sun. Deviation of such effects are known as "Nordtvedt effect" and can also be constrained sharply experimentally.

In a sense EEP, tells us that there is a single metric $g$ appearing in the matter action, to which all fields are coupled:

$$S_{m}= \int\sqrt{-|g|}\mathcal{L}_m(\psi,g_{\mu\nu})\text{d}^4x$$

This allows to interpret that all matter fields live and evolve on the same geometry, dictated by $g$.

By excluding the gravitational experiments from the EEP, we are however blind to the metric appearing in the action of gravity

$$S_{\rm g} = \int\sqrt{-|g^{*}|} \frac{c^4}{16 \pi G} R(g^{*})\text{d}^4x$$

A more general action for the gravitational sector could thus be a function $S_{\rm g}(g^{*},\phi...)$ of another metric and some other fields, from which $g$ could be derived.
The Strong equivalence principle (SEP) states that the same metric appears in both actions:

$$\boxed{g^{*}= g}$$

and that no other dynamical field but appears in $S_{\rm g}$. This is immediately satisfied within GR as by axiom S2, $M$ is equipped with a single and only metric $g$. While this is vividly debated, it might be that GR is the only theory of gravitation satisfying the SEP (with Nordström theory discussed in [a later class](./GR_fieldtheory.md)). Exploring various theories which violate SEP is an interesting exercise, which we will explore in the next lectures.

A noticeable consequence of the SEP is that Newton's constant $G$ must be the same everywhere in space and time. We will come back to this point in a later lecture.

As a wrap-up, recall that:

- any theory satisfying the EEP is called a **metric theory of gravitation**. In such theories, a single field, the metric $g$ can interact with matter to induce gravitational motion. GR is only one of such metric theories.
- The SEP is a stronger principle, stating that EEP is valid and that on top of it, only the unique metric $g$ can be part of the gravitational dynamics. GR might be the unique theory satisfying the SEP, which makes it a much more restrictive condition.

## Propagation of light

Another deep (and unfortunately complicated) question is how light propagates within a given theory of gravity, or more profoundly: what are the possible links between gravity and electromagnetism? As we said, this is a very complex question that we will revisit multiple times during this class, but it is of first importance, notably because light is one of our best way to probe gravity — both in the laboratory, with precision tools such as lasers, and on the very large scales of our Universe, with the light we collect in our telescopes.

We simply introduce here:

- The **weak equivalence principle for photons ($\gamma$-WEP):** in the "light-ray" approximation limit of light, the trajectory of a ray in a gravitational field depends only on its initial position and direction of propagation. In particular, it does not depend on the frequency (energy) of the light, nor on its polarization state — two beams leaving the same point in the same direction follow the same path, whatever their colour or polarization. To this we can add two further conditions along the trajectory: that there is no anomalous dimming or brightening beyond the expected geometrical and redshift effects, and that the polarization state remains unchanged (no rotation). (This definition is inspired from WEP II of [Ni (2015)](https://arxiv.org/pdf/1512.08426).)

Note that the first condition concerns the *path* followed by the light, not its frequency: light can be redshifted when it propagates through a gravitational potential or an expanding universe, and this is a consequence of the EEP rather than a violation of it.

A very important point for our discussion is that one can show that the validity of the EEP implies the validity of the $\gamma$-WEP. The $\gamma$-WEP is therefore already contained within GR. As we will discuss later, some of the effects actively searched for with our telescopes — the so-called cosmic birefringence of the CMB, or a variation of the fine-structure constant, possibly generated by new fundamental fields such as the axion and the dilaton respectively — would leave the trajectories untouched but violate the two additional conditions above, and with them the EEP.

# Further reading

### Articles on foundations of GR:

- [C.M. Will -The Confrontation between General Relativity and Experiment - 2014 - Living reviews in relativity](https://blackholes.tecnico.ulisboa.pt/gritting/pdf/gravity_and_general_relativity/Clifford-Will_The-Confrontation-between-General-Relativity-and-Experiment.pdf) 
- [C. M. Will - theory and experiment in gravitational physics - second edition 2018 - Cambridge University Press.](https://www.cambridge.org/core/books/theory-and-experiment-in-gravitational-physics/8A5923C93E43FAFDEC17C3E0FD01A623)
- [W.T. Ni - Equivalence Principles, Spacetime Structure and the Cosmic Connection - 2015 - International Journal of Modern Physics D Vol. 25, No. 4](https://arxiv.org/pdf/1512.08426)

### General textbooks on GR:

- S. Caroll - Spacetime and Geometry - 2019 - Cambridge University Press
- R. M. Wald - General relativity  - 1984 - Chicago University Press
- [C.W. Misner, K. Thorne, J. Wheeler - Gravitation - 1973 -  	W. H. Freeman and Company](https://physicsgg.me/wp-content/uploads/2023/05/misner_thorne_wheeler_gravitation_freema.pdf)