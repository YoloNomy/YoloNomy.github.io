---
layout: default
title: Massive gravity
parent: cosmo
---

As the bosons of the weak force are massive, it is legitimate to investigate whether the mediator of gravity could be massive too. Gravity is a long range force, so it cannot be *too* massive — but "not too massive" is not the same as "exactly zero", and the difference turns out to be one of the richest stories in modified gravity.

This class is organised around a single question: **what goes wrong when you give the graviton a mass, and can it be fixed?** The answer took forty years, produced three famous obstructions, and generated along the way most of the technology (Galileons, Vainshtein screening) that we used in the previous classes. This class is inspired by the great lectures on massive gravity by [Rachel Rosen](https://www.youtube.com/watch?v=1THLppx96T8), and you should have a look at them for more details!

## Warm-up: a mass term for a spin-0 field

Before touching gravity, let us recall what we saw already in the [field class](./GR_fieldtheory.md) and consider what a mass is for a scalar graviton (Nordstrom theory). Expand a potential around its minimum ($\partial V /\partial \phi=0$), then $V(\phi) \simeq V_0 + \tfrac12 V''(\phi_0)(\phi-\phi_0)^2$. The mass is defined by

$$\boxed{\;m^2 = \frac{\partial^2 V}{\partial\phi^2}\Big|_{\phi_0}\;}$$

— note $m^2$, not $m$. So the mass squared is the curvature of the potential function. A negative $V''$ means a *tachyon*: it does not necessarily mean "faster than light travel" but instead that the configuration is unstable. This is for example case of the Higgs mechanism before it falls of its Mexican hat potential!  A **pure mass** term in the Lagrangian would be a potential of the form $$V(\phi) = m^2 \phi^2/2$$. Now consider adding such a mass term to the Nordstrom theory, a massive scalar coupled to the trace $T \equiv T^\mu{}_\mu$ of the matter stress tensor is

$$\mathcal{L} = -\tfrac12\,\partial_\mu\phi\,\partial^\mu\phi \;-\; \tfrac12 m^2\phi^2 \;+\; g\,\phi\,\mathcal{T} .$$

The corresponding field equation is $(\Box - m^2)\phi = -gT$. For a static point source $\mathcal{T}=-M\delta^{(3)}(\vec r)$ this is the *screened* Poisson equation $(\nabla^2 - m^2)\phi = gM\delta^{(3)}$, whose solution is

$$\phi(r) = -\frac{g M}{4\pi}\frac{e^{-mr}}{r} .$$

If another mass is coupled to the field, we obtain the **Yukawa potential**:

$$\boxed{\;V(r) = -\frac{g^{2}}{4\pi}\,\frac{M_1M_2}{r}\;e^{-mr}\;}$$

Thus, **a mass gives the force a finite range** $\lambda = 1/m$ (restoring units, $\lambda = \hbar/mc$). Below $r\ll\lambda$ you cannot tell the difference from a massless force; beyond $r\gg\lambda$ the force is exponentially dead. The pion mass gives the nuclear force its femtometre range; the $W$ and $Z$ masses make the weak force weak.

**So what would a graviton mass mean?** Gravity would switch off beyond $\lambda_g = \hbar/m_gc$. If we want the modification to matter for cosmic acceleration, we need $\lambda_g\sim$ the Hubble radius, i.e.

$$m_g \sim \hbar H_0/c^2 \sim 10^{-33}\ \mathrm{eV}.$$

That's indeed extremely small. In fact, it is the smallest mass anyone has ever seriously proposed for anything!

## Counting degrees of freedom

Now, we also saw in the [field class](./GR_fieldtheory.md), that massless fields had 2 physical degrees of freedom no matter their spin, while a massive field has $2s+1$ degrees of freedom.  So switching on a spin-2 graviton mass must increase the degrees of freedom from 2 to 5 i.e. produce **three new degrees of freedom**: two helicity-$\pm1$ modes and one helicity-$0$ mode. Let us see where they come from.

The graviton field $h_{\mu\nu}$ is a symmetric $4\times4$ matrix: **10** components. We saw already that in linearised GR/Fierz Pauli there is a gauge symmetry, inherited from diffeomorphisms:

$$h_{\mu\nu} \;\to\; h_{\mu\nu} + \partial_\mu\xi_\nu + \partial_\nu\xi_\mu ,$$

with $\xi_\mu$ four arbitrary functions. Gauge symmetry removes components twice over — four by the gauge choice, four more by the associated constraints — leaving $10-4-4 = 2$.

A mass term $\propto h_{\mu\nu}h^{\mu\nu}$ is *not invariant* under that transformation. **A graviton mass breaks the gauge symmetry**, exactly as a photon mass breaks $U(1)$. Without gauge symmetry, nothing removes those components, and we are left with (generically) all 10 — or, with the right tuning, 5. Let's see how this comes about concretely.

## Massive Fierz–Pauli

The original action proposed by [Fierz and Pauli (1939)](https://doi.org/10.1098/rspa.1939.0140) was in fact already a massive one. Indeed, since the linear theory is a field theory like any other, we can simply ask what happens if we add a mass term. We can think of two possible mass terms to add to the Lagrangian (mass=quadratic term in the field):

$$\mathcal{L}_{\rm mass} = \frac{1}{2}\left(m_1^2 h_{\mu\nu}h^{\mu\nu} + m_2^2\,h^2\right),\qquad h \equiv h^\mu{}_\mu ,$$

It is quite straightforward to show that the equation of motions in vacuum (wave propagation) with such additional terms will become:

$$G^{(1)}_{\mu\nu} +m_1^2 h_{\mu\nu}+ m_2^2\,h^2 = 0  $$

Which, by Bianchi identity becomes the constraints:

$$m_1^2 \partial^\mu h_{\mu\nu} =- m_2^2\partial^\mu \,h^2$$

these gives four constraints (1 per $\mu$) removing thus four degrees of freedom and leaving $10-4=6$$ degrees of freedom.  Now by playing with the equations of motions, it can be shown that this sixth's degree of freedom is, in general, a **ghost** and as we discussed already in a [previous class](./Brans-Dicke.md): **a theory with a ghost is not a theory with a problem; it is not a theory.**. As shown by Fierz and Pauli in their original paper, the only choice removing this pathology is the choice

$$\boxed{m_1^2 = -m_2^2 = m^2}$$

such that the mass term should be:

$$\boxed{\mathcal{L}_{\rm mass} = \frac{1}{2}m^2\left(h_{\mu\nu}h^{\mu\nu} -\,h^2\right)}$$

With this choice, taking the trace of the equation of motion and combining with the Bianchi identity again, one gets the additional fifth constraint $m^2 h=0$, leaving 5 free degrees of freedom as desired for a massive spin-2 graviton. All constraints considered, the final equation of motion coupled to matter is:

$$\boxed{\;(\Box-m^2)\,h_{\mu\nu} \;=\; -\frac{2}{M_{\rm pl}^{2}}\left[T_{\mu\nu}-\frac{1}{3}\left(\eta_{\mu\nu}-\frac{\partial_\mu\partial_\nu}{m^{2}}\right)\mathcal{T}\right]\;}$$

with $\mathcal{T}\equiv\eta^{\mu\nu}T_{\mu\nu}$ and $2/M_{\rm pl}^2 = 16\pi G$. Compare with linearised GR in harmonic gauge that we obtained in a [previous class](./validation_GR.md): $\Box h_{\mu\nu} = -\frac{2}{M_{\rm pl}^2}\left[T_{\mu\nu}-\frac12\eta_{\mu\nu}\mathcal{T}\right]$: an additional term inversely proportional to $m^2$ and containing two partial derivatives appears and the factor of $\tfrac12$ has become a $\tfrac13$. While the additional term disappears when $m\to0$, the factor does not change ... This is strange and this is the source of the vDVZ discontinuity discussed in the next section.

<details markdown="1">
  <summary><strong>Proofs and discussion</strong></summary>

We showed already multiple times that the linearized Einstein tensor is:

$$G^{(1)}_{\mu\nu}=R^{(1)}_{\mu\nu}-\tfrac12\eta_{\mu\nu}R^{(1)}
=-\tfrac12\Big(\Box h_{\mu\nu}-\partial_\alpha\partial_\mu h^{\alpha}{}_{\nu}-\partial_\alpha\partial_\nu h^{\alpha}{}_{\mu}+\partial_\mu\partial_\nu h+\eta_{\mu\nu}\partial_\alpha\partial_\beta h^{\alpha\beta}-\eta_{\mu\nu}\Box h\Big).$$

On top of which is added the Bianchi identity:

$$\partial^\mu G^{(1)}_{\mu\nu}\equiv 0 .$$

Now vary the Fierz-Pauli action with the two masses free:

$$\frac{\delta}{\delta h_{\mu\nu}}\left(-\tfrac12 m_1^2 h_{\alpha\beta}h^{\alpha\beta}\right)=-m_1^2 h^{\mu\nu},
\qquad
\frac{\delta}{\delta h_{\mu\nu}}\left(-\tfrac12 m_2^2 h^2\right)=-m_2^2\,\eta^{\mu\nu}h,$$

(the second because $$h=\eta^{\mu\nu}h_{\mu\nu}$$). With $$\delta S^{(2)}_{\rm EH}/\delta h_{\mu\nu}=-2G^{(1)\mu\nu}$$:

$$-2G^{(1)\mu\nu}-m_1^2h^{\mu\nu}-m_2^2\eta^{\mu\nu}h=0
\qquad\Longleftrightarrow\qquad
G^{(1)}_{\mu\nu}+\tfrac12\left(m_1^2h_{\mu\nu}+m_2^2\eta_{\mu\nu}h\right)=0 .$$

Apply $\partial^\mu$ and use Bianchi identity (and $\partial^\mu(\eta_{\mu\nu}h)=\partial_\nu h$):

$$m_1^2\,\partial^\mu h_{\mu\nu}+m_2^2\,\partial_\nu h=0 .$$

These are four constraints, leaving $10-4=6$ degrees of freedom.

Now, introduce the single dimensionless parameter measuring the detuning,

$$a \equiv -\frac{m_2^2}{m_1^2}$$

The constraints from Bianchi then reads $$\partial^\mu h_{\mu\nu}=a\,\partial_\nu h$$, hence $$\partial_\mu\partial_\nu h^{\mu\nu}=a\,\Box h$$ and

$$R^{(1)}=\partial_\mu\partial_\nu h^{\mu\nu}-\Box h=(a-1)\,\Box h .$$

Now take the trace of the field equation. Since $$\eta^{\mu\nu}G^{(1)}_{\mu\nu}=R^{(1)}-\tfrac42R^{(1)}=-R^{(1)}$$ and $$\tfrac12(m_1^2h+4m_2^2h)=\tfrac{m_1^2}{2}(1-4a)h$$:

$$-(a-1)\,\Box h+\frac{m_1^2}{2}(1-4a)\,h=0 .$$

Everything hangs on the coefficient $(a-1)$:

- **$a\neq1$:** $\;\Box h=\dfrac{m_1^2(1-4a)}{2(a-1)}\,h\;$ — a **wave equation**. The trace is a genuine sixth propagating mode, with $m^2_{\rm 6th}=\dfrac{m_1^2(4a-1)}{2(a-1)}$.
- **$a=1$:** the derivative term disappears identically and we are left with the purely **algebraic** $-\tfrac32 m_1^2\,h=0\Rightarrow h=0$. A constraint, not a wave. $10-4-1=5$. 

The Fierz–Pauli tuning is exactly the condition that kills the $\Box h$ term. Now, why is this sixth mode a *ghost*? Two complementary arguments. The first says *why the tuning is special*, the second says *why the alternative is fatal*.

**(i) Structural: $h_{00}$ must remain a Lagrange multiplier.**
Expand the mass term in $3+1$ components. With $h^{00}=h_{00}$, $h^{0i}=-h_{0i}$, $h^{ij}=h_{ij}$ and $h=-h_{00}+h_{kk}$:

$$h_{\mu\nu}h^{\mu\nu}=h_{00}^2-2h_{0i}h_{0i}+h_{ij}h_{ij},
\qquad h^2=h_{00}^2-2h_{00}h_{kk}+h_{kk}^2,$$

$$\Longrightarrow\quad h_{\mu\nu}h^{\mu\nu}-a\,h^2 = \underbrace{(1-a)\,h_{00}^{2}}_{\text{the dangerous term}}+2a\,h_{00}h_{kk}+\big(\text{terms without }h_{00}\big).$$

The linearised Einstein–Hilbert Lagrangian contains **no $\dot h_{00}$ and no $h_{00}^2$**: $h_{00}$ appears only linearly, i.e. as a Lagrange multiplier enforcing a constraint (the linearised Hamiltonian constraint). Then:

- $a=1$: the coefficient $(1-a)$ vanishes, $h_{00}$ **stays linear** $\Rightarrow$ still a multiplier $\Rightarrow$ one extra constraint $\Rightarrow$ 5 DOF.
- $a\neq1$: $h_{00}^2$ appears, so $h_{00}$ becomes an *auxiliary* field which you solve for algebraically and substitute back. The constraint is **destroyed** $\Rightarrow$ 6 DOF.

So the tuning is not an aesthetic choice: it is precisely the condition preserving the multiplier structure of $h_{00}$.

**(ii) The sign: the conformal mode of the metric carries negative kinetic energy.**
Insert a pure-trace configuration $h_{\mu\nu}=\tfrac14\eta_{\mu\nu}h$ into the four terms of the linearised EH Lagrangian $\left(-\tfrac12\partial_\lambda h_{\mu\nu}\partial^\lambda h^{\mu\nu}+\partial_\mu h_{\nu\lambda}\partial^\nu h^{\mu\lambda}-\partial_\mu h^{\mu\nu}\partial_\nu h+\tfrac12\partial_\lambda h\partial^\lambda h\right)$. Term by term, in units of $\partial_\lambda h\,\partial^\lambda h$:

$$-\frac{1}{8}\;+\;\frac{1}{16}\;-\;\frac{1}{4}\;+\;\frac{1}{2}\;=\;+\frac{3}{16}
\qquad\Longrightarrow\qquad
\mathcal{L}^{(2)}_{\rm EH}\Big|_{\rm trace}=+\frac{3}{16}\,\partial_\lambda h\,\partial^\lambda h=-\frac{3}{16}\dot h^2+\dots$$

A healthy scalar has $\mathcal{L}=-\tfrac12\partial_\mu\varphi\partial^\mu\varphi=+\tfrac12\dot\varphi^2-\dots$. **The sign is wrong**: the conformal (trace) direction of the metric always has negative kinetic energy. This is the old *conformal factor problem*. In massless GR it is harmless, because $h$ is pure gauge and never appears in the physical spectrum. In the massive theory the gauge freedom is gone, and the only thing standing between us and a propagating negative-energy state is the FP tuning.

A ghost is fatal, not merely ugly: the Hamiltonian is unbounded below, so the vacuum decays into (ghost + ordinary particle) pairs at a rate that diverges with the cutoff. Nothing is stable. *(Caveat, to be honest: argument (ii) as written ignores the mixing between the trace and the traceless part; the airtight version diagonalises the scalar sector, e.g. via the Stückelberg decomposition. The conclusion is unchanged.)*

At linear order the FP tuning removes the ghost completely. At **nonlinear** order it comes back — that is the Boulware–Deser ghost ([Boulware & Deser 1972](https://doi.org/10.1103/PhysRevD.6.3368)), and removing it too required tuning the whole nonlinear potential ([de Rham, Gabadadze & Tolley 2011](https://arxiv.org/abs/1011.1232)).

Set $$m_1^2=-m_2^2=m^2$$ and add matter (normalisation such that $m\to0$ gives linearised Einstein, $$G^{(1)}_{\mu\nu}=T_{\mu\nu}/M_{\rm pl}^2$$):

$$G^{(1)}_{\mu\nu}+\frac{m^2}{2}\left(h_{\mu\nu}-\eta_{\mu\nu}h\right)=\frac{1}{M_{\rm pl}^{2}}T_{\mu\nu}.$$

With the two constraints:

**(a) Divergence.** $$\partial^\mu G^{(1)}_{\mu\nu}\equiv0$$ and $$\partial^\mu T_{\mu\nu}=0$$, so

$$\partial^\mu h_{\mu\nu}=\partial_\nu h .$$

**(b) Trace.** By Step 3 with $a=1$, $R^{(1)}=0$, so $\eta^{\mu\nu}G^{(1)}_{\mu\nu}=0$ and the trace of $(\star)$ is purely algebraic:

$$\frac{m^2}{2}(h-4h)=\frac{T}{M_{\rm pl}^{2}}
\qquad\Longrightarrow\qquad
h=-\frac{2\,T}{3m^{2}M_{\rm pl}^{2}} .$$

Two things worth noticing: the trace is *slaved* to the source, with no wave equation of its own; and it carries a $1/m^2$, the first sign that the massless limit will not be smooth.

Now simplify $G^{(1)}$ using the divergence constraint. With $$\partial_\alpha h^{\alpha}{}_{\nu}=\partial_\nu h$$ we get $$\partial_\alpha\partial_\mu h^{\alpha}{}_{\nu}=\partial_\mu\partial_\nu h$$ and $$\partial_\alpha\partial_\beta h^{\alpha\beta}=\Box h$$, so four of the six terms cancel pairwise:

$$G^{(1)}_{\mu\nu}=-\tfrac12\Big(\Box h_{\mu\nu}-\underbrace{\partial_\mu\partial_\nu h-\partial_\mu\partial_\nu h+\partial_\mu\partial_\nu h}_{=\;\partial_\mu\partial_\nu h}+\underbrace{\eta_{\mu\nu}\Box h-\eta_{\mu\nu}\Box h}_{=\;0}\Big)
=-\tfrac12\left(\Box h_{\mu\nu}-\partial_\mu\partial_\nu h\right).$$

Now put it together. Substituting into the Einstein equation and multiplying by $-2$:

$$\Box h_{\mu\nu}-\partial_\mu\partial_\nu h-m^{2}h_{\mu\nu}+m^{2}\eta_{\mu\nu}h=-\frac{2}{M_{\rm pl}^{2}}T_{\mu\nu},$$

then eliminate $h$ with the trace constraint, using $\partial_\mu\partial_\nu h=-\frac{2}{3m^2M_{\rm pl}^2}\partial_\mu\partial_\nu T$ and $m^2\eta_{\mu\nu}h=-\frac{2}{3M_{\rm pl}^2}\eta_{\mu\nu}T$:

$$\boxed{\;(\Box-m^{2})h_{\mu\nu}=-\frac{2}{M_{\rm pl}^{2}}\left[T_{\mu\nu}-\frac13\left(\eta_{\mu\nu}-\frac{\partial_\mu\partial_\nu}{m^{2}}\right)T\right]\;}$$

</details>

## vDVZ discontinuity

Now, there is a problem with the new massive term proposed! Naively, taking $m\to0$ in Fierz–Pauli should give back GR. This is an important condition to explain why we could observe gravity behaving as GR while the graviton is indeed massive, with a very weak mass. As first discussed in  [van Dam & Veltman (1970)](https://doi.org/10.1016/0550-3213(70)90416-5) and [Zakharov (1970)](http://jetpletters.ru/ps/1716/article_26086.shtml), **it does not**. 

Computing the coupled equation of motion for the massive theory with the constraints and considering a point source as usual, we get

$$h_{00} = \frac{-4}{3} \frac{M}{8\pi M_{\rm pl}r}e^{-mr} = -1 \qquad h_{ij} = \frac{3}{8} \frac{M}{8\pi M_{\rm pl}r}e^{-mr}$$

From which we read the post Newtonian parameters $$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$$ (see [our dedicated class](./validation_GR.md)):

$$g_{00} = -1 + \frac{8}{3}\frac{GM}{r}e^{-mr} \qquad g_{ij} = \left(1 + \frac{4}{3}\frac{GM}{r}e^{-mr}\right)\delta_{ij}$$

From which one can read directly that $$G^{\rm eff}=  4 G/3$$. Hence gravity is stronger than it would be with a naïve identification of $G$ as the one of GR's Newtonian limit. However we **absolutely don't care** since $G$ is a constant we introduced here in the Lagrangian that no one would ever measure. A constant change in $G$ have no impact as the force of gravity will be dictated $G^{\rm eff}$ and this is the quantity that would be measured by Cavendish like experiment or solar system tests. In other word: this extra $4/3$ factor can just be reabsorbed in the definition of $G$ without consequence.  What matters however is the difference between the $00$ and the $ij$ component: we find $$\gamma=1/2$$ and the deviation of light would be:

$$\delta \theta = \left(\frac{1+\gamma}{2}\right)\frac{4G_{\rm eff}M}{bc^2} = \frac{3G_{\rm eff}M}{bc^2} $$

with a $25\%$ deviation from GR (no matter the mass of the graviton).
Even when $m\to0$, there is thus a deviation from GR that one can't get rid of! This makes sense: we have three additional degrees of freedom in this theory. Even in the limit $m\to0$, these degrees of freedom become massless but they do not disappear !

<details markdown="1">
  <summary><strong>Proof</strong></summary>

We saw that the equation of motion is:

$$(\Box-m^2)h_{\mu\nu} = -\frac{2}{M_{\rm pl}^{2}}\left[T_{\mu\nu}-\frac13\left(\eta_{\mu\nu}-\frac{\partial_\mu\partial_\nu}{m^{2}}\right)\mathcal{T}\right],
\qquad \frac{2}{M_{\rm pl}^2}=16\pi G .$$

Consider now a point source $$T_{\mu\nu} = M\,\delta^0_\mu\delta^0_\nu\,\delta^{(3)}(\vec x - \vec x_0), \qquad T \equiv \eta^{\mu\nu}T_{\mu\nu} = -M\,\delta^{(3)}(\vec x-\vec x_0),$$. In the static limit, everything is time-independent, so $\Box\to\nabla^2$. Using the Green function of the Klein-Gordon term as we did multiple times:

$$\left(\nabla^2-m^2\right)h_{00} = -\frac{2}{M_{\rm pl}^2}\Big[\underbrace{M}_{T_{00}}-\tfrac13\underbrace{(-1)}_{\eta_{00}}\underbrace{(-M)}_{T}\Big]\delta^{(3)}
= -\frac{2}{M_{\rm pl}^{2}}\cdot\frac{2M}{3}\,\delta^{(3)}$$

$$\Longrightarrow\quad h_{00} = \frac{4M}{3M_{\rm pl}^{2}}\cdot\frac{e^{-mr}}{4\pi r} = \frac{M}{3\pi M_{\rm pl}^{2}r}e^{-mr} = \frac83\frac{GM}{r}e^{-mr}.$$

Note that if you repeat this with $\tfrac12$ instead of $\tfrac13$ and $m=0$: the bracket becomes $M-\tfrac12 M=\tfrac{M}{2}$ and you recover $h_{00}=2GM/r$ as we did already in GR. The whole discontinuity is the ratio $\tfrac23/\tfrac12 = \tfrac43$.
And for the spatial components:

$$\left(\nabla^2-m^2\right)h_{ij} = -\frac{2}{M_{\rm pl}^2}\left[0-\tfrac13\left(\delta_{ij}-\frac{\partial_i\partial_j}{m^2}\right)(-M)\right]\delta^{(3)}
= -\frac{2M}{3M_{\rm pl}^{2}}\left(\delta_{ij}-\frac{\partial_i\partial_j}{m^{2}}\right)\delta^{(3)}$$

$$\Longrightarrow\quad h_{ij} = \frac{M}{6\pi M_{\rm pl}^{2}}\left(\delta_{ij}-\frac{\partial_i\partial_j}{m^{2}}\right)\frac{e^{-mr}}{r}.$$

This second term in the sum is a pure gradient and is quite annoying. We will get rid of it by choosing the (static, purely spatial) coordinate shift $x^\mu\to x^\mu+\xi^\mu$ with

$$\xi_0 = 0,\qquad \xi_j = -\frac{M}{12\pi M_{\rm pl}^{2}m^{2}}\,\partial_j\frac{e^{-mr}}{r},$$

we have, as always for diffeomorphisms at linear order: $\delta h_{ij}=\partial_i\xi_j+\partial_j\xi_i$, which cancels it exactly, while $\delta h_{00}=2\partial_0\xi_0=0$ and $\delta h_{0i}=\partial_0\xi_i+\partial_i\xi_0=0$ leave the other components untouched. Two remarks:

- Massive gravity has **no** linearised diffeomorphism invariance, so this is *not* a gauge transformation of the field $h_{\mu\nu}$. It is a genuine change of coordinates in which we describe the metric $g=\eta+h$. Since the observables we extract (deflection angle, time delay, orbits) are coordinate-invariant, we may compute them in whichever coordinates we like.
- This step is not cosmetic: the term carries a $1/m^2$ and *diverges* as $m\to0$. It must be removed before the massless limit is even discussable. What survives the removal is the genuine, finite discontinuity.

Once this term is cancelled, we are now left with:

$$h_{00}=\frac83\frac{GM}{r}e^{-mr},\qquad h_{ij}=\frac43\frac{GM}{r}e^{-mr}\delta_{ij}.$$

Now interpreting $h$ as a small perturbation of a metric tensor in GR, we get:

$$g_{00}=-1+h_{00}\equiv-(1-2U)\;\Longrightarrow\; U=\tfrac12 h_{00}=\tfrac43\tfrac{GM}{r}e^{-mr},$$

$$g_{ij}=(1+h_{ij})\equiv(1+2\gamma U)\delta_{ij}\;\Longrightarrow\; 2\gamma U = \tfrac43\tfrac{GM}{r}e^{-mr}=U\;\Longrightarrow\;\gamma=\tfrac12 .$$

</details>

## Non linear massive gravity and Vainshtein mechanism

The way out of this vDVZ discontinuity is the introduction of the Vainshtein screening which appears naturally in modified gravity. We discussed this mechanism already in the [screening class](./Screening.md). Here is how it appears naturally in massive gravity. [Vainshtein (1972)](https://doi.org/10.1016/0370-2693(72)90147-5)'s insight was to ask a question nobody had asked: **is linear perturbation theory actually valid near the Sun?**

Indeed, all of the above is within the linear theory. Now we know that in order to get the complete theory, we must account for all the coupling of $h$ with itself (bootstrap). We know that this gives GR in the massless case, so let's consider the following action:

$$S = \frac{1}{16\pi G}\int \text{d}^4x \left(\sqrt{-\vert g \vert} R - \frac{1}{4}m^2\eta^{\mu\alpha}\eta^{\nu\beta}(h_{\mu\nu}h_{\alpha\beta}- h_{\mu\alpha}h_{\nu \beta}) \right) $$

This is a sort of "semi-non-linear" theory. Indices of the mass terms are raised and lowered with the flat metric. It is actually impossible to build a non linear mass term action without the introduction of some additional rigid structure, as all the scalars that can be built from $g$ alone are constant numbers (its trace $4$ or it's determinant $-1$).  No cosmological constant is added, as our goal is ultimately to explain it with the massive gravity terms.


We now look for perturbative solutions for the metric around a point source. 
A perturbative solution is written as (leading term) $\times\,\big(1 - c_1\,\epsilon(r) + c_2\,\epsilon(r)^2 - \dots\big)$, where $\epsilon(r)$ is dimensionless. Nonlinearities become important where the series stops converging usefully, i.e. where $$\epsilon(r)\sim 1 .$$ Finding the "nonlinear radius" is nothing more than solving $\epsilon(r)=1$. In these regions the expansion expression for the metric stop being valid.

In General relativity, the expansion parameter is $\epsilon = r_S/r$. Around a static point mass, the exact Schwarzschild solution in **isotropic coordinates** expands as

$$h_{00} = -\frac{2GM}{r}\left( 1 - \frac{GM}{r} + \dots\right),
\qquad
h_{rr} = -\frac{2GM}{r}\left( 1 + \frac{3GM}{4r} + \dots\right).$$

The expansion parameter is manifestly $\epsilon = GM/r \simeq r_S/r$, so

$$\epsilon = 1 \iff r \sim 2GM = r_S \simeq 3\ \mathrm{km}\ \ (\text{Sun}).$$

The same answer follows from power counting, which is the form we will need in a moment. In GR the graviton self-couplings are suppressed by the Planck mass, $$\mathcal{L}_{\rm int}\sim h(\partial h)^2/M_{\rm Pl}$$, so the field equation reads $$\;\Box h + \frac{1}{M_{\rm Pl}}\partial^2(h^2)\sim T/M_{\rm Pl}$$. With the linear solution $$h_{\rm lin}\sim M/(M_{\rm Pl}r)$$,

$$\epsilon \equiv \frac{\text{nonlinear}}{\text{linear}} = \frac{h_{\rm lin}}{M_{\rm Pl}} = \frac{M}{M_{\rm Pl}^2\,r} \simeq \frac{r_S}{r}. \qquad\checkmark$$

Now in massive gravity: the helicity-0 mode changes $\epsilon$ The dangerous mode is the helicity-0 scalar $\pi$ introduced by the Stückelberg substitution $h_{\mu\nu}\to h_{\mu\nu}+\partial_\mu A_\nu+\partial_\nu A_\mu + \frac{2}{m^2}\partial_\mu\partial_\nu\pi$. That factor $1/m^2$ means every nonlinear term is suppressed by a scale **far below** $M_{\rm Pl}$:

| theory | leading self-interaction | suppression scale |
|---|---|---|
| Fierz–Pauli (generic) | $(\partial^2\pi)^3/\Lambda_5^5$ | $\Lambda_5=(M_{\rm Pl}m^4)^{1/5}$ |
| dRGT | cubic Galileon $(\partial\pi)^2\Box\pi/\Lambda_3^3$ | $\Lambda_3=(M_{\rm Pl}m^2)^{1/3}$ |

Repeat the power count of (a) with $\pi_{\rm lin}\sim M/(M_{\rm Pl}r)$, hence $\partial^2\pi_{\rm lin}\sim M/(M_{\rm Pl}r^3)$, and every $\partial\to 1/r$:

$$\underbrace{\epsilon_{\rm FP} = \frac{1}{\Lambda_5^5 r^2}\,\frac{M}{M_{\rm Pl}r^3} = \frac{M}{M_{\rm Pl}^2\,m^4 r^5} \simeq \frac{r_S}{m^4 r^5}}_{\text{matches the bracket below}},
\qquad
\epsilon_{\rm dRGT} = \frac{1}{\Lambda_3^3}\,\frac{M}{M_{\rm Pl}r^3} = \frac{M}{M_{\rm Pl}^2 m^2 r^3} \simeq \frac{r_S}{m^2 r^3}.$$

Recomputing the field of a point source in this regime confirms it (see [Hinterbichler (2011)](https://arxiv.org/pdf/1105.3735), §6):

$$h_{00} = -\frac{4}{3}\frac{2GM}{r}\left( 1 - \frac{1}{6}\,\frac{GM}{m^4r^5} + \dots\right),
\qquad
h_{rr} = -\frac{4}{3}\frac{2GM}{r}\frac{1}{m^2r^2}\left( 1 - 14\,\frac{GM}{m^4r^5} + \dots\right).$$

Both components carry the **same** $\epsilon_{\rm FP}=GM/(m^4r^5)$, so both fail at the same radius. Applying the Rule:

$$\boxed{\;r_V = \left(\frac{r_S}{m^{4}}\right)^{1/5}\ \text{(Fierz–Pauli)},\qquad
r_V = \left(\frac{r_S}{m^{2}}\right)^{1/3}\ \text{(dRGT)},\qquad r_S = 2GM.\;}$$

Equivalently, in a form that makes the pattern transparent,

$$r_V = \frac{1}{\Lambda_n}\left(\frac{M}{M_{\rm Pl}}\right)^{1/n},
\qquad n = 1\ (\text{GR},\ \Lambda_1 = M_{\rm Pl}),\quad n = 5\ (\Lambda_5),\quad n = 3\ (\Lambda_3).$$

**GR is simply the $n=1$ member of the family, and $r_S$ is its Vainshtein radius.** Lowering the suppression scale from $M_{\rm Pl}$ to $\Lambda_5$ is what inflates 3 km into 100 kpc.

Now, **do not over-read $h_{rr}$.** Its leading term, the factor $1/(m^2r^2)$, is **pure gauge**. It descends from the $p_ip_j/m^2$ piece of the linear solution ([Hinterbichler](https://arxiv.org/pdf/1105.3735), eq. 3.11), which in position space is $\propto\partial_i\partial_j(1/r)$ and is removed by the coordinate change $x^i\to x^i+\partial^i\chi$ — Hinterbichler discards it explicitly at his eq. (3.25). It integrates to a total derivative along a light ray and so contributes **nothing** to light bending. The physical statement is the PPN one: $\gamma = 1/2$ instead of $1$. Comparing this $h_{rr}$ against GR's $h_{rr}=2GM/r$ is comparing a coordinate artefact with an observable.

### The numbers, and why the limits do not commute

With $m\sim H_0$, as cosmology requires ($m^{-1}=c/H_0\simeq1.4\times10^{26}$ m), for the Sun ($r_S\simeq2.95$ km):

| | $r_V$ | |
|---|---|---|
| GR ($n=1$) | $3$ km | $=r_S$ |
| Fierz–Pauli ($\Lambda_5$) | $4\times10^{21}$ m | $\simeq 130$ kpc |
| dRGT ($\Lambda_3$) | $4\times10^{18}$ m | $\simeq 120$ pc |

The **hundred-parsec** scale — exactly the number we computed in the screening class. The solar system sits at $r/r_V\sim10^{-8}$ (Earth's orbit) to $\sim10^{-6}$ (heliopause). Inside $r_V$ the scalar is screened, and the fifth force is suppressed relative to Newtonian gravity by

$$\frac{F_\pi}{F_N}\sim\left(\frac{r}{r_V}\right)^{n/2}
\;\Longrightarrow\;
10^{-12}\!-\!10^{-9}\ (\text{dRGT},\ n=3),
\qquad 10^{-20}\!-\!10^{-15}\ (\text{FP},\ n=5).$$

This also explains the logical structure of the rescue. The vDVZ result is obtained by taking $m\to0$ in a formula valid only for $r_V\ll r\ll m^{-1}$. But $r_V\propto m^{-4/5}\to\infty$ as $m\to 0$: **the window of validity closes faster than the limit can be taken.** The two operations do not commute,

$$\lim_{m\to 0}\big[\text{linearised massive gravity}\big] \;\neq\; \big[\text{linearised massless gravity}\big],$$

and inside $r_V$ one finds $\gamma = 1 + \mathcal{O}\big[(r/r_V)^{n/2}\big]\to 1$: GR is recovered smoothly.

**So the 25% is real but unobservable:** it applies only at distances far beyond any body whose light bending we can measure. The vDVZ no-go was an artefact of trusting a linear approximation outside its regime.

This is worth pausing on as a lesson in method. A theory was declared dead for two years on the strength of a calculation that was internally correct but performed in the wrong regime. **The screening idea that now underpins all of modified-gravity phenomenology was born as a repair job on massive gravity.**

*Caveat, to be honest with the students:* the expansions above are the **exterior** ones ($r\gg r_V$). Demonstrating that they connect to a healthy interior solution is a separate problem. It works for dRGT; for pure Fierz–Pauli it is still unresolved, and numerical searches found no smooth interpolating solution ([Damour, Kogan & Papazoglou 2003](https://arxiv.org/abs/hep-th/0212155)).


## The Boulware–Deser ghost

*Reference: [Boulware & Deser (1972)](https://doi.org/10.1103/PhysRevD.6.3368).*

Vainshtein's rescue came at a price. If nonlinear terms are what save the theory, we must ask what *else* they do. And what they do is bring back the ghost.

The Fierz–Pauli tuning was arranged at **quadratic** order. At cubic order and beyond there is no reason for the cancellation to persist, and generically it does not: the sixth mode reappears, with negative energy.

The clean way to see it is the **ADM decomposition**, $ds^2 = -N^2dt^2 + \gamma_{ij}(dx^i+N^idt)(dx^j+N^jdt)$, where $N$ is the lapse, $N^i$ the shift and $\gamma_{ij}$ the spatial metric (6 components).

1. In GR, $N$ and $N^i$ appear **linearly** in the action. Varying them yields **constraints**, not equations of motion.
2. Those constraints, plus the gauge freedom they generate, cut $6\to2$ propagating modes.
3. The Fierz–Pauli mass term breaks the gauge symmetry but preserves one residual constraint, leaving $5$ — the correct count for a massive spin-2 field.
4. A **generic** nonlinear mass term makes $N$ appear **quadratically**. It is no longer a Lagrange multiplier, the last constraint is lost, and the sixth mode propagates:

$$\textbf{5 healthy modes } + \textbf{ 1 ghost } = \textbf{6}.$$

Worse, the ghost's mass depends on the background and can be made arbitrarily light, so it cannot be dismissed as a high-energy artefact.

For nearly forty years this was believed to be fatal, and massive gravity was largely abandoned.

## dRGT massive gravity

*References: [de Rham, Gabadadze & Tolley (2010)](https://arxiv.org/abs/1011.1232); ghost-freedom proved by [Hassan & Rosen (2012)](https://arxiv.org/abs/1106.3344).*

The resolution is beautifully simple to state: **tune the potential at every order, not just the second, so that the lapse remains a Lagrange multiplier.** The remarkable fact — the reason this is a theorem and not a wish — is that such a tuning *exists*, is essentially **unique**, and **terminates** after a finite number of terms:

$$S = \frac{M_{\rm Pl}^2}{2}\int d^4x\,\sqrt{-g}\left[R + m^2\sum_{n=2}^{4}\alpha_n\,\mathcal{U}_n(\mathcal{K})\right] + S_m ,
\qquad
\mathcal{K}^\mu{}_\nu = \delta^\mu{}_\nu - \left(\sqrt{g^{-1}f}\right)^\mu{}_\nu ,$$

with $f_{\mu\nu}$ a **fiducial (reference) metric**, $\sqrt{\;}$ the matrix square root, and $\mathcal{U}_n$ specific elementary symmetric polynomials of the eigenvalues of $\mathcal{K}$. In $d=4$ the tower stops at $n=4$ ($\mathcal{U}_{5,6}$ are total derivatives), and after normalising the mass only **two free parameters** $\alpha_3,\alpha_4$ remain.

Hassan and Rosen's proof is worth stating precisely, because it is not merely "the lapse stays linear": one must first perform a **field redefinition of the shift**, $N^i \to N^i(n^j, N)$, after which $N$ appears linearly and the missing constraint — together with its secondary constraint — reappears. The theory then propagates exactly 5 degrees of freedom on **any** background: **ghost-free nonlinear massive gravity**, a forty-year-old problem solved.

> **But notice what had to be introduced: a second metric $f_{\mu\nu}$** — exactly the rigid structure we argued at the start was unavoidable. "Massive" means "deviating from a reference", and a mass term $h_{\mu\nu}h^{\mu\nu}$ presupposes a background to define $h$. This is a genuine conceptual cost: a fixed $f_{\mu\nu}$ reintroduces an **absolute element**, precisely the sort of structure we criticised in our [Mach discussion](./Brans-Dicke.md). The natural repair is to give $f_{\mu\nu}$ its own dynamics, yielding **bimetric gravity** ([Hassan & Rosen 2012](https://arxiv.org/abs/1109.3515)): two interacting metrics, one massless and one massive graviton, $2+5=7$ degrees of freedom.

### Problems and status

Let us be honest about where this leaves us.

- **No stable flat FLRW cosmology.** Flat homogeneous isotropic solutions simply do not exist in dRGT with a flat reference metric ([D'Amico et al. 2011](https://arxiv.org/abs/1108.5231)); open ones exist but are unstable. For a theory whose selling point was cosmic acceleration, this is severe. Bimetric gravity does better.
- **A very low cutoff.** The strong-coupling scale is $\Lambda_3 = (M_{\rm Pl}m^2)^{1/3}$, which for $m\sim H_0$ gives $\Lambda_3^{-1}\simeq 1100$ km — the same number we met for cosmological Galileons, and for the same reason. The EFT is not trustworthy at scales we care about. (Note that this is the *quantum* cutoff; it is unrelated to the *classical* radius $r_V$, and $\Lambda_3^{-1}\ll r_V$.)
- **Superluminality and acausality** on some backgrounds (Deser, Waldron and collaborators), still debated.

### How heavy can the graviton be?

| bound | value | corresponding $\lambda_g = h/m_gc$ |
|---|---|---|
| GW dispersion, [LVK, *Tests of GR with GWTC-3*](https://arxiv.org/abs/2112.06861) | $m_g \le 2.42\times10^{-23}\ \mathrm{eV}/c^2$ (90% cred.) | $\gtrsim5\times10^{16}\,\mathrm{m}\simeq1.7\,$pc |
| solar-system Yukawa tests | $m_g\lesssim10^{-23}\!-\!10^{-22}\ \mathrm{eV}/c^2$ | comparable |
| **value wanted for dark energy** | $m_g\sim\hbar H_0/c^2\simeq1.4\times10^{-33}\ \mathrm{eV}/c^2$ | Hubble radius |

**Read the last row against the first.** The observational bounds are **ten orders of magnitude weaker** than the mass that would be cosmologically interesting. This is counter-intuitive and worth stating clearly to students: gravitational-wave astronomy has *not* excluded massive gravity as dark energy, and is nowhere close to doing so. The obstacles to the theory are theoretical — ghosts, cosmological solutions, the cutoff — not observational.

Note also that a graviton mass produces a **frequency-dependent** propagation speed,

$$\frac{v_g}{c} = \sqrt{1-\frac{m_g^2c^4}{E^2}},$$

which is a *dispersion*: it is measured by comparing the arrival times of different frequencies **within a single event**. This is a different signature from the constant $c_T\neq c$ constrained by GW170817 in the [Horndeski class](./Horndeski.md).

## Further reading/watching

- [Modified gravity - Rachel Rosen](https://www.youtube.com/watch?v=1THLppx96T8)
- [Massive Gravity - Claudia de Rham - 2014](https://arxiv.org/pdf/1401.4173) 
- [Theoretical Aspects of Massive Gravity - Kurt Hinterbichler - 2011](https://arxiv.org/pdf/1105.3735)
- [Schmidt-May & von Strauss - Recent developments in bimetric gravity (2015)](https://arxiv.org/abs/1512.00021)
