---
layout: default
title: transfer equations
parent: radiation
nav_order: 1
---

### Studying the thermodynamic of radiation 

As discussed in the previous thermodynamic class, radiation is one form of [heat transfer](../thermo/firstprinciple.md). Its fine understanding is however complicated, as it is at the interface of thermodynamics, electromagnetism and atomic physics. Ultimately, our finest understanding of radiation so far requires the machinery of quantum electrodynamics. However, we do not need to go that far yet in order to study the thermal properties of radiation.

In this class, we will take a thermodynamic approach, considering radiation as one way of heat transform, and basing ourselves on our previous understanding of the [blackbody radiation](../statistical/BB.md).

While a bit abstract at first, such understanding of radiation will play a crucial role in our study of astrophysics and cosmology.

### Quantities to study radiation

We will not discuss here in detail the physical nature of radiation. This will be the purpose of the [electromagnetism](../../../EM/EM) class. For this class, we can just assume that radiation is composed of a linear sum of multiple waves, carrying energy with them. These waves propagate through space and can be absorbed or scattered when interacting with material elements.

### Flux and luminosity

Let's start with the simplest definitions!
Consider a source radiating a total energy $E$ at a given time, for example a light bulb, or a star.

The total **luminosity** of this source, is its power, that is the energy it radiates away per unit of time:

$$L = \frac{\text{d} E}{\text{d} t}$$

The **flux** of the source, at a given point in space, is the energy per unit of time and surface, that is

$$F = \frac{\text{d} E}{ \text{d} S \text{d} t}$$

Simply put, consider an infinesitmal surface $\text{d}S$ somewhere in space. $F$ will quantify how much energy of radiation from the source goes through this surface element, per unit of time.

The conservation of energy becomes:

$$F \propto \frac{1}{r^2} $$

For a star:

$$F = \frac{L}{4\pi R^2}$$

$$F = \frac{L}{4\pi d^2}$$

Which allows to estimate the distance of nearby stars. 

### Specific intensity: frequency and solid angles 

$\nu$ the **frequency** of the radiation, in s$^{-1}$. Equivalently, one can consider the **wavelength** $\lambda$ in m. For a monofrequency radiation travelling in a medium, both are related by $\lambda = c/\nu$, where $c$ is the speed of light in the medium.

$\Omega$ the **solid angle**.

$$\int \text{d}\Omega = 4\pi$$

The **specific intensity** (or spectral radiance) $I_\nu$ is the flux per unit of solid angle and frequency.

$$I_\nu = \frac{\text{d}E}{ \text{d}S \text{d}t \text{d}\Omega \text{d}\nu} $$

### Absorption and emission

- **emission coefficient** $j_\nu$ 
- **absorption coefficient** $\alpha_\nu$ 

### Radiative transfer equation

$$\frac{\text{d} I_\nu}{\text{d} s} =  j_\nu - \alpha_\nu I_\nu$$

**Optical depth**

$$\tau_\nu = \int_s \alpha_\nu(s)\text{d}s $$

Atmospheres of planets

Dust in the ISM

Reionisation and $\Lambda$-CDM.

### Thermal radiation

### Further reading

- [Radiative processes in astrophysics - G. B. Rybicki and A.P. Lightman (2004, 2nd ed.) - Wiley-VCH](https://www.bartol.udel.edu/~owocki/phys633/RadProc-RybLightman.pdf)