---
layout: default
title: Distances
parent: cosmo
nav_order: 1
---

# What is a distance?
Distance measurements are one of the most important probes in cosmology. Distances are directly linked to the geometry of space time through Einstein's equations and thus, measuring them allow to learn about the Universe geometry and components. However the definition of the distance on cosmological scales is not nique. Here we will define the different distances that are used in cosmology. 

# Distances in the (very) local Universe
Paralaxes.


# Few reminders
Here we will use the FLRW metric under the form

$$ds^2 = -dt^2 + a^2(t)\left\{d\chi^2 + S_k^2(\chi)\left(d\theta^2 + \sin^2\theta d\phi^2\right)\right\},$$

where $S_k(\chi)$ is a function that depends on the intrinsic curvature $k$ of our Universe

$$
S_k(\chi) =
  \left\{
    \begin{matrix}
        R_0\sin\left(\frac{\chi}{R_0}\right) &\text{k>0} \ \mathrm{(closed \ universe)}\\

        \chi &\text{k=0} \ \mathrm{(flat \ universe)}\\

        R_0\sinh\left(\frac{\chi}{R_0}\right) &\text{k<0} \ \mathrm{(open \ universe)}
    \end{matrix}.
\right.
$$

We remind the relation between the Hubble parameter $H$ and the scale factor $a$ (see [Friedmann equations](../friedmann))

$$
    H = \frac{\dot{a}}{a},
$$

and the relation between the scale factor $a$ and the redshift $z$

$$
    a = \frac{1}{1 + z}.
$$

# The (line of sight) comoving distance

The comoving distance correspond to the distance between two objects if we could freeze the universe expansion today. It is equivalent to the distance between two events $A$ and $B$ in the frame where they occurs at the same time. The comoving distance could be computed as the variation along the path of a photon (a null geodesic) emitted at $t_e$ and receive by us at $t_0$. From the FLRW metric, for a null geodesic we get the relation

$$
    d\chi = -\frac{dt}{a}.
$$

We change the $t$ variable to $a$ by using $dt = \frac{da}{aH}$ to get the integral

$$
    \chi(a) = - \int_{a}^{1} \frac{da'}{a'^2 H(a)} =  \int_{1}^{a} \frac{da'}{a'^2 H(a')},
$$

where $a(t_e)\equiv a$ and $a(t_0) \equiv 1$. We generally prefer to express the distance in terms of redshift. By using the relation $da = -a^2dz$ one could obtain

$$
    \chi(z) = \int_{0}^{z} \frac{dz'}{H(z')}.
$$

# The transverse comoving distance
The transverse comoving distance $D_A$ is define such that the distance $D_\perp$ measured today (at $a=1$) between two objects at the same comoving distance $\chi$ and separate by an infinitessimal angle $\delta\alpha$ is given by $D_\perp = D_A \delta\alpha$. From the FLRW metric we could see that it correspond to the case where $dt=0$, $d\chi=0$ and $a=1$. By identifying $D_\perp \equiv ds$ and $\delta\alpha \equiv \sqrt{d\theta^2 + \sin^2\theta d\phi^2}$ we are left with the expression for the transverse comoving distance

$$
    D_A(z) = S_k(\chi(z)).
$$

For a flat Universe the transverse and the line of sight comoving distances are equals.
 