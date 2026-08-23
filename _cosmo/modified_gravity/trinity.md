---
layout: default
title: The trinity of gravity
parent: cosmo
---

We are used to saying that "gravity is the curvature of spacetime". This class is about a fact that should genuinely unsettle that sentence: **one can write down two other theories, using no curvature at all, which make exactly the same predictions as general relativity.** Not approximately — identically, for every experiment.

If three different geometries give the same physics, then "gravity *is* curvature" cannot be a statement about the world. It is a statement about one convenient way of writing the world down. Working out what that means, and why it nevertheless matters enormously for modified gravity, as we will see later in this class. This is for the same reason as for the "field theory" rewriting of GR. Going beyond GR can take many forms depending on the original formulation of GR one consider to start with. 

## Three different geometric objects: torsion, curvature, non-metricity

![image](../pictures/Trinity-geom.png){: width="80%"}

*Figure 1: The three different ways a connection can affect parallel transport through its curvature, torsion and non-metricity. From [Jiménez (2019)](https://arxiv.org/pdf/1903.06830)*

Take a bare manifold $M$ that is an empty space-time. In order to do physics, or even just geometry, structure must be added on it (the manifold already has a topology, but that's not enough). **Two logically independent** structures can be added:

1. an **affine connection** $\Gamma^\rho{}_{\mu\nu}$, which tells you how to **parallel-transport** a vector from a point to its neighbour — and hence how to differentiate vector fields (as well as tensors and spinors under suitable generalisations);
2. a **metric** $g_{\mu\nu}$, which tells you how to **measure** lengths and angles of vectors at every points.

It is worth insisting on how independent these are. Nothing in the definition of a manifold relates them. General relativity *imposes* a relation, by hand, through two extra conditions — and the whole class consists in asking what happens if we impose different ones instead.

Given a connection and a metric, exactly **three** tensors measure how far the geometry departs from flat Euclidean intuition[^gauge]:

[^gauge]: As a sidenote for the differential-geometry amateur. These three geometrical concepts are tied here to the tangent bundle in the way they are defined. **Torsion** is not something a general connection has on its own: it can only be defined for affine connections on the tangent bundle, acting on vectors (more precisely it requires a **solder form**), a canonical identification between the fibre of the bundle and the tangent space of the base. You can see the need for it in the definition $T(X,Y)=\nabla_X Y-\nabla_Y X-[X,Y]$: the bracket only makes sense because $X,Y$ are vector fields *on $M$*, i.e. sections of the very bundle being differentiated. The tangent bundle $TM$ has such an identification for free; a gauge bundle does not — an $SU(3)$ colour index is not a space-time direction. So a Yang-Mills connection (a connection on a principal $G$-bundle, induced on the associated vector bundles, with curvature the field strength $F=\mathrm{d}A+A\wedge A$) has simply *no* torsion (it does not even make sense). Hence Yang-Mills theories could not be rewritten in term of torsion as GR is. **Non-metricity** is a different matter: $Q=\nabla g$ makes sense on any bundle with a fibre metric, and a gauge bundle has one (the Hermitian metric on matter sections). There $Q$ is not undefined but identically **zero**, because demanding $$\partial_\mu(\psi^\dagger\phi)=(D_\mu\psi)^\dagger\phi+\psi^\dagger D_\mu\phi$$ forces $A_\mu^\dagger=-A_\mu$ — which is exactly the statement that the structure group is $U(N)$ rather than $GL(N,\mathbb{C})$. It is therefore **soldering**, not the definability of $Q$, that singles gravity out and allows curvature to be traded for torsion or non-metricity in the "geometric trinity" ([Beltrán Jiménez, Heisenberg & Koivisto 2019](https://arxiv.org/abs/1903.06830)).

-   The **curvature**:[^curv]

    $$\boxed{\;R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}\;}$$

    Parallel-transport a vector around a small closed loop and bring it back to where it started. If it comes back **rotated**, the geometry is curved, and $R$ tells you by how much. This is the familiar one: transport a vector around a triangle on a sphere and it returns turned.
-   The **non-metricity**:[^Q]

    $$\boxed{\;Q_{\rho\mu\nu} \equiv \nabla_\rho\, g_{\mu\nu}\;}$$

    It quantifies whether **lengths** are preserved by parallel transport. If $Q\ne0$, a ruler transported from here to there is no longer the same length, and two vectors that started orthogonal need not stay orthogonal. Setting $Q=0$ is called **metricity**, and it is the first of the two conditions GR imposes, which we called S3a in our [first class](./foundations-GR.md). As a sidenote, non-metricity is not a modern invention. [Weyl (1918)](https://doi.org/10.1007/BF01199420), believing that length should not be an absolute quantity, but a relative one that can be compared only by parallel transport (as orientation is in General relativity), introduced an additional **length connection** to space-time, in the first-ever attempt at a unified theory of gravity and electromagnetism. This length connection can be identified with the electromagnetic potential, as it transforms like a gauge transformation when one operates a conformal transformation of the metric (change of length without change in angle). The length connection is what can be understood in modern language as the trace of $Q$. Einstein raised a devastating objection to Weyl theory: if lengths changed along a path, then two atoms that traveled different histories would have different sizes, and hence different spectral lines. We would see it immediately in stellar spectra — and we do not. Weyl's specific theory died, but the geometric ingredient survived, and it even gave rise to modern gauge theories and connection theories. For more on this, you can see my little essay on this topic [here](https://leovacher.github.io/files/connexion-Vacher-en.pdf).

- The **torsion**:[^T]

    $$\boxed{\;T^\rho{}_{\mu\nu} \equiv \Gamma^\rho{}_{\mu\nu} - \Gamma^\rho{}_{\nu\mu} = 2\,\Gamma^\rho{}_{[\mu\nu]}\;}$$

    It quantifies whether infinitesimal **parallelograms close**. Take two small vectors $u$ and $v$ at a point. Transport $u$ along $v$, and $v$ along $u$. In Riemannian geometry the two paths meet. With torsion there is a **gap**, and the gap is exactly $T(u,v)$. Setting $T=0$ is the second condition GR imposes (called S3b), and we devote the [a future class](./torsion.md) to it.


[^curv]: Or $$R(X,Y)Z \;=\; \nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z$$; $\forall X,Y,Z \in TM$ and in term of vierbein $$R^a{}_b = \text{d}\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b$$.

[^Q]:Or $$Q(X,Y,Z) \;=\; \big(\nabla_X g\big)(Y,Z)\;=\;X\big[g(Y,Z)\big]-g(\nabla_X Y,Z)-g(Y,\nabla_X Z)$$; $\forall X,Y,Z \in TM$ and and in term of vierbein $$Q_{ab} = \text{D}g_{ab}=\text{d}g_{ab}-\omega^c{}_a\,g_{cb}-\omega^c{}_b\,g_{ac}$$.

[^T]: Or $$T(X,Y) \;=\; \nabla_X Y-\nabla_Y X-[X,Y]$$; $\forall X,Y \in TM$ and in term of vierbein $$T^a = \text{d}e^a+\omega^a{}_b\wedge e^b $$.

The effect of these three quantities on vectors is illustrated in Figure 1.
Here is the picture to remember. Transport a vector around, and three things can go wrong:

| | what fails | associated transformation |
|---|---|---|
| **Curvature** $R$ | the vector's **direction** changes | rotation |
| **Torsion** $T$ | the loop's **position** fails to close | translation |
| **Non-metricity** $Q$ | the vector's **length** changes | dilation |

Rotations, translations, dilations. This is not a coincidence: it reflects the group structure underlying each object, a point we will exploit when we discuss [gauge theories of gravity](./Torsion.md).

Now, any connection can be **split uniquely** into three pieces:

$$\boxed{\;\Gamma^\rho{}_{\mu\nu} = \underbrace{\genfrac\{\}{0pt}{}{\rho}{\mu\nu}}_{\text{Levi-Civita}} + \underbrace{K^\rho{}_{\mu\nu}}_{\text{contorsion}} + \underbrace{L^\rho{}_{\mu\nu}}_{\text{disformation}}\;}$$

where contorsion $K$ is built from torsion and disformation $L$ from non-metricity as:

$$
\begin{aligned}
\genfrac\{\}{0pt}{}{\rho}{\mu\nu}&=\tfrac12\,g^{\alpha\lambda}\big(\partial_\mu g_{\lambda\nu}+\partial_\nu g_{\lambda\mu}-\partial_\lambda g_{\mu\nu}\big)\\[4pt]
K^{\alpha}{}_{\mu\nu}&=\tfrac12\,T^{\alpha}{}_{\mu\nu}+T_{(\mu}{}^{\alpha}{}_{\nu)}\\[4pt]
L^{\alpha}{}_{\mu\nu}&=\tfrac12\,Q^{\alpha}{}_{\mu\nu}-Q_{(\mu}{}^{\alpha}{}_{\nu)}
\end{aligned}
$$

Let us check that this accounts for everything: a general connection $\Gamma^\rho{}_{\mu\nu}$ has $4^3 = \mathbf{64}$ components;
a torsion is antisymmetric in its last two indices: $4\times6 = \mathbf{24}$; a non-metricity is symmetric in its last two indices: $4\times10 = \mathbf{40}$ and $24+40 = \mathbf{64}$, as desired. Nothing is left over. Once the metric fixes the Levi-Civita part, *all* the remaining freedom in a connection is torsion plus non-metricity. There is no fourth possibility, and no fourth theory. That is why the trinity is a trinity.

**General relativity is the choice $K = L = 0$.** Two conditions, imposed by hand in 1915, on grounds that were partly historical (Cartan's torsion did not exist until 1922) and partly aesthetic. Hence:

- It is possible to **generalize GR** to also include non vanishing contorsion and disformation in the connection. A famous example is the so-called **Einstein-Cartan** theory, which is just general relativity with non vanishing torsion.
- It is possible to **propose other theories of gravity** based on contorsion and torsion instead of curvature. We will see in the next section that in fact, general relativity can be entirely rewritten either in term of torsion or non-metricity with **zero curvature**. These different formulations are important, as they will suggest different possible modifications to propose new gravity theories  beyond GR.

A [later class](./torsion.md) will be focused on discussing the first option. This class is dedicated to the second option.

## Three formulations of general relativity

![image](../pictures/Trinity-eqs.png){: width="80%"}

*Figure 2: The three different formulations of General relativity: Einstein GR in term of curvature, Teleparallel Equivalent of GR (TEGR) and Symmetric Teleparallel Equivalent of GR (STEGR). From [Jiménez (2019)](https://arxiv.org/pdf/1903.06830)*

Instead of switching off torsion and non-metricity, switch off **any two of the three** and let the survivor carry the gravitational field. There are three ways to do it, and — this is the surprise — **all three reproduce general relativity exactly.**

| | **GR** | **TEGR** | **STEGR** |
|---|---|---|---|
| curvature $R$ | $\ne0$ | $=0$ | $=0$ |
| torsion $T$ | $=0$ | $\ne0$ | $=0$ |
| non-metricity $Q$ | $=0$ | $=0$ | $\ne0$ |
| connection | Levi-Civita | Weitzenböck | "coincident" |
| variable | metric $g_{\mu\nu}$ | tetrad $e^a{}_\mu$ | metric $g_{\mu\nu}$ |
| Lagrangian | $\mathring{R}$ | $\mathbb{T}$ | $\mathbb{Q}$ |
| gravity is… | **geometry** (no force) | a **force** | a **force** |

"TEGR" = *teleparallel equivalent of GR*; "STEGR" = *symmetric teleparallel equivalent of GR*. "Teleparallel" means *parallel at a distance*: with zero curvature, you can compare vectors at distant points unambiguously, which is impossible in GR.

The three Lagrangians are built from quadratic invariants. In the conventions of [Jiménez, Heisenberg & Koivisto (2019)](https://arxiv.org/abs/1903.06830):

$$\mathbb{T} = \tfrac14 T_{\alpha\mu\nu}T^{\alpha\mu\nu} + \tfrac12 T_{\alpha\mu\nu}T^{\mu\alpha\nu} - T_\alpha T^\alpha ,$$

$$\mathbb{Q} = -\tfrac14 Q_{\alpha\mu\nu}Q^{\alpha\mu\nu} + \tfrac12 Q_{\alpha\mu\nu}Q^{\mu\alpha\nu} + \tfrac14 Q_\alpha Q^\alpha - \tfrac12 Q_\alpha\tilde Q^\alpha ,$$

and the coefficients are **not adjustable**: they are fixed uniquely by demanding what follows. Writing $\mathring{R}$ for the ordinary Levi-Civita Ricci scalar, one can show

$$\boxed{\;\mathring{R} \;=\; -\,\mathbb{T} + B_{\mathbb{T}} \;=\; -\,\mathbb{Q} + B_{\mathbb{Q}}\;}$$

where $B_{\mathbb{T}}$ and $B_{\mathbb{Q}}$ are **total derivatives** — pure boundary terms.

**And that is the whole proof.** Two actions differing by a total derivative give the *same* field equations, because the boundary term does not contribute to the variation. So

$$\int\sqrt{-g}\,\mathring{R}\;,\qquad -\int\sqrt{-g}\,\mathbb{T}\;,\qquad -\int\sqrt{-g}\,\mathbb{Q}$$

yield **identical** Einstein equations. Same predictions, same tests passed, same everything.

*(Sign conventions for $\mathbb{T}$ and $\mathbb{Q}$ differ widely between papers; many authors flip them so that the action reads $+\int e\,\mathbb{T}$. Check before comparing formulas — the structural statement "they differ by a boundary term" is what is convention-independent.)*

**But they are not the *same theory* to think with!** Empirical equivalence does not mean conceptual equivalence, and the differences are instructive.

**In GR**, spacetime is curved, free particles follow geodesics, and there is **no gravitational force** — that is Einstein's central insight.

**In TEGR**, spacetime is **flat** (zero curvature). Parallel transport is path-independent. Gravity is a genuine **force**, with a force law structurally like the Lorentz force, and free particles are *pushed off* the straight lines they would otherwise follow. This is much closer to Newton's picture than to Einstein's — written in a fully relativistic language.

**In STEGR** something remarkable happens. Since both curvature *and* torsion vanish, the connection is pure gauge and can be set to **zero globally** by a choice of coordinates — the so-called **coincident gauge**. Then $\nabla_\mu\to\partial_\mu$, and

$$Q_{\rho\mu\nu} = \partial_\rho\, g_{\mu\nu} .$$

The gravitational action becomes a functional of the metric and its **first derivatives only**. This is genuinely attractive: it means the variational principle is well posed with no Gibbons–Hawking–York boundary term, and it makes gravity look, formally, like an ordinary field theory on a flat background.

**One more practical difference: gravitational energy.** In GR, the energy of the gravitational field is famously **non-localisable** — there is no covariant local stress tensor for it, only pseudotensors, for the same reason we found no well-defined stress tensor for the Brans–Dicke scalar. In the teleparallel formulations one *can* construct a proper energy–momentum tensor for the gravitational field. Whether this counts as solving the problem or dissolving it is a matter of taste, but it is a real formal advantage.

## A philosophical sidenote: on theoretical underdetermination (feel free to skip!)

We now have three theories that agree on every observable, and disagree about what the world is made of. One says spacetime is curved and there is no force; another says spacetime is flat and gravity is a force; the third says spacetime is flat, torsionless, and lengths change under transport. Now, **which one is true?** This might appear as an irrelevant question for a physicist, but this is a deep question of philosophy of physics. This is a textbook case of **theoretical underdetermination**: the empirical data cannot, even in principle, select between rival theories. It is one of the oldest problems in philosophy of science, and physics keeps producing fresh instances of it.

Facing this, one could for example think of three responses:

**1. The deflationary (structuralist) answer.** The question is malformed. What is *physically real* is the shared empirical content — the common structure the three formulations encode. The geometry is representational scaffolding, like a coordinate system: indispensable for calculating, meaningless to ask which is "correct". On this view "gravity is curvature" has the same status as "the Earth is at rest in these coordinates".

**2. The realist answer.** One of them *is* right, we simply cannot tell yet. Underdetermination is a fact about our current evidence, not about the world, and it may be broken later. **This turns out to be the correct attitude here** as we will see in the next section.

**3. The pragmatist answer.** Choose whichever makes your problem easiest or your generalisation most natural. This is what working physicists actually do, and it is not intellectually shameful.

Of course this is just a hand waving grasp of the gigantic landscape of proposed answers to this great question, that can be discussed on and on! From a physicist perspective, being aware of this underdetermination of theories is extremely important, as it allows to see all the subtleties and richness of your favorite theory instead of simply and naively believing that "GR tells you that space-time is curved". We already encountered one such example of underdetermination in the case of Newton gravity vs Newton-Cartan theories and we will meet other examples (for example in the Jordan/Einstein frame question in the [Brans-Dicke class](./Brans-Dicke.md)). Other classical cases are the various formulations of quantum mechanics (Copenagen vs Bohm pilot wave). If you are a curious french speaker, you can see my short essay on this topic [here](https://leovacher.github.io/files/BQM.pdf). For a careful treatment of the trinity specifically, see [March, Wolf & Read (2023)](https://arxiv.org/abs/2309.06889), who identify the common dynamical core of the *non-relativistic* trinity as **Maxwell gravitation**, and argue that no analogous distinct core exists in the relativistic case.

## Trinity and modified gravity

Here is the payoff, and it is the reason this class is relevant in a modified gravity class rather than being a curiosity. **The three formulations are equivalent, but their modifications are not.**

Because $\mathring{R}$, $\mathbb{T}$ and $\mathbb{Q}$ differ only by boundary terms, and because a nonlinear function of a boundary term is *not* a boundary term:

$$f(\mathring{R}) \;\ne\; f(\mathbb{T}) \;\ne\; f(\mathbb{Q}) .$$

**Three genuinely different theories**, all reducing to GR when $f$ is linear, all disagreeing as soon as it is not. Choosing a formulation of GR is a free choice; choosing which one to deform is a physical commitment.

The differences are not cosmetic:

| | $f(\mathring{R})$ | $f(\mathbb{T})$ | $f(\mathbb{Q})$ |
|---|---|---|---|
| field equations | **4th order** | **2nd order** | **2nd order** |
| why | $\mathring{R}$ contains $\partial^2 g$ | $\mathbb{T}$ contains only $\partial e$ | $\mathbb{Q}$ contains only $\partial g$ |
| local Lorentz invariance | preserved | **broken** | preserved |
| extra d.o.f. | 1 (the scalaron) | contested | contested |
| screening | chameleon | — | — |
| maturity | 20+ years, well understood | active, contested | newest, least understood |

Three comments on that table.

**The order of the equations.** $\mathring{R}$ contains second derivatives of the metric, so $f(\mathring{R})$ gives *fourth-order* field equations — which, as we will see in the [Horndeski class](./Horndeski.md), is exactly the sort of thing Ostrogradsky warns about. ($f(\mathring R)$ escapes only because it is degenerate, and is equivalent to a scalar-tensor theory with an extra healthy mode.) We will discuss more in the [dedicated class](./fR.md). By contrast $\mathbb{T}$ and $\mathbb{Q}$ contain only *first* derivatives, so their deformations give **second-order equations automatically**. That is a genuine structural advantage, and it is the main reason cosmologists became interested.

**The Lorentz problem.** TEGR uses a tetrad $e^a{}_\mu$ (16 components) rather than a metric (10). Tetrads are defined in the [next class](./altform_GR.md). The extra 6 correspond to local Lorentz transformations, and in TEGR they are pure gauge — because $\mathbb{T}$ changes only by a **total derivative** under a local Lorentz rotation. But apply a nonlinear $f$ and that total derivative no longer drops out: **$f(\mathbb{T})$ breaks local Lorentz invariance.** Different tetrads describing the *same* metric then give different physics. This is not a technicality, and it is why many relativists remain sceptical of $f(\mathbb{T})$ despite its popularity.

**The degrees of freedom are genuinely unsettled.** Independent Hamiltonian analyses of $f(\mathbb{T})$ do not agree with one another — Ferraro & Guzmán find one extra mode, Blagojević and collaborators find five in the generic case — and perturbations around Minkowski and cosmological backgrounds reveal *no* extra modes at all, a classic symptom of **strong coupling** ([Blagojević & Yo 2020](https://arxiv.org/abs/2006.15303)). When linear perturbation theory breaks down on the backgrounds you want to use, you should be cautious about the cosmological constraints derived from it. $f(\mathbb{Q})$ has closely related problems.

We will look at each of these in later classes. For now, the message to take away is the structural one: **the "geometry of gravity" is a choice of language at the level of GR, and a choice of physics the moment you go beyond it.**

### Further reading

- [Jimenez - The Geometrical Trinity of Gravity - 2019 - arXiv:1903.06830](https://arxiv.org/pdf/1903.06830)
- [March, Wolf & Read - On the Geometric Trinity of Gravity, Non-Relativistic Limits, and Maxwell Gravitation (2023)](https://arxiv.org/abs/2309.06889)
- [Heisenberg - A systematic approach to generalisations of General Relativity and their cosmological implications (2018)](https://arxiv.org/abs/1807.01725)
- [Bahamonde et al. - Teleparallel Gravity: From Theory to Cosmology (2021)](https://arxiv.org/abs/2106.13793) — the comprehensive review of the torsion branch.
