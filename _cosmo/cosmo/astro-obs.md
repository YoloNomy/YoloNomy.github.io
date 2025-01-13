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

## The blackbody radition

### Colors and temperatures

![image](../images/blackbody.png){: width="80%"}

*Black-body spectra for some specific stars and illustration of Wien's law. Generated with this [python code](../codes/blackbody.py).*

Assuming that the star is in thermal equilibrium, it should radiate as a blackbody. We derived and discussed this law in the lecture of [statistical mechanics](../../_thermo/statistical/BB.md), but for now it can also be assumed as an experimental fact. The blackbody law of emission is written as

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

Thankfully, this can be computed numerically using scipy's function "lambertw". Using this  <a href="../codes/blackbody.py" target="_blank">python code </a> , you can easily obtain the value of $b\simeq 0.0588$ THz.K$^{-1}$ for Wien's constant.

</details>

In the above figure, we have computed the blackbody spectrum of different iconic stars of the winter night sky.  We can clearly see that, the hotter the star, the more energy it emits (i.e. the bigger the peak of the curve). Furthermore, the hotter the star, the more blue its spectra is i.e. the more it is shifted to the right in frequency space (remember that higher frequencies mean shorter wavelengths). This figure allow us to verify the validity of Wien's law. We also note that our Sun is an "average" star, which is not so bright compared to other bluer (and bigger) stars as Rigel. We also find back the colors observable with the naked eye : red for Betelgeuse and Aldebaran and blue for Sirius and Rigel.

### Brightness:  temperature, radius and distance

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


As we said above, a star is characterized by its intrinsic luminosity $L$, which is how much energy it is releasing into space per unit of time.

$$ F = \frac{L}{4\pi d^2}$$

You will recognize here the surface of a sphere $4\pi d^2$, which means that while the radiation of a star is emitted into space, the total energy emitted is diluted -- and equally distributed -- over a sphere of radius $d$ centered on the star.
Hence, as stated earlier, the brightness of a star is indeed linked to its radius, its temperature as well as it's distance to us

$$ F = \frac{\sigma R^2 T^4}{d^2}$$

The distance $d$ here is called the 'luminosity distance'. It can be estimated using the *parallax* method as explained below. In practice this concept can not be used for objects too far from us. For distances on larger (cosmological) scales, have a look [here](../distances/).

So overall, stars are rather simple objects, as their observable properties can be (in first approximation) charaterized by 4 numbers : their temperature $T$, their radius $R$, their luminosity $L$ and their distance $d$.
Let's now see how we can infer these four properties from concrete measurements with telescopes.

**Exercice: try to list all the hypothesis we assumed in order to  describe stars with these four parameters. For each hypothesis, discuss what could be their limits.**
<details>
  <summary>Solution</summary>
  We assumed the following:
  <ul>
  <li>Stars are in <strong>thermal equilibrium</strong>. This assumption is crucial and is required to define the temperature $T$, constant for the whole star and that its radiation behaves as a blackbody. Clearly, the temperature varies inside of stars, moreover, as they are open systems, radiating into space, stars are clearly not in thermal equilibrium. This is even worse fort out-of main sequences/pulsating stars which evolve quickly and are not in hydrostatic equlibrum (see next lectures).  However, stars are more corectly understood to be in local thermal equilbrium, meaning that small regions are in equilibrium with their surroundings. From observation of stars, we know that they radiate largely as  blackbody, which garantees that this assumption is largely verified. Additionaly other features are imposed on there spectra beyond the modified black body (as absorption lines from the stellar atmosphere), but still this will not have any impact on the underlying blackbody assumption.</li> 
  <li>Furthermore, we assumed that stars were <strong>perfect spheres</strong> characterized by a radius $R$. Stars are formed and bounded together by gravitation, which is radially symetric (see next lectures). As such, sphere is indeed the natural shape they are expected to take. However, due to rotation, stars can be flattened at the poles. This effect is small for most stars but can take incredible proportions for some stars. For example, the star Achenar is rotating so fast (75$\%$ of the centrifugal limit), that it present itself as a flatten ellipsoid with the equator being 1.5 larger than the distance joining the poles.</li>

  <li> This one is trickier to see, but in order to define the distance $d$ we assumed that our Universe is an <strong>Euclidian space</strong>, that is: flat, static and obeing Galilean relativity. While this is true for stars close to us, it is not so simple to define a distance for objects further away from us like stars in other Galaxies. This has to be done in the context of General relativity, in which space can be curved and expanding. For this, see our lecture <a href="../distances/" target="_blank">there</a>.</li>
</ul>
</details>


## Observable properties of the stars

### Brightness: Magnitudes

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

### Color indices

Now, trickier question: how to quantify the observed color of a star?

The flux $F$ is dependent on frequency, such that $F=\int_{0}^\infty F_\nu \text{d}\nu$.

The $B-V$ magnitude or **color index**.

$$B-V = m_B - m_V $$

Other color indices exist as $U-B$ or $R-I$ !

| Stars | U-B | B-V|R-I
|----------|:-------------:|------:|
| Sun |  −27 | 4,83 | |
| Sirius |    −1   |   1,43 | |
| Aldebaran | +0,87  | -0,641| 
| Rigel | −0,66 | -0.03 | -0.02|
| Betelgeuse |2,06 | 1,86| 1,28 |

### Distance Parallaxes and standard candles

## From observable quantities to physical properties of stars

$$L = $$

Ballesteros' formula: 

$$ T = 4600 K \left(\frac{1}{0.92(B-V)+1.7}+ \frac{1}{0.92(B-V)+0.62}\right) $$ 

Direct measurements of the radius of a star is very difficult to obtain. However it can be deduced as

$$ R =\sqrt{\frac{L}{4 \pi \sigma T^4}}$$

## The Hertzsprung-Russell diagramms

![image](../images/Hertzsprung-Russell.png){: width="80%"}

*Hertzsprung-Russel diagram using the v.4.1. of [hygdata](http://www.astronexus.com/projects/hyg). Generated with this [python code](../codes/HR-diagramm.py), inspired from this [code](https://github.com/RobertoIA/Hertzsprung-Russell/blob/master/Hertzsprung-Russell.ipynb).*

## Spectral classification

Harvard spectral classification, Morgan-Keenan

- O,B,A,F,G,K,M
- 0,Ia, Iab, II,III,IV,V,VI, VII 

W, S, C, L, T, Y.

| Stars | Spectral type | $T$ [K] | $R/R_{\odot}$ | $L/L_{\odot}$ | $d$ [Ly] |
|----------|:-------------:|------:|
| Sun |  G2V | 5 772 | $R_{\odot}$ = 696 342 km | $L_{\odot}$ 3.846$\times 10^{26}$ W | 1,58$\times 10^{-5}$ | 
| Sirius |  A1V | 9845 | 1,714 | 24,74 | 8,601 |
| Aldebaran | K5III | 3 910 | 45,1 | 518 | 66 |
| Rigel (A) |   B8Ia | $\sim$ 10 000 | 78,9 | 40 000 | 863,|
| Betelgeuse | M1Ia | $\sim$ 3 600 | $\sim$ 1000 | 108 900 | 643|


![image](../images/Hertzsprung-Russell-2.png){: width="80%"}

*Hertzsprung-Russel diagram using the v.4.1. of [hygdata](http://www.astronexus.com/projects/hyg). Generated with this [python code](../codes/HR-diagramm.py), inspired from this [code](https://github.com/RobertoIA/Hertzsprung-Russell/blob/master/Hertzsprung-Russell.ipynb).*


## Going further: recommended readings



