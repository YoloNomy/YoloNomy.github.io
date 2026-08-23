---
layout: default
title: Torsion and gauge gravity
parent: cosmo
---

In the previous classes we went beyond GR by **adding new fields** — a scalar, a vector. Here we do something different and, in a sense, more conservative: we add nothing at all. We simply notice that GR quietly *switched off* a structure that was available from the start, and we switch it back on.

## But why would one set null torsion in GR?

### Two independent structures

A manifold carries **two logically independent** pieces of structure, and it is worth insisting on how independent they really are:

1. a **metric** $g_{\mu\nu}$, which tells you how to measure lengths and angles;
2. an **affine connection** $\Gamma^\rho_{\mu\nu}$, which tells you how to parallel-transport a vector from one point to a neighbouring one, and hence how to differentiate.

Nothing in the definition of a manifold forces these to be related. GR imposes *two extra conditions* by hand:

$$\underbrace{\nabla_\rho g_{\mu\nu} = 0}_{\text{metricity}}, \qquad \underbrace{\Gamma^\rho_{\mu\nu} = \Gamma^\rho_{\nu\mu}}_{\text{no torsion}} .$$

Together these are exactly enough to fix $\Gamma$ uniquely in terms of $g$ — that is the **fundamental theorem of Riemannian geometry**, and the result is the Levi-Civita connection (the Christoffel symbols). The point to appreciate is that this is a *choice*, not a theorem about nature.

### Definitions

$$\boxed{\;T^\rho{}_{\mu\nu} \;\equiv\; \Gamma^\rho_{\mu\nu} - \Gamma^\rho_{\nu\mu} \;=\; 2\,\Gamma^\rho_{[\mu\nu]}\;}\qquad\textbf{torsion}$$

$$\boxed{\;Q_{\rho\mu\nu} \;\equiv\; \nabla_\rho\, g_{\mu\nu}\;}\qquad\textbf{non-metricity}$$

**Torsion is a tensor**, even though $\Gamma$ is not. The proof is one line, and it is exactly the argument we used for $\delta\Gamma$ in the [Brans-Dicke class](./Brans-Dicke.md): under a change of coordinates the connection acquires the inhomogeneous term

$$\frac{\partial x'^\rho}{\partial x^\sigma}\frac{\partial^2 x^\sigma}{\partial x'^\mu\partial x'^\nu},$$

which is **symmetric in $\mu\nu$** because partial derivatives commute. Antisymmetrising therefore kills it. $\square$

This matters enormously. Because $T^\rho{}_{\mu\nu}$ is a tensor, **it cannot be removed by any choice of coordinates**. If it is non-zero anywhere, it is non-zero for every observer.

The general connection then decomposes uniquely as

$$\Gamma^\rho_{\mu\nu} = \underbrace{\genfrac\{\}{0pt}{}{\rho}{\mu\nu}}_{\text{Levi-Civita}} + \underbrace{K^\rho{}_{\mu\nu}}_{\text{contorsion}} + \underbrace{L^\rho{}_{\mu\nu}}_{\text{disformation}},$$

where contorsion is built from torsion, $$K^\rho{}_{\mu\nu} = \tfrac12\big(T^\rho{}_{\mu\nu} + T_\mu{}^\rho{}_\nu + T_\nu{}^\rho{}_\mu\big)$$, and disformation from non-metricity. **GR is the choice $K=L=0$.**

### What torsion means geometrically

The cleanest picture, and the one to remember:

> **Curvature**: parallel-transport a vector around a closed loop and it comes back **rotated**.
> **Torsion**: try to build the loop and it **does not close**.

Concretely: take two infinitesimal vectors $u$ and $v$ at a point. Parallel-transport $u$ along $v$, and $v$ along $u$. In Riemannian geometry the two paths meet — the parallelogram closes. With torsion there is a **gap**, and the gap is precisely $T(u,v)$. Torsion is the failure of infinitesimal parallelograms to close.

A useful mental image from condensed matter: in a crystal, curvature corresponds to *disclinations* (rotational defects) and torsion to *dislocations* (translational defects). This is not merely an analogy — the mathematics is identical.

### So why did Einstein set it to zero?

Four reasons, of very unequal quality.

**1. History.** Riemannian geometry — Riemann, Ricci, Levi-Civita — was built with $T=0$ from the start, and it was the only geometry available in 1915. Cartan introduced torsion in **1922**, seven years *after* GR. Einstein could not have used what did not exist. (Cartan and Einstein then corresponded about it at length in 1929–1932, without agreeing.)

**2. Economy.** With $T=Q=0$, the connection is *determined* by the metric. Allowing torsion means carrying $24$ extra independent components with no obvious source, and GR was already reproducing observations.

**3. A version of the equivalence principle.** With $T=0$ one can always choose coordinates such that $\Gamma^\rho_{\mu\nu}(p)=0$ at a chosen point — this is the local inertial frame, the mathematical expression of "freely falling observers see no gravity". With torsion this is **impossible**, since a tensor cannot be transformed away.

> **But be careful here — this is often overstated.** It does *not* mean torsion violates the WEP. A structureless test particle obeys the equation of motion derived from its action $S = -m\int\sqrt{-g_{\mu\nu}dx^\mu dx^\nu}$, which contains the **metric only**, so it follows an ordinary metric geodesic whatever the torsion does. What fails is only the statement "the connection can be flattened at a point", not "all bodies fall alike". Torsion couples to **spin**, not to mass.

**4. The retrospective reason, and the best one.** As we will see in the next section, in the minimal theory torsion turns out to be **non-propagating** and to vanish identically outside matter. Setting $T=0$ was therefore, by accident, almost harmless. Einstein got the right answer for the wrong reason.

> **A modern footnote: the geometric trinity.** One can build a theory of gravity empirically equivalent to GR out of *any one* of the three ingredients, switching off the other two: curvature (GR), torsion (**TEGR**, teleparallel), or non-metricity (**STEGR**, symmetric teleparallel). The gravitational field is not "curvature" in any absolute sense — that is a representation. See [Beltrán Jiménez, Heisenberg & Koivisto (2019)](https://arxiv.org/abs/1903.06830).

## What could be the impact of torsion?

### Einstein–Cartan theory in three steps

*References: [Cartan 1922]; [Sciama 1964](https://doi.org/10.1103/RevModPhys.36.463); [Kibble 1961](https://doi.org/10.1063/1.1703702); review: [Hehl, von der Heyde, Kerlick & Nester 1976](https://doi.org/10.1103/RevModPhys.48.393).*

**Step 1 — change nothing but the variation.** Keep the Einstein–Hilbert action exactly as it is,

$$S = \frac{1}{16\pi G}\int d^4x\,\sqrt{-g}\;R(g,\Gamma) \;+\; S_m[g,\Gamma,\psi],$$

but now treat $g_{\mu\nu}$ and $\Gamma^\rho_{\mu\nu}$ as **independent variables** and vary with respect to both (the *Palatini* procedure). That is the entire modification. No new field, no new parameter, no new scale.

**Step 2 — vary with respect to the connection.** One obtains

$$T^\rho{}_{\mu\nu} + \delta^\rho_\mu\,T^\sigma{}_{\sigma\nu} - \delta^\rho_\nu\,T^\sigma{}_{\sigma\mu} \;=\; 8\pi G\; s^\rho{}_{\mu\nu},$$

where $$s^\rho{}_{\mu\nu} \equiv \delta S_m/\delta K^{\mu\nu}{}_\rho$$ is the **spin angular momentum density** of matter — the *intrinsic* spin, not orbital.

**Read this equation carefully, because everything follows from its form.** It contains **no derivatives of the torsion**. It is *algebraic*. Therefore:

- **Torsion does not propagate.** There are no torsion waves, no torsion radiation, no extra degrees of freedom.
- **Torsion is strictly local.** It is non-zero exactly where the spin density is non-zero, and vanishes identically outside matter — no $1/r$ tail, no long-range force.
- **In vacuum, Einstein–Cartan *is* general relativity.** Every classical test of GR — light bending, perihelion precession, Shapiro delay, binary pulsars, gravitational waves — is passed automatically, because they are all vacuum measurements.

This is a very unusual situation among the theories in this course: a modification of gravity that costs nothing observationally, because it is invisible by construction rather than by screening.

**Step 3 — substitute back.** Eliminating torsion algebraically leaves an ordinary Einstein equation with an extra piece:

$$G_{\mu\nu}(\{\}) = 8\pi G\left(T_{\mu\nu} + T^{\rm spin}_{\mu\nu}\right),\qquad T^{\rm spin}_{\mu\nu} \sim -\,8\pi G\,s^2 .$$

The spin correction is a **four-fermion contact interaction** (the Hehl–Datta term), schematically $\sim G\,(\bar\psi\gamma^5\gamma^\mu\psi)^2$, and — this is the crucial sign — it enters with a **negative effective energy density**. Gravity acquires a **repulsive** component at very high fermion density.

### When does any of this matter?

Let us estimate it. Spin density $s\sim \hbar n/2$ for $n$ fermions per unit volume. The spin term competes with the ordinary one when

$$\underbrace{G\,s^2}_{\text{spin}} \;\sim\; \underbrace{m\,n}_{\text{mass}} \qquad\Longrightarrow\qquad n \;\sim\; \frac{m}{G\hbar^2} \;=\; \frac{1}{\overline{\lambda}_{\rm C}\,\ell_{\rm Pl}^2},$$

with $\overline{\lambda}_{\rm C}=\hbar/mc$ the Compton wavelength and $\ell_{\rm Pl}$ the Planck length. For nucleons this gives the **Cartan density**

$$\boxed{\;\rho_C \;\sim\; 10^{54}\ \mathrm{g/cm^3}\;}$$

Put it in context:

| | density (g/cm³) |
|---|---|
| water | $1$ |
| neutron star core | $10^{15}$ |
| **Cartan density** | $\mathbf{10^{54}}$ |
| Planck density | $10^{93}$ |

So torsion is utterly negligible for stars — including neutron stars, by nearly forty orders of magnitude. But notice the **second** comparison, which is the interesting one: $\rho_C$ is roughly $10^{-40}$ of the Planck density. Since $\rho\sim T^4$, that means it is reached at a temperature

$$T_C \sim 10^{-10}\,T_{\rm Pl} \sim 10^{9}\ \mathrm{GeV},$$

**ten orders of magnitude below the Planck scale.** Whatever torsion does in the early universe, it does *before* quantum gravity is required. That is what makes Einstein–Cartan cosmology worth taking seriously rather than dismissing as speculation.

### Geodesics or autoparallels?

With torsion, "straightest" and "shortest" come apart:

- **autoparallel** (straightest): $\ddot x^\rho + \Gamma^\rho_{\mu\nu}\dot x^\mu\dot x^\nu = 0$, using the **full** connection;
- **geodesic** (shortest): extremum of $\int d\tau$, using **Levi-Civita only**.

Which one do particles follow? The question sounds deep but the answer is prosaic: **you do not get to choose — the matter action decides.** A structureless particle has $S=-m\int d\tau$, which knows only about $g_{\mu\nu}$, so it follows the metric **geodesic**. Autoparallels are a different curve that nothing forces particles onto.

(Worth adding: for the *totally antisymmetric* torsion that a Dirac field actually generates, the two coincide anyway — the symmetric part of the contorsion vanishes identically.)

Spinning bodies are another matter: their spin precesses relative to the metric-parallel-transported frame. **This is the only way torsion could ever be detected directly.**

### Experimental constraints

Because torsion couples to spin, the tests are spin-polarised experiments, not orbital ones:

- **Torsion-balance and spin-pendulum experiments** (Eöt-Wash), which look for a coupling of electron spin to a hypothetical background torsion field;
- **Lorentz-violation searches** reinterpreted as torsion bounds: [Kostelecký, Russell & Tasson (2008)](https://arxiv.org/abs/0712.4393) obtained limits on constant background torsion components down to $10^{-31}\,\mathrm{GeV}$;
- **Gravity Probe B** was proposed as a torsion probe ([Mao, Tegmark, Guth & Cabi 2007](https://arxiv.org/abs/gr-qc/0608121)), though the claim was contested — in Einstein–Cartan proper, gyroscopes made of unpolarised matter do not couple to torsion at all ([Flanagan & Rosenthal 2007](https://arxiv.org/abs/0704.1447)).

**Be honest about what these bounds mean.** They constrain a hypothetical *background* torsion. They say almost nothing about Einstein–Cartan theory itself, which predicts zero torsion outside matter and is therefore, in its minimal form, essentially **untestable** with present technology.

### Making torsion propagate

If you want torsion to do something observable, you must give it dynamics — that is, put derivatives of torsion into the action. This means quadratic invariants:

$$\mathcal{L} = a_0 R + \sum_i a_i\, T^2 + \sum_j b_j\, R^2 ,$$

the general **Poincaré gauge theory** (PGT), with about ten free parameters. Now torsion propagates and carries massive modes of spin-parity $0^\pm, 1^\pm, 2^\pm$.

The price is severe: **generic parameter choices give ghosts or tachyons.** Only a small number of combinations are healthy ([Sezgin & van Nieuwenhuizen 1980](https://doi.org/10.1103/PhysRevD.21.3269); see [Obukhov 2018](https://arxiv.org/abs/1805.07385) for the modern overview). This is the same Ostrogradsky-flavoured problem that motivated the Horndeski construction, reappearing in the connection sector.

## Gauge theory of gravity

### The gauge principle, in one paragraph

Every other force in the Standard Model comes from the same recipe. Start with a **global** symmetry of the matter action. Demand that it hold **locally** — with a different transformation at each spacetime point. The derivative $\partial_\mu\psi$ then fails to transform covariantly, so you must introduce a **connection** (gauge field) $A_\mu$ and replace $\partial_\mu\to D_\mu=\partial_\mu - igA_\mu$. The **field strength** is the commutator $F_{\mu\nu}\propto[D_\mu,D_\nu]$, and the **Noether current** of the original symmetry is what the gauge field couples to. Electromagnetism is $U(1)$ with current = electric charge; the weak and strong forces are $SU(2)$ and $SU(3)$.

**The obvious question:** can gravity be obtained this way? And if so, from which symmetry?

### Utiyama, Kibble, Sciama

- [**Utiyama (1956)**](https://doi.org/10.1103/PhysRev.101.1597) gauged the **Lorentz** group $SO(1,3)$. He recovered a theory of gravity, but had to introduce the tetrad **by hand** — unsatisfying, because the gauge principle was supposed to produce it.
- [**Kibble (1961)**](https://doi.org/10.1063/1.1703702) and [**Sciama (1964)**](https://doi.org/10.1103/RevModPhys.36.463) fixed this by gauging the **full Poincaré group** $ISO(1,3)$ = translations $\ltimes$ Lorentz. Now everything appears automatically — and what comes out is **Einstein–Cartan theory**, torsion included.

**This is the key result of the whole class:** if you insist that gravity be a gauge theory in the same sense as electromagnetism, you do not get GR. **You get Einstein–Cartan.** Torsion is not an optional decoration; it is the field strength that the gauge principle hands you, and setting it to zero is an extra assumption imposed afterwards.

### The dictionary

| symmetry gauged | gauge field | field strength | Noether current it couples to |
|---|---|---|---|
| $U(1)$ | $A_\mu$ | $F_{\mu\nu}$ | electric charge |
| Lorentz $SO(1,3)$ | spin connection $\omega^{ab}{}_\mu$ | **curvature** $R^{ab}{}_{\mu\nu}$ | **spin** angular momentum |
| translations | tetrad $e^a{}_\mu$ | **torsion** $T^a{}_{\mu\nu}$ | **energy–momentum** |

Read the last two rows together. The Poincaré group has two factors, so gravity has *two* field strengths, and they pair with the *two* conserved currents of relativistic matter. GR uses only half of the structure. Torsion is the missing half.

### Why gravity is not quite Yang–Mills

Three genuine differences, worth stating so that the analogy is not oversold:

1. **The tetrad is a soldering form, not a connection.** It carries one internal index $a$ and one spacetime index $\mu$, and it *identifies* the internal space with the tangent space. Nothing like this exists in Yang–Mills theory, and it is why gravity has a metric at all.
2. **The coupling constant is dimensionful.** $[G]=\mathrm{mass}^{-2}$, whereas $e$ and $g$ are dimensionless — hence non-renormalisability.
3. **The gauge group acts on spacetime itself**, not on an internal space, so "gauge transformations" include diffeomorphisms.

### Teleparallel gravity: the opposite extreme

If Einstein–Cartan keeps curvature and *adds* torsion, **teleparallel gravity** does the reverse: it sets the **curvature to zero** and lets torsion carry the entire gravitational field. This is the gauge theory of **translations alone**, using the Weitzenböck connection. Its action is built from the torsion scalar $\mathbb{T}$, and remarkably

$$R(\{\}) = -\mathbb{T} + (\text{total derivative}) \qquad\Longrightarrow\qquad \textbf{TEGR is exactly equivalent to GR}.$$

Same equations, same predictions, completely different geometry: in TEGR spacetime is *flat*, and gravity is a force again, mediated by torsion. Free particles do not follow geodesics — they are pushed.

The reason cosmologists care is what happens when you deform it. Just as $f(R)$ generalises GR, $f(\mathbb{T})$ generalises TEGR — but because the equivalence only held up to a total derivative, **$f(R)$ and $f(\mathbb{T})$ are genuinely different theories.** $f(\mathbb{T})$ has second-order field equations (unlike $f(R)$) which is attractive.

> **The catch, and it is serious.** $f(\mathbb{T})$ **breaks local Lorentz invariance**: the torsion scalar $\mathbb{T}$ is not a Lorentz scalar, only invariant up to the total derivative that $f$ destroys. Different tetrads describing the *same* metric then give *different* physics, and the theory carries extra, poorly understood degrees of freedom. This is not a technicality; it is why many relativists regard $f(\mathbb{T})$ with suspicion despite its popularity in the cosmology literature.

## Torsion and cosmology

### The spin fluid

To do cosmology we need a macroscopic description of spinning matter. The standard one is the **Weyssenhoff fluid**: a perfect fluid whose constituents carry intrinsic spin. On a homogeneous, isotropic background, the *average* spin vector must vanish (isotropy!), but the *square* of the spin density does not — so what survives is a term $\propto s^2$.

Since spin density is proportional to number density,

$$s \;\propto\; n \;\propto\; a^{-3} \qquad\Longrightarrow\qquad s^{2}\;\propto\;a^{-6}.$$

### The modified Friedmann equation

$$\boxed{\;H^2 = \frac{8\pi G}{3}\Big(\rho \;-\; \alpha\,G\,s^{2}\Big) - \frac{K}{a^{2}}\;}$$

with $\alpha$ a positive number of order unity (conventions differ; see [Poplawski](https://arxiv.org/abs/1007.0587), [Gasperini](https://doi.org/10.1103/PhysRevLett.56.2873)).

Now compare the scalings and the punchline writes itself:

| component | scaling |
|---|---|
| matter | $a^{-3}$ |
| radiation | $a^{-4}$ |
| **spin–spin (negative!)** | $\mathbf{a^{-6}}$ |

The negative term **grows fastest** as $a\to0$. So no matter how small it is today, it *must* eventually dominate on the way back in time. When it does, $H^2\to0$ and then would go negative — which is impossible, so instead the universe reaches a minimum size and **bounces**.

$$\textbf{The Big Bang singularity is replaced by a bounce at }\rho\simeq\rho_C\sim10^{54}\ \mathrm{g/cm^3}.$$

This is a genuinely remarkable claim: singularity avoidance from **classical** physics, with **no new fields, no new parameters, and no new scale** — only the observation that fermions have spin and that Einstein set torsion to zero without checking. It goes back to [Trautman (1973)](https://doi.org/10.1038/physci242007a0) and has been developed extensively since, notably by Popławski, who argues that the same mechanism operates inside black holes: every black hole would bounce into a new expanding region.

Related lines of work: torsion-driven **inflation** (the spin term can also produce a brief accelerating phase), and **$f(\mathbb{T})$ dark energy** in the teleparallel language.

### An honest assessment

Let us end this class the way we ended the one on screening, by asking whether we should believe any of it.

**In favour.** The theory is *minimal* in a way none of the others in this course are: no free parameter, no new field, no tuning. It is what the gauge principle gives you when applied honestly to the Poincaré group. It passes every existing test automatically. And it resolves the Big Bang singularity — the deepest known failure of GR — at an energy scale ten orders of magnitude below where we would have to admit ignorance about quantum gravity.

**Against.** The same feature that makes it safe makes it nearly empty. Torsion does not propagate, vanishes outside matter, and becomes relevant only at $10^{40}$ times nuclear density. **There is currently no realistic prospect of testing Einstein–Cartan theory.** The bounce is a genuine prediction, but it concerns an epoch we observe only through its late-time relics, and inflation efficiently erases what came before it. Meanwhile the versions that *would* be testable — propagating torsion, $f(\mathbb{T})$ — pay for that testability with ghosts or with broken Lorentz invariance.

**A fair verdict.** Torsion is best regarded not as a phenomenological model competing with $\Lambda$CDM, but as a **structural correction to how we formulated GR in the first place**: the statement that Einstein's theory was written in a geometry that was, historically speaking, one step too narrow. Whether nature uses that extra room is a separate question, and one we currently have no way to answer.

## Further reading

- [Hehl, von der Heyde, Kerlick & Nester - *General relativity with spin and torsion* (1976)](https://doi.org/10.1103/RevModPhys.48.393) — still the standard reference. Read §1–3.
- [Blagojević & Hehl - *Gauge Theories of Gravitation* (2013)](https://arxiv.org/abs/1210.3775) — a reader with commentary on the original papers, including Utiyama, Kibble and Sciama.
- [Obukhov - *Poincaré gauge gravity: an overview* (2018)](https://arxiv.org/abs/1805.07385)
- [Beltrán Jiménez, Heisenberg & Koivisto - *The Geometrical Trinity of Gravity* (2019)](https://arxiv.org/abs/1903.06830) — curvature, torsion and non-metricity as three equivalent languages.
- [Hehl - *Élie Cartan's torsion in geometry and in field theory, an essay* (2007)](https://arxiv.org/abs/0711.1535) — the history, including the Cartan–Einstein correspondence.
