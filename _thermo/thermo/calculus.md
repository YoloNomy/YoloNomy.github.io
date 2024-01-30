---
layout: default
title: Calculus
parent: thermo
nav_order: 1
---

# Studying change

Disclaimer: this is not a proper class on derivatives and integrals. Go grab a book before or after reading this page.

## Derivatives

$$ \boxed{Q = \frac{\text{d} f}{\text{d} x}} $$

In your brain, you should immediately think "Oh, $Q$ is a function that tells me how does $f$ changes if $x$ changes". It works as follows:

- If $Q>0$, then $f$ increases with $x$. The stronger the increase, the bigger the value of $Q$.
- If $Q<0$, then $f$ decreases with $x$. The stronger the increase, the bigger the absolute value of $Q$.
- If you find that $Q=0$, it means that $Q$ is a constant with respect to $x$: $x$ can take whatever value, $f$ will always give the same number.

Velocity, is how much the position $x$ of a body change with time $t$, hence it should be no surprise that we can write

$$v = \frac{\text{d} x}{\text{d} t}$$

### Illustration: temperature along a bar of metal

Unfortunately I am not talking here about a place where you can drink and listen to heavy music but about a long stick made of metal which can be heated. Now consider such a stick, and imagine that for some reason, its temperature changes along its lenght. I choose here a (non-realistic) way to model it such that it can be easily understood.

To be a bit fancy, consider a 30 cm bar with a $x$ axis labelling the position on the bar. Now one can measure the temperature $T$ at each point $x$, in order to obtain $T(x)$. Such a function will give us the temperature, say in degrees Celsius, all along the bar. Let us imagine that this temperature varies as a Gaussian curve, i.e. as on the figure below:

![image](../images/temperature.png){: width="60%"}

Now what would tell us the quantity

$$Q=\frac{\text{d} T}{\text{d} x}?$$

Read again what we said in introduction and try to picture what $Q$ means and would it would looks like.

So, $Q(x)$ will be a function, telling us at which point $x$, how the temperature is changing when progressing on the metal bar along $x$. From the red curve above, you can guess that:
- Before $x=15$ cm, the temperature increases when progressing along $x$. The derivative should hence be positive. 
- After $x=15$ cm, the temperature decreases when progressing along $x$. The derivative should hence be negative.
- At $x=15$, the variation stops a bit around the peak while it changes direction. Hence $T(x)$ behaves as a constant function near that point. We expect the derivative to be exactly 0 at that point. 

If you found all of these, good job! Here is the exact plot of the derivative:

![image](../images/dTdx.png){: width="50%"}![image](../images/T-dTdx.png){: width="50%"}


*Left: $\frac{\text{d}T}{\text{d}x}$ for the case illustrated above Right: comparison between $\frac{\text{d}T}{\text{d}x}$ and $T(x)$*

Its value also inform us on how brutally or not $T$ changes as a given $x$. A closer comparison between the two curve allow you to interpret it exactly as such. Try any function $T(x)$ you want with [this code](../codes/metalbar.py) in order to train your intuition of derivatives!

### Formalism of derivatives

Derivation is defined formally as

$$\frac{\text{d} f}{\text{d} x} = \lim_{\epsilon\to0}\frac{f(x+\epsilon)-f(x)}{\epsilon}$$

This definition makes sense for the notation $\frac{\text{d} f}{\text{d} x}$, as it is the computation of a tangent $\Delta y/\Delta x$ to a curve at a given point, by taking the limit $\Delta y\to 0$ and $\Delta x\to 0$. Hence it explains why the derivative is informing us on the rate of change of a function at a given point.

From this definition, you can for exemple compute the derivative of any functions, as for example $f(x)=x^2$. Doing so, you would find:

$$\frac{\text{d}(f=x^2)}{\text{d} x}=2x$$

<details>
  <summary>Proof</summary>

$$
\begin{aligned}
\frac{\text{d} f}{\text{d} x}
&=  \lim_{\epsilon\to0}\frac{(x+\epsilon)^2-x^2}{\epsilon}\\
&=  \lim_{\epsilon\to0}\frac{x^2+2x+\epsilon^2 - x^2}{\epsilon}\\
&= \lim_{\epsilon\to0}\frac{2x\epsilon+\epsilon^2}{\epsilon}\\
&= \lim_{\epsilon\to0}\left(2x + \epsilon\right)\\
&=2x
\end{aligned}
$$

</details>

Luckily, there are plenty of formulas you can learn that allows imediately to compute the derivative of usual functions. They are extremely important in physics, so at some point you will have to learn them by heart. Here is a list containing the most common functions you will encounter: 

| $f$   |      $\frac{\partial f}{\partial x}$ |
|----------|:-------------:|
| $ax+b$ |  $a$ |
| $x^n$ |  $nx^{n-1}$ |
| $\sqrt{x}$ |   $\frac{1}{2\sqrt{x}}$| 
| $\cos(x)$ | $-\sin(x)$ |
| $\sin(x)$ | $\cos(x)$ |
| $e^{x}$ | $e^{x}$ |
| $\ln(x)$ | $\frac{1}{x}$ |

As long as we encounter some examples in physics, you will become familiar with these rules.

Chain rule:

$$ \boxed{\frac{\text{d} f}{\text{d} y} = \frac{\text{d} f}{\text{d} x}\frac{\text{d} x}{\text{d} y}}$$

Product rule:

$$ (uv)' = u'v + v'u $$

| $f(u(x))$   |      $\frac{\partial f}{\partial x}$ |
|----------|:-------------:|
| $au+b$ |  $au'$ |
| $u^n$ |    $nu'u^{n+1}$   | 
| $\sqrt{u}$ |   $\frac{u'}{2\sqrt{u}}$| 
| $\cos(u)$ | $-u'\sin(u)$ |
| $\sin(u)$ | $u'\cos(u)$ |
| $e^{u}$ | $u'e^{u}$ |
| $\ln(u)$ | $\frac{u'}{u}$ |

### Partial derivatives

### Differentials

## Integrals

### Illustration: getting position from velocity 

### Tables of integrals
