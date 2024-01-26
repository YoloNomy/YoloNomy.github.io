---
layout: default
title: Observing the stars
parent: cosmo
nav_order: 1
---

# Observing the stars

![image](../images/potw1631a.jpg){: width="80%"}

*The NGC 4833 globular cluster as seen by Hubble. Credit: [ESA/Hubble and NASA](https://esahubble.org/images/potw1631a/)*



Picture a clear night sky in the countryside and think carefully about the stars (exercie: do it!). They appear as a myriad of shining points covering the whole sky. Now, how could you distinguish them from one another?
Sure, they are not all located at the same points of the sky, but that does not tell us much about what is going on up there. What else?

You might come up with this idea: their brightness! Indeed, all the stars are not appearing as bright. Now what can the brightness of a star teach us about it? If a star is very bright, it can be for two reasons: either it is intrinsically very bright, because it is big and/or powerfull, or because it is very close to us. So brightness of stars tells us both about their luminosity and about their distance.

With a bit of experience, you might also come with something else: their colors! Indeed, even if it's not always easy to see, all stars does not have the same colors. Some are pretty reds, some blue and some more yellow. Now what could this possibly tell us? Turns out that the color of a star is directly related to its temperature, as we will further discuss here.

As we will see in the next class, brightness and temperature are ultimately linked with two properties of stars: their masses and how evolved they are.

## Brightness: Magnitudes

## Infering the distances

A star is characterized by its intrinsic luminosity $L$, which is how much energy it is releasing into space per unit of time.

$$ L_d = \frac{L}{4\pi d^2}$$

## Colors: Temperatures

Assuming that the star is at thermal equilbrium, it should radiate as a blackbody. We derived this law in the lecture of statistical mechanics, but once again if you don't know it you can assume it as an experimental fact. It is writen as

$$B_\nu(T)= \frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{k_BT}}-1}$$

where $B_\nu$ is the energy radiated by the star per unit of surface of the body, per unit time, per solid angle and per frequency $\nu$. $T$ is the temperature.

As such, the radiation of a star is closely linked to its temperature (or at least the temperature of its surface). More exactly, we can infer the surface temperature of a star from its color!
From the blackbody law, we can infer that 

$$T = \frac{h\nu_{\text{max}}}{3k_b}$$

Where $\nu_{\text{max}}$ is the frequency at which the star emits the most energy. This is known as "Wien's law". From which we can conclude that, the redder the star, the colder its temperature and the bluer the hotter.

<details>
  <summary>Proof</summary>


*Add a code that proves it graphically*

To find the maximum $\nu_{\text{max}}$ of the blackbody law $B_\nu$, we need to derivate it with respect to $\nu$ and set this derivative equal to zero, that is, we must solve

$$\frac{\text{d} B_\nu(T)}{\text{d}\nu}=0$$

that is

$$\frac{\text{d}}{\text{d}\nu}(\frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{k_BT}}-1})=0$$

</details>

From the blackbody law, we can also infer a link between the intrinsic luminosity of the star $L$ -- that is the energy the star radiates in space per unit of time -- and its size (radius) $R$ and temperature $T$ as

$$ L = 4\pi R^2\sigma T^4,$$

where 

$$\sigma=\frac{2\pi^5k_B^4}{15h^3c^2}.$$

This is known as Stefan's Boltzmann's law.

<details>
  <summary>Proof</summary>

The total luminosity of the star is the integral of the Boltzmann law over the surface of the star, the total solid angle and the frequency

$$L = \int \int B_\nu(T) \text{d}S\text{d}\Omega\text{d}\nu $$

As $B_\nu$ is only a function of $\nu$, it becomes the product of three integrals

$$L = \int \int B_\nu(T)\text{d}\nu \int \text{d}S \int \text{d}\Omega $$

Assuming that a star is a sphere, then

$$\int \text{d}S = 4\pi R^2 $$

</details>



## The Hertzprung-Russel diagramms

## Going further: recommended readings



