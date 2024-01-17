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

The gravitational energy:

$$V = \frac{GM^2}{R} $$

The thermal energy, energy of a monoatomic gas $3k_B T/2$ per atom:

$$E_T = N\frac{3 k_B T}{2}= \frac{M}{\mu}\frac{3k_B T}{2}$$

where $\mu$ is the mean mass of an atom in the cloud.
Such that

$$\frac{GM^2}{R} \geq \frac{3 k_B T}{2} \frac{M}{\mu}$$

By using $\rho = M/V$ and $V=\frac{4}{3}\pi R^3$.

Jean Mass

$$M \geq M_{J}$$

$$M_J \propto \left(\frac{T}{\mu}\right)^{3/2}\frac{1}{\sqrt{\rho}}$$

<details>
  <summary>Proof</summary>

Starting from the inequality 

$$\frac{GM^2}{R} \geq \frac{3k_B T}{2} \frac{M}{\mu}$$

We can simply isolate $M$ as

$$M^2 \geq  \frac{3k_B T}{2} \frac{RM}{G\mu}$$

$$M \geq \frac{3k_B T}{2}\frac{R}{G\mu}$$

Now consider the density 

$$ \rho = \frac{M}{V}= \frac{3M}{4\pi R^3}$$  

such that the radius is

$$ 1/R^3 = \frac{4 \pi \rho}{3M} \Rightarrow R = \left(\frac{3M}{4 \pi \rho}\right)^{1/3} $$

Puting this in the above equation on $M$, we have

$$M \geq \frac{(3M)^{1/3} 3k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M^{2/3} \geq \frac{3(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}$$

$$M \geq \left(3\frac{(3)^{1/3} k_B T}{2(4\pi \rho)^{1/3}G\mu}\right)^{3/2}$$

$$ M\geq \frac{3^{3/2}(3)^{1/2} (k_B T)^{3/2}}{2^{3/2}(4\pi \rho)^{1/2}(G\mu)^{3/2}}$$

$$ M\geq \left(\frac{3k_B}{2G}\right)^{3/2}\sqrt{\frac{3}{4\pi}} \left(\frac{T}{\mu}\right)^{3/2}\frac{1}{\sqrt{\rho}}=M_J$$
</details>

free fall time and turbulence

Rotation barrier: