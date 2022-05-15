---
layout: post
title: "Cosmological Horizons"
---

## FLRW metric and travel of photons

Here we will talk about cosmological horizons. To do that we need to define distance in the Universe. A common way to measure distance is to look at photon travel path.

Before we can recall the FLRW metric:

$$ 
ds^2 = -dt^2 + a(t)^2\left( \frac{dr^2}{1 - kr^2}  + r^2d\Omega^2\right) 
$$

That can be rewrite as :

$$ 
ds^2 = -c^2dt^2 + a(t)^2\left(d\chi^2 + S_k^2(r) d\Omega^2\right) 
$$

Where

$$ 
S_k(r) =R_0 \left\{\begin{matrix}\frac{\chi}{R_0} \text{ if } k = 0\\
                 \sin\left(\frac{\chi}{R_0}\right) \text{ if } k = 1\\
                  \sinh\left(\frac{\chi}{R_0}\right) \text{ if } k = -1\\
				\end{matrix}\right. 
$$

Since a photon is massless it follow the geodesic with $ds^2 = 0$

So, assuming that our coordinates system is such as the photon only travel on the radial coordinate we have:

$$ 
cdt = \pm a(t) d\chi 
$$

and the co-moving distance between a source that the photon leave at $t_0$ and an observer that receive it at $t_1$ is given by:

$$ 
\chi = c \int_{t_0}^{t_1} \frac{dt}{a(t)} 
$$

## The Hubble Horizon

Maybe the most famous, it describe the distance at which galaxies recessed at the speed of light. The physical distance to a galaxy is given by:

$$ 
d = a(t)\chi 
$$

So the recession velocity is

$$ 
v = \frac{\text{d}d}{\mathrm{dt}} = \dot{a}\chi = aH\chi
$$

If the velocity is $v = c$ the galaxy is at the distance of :

$$ 
d_H(t) = a(t)\chi = \frac{c}{H}
$$

## Particle horizon

The particle horizon is the answer to the question :  What is the maximum distance of the object that emit light that we receive today?

If a photon is emitted at the first moment of the universe $t = 0$ the distance it has travel is:

$$
\chi_p(t) = c \int_{0}^{t} \frac{dt'}{a(t')} 
$$


This distance is sometimes called *conformal time* $\eta$

In terms of proper distance we can write

$$ 
d_p(t) = a(t)\chi_p(t)
$$

## Event horizon

The event horizon answer to the question : If we send a photon today what is the maximum distance it can reach until the end of the Universe?

It's pretty same as for the particle horizon but this time we emitting the photon today $t_0$ and we let it travel until $t_f = +\infty$

$$ 
\chi_{evt}(t) = c\int_{t}^{+\infty} \frac{dt'}{a(t')} 
$$

In proper distance it is

$$
d_{evt}(t) = a(t)\chi_{evt}(t)
$$

Note that as we cannot reach something behind the event horizon, we cannot see what is emitted today behind it.

Another remark is that the event horizon can diverge and be infinite.

## The $\Lambda$CMD case 
Take the example of the $\Lambda$CDM cosmology using Planck parameters.

   ![my image](./images/LCDMhorizons.png)
  
  
We can give a value for today horizons : in present time the particle is at ~ 48 Glyrs, the event horizon is at ~ 17 Glyrs and the Hubble horizon is at ~ 14 Glyrs.

Looking at the particle horizon we can see that due to expansion it's distance increase rapdily, it means that the farthest light we can see was emits by objects that are today at 48 Glyrs of us ! In our expansing universe the particle univers will tend to infinity.

Another remark is that the event horizon is greater than the Hubble distance : photons that lie between the two are currently receeding at supra-light speed but we will finally saw them as they will enter in the Hubble horizon ! 
