---
layout: default
title: Screening
parent: cosmo
---

In the [previous lecture](./Brans-Dicke.md), we saw that beautiful theoretical ideas, like Brans-Dicke trying to implement Mach's principle, are completely killed by solar system constraints or gravitational waves. There is a way around this that is often used by cosmologists: **screening mechanisms**. These mechanisms (which are arguably a bit cheating) allow the theory to remain active on cosmological scales while hiding almost completely from local data. We will look at the three main ones, and at the end we will discuss whether this it is fair to ask such features in our models.

## What should be screened?

Let us first remember again what we are trying to hide. Consider a general scalar tensor theory in the Einstein frame that we considered at the end of the [previous lecture](./Brans-Dicke.md). All the equations below were proven in the dedicated lecture, we remind them all here only for context. In the Einstein frame, gravity is ordinary GR and the scalar couples universally to matter and:

$$S = \int d^4x\sqrt{-\vert g\vert}\left[\frac{M_{\rm Pl}^2}{2}R - \frac12(\partial\phi)^2 - V(\phi)\right] + S_m\big[A^{2}(\phi)\,g_{\mu\nu},\psi\big],$$

with $M_{\rm Pl}^2 = 1/8\pi G$ the reduced Planck mass and $A(\phi)=e^{\beta\phi/M_{\rm Pl}}$ the coupling function. (We have been sloppy and renamed $\phi$ what was noted $\tilde{\phi}$ in the previous class, to un-clutter the notations). We saw that the single number

$$\beta \;\equiv\; M_{\rm Pl}\,\frac{d\ln A}{d\phi}$$

is the **dimensionless coupling strength** to matter. For Brans-Dicke, we also saw that $$\beta = 1/\sqrt{4\omega+6}$$. For a static, non-relativistic source of density $\rho$, the field equation is simply a Poisson equation with a potential term:

$$\;\nabla^2\phi = \frac{\text{d}}{\text{d}\phi}\left(V(\phi) \;+\; \frac{\beta\,\rho\,\phi}{M_{\rm Pl}}\;\right)$$

and a test particle feels, on top of gravity, a **fifth force**

$$\frac{\vec F_\phi}{m} = -\frac{\beta}{M_{\rm Pl}}\vec\nabla\phi .$$

Now take $V=0$ (a massless scalar). Then $\nabla^2\phi = \beta\rho/M_{\rm Pl}$ has the same form as the Newtonian equation $\nabla^2\Phi = \rho/(2M_{\rm Pl}^2)$, so the two forces have the *same* $1/r^2$ falloff and their ratio is a pure number:

$$\frac{F_\phi}{F_N} = 2\beta^2 .$$

A coupling of order unity therefore doubles gravity. Meanwhile the solar system measures $\gamma-1$ at the level of $10^{-5}$ ([from our second class](./validation_GR.md)). So we need either

$$\beta \lesssim 10^{-3}$$

which is a very tight constraint making the scalar almost invisible everywhere, or a mechanism that makes $\beta$, or $\nabla\phi$, small **locally** while leaving them large **cosmologically**. That is screening.

## The three classical screening mechanisms

Look at the fifth force $\propto \beta\,\nabla\phi$. There are exactly three things in the theory that can become nonlinear and kill it, and they classify the three mechanisms:

| the nonlinearity sits in… | what gets suppressed | mechanism |
|---|---|---|
| the **value** of the field: $V(\phi)$ or $\beta(\phi)$ | the field's range, or its coupling | **Chameleon** (and symmetron, dilaton) |
| the **first derivative**: $(\partial\phi)^2$ | $\vert\nabla\phi\vert$ | **K-mouflage** |
| the **second derivative**: $\partial\partial\phi$ | $\vert\nabla\phi\vert$ | **Vainshtein** |

And there is a matching statement in terms of what quantity controls whether a given object is screened in terms of the Newtonian potential $\Phi$ and its derivatives:

$$\underbrace{\Phi}_{\text{chameleon}} \qquad \underbrace{\nabla\Phi}_{\text{K-mouflage}} \qquad \underbrace{\nabla^2\Phi}_{\text{Vainshtein}}$$

— the Newtonian **potential**, the **acceleration**, and the **density**. Keep this in mind; everything below is an elaboration of this one table.

## Chameleon

Through the chameleon mechanism, **the field gets effectively heaver where matter is dense, so its force becomes short-ranged and cannot be seen.** For more on Chameleon, see e.g. [Khoury & Weltman (2004)](https://arxiv.org/abs/astro-ph/0309300). First, choose a potential that decreases with $\phi$, for example

$$V(\phi) = \frac{\Lambda^{4+n}}{\phi^{n}}, \qquad n>0 .$$

The total effective potential felt by the field is $V_{\rm eff} = V(\phi) + \beta\rho\phi/M_{\rm Pl}$. The first piece decreases with $\phi$, the second increases with $\phi$. Their sum therefore has a **minimum**. This is the whole trick: neither $V$ alone nor the coupling alone has a minimum, but the sum does. Let's locate that minimum. Set $\text{d}V_{\rm eff}/\text{d}\phi=0$:

$$-\frac{n\Lambda^{4+n}}{\phi^{n+1}} + \frac{\beta\rho}{M_{\rm Pl}} = 0$$

and hence

$$ \phi_{\rm min} = \left(\frac{n\Lambda^{4+n}M_{\rm Pl}}{\beta\rho}\right)^{\frac{1}{n+1}} \;\propto\; \rho^{-\frac{1}{n+1}} .$$

**Denser matter regions thus imply a smaller $\phi_{\rm min}$.** The effective mass of the field is the curvature of the effective potential at that minimum, $m_{\rm eff}^2 = \text{d}^2V_{\rm eff}/\text{d}\phi^2$:

$$m^2_{\rm eff} = \frac{n(n+1)\Lambda^{4+n}}{\phi_{\rm min}^{\,n+2}} \;\propto\; \rho^{\frac{n+2}{n+1}} .$$

**Denser regions means heavier field.** For $n=1$: $m_{\rm eff}\propto\rho^{3/4}$. Now, we know that a field of mass $m$ produces a [Yukawa force](./GR_fieldtheory.md) of the type

$$F_\phi \;\propto\; \frac{e^{-m_{\rm eff} r}}{r^2},$$

so its range is $\lambda = 1/m$. In the solar system $\rho$ is huge, $m$ is huge, $\lambda$ is microscopic: **no force**. In the cosmological background $\rho\sim10^{-29}\,\mathrm{g/cm^3}$, $m$ is tiny, $\lambda\sim$ Gpc: **the modification is fully active**. The field literally changes colour with its environment — hence the name.

The mass argument above is the *local* effect. For an *extended* body there is a second, stronger effect, and it is the one that actually does the work in the solar system. Let us derive it slowly. Take a static ball of radius $R$, uniform density $\rho_{\rm in}$, total mass $M$, sitting in a background of density $\rho_{\rm out}\ll\rho_{\rm in}$. Write

$$\phi_{\rm in}\equiv\phi_{\rm min}(\rho_{\rm in}),\qquad \phi_{\rm out}\equiv\phi_{\rm min}(\rho_{\rm out}),\qquad \phi_{\rm in}\ll\phi_{\rm out},$$

the two values the field would take if it were sitting at the bottom of the effective potential inside and outside. The static field equation is

$$\nabla^2\phi = \frac{\text{d}V_{\rm eff}}{\text{d}\phi} = V'(\phi) + \frac{\beta\rho}{M_{\rm Pl}} .$$

Switch off $V$ for a moment ($V'=0$). Then

$$\nabla^2\phi = \frac{\beta\rho}{M_{\rm Pl}}
\qquad\text{versus}\qquad
\nabla^2\Phi = 4\pi G\rho = \frac{\rho}{2M_{\rm Pl}^2}.$$

**Same source, same equation.** So up to a constant,

$$\boxed{\;\phi(r) = \phi_{\rm out} - 2\beta M_{\rm Pl}\,\Phi(r)\;}$$

The scalar field profile *is* the Newtonian potential, rescaled by $2\beta M_{\rm Pl}$ and flipped in sign (the field is pulled *down* where gravity is deep). Outside the body $\Phi(r)=GM/r$, and a test particle feels the acceleration $a_\phi = -(\beta/M_{\rm Pl})\nabla\phi$, giving the unscreened result

$$\frac{F_\phi}{F_N} = 2\beta^2 \qquad\text{(no screening).}$$

Keep this picture in mind: **the chameleon *wants* to be a rescaled Newtonian potential.** Screening is what happens when it is not allowed to.

Now switch $V$ back on. As $\phi$ decreases towards zero, $V(\phi)=\Lambda^{4+n}/\phi^n$ blows up: there is a wall. The field cannot descend below $\phi_{\rm in}$, where the wall exactly balances the density term. So the "Newtonian copy" of Step 1 has **a floor at $\phi_{\rm in}$**.

Compare two numbers:

| quantity | meaning |
|---|---|
| $2\beta M_{\rm Pl}\Phi$ | the drop the field *would like* to make (Step 1) |
| $\phi_{\rm out}-\phi_{\rm in}$ | the drop it *is allowed* to make (Step 2) |

- **Allowed drop $>$ requested drop** — the field never reaches the floor, Step 1 holds everywhere, the body is **unscreened**: $F_\phi/F_N = 2\beta^2$. (In the literature: *thick shell*.)
- **Allowed drop $<$ requested drop** — the field hits the floor at some radius $R-\Delta R$, and just *sits there* all the way to the centre. The body is **screened**. (In the literature: *thin shell*.)

Everything below is the second case.

For $r < R-\Delta R$ the field is constant, $\phi=\phi_{\rm in}$, hence $\nabla\phi = 0$: **no gradient, no force, and — crucially — no contribution to the exterior field.** Why is the core so rigid? Because inside, $m_{\rm eff}(\rho_{\rm in})$ is huge: any attempt to displace $\phi$ from $\phi_{\rm in}$ is damped over a distance $1/m_{\rm eff}\lll R$. The interior is a Faraday-cage-like region for $\phi$.

Only the outer layer $R-\Delta R < r < R$, where the field climbs from $\phi_{\rm in}$ up towards $\phi_{\rm out}$, has a gradient. That layer is the **thin shell**.

Integrate $$\nabla^2\phi = \beta\rho/M_{\rm Pl}$$ over a sphere of radius $R$ (dropping $V'$, which is negligible compared to $$\beta\rho_{\rm in}/M_{\rm Pl}$$ as soon as $$\phi>\phi_{\rm in}$$ — by definition of $$\phi_{\rm in}$$ the two are equal *at* $$\phi_{\rm in}$$, and $\vert V'\vert$ falls off above it):

$$4\pi R^2\,\phi'(R) = \frac{\beta}{M_{\rm Pl}}\,M_{\rm shell},
\qquad
M_{\rm shell} \simeq 4\pi R^2\,\Delta R\,\rho_{\rm in} = M\,\frac{3\Delta R}{R}.$$

The core contributes nothing because $\phi'=0$ on its boundary. Therefore the exterior solution is exactly the Step-1 solution **with $M$ replaced by an effective charge**

$$M_{\rm eff} = \frac{3\Delta R}{R}\,M \;\ll\; M,
\qquad
\phi(r>R) = \phi_{\rm out} - 2\beta M_{\rm Pl}\,\frac{G M_{\rm eff}}{r}\,e^{-m_{\rm out}(r-R)} .$$

**This is what "thin shell" means: as far as the scalar field is concerned, the object weighs only $M_{\rm shell}$, not $M$.** A screened Sun is, for $\phi$, a hollow shell.

We know the *shape* of the solution but not yet the thickness $\Delta R$. Fix it by requiring that the field, going from the floor $\phi_{\rm in}$ out to infinity, climbs exactly the available height $\phi_{\rm out}-\phi_{\rm in}$.

The climb happens in two places, and this is the subtle point:

1. **Across the shell itself.** There $\phi'' \simeq \beta\rho_{\rm in}/M_{\rm Pl}$ (locally 1D since $\Delta R\ll R$), with $\phi'=0$ at the inner edge. Integrating twice, $\phi(R)-\phi_{\rm in} = \tfrac12(\beta\rho_{\rm in}/M_{\rm Pl})\Delta R^2 = 3\beta M_{\rm Pl}\Phi\left(\Delta R/R\right)^2$.
2. **Along the exterior $1/r$ tail**, from $r=R$ to infinity: $\phi_{\rm out}-\phi(R) = 2\beta M_{\rm Pl}\dfrac{GM_{\rm eff}}{R} = 6\beta M_{\rm Pl}\Phi\dfrac{\Delta R}{R}$.

Contribution 2 is $O(\Delta R/R)$, contribution 1 is $O((\Delta R/R)^2)$: **most of the climb happens outside the body, not in the shell.** (This is why the final answer is *linear* in $\Delta R/R$; a naive "the field climbs across the shell" argument gives a wrong quadratic law.) Keeping the leading term,

$$\phi_{\rm out}-\phi_{\rm in} \simeq 6\beta M_{\rm Pl}\Phi\,\frac{\Delta R}{R}
\qquad\Longrightarrow\qquad
\boxed{\;\frac{\Delta R}{R} \simeq \frac{\phi_{\rm out}-\phi_{\rm in}}{6\,\beta\,M_{\rm Pl}\,\Phi}\;},
\qquad \Phi=\frac{GM}{R}.$$

Combining Steps 1 and 4, the exterior fifth force is the unscreened one reduced by $M_{\rm eff}/M$:

$$\frac{F_\phi}{F_N} \simeq 2\beta^2\cdot\frac{3\Delta R}{R} = \frac{\beta\,(\phi_{\rm out}-\phi_{\rm in})}{M_{\rm Pl}\,\Phi}\;\ll\;2\beta^2 .$$

Read the last expression: **at fixed model parameters the fifth force is suppressed as $1/\Phi$.** Note also that one power of $\beta$ has cancelled — a *stronger* coupling makes the body *more* screened, which is the counter-intuitive signature of the mechanism.

Note however that the formula was derived for $\Delta R/R\ll1$. Setting $\Delta R/R\to1$ gives the screening criterion $\Phi \gtrsim \chi \equiv (\phi_{\rm out}-\phi_{\rm in})/(6\beta M_{\rm Pl})$, where $\chi$ is called the **self-screening parameter**. The $O(1)$ coefficient there should not be taken seriously — the crude argument of Step 2 gives $2\beta M_{\rm Pl}\Phi$ instead of $6\beta M_{\rm Pl}\Phi$ — but the *scaling* $\Phi$ vs. $(\phi_{\rm out}-\phi_{\rm in})/\beta M_{\rm Pl}$ is exact.

Thus **Screening is controlled by $\Phi$, not by $\rho$**. This deserves to be stated on its own, because it is constantly confused: **the criterion is the depth of the gravitational potential well, not the density.** A diffuse but massive halo can be screened; a dense but small object need not be.

Two further consequences:

- **Environmental (or "blanket") screening.** $\phi_{\rm out}$ is the ambient value, set by the *neighbourhood*, not by the cosmological mean. A small body inside an already-screened big one lives in a bath where $\phi$ is already low, so $\phi_{\rm out}-\phi_{\rm in}$ is tiny and it is screened for free. This is why the Earth passes, despite $\Phi_\oplus = 7\times10^{-10}$. See [Hui, Nicolis & Stubbs (2009)](https://arxiv.org/abs/0905.2966).
- **Violation of the (weak) equivalence principle.** A screened and an unscreened body fall differently in the same external field: only the unscreened one feels $F_\phi$. Hui, Nicolis & Stubbs make this the sharp prediction — *small galaxies fall faster than large ones*.

| object | $\Phi$ | screened? |
|---|---|---|
| galaxy cluster | $\sim10^{-5}$ | yes |
| Sun | $2\times10^{-6}$ | yes |
| Milky Way | $\sim10^{-6}$ | yes |
| Earth | $7\times10^{-10}$ | yes — blanketed by the Galaxy |
| **dwarf galaxy in a void** | $\sim10^{-8}$ | **no** |

For Hu–Sawicki $f(R)$ with $n=1$ the self-screening parameter is $$\chi=\tfrac32\vert f_{R0}\vert$$, so requiring the Milky Way ($\Phi\sim10^{-6}$) to be screened gives the familiar bound $$\vert f_{R0}\vert\lesssim10^{-6}$$ (see the review [Brax, Casas, Desmond & Elder (2022)](https://arxiv.org/abs/2201.10817)).

That last table line is a genuine observational strategy, not a curiosity: **look for dwarf galaxies in voids and compare them with identical dwarfs inside clusters.** If gravity is environment-dependent, their stars (screened, compact) and their gas (unscreened, extended) will not trace the same rotation curve, and the two populations of dwarfs will differ systematically. This is a prediction $\Lambda$CDM simply cannot make.


[Wang, Hui & Khoury (2012)](https://arxiv.org/abs/1208.4612) is the paper to know before believing any claim that a chameleon "explains dark energy" or "modifies structure growth". The remarkable thing is that it uses **one single observational input** — the Milky Way must be screened — and gets two very strong conclusions out of it. From before, the Milky Way is screened provided:

$$\Delta\ln A \;\equiv\; \ln\frac{A(\phi_{\rm out})}{A(\phi_{\rm in})} \;=\; \frac{\beta\,(\phi_{\rm out}-\phi_{\rm in})}{M_{\rm Pl}} \;\lesssim\; \Phi_{N,\rm MW}\sim 10^{-6}.$$

Note how the thin-shell condition has been rewritten: it is a statement about **how much the conformal factor $A$ is allowed to vary between the cosmological environment and the interior of a galaxy.** That reformulation is the whole idea, because $A$ is also what controls the cosmology.

Today the ambient field sits at $\phi_{\rm min}(\bar\rho_0)$. At $z\simeq1$ the mean density was $\sim8$ times larger, so $\phi$ was smaller — but it was still far above the value it takes inside the Milky Way, since $\rho_{\rm MW}\ggg\bar\rho(z=1)$. So the cosmological excursion of $\phi$ over the last Hubble time is *bounded by* the galactic one:

$$\Delta\ln A\Big|_{z=1\to0} \;\lesssim\; 10^{-6}.$$

**The conformal factor is frozen to one part in a million over the entire recent history of the Universe.**

A chameleon cannot self-accelerate. Matter, rulers and clocks live in $\tilde g_{\mu\nu}=A^2 g_{\mu\nu}$. The *entire* difference between "GR + a scalar" and "modified gravity" is carried by $A$. If $A$ is constant to $10^{-6}$ over the last Hubble time, then the observed (Jordan-frame) expansion history is identical to the Einstein-frame one to one part in $10^{6}$ — and the Einstein frame is plain GR plus a minimally coupled scalar with potential $V$.

Therefore whatever accelerates the Universe is $V$ itself: **quintessence or a cosmological constant**. In the authors' words, *"the modification of gravity has nothing to do with the acceleration phenomenon."* Concretely: a Hu–Sawicki $f(R)$ model accelerates because $f(R)$ contains an effectively constant piece $\simeq-2\Lambda$. You have not explained $\Lambda$ — you have rewritten it.

Now The chameleon force can never reach beyond $\sim$ Mpc today. This one is a short chain of steps; let us do them all.

**(a) The field tracks the minimum.** Differentiate the minimum condition $V'(\phi_{\rm min})+\beta\rho/M_{\rm Pl}=0$ with respect to cosmic time, using $m^2 = V''$:

$$m^2\,\dot\phi_{\rm min} + \frac{\beta}{M_{\rm Pl}}\dot\rho = 0,
\qquad \dot\rho = -3H\rho
\quad\Longrightarrow\quad
\dot\phi_{\rm min} = \frac{3H\beta\rho}{M_{\rm Pl}\,m^{2}} .$$

**(b) Bound the density.** Matter cannot exceed the critical density: $\rho \le 3M_{\rm Pl}^2H^2$. Hence $\dot\phi_{\rm min}\lesssim 9\beta M_{\rm Pl}H^{3}/m^{2}$.

**(c) Excursion over a Hubble time**, $\Delta t\sim1/H$:

$$\Delta\phi \;\sim\; \frac{\dot\phi_{\rm min}}{H} \;\lesssim\; \frac{9\beta M_{\rm Pl}H^{2}}{m^{2}} .$$

**(d) Impose Step 1**, $\beta\Delta\phi/M_{\rm Pl}\lesssim10^{-6}$:

$$\frac{9\beta^{2}H^{2}}{m^{2}} \lesssim 10^{-6}
\qquad\Longrightarrow\qquad
m_0 \;\gtrsim\; 3\times10^{3}\,\beta\,H_0 .$$

**(e) Translate into a range.** With $H_0^{-1}\simeq4.4\,$Gpc,

$$\lambda_0 = \frac{1}{m_0} \;\lesssim\; \frac{10^{-3}}{\beta}\,H_0^{-1} \;\sim\; \frac{{\rm few}}{\beta}\ \mathrm{Mpc}.$$

**So the naive expectation "$\lambda\sim$ Gpc in the cosmological background" is wrong by three orders of magnitude.** The logic is a tug-of-war: a light field has a long range, but a light field also rolls a lot as $\rho$ dilutes, and rolling a lot means $A$ changes a lot, which the Milky Way forbids. The Milky Way constraint is therefore *also* a constraint on the cosmological Compton wavelength.
Hence:

- **No signal on linear scales.** Linear $P(k)$, redshift-space distortions, the CMB, the growth rate $f\sigma_8$ on $\gtrsim10\,$Mpc scales: a chameleon does nothing there. Any claim of a chameleon modifying linear growth at $100\,$Mpc is wrong.
- **The observational programme must be non-linear or local**: dwarf galaxies, galaxy outskirts, cluster profiles, the lab. Far from killing the void-dwarf strategy of §4, the theorem is what *forces* you into it.
- **Scope — read this carefully.** The theorems apply to screening by a *conformal coupling plus a potential*: chameleon, symmetron, dilaton, $f(R)$. They do **not** apply to derivative/Vainshtein screening (galileons, massive gravity, K-mouflage), where the coupling is not of the form $A(\phi)$ and the non-linearity is in the kinetic term. Those models are constrained differently — this is one of the main reasons the field moved towards Horndeski/Vainshtein after 2012.
- **Loopholes are narrow but exist**: the derivation assumes the field adiabatically tracks the minimum, and that the Milky Way is screened *by the chameleon itself*.

Many well known models have chameleon behavior:

- **Symmetron** ([Hinterbichler & Khoury 2010](https://arxiv.org/abs/1001.4525)): instead of the mass growing, the *coupling* switches off. Take $V=-\tfrac12\mu^2\phi^2+\tfrac{\lambda}{4}\phi^4$ and $A = 1 + \phi^2/2M^2$, so $\beta\propto\phi$. In dense regions the effective potential's minimum returns to $\phi=0$ — the symmetry is *restored* — and with it $\beta\to0$. No coupling, no force.
- **Dilaton** :
- **$f(R)$ gravity is a chameleon.** As we will see (and said many times already), $f(R)$ is a Brans-Dicke theory with $\omega=0$ and a potential — and $\omega=0$ is wildly excluded by the solar system. It survives only because the potential screens it (Hu–Sawicki model).
- Because "dense environment" includes *the walls of a vacuum chamber*, chameleons are strongly constrained in the **laboratory** or **near earth**: atom interferometry, torsion balances, atomic clocks, Casimir experiments, or in earth's orbit: ([Burrage, Copeland & Hinds 2015](https://arxiv.org/abs/1408.1409), [Pernot-Borràs (2019)](https://arxiv.org/pdf/1907.10546), [(2020)](https://arxiv.org/pdf/2004.08403) and [(2021)](https://arxiv.org/pdf/2102.00023).

## K-mouflage

As its name indicates, K-mouflage is a sort of camouflage for k-essence models! See for example [Babichev, Deffayet & Ziour (2009)](https://arxiv.org/abs/0905.2943). The idea is to **give the field a non-standard kinetic term, so that where the field gradient is large the field becomes hard to move, and its gradient — hence the force — is suppressed.** For this one has to deform the kinetic term. Instead of the standard $-\tfrac12(\partial\phi)^2$, write

$$\mathcal{L}_\phi = M^4\,K(X),\qquad X \equiv \frac{(\partial\phi)^2}{2M^4},$$

with $K(X) \simeq X$ for small $X$ (so we recover the standard theory at small gradients) but $K(X)\simeq X^{m}$ with $m>1$ for large $X$.

The field equation becomes

$$\vec\nabla\cdot\big[\,K'(X)\,\vec\nabla\phi\,\big] = \frac{\beta\rho}{M_{\rm Pl}} .$$

Compare with electrostatics in a **dielectric**: $K'(X)$ plays the role of a field-dependent permittivity. Where the gradient is large, the medium becomes "stiff" and resists.

Now integrate again for a point mass. Spherical symmetry lets us integrate once over a ball of radius $r$:

$$K'(X)\;\phi'(r)\;r^2 = \frac{\beta M}{4\pi M_{\rm Pl}} \equiv \text{const}.$$

Now we identify two regimes:

*Far away (small gradient), $K'=1$:*
$$\phi'(r) = \frac{\beta M}{4\pi M_{\rm Pl}\,r^{2}} \qquad\Longrightarrow\qquad \frac{F_\phi}{F_N}=2\beta^2 \quad\text{(unscreened)}.$$

*Close in (large gradient), $K'\propto X^{m-1}\propto (\phi')^{2(m-1)}$:*
$$(\phi')^{2m-1}\,r^{2} = \text{const} \qquad\Longrightarrow\qquad \phi' \propto \left(\frac{M}{r^{2}}\right)^{\frac{1}{2m-1}} .$$

Since $F_N \propto M/r^2$,

$$\frac{F_\phi}{F_N} \;\propto\; \left(\frac{M}{r^2}\right)^{\frac{1}{2m-1}-1} = \left(\frac{M}{r^2}\right)^{-\frac{2(m-1)}{2m-1}} .$$

For any $m>1$ the exponent is **negative**: the larger $M/r^2$, the smaller the ratio. For $m=2$ it goes as $(M/r^2)^{-2/3}$.

Nonlinearity switches on when $X\sim1$, i.e. $$\vert\nabla\phi\vert\sim M^2$$. Substituting the far-field solution:

$$R_K = \left(\frac{\beta M}{4\pi M_{\rm Pl}M^{2}}\right)^{1/2}.$$

Inside $r<R_K$, the fifth force is suppressed. Notice that $M/r^2$ is (up to constants) the **Newtonian acceleration** $$g_N = \vert \vec\nabla\Phi\vert$$. So: **K-mouflage screens wherever the gravitational field is strong**, regardless of the depth of the potential well. This is a genuinely different criterion from the chameleon's. In particular it does *not* switch off far from a body even if the body is massive, and it is therefore constrained mostly by the outer solar system and cluster outskirts rather than by laboratory tests.

Acceleration-based modification of gravity should ring a bell: it is exactly the logic of **MOND**, where new physics turns on below $a_0\simeq1.2\times10^{-10}\,\mathrm{m\,s^{-2}}$. K-mouflage is, in this sense, MOND run backwards: instead of switching the modification *on* at low acceleration, it switches it *off* at high acceleration. Same organising variable, opposite intent.

## Vainshtein

[Vainshtein (1972)](https://doi.org/10.1016/0370-2693(72)90147-5)'s problem was not dark energy but **massive gravity**. It is as such the oldest form of screening in modified gravity. This mechanism was then rediscovered as the key feature of Galileon theories. We will discuss how it appears in massive gravity in the [dedicated class](./massive-gravity.md). 

In one sentence: **Make the field's own second-derivative self-interactions large near a source, so that the field is "stiffened" and its gradient suppressed.**

First we introduce **the cubic Galileon.** Take the simplest theory with second-derivative self-interaction:

$$\mathcal{L} = -\frac12(\partial\phi)^2 - \frac{1}{\Lambda^3}(\partial\phi)^2\,\Box\phi + \frac{\beta}{M_{\rm Pl}}\phi\,\rho ,$$

where $\Lambda$ is a new energy scale. (In the language of the [Horndeski class](./Horndeski.md), this is $G_3\propto X$.)

**Spherical symmetry makes it algebraic.** Integrating the field equation once over a ball, and writing $y \equiv \phi'(r)/r$, everything collapses to a **quadratic equation**:

$$y \;+\; \frac{4}{\Lambda^3}\,y^{2} \;=\; \frac{\beta}{4\pi M_{\rm Pl}}\frac{M}{r^{3}} .$$

This is the whole mechanism in one line: one linear term, one nonlinear term, and a source.

**Far from the source** the linear term wins:

$$\phi'(r) = \frac{\beta M}{4\pi M_{\rm Pl}r^{2}} \qquad\Longrightarrow\qquad \frac{F_\phi}{F_N} = 2\beta^2 \quad\text{(unscreened)}.$$

**Close to the source** the quadratic term wins:

$$\left(\frac{\phi'}{r}\right)^{2} \simeq \frac{\Lambda^3\beta M}{16\pi M_{\rm Pl}r^{3}} \qquad\Longrightarrow\qquad \phi' \;\propto\; r^{-1/2},$$

which is a *much* gentler profile than the $r^{-2}$ of gravity.

Comparing with $F_N\propto r^{-2}$,

$$\boxed{\;\frac{F_\phi}{F_N} \;\sim\; 2\beta^2\left(\frac{r}{r_V}\right)^{3/2}\;}$$

which vanishes as $r\to0$. The **Vainshtein radius** is where the two terms in Step 2 balance:

$$r_V \sim \left(\frac{\beta M}{M_{\rm Pl}\Lambda^{3}}\right)^{1/3} \sim \left(\frac{r_S}{\Lambda^3}\right)^{1/3},\qquad r_S = 2GM .$$

This is worth doing, because the result is startling. If the Galileon is to drive cosmic acceleration, its scale must be $\Lambda^3\sim M_{\rm Pl}H_0^2$, so $r_V\sim\big(r_S H_0^{-2}\big)^{1/3}$. For the **Sun**, $r_S = 3\,$km and $H_0^{-1}=1.3\times10^{26}\,$m:

$$r_V \simeq \left(3\times10^{3}\times(1.3\times10^{26})^{2}\right)^{1/3}\,\mathrm{m} \simeq 1.7\times10^{18}\,\mathrm{m}\;\simeq\;\boxed{55\ \mathrm{pc}}$$

Compare with the size of the solar system, $\sim30\,$AU $=1.5\times10^{-4}\,$pc. So we live at

$$\frac{r}{r_V}\sim 3\times10^{-6} \qquad\Longrightarrow\qquad \frac{F_\phi}{F_N}\sim\left(3\times10^{-6}\right)^{3/2}\sim 10^{-9}.$$

**Four orders of magnitude below what Cassini could ever detect** — and the screening region extends out to a hundred times the distance to the nearest star. The theory is completely invisible locally while being an $\mathcal{O}(1)$ modification on cosmological scales. That is why Vainshtein is the most powerful of the three, and also why it is the most frustrating: there is essentially no local experiment that can test it.

Since $M/r^3\sim\rho$, and $\nabla^2\Phi \propto \rho$:

**Vainshtein screens wherever the density (equivalently the spacetime curvature) is high.**

### One crack

In **beyond-Horndeski** theories (GLPV, DHOST — see the [previous class](./Horndeski.md)) the Vainshtein mechanism is **partially broken *inside* matter**: the fifth force is suppressed outside a body but survives within it. This is very good news observationally, because it gives back a handle: modified stellar structure (and hence the mass–radius relation of dwarf stars), altered cluster density profiles, and deviations in the interiors of neutron stars.

## Summary

| | Chameleon | K-mouflage | Vainshtein |
|---|---|---|---|
| nonlinearity in | $\phi$ (potential/coupling) | $\partial\phi$ | $\partial\partial\phi$ |
| screened when large | $\Phi$ (potential) | $\nabla\Phi$ (acceleration) | $\nabla^2\Phi$ (density) |
| typical theories | $f(R)$, symmetron, dilaton | k-essence, DBI | Galileons, DGP, massive gravity |
| suppression close in | Yukawa $e^{-mr}$ + thin shell | $(M/r^2)^{-\frac{2(m-1)}{2m-1}}$ | $(r/r_V)^{3/2}$ |
| best test | dwarf galaxies in voids; lab experiments | outer solar system; cluster outskirts | breaking inside matter (beyond-Horndeski) |
| escapes GW170817? | yes ($G_4(\phi)$ only) | yes | the cubic Galileon does, higher ones do not |


## So — is it cheating?

Now you might feel that adding such mechanism to "hide the undesired effects" is some kind of cheating. Indeed, if screening is introduced *after* the theory has failed, and its only job is to hide the very effect the theory was invented to predict, it is arguably unsatisfying. Each new null result is absorbed by tightening the screening rather than by abandoning the model. There is something unfalsifiable in that pattern. Worse, screened theories typically have a very low strong-coupling scale — for a cosmological Galileon, $$\Lambda\sim(M_{\rm Pl}H_0^2)^{1/3}\sim10^{-13}\,$$eV, corresponding to a length of about $1000\,$km — so the effective field theory we are computing with breaks down at scales at which we would like to trust it. (This is the same worry as the [de Rham–Melville caveat](https://arxiv.org/abs/1806.09417) on GW170817.)

However, it is still worth considering screening for at least three reasons:

1. **Screening is not put in by hand in some models.** The chameleon needs only a runaway potential; the Galileon nonlinearity is *required* by the Galileon symmetry $\partial_\mu\phi\to\partial_\mu\phi + c_\mu$ that protects the theory from quantum corrections. Nobody added a term whose purpose is to hide things; the terms were already there, and the hiding is a consequence. The same thing apply for Vainshtein screening; which as further discussed in the [massive gravity](./massive-gravity.md) class, appears naturally to answer specific questions of these models and not as a way to "hide the problems". 
2. **There is ample precedent in physics! Screening exists** Debye screening hides electric charge in a plasma; the Higgs mechanism hides the weak force by giving it a mass; QCD confinement hides colour entirely. "A fundamental interaction is invisible in the regime we happen to inhabit, because of a medium or a nonlinearity" is a completely standard physical situation, not a dodge.
3. **It makes a sharp, distinctive prediction that $\Lambda$CDM cannot make: gravity becomes environment-dependent.** Two identical galaxies, one in a void and one in a cluster, should have measurably different internal dynamics. Nothing in standard cosmology allows that. Far from being unfalsifiable, screening tells you exactly where to look.

Screening is legitimate physics but a poor scientific bargain: it rescues the theories at the cost of pushing their signatures into precisely the regimes that are hardest to measure. And it is worth keeping in mind — as our Brans-Dicke discussion showed — that the parameter space keeps shrinking under each new constraint, without any positive detection so far. A mechanism that is invoked only to explain non-detections is not wrong, but it is not yet evidence for anything either.

## Further reading

- [Joyce, Jain, Khoury & Trodden - Beyond the Cosmological Standard Model (2015)](https://arxiv.org/abs/1407.0059) — §4 is the standard pedagogical treatment of all three mechanisms.
- [Brax - Screening mechanisms in modified gravity (2013)](https://doi.org/10.1088/0264-9381/30/21/214005)
- [Burrage & Sakstein - Tests of chameleon gravity (2018)](https://arxiv.org/abs/1709.09071).
- [Khoury - Les Houches lectures on physics beyond the Standard Model of cosmology (2010)](https://arxiv.org/abs/1011.5909)
