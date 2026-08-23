---
layout: default
title: Lovelock theorem
parent: cosmo
---

## How to modifiy gravity?

If one wants to come up with a modified theory of gravity that is not GR, one must find a way around two very powerful theorems: **the Lovelock theorem** and the **Weinberg-Deser** theorem. The first comes from the [geometric understanding of GR](./foundations-GR.md), the second from the [field point of view](./GR_fieldtheory.md).
Both theorems say that GR is the only possible theory under some suitable assumptions. Neither is a prohibition on modifying gravity — each is really a **list of assumptions**, and every modified-gravity theory in the literature is obtained by breaking one of them.

### Lovelock's theorem

This famous theorem is due to [Lovelock (1971)](https://pubs.aip.org/aip/jmp/article-abstract/12/3/498/223441/The-Einstein-Tensor-and-Its-Generalizations?redirectedFrom=fulltext). It says that in **four** spacetime dimensions, the only symmetric, rank-2, divergence-free tensor that can be built **locally** from the **metric alone** and its derivatives up to **second order** is
$$\alpha\,G^{\mu\nu}+\Lambda\,g^{\mu\nu}$$. So this is the only tensor field we can hope to couple with the stress-energy tensor of matter $T_{\mu\nu}$ in a field equation.
Equivalently put:

> **The Einstein-Hilbert action with a cosmological constant is the *only* local, diffeomorphism-invariant action of the metric alone whose field equations are second order in 4D.**

This theorem thus relies on the following assumptions we can break (with parallel to the first class axioms we proposed):

| | Assumption | [First class](./foundations-GR.md) |
|---|---|
| **L1** | Four spacetime dimensions | Hidden in S1 |
| **L2** | The metric $g_{\mu\nu}$ is the only field | Assumption S2 | 
| **L3** | Field equations of at most second order in derivatives | Hidden in D1 |
| **L4** | Diffeomorphism invariance | Hidden in the tensorial formalism (inherited from general covariance discussion) |
| **L5** | Locality, and the equations follow from an action | Hidden in D1 and D2 |
| **L6** | *(implicit)* The connection is the Levi-Civita connection of $g$ — no torsion, no non-metricity | S3 |

### Weinberg-Deser theorem 

Now, we already discussed extensively the field theoretic understanding of GR in the [dedicated class](./GR_fieldtheory.md). This allows us to propose what is sometimes called the **Weinberg-Deser theorem**:

> **General relativity is the unique consistent low-energy theory of a single self-interacting massless spin-2 field on flat four-dimensional spacetime.**

This was reached historically by two independent arguments, that we quickly covered in the dedicated class:

- **Weinberg (1964, 1965)** — Lorentz invariance and unitarity of the $S$-matrix for a massless spin-2 particle force the coupling to matter to be *universal* (this is the equivalence principle, derived rather than assumed), and force the low-energy field equations to be Einstein's. The same soft-theorem argument also forbids consistent long-range forces mediated by massless spin $>2$.
- **Deser (1970)** — the bootstrap: coupling Fierz-Pauli to its own conserved stress-energy tensor and iterating closes on the Einstein-Hilbert action. In first-order (Palatini) variables the iteration terminates after a single step.

This theorem relies on the following assumptions:

| | Assumption |
|---|---|
| **W1** | Exactly **one** spin-2 field |
| **W2** | It is exactly **massless** |
| **W3** | Poincaré (Lorentz) invariance |
| **W4** | Unitarity / positive energy — no ghosts |
| **W5** | Locality |
| **W6** | Two-derivative, i.e. leading order in a derivative expansion |
| **W7** | Four dimensions |
| **W8** | Flat (Minkowski) background |
| **W9** | No other light fields coupling to matter |

### The ways around

Now that the assumptions making GR unavoidable have been laid down, we can propose ways to break them. In this table we go a bit ahead of ourselves and give presentations of some theories that will be later discussed in detail. Use it as an overview of the road ahead of us!

| Assumption dropped | Breaks | What you get | Price you pay |
|---|---|---|---|
| **Add extra fields** | L2, W9 | *Scalar-tensor*: Brans-Dicke, quintessence, Horndeski, DHOST. *Vector-tensor*: Einstein-Aether, TeVeS, generalised Proca. *Tensor-tensor*: bigravity | Fifth forces may pop, so you need a screening mechanism (chameleon, symmetron, Vainshtein). Furthermore, **GW170817** ($\vert c_T/c-1\vert\lesssim10^{-15}$) eliminated many possibilities (see the [Horndeski](./Horndeski.md) class).|
| **Allow higher derivatives** | L3, W6 | $f(R)$; Stelle quadratic gravity ($R^2$, $R_{\mu\nu}R^{\mu\nu}$); scalar-Gauss-Bonnet; infinite-derivative gravity | **Instability** (Ostrogradsky ghost) generically. $f(R)$ escapes only because it is degenerate — it is secretly an $\omega=0$ Brans-Dicke theory, i.e. really the row above. Stelle gravity is renormalizable but carries a massive spin-2 ghost |
| **Go to $D>4$** | L1, W7 | Lovelock / Gauss-Bonnet gravity in $D\geq5$, braneworlds (DGP, Randall-Sundrum), Kaluza-Klein | The extra dimensions must be hidden; the DGP self-accelerating branch has a ghost |
| **Give up locality** | L5, W5 | $f(R/\Box)$, $R\,\Box^{-2}R$, non-local infinite-derivative gravity | The Cauchy problem and causal structure become obscure; predictivity is hard to establish |
| **Break diffeomorphism or Lorentz invariance** | L4, W3 | Hořava-Lifshitz (anisotropic scaling), unimodular gravity (restricted/TDiff), Einstein-Aether, Lorentz-violating massive gravity | An extra propagating scalar and strong-coupling problems; Lorentz violation in the matter sector is bounded at the $10^{-15}$-$10^{-20}$ level |
| **Give the graviton a mass** | W2 (and W3, since a mass term breaks diffeos) | Fierz-Pauli massive gravity → **dRGT**; the resurrected interest in the FP mass term | **vDVZ discontinuity** (cured by Vainshtein screening), **Boulware-Deser ghost** (cured only by the specific dRGT potential tuning); ongoing acausality/superluminality debates; $m_g\sim10^{-23}$ eV from LVK dispersion tests |
| **Use more than one spin-2 field** | W1 | Hassan-Rosen bigravity, multi-gravity | Ghost-freedom again requires the dRGT potential; only one massless combination survives, the rest are massive |
| **Expand around a curved background** | W8 | **Partially massless** gravity in de Sitter (Deser-Waldron); higher-spin theories in (A)dS | The PM gauge symmetry exists only at the tuned value $m^2=2\Lambda/3$ in 4D, and no consistent nonlinear completion is known |
| **Accept ghosts** | W4 | Stelle quadratic gravity; "fakeon" prescriptions | Negative-norm states — you need a nonstandard quantisation prescription to make sense of it at all |
| **Change the connection** | **L6** | Einstein-Cartan, metric-affine gravity, Poincaré gauge theory, $f(T)$, $f(Q)$ | TEGR and STEGR are *identical* to GR, so no escape there at all. $f(T)$ breaks local Lorentz invariance and has strongly coupled extra modes; $f(Q)$ has been argued to carry a ghost |
| **Abandon the action principle** | L5 | Thermodynamic / entropic gravity, emergent-gravity programmes | Usually no systematic calculational scheme, hence little predictivity |
| **Massless spin $>2$** | Weinberg's soft theorem | String theory (an infinite tower, all massive above the graviton); Vasiliev higher-spin gravity | Only works with an **infinite** tower of fields and, for Vasiliev, $\Lambda\neq0$ — so there is no flat-space $S$-matrix, which is precisely how the no-go is dodged |

Three remarks regarding the table:

1. **The routes are not independent.** $f(R)$ appears under "higher derivatives" but is equivalent to a scalar-tensor theory, i.e. "extra fields". Massive gravity appears under "graviton mass" but, once the broken diffeomorphisms are restored with Stückelberg fields, is again "extra fields". In practice almost everything collapses onto **extra degrees of freedom**, and the real question is always *how many extra modes, and is one of them a ghost?*
2. **Lovelock's L6 is usually left unstated**, which is why the geometric trinity often looks like it violates the theorem. It does not: Lovelock assumes from the start that $\nabla$ is the Levi-Civita connection of $g$. Relax that and torsion/non-metricity theories become a legitimate exit — though the two *equivalent* formulations (TEGR, STEGR) walk straight back in through the front door.
3. **Weinberg-Deser is a statement about low energies.** It says nothing about the ultraviolet: GR is the unique two-derivative theory, but higher-derivative operators suppressed by a cutoff are allowed and generically present. That is exactly the effective-field-theory reading of gravity, and it is why "GR is unique" and "GR is an EFT that must break down" are both true.

## The landscape of modified gravity theories

Theories can thus be classified by the way the go around Lovelock and/or Weinberg-Deser theorems to produce an alternative to GR. These different roads are sketched on Figure 1 and 2.

![image](../pictures/modgrav-map.png){: width="80%"} 

*Figure 1: The routes to modified gravity from Lovelock theorem, from [Ishak et al. (2018)](https://arxiv.org/pdf/1806.10122).*

![image](../pictures/Baker-landscape.png){: width="80%"} 

*Figure 2: The landscape of modified gravity, from [Tessa Baker's website](https://www.tessabaker.space/images/map_slide_v2.pdf).*

That's a lot of theories, and clearly we can not cover them all! We will just have a look at the better understood ones and lay general principles.
Once we propose a theory, we must always check, in order: 

- Understand the theory and its physical motivations, where does it stands on the landscape of Figure 1? 
- Look at the Lagrangian (if it has one)
- Derive from it the equations of motion for the background
- Look at perturbations
- Ask: does it violate the EEP (is it metric)? Does it violate the SEP? Get **constraints** from it.
- Look at the PPN parameters: Get **constraints** from it.
- How do gravitational wave propagates and how does it compare with data? Get **constraints** from it.
- Which fundamental constants vary if any and how does it compare with data? Get **constraints** from it.
- Compute cosmological perturbations and observables. Get **constraints** from it.

Let's be fair: studying modified gravity is not an easy job! 

