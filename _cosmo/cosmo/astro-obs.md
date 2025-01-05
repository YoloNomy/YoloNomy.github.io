---
layout: default
title: Observing the stars
parent: cosmo
nav_order: 1
---

# Observing the stars

![image](../images/stellarium.png){: width="100%"}

*Winter night sky in Europe and its constellations simulated using the [Stellarium](https://stellarium.org) software 
(To reproduce use the following coordinates: Earth (48.8582,2.3387), 2025-01-05 21:45:23 UTC+01:00).*

Picture a clear night sky in the countryside, or even better, have a look outside at night! If you are located in the northern hemisphere in winter, you might be able to see a sky very similar to the one represented in the picture above, with some emblematic constellations as Orion, Canis Major, Gemini and Taurus. Stars appear as a myriad of shining points covering the whole sky. How could they be distinguished?
Sure, they are not all located at the same point of the sky, but that does not tell us anything about their physical properties. What else?

One obvious characteristic comes to mind: their brightness! Indeed, all the stars do not appear as bright. For example, you might notice that Sirius appears as much brighter than all the other stars around. It is actually the brightest star visible from the Northern hemisphere!  Now what can the brightness of a star teach us? If a star is very bright, it can be for two reasons: either it is intrinsically very bright, because it is big and/or powerful, or because it is very close to us. The brightness of stars thus contain entangled information about both their luminosity and their distance.

Another property distinguishes the stars: their color. Indeed, even if it's not always easy to see, stars do not have the same colors. With a careful eye, you will notice that Betelgeuse and Aldebaran are clearly red, while Rigel is light blue. Now how to quantify this color, and what could we possibly infer from it? It turns out that the color of a star is directly related to its temperature, as we will further discuss below.

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

This equation is tricky to solve and requires to use the involved concept of "Lambert's W-functions" noted $W_0(z)$ (for the principal mode). For simplicity, we will admit that the $x$ solving this equation is given by
 
$$\frac{h\nu_{\rm max}}{k_bT}=3+ W_0(-3e^{-3})$$

Thankfully, this can be computed numerically using scipy's function "lambertw". This (check the joined python code) allows us to obtain the value of $b\simeq 0.0588$ THz.K$^{-1}$ for Wien's constant.

</details>

In the above figure, we have computed the blackbody spectrum of different iconic stars of the winter night sky.  We can clearly see that, the hotter the star, the more energy it emits (i.e. the bigger the peak of the curve). Furthermore, the hotter the star, the more blue its spectra is i.e. the more it is shifted to the right in frequency space (remember that higher frequencies mean shorter wavelengths). This figure allow us to verify the validity of Wien's law. We also note that our Sun is an "average" star, which is not so bright compared to other bluer (and bigger) stars as Rigel. We also find back the colors observable with the naked eye : red for Betelgeuse and Aldebaran and blue for Sirius and Rigel.

From the blackbody law, we can also infer a link between the intrinsic luminosity of the star $L$ -- that is the total energy the star radiates in space per unit of time -- and its size (radius) $R$ and temperature $T$ as

$$ L = 4\pi R^2\sigma T^4,$$

where 

$$\sigma=\frac{2\pi^5k_B^4}{15h^3c^2}.$$

This is known as the Stefan-Boltzmann law.

<details>
  <summary>Proof</summary>

The total luminosity of the star is the integral of the Boltzmann law over the surface of the star, the total solid angle and the frequency

$$L = \iiint B_\nu(T) \text{d}S \cos(\theta)\text{d}\Omega\text{d}\nu $$

The additional and perhaps strange $\cos(\theta)$ factor will be explained below.

As $B_\nu$ is only a function of $\nu$, it becomes the product of three integrals

$$L = \int B_\nu(T)\text{d}\nu \int \text{d}S \int \text{d}\Omega $$

Assuming that a star is a sphere, then

$$\int \text{d}S = 4\pi R^2 $$
 
The solid angle integral is 

$$\int \cos(\theta)\text{d}\Omega = \int_0^{2\pi}\int_0^{\pi/2} \cos(\theta) \sin(\theta)\text{d}\varphi \text{d} \theta=\pi $$

It takes this form with an additional $\cos(\theta)$ because of Lambert's cosine law for the blackbody emission, saying that the intensity is smaller when looking the surface at an angle. We will have to admit this law here for simplicity. We integrate only over the half sphere as we are considering here the emission of an infinitesimal element of surface around itself.  
 
Now we must compute the final (and hardest) integral

$$ \int B_\nu(T)\text{d}\nu =\int \frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{k_bT}}-1} \text{d}\nu$$

Posing $x=\frac{h\nu}{k_b T}$ and thus $\text{d}x=\frac{h}{k_b T}\text{d}\nu$, the integral becomes

$$ \int B_\nu(T)\text{d}\nu = \frac{2h}{c^2}\left(\frac{k_b T}{h}\right)^4\int_0^\infty \frac{x^3}{e^{x}-1} \text{d}x$$

The integral is the Riemann zeta function and can be shown to be equal to $\frac{\pi^4}{15}$. We will also admit this last result here.

Combining the three integrals we finally obtain as desired 

$$L =  \frac{2\pi^5k_B^4}{15h^3c^2} 4\pi R^2 T^4$$

</details>

## Distance and luminosity

As we said above, a star is characterized by its intrinsic luminosity $L$, which is how much energy it is releasing into space per unit of time.

$$ F = \frac{L}{4\pi d^2}$$

You will recognize here the surface of a sphere $4\pi d^2$, which means that while the radiation of a star is emitted into space, the total energy emitted is diluted -- and equally distributed -- over a sphere of radius $d$ centered on the star.
Hence, as stated earlier, the brightness of a star is indeed linked to its radius, its temperature as well as it's distance to us

$$ F = \frac{4\pi R^2 \sigma T^4}{4\pi d^2} + C$$

The distance $d$ here is called the 'luminosity distance'. It can be estimated using the *parallax* method. In practice this concept can not be used for objects too far from us. For distances on larger (cosmological) scales, have a look [here](../distances/).

## Brightness: Magnitudes

The brightness of a star, as seen in the sky, is quantified by its *apparent magnitude* $m$. $m$ is a unitless number defined as

$$m = -2.5 \log_{10}\left(F\right) + m_0$$

where $F$ is the received flux of the star that is its luminosity as measured on Earth. $m_0$ is the arbitrary magnitude $0$ which defines the origin of the magnitude system.
The use of a logarithm function here is to match the sensitivity of the human eye.
The brighter the star, the more negative will be $m$.

The *absolute magnitude* $M$ is its apparent magnitude observed at a distance of 10 parsecs, that is

$$M = -2.5 \log_{10}\left(\frac{L}{4\pi (10 \text{ pc})^2}\right) + m_0$$

In the table below, you can find the values of $m$ and $M$ for our iconic stars:

| Stars | apparent magnitude $m$ | absolute magnitude $M$|
|----------|:-------------:|------:|
| Sun |  −27 | 4,83 |
| Sirius |    −1   |   1,43 |
| Aldebaran | +0,87  | -0,641|
| Rigel | 0,12 | -7,84
| Betelgeuse | 0,58 | -5,85 |
| Naked eye limit | 6 |  |
| Hubble telescope limit | 31.5 |  |

We see that the Sun, which is obviously the brightest star visible from Earth (during the day!!!), has a greatly negative magnitude of -27. However, its absolute magnitude is of 4.83, which is rather high, making it the least "absolutely" bright star of the table!

It can also be useful to define the distance modulus, which is the difference between the absolute and apparent magnitude:

$$ \mu = M-m$$

It is a useful quantity as it can be related to the distance as

$$\mu = 5\log_{10}(d/\text{pc}) - 5$$

**Exercice: proove this!**
<details>
  <summary>Solution</summary>

Remember, as always, the usual log properties: $\log_{10}(a^b)=b\log_{10}(a)$, $\log_{10}(a\times b)=\log_{10}(a)+\log_{10}(b)$ and $\log_{10}(a/b)=\log_{10}(a)-\log_{10}(b)$. Note also that $\log_{10}(10)=1$.

From these properties:
$$ \mu = M-m $$
$$ = -2.5 \log_{10}\left(\frac{L}{4\pi d^2}\right) - 2.5 \log_{10}\left(\frac{L}{4\pi (10 \text{ pc})^2}\right)$$
$$= -2.5 \log_{10}\left(\frac{(10 \text{ pc})^2}{d^2}\right) $$
$$= -5 \log_{10}\left(\frac{(10 \text{ pc})}{d}\right) $$
$$= 5 \log_{10}\left(\frac{d}{(10 \text{ pc})}\right) $$
$$5\left( \log_{10}\left(d\right)-\log_{10}\left(10\right) \right) $$
$$5\log_{10}\left(d\right)-5$$

</details>

## Color: B-V

Now, trickier question: how to quantify the observed color of a star?

The flux $F$ is dependent on frequency, such that $F=\int_{0}^\infty F_\nu \text{d}\nu$.

The $B-V$ magnitude.

$$m_B - m_V $$


## The Hertzprung-Russel diagramms

## Going further: recommended readings



