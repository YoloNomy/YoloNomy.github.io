---
layout: default
title: Cosmological Horizons
parent: cosmo
---

## Horizons in cosmology

An Horizon is a virtual region from which no information can travel. The most familiar exemple is given by the event horizons of black holes, from which not even light can espace (if you want to know more about them, go check the Black holes page).

However, black holes are not the only objects to display such a feature ... the whole universe is! Intuitively, the Hubble-Lemaître law ($v = H_0d$) implies that the speed at which objects are pulled away from us due to expansion increase with their distance. One can then naturally ask the question : what happens when this speed becomes greater than the speed of light? In some sense, this horizon, works like a 'reversed black hole'. This even leads some physicists to assert that "we live in a black hole"! We'll come back to this ...

For horizons at the scale of the universe, we talk about cosmological horizons, and they can be of different kinds. Instead of being localized in a region of space time, like for black holes, we will see that cosmological horizons are defined relatively to an observer.

When we discussed in evolutions of the universe page, we saw that one of the building principles of cosmology is to assume that the universe is homogeneous and isotropic on large scales. This will also be our starting point. From this assumption, one can find the metric i.e. the way to measure distance in a given frame, satisfying the Einstein's equation for the universe.
The most general result is given by the *Friedmann-Lemaître-Robertson-Walker (FLRW) metric*:

$$
\text{d}s^2 = -c^2\text{d}t^2 + a(t)^2\left( \frac{\text{d}r^2}{1 - kr^2}  + r^2\text{d}\Omega^2\right) 
$$

This is in the comoving frame $(t,r,\theta,\varphi)$ expanding with the expansion. $\text{d}\Omega^2 = r^2\sin\theta^2 \text{d}\varphi^2$ is the spherical infinetisimal surface element. $a(t)$ is called the *scale factor* and quantify the expansion of the universe and of the coordinate system (i.e. objects always keep the same comoving coordinates but the physical distance between them evolves with $a(t)$.)). $k$ is the *spatial curvature* of the universe.
For practical purposes, the whole metric can be rewritten as:

$$
\text{d}s^2 = -c^2\text{d}t^2 + a(t)^2\left(\text{d}\chi^2 + S_k^2(r) \text{d}\Omega^2\right), 
$$

where

$$
S_k(r) =R_0 \left\{\begin{matrix}\frac{\chi}{R_0} \text{ if } k = 0\\
                 \sin\left(\frac{\chi}{R_0}\right) \text{ if } k = 1\\
                  \sinh\left(\frac{\chi}{R_0}\right) \text{ if } k = -1\\
            \end{matrix}\right. 
$$

$\chi$ is called the *comoving distance*. One can then recover the physical space distance $\ell$ by integration of $\text{d}\ell = \sqrt{a^2(t)\text{d}\chi^2 + S_k^2(r) \text{d}\Omega^2} $.
If $k=0$ then $\chi = r$. 

Using this metric, we will be able to define three different types of horizons on cosmological scales: the Hubble, particle and even horizons. Understanding the difference between them is quite subtle, hang on!

## The Hubble Horizon

The *Hubble Horizon* is the most known and easily understandable type cosmological horizon. It is actually the one we discussed in introduction, describing the distance at which galaxies recessed at the speed of light. To every point of the universe one can associate a surface, also called the *Hubble sphere*, delimited by this horizon. Beyond this horizon, it is de facto impossible to receive any signal and thus observe any galaxy. In a sense, it defines the size of what is commonly called the *observable universe*.

As we discussed already, the physical distance from the origin (say earth) to a galaxy is given by:

$$
d = a(t)\chi 
$$

The recession velocity is given by its time derivative (which gives us  the Hubble-Lemaître law)

$$
v = \frac{\text{d}d}{\mathrm{dt}} = \dot{a}\chi = aH\chi
$$

Where $H := \dot{a}/a$ is the *Hubble parameter*.
From this, we deduce that the velocity reaches $v = c$ at the distance of:

$$
d_H(t) = a(t)\chi = \frac{c}{H}
$$

This defines the radius of the Hubble sphere around earth.

## Particle horizon

The particle horizon around a given point is the surface answering the question:  What is the maximum distance of the object that emits light that we can still receive today despite the expansion? 

Before understanding what we really mean, let's first cover how to calculate the distance travelled by light in a given time.

The maximal speed at which information can be carried is indeed the speed of light. By definition, light has the physical speed $c = \text{d}\ell/\text{d}t$ (This condition is equivalent to ask for $\text{d}s^2=0$).

Choosing our coordinate system such that the photons only travel on the radial coordinate, this allows us to write:
$$
cdt = \pm a(t) \text{d}\chi 
$$
(the two solutions comes from the square root) and the co-moving distance $\chi$ between a source that the photon leave at $t_0$ and an observer that receive it at $t_1$ is given by:
$$
\chi = c \int_{t_0}^{t_1} \frac{\text{d}t}{a(t)} 
$$

If a photon is emitted at primordial singularity, $t = 0$ the maximal distance it has then been able to travel is:

$$
\chi_p(t) = c \int_{0}^{t} \frac{\text{d}t'}{a(t')} 
$$

When setting $c=1$, this distance can be identified with a time usually called *conformal time* $\eta$ (formally $\text{d}t = a \text{d}\eta$).

In terms of proper distance we can write 

$$
d_p(t) = a(t)\chi_p(t)
$$

Receiving some signals from earth, no light can have been emitted from further away than this physical distance $d_p(t)$. This gives us the radius of the particle horizon which, in principle is different from the Hubble horizon.

## Event horizon

This time, we will ask ourselves the following question: If we send a photon today what is the maximum distance it can reach until the end of the Universe?

Even if the universe is eternal, this question can surprinsingly have a finite answer due to the expansion. However, it can also diverge and be infinite.
In some sense, the event horizon is a "reversed" particle horizon but this time the photon is emitted today $t_0$ on earth and we let it travel until $t_f \to +\infty$. Contrary to the two other kinds, this horizon does not set a limit on how far we can receive informations from, but on how far we can send informations to.

From previous considerations it is now straightforward to calculate it's conformal radius as:

$$
\chi_{evt}(t) = c\int_{t}^{+\infty} \frac{\text{d}t'}{a(t')} 
$$

From which we calculate the physical distance

$$
d_{evt}(t) = a(t)\chi_{evt}(t)
$$

Note that as we our light will never reach something behind the event horizon, we will never be able to see what is emitted today behind it. In that sense it is similmar to the other two we presented.

## The $\Lambda$-CMD case

In order to predict the evolution of the horizons through the history of the universe, we need to find a way to predict $a(t)$. In order to do so, you need to find invoque the fundamental equation of cosmology, called the Friedmann-Lemaître equation, that we will consider in the following form:

$$ \frac{H^2}{H_0^2} = \sum_i \Omega_i a^{-3(1+w_i)}$$

Where $w_i$ are the coefficients of the equations of states.
Considering the $\Lambda$CDM cosmology using Planck parameters, the evolution of the horizons are given by:    

![my image](../images/LCDMhorizons.png "my image") 


We can give a value for today horizons : in present time the particle is at ~ 48 Glyrs, the event horizon is at ~ 17 Glyrs and the Hubble horizon is at ~ 14 Glyrs.

Looking at the particle horizon we can see that due to expansion it's distance increase rapdily, it means that the farthest light we can see was emits by objects that are today at 48 Glyrs of us! In our expansing universe the particle horizon will diverge towards infinity.

Another remark is that the event horizon is greater than the Hubble distance : photons that lie between the two are currently receeding at supra-light speed but we will finally saw them as they will enter in the Hubble horizon! 

We can prove that the Hubble horizon and the event horizon converge to the same limit:
the Friedmann equations give us 

$$
\frac{\dot{a}}{a} = H(a) = H_0\sqrt{\Omega_m a^{-3} + \Omega_\Lambda}
$$

Then when $a \rightarrow +\infty$ we have $H \rightarrow \sqrt{\Omega_\Lambda}$

We can solve the differential equation of $a(t)$ in the limit when $t \rightarrow +\infty$ :

$$
a(t) = e^{\sqrt{\Omega_\Lambda} t}
$$

With this solution for $a(t)$ we can compute the limit of the event horizon :

$$
d_{evt} \sim a(t) c\int_t^{+\infty} e^{-\sqrt{\Omega_\Lambda} t}
$$

That give us :

$$
d_{evt} \sim a(t) \frac{1}{a(t) \sqrt{\Omega_\Lambda}} = \frac{c}{H} 
$$

That is the definition of the Hubble radius!

Something that can be strange is that our future light-cone seems to cross the event horizon : How can it be possible to interact with what is beyond? 

What we have to remember is that if we emit a photon at a time t it will never reach object that lay at the event horizon at the same time t because the proper distance of these objects will evolve during the photon travel du to the universe expansion !
