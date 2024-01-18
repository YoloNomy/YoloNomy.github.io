---
layout: default
title: Stars, formation 
parent: cosmo
nav_order: 1
---

# The birth of stars 


By trying to answer the vast question "what is a star?", we will apply most of the things we have learn in our physics classes in an exciting context. We will hence discover one of the multiple reasons why astrophysics is so exciting : it involves many different branches of physics and put them in a cosmic perspective! If you don't master yet all of the concepts here, but are excited about astrophysics, you can still try to follow these notes. Hopefully, it should give you motivation to dig deeper the other classes. 


## Jeans mass

<!-- ![image](../images/Tarantula-HST-ESO-Webb-LL.jpg){: width="80%"} -->
![image](../images/tarantula-wst.jpg){: width="80%"}

*The Tarantula nebula in the large Magellanic cloud provides a good exemple of molecular cloud in which we can witness clusters of newborn stars ionizing the gas around them with their light. Credit: [NASA, ESA, CSA, and STScI](https://esawebb.org/images/weic2212a/)*

<!-- HST, ESO and JWST data processed by [Robert Gendler](https://apod.nasa.gov/apod/ap220916.html). -->

Stars form inside large clouds called molecular clouds. These clouds are gigantic, cold ($10\geq T \geq 50$ K) and relatively dense for astrophysical standards ($10^2-10^3$ atoms/cm$^{3}$). They can reach a radius of $\sim 100$ pc and a mass of $10^5$ $M_\odot$, where $M_\odot$ is the mass of the Sun. One parsec (pc) is worth 3.26 light years. For comparison our whole solar system is around 15 pc in radius.

The formation of stars occurs in these clouds when gravitational energy becomes greater than the thermal energy, inducing a collapse of the cloud on itself due to gravity.

This condition can be written as $E_T+V\leq 0$, that is

$$-V\geq E_T$$

traducing that the negative contribution of the gravitational potential energy $V$ overcomes the contribution of the thermal energy $E_T$, which would make the sphere expand.

Let us roughly estimate when this condition is met in a cloud. Assuming that the cloud is an homogenous sphere, its total gravitational energy can be expressed as:

$$V = -\frac{3}{5}\frac{GM^2}{R} $$

You can recognize here the $GM^2/R$ contribution from Newtonian mechanics (link), which is the energy of gravitation of two masses $M$ separated by a distance $R$. The factor of $3/5$ asks for a bit of extra work. The proof is detailed below, but if you don't want to face the trouble, you can just assume it for now.

<details>
  <summary>Proof</summary>

The trick is to write the total potential of the sphere as the integral

$$ V = -\int_0^M \frac{G m(r)}{r}{\rm d}m $$

which sums all the contributions between a sphere of mass $m(r)$ (and $r<R$) and a thin shell of mass ${\rm d}m$ located between $r$ and $r+{\rm d}r$.

The infinitesimal mass can then be expressed as

$${\rm d}m = \rho {\rm d}\mathcal{V}=4\pi \rho r^2 {\rm d}r $$

where $\mathcal{V}=4\pi r^3/3$ is the volume of the sphere of mass $m(r)$ and ${\rm d}\mathcal{V}$ is the volume of the shell between $r$ and $r+{\rm d}r$, given by the differential ${\rm d}\mathcal{V}=(\partial \mathcal{V}/\partial r) {\rm d}r$. We will assume here and in the rest of the derivation that the gas is homogeneous, that is $\rho={\rm cst}$. This is of course a simplifying hypothesis, and we could have derived something more fancy using a $rho(r)$ function.
Inserting the expression of ${\rm d}m$ in the equation for $V$, we get

$$ V = -\int_0^R 4\pi\frac{G m(r)}{r}\rho r^2{\rm dr} $$


$$ V = -\int_0^R 4\pi G m(r)r\rho{\rm dr} $$

Now we can also express $\rho=\frac{m(r)}{4\pi r^3/3}$ (which is has the same value regardless of $r$, under the assumption of homogeneity) and thus $m(r)=\frac{4}{3}\rho \pi r^3$. Inserting this in $V$, we have

$$ V = - \frac{16\pi^2}{3}\int_0^R G \rho^2 r^{4}{\rm d}r $$

$$ V= - \frac{16\pi^2}{3}G\rho^2 \frac{R^5}{5}$$

Now using again $\rho= 3M/(4\pi R^3)$ and hence $\rho^2=9M/(16\pi^2R^6)$, we have as desired

$$ V=  -\frac{3}{5}\frac{GM^2}{R}$$

</details>

The thermal energy, can be understood as the kinetic energy due to the constituant of the gas. It can be shown that, for a monoatomic ideal gas, the mean kinetic energy per particle is given by $\langle mv^2/2 \rangle = 3k_B T/2$, where $k_B$ is the Boltzmann constant, allowing to translate temperatures into energy. If you do not know this formula, you can also take it for granted for now. The total thermal energy of our sphere of gas is then given by

$$E_T = N\frac{3 k_B T}{2}= \frac{M}{\mu}\frac{3k_B T}{2}$$

where $N=M/\mu$ is the total number of particles in the sphere of gas and $\mu$ is the mean mass of an atom in the cloud.

Using the two formulas above, our condition for gravitational collapse becomes

$$\frac{3}{5}\frac{GM^2}{R} \geq \frac{3 k_B T}{2} \frac{M}{\mu}$$

Of course, the formulas used here are approximations of what is really happening in real conditions[^1], but they will give us pretty good understanding of what is really going on.

[^1]: Overall, we assume here that the cloud is spherical and homogeneous and that no exterior force acts on it. We further assume that it is made of monoatomic gas at a constant temperature $T$ and furthermore that the cloud is not rotating and not magnetized. Indeed this is a lot of assumptions! Reality is much more complex (as we discuss later on) but the computations become quickly unbearable and better suited for computers!

Isolating the mass in this expression, we are able to find the limit mass $M_J$, called the *Jeans mass*, at which the cloud will start to collapse under its own gravity. The condition for collapse hence becomes

$$M \geq M_{J}$$

with

$$M_J \propto \left(\frac{T}{\mu}\right)^{3/2}\frac{1}{\sqrt{\rho}}$$

<details>
  <summary>Proof</summary>

Starting from the inequality 

$$\frac{3}{5}\frac{GM^2}{R} \geq \frac{3k_B T}{2} \frac{M}{\mu}$$

We can simply isolate $M$ as

$$M^2 \geq  \frac{5k_B T}{2} \frac{RM}{G\mu}$$

$$M \geq \frac{5k_B T}{2}\frac{R}{G\mu}$$

Now consider the density 

$$ \rho = \frac{M}{V}= \frac{3M}{4\pi R^3}$$  

such that the radius is

$$ 1/R^3 = \frac{4 \pi \rho}{3M} \Rightarrow R = \left(\frac{3M}{4 \pi \rho}\right)^{1/3} $$

Puting this in the above equation on $M$ and brute forcing our way through the equations, we obtain

$$M \geq \frac{(3M)^{1/3} 5k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M^{2/3} \geq \frac{5(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M \geq \left(5\frac{(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}\right)^{3/2}$$

$$ M\geq \frac{5^{3/2}(3)^{1/2} (k_B T)^{3/2}}{2^{3/2}(4\pi \rho)^{1/2}(G\mu)^{3/2}}$$

$$ M\geq \left(\frac{5k_B}{2G}\right)^{3/2}\sqrt{\frac{3}{4\pi}} \left(\frac{T}{\mu}\right)^{3/2}\frac{1}{\sqrt{\rho}}=M_J$$

which is the result given above.
</details>

Hence, the hotter the gas, the higher the mass required for collapse, and the denser the gas, the smaller the mass.

Assuming the gas is molecular hydrogen ($\mu=m_p$) and computing the factors (using $\rho = n m_p$), we get

$$ M_J \sim 6 \times 10^{4}\sqrt{\frac{T^3}{n}} M_{\odot}$$

where $n$ is the density of hydrogen atoms. We hence see something exciting here: a cascading effect is hidden in this formula. When the cloud will start contracting, its density $n$ will automatically increase, leading $M_J$ to decrease. Hence the cloud will fragment itself in smaller clouds, over and over again during the gravitational collapse. This collapsing is also due to the increasing rotation speed of the collapsing cloud. 

Indeed, to keep things simple and hand waving for now, consider the angular momentum $\vec{L}$ of a particle rotating at the edge of the collapsing cloud. We saw in the classical mecanics class that it was given by $\vec{L}=r\wedge m\vec{v}$ and that it was conserved if we consider only the gravitational force. Now, as the cloud contracts after having overpassed Jean's mass, the radius $r$ will decrease. In order for $\vec{L}$ to be conserved when $r$ decreases, $\vec{v}$ must increase. At some point, the speed will then be large enough to thorn apart the cloud in smaller patches (a proper account of this would have been to use the moment of inertia of the cloud, treating it as a solid sphere).

This all explains why the stars are born in clusters of thousands of stars inside large clouds instead of obtaining a single large star. After some time, all these stars are separated and spread apart in the Galaxy along their rotation around the Galactic center.

## Closer to reality: turbulence and magnetic fields

![image](../images/pillarsofcreation.jpg){: width="53.5%"}![image](../images/orion.jpg){: width="45%"}

*Left: The iconic "Pillars of Creation" nebula as seen by the JWST. It provides another caracteristic example of star forming region within a nebular cloud. Credit: [NASA, ESA, CSA, and STScI](https://esawebb.org/images/pillarsofcreation_composite/). Right: Portio of the Orion nebula. In both images, notice the complex patern made by the interstellar medium. Credit: [ESA/Webb, NASA, CSA, PDRs4All ERS Team](https://esawebb.org/images/weic2315b/)*

$$ t_f = \sqrt{\frac{3\pi}{32 G \rho}} $$

<details>
  <summary>Proof</summary>

</details>

free fall time and turbulence magnetic field and structure formation

fractal filaments, clumps

# Going further: recommanded readings

- An introduction to Star Formation - D. Ward-Thompson and A. P. Whitworth - Cambdrige University Press - 2011
- Stellar Structure and Evolution -  R. Kippenhahn, A. Weigert - Spriner - 1996
