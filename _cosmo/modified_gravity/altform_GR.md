---
layout: default
title: Palatini action, forms and tetrads and ADM formalism
parent: cosmo
---

As we said many times, before trying to understand "beyond GR" it is absolutely critical to understand GR in all of its aspects and this is far from an easy task (The MTW *Gravitation* book is 1279 pages long and a lot more has been found since then!). Here we review some other theoretical aspects of GR that you might encounter in your reading of modified gravity. You can safely skip this lecture and go back to it if need be in the future.

Each section is organised the same way: **what the formalism is**, **the minimum you need to read a paper**, and **why it shows up in modified gravity**. Here is the map:

| formalism | the one-line reason it exists | where you will meet it |
|---|---|---|
| **Palatini** | metric and connection need not to be tied together, one can minimize the action with respect to both $g$ and $\Gamma$ | $f(R)$ ambiguities, Einstein–Cartan etc |
| **Tetrads & forms** | you cannot write spinors with coordinate indices. They are also useful for a deep geometric understanding of GR | teleparallel gravity, supergravity, LQG |
| **ADM (3+1)** | you cannot do Hamiltonian mechanics without a time | counting d.o.f., finding ghosts, EFT of dark energy, quantum gravity |
| **Geometric algebra** | spinors, vectors, forms and tensors in one single algebra. The fundamental building blocks of space-time are all related and are spinors! | gauge theories gravity |
| **Killing vectors** | symmetries give conserved quantities | every exact solution for the metric you will ever meet will admit these symmetries |


## The Palatini formulation

In the [standard formulation of GR](./foundations-GR.md), we write the Einstein–Hilbert action, declare that $\Gamma$ is the Levi-Civita connection expressed in term of $g$, and vary with respect to the metric alone.

The **Palatini** (or *first-order*, or *metric-affine*) formulation does something more general: it treats $$g_{\mu\nu}$$ and $$ \Gamma^\rho{}_{\mu\nu} $$ as **independent** variables, and varies with respect to both. In a sense this drops the S2 assumption stating that $g$ is the only dynamical quantity of gravity. Notice how neatly the action separates when you do this:

$$S = \frac{1}{16\pi G}\int d^4x\; \underbrace{\sqrt{-\vert g\vert }\,g^{\mu\nu}}_{\text{metric only}}\;\underbrace{R_{\mu\nu}(\Gamma)}_{\text{connection only}} \;+\; S_m[g,\psi].$$

The Ricci tensor $$R_{\mu\nu}(\Gamma)$$ is built purely from the connection; the metric appears only in the prefactor. Vary the action with respect to $\Gamma$ only, assuming using the Palatini identity $$\delta R_{\mu\nu} = \nabla_\rho\,\delta\Gamma^\rho{}_{\mu\nu} - \nabla_\nu\,\delta\Gamma^\rho{}_{\rho\mu}$$ (the same identity we used in the [first class](./foundations-GR.md)), integrate by parts, and you obtain after a few manipulations:

$$\nabla_\rho\, g_{\mu\nu}=0$$

which is the definition of a metric connection!

<details markdown="1">
  <summary><strong>Proof: the connection field equation gives metricity</strong></summary>

*in prep*

</details>


**This is a genuinely satisfying result.** The fact that our connection should be metric compatible is not as much as an ad-hock postulate, as it looks — it is a **field equation** (we called this postulate S3a in the [first class](./foundations-GR.md)). "Metricity" is something GR *derives* rather than assumes, provided you were willing to let the connection be free in the first place. 

If you ask as an additional postulate that the connection is **torsion free**, you immediately get the unique Levi-Civita connection (adding S3b implies the full S3). If you do not make further assumption and thus allow the connection to be non-symmetric, the same variation no longer gives GR: it gives **Einstein–Cartan** theory, with torsion algebraically determined by spin. That is precisely the [topic of a future class](./torsion.md).

<!-- In a complex fashion, this fact is related to the notion of **projective invariance** i.e. that the Einstein–Hilbert action is invariant under $$\Gamma^\rho{}_{\mu\nu}\to\Gamma^\rho{}_{\mu\nu}+\delta^\rho{}_\mu\,\xi_\nu$$ for arbitrary covector $\xi$, so the solution above is really "Levi-Civita up to a projective transformation". This must be gauge-fixed, and forgetting to do so has produced confusion in the literature. We will not discuss this in detail here.  -->

Now here is the reason why all of this is is so important. For the *linear* action of GR the two procedures agree. For more general Lagrangians, as $f(R)$ they do **not**, and even worse they give very different theory. **Hence:** *a theory of modified gravity, as "$f(R)$ gravity" is not a theory until you say which variational principle you meant.* The same Lagrangian gives two inequivalent theories. See [Sotiriou & Faraoni (2010)](https://arxiv.org/abs/0805.1726) for the full story.

## Tetrads, forms and gauge formulation of gravity

Now, what if we want to introduce spinor fields within GR? This happens to be simply impossible in the standard formulation of GR in term of $g$. The group of diffeomorphisms/frame transition is $GL(4,\mathbb{R})$ and has no finite-dimensional spinor representations; only the Lorentz group does. So to put an electron on a curved spacetime you *must* introduce, at each point, a local Lorentz frame. Thanksfully, this is easy as we know that space-time is locally Lorentzian, it is always possible to find at each point (event) an inertial (free falling frame) in which $g=\eta$. Note that this is not possible **globally**: such a transformation exist at each point but no single transformation can set $g=\eta$ at every point simultaneously, unless space-time is flat.

The proper understanding of the subtleties of general relativity and modern physics as a whole requires the understanding of differential geometry and $p$-forms. There is simply no way around it and we already spread a bit of it everywhere in this class. Unfortunately, this is a vast and rich topic that we can not cover here. I could not recommend you enough to read the following references which are my personal favorites: [Baez & Muniain (1994)](https://pages.jh.edu/rrynasi1/PhysicalPrinciples/literature/Baez+Muniain1994GaugeFieldsKnots+Gravity.pdf), [Frankel (1997)](https://api.pageplace.de/preview/DT0400.9781139154147_A23866698/preview-9781139154147_A23866698.pdf), [Coqueraux (2016)](https://www.cpt.univ-mrs.fr/~coque/EspacesFibresCoquereaux.pdf) (for french speakers) and [Nakahara (2003)](http://www.stat.ucla.edu/~ywu/GTP.pdf). We will simply gloss here over the details, such that you might get a glance of the meaning of the formalism.

**I might write a general introduction to geodiff here in the future, possibly in an expandable box.**

When one use vectors and co-vectors $u^\mu$ or $w_\nu$ one should keep in mind that these are just the coordinates of geometric objects, expressed in a local frame, itself associated to a local chart. Indeed, when doing so, one always implicitly choose some frames $e_\mu(x)$ of the tangent space at every point of some region of space-time. The geometric vectors and covectors are really $u= u^\mu e_\mu$ or $\omega=\omega_\nu e^\nu$ and we keep their components only as an, often confusing, abuse of notation. The covector frame $e^\nu$ is defined such that $e^\mu e_\nu=\delta^\mu_\nu$ In differential geometry, a preferred choice of frames, the **natural frames** are given by the differential operators $e_\mu = \partial_\mu$ and $e^\mu = \text{d}x^\mu$, such that the frames are pointing in the direction of the coordinate lines $x^\mu$ of the space-time chart (This is at first extremely confusing for physicist. However differential operators really form a natural basis of the vector space $TM$ at each space-time point and is the genuinely smart choice to consider. If you are too confused about this, just forget about it for now).

Identically, when one consider the metric tensor $g_{\mu\nu}$, one is really just playing with the coordinates of the geometric object:

$$g= g_{\mu\nu}e^\mu \otimes e^\nu$$

where $\otimes$ is the tensor product. $g$ acts on vectors as $$g(u,v)= g_{\mu\nu}e^\mu \otimes e^\nu (u^\lambda e_\lambda, v^\rho e_\rho) = g_{\mu\nu}u^\mu u^\nu$$ and the coordinates are obtained as $$g_{\mu\nu}=g(e_\mu, e_\nu)$$. If you are completely lost at this point, have a look at these wonderful [video classes](https://www.youtube.com/watch?v=_pKxbNyjNe8&list=PLRlVmXqzHjUQARA37r4Qw3SHPqVXgqO6c).

Now, the fact that $M$ is locally Lorentzian means that there exist a special frame $$\tilde{e}_\mu$$ at every point of space-time in which $g=\eta$ i.e. $$g(\tilde{e}_\mu,\tilde{e}_\nu)= \eta_{\mu\nu}$$. We now note $$e^a{}_\mu$$ the transformation going from the natural frame $e_\mu$ to the inertial frame $$\tilde{e}_a$$: $$e_\mu = e^a{}_\mu \tilde{e}_a$$. That's a lot of $e$ and some quite confusing notations, but this is aligned with the literature. 

$$ g_{\mu\nu} = g(e_\mu, e_\nu) = g(e^a{}_\mu \tilde{e}_a,e^a{}_\mu \tilde{e}_a) =e^a{}_\mu e^a{}_\mu g(\tilde{e}_a, \tilde{e}_a) = e^a{}_\mu e^a{}_\mu \eta_{ab}  $$

that is:

$$\boxed{\;g_{\mu\nu} = \eta_{ab}\;e^a{}_\mu\,e^b{}_\nu\;}$$

$e^a{}_\mu$ is known as the **tetrad**, **vierbein**, or **frame field**.
Read this as: the tetrad is the "square root of the metric. Latin indices $a,b$ label the **local Lorentz frame**; Greek indices $\mu,\nu$ label **coordinates**.

Count: $$e^a{}_\mu$$ has $16$ components, $g_{\mu\nu}$ has $10$. The extra $6$ are exactly the dimension of the Lorentz group — the freedom to rotate/boost the frame at each point without touching the metric. **This local Lorentz symmetry is new gauge freedom that the metric formulation does not have**, and it is the whole reason $f(\mathbb{T})$ gravity is problematic (see the [trinity class](./Trinity.md)).

To differentiate objects carrying Latin indices you need a second object, the **spin connection** $\omega^{ab}{}_\mu$, antisymmetric in $ab$.

This is where the formalism becomes beautiful. Package the tetrad and connection as **differential forms** (i.e. write the covectors in their natural basis):

$$e^a = e^a{}_\mu\,dx^\mu \quad(\text{1-form}), \qquad \omega^a{}_b = \omega^a{}_{b\mu}\,dx^\mu \quad(\text{1-form}).$$

Then the two fundamental tensors of geometry are just:

$$\boxed{\;T^a = de^a + \omega^a{}_b\wedge e^b\;}\qquad\textbf{torsion (1st structure equation)}$$

$$\boxed{\;R^a{}_b = d\omega^a{}_b + \omega^a{}_c\wedge\omega^c{}_b\;}\qquad\textbf{curvature (2nd structure equation)}$$

with the **wedge product** $$a\wedge b = a\otimes b - b\otimes a$$. These are the so called **Cartan structure equations**. Two whole pages of Christoffel symbols compress into two lines. Anyone who had the chance to look at gauge theories from the geometric perspective will recognize that the second term (curvature) is **exactly the Yang–Mills field strength** $F = dA + A\wedge A$, with the spin connection playing the role of the gauge field. Compare it with the first: torsion is the field strength of the **tetrad**. This is a strong connection between gauge theories and gravity. We will rediscuss this in the [gauge gravity class](./Torsion.md):

The Einstein-Hilbert action becomes (sometimes called the **Palatini–Cartan** action):

$$S_{\rm EH} = \frac{1}{4\kappa}\int \epsilon_{abcd}\;e^a\wedge e^b\wedge R^{cd},$$

varied independently with respect to $e^a$ and $\omega^{ab}$ (conventions on the prefactor vary). Here $\kappa=4\pi G$ is written separately in order to hilight the symmetry of this action with the Yang-Mills action ($\propto 1/4 F\wedge \star F$). Note that this action is linear in curvature while Yang-Mills is quadratic. No metric determinant, no $\sqrt{-\vert g\vert }$, no Christoffels — the volume element is generated by the wedge products themselves.

This formalism, beside being extremely beautiful, is useful in multiple contexts:

- **Teleparallel gravity** is naturally written in tetrads (indeed it *must* be — see the [trinity class](./Trinity.md)).
- **Loop quantum gravity** starts from the Palatini–Cartan action plus the **Holst term**, whose coefficient is the Barbero–Immirzi parameter.
- **Supergravity** is unwritable without tetrads, because supersymmetry relates the graviton to a spin-3/2 field.
- **Lovelock, Gauss–Bonnet and Chern–Simons terms** are one-line expressions in form language and horrible in index notation.

## The ADM formalism

Hamiltonian mechanics needs a time. General relativity does not come with one. The **ADM** (Arnowitt–Deser–Misner) formalism supplies one by hand: **slice spacetime into a family of spatial hypersurfaces** labelled by a time coordinate $t$, and rewrite everything in terms of what lives on a slice and how slices are stacked.

$$\boxed{\;ds^2 = -N^2\,dt^2 + \gamma_{ij}\left(dx^i + N^i dt\right)\left(dx^j + N^j dt\right)\;}$$

with three ingredients, all with direct geometrical meaning:

| symbol | name | meaning |
|---|---|---|
| $N$ | **lapse** | proper time elapsed per unit $t$, for an observer moving normal to the slice |
| $N^i$ | **shift** | how much the spatial coordinates slide sideways from one slice to the next |
| $\gamma_{ij}$ | **spatial metric** | the geometry *within* a slice |

Count: $1+3+6 = 10$ ✓ — the same information as $g_{\mu\nu}$, repackaged.

The "velocity" of the geometry is the **extrinsic curvature**

$$K_{ij} = \frac{1}{2N}\left(\dot\gamma_{ij} - D_iN_j - D_jN_i\right),$$

with $D_i$ the covariant derivative within the slice. The action becomes (Gauss–Codazzi)

$$S = \frac{1}{2\kappa}\int dt\,d^3x\;\sqrt{\gamma}\;N\left({}^{(3)}\!R + K_{ij}K^{ij} - K^2\right).$$

**Look for time derivatives of $N$ and $N^i$. There are none.** They are not dynamical variables at all — they are **Lagrange multipliers**. Varying with respect to them produces not equations of motion but **constraints**:

$$\underbrace{ {}^{(3)}\!R + K^2 - K_{ij}K^{ij} = 2\kappa\rho}_{\textbf{Hamiltonian constraint (from } N)}, \qquad \underbrace{D_j\!\left(K^{j}{}_i - \delta^j{}_i K\right) = \kappa\, j_i}_{\textbf{momentum constraint (from } N^i)} .$$

And now the payoff — the cleanest derivation of a famous number:

- $\gamma_{ij}$ has $6$ components and $6$ conjugate momenta: $\mathbf{12}$ phase-space dimensions;
- there are $4$ first-class constraints, each removing $2$ phase-space dimensions: $-\mathbf{8}$;
- leaving $4$ phase-space dimensions $=$ $\mathbf{2}$ configuration-space degrees of freedom.

**The two polarisations of the graviton**, obtained by counting rather than by solving anything. This is the most practically important formalism in the list, because **it is how you find out whether your theory is sick.**

- **The Boulware–Deser ghost.** In the [massive gravity class](./Massive-gravity.md) we will see that a graviton mass makes the lapse appear *quadratically*, so it stops being a Lagrange multiplier, the Hamiltonian constraint is lost, and a sixth (ghostly) mode propagates. That statement is an ADM statement, and dRGT is precisely the tuning that keeps $N$ linear. **The whole 40-year problem of massive gravity is a statement about the lapse.**
- **Degeneracy conditions.** "Beyond Horndeski" and DHOST theories are *defined* by degeneracy of the kinetic matrix in ADM form — that is what lets them have higher-order equations without an Ostrogradsky ghost.
- **The EFT of dark energy** is constructed in ADM variables, in the *unitary gauge* where the scalar field is used as the time coordinate ($\phi = \phi(t)$, so slices of constant $\phi$ *are* the slices).
- **The $f(\mathbb{T})$ controversy** we mention in the [trinity class](./Trinity.md) is a disagreement between Hamiltonian analyses.
- **Numerical relativity** — every binary-merger waveform ever computed — evolves the ADM (or BSSN) equations.

**A parting curiosity.** The Hamiltonian constraint says $\mathcal{H}=0$: the total Hamiltonian of a closed universe vanishes. Quantising naively gives the Wheeler–DeWitt equation $\hat{\mathcal{H}}\Psi=0$, a Schrödinger equation with **no time in it**. This is the *problem of time* in quantum gravity, and it is a direct descendant of the innocuous observation that $\dot N$ does not appear in the action.


## Geometric algebra

**Geometric (Clifford) algebra** replaces the usual zoo — vectors, tensors, differential forms, spinors, each with its own rules — with a **single associative product**. For two vectors,

$$\boxed{\;ab = \underbrace{a\cdot b}_{\text{symmetric, scalar}} + \underbrace{a\wedge b}_{\text{antisymmetric, bivector}}\;}$$

Applied to spacetime, the generators $\gamma_\mu$ obey

$$\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2\eta_{\mu\nu},$$

which you will recognise instantly: **it is the Dirac algebra**. The point is that the $\gamma_\mu$ are being treated here as *basis vectors of spacetime*, not as matrices acting on some auxiliary spinor space. Vectors, bivectors (= 2-forms = the Lorentz algebra), and spinors all become elements of one algebra, and rotations are written as $a \to R\,a\,\tilde R$ with $R = e^{-B/2}$ for a bivector $B$ — the same formula for spacetime rotations of vectors and of spinors.

Authors as [Lasenby, Doran & Gull 1998](https://doi.org/10.1098/rsta.1998.0178) used this to build **Gauge Theory Gravity (GTG)**: gravity formulated on a **flat background** as a genuine gauge theory of two symmetries, position-gauge (translations) and rotation-gauge (Lorentz), with no curved manifold anywhere in the formalism.

**Be clear about the status.** GTG is *physically equivalent to Einstein–Cartan theory* — same predictions, torsion sourced by spin. It is a **reformulation**, not a new theory, and it makes no new predictions. What its advocates claim is conceptual and practical: spinors are treated on the same footing as everything else, global and topological questions are posed differently (their treatment of the $r=0$ region of black holes is notably distinct), and calculations are often shorter.

**An honest assessment:** the formalism is elegant and under-used, but it has not been widely adopted, and you should not expect to need it. Know that it exists, so that when you open a paper by the Cambridge group on ghost-free Poincaré gauge theory and find no indices anywhere, you know what you are looking at.

## Other useful concepts: Killing vectors and Lie Derivative

### Lie derivative

As we said many times, on a bare manifold, there is no way to differentiate a tensor field. The obstruction is that $T_{\mu\nu}(x)$ and $T_{\mu\nu}(x+\mathrm{d}x)$ live in **different** vector spaces — different tangent spaces — and subtracting them is meaningless: there is no canonical identification between them. This is exactly why $\partial_\lambda T_{\mu\nu}$ is not a tensor.

We already know one way out: introduce a **connection** $\nabla$, which is the **definition** of parallelism on $M$ that is a definition of how to parallel-transport a tensor from one point to the other so that the two can be compared. But we saw in the Palatini section above that $\nabla$ is *extra structure* — a choice, and in metric-affine gravity a dynamical field in its own right.

There is a second, cheaper way out, and it needs **nothing at all** beyond the manifold: no metric, no connection. That is the **Lie derivative**.

The idea is to drag the tensor along a flow defined by a vector. Let me insist on this again: if you do not follow a proper class on differential geometry **all of the following content will look, at best obscure**. I try however (and possibly fail) to write it in a way that would allow you to get the idea, if not the details. A vector field $X^\mu(x)$ generates a **flow**: the one-parameter family of diffeomorphisms $\phi_\epsilon$ obtained by following the integral curves of $X$ for a parameter distance $\epsilon$. Put simply: the flow are a bunch of curves paving $M$ like a coordinate chart, that follows the direction indicated by the vector field at every point of $M$. In coordinates, to first order,

$$\phi_\epsilon:\quad x^\mu\;\longmapsto\;\tilde{x}^\mu=x^\mu+\epsilon\,X^\mu(x)$$

Now the trick. Instead of transporting $T$ from $p$ to $\phi_\epsilon(p)$ with a connection, use the **flow itself** to drag it back, and compare the dragged tensor with the original at the *same* point:

$$\boxed{\;\mathcal{L}_X T\big|_p\;=\;\lim_{\epsilon\to0}\frac{\big(\phi_\epsilon^{*}T\big)_p-T_p}{\epsilon}\;=\;\frac{\mathrm{d}}{\mathrm{d}\epsilon}\bigg|_{\epsilon=0}\big(\phi_\epsilon^{*}T\big)_p\;}$$

where $\phi_\epsilon^{*}$ is the **pullback**: it uses the Jacobian of the map $\phi_\epsilon$ to convert indices, which is the only thing available and costs nothing. The Lie derivative therefore measures **how much a tensor field fails to be invariant under being dragged along $X$** — which is why it will turn out to be the natural language for symmetries.

**Components.** Carrying out that limit (proof box below) gives, for a general $(k,l)$ tensor,

$$\boxed{\;
\mathcal{L}_X T^{\mu_1\ldots\mu_k}{}_{\nu_1\ldots\nu_l}
=X^\lambda\partial_\lambda T^{\mu_1\ldots\mu_k}{}_{\nu_1\ldots\nu_l}
-\sum_{i=1}^{k}T^{\ldots\lambda\ldots}{}_{\nu_1\ldots\nu_l}\,\partial_\lambda X^{\mu_i}
+\sum_{j=1}^{l}T^{\mu_1\ldots\mu_k}{}_{\ldots\lambda\ldots}\,\partial_{\nu_j}X^{\lambda}\;}$$

Read it as: *one transport term* ($X^\lambda\partial_\lambda$, the change of $T$ as you move along the flow) plus *one correction per index* accounting for the fact that the flow also rotates and stretches the coordinate frame. Note the signs: upper indices come with a minus, lower indices with a plus. The three cases you will use constantly:

$$
\begin{aligned}
\text{scalar}\qquad & \mathcal{L}_X f = X^\lambda\partial_\lambda f\\[4pt]
\text{vector}\qquad & \mathcal{L}_X Y^\mu = X^\lambda\partial_\lambda Y^\mu-Y^\lambda\partial_\lambda X^\mu = [X,Y]^\mu\\[4pt]
\text{metric}\qquad & \mathcal{L}_X g_{\mu\nu} = X^\lambda\partial_\lambda g_{\mu\nu}+g_{\lambda\nu}\partial_\mu X^\lambda+g_{\mu\lambda}\partial_\nu X^\lambda
\end{aligned}
$$

The middle line is worth pausing on: **the Lie derivative of a vector field is just the Lie bracket**. Geometrically, $[X,Y]$ measures the failure of the flows of $X$ and $Y$ to commute — flow along $X$ then $Y$, versus $Y$ then $X$, and you do not come back to the same point. The little parallelogram does not close.

<details markdown="1">
  <summary><strong>Proof: the component formula from the flow</strong></summary>

Everything follows from expanding the pullback to first order in $\epsilon$, so we just need the Jacobian of $\tilde{x}^\mu=x^\mu+\epsilon X^\mu(x)$ and its inverse:

$$\frac{\partial\tilde{x}^\alpha}{\partial x^\mu}=\delta^\alpha_\mu+\epsilon\,\partial_\mu X^\alpha,
\qquad
\frac{\partial x^\mu}{\partial\tilde{x}^\alpha}=\delta^\mu_\alpha-\epsilon\,\partial_\alpha X^\mu+\mathcal{O}(\epsilon^2)$$

(the second is the inverse of the first, since $(\mathbb{1}+\epsilon A)^{-1}=\mathbb{1}-\epsilon A+\mathcal{O}(\epsilon^2)$). We will also need that evaluating any field at the displaced point costs one Taylor term, $F(\tilde{x})=F(x)+\epsilon X^\lambda\partial_\lambda F(x)+\mathcal{O}(\epsilon^2)$.

**Case 1: a $(0,2)$ tensor.** The pullback carries *lower* indices with the forward Jacobian:

$$
\begin{aligned}
\big(\phi_\epsilon^{*}T\big)_{\mu\nu}(x)
&=\frac{\partial\tilde{x}^\alpha}{\partial x^\mu}\,\frac{\partial\tilde{x}^\beta}{\partial x^\nu}\;T_{\alpha\beta}(\tilde{x})\\[4pt]
&=\big(\delta^\alpha_\mu+\epsilon\,\partial_\mu X^\alpha\big)\big(\delta^\beta_\nu+\epsilon\,\partial_\nu X^\beta\big)\Big(T_{\alpha\beta}(x)+\epsilon\,X^\lambda\partial_\lambda T_{\alpha\beta}\Big)\\[4pt]
&=T_{\mu\nu}+\epsilon\Big(X^\lambda\partial_\lambda T_{\mu\nu}+T_{\lambda\nu}\,\partial_\mu X^\lambda+T_{\mu\lambda}\,\partial_\nu X^\lambda\Big)+\mathcal{O}(\epsilon^2)
\end{aligned}
$$

Subtract $T_{\mu\nu}$, divide by $\epsilon$, let $\epsilon\to0$:

$$\mathcal{L}_XT_{\mu\nu}=X^\lambda\partial_\lambda T_{\mu\nu}+T_{\lambda\nu}\partial_\mu X^\lambda+T_{\mu\lambda}\partial_\nu X^\lambda$$

**Case 2: a vector field.** *Upper* indices are carried by the inverse Jacobian, and this is where the minus sign comes from:

$$
\begin{aligned}
\big(\phi_\epsilon^{*}Y\big)^{\mu}(x)&=\frac{\partial x^\mu}{\partial\tilde{x}^\alpha}\,Y^\alpha(\tilde{x})
=\big(\delta^\mu_\alpha-\epsilon\,\partial_\alpha X^\mu\big)\Big(Y^\alpha+\epsilon\,X^\lambda\partial_\lambda Y^\alpha\Big)\\[4pt]
&=Y^\mu+\epsilon\Big(X^\lambda\partial_\lambda Y^\mu-Y^\lambda\partial_\lambda X^\mu\Big)+\mathcal{O}(\epsilon^2)
\end{aligned}
$$

so $\mathcal{L}_XY^\mu=[X,Y]^\mu$.

**The general case** is now just bookkeeping: each upper index brings one inverse Jacobian (hence $-\,T^{\ldots\lambda\ldots}\partial_\lambda X^{\mu_i}$), each lower index brings one forward Jacobian (hence $+\,T_{\ldots\lambda\ldots}\partial_{\nu_j}X^\lambda$), and the Taylor term $X^\lambda\partial_\lambda T$ appears once regardless. Notice that **no metric and no connection appeared anywhere** in this derivation — only the map $\phi_\epsilon$ and its Jacobian, which exist on any smooth manifold. 

</details>

**Properties worth memorising.**

- $\mathcal{L}_X$ is $\mathbb{R}$-linear, obeys the Leibniz rule, commutes with contractions, and maps $(k,l)$ tensors to $(k,l)$ tensors.
- **It is *not* tensorial in $X$.** Whereas $\nabla_X T$ at a point depends only on the value $X^\mu(p)$ — so that $\nabla_{fX}T=f\nabla_XT$ — the Lie derivative involves $\partial X$, so $\mathcal{L}_{fX}T\neq f\,\mathcal{L}_XT$ in general. You need the whole vector *field*, not just one vector. That is the price of not having a connection.
- $$[\mathcal{L}_X,\mathcal{L}_Y]=\mathcal{L}_{[X,Y]}$$: Lie derivatives furnish a representation of the Lie algebra of vector fields. This is why symmetry generators close into an algebra.
- On differential forms, **Cartan's magic formula** $$\mathcal{L}_X=\mathrm{d}\,\iota_X+\iota_X\,\mathrm{d}$$, with $\iota_X$ the interior product (the "inverse" of the exterior derivative, or concretely the contraction of the first slot with $X$).
- On the volume element, $$\mathcal{L}_X\sqrt{-g}=\sqrt{-g}\,\nabla_\mu X^\mu=\partial_\mu\big(\sqrt{-g}\,X^\mu\big)$$ — the identity that makes $\delta_\xi S=0$ work out for diffeomorphism-invariant actions.

**Relation to the covariant derivative.** For a **torsion-free** connection, every partial derivative in the component formula may be replaced by a covariant one, all the extra $\Gamma$'s cancelling among themselves:

$$\boxed{\;\mathcal{L}_X T^{\mu\ldots}{}_{\nu\ldots}
=X^\lambda\nabla_\lambda T^{\mu\ldots}{}_{\nu\ldots}
-T^{\ldots\lambda\ldots}{}_{\nu\ldots}\nabla_\lambda X^{\mu}
+T^{\mu\ldots}{}_{\ldots\lambda\ldots}\nabla_{\nu}X^{\lambda}\;}\qquad(T^\lambda{}_{\mu\nu}=0)$$

This is a *convenience*, not new content — the left-hand side never knew about $\nabla$ in the first place. But it is the step that turns $$\mathcal{L}_\xi g_{\mu\nu}=0$$ into the Killing equation, so it is worth seeing done.

<details markdown="1">
  <summary><strong>Proof: replacing $\partial$ by $\nabla$, and what torsion does to it</strong></summary>

Take a $(0,2)$ tensor $S_{\mu\nu}$ and a general connection (torsion allowed). Expand the would-be covariant expression:

$$
\begin{aligned}
&X^\lambda\nabla_\lambda S_{\mu\nu}+S_{\lambda\nu}\nabla_\mu X^\lambda+S_{\mu\lambda}\nabla_\nu X^\lambda\\[4pt]
&=X^\lambda\Big(\partial_\lambda S_{\mu\nu}-\Gamma^{a}{}_{\lambda\mu}S_{a\nu}-\Gamma^{a}{}_{\lambda\nu}S_{\mu a}\Big)
+S_{\lambda\nu}\Big(\partial_\mu X^\lambda+\Gamma^{\lambda}{}_{\mu a}X^a\Big)
+S_{\mu\lambda}\Big(\partial_\nu X^\lambda+\Gamma^{\lambda}{}_{\nu a}X^a\Big)
\end{aligned}
$$

The three $\partial$ terms are exactly $$\mathcal{L}_XS_{\mu\nu}$$. Collect what is left over, pairing the $\mu$-terms (relabel $$\lambda\leftrightarrow a$$ in the second):

$$-\Gamma^{a}{}_{\lambda\mu}X^\lambda S_{a\nu}+\Gamma^{a}{}_{\mu\lambda}X^\lambda S_{a\nu}
=\big(\Gamma^{a}{}_{\mu\lambda}-\Gamma^{a}{}_{\lambda\mu}\big)X^\lambda S_{a\nu}
=T^{a}{}_{\mu\lambda}\,X^\lambda S_{a\nu}$$

and identically for the $\nu$-pair. Hence the **exact** relation, valid for any connection,

$$\mathcal{L}_XS_{\mu\nu}=X^\lambda\nabla_\lambda S_{\mu\nu}+S_{\lambda\nu}\nabla_\mu X^\lambda+S_{\mu\lambda}\nabla_\nu X^\lambda
\;-\;T^{\lambda}{}_{\mu\rho}X^\rho S_{\lambda\nu}\;-\;T^{\lambda}{}_{\nu\rho}X^\rho S_{\mu\lambda}$$

When $T^\lambda{}_{\mu\nu}=0$ the last two terms disappear and we recover the boxed replacement rule.

**Two remarks.**

*First*, the fact that the $\Gamma$'s cancel is not luck: it has to happen, because the left-hand side was defined without any connection. Any $\Gamma$-dependence surviving on the right would be a contradiction. What is *not* guaranteed is that the surviving $\Gamma$-dependence organises itself into a tensor — and it does, into the torsion. So if you use the naive $\partial\to\nabla$ rule inside a metric-affine or Einstein-Cartan calculation, you are silently assuming $T=0$.

*Second*, this gives the cleanest possible characterisation of torsion, which we can now state in one line. Comparing the definitions,

$$T(X,Y)=\nabla_XY-\nabla_YX-[X,Y]=\nabla_XY-\nabla_YX-\mathcal{L}_XY$$

**torsion is precisely the mismatch between the two ways of differentiating a vector field along another** — the connection way and the flow way. The Lie bracket in the definition of torsion, which can look like an unmotivated subtraction, is exactly the Lie derivative.

</details>

**Where this shows up in what we have already done.** The Lie derivative is not a side topic; it has been quietly running the whole course.

- **Diffeomorphism invariance.** Under an infinitesimal active diffeomorphism generated by $\xi$, *every* field changes by its Lie derivative: $$\delta_\xi g_{\mu\nu}=\mathcal{L}_\xi g_{\mu\nu}$$, $$\delta_\xi\psi=\mathcal{L}_\xi\psi$$. Diffeomorphism invariance of the action is the statement $$\delta_\xi S=0$$ for all $\xi$, and by Noether's second theorem it is equivalent to the Bianchi identity $$\nabla_\mu G^{\mu\nu}=0$$.
- **Gauge transformations of the graviton.** In the [Fierz-Pauli section](./spin2.md) this tool can be used to show that the Lagrangian has the gauge symmetry $$h_{\mu\nu}\to h_{\mu\nu}+\partial_\mu\xi_\nu+\partial_\nu\xi_\mu$$. We can now name it: since $\eta_{\mu\nu}$ is constant, $$\mathcal{L}_\xi\eta_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu$$, so the graviton's gauge symmetry *is* a linearised diffeomorphism.
- **Galilean invariance in [Newton-Cartan](./newton-cartan.md).** The statement that $\tau_\mu$ and $h^{\mu\nu}$ are the invariant data is the statement that their Lie derivatives along the Galilean boost generator vanish.
- **Conserved currents.** If $$\mathcal{L}_\xi g_{\mu\nu}=0$$ then $$J^\mu=T^{\mu\nu}\xi_\nu$$ is covariantly conserved, $$\nabla_\mu J^\mu=0$$, which is the field-theory version of the geodesic result below. (Check: $$\nabla_\mu(T^{\mu\nu}\xi_\nu)=(\nabla_\mu T^{\mu\nu})\xi_\nu+T^{\mu\nu}\nabla_{(\mu}\xi_{\nu)}$$, and both terms vanish.)

This last point is the bridge to the next subsection: **a symmetry of the geometry is a vector field whose Lie derivative of the metric vanishes.** Such a vector has a name.

### Killing vectors

Once a metric solution $g_{\mu\nu}$ of Einstein equations has been found, it is very relevant to study its symmetries, and associated conserved quantities. 
A **Killing vector** $\xi^\mu$ generates a symmetry of the metric — an *isometry*. Flow along it and the geometry is unchanged:

$$\boxed{\;\mathcal{L}_\xi\, g_{\mu\nu} = 0 \qquad\Longleftrightarrow\qquad \nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu = 0\;}\qquad\textbf{Killing equation}$$

If $\xi$ is Killing and $u^\mu$ is tangent to a geodesic, then $\xi_\mu u^\mu$ is **conserved along the geodesic**:

$$\frac{d}{d\tau}\left(\xi_\mu u^\mu\right) = \underbrace{u^\mu u^\nu\,\nabla_{(\nu}\xi_{\mu)}}_{=\,0\ \text{by Killing}} + \underbrace{\xi_\mu\, u^\nu\nabla_\nu u^\mu}_{=\,0\ \text{by geodesic}} = 0 .$$

This is Noether's theorem in geometric clothing, and it is how essentially every exact orbit calculation in GR is actually done.

| spacetime | Killing vectors | conserved quantity |
|---|---|---|
| Minkowski | $10$ (4 translations, 3 rotations, 3 boosts) | the full Poincaré algebra |
| Schwarzschild | $\partial_t$ (static), $\partial_\varphi$ (axial), $+2$ more | energy $E$, angular momentum $L$ |
| Kerr | $\partial_t$, $\partial_\varphi$ | $E$, $L$ (+ Carter constant, from a Killing **tensor**) |
| **FLRW** | $6$: 3 translations $+$ 3 rotations | momentum; **but no $\partial_t$** so no energy! |

**Do not skip that last row.** FLRW is homogeneous and isotropic but **not** static: $\partial_t$ is not a Killing vector. There is therefore **no conserved energy in an expanding universe** — which is why photons redshift and why "where does the energy of redshifted light go?" is a question with no good answer. It does not go anywhere; energy conservation simply requires a time-translation symmetry that the universe does not have.

A maximally symmetric $n$-dimensional space has $n(n+1)/2$ Killing vectors — ten in 4D, achieved by Minkowski, de Sitter and anti-de Sitter, and by nothing else.

This is useful in GR and modified gravity for:

- **Defining your ansatz.** "Static", "stationary", "spherically symmetric", "axisymmetric" are all statements about Killing vectors, and they are what make field equations solvable at all.
- **No-hair theorems** are proved using the horizon-generating Killing vector.
- **Black hole thermodynamics**: the surface gravity $\kappa$ — hence the Hawking temperature $T=\kappa/2\pi$ — is defined via the Killing vector that becomes null on the horizon.
- **Masses in asymptotically flat spacetimes** (Komar, ADM) require an asymptotic time-translation Killing vector — which is precisely why energy is well defined for an isolated star and not for the universe.
- **Conformal Killing vectors** ($$\mathcal{L}_\xi g_{\mu\nu} = 2\sigma g_{\mu\nu}$$) generate symmetries that preserve angles but not lengths, and are the natural language for the conformal transformations we used throughout the [Brans-Dicke class](./Brans-Dicke.md).


### Further reading

- Misner, Thorne & Wheeler, *Gravitation* (1973) — §21 for ADM, §14 for forms. Long, but unmatched on intuition.
- Wald, *General Relativity* (1984) — App. E for tetrads, Ch. 10 for the initial-value formulation. Terse and reliable.
- Carroll, *Spacetime and Geometry* (2004) — App. J on tetrads and forms is the gentlest introduction available.
- Baez & Muniain, *Gauge Fields, Knots and Gravity* (1994) — the friendliest route into forms, connections and the Palatini–Cartan action.
- [Gourgoulhon - *3+1 Formalism and Bases of Numerical Relativity* (2007)](https://arxiv.org/abs/gr-qc/0703035) — the definitive pedagogical treatment of ADM, and free.
- Doran & Lasenby, *Geometric Algebra for Physicists* (CUP, 2003); [Lasenby, Doran & Gull (1998)](https://doi.org/10.1098/rsta.1998.0178) for GTG itself.
- Nakahara, *Geometry, Topology and Physics* (2003) — the mathematical background for all of the above.