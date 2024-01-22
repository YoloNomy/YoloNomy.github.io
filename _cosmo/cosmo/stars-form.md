---
layout: default
title: Stars, formation 
parent: cosmo
nav_order: 1
---

# The birth of stars 


By trying to answer the vast question "what is a star?", we will apply most of the things we have learn in our physics lectures in an exciting context. We will hence discover one of the multiple reasons why astrophysics is so exciting : it involves many different branches of physics and put them in a cosmic perspective! If you don't master yet all of the concepts here, but are excited about astrophysics, you can still try to follow these notes. Hopefully, it should give you motivation to dig deeper the other lectures. 


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

Let us roughly estimate when this condition is met in a cloud. Assuming that the cloud is an homogenous sphere, its total [gravitational energy](../../../meca/Newton/energy/) can be expressed as:

$$\boxed{V = -\frac{3}{5}\frac{GM^2}{R}}$$

You can recognize here the $GM^2/R$ contribution from Newtonian mechanics (link), which is the energy of gravitation of two masses $M$ separated by a distance $R$. The factor of $3/5$ asks for a bit of extra work. The proof is detailed below, but if you don't want to face the trouble, you can just assume it for now.

<details>
  <summary>Proof</summary>

The trick is to write the total potential of the sphere as the integral

$$ V = -\int_0^M \frac{G m(r)}{r}\text{d}m $$

which sums all the contributions between a sphere of mass $m(r)$ (and $r<R$) and a thin shell of mass $\text{d}m$ located between $r$ and $r+\text{d}r$.

The infinitesimal mass can then be expressed as

$$\text{d}m = \rho \text{d}\mathcal{V}=4\pi \rho r^2 \text{d}r $$

where $\mathcal{V}=4\pi r^3/3$ is the volume of the sphere of mass $m(r)$ and $\text{d}\mathcal{V}$ is the volume of the shell between $r$ and $r+\text{d}r$, given by the differential $\text{d}\mathcal{V}=(\partial \mathcal{V}/\partial r) \text{d}r$. We will assume here and in the rest of the derivation that the gas is homogeneous, that is $\rho={\rm cst}$. This is of course a simplifying hypothesis, and we could have derived something more fancy using a $rho(r)$ function.
Inserting the expression of $\text{d}m$ in the equation for $V$, we get (remember that $\int_a^b r^n \text{d}r=[r^{n+1}/n+1]^b_a$)

$$ V = -\int_0^R 4\pi\frac{G m(r)}{r}\rho r^2{\rm dr} $$


$$ V = -\int_0^R 4\pi G m(r)r\rho{\rm dr} $$

Now we can also express $\rho=\frac{m(r)}{4\pi r^3/3}$ (which is has the same value regardless of $r$, under the assumption of homogeneity) and thus $m(r)=\frac{4}{3}\rho \pi r^3$. Inserting this in $V$, we have ()

$$ V = - \frac{16\pi^2}{3}\int_0^R G \rho^2 r^{4}\text{d}r $$

$$ V= - \frac{16\pi^2}{3}G\rho^2 \frac{R^5}{5}$$

Now using again $\rho= 3M/(4\pi R^3)$ and hence $\rho^2=9M/(16\pi^2R^6)$, we have as desired

$$ V=  -\frac{3}{5}\frac{GM^2}{R}$$

</details>

The thermal energy, can be understood as the kinetic energy due to the constituant of the gas. It can be shown that, for a monoatomic [ideal gas](../../../thermo/thermo/idealgas/), the mean kinetic energy per particle is given by $\langle mv^2/2 \rangle = 3k_B T/2$, where $k_B$ is the Boltzmann constant, allowing to translate temperatures into energy. If you do not know this formula, you can also take it for granted for now. The total thermal energy of our sphere of gas is then given by

$$E_T = N\frac{3 k_B T}{2}= \frac{M}{\mu}\frac{3k_B T}{2}$$

where $N=M/\mu$ is the total number of particles in the sphere of gas and $\mu$ is the mean mass of an atom in the cloud.

Using the two formulas above, our condition for gravitational collapse becomes

$$\frac{3}{5}\frac{GM^2}{R} \geq \frac{3 k_B T}{2} \frac{M}{\mu}$$

Of course, the formulas used here are approximations of what is really happening in real conditions[^1], but they will give us pretty good understanding of what is really going on.

[^1]: Overall, we assume here that the cloud is spherical and homogeneous and that no exterior force acts on it. We further assume that it is made of monoatomic gas at a constant temperature $T$ and furthermore that the cloud is not rotating and not magnetized. Indeed this is a lot of assumptions! Reality is much more complex (as we discuss later on) but the computations become quickly unbearable and better suited for computers!

Isolating the mass in this expression, we are able to find the limit mass $M_J$, called the *Jeans mass*, at which the cloud will start to collapse under its own gravity. The condition for collapse hence becomes

$$M \geq M_{J}$$

with

$$\boxed{M_J = \mathcal{C}\left(\frac{T}{\mu}\right)^{3/2}\frac{1}{\sqrt{\rho}}}$$

with the proportionality constant

$$\mathcal{C}= \left(\frac{5k_B}{2G}\right)^{3/2}\sqrt{\frac{3}{4\pi}}$$

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

Putting this in the above equation on $M$ and brute forcing our way through the equations, we obtain

$$M \geq \frac{(3M)^{1/3} 5k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M^{2/3} \geq \frac{5(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M \geq \left(5\frac{(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}\right)^{3/2}$$

$$ M\geq \frac{5^{3/2}(3)^{1/2} (k_B T)^{3/2}}{2^{3/2}(4\pi \rho)^{1/2}(G\mu)^{3/2}}$$

$$ M\geq \left(\frac{5k_B}{2G}\right)^{3/2}\sqrt{\frac{3}{4\pi}} \left(\frac{T}{\mu}\right)^{3/2}\frac{1}{\sqrt{\rho}}=M_J$$

which is the result given above.
</details>

Hence, the hotter the gas, the higher the mass required for collapse, and the denser the gas, the smaller the mass.

Assuming the gas is molecular hydrogen ($\mu=m_p$) and computing the constants factors (using $\rho = n m_p$), we obtain

$$ M_J \sim 6 \times 10^{4}\sqrt{\frac{T^3}{n}} M_{\odot},$$

where $n$ is the density of hydrogen atoms. We hence see something exciting here: a cascading effect is hidden in this formula. When the cloud will start contracting, its density $n$ will automatically increase, leading $M_J$ to decrease. Hence independent subparts of the cloud will reach the condition $M\leq M_J$ and collapse, such that the cloud will fragment in smaller clouds, over and over again during the gravitational collapse. 

<!-- This collapsing is also helped due to the increasing rotation speed of the collapsing cloud.  -->
<!-- Indeed, to keep things simple and hand waving for now, consider the angular momentum $\vec{L}$ of a particle rotating at the edge of the collapsing cloud. We saw in the classical mecanics class that it was given by $\vec{L}=r\wedge m\vec{v}$ and that it was conserved if we consider only the gravitational force. Now, as the cloud contracts after having overpassed Jean's mass, the radius $r$ will decrease. In order for $\vec{L}$ to be conserved when $r$ decreases, $\vec{v}$ must increase. At some point, the speed will then be large enough to thorn apart the cloud in smaller patches (a proper account of this would have been to use the moment of inertia of the cloud, treating it as a solid sphere). -->

This all explains why the stars are born in clusters of thousands of stars inside large clouds instead of obtaining a single large star. After some time, all these stars are separated and spread apart in the Galaxy along their rotation around the Galactic center.

## Closer to reality: turbulence and magnetic fields

![image](../images/pillarsofcreation.jpg){: width="53.5%"}![image](../images/orion.jpg){: width="45%"}

*Left: The iconic "Pillars of Creation" nebula as seen by the JWST. It provides another characteristic example of star forming region within a nebular cloud. Credit: [NASA, ESA, CSA, and STScI](https://esawebb.org/images/pillarsofcreation_composite/). Right: Portio of the Orion nebula. In both images, notice the complex patern made by the interstellar medium. Credit: [ESA/Webb, NASA, CSA, PDRs4All ERS Team](https://esawebb.org/images/weic2315b/)*

Under the same assumptions used before, we can estimate that the cloud should collapse on itself under its own gravity in a free-fall time of

$$ \boxed{t_f = \sqrt{\frac{3\pi}{32 G \rho}}}$$

This time suppose that nothing is stopping the cloud while it collapse on itself. 

<details>
  <summary>Proof</summary>

Consider a a particle of mass $m$ located at the edge of the collapsing cloud. We label its position by the radial distance $r$. The particle starts at $r=R$ and fall freely until it reaches the center of the cloud at $r=0$. The [second law of dynamics](../../../meca/Newton/laws/) for this particle becomes

$$ m\frac{\text{d}^2r}{\text{d}t^2}=\frac{-GMm}{r^2} $$

in which $m$ simplifies on both sides. Hence all little particles of mass $m$ part of the outer spherical shell of the cloud will fall identically and in the same time (under our simplifying assumptions), always attracted by the whole mass $M$ of the cloud contained within the outer shell.

First, we integrated this equation from $R$ to $r$, and work out the right hand side until we obtain (remember again that $\int_a^b r^n \text{d}r=[r^{n+1}/n+1]^b_a$)

$$ 
\begin{aligned}
\int_R^0\frac{\text{d}^2r}{\text{d}t^2}\text{d}r&=-\int_R^r GM\frac{1}{r^2}\text{d}r\\
&=-GM\int_R^r r^{-2}\text{d}r\\
&=GM[r^{-1}]_R^r\\
&=-\frac{GM}{R}+\frac{GM}{r}\\
&= \frac{GM}{R}\left(-1+\frac{R}{r}\right)\\
&= \frac{GM}{R}\left(-\frac{r}{r}+\frac{R}{r}\right)\\
&=\frac{GM}{R}\left(\frac{R-r}{r}\right)
\end{aligned}
$$

Similarly to what we did to derive the kinetic energy in Newtonian mechanics, the left hand side can be rewritten as an integral over time as

$$
\begin{aligned}
\int_{0}^{t(r)}\frac{\text{d}^2r}{\text{d}t^2}\frac{\text{d}r}{\text{d}t}\text{d}t=\frac{GM}{R}\left(\frac{R-r}{r}\right)
\end{aligned}
$$

where $t(r)$ is the time it takes for the cloud to collapse from a radius of $R$ to a radius of $r$.

Remembering that $2\int_a^bu'u\text{d}x=[u'^2]_a^b$ and stating that the velocity at initial time $t_R$ should be $0$, we obtain

$$\frac{1}{2}\left(\frac{\text{d}r}{\text{d}t}\right)^2= \frac{GM}{R}\left(\frac{R-r}{r}\right) $$

that is (remember that a square root comes with two solutions positive and negative)

$$\frac{\text{d}r}{\text{d}t}= \pm\sqrt{2\frac{GM}{R}}\sqrt{\frac{R-r}{r}}$$

The negative solution $(-)$ will be of interest here, as it is the one with decreasing $r$, that is the collapsing case. Taking this solution and rearranging the expression such that we separate $r$ on the left hand side and $t$ on the right hand side, we get, after integrating

$$\int_R^0 \sqrt{\frac{r}{R-r}}\text{d}r = -\int_{0}^{t(r)}\sqrt{2\frac{GM}{R}} \text{d}t$$

The right hand side of this integral is tricky to compute, so we will accept here the following result:

$$ \int_a^b \sqrt{\frac{x}{x_0-x}}{\rm d}x =  \left[x_0 \arcsin\left(\sqrt{\frac{x}{x_0}}\right) - \sqrt{x(x_0-x)}\right]^b_a$$

You can try to prove it yourself or look for a derivation in a mathematical textbook!

Computing the integral on both sides, we then get

$$R \arcsin\left(\sqrt{\frac{r}{R}}\right) - \sqrt{r(R-r)}-\frac{\pi R}{2}= -\sqrt{\frac{2GM}{R}}t(r)$$,

using $\arcsin(1)=\pi/2$.
We can then isolate

$$t(r)= R \sqrt{\frac{R}{2GM}}\left(-\arcsin\left(\sqrt{\frac{r}{R}}\right) + \sqrt{r(R-r)}+\frac{\pi R}{2}\right)$$

Now, it is really easy to obtain the time of free fall for the cloud to collapse. Remember that $t(r)$ is the time it takes for the cloud to collapse from a radius $R$ to a radius $r$. The total free fall time is then given by this expression for $r=0$. We then get

$$t_f= t(0)= \pi \sqrt{\frac{R^3}{8GM}}$$ 

much simpler! Now remembering that $\rho = M/V=3M/(4\pi R^3)$ i.e. $R^3=3M/(\rho 4\pi)$, we obtain 

$$ t_f =\pi \sqrt{\frac{3M}{8GM\times 4\pi}} = \frac{3\pi}{32G\rho}$$

as desired! ($\pi/\sqrt{\pi}=\sqrt{\pi\pi}/\sqrt{\pi}=\sqrt{\pi}$).

</details>

Assuming the cloud is made of hydrogen only, we obtain a time of free fall of $\sim 300 000$ years. This might seems like a long time for something to free-fall, but remember that our Galaxy is $~13.5$ billion years old, and hence it is a very short time on astrophysical scales!  From observations : clouds live for $15 000 0000$ years. Hence it is clear that the clouds are not free-falling, but something must stop them.

Rotation accelerates when the cloud shrinks, which gives some significant amount of energy preventing the collapse. Magnetic fields slow down this rotation (known as magnetic breaking).

The study of molecular clouds is hence a whole exciting field by itself. Turbulence, magnetic field and structure formation, fractal, filaments, clumps. + complex chemistry on dust grains --> life.

## The source of stellar energy

Eventually, clusters of stars will light up within the cloud.
As they are the end product of gravitational collapse, it is no surprise that they appear as spherical objects. The spherical shape of heavenly bodies is indeed the direct consequence of the law of gravitation, from which smaller masses are attracted towards larger mass, with a radial symmetry (Putting a large mass at the center of a frame, acts only and identically along $\vec{u_r}$). 

The very first stage of a star's life, is called a protostar.

![image](../images/HL_Tau_protoplanetary_disk.jpg){: width="53.5%"}


*Credit: HL-$\tau$ protostar [Credit: ALMA (/NRAO/ESO/NAOJ)](https://www.almaobservatory.org/en/press-releases/revolutionary-alma-image-reveals-planetary-genesis/)* 

If one assumes again that the proto-star has constant density, it is possible to infer the pressure at its center to be

$$ P_c = \frac{3}{8\pi}\frac{GM^2}{R^4}$$

For a star like the sun, we obtain $P_c\sim$. This enormous pressure needs to be balanced or the star will shrink again and can not appear as the "eternal" spheres we are observing in the sky.

We will demonstrate this equation in the next class on [stellar structure](../stars-struc/). 

Now, making the *very* rough assumption that the gas at center of the star is an [ideal gas](../../../thermo/thermo/idealgas/), it must obey the famous relationship $$PV=n\mathcal{R}T$$. From this, we can estimate the central temperature to be

$$\boxed{T_c\sim\frac{1}{2}\frac{GM\mu}{k_BR}}$$ 

<details>
  <summary>Proof</summary>

The ideal gas law reads:

$$P=\frac{nRT}{V}$$ 

Now, you have to remember that $n=N/N_A$ is the number of moles of particles in the gas (with $N$ the number of particles). Hence:

$$P=\frac{N\mathcal{R}T}{N_AV}$$

Now, we can introduce the boltzmann constant $k_B=\mathcal{R}/N_A$ and write $N=M/\mu$, as we did for the cloud, where $\mu$ is the mean mass of a particle in the star. The ideal gas law now reads

$$P=\frac{N k_BT}{V\mu}$$

Putting 

$$P=\frac{N kT}{\mu V}=\frac{3Mk_BT}{4\pi R^3\mu}$$ 

Now looking for the pressure at the center $T_c$, we get

$$\frac{3}{8\pi}\frac{GM^2}{R^4}=\frac{3Mk_BT_c}{4\pi R^3 \mu}$$

which becomes after simplification:

$$T_c\sim\frac{1}{2}\frac{GM\mu}{k_BR}$$

</details>

### Chemical?

### Thermal?

### Nuclear!


## Minimal mass to pretend at the star title

## Going further: recommanded readings

- An introduction to Star Formation - D. Ward-Thompson and A. P. Whitworth - Cambdrige University Press - 2011
