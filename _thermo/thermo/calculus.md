---
layout: default
title: Calculus
parent: thermo
nav_order: 1
---

# Studying change

Disclaimer: this is not a proper class on derivatives and integrals. Go grab a book before or after reading this page.

## Derivatives

$$ \boxed{Q = \frac{\partial f}{\partial x}} $$

In your brain, you should immediately think "Oh, $Q$ is a function that tells me how does $f$ changes if $x$ changes". It works as follows:

- If $Q>0$, then $f$ increases with $x$.
- If $Q<0$, then $f$ decreases with $x$.
- If you find that $Q=0$, it means that $Q$ is a constant with respect to $x$: $x$ can take whatever value, $f$ will always give the same number.

Velocity, is how much the position $x$ of a body change with time $t$, hence it should be no surprise that we can write

$$v = \frac{\partial x}{\partial t}$$

### Illustration: temperature along a bar of metal

Unfortunately I am not talking here about a place where you can drink and listen to heavy music but about a long stick made of metal which can be heated. Now consider such a stick, and imagine that for some reason, its temperature changes along its lenght. I choose here a (non-realistic) way to model it such that it can be easily understood.

To be a bit fancy, consider a 30 cm bar with a $x$ axis labelling the position on the bar.

![image](../images/temperature.png){: width="60%"}

$$\frac{\partial T}{\partial x}$$



### Tables of derivatives

| $f$   |      $\frac{\partial f}{\partial x}$ |
|----------|:-------------:|
| $x^n$ |  $nx^{n-1}$ |
| $\sqrt{x}$ |   $\frac{1}{2\sqrt{x}}$| 
| $\cos(x)$ | $-\sin(x)$ |
| $\sin(x)$ | $\cos(x)$ |
| $e^{x}$ | $e^{x}$ |
| $\ln(x)$ | $\frac{1}{x}$ |

Chain rule:

$$ \boxed{\frac{\partial f}{\partial y} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial y}}$$

Product rule:

$$ (uv)' = u'v + v'u $$

| $f(u(x))$   |      $\frac{\partial f}{\partial x}$ |
|----------|:-------------:|
| col 1 is |  left-aligned |
| col 2 is |    centered   | 
| col 3 is | right-aligned |


## Integrals

### Illustration: getting position from velocity 

### Tables of integrals
