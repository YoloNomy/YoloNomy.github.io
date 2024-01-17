---
layout: default
title: Stars, formation and structure
parent: cosmo
nav_order: 1
---

By trying to answer the vast question "what is a star?", we will apply most of the things we have learn in our physics class in an exciting context.

# Stars: formation and structure

## The birth: Jean's parameters

Star form inside large clouds called molecular clouds. 

Formation can happen when the potential energy becomes greater than the thermal energy, that is

$$-V\geq E_T$$

Let us roughly estimate what this condition is for the cloud.

The total gravitational energy of a sphere contained within the cloud is given by:

$$V = -\frac{3}{5}\frac{GM^2}{R} $$

You can recognize the $GM^2/R$ contribution from Newtonian mechanics (link), which is the energy of gravitation of two masses $M$ separated by a distance $R$. The factor of $3/5$ asks for a bit of extra work, but if you don't want to face the trouble, just assume it for now.

<details>
  <summary>Proof</summary>

$$ V = -\int_0^M \frac{G m}{r}{\rm d}m $$

$${\rm d}m = \rho {\rm d}\mathcal{V}=4\pi \rho r^2 {\rm d}r $$

$$ V = -\int_0^R 4\pi\frac{G m(r)}{r}\rho r^2{\rm dr} $$


$$ V = -\int_0^R 4\pi G m(r)r\rho{\rm dr} $$

$\rho=\frac{m(r)}{4\pi r^3/3}$ and thus $m(r)=\frac{4}{3}\rho \pi r^3$

$$ V = - \frac{16\pi^2}{3}\int_0^R G \rho^2 r^{4}{\rm d}r $$

$$ V= - \frac{16\pi^2}{3}G\rho^2 \frac{R^5}{5}$$

Now using again $\rho= 3M/(4\pi R^3)$ and hence $\rho^2=9M/(16\pi^2R^6)$, we have as desired

$$ V=  -\frac{3}{5}\frac{GM^2}{R}$$

</details>

The thermal energy, energy of a monoatomic gas $3k_B T/2$ per atom:

$$E_T = N\frac{3 k_B T}{2}= \frac{M}{\mu}\frac{3k_B T}{2}$$

where $\mu$ is the mean mass of an atom in the cloud.
Such that

$$\frac{3}{5}\frac{GM^2}{R} \geq \frac{3 k_B T}{2} \frac{M}{\mu}$$


Jean Mass

$$M \geq M_{J}$$

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

Puting this in the above equation on $M$, we have

$$M \geq \frac{(3M)^{1/3} 5k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M^{2/3} \geq \frac{5(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M \geq \left(5\frac{(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}\right)^{3/2}$$

$$ M\geq \frac{5^{3/2}(3)^{1/2} (k_B T)^{3/2}}{2^{3/2}(4\pi \rho)^{1/2}(G\mu)^{3/2}}$$

$$ M\geq \left(\frac{5k_B}{2G}\right)^{3/2}\sqrt{\frac{3}{4\pi}} \left(\frac{T}{\mu}\right)^{3/2}\frac{1}{\sqrt{\rho}}=M_J$$
</details>

free fall time and turbulence

Rotation barrier: