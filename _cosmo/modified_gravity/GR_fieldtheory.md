---
layout: default
title: General relativity field theory or geometry?
parent: cosmo
---

As discussed in the [previous lecture](./foundations-GR.md), GR is largely interpreted as geometry of space and time. But, is it a field theory, and in what sense? We will see that, most physical theories can be seen either as pure theories talking about fields moving on a flat space-time background or as geometrical theories. Those are two faces of the same coin.

## GR as a field theory 

Can we forget everything about geometry when talking about GR, and instead present it purely as a field theory?

### What is a field theory?

A field $\phi(x,y,z,t)$. 

$$\mathcal{L} = \mathcal{L}_{\rm kin}(\phi) - V(\phi) + \mathcal{L}_{\rm int}(\phi,J) + \mathcal{L}_m(\psi) $$

$J$ is some form of current 

$\mathcal{L}_{\rm int}(J,\phi) = g \langle J\phi\rangle$

Euler-Lagrange equations:

$$\frac{\partial \mathcal{L}}{\partial \phi} = \partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\right)  $$

For a massless scalar field without interaction:

$$\mathcal{L}_{\rm kin}= -\frac{1}{2}\partial_\mu\phi\partial^\mu\phi$$

Where the minus sign comes from our choice of signature $(-,+,+,+)$.

$$\Box \phi = 0 $$

$$\mathcal{L}= -\frac{1}{2}(\partial_\mu\phi)^2 - V(\phi)$$

A **mass**

$$ m_\phi^2 = \frac{\partial^2 V}{\partial \phi^2}$$

$V(\phi)=m^2\phi^2/2$.


## What can the gravity be coupled to?

$$T_{\mu\nu}$$

## Why gravity must be mediated by an integer spin field?

The challenge is to reproduce:

$$V(r) = \frac{Gm_1m_2}{r} $$

from the coupling $\mathcal{L}_{\rm int} = g \langle J\phi\rangle$


### Can gravity be mediated by a spin 0 field?

"Nordström-like gravity (1912-1913)", relativistic version of Newton gravity.
In the modern language of field theories, 

$$ \mathcal{L} = -\frac{1}{2}\partial_\mu \phi\partial^\mu \phi   + g\phi {\rm Tr}(T_{\mu\nu})$$ 

Which leads to the equation of motion:

$$\partial_\mu \phi\partial^\mu\phi = g{\rm Tr}(T_{\mu\nu}) $$

$\partial_\mu\phi\partial^\mu \phi = \Box \phi = \partial_t^2\phi - \partial_x^2\phi$.
To which the potential associated is:

$$V(r) = \frac{g^2}{4\pi} \frac{M_1M_2}{r} $$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Consider

$$ \mathcal{L} = -\frac{1}{2}\partial_\mu \phi\partial^\mu \phi  + g\phi {\rm Tr}(T_{\mu\nu})$$ 

The Euler-Lagrange equation of motions associated to the extremization of the action are:

$$\partial_\mu \left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\right) = \frac{\partial \mathcal{L}}{\partial \phi} $$

The left hand side gives $\partial_\mu\phi\partial^\mu\phi$. The proof of this expression can be found in our [class on scalar fields in cosmology](../cosmo/scalar_fields.md). 

</details>

$ G = g^2/4\pi$ 

As a side-note electromagnetism too. Hence we see that under suitable simplifying limits, many theories behave like scalar fields, which justify the existence of forces in $1/r^2$ for long-range forces.

<details markdown="1">
  <summary><strong>Comparaison with electromagnetism</strong></summary>

$$\mathcal{L}= -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}-j^\mu A_\mu $$

If $A_\mu = (\phi,0,0,0)$.

$$\mathcal{L} = -\frac{1}{2}\partial_\mu\phi\partial^\mu \phi - \rho \phi$$

Because:

</details>

But these theories do not deflect light, because for relativistic matter ${\rm Tr}(T_{\mu\nu})=0$. Thus, such a simple theory can not describe gravity.

Furthermore, the perihelion shift is incorrect.

How about other terms like $\partial_\mu \phi \partial_\nu \phi T^{\mu\nu}$? Fails too.

Spin zero gravity does not seem to work.

### Can gravity be mediated by a spin # field?

$A_\mu$ : positive masses repel each others 

### Can gravity be mediated by a spin $\geq 3$ field?

Forbidden from Weinberg theorems.

### The Fierz-Pauli approach 

Equivalent to GR when adding a coupling of $h$ with its own $T^{(h)}_{\mu\nu}$ according to the SEP, through an infinite tower of corrections (Gupta 1954, Deser 1970).

### Non-metricity vs fifth force

## Newton-Cartan approach: Newtonian theory is about curved space-time

Newton gravity can be read as a geometric theory

Similarly, gauge theories all admit reading as theories talking about curvature and abstract geometry.

## Further reading and watching

- R. P. Feynmann - Lectures on gravitation 
- [Modified gravity - Rachel ROSEN](https://www.youtube.com/watch?v=1THLppx96T8) 