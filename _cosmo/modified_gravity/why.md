---
layout: default
title: Why?
parent: cosmo
---

## Why going beyond GR?

Now, we saw in the previous classes that GR is an extremely successful theory both:

- *from an observational point of view*: EEP and SEP are validated at extremely high precisions in very wide different physical conditions and different systems. This concerns very different conditions and space-time scales in the Universe: laboratory, solar system, astrophysics, cosmology and very different field conditions: weak, strong, dynamical and even extreme. Only the quantum regime realm remains largely unexplored.
- *from a theoretical point of view*: Most physicist would surely agree that GR is for sure a  beautiful theory, which unifies some of the deepest concepts of physics as gravity, space and time in a single geometric framework. Can we dream of more? Furthermore, we saw that GR admits a field theoretic reading, and that it can have multiple geometrical faces. Even more powerfully: **Weinberg-Deser theorem** and its geometric counterpart, the **Lovelock theorem** (discussed in the [next class](./Lovelock_thm.md)) are powerful **no-go theorems** that tell us that GR is **hard to avoid** and it always appears as the required theory when one try to build a field or geometric theory of gravity with minimal assumptions.

So why would we even want to go beyond GR?

### Why not?

Well, the trivial answer to this question is simply that we are physicists and as physicists we need to explore all possibilities.

But this answer is much less trivial than it sounds. **A theory like GR is only ever tested *against* something else.** Saying "GR is validated at the $10^{-15}$ level" is, strictly speaking, meaningless until we say *validated against which alternative* (in that case, a deviation of UFF). What we actually constrain is a **parameter of deviation**: a number that vanishes if GR is exact and is non-zero otherwise. We already saw some examples in [the second lecture](./validation_GR.md) with the $\eta,\tilde{\alpha},\delta$ parametrization of the EEP and the **PPN formalism**.

The no-go theorems do not say that "nothing else than GR exists". On the other hand, they say that *given a list of assumptions $A_1, \dots, A_n$, GR is unique*. This is fantastic, because we know exactly what assumptions we may want to break and try to think how and if it could be really motivated by deeper physics. This will be the topic of our [next lecture](./Lovelock_thm.md). 

As beautiful and resilient as it is, GR is not perfect as a theory: we poorly understand how energy conservation works at all in GR, we do not understand where the information goes when it enters a black hole, we have almost no idea what singularities are and if they exist, in the center of black holes and at the origin of the Universe. Worse than this: as you know for sure, we have no idea how to properly combine GR with all our other (quantum) physical theories!

Note that, Newtonian gravity was, in 1900, in a comparable position than GR: verified to spectacular precision over two centuries, theoretically compelling, with one small anomaly of $43''$ per century in the perihelion of Mercury. The lesson is not that anomalies always win — most do not — but that the *only* way to know is to have the alternative theory written down and confronted with data.

### Dark energy and dark matter

Let us now turn to the classic cosmological motivations. As discussed in the [dedicated class](./cosmology.md), the standard model of cosmology, $\Lambda$CDM, requires two dark components that represent $\sim 95\%$ of today's energy content of the Universe.

We saw that modifying gravity could be a good idea to explain these dark components: a different law of gravity above a treshold acceleration (MOND like) could explain **dark-matter** and modifications of the gravitational pull on the very large scale (like its weakening because of a massive graviton) could explain **dark energy**. 

**However** we also saw that both of these approaches are in real difficulties today:

- MOND like theories and its relativistic generalizations (like TeVS) have a hard time explaining observations as the **bullet cluster** or the **CMB acoustic peaks** without a "matter like" component that generates gravity **independently of the baryons**. This component could be a new field, but then it becomes totally blurred whether this still counts as a simple modification of gravity.

- Modified gravity models targeting dark energy can provide multiple path to explain today's acceleration of the Universe, but $\Lambda$ does as well, and so-far it does it very well. Such models however **rarely solve or even address the cosmological constant problem**  because they face strong no-go theorems and huge fine tuning problems as discussed by [Weinberg (1989)](https://doi.org/10.1103/RevModPhys.61.1).

### Cosmological tensions

A second, more recent, empirical motivation comes from observational *tensions* within $\Lambda$CDM: cases where two different datasets, both analysed within the same model, return incompatible values for the same parameter. A tension is not a detection of new physics — it can always be an instrumental or astrophysical systematic effect — but it is precisely the kind of crack where new physics would first appear.

**The $H_0$ tension.** $H_0 \equiv \dot a/a \vert_{t_0}$ is the present expansion rate. It is measured in two very different ways:

- *Late-time, direct (the distance ladder)*: calibrate Cepheids geometrically, use them to calibrate Type Ia supernovae, read off the local expansion rate. SH0ES obtains $H_0 = 73.04 \pm 1.04\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ [Riess (2022)](https://arxiv.org/abs/2112.04510).
- *Early-time, indirect (the CMB)*: fit the acoustic peaks of the CMB assuming $\Lambda$CDM, which fixes the **sound horizon at last scattering** $r_s \simeq 147$ Mpc — the comoving distance a sound wave travels in the photon–baryon plasma before recombination — and then infer $H_0$. Planck obtains $H_0 = 67.27 \pm 0.60\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ [Planck 2018](https://arxiv.org/abs/1807.06209).

The discrepancy sits around $5\sigma$, and reaches higher significance for some dataset combinations [Cai and Wang (2026)](https://arxiv.org/abs/2606.20434).

The crucial point — and the reason this is a *gravity* question and not only an astronomy question — is the following. The CMB and BAO do not measure $H_0$; they measure the **angular scale** $\theta_s = r_s / D_A$, where $D_A$ is the distance to the last-scattering surface, itself an integral $\int dz/H(z)$. So the data constrain the *combination* $r_s H_0$. It follows that you can raise $H_0$ either by *lowering $r_s$* (early-time new physics, before recombination) or by *changing $H(z)$ at low $z$* (late-time new physics). But the low-$z$ route is boxed in from both sides: supernovae and BAO already pin the shape of $H(z)$ for $z \lesssim 2$ quite tightly, so late-time modifications — including most modified-gravity dark energy — cannot move $H_0$ enough without breaking the fit. This is the "**Hubble hunter's guide**" argument [Knox & Millea (2020)](https://arxiv.org/abs/1908.03663), and it is why attention has shifted to *early*-time solutions such as **early dark energy** [Poulin et al. (2019)](https://arxiv.org/abs/1811.04083) or **early variation of the fundamental constants** [Hart and Chluba (2021)](https://arxiv.org/abs/2107.12465). Even these are strongly constrained, and [Cai and Wang (2026)](https://arxiv.org/abs/2606.20434) concludes that a full resolution likely requires *correlated* early- and late-time modifications.

**The $w_0$–$w_a$ hint.** The second tension concerns the equation of state of dark energy, $w \equiv p_{\rm DE}/\rho_{\rm DE}$, with $w = -1$ exactly for a cosmological constant. It is standard to allow $w$ to vary with the scale factor $a$ through the **CPL (Chevallier–Polarski–Linder) parametrization**
$$w(a) = w_0 + w_a(1-a), \qquad a = \frac{1}{1+z},$$
so that $w_0$ is the value today ($a=1$) and $w_0 + w_a$ its asymptotic past value. DESI's BAO measurements, combined with the CMB and supernovae, prefer $w_0 > -1$ and $w_a < 0$ over $\Lambda$CDM [DESI (2025)](https://arxiv.org/abs/2503.14738). The significance is **strongly dataset-dependent**: around $2$–$3\sigma$ for BAO+CMB alone, rising to $2.8$–$4.2\sigma$ depending on which supernova compilation is used, and it is sensitive to redshift-dependent SN calibration residuals at the few $\times 10^{-2}$ mag level (see e.g. by , [Turyshev (2026)](https://arxiv.org/abs/2602.05368), and [Wang (2026)](https://arxiv.org/abs/2504.15222))

Why does this matter *for gravity*? Because $w_0 > -1$ with $w_a<0$ means $w(z)$ **crossed** the *phantom divide* $w=-1$ at low redshift. And there is a small no-go theorem here too: a single canonical, minimally coupled scalar field in GR has $-1 \le w \le 1$ and cannot cross $w=-1$ without developing a ghost or a gradient instability [Vikman (2005)](https://arxiv.org/abs/astro-ph/0407107). If the crossing is real, then the minimal quintessence picture fails, and one is pushed towards *non-minimal coupling to curvature*, *multiple fields*, or *genuinely modified gravity*. This is, at present, the sharpest observational hint pointing beyond the simplest GR + scalar field picture — with the emphasis on *hint*.

### Quantum gravity

Probably the most important point of all — and the only one of these motivations that is a **theoretical necessity** rather than an empirical hint. **Gravity must be quantized, at least in part.** Einstein's equations relate the classical tensor $G_{\mu\nu}$ to $T_{\mu\nu}$, the stress-energy of matter — but matter is quantum. Writing $G_{\mu\nu} = \kappa \langle \hat T_{\mu\nu}\rangle$ (semi-classical gravity) is a useful approximation but cannot be fundamental: it is non-linear in the quantum state and leads to inconsistencies with the measurement postulate. We must understand what to do with this.

There is no easy answer as **GR quantized naively is famously non-renormalizable.** Expanding $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ and quantizing $h_{\mu\nu}$ works fine as a **perturbative expansion at low energies** — but the coupling constant is $\kappa = 8\pi G/c^4$, which is *dimensionful*: $[G] = (\text{mass})^{-2}$ in natural units. Dimensional analysis then implies that loop corrections come with positive powers of $E/M_{\rm Pl}$, where $M_{\rm Pl} = \sqrt{\hbar c/G} \simeq 1.22\times 10^{19}\ \mathrm{GeV}$, and that the divergences require *new counterterms at every loop order*. Concretely:
  - pure gravity is finite at one loop (the divergence is a total derivative, by the Gauss–Bonnet identity in $D=4$), but gravity **coupled to matter** already diverges at one loop;
  - pure gravity diverges at **two loops**, with a counterterm $\propto \int d^4x \sqrt{-g}\, C_{\mu\nu}{}^{\rho\sigma}C_{\rho\sigma}{}^{\alpha\beta}C_{\alpha\beta}{}^{\mu\nu}$ built from the Weyl tensor, and a non-zero coefficient $209/(2880(4\pi)^4)$.

  Predictivity is therefore lost at high energy: one would need infinitely many measurements to fix infinitely many couplings.

In a way, **GR predicts its own breakdown.** The **singularity theorems** show that, under reasonable energy and causality conditions, geodesic incompleteness is generic in gravitational collapse and in cosmology [Penrose (1965)](https://doi.org/10.1103/PhysRevLett.14.57). A theory that predicts, from its own equations, that its own description fails at finite proper time, is telling us it is incomplete. Add the **black hole information problem** and the thermodynamic interpretation of horizons ($S = A/4G\hbar$), and the conclusion is hard to escape: GR is the low-energy limit of something else.

**This *already* forces us beyond GR.** The modern reading is thus that GR is an **effective field theory (EFT)**: perfectly predictive below $M_{\rm Pl}$, provided one writes the *most general* action compatible with diffeomorphism invariance,
$$S = \int d^4x\,\sqrt{-g}\left[ \frac{M_{\rm Pl}^2}{2}\left(R - 2\Lambda\right) + c_1 R^2 + c_2 R_{\mu\nu}R^{\mu\nu} + \mathcal{O}(\partial^6) + \dots\right],$$
and treats the higher-curvature terms perturbatively. Quantum loops **generate these terms whether we want them or not**. In this precise sense, "beyond GR" is not optional: it is what quantum mechanics does to Einstein's theory. The EFT is even predictive enough to give unambiguous quantum corrections, e.g. to the Newtonian potential ([Donoghue (1994)](https://arxiv.org/abs/gr-qc/9405057), [Burgess (2004)](https://arxiv.org/abs/gr-qc/0311082)). What the EFT cannot do is tell us what happens *at* $M_{\rm Pl}$ — that is the domain of string theory, asymptotic safety, loop quantum gravity, causal sets, and so on.

**These quantum perturbations are fantastic: they behave as higher order terms in the Lagrangian and very often as new effective scalar fields which might have a cosmological impact and explain for example inflation and dark energy!!!!** Since the corrections are suppressed by $E/M_{\rm Pl}$, the natural place to look for them is the **strong-field, high-curvature regime** — black hole mergers, the ringdown, the very early Universe — which is exactly the regime that gravitational-wave astronomy and early cosmology has just opened. This is why the three motivations stated above, philosophical, empirical and theoretical, are somehow converging.

**A third part of this lecture, still being written, will be dedicated to quantum gravity**

As a summary:
- we cannot test it without alternatives,
- the dark sector is a mystery that is tempting but hard to explain with modifications of GR
- there are $\sim 3$–$5\sigma$ cracks in $\Lambda$CDM whose resolution may or may not involve gravity. If further confirmed, this will be very exciting!
- Quantum mechanics *guarantees* that GR is not the final answer. 

The rest of this course is about how to modify it in a controlled way — which is exactly what the [no-go theorems](./Lovelock_thm.md) tells us how to do.