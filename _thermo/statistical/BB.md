---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---


## Radiation pressure and the black-body

Let's consider now a closed box of volume $V$containing a photon gas at equilibrium at temperature $T$. The gas is thermalized by the constant interactions with the electrons of the atoms of the walls and has a continuous spectrum. (this spectrum would then be emitted by the gas if a hole was open in it).

### For photon in equilibrium, $\mu_\gamma=0$

For photons, $\mu_\gamma=0$. This fact is often confusing and misunderstood, so we will try to explain it here with great details.

Multiple different complementary ways to understand this result:

- Photons can be absorbed or emitted by electrons:
$e^{-}+ \gamma \leftrightarrow e^{-}$, which implies $\mu_{e^-} + \mu_\gamma = \mu_\gamma$ and thus:

    $$\mu_\gamma=0$$

- Photon are massless and their number is not conserved as they are constantly absorbed and emmited by the walls of the box.

- $\mu_\gamma$ is how much the energy of the photon gas changes when increasing the number of photons, keeping volume and entropy fixed. The addition of a photon to the energy $\Delta U = \hbar \omega$. $\Delta S = (\hbar \omega)/T$, such that $\mu = \Delta U - T \Delta S = 0$.

- As we will see, the number of photon is entierly given by the temperature. As such, adding a lagrange multiplier for $\mathcal{N}$ would be redudant and bias (or add no information), as it is not independent from the constraint imposed on $U$.

Spectral distortions of the CMB.

### The black-body radiation

$$
\langle \epsilon_\lambda\rangle = \langle n_\lambda\rangle\epsilon_\lambda =  \langle n_\omega \rangle \hbar \omega
$$


$$
g(\omega)= \frac{V}{\pi^2 c^3}\omega^2
$$

$$
u(\omega)= \frac{1}{V}\frac{dE}{d\omega}=\frac{1}{\pi^2c^3}\frac{\hbar \omega^3}{e^{\beta \hbar \omega}-1}
$$

$$
B_\nu(T)= u(\omega)\frac{d\omega}{d\nu}
$$

$$
w=\frac{1}{3}
$$
