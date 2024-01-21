---
layout: default
title: Stars, structure
parent: cosmo
nav_order: 1
---

# Inside a star

## What is a star?

Quantities to describe a star : $\rho$, $T$, $R$, $M$, $P$, $L$.

## Equations of structure

$$ \frac{\text{d} P}{\text{d}r}= -\rho(r)\frac{GM_r(r)}{r^2} $$

$$ \frac{\text{d} M}{\text{d}r}= 4\pi r^2\rho(r) $$


$$ \frac{\text{d} L}{\text{d}r}= 4\pi r^2\rho \epsilon $$

$$ \frac{\text{d} T}{\text{d}r}= \frac{3}{4a_Bc}\frac{\chi \rho}{T^3}\frac{L}{4\pi r^2}$$

$$ \frac{\text{d} T}{\text{d}r}=\left(1-\frac{1}{\gamma}\right)\frac{T}{P}\frac{\text{d} P}{\text{d} r} $$

Solving and put together, equation of state.

## Under pressure: hydrostatic equilibrium

Consider a point located at a radius $r\leq R$ inside a sphere.
Using Gauss's law for gravitation, it is possible to proof that only the mass $M_{\text{int}}$ inside the ball of radius $r$ contributes to gravitational field at $r$, while the field of the shell contained between $r$ and $R$ cancels out, as long as there is spherical symmetry. This is known as the shell theorem or Newton's theorem. As such, at the point $r$, the graviational field is given by

$$ \vec{g}= -\frac{GM_{\text{int}}}{r^2}\vec{u}_r $$

Now consider a small element of volume.

$$ \frac{\text{d} P}{\text{d}r}\vec{u}_r= \rho(r)\vec{g} $$

$$ \frac{\text{d} P}{\text{d}r}= -\rho(r)\frac{GM_r(r)}{r^2} $$

$$P_c = \frac{3}{8\pi}\frac{GM^2}{R^4}$$

<details>
  <summary>Proof</summary>


The density in the sphere is constant, and is given by $M_{\text{int}}=\rho V_{\text{int}}= 4\pi r^3/3$.

Hence 
$$ \vec{g}(r)= -\frac{4\pi G\rho r}{3}\vec{u}_r $$

Thus the equation of hydrostatic equilibrium becomes

$$ \frac{\text{d} P}{\text{d}r}\vec{u}_r= -\rho\vec{g} = \frac{4\pi G\rho^2 r}{3}\vec{u}_r $$

The central pressure is computed by integrating 

$$ P_c = \int_0^R\frac{4\pi G\rho^2 r}{3}\text{d}r  $$

$$ P_c = \frac{4\pi G\rho^2}{3} GM\int_0^Rr\text{d}r $$

$$ P_c= \frac{4\pi G\rho^2}{3} \frac{R^2}{2}$$

Now using $\rho = M/V=3M/(4\pi R^3)$, we get 

$$ P_c = \frac{3GM^2}{8\pi R^4}$$

</details>

## Mass-luminosity relationship

## Lifetime

## Going further: recommanded readings


- Stellar Structure and Evolution -  R. Kippenhahn, A. Weigert - Spriner - 1996
