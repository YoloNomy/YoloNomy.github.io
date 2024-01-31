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

$$\boxed{\frac{\text{d} f}{\text{d} x} = \lim_{\epsilon\to0}\frac{f(x+\epsilon)-f(x)}{\epsilon}}$$

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

As long as we encounter some examples in physics, you will become familiar with these rules. If you feel like training, try to proove them from the definition of the derivative.

To clear a bit the notation, let us write derivatives with a prime, i.e. $f'=\frac{\text{d} f}{\text{d} x}$.

Regarding summation, derivatives are very easy. Indeed, the derivative of a sum is the sum of the derivatives:

$$ \boxed{(f+g)' = f' + g'} $$

Hence, for example, if $f=x^2+\ln(x) + 3$, then by taking the derivative of each term of the sum, we obtain $f'=2x+\frac{1}{x}$.

For a product, things are a bit more complicated and the *product rule* is:

$$ \boxed{(fg)' = f'g + g'f} $$

Hence, for another example, if $f=x^3\sqrt{x}$, then $f'=3x^2\sqrt{x}+\frac{x^3}{2\sqrt{x}}$.

Imagine that $f$ is a function of another function $g(x)$ such that $f=f(g(x))$.
In such case, we will use an important rule named the so called *chain rule*:

$$ \boxed{\frac{\text{d} f}{\text{d} x} = \frac{\text{d} f}{\text{d} g}\frac{\text{d} g}{\text{d} x}}$$

From this, we are able to derive the following relations:

| $f(g(x))$   |      $\frac{\partial f}{\partial x}$ | Example 
|----------|:-------------:|:-------------:|
| $ag+b$ |  $ag'$ |$f=3(x^4)+2$,$f'=12x^3$|
| $g^n$ |    $ng'g^{n-1}$   | $f=(3x+1)^4$,$f'=12(3x+1)^3$
| $\sqrt{g}$ |   $\frac{g'}{2\sqrt{u}}$| $f=\sqrt{x^3+1}$, $f'=\frac{3x^2}{2\sqrt{x^3+1}}$
| $\cos(g)$ | $-g'\sin(g)$ | $f=\cos(3x)$,$f'=-3\sin(3x)$
| $\sin(g)$ | $g'\cos(g)$ |$f=\sin(x^2)$,$f'=2x\cos(x^2)$
| $e^{g}$ | $g'e^{g}$ | $f=e^{\cos(x)}$,$f'=-\sin(x)e^{\cos(x)}$
| $\ln(g)$ | $\frac{g'}{g}$ | $f=\ln(x^5)$, $f'=\frac{5x^4}{x^5}$

Try to rederive the examples to see if you understand them!

$$ \boxed{\left(\frac{f}{g}\right)' = \frac{f'g - g'f}{g^2}} $$

<details>
  <summary>Proof</summary>

This one is a bit intricate but it is a good training! 
The trick is to rewrite 

$$ \left(\frac{f}{g}\right)=f g^{-1}$$

Hence, from the product rule

$$\left(\frac{f}{g}\right)'=(f g^{-1})'=f'g^{-1}+ f(g^{-1})'$$

Now, you should use the rule for the derivative of a power, to get

$$(g^{-1})'=-1 g' g^{-2}=-\frac{g'}{g^2}$$

Hence, we can rewrite

$$\left(\frac{f}{g}\right)'=\frac{f'}{g}-\frac{fg'}{g^2} = \frac{f'g-g'f}{g^2}$$

</details>

### Partial derivatives

A function can depend on several variables $f(x,y,z,...)$. In that case, we can define the partial derivative with respect to $x$ as

$$\frac{\partial f}{\partial x}$$

which consist of derivating with respect to $x$ and treating all the other variables ($y,z...$) as if they where constants. The same rules for the derivative discussed above apply identically to compute the partial derivatives.

One can obtain the total derivative from the partial derivatives, using the chain rule in order to explicit all the possible dependence in $x$ of the other variables as

$$\frac{\text{d} f}{\text{d} x}=\frac{\partial f}{\partial x} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial x}+\frac{\partial f}{\partial z}\frac{\partial z}{\partial x} + ... $$

### Differentials

$\text{d}f$, the differential of $f$ is a small variation of $f$. $f(x,y,z)$

$$\boxed{\text{d}f = \frac{\partial f}{\partial x}\text{d}x  + \frac{\partial f}{\partial y}\text{d}y + \frac{\partial f}{\partial z}\text{d}z + ... }$$

## Integrals

$$ \boxed{I = \int_{x_A}^{x_B} f(x) \text{d}x} $$


$$ f(x_B)-f(x_A) = \int_A^B f'(x) \text{d}x $$


### Illustration: getting position from velocity 

### Tables of integrals
