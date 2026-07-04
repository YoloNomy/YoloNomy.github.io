---
layout: default
title: Spectral distortions
parent: cosmo
nav_order: 1
---


# Preliminaries

## Photon number, phase space distribution and intensity

As we saw in our lecture on the [thermodynamics in an expanding universe](./thermo_cosmo.md), the different species in the Universe are described by a **distribution function** $f(q,p,t)$, which quantifies the probability to observe a particle at position $q$, time $t$ and with momentum $p$. A key to understand the thermal history of our Universe is thus to find how to express $f$ for each species, and describe how it might evolve with the cosmic time.

We will now focus on the study of what $f$ is, and how it evolves for **light**, that is, for the **photons**. This study is extremely important, as the photon bath which is carried along with the expansion, the **cosmic microwave background** is something we can directly observe with telescopes. While, we never directly observe $f(q,p,t)$, we receive an intensity $I_\nu$ at different electromagnetic frequency $\nu$. To connect the two concepts, we shall recall that, for photons the De-Broglie relation is $p=h/\lambda = h \nu/c$. Hence, we can express $f$ in term of $\nu$ simply as $f(\nu,t)$, if we assume that the universe is homogeneous, we can drop the dependence of $f$ in the position $q$. The intensity is then obtained as

$$\boxed{I_\nu = \frac{2 h\nu^3}{c^2}f(\nu,t_0)}$$

where $t_0$ is the cosmic time at which we observe the photons (i.e. today).

<details markdown="1">
  <summary><strong>Proof</strong></summary>

The intensity is the energy of the photon field per unit frequency, time, unit angle and area:

$$\text{d}E  = I_\nu \cos(\theta)\text{d}t \text{d}A \text{d}\Omega  \text{d}\nu$$

considering light going through an infinitesimal surface $\text{d}A$ with an incident angle $\theta$.

Now, the infinitesimal energy in a volume filled by photons is:

$$\text{d}E =g_s E(p) f(q,p,t)\frac{\text{d}^3q \text{d}^3p}{h^3}$$

To equate $\text{d}E$ with the one used to define intensity, we consider that all the energy contained in the infinetismal volume should go through the surface $\text{d}A$ in a time $\text{d}t$. For this, we should consider a small space element adjacant to surface, such that $\text{d}^3q=\cos(\theta)\text{d}A c\text{d}t$.

For photons, $g_s=2$, $E=pc= h\nu$. The energy density becomes:

$$\text{d}E = 2 h\nu f(q,p,t) \frac{\cos(\theta)\text{d}A c\text{d}t \text{d}^3p}{h^3} $$

In spherical coordinates in momentum space, the momentum is $\text{d}^3p = p^2 \text{d}p \text{d}\Omega$. For photons $p=h\nu/c$ and hence $\text{d}p=h\text{d}\nu/c$, such that 

$$\text{d}^3p = \frac{h^3\nu^2}{c^3}\text{d}\nu\text{d}\Omega. $$

We then have:

$$\text{d}E = 2 h\nu f(q,\nu)\cos(\theta)\text{d}A c\text{d}t\frac{h^3\nu^2}{c^3}\frac{\text{d}\nu\text{d}\Omega}{h^3} = \frac{2 h\nu^3}{c^2}f(q,\nu,t)\text{d}t \text{d}A \text{d}\Omega  \text{d}\nu$$ 

Comparing with the intensity definition, we find that

$$\boxed{I_\nu = \frac{2 h\nu^3}{c^2}f(q,\nu,t)}$$

</details>

For a [black body radiation](../../_thermo/statistical/BB.md),

$$\boxed{f^{BB}(\nu) = B_\nu(T) = \frac{1}{e^{\frac{h\nu}{kT}} - 1}}$$

We saw in our previous lecture on the cosmic microwave background that the CMB light is very close to a blackbody radiation $B_\nu(T_{\rm cmb})$, signature of thermal equilibrium in the primordial plasma. However we can look for small deviations, known as **spectral distortions** to this emission law:

$$\boxed{\Delta I_\nu = I^{\text{cmb}}_\nu -B_\nu(T_{\rm cmb})}$$

which would be the result of a distortion $\Delta f$ of the photon distribution function.

# The Boltzmann equation for photons

We now introduce the unitless frequency $x= p/T = h\nu/T$. This quantity does not depend on the evolution.

Expressing $f(q,p)$ as $f(q,x)$, we get simply:

$$\boxed{\frac{\partial f}{\partial t} = \mathcal{C}}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

$$\frac{\text{d}f}{\text{d}t} = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial x}\frac{\partial x}{\partial t} = \mathcal{C}(f) $$

</details>

For photons in the early Universe:

$$\boxed{\frac{\partial f}{\partial t} = \mathcal{C}^{CS} +  \mathcal{C}^{BR} +  \mathcal{C}^{2\gamma}}$$

## Temperatures

$$T_z = T_0(1+z)$$

$T_\gamma$, $T_e$.

# Three types of spectral distortions


## Temperature shifts

## The Kompanets equation:

The interaction term for the **Compton interaction** is

$$\mathcal{C}^{CS}(x) = \frac{1}{x^2}\frac{\partial}{\partial x}\left(x^4 \left(\frac{\partial f}{\partial x} + f^2+f\right)\right)$$

## $\mu$ distortions

The shape is stable:

$$ \frac{\partial f}{\partial t} \simeq 0 = \mathcal{C}^{CS}$$

But what physical connection with $\mu$ in thermodynamics?

## $y$ distortions

$$ \frac{\partial f}{\partial \tau} \simeq \frac{\Delta f}{\Delta \tau} = \mathcal{C}^{CS}$$


## The $\mu/y$ regime

# Branching ratios and injections


## Further reading:

- [Lucca et al (2020) - The synergy between CMB spectral distortions and anisotropies](https://arxiv.org/pdf/1910.04619)
- [Chluba (2025) - The Cosmic Microwave Background: Spectral Distortions ](https://arxiv.org/pdf/2502.05188)