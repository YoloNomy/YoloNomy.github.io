---
layout: default
title: Thermodynamics in an expanding Universe
parent: cosmo
---

# Thermodynamics in an expanding Universe: the content of the cosmos

### The continuity equation

From the local conservation of energy-momentum in a curved space-time $\nabla_\mu T^{\mu}_{\, \,\nu}=0$, one can easily derive the continuity equation 

$$\boxed{\dot{\rho} = -3H(\rho + P)}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

First we recall that, in a comoving frame and for a perfect fluid $T=\text{diag}(-\rho,P,P,P)$.
Furthermore, we showed that, in a flat FLRW metric:

$$
\begin{aligned}
&\Gamma^{0}_{00}=\Gamma^{0}_{0i} = \Gamma^{0}_{i0} = 0, \\
&\Gamma^{0}_{ij} = a \dot{a}\,\delta_{ij}, \\
&\Gamma^{i}_{0j} = \Gamma^{i}_{j0} = \frac{\dot{a}}{a}\,\delta^{i}_{j}.
\end{aligned}
$$

All other components are null. Now recall that the covariant derivative of a rank-(1,1) tensor is:

$$\nabla_\mu T^{\mu}_{\,\,\nu} = \partial_\mu T^{\mu}_{\,\,\nu} + \Gamma^{\alpha}_{\,\,\mu\nu} T^{\mu}_{\,\,\alpha} - \Gamma^{\mu}_{\,\,\mu\alpha} T^{\alpha}_{\,\,\nu} $$

Focusing on the $\nu=0$ component:

$$
\begin{aligned}
\nabla_\mu T^{\mu}_{\,\,0} &= \partial_\mu T^{\mu}_{\,\,\nu} + \Gamma^{\alpha}_{\,\,\mu0} T^{\mu}_{\,\,\alpha} - \Gamma^{\mu}_{\,\,\mu\alpha} T^{\alpha}_{\,\,0}\\
-\partial_0 \rho &= 3 P \frac{\dot{a}}{a}  + 3 \rho \frac{\dot{a}}{a}
\end{aligned}
$$

Setting it to zero as imposed by the conservation law and defining $H= \dot{a}/a$.:

$$\dot{\rho} + 3H(\rho + P)=0$$

</details>

This equation translates how the energy density of a particle specie is getting diluted by the expansion (through $H$).
It is common to introduce an **equation of state** for different particle specie, relating the pressure and the energy density as $P = w\rho$.

$$
\boxed{\dot{\rho} + 3H(1+w)\rho=0}
$$

Considering only one specie in the expanding Universe, this equation can be exactly solved to obtain:

$$\boxed{\rho= \rho_0 a^{-3(1+w)}}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

$$ \begin{aligned}
&\dot{\rho} + 3H(1+w)=0\\
&\frac{\text{d} \rho}{\text{d}t} = -3(1+w)\frac{\text{d}a}{\text{d}t}\rho\\
& \text{d}\ln(\rho) = -3(1+w) \text{d}\ln(a)\\
& \ln(\rho) = -3(1+w)\ln(a) + C\\
& \ln(\rho) = \ln(a^{-3(1+w)}) + C\\
& \rho = e^{C} a^{-3(1+w)}
\end{aligned}
$$

Defining $e^{C}=\rho(a=1)=\rho_0$, we obtain

$$\dot{\rho} + 3H(1+w)\rho=0$$

</details>

- For **matter**, the pressure is vastly negligeable compared to the energy density (which is given by mass $\rho \sim \frac{\text{d} m}{\text{d} V}c^2$). Thus, $w=0$, and $\rho \propto a^{-3}$. The energy density gets diluted with the expansion. 
- For **radiation** or **relativistic species**, we will show below that $w=1/3$. As such $\rho \propto a^{-4}$. There are multiple complementary ways to understand this result. This corresponds to a dilution of the number of particles as $a^{-3}$ with an additional dilution of the wavelength/energy in $a^{-1}$. 
- For a **cosmological constant**, it is possible to show that $w=-1$ and thus $\rho = cst$. The energy of the vacuum never gets diluted.

### Densities and units

In cosmology, it is convenient to introduce the **densities**:

$$\Omega_i = \frac{\rho_{i}(a=1)}{\rho_{\rm crit}}$$

where the **critical density**

$$\rho_{\rm crit}= \frac{3 H_0^2}{8\pi G}$$

quantifies the total density of the Universe content today, if it was perfectly flat.
$H_0$ is today's value of the acceleration of the scale factor $H_0 = \dot{a}(z=0)$. It is expressed in unit of inverse time, like $1/$s. However, it is more common to express it in units of $\text{km}/\text{s}/\text{Mpc}$. We know that its value must be around $70 \text{km}/\text{s}/\text{Mpc}$, meaning that a galaxy located at 1 Mpc from us escapes from us at a velocity of $\sim 70$ km/s and one at two Mpc recedes at 140 km/s. The value of $H_0$ remains poorly known and is source of the strongest tension in cosmology today. It is thus convenient to introduce the unitless parameter $h=H_0/(100 \text{km}/\text{s}/\text{Mpc})$.

$$ \rho_{\rm crit} = 1.878\times 10^{−29} h^2 \text{g}/\text{cm}^3.$$

With $h\simeq 0.674$ (Planck 2018)
$\rho_{\rm crit} \simeq 8.53×10^{−30} \text{g}/\text{cm}^3$, which corresponds to roughly 5 protons per cubic meter — an extraordinarily dilute universe. 

As such, we get from the Friedmann equation the so-called **closure relation**:

$$\sum_i \Omega_i = 1$$

allowing to interpret the $\Omega_i$ as contributions to the total energy budget of the Universe **today** (that is, for $z=0$ and $a=1$).
Again, since $H_0$ is poorly known, it is more convenient to consider the reduced densities $\omega_i =\Omega_i h^2$ which are independent of the value of $H_0$. Thus $\rho_{i,0} =\Omega_i h^2  1.878\times 10^{−29} \text{g}/\text{cm}^3$ or in other words, $\Omega_i h^2$ is the actual physical density of the component $i$, in abstract unit of $1.878\times 10^{−29} \text{g}/\text{cm}^3$.

## Thermodynamics in the expanding Universe

### Particle number density

The number density i.e. the mean number of particle in a state of position $x$ and spatial momentum $p$ in phase space is noted $f(x, p)$. If the content of the universe is homogeneous $f(x,p)=f(p)$. This function can be identified with the $\langle n_{p} \rangle$ in [statistical mechanics](../../../thermo/statistical/fermions_bosons/), where the energy of the state is expressed in terms of its momentum $p$. [Phase space](../../../thermo/statistical/phasespace/) is re-introduced from Fock-space using the semi-classical limit. From this, it is possible to express, $n$ the number density of particles at a point $x$ in space-time as

$$\boxed{n = g \int f(p) \frac{\text{d}^3p}{(2\pi \hbar)^3}.}$$

The factor $1/(2\pi\hbar)^3$ is the semi-classical volume of a cell in phase space. $g$ is the **degeneracy**, quantifying the multiplicity of the energy states.

<details markdown="1">
  <summary><strong>Supplement: from statistical physics to cosmology</strong></summary>

In [statistical mechanics](../../../thermo/statistical/fermions_bosons/), we saw that quantum statistical systems made of identical non-interacting particles were properly described in Fock space. The operator for the number of particles was noted $\hat{\mathcal{N}}$. Furthermore, quantum systems were characterized by occupation number $n_lambda$ of each accessible energy state, labelled by the index $\lambda$. Assuming that we are considering free particles, there energy states can alternatively be labelled by their spatial momenta $p$. Indeed, it will be possible to recover the energy state from $p$ through some form of dispersion relation as $E(p)=\sqrt{p^2+m^2}$. From the partition functions, we were able to express the mean number of particles in a given state, $\langle n_{p}\rangle$.

The mean number of particles of the total system becomes:

$$
\mathcal{N} = \sum_{p} \langle n_{p}\rangle
$$

Here, $p$ labels discrete momentum eigenstates.

We now want to connect this description to the classical phase space description.
To make the problem well-defined, place the system in a box of finite volume $V = L^3$. While this might seems arbitrary, it is the standard way to obtain the semi-classical limit. We will then be able to consider the limit $L\to infty$.

With periodic boundary conditions, each component of the momentum is quantized as:

$$
p_i = \frac{2\pi \hbar}{L} n_i, \quad n_i \in \mathbb{Z}
$$

This is standard in quantum mechanics. For example, a plane wave satisfying $\psi(x_i)=\psi(x_i+L)$, will satisfy $e^{i \hbar p_x x_i}=e^{i \hbar p_x(x_i +L)}$ and hence $p_x L = 2\pi n_x$.

As such, one can imagine the momentum space as a grid, each possible value along an axis separated by a value of $2\pi \hbar/L$. The larger the box will be, the smaller will be the distance between two accessible momenta. A volume of a cell in the momentum space is:

$$
\Omega = \left(\frac{2\pi \hbar}{L}\right)^3 = \frac{(2\pi \hbar)^3}{V}
$$

In other word, considering a large box $\Delta p^3$ of momentum space, it must contains $\Delta p^3/\Omega$ states. Hence, $1/\Omega$ plays the role of a density of quantum state in phase space.
In the large-volume limit, sums become integrals:

$$
\sum_{p} \;\longrightarrow\; \int \frac{\text{d}^3p}{\Omega} = \frac{V}{(2\pi \hbar)^3} \int \text{d}^3p
$$

The division by $\Delta p^3$ counts the number of states contained in the infinitesimal phase space volume $ \text{d}^3p$.

Thus:

$$
\mathcal{N} = \frac{V}{(2\pi \hbar)^3} \int \text{d}^3p \, \langle n_{p}\rangle
$$

If the particle has degeneracy $ g $ (e.g. spin states), include it:

$$
\mathcal{N} = g \, \frac{V}{(2\pi \hbar)^3} \int \text{d}^3p \, \langle n_{p}\rangle
$$

Rewrite $f(p)= \langle n_{p}\rangle$ and define the number density:

$$
n = \frac{\mathcal{N}}{V}
$$

Then:

$$
n = g \int \frac{\text{d}^3p}{(2\pi \hbar)^3} \, f(p)
$$

</details>

From now on, we work in units in which $\hbar=1$.
During the expansion, particles interact with one another, and we can assume that the expansion is slow enough for particles to get thermalized (we will get back on this hypothesis later).
As such, we can further assume that particles in the expanding Universe are in **thermal equilibrium** thus associated with a single temperature $T$. As such, $f(p)$ will be given by an **equilibrium distributions**.
As we saw in the [statistical mechanics class](../../../thermo/statistical/fermions_bosons/), there are two characteristic equilibrium distributions depending on the spin of the particle:

$$
\begin{aligned}
f(p) &= \frac{1}{e^{(E - \mu)/T} - 1} \quad \text{for bosons}, \\
f(p) &= \frac{1}{e^{(E - \mu)/T} + 1} \quad \text{for fermions}.
\end{aligned}
$$

In an expanding universe we use the **physical momentum**:

$$ p^i =P^i/a $$

which is the value of the momentum scaled by the effect of the expansion of the Universe. Using this variable, the expansion preserves the form of the distribution function. 

The **energy density** is simply:

$$\boxed{\rho = g \int f(p) E(p) \frac{\text{d}^3p}{(2\pi)^3}}$$

in which we sum over all momentum space the product of the number of particles with momentum $p$ with the energy associated to this momentum $E(p)$.

The expression for the **pressure** is trickier and reads:

$$\boxed{P = g \int f(p)\frac{p^2}{3E(p)}\frac{\text{d}^3p}{(2\pi)^3}}$$

and expresses the flux of momentum through a surface.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Consider putting a small square box of size $L$ and volume $V$ within the cosmological fluid. The pressure is the force transmitted by the particles on one of the face of the box. We will show that, the pressure associated to particles of momentum $p$ in a box of volume $V$ is:

$$P=\frac{1}{3}\frac{\vec{p}\cdot\vec{v}}{V}$$

Consider first the walls of the box in the $y,z$ plane. Assuming particles arrives with momentum $p_x$ and goes back in the opposite direction with momentum $-p_x$. When a particle hits it, it transfers an average momentum of $\Delta p_x =  p_x - (-p_x)= 2p_x$. The average time between two colisions (the time for the particle to go back and forth in the box) is $\Delta t = 2L/v_x$. So the force is $F_x = \Delta p_x / \Delta t=p_x v_x/L$.

Hence the pressure on that face is

$$P = \frac{F_x}{S} = \frac{p_x v_x/L}{L^2} = \frac{p_x v_x}{V}$$

Now, assuming isotropy, all directions are equivalent such that $\langle \vec{p}\cdot \vec{v} \rangle =\langle p_x v_x \rangle + \langle p_y v_y \rangle+ \langle p_z v_z \rangle = 3\langle p_x v_x \rangle$ and hence, the pressure exerted by the particles on a wall of the box is:

$$P=\frac{1}{3}\frac{\vec{p}\cdot\vec{v}}{V}$$

Now, for a relativistic particle, we better use the relationship:

$$\vec{v}=\frac{\vec{p}}{E}$$

Which, is $\vec{v}/c^2=\vec{p}/E$ when explicating back the $c$ factors.
This expression is true both for massive particles with $\vec{p}= \gamma m \vec{v}$ and $E=\gamma mc^2$, as well as for massless particles with $\|\vec{v}\|= c$ and $E= \|\vec{p}\|c$.

Hence:

$$P = \frac{p^2}{3V}.$$

Now, we can get the total pressure simply by multiplying by all possible particles contained in the box $\mathcal{N}(p)= n(p) V$ and having a momentum $p$:

$$\begin{aligned}
P_{\rm tot} &=  \int P(p)\mathcal{N}(p) \text{d}^3 p\\
&= g \int P(p) f(p) V \frac{\text{d}^3 p}{(2\pi )^3}\\
&= g \int \frac{p^2}{3E^2} \frac{\text{d}^3 p}{(2\pi )^3}
\end{aligned}
$$

We thus see that, no matter what volume $V$ is chosen for the box to study, the expression for the total pressure becomes independent of such choice.

</details>


### The entropy 

In term of $f(p)$, the entropy density takes the rather complicated form:

$$s= -g\int f(p)\ln(f(p))\mp(1\pm f(p))\ln(1\pm f(p)) \frac{\text{d}^3 p}{(2\pi)^3},$$

which generalizes the statistical mechanics formula $S= -\int \rho \ln(\rho)\text{d}\Gamma$. Thanksfully, we will not have to work directly with such a complicated expression, and we present this formula and discuss it in the following supplement only for the curious reader. 

<details markdown="1">
  <summary><strong>Supplement: from statistical entropy to $s$ </strong></summary>


</details>

$s$ can be more simply expressed from the first principle of thermodynamics as:

$$\boxed{s= \frac{\rho + P - \sum_i \mu_i n}{T}}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Starting from the first principle:

$$\text{d}U = -P\text{d}V + T \text{d}S +\sum_i \mu_i  \text{d}\mathcal{N}$$

Dividing by $\text{d}V$:

$$\rho = - P + T s + \sum_i \mu_i n $$

isolating $s$:

$$s = \frac{\rho + P - \sum_i \mu_i n }{T}$$

</details>

Using the continuity equation we can show that $s$ evolves with the expansion as

$$s = \frac{s_0}{a^3}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>


## Application to the different species in the Universe

### Baryons and Dark matter

As we know very well, our universe contains matter composed of particles of the standard model: electrons and quarks. The mass of such matter is mostly dominated by baryons in the form of protons (and neutrons when bounded into atoms). As such, it is standard to name as **baryonic matter** such matter.
From now one, we will use the indices $m$ for matter, $b$ for baryonic matter. Baryonic matter is slow on cosmological scales, and its energy is largely dominated by its mass $m$.

Restoring units, the energy of a relativistic particle is related to its momentum and mass $m$ through the dispersion relation
$E(p)= \sqrt{p^2c^2 + m^2c^4}$. In the limit of a massive and slow (non-relativistic) particle, this expression takes the form $E(p)\simeq \frac{p^2}{2m} + mc^2$. Using this formula in the definition of the number density, we obtain, for slow moving particles:

$$\boxed{n_b = g_b \left(\frac{m T}{2 \pi}\right)^{3/2} e^{\frac{\mu - m}{T_b}}}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

First, as a warm up, we recall that $E(p)= \sqrt{p^2c^2 + m^2c^4} = mc^2 \sqrt{1 + \frac{p^2}{m^2c^2}}$. We then assume that, for a slowly moving particle, most of the energy is contained within its mass, and then $m^2c^2 \gg p^2$, so $p^2/(m^2c^2)\ll 1$. Now, recall that $(1+x)^n \simeq 1 + nx$ at first order if $x\ll 1$. Hence

$$E(p)\simeq mc^2(1 + \frac{p^2}{2m^2c^2})= mc^2 + \frac{p^2}{2m},$$

as claimed above.

Now, the number density is, with all the physical constants displayed:

$$\begin{aligned}
n_b &=  g_b\int f(p)\frac{\text{d}^3p}{(2\pi)^3} \\
&= g_b \int \frac{1}{e^{(\frac{p^2}{2m}+ mc^2 -\mu)/(k_b T_b)}\pm 1}\frac{\text{d}^3p}{(2\pi \hbar)^3}
\end{aligned}$$

We know that the energy of the baryonic matter is dominated by protons and neutrons which are fermions, such that we could focus on the $+1$ solution. However, since $mc^2$ is so large, we can safely assume that the mass energy is much larger than the thermal energy, that is $mc^2 \gg k_b T$ (as long as we are not in the very early universe). Hence, the argument of the exponential and thus the exponential itself must be very large compare to one and, getting back to natural units:

$$\begin{aligned}
n_b &= g_b \int \frac{1}{e^{(\frac{p^2}{2m}+ m -\mu)/ T_b}}\frac{\text{d}^3p}{(2\pi)^3}\\
\end{aligned}$$

</details>

baryon asymmertry and CP violation.

The energy density becomes

$$\boxed{\rho_b = n_b\left(m + \frac{3}{2}T_b\right)}$$

Recongizing the ideal gas energy.

The pressure 

$$\boxed{P_b = n_b T_b}$$

Since $mc^2 \gg k_bT_b$, $P_b\gg \rho_b$. As such $w=0$ for baryonic matter.

$\Omega_b h^2$ $\Omega_b$


Assumption is that dark matter is a form of matter, which is **cold** and **heavy**. As such we assume that $w=0$ even though its nature remain unknown.

$\Omega_{\rm cdm}h^2$, $\Omega_{\rm cdm}$


$\Omega_{m}= \Omega_b+ \Omega_{\rm cdm}$.

### Photons

For photons, we are able to recover classical results known for the blackbody distribution. Photons are characterized by $g=2$, corresponding to their two possible spin states (helicities). As massless particles, their energy is related to their momentum as $E=pc$. Furthermore, if in thermal equilibrium, photons have a zero chemical potential $\mu_\gamma=0$.

First, we can easily find from the definition of $\rho$ and $P$ that, for photons, $w=P/\rho=1/3$. Thus, a universe dominated by a photon contribution grows as $a^{-4}$ from the continuity equation.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

For photons, $E(p)=p$, so $p^2/E(p) = p = E(p)$, hence:

$$\begin{aligned}
P_\gamma &= g_\gamma \int f(p)\frac{p^2}{3E(p)}\frac{\text{d}^3p}{(2\pi)^3}\\
&= g_\gamma \int f(p)\frac{E(p)}{3}\frac{\text{d}^3p}{(2\pi)^3}\\
&= \frac{\rho_\gamma}{3}
\end{aligned}
$$

</details>

Then, we obtain that the number density of photons depends on the third power of the temperature:

$$\boxed{n_\gamma = \frac{2}{\pi^2}\zeta(3) T_\gamma^3}$$


<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

We also get that the energy density is proportional to the fourth of the temperature:

$$\boxed{\rho_\gamma = \frac{\pi^2}{15} T_\gamma^4}$$

also known as the Stefan-Boltzmann's law. Since $\rho \propto a^{-4}$, $T\propto a^{-1}$ when photon dominates the energy budget.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

$$ \rho_\gamma = \frac{g_\gamma T^4}{2\pi^2}\int_0^\infty \frac{x^3}{e^x \pm 1}\text{d}x $$

</details>

From this, we can obtain the entropy of photons:

$$\boxed{s_\gamma =\frac{4\pi^2}{45} T_\gamma^3}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Since $\mu_\gamma=0$:

$$s_\gamma = \frac{P_\gamma+\rho_\gamma}{T_\gamma}$$

Using $w=1/3$:

$$ s_\gamma =\frac{4\rho_\gamma}{3T_\gamma}$$

Reusing the fact that $\rho_\gamma = \pi^2 T_\gamma^4/15$, we get

$$ s_\gamma =\frac{4\pi^2}{45}T_\gamma^3$$

</details>

### Neutrinos

Since neutrinos are highly relativistic, they also have $E\sim pc$, such that $w~1/3$, for the same reasons as for the photons.

$$n_\nu= $$


<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

For neutrinos, we get a similar dependence with temperature

$$\rho_\nu = N_\nu\frac{7}{8}\frac{\pi^2}{15}T_\nu^4 $$

where $N_\nu$ is the number of neutrino generations, $N_\nu=3$.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>


## Decoupling and the effective number of relativistic species

Now all these components are together. Only when all can interact enough to thermalize do we have a single $T=T_b=T_\gamma=T_\nu$ shared by all of them.

The neutrino energy density can be expressed in terms of the photon energy density as

$$\boxed{\rho_\nu = N_\nu \frac{7}{8} \rho_\gamma \left(\frac{T_\nu}{T_\gamma}\right)^4}$$

Now, what should be the difference of temperature between the photons and the neutrinos?

It is possible to show that:

$$\boxed{\left(\frac{T_\nu}{T_\gamma}\right)^4 =  \left(\frac{4}{11}\right)^{\frac{3}{4}}}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>


$$\boxed{N_{eff} = \frac{8}{7}\left(\frac{11}{4}\right)^{\frac{4}{3}} \frac{\rho_\nu}{\rho_\gamma}}$$

### Dark energy 

### Further reading

- S. Dodelson - Modern Cosmology - 2025 (3rd edition)