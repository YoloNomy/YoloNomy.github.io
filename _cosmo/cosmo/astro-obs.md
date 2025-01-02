---
layout: default
title: Observing the stars
parent: cosmo
nav_order: 1
---

# Observing the stars

![image](../images/potw1631a.jpg){: width="80%"}

*The NGC 4833 globular cluster as seen by Hubble. Credit: [ESA/Hubble and NASA](https://esahubble.org/images/potw1631a/)*

Picture a clear night sky in the countryside. Stars appear as a myriad of shining points covering the whole sky. How could they be distinguished?
Sure, they are not all located at the same point of the sky, but that does not tell us anything about their physical properties. What else?

One obvious characteristic comes to mind: their brightness! Indeed, all the stars do not appear as bright. Now what can the brightness of a star teach us? If a star is very bright, it can be for two reasons: either it is intrinsically very bright, because it is big and/or powerful, or because it is very close to us. The brightness of stars thus contain entangled information about both their luminosity and their distance.

Another property distinguishes the stars: their color. Indeed, even if it's not always easy to see, stars do not have the same colors. With a careful eye, it is possible to note that some appear as red, some blue and some more yellow. Now what could this possibly tell us? It turns out that the color of a star is directly related to its temperature, as we will further discuss below.

These two measurable characteristics of stars are fundamental, as temperature and brightness can be ultimately linked with two physical properties of a star: its mass and the stage of its evolution.

## Colors: Temperatures

![image](../images/blackbody.png){: width="80%"}

*Black-body spectra for some specific stars and illustration of Wien's law. Generated with this [python code](../codes/blackbody.py).*

Assuming that the star is in thermal equilibrium, it should radiate as a blackbody. We derived this law in the lecture of statistical mechanics, but for now it can also be assumed as an experimental fact. The blackbody law of emission is written as

$$B_\nu(T)= \frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{k_bT}}-1}$$

where $B_\nu$ is the energy radiated by the star per unit of surface of the body, per unit time, per solid angle and per frequency $\nu$. $T$ is the temperature of the radiating body, which in our case corresponds to the surface temperature of the star. $h$, $k_b$ and $c$ are respectively Planck and Boltzmann's constants and the speed of light in vacuum.

The radiation of a star is thus closely linked to the temperature of its surface. It is thus possible to infer the surface temperature of a star from its "color" i.e. from its spectrum.
From the blackbody law, it is possible to obtain 

$$T = \frac{\nu_{\text{max}}}{b},$$

where $\nu_{\text{max}}$ is the frequency at which the star emits the most energy and $b\simeq 0.0588$ THz.K$^{-1}$ is known as Wien's constant. This relation is known as "Wien's displacement law". As such, the redder is a star, the colder it is and the bluer is a star the hotter it is.

<details>
  <summary>Proof</summary>

To find the maximum $\nu_{\text{max}}$ of the blackbody law $B_\nu$, we need to compute its derivative with respect to $\nu$ and set this derivative equal to zero, that is, we must solve

$$\frac{\text{d} B_\nu(T)}{\text{d}\nu}=0$$

Since

$$\frac{\text{d} }{\text{d}\nu}\left(\frac{2h\nu^3}{c^2}\right)= \frac{6h\nu^2}{c^2}$$

and 

$$\frac{\text{d}}{\text{d}\nu}\left(\frac{1}{e^{\frac{h\nu}{k_bT}}-1}\right)=\frac{h}{k_bT}\frac{e^{\frac{h\nu}{k_bT}}}{\left(e^{\frac{h\nu}{k_bT}}-1\right)^2} $$

Using the product rule, one finds that

$$\frac{\text{d} B_\nu(T)}{\text{d}\nu}= \frac{2h}{c^3}\left(\frac{3\nu^2}{e^{\frac{h\nu}{k_bT}}-1} - \frac{h\nu^3}{k_bT}\frac{e^{\frac{h\nu}{k_bT}}}{\left(e^{\frac{h\nu}{k_bT}}-1\right)^2}\right)$$

Writing $x=\frac{h\nu}{k_bT}$ and setting this equation to zero, one obtains

$$ 3(e^{x}-1)-xe^x=0 $$

This equation is tricky to solve and requires to use the involved concept of "Lambert's W-functions" noted $W_0(z)$ (for the principal mode).

$$\frac{h\nu_{\rm max}}{k_bT}=3+ W_0(-3e^{-3})$$

Thankfully, this can be computed numerically using scipy's function "lambertw".

</details>

In the above figure, we have computed the blackbody spectrum of different iconic stars. You can easily spot some of these stars in the night sky, with the help of softwares as [Stellarium](https://stellarium.org). We can clearly see that, the hotter the star, the more energy it emits (i.e. the bigger the peak of the curve). Furthermore, the hotter the star, the more blue its spectra is i.e. the more it is shifted to the right in frequency space (remember that higher frequencies mean shorter wavelengths). This figure allow us to verify the validity of Wien's law. We also note that our Sun is an "average" star, which is not so bright compared to other bluer (and bigger) stars as Rigel.

From the blackbody law, we can also infer a link between the intrinsic luminosity of the star $L$ -- that is the energy the star radiates in space per unit of time -- and its size (radius) $R$ and temperature $T$ as

$$ L = 4\pi R^2\sigma T^4,$$

where 

$$\sigma=\frac{2\pi^5k_B^4}{15h^3c^2}.$$

This is known as the Stefan-Boltzmann law.

<details>
  <summary>Proof</summary>

The total luminosity of the star is the integral of the Boltzmann law over the surface of the star, the total solid angle and the frequency

$$L = \iiint B_\nu(T) \text{d}S\text{d}\Omega\text{d}\nu $$

As $B_\nu$ is only a function of $\nu$, it becomes the product of three integrals

$$L = \int B_\nu(T)\text{d}\nu \int \text{d}S \int \text{d}\Omega $$

Assuming that a star is a sphere, then

$$\int \text{d}S = 4\pi R^2 $$
 
The solid angle integral

$$\int \text{d}\Omega = \pi $$
 
Now we must compute the final (and hardest) integral

$$ \int B_\nu(T)\text{d}\nu =\int \frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{k_bT}}-1} \text{d}\nu$$

Posing $x=\frac{h\nu}{k_b T}$ and thus $\text{d}x=\frac{h}{k_b T}\text{d}\nu$, the integral becomes

$$ \int B_\nu(T)\text{d}\nu = \left(\frac{k_b T}{h}\right)^4\int_0^\infty \frac{x^3}{e^{x}-1} \text{d}x$$

The integral is the Riemann zeta function and can be shown to be equal to $\frac{\pi^4}{15}$.

</details>

## Brightness: Magnitudes

The brightness of a star, as seen in the sky, is called its *apparent magnitude* $m$. It is defined as

$$m = -2.5 \log\left(\frac{F}{F_0}\right)$$

where $F$ is the received flux of the star.

*absolute magnitude* $M$

$$ \mu = M-m$$

## Infering the distances

A star is characterized by its intrinsic luminosity $L$, which is how much energy it is releasing into space per unit of time.

$$ L_d = \frac{L}{4\pi d^2}$$

Hence, as stated earlier, the brightness of a star is indeed linked to its radius, its temperature as well as it's distance to us

$$ L_d = \frac{4\pi R^2 \sigma T^4}{4\pi d^2} + C$$

For distances on larger (cosmological) scales, have a look [here](../distances/).


## The Hertzprung-Russel diagramms

## Going further: recommended readings



