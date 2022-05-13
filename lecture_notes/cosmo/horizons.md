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
d_H = a\chi = \frac{c}{H}
$$

## Particle horizon

The particle horizon is the answer to the question :  What is the maximum distance of the object that emit light that we receive today?

If a photon is emitted at the first moment of the universe $t = 0$ the distance it has travel is:
$$
\chi_p = c \int_{0}^{t_0} \frac{dt}{a(t)}
$$


This distance is sometimes called *conformal time* $\eta$

In terms of proper distance we can write
$$
d_p = a\chi_p
$$

## Event horizon

The event horizon answer to the question : If we send a photon today what is the maximum distance it can reach until the end of the Universe?

It's pretty same as for the particle horizon but this time we emitting the photon today $t_0$ and we let it travel until $t = +\infty$
$$
\chi_{evt} = c\int_{t_0}^{+\infty} \frac{dt}{a(t)}
$$
Note that as we cannot reach something behind the event horizon, we cannot see what is emmited today behind it.

