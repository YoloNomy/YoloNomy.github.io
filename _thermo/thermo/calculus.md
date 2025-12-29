---
layout: default
title: Calculus
parent: thermo
nav_order: 1
---

# Studying change

Some extremely important tools for all kind of physics are the notions of "derivative" and "integral". They are very general concepts used to study and quantify the notion of change. There exist several type of derivatives, which can sometimes be very subtle to understand.

Derivative and integrals will be absolutely necessary to study the changes occuring in thermodynamic systems and every kind of physics. As such, there is no way to escape them! 

As for every mathematical object, there exist different levels of abstraction and subtelty which you can use to approach and understand them. We will present here the simplest possible approach, presenting only the very absolute basics. Clearly, this is not a proper class on derivatives and integrals. To know more, you should go grab a book reading this page and become as expert as you can on these concepts. If you are already an expert, just skip this lecture!

## Derivatives

Consider a quantity $f$ which can change when a variable $x$ change. It could be for example the temperature $T$ at different point $x$ in a room or the position of something with respect to time. As such, it is described by a function $f(x)$.

The **derivative** $Q$ of $f$ with respect to $x$ is another function noted as:

$$ \boxed{Q = \frac{\text{d} f}{\text{d} x}} $$

Do not be (yet) too impressed with the d and the fraction. Just consider this as a fancy notation.
Seeing such a quantity, you should immediately think "Oh, $Q$ is a function that tells me how does $f$ changes if $x$ changes". It works as follows:

- If $Q>0$, then $f$ increases with $x$. The stronger the increase, the bigger the value of $Q$.
- If $Q<0$, then $f$ decreases with $x$. The stronger the increase, the bigger the absolute value of $Q$.
- If you find that $Q=0$, it means that $Q$ is a constant with respect to $x$: $x$ can take whatever value, $f$ will always give the same number.

Let's look at a simple example. If you think about it, the velocity of an object is encoded in the change of its position. As such, you may have the intuition that the derivative is a good concept to describe velocity. Indeed, consider a moving object with position labelled by a number $X$ (for exemple the distance you could measure with a ruler between you and the object). If this object moves, the position $X$ will depend on time $t$ i.e. it will be different at different time. It is thus a function $X(t)$. The velocity $v$ is defined as being the derivative of $X$ with respect to $t$:

$$v = \frac{\text{d} X}{\text{d} t}$$

We can now understand why derivatives are so important for physics! 

### An illustration: temperature along a bar of metal

Consider a long stick made of metal which can be heated (I agree that this might not be the most exciting exemple, but it is simple enough). Now consider such a stick, and imagine that, for some reason, its temperature changes along its lenght. It could be for exemple be heated only in some place by a candle.

To be a bit fancy, consider a 30 cm bar with a $x$ axis labelling the position on the bar. Now one can measure the temperature $T$, in whatever unit you prefer, at each point $x$, in order to obtain $T(x)$. Such a function will give us the temperature all along the bar. 
Imagine that by doing such a measurement, you obtain this curve:

![image](../images/temperature.png){: width="60%"}

This shape is called a Gaussian curve, and it is adminitedly not a realistic model for temperature of a bar of metal, but we that's not the point here!

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

We can define derivative a bit more formally as

$$\boxed{\frac{\text{d} f}{\text{d} x} = \lim_{\epsilon\to0}\frac{f(x+\epsilon)-f(x)}{\epsilon}}$$

This definition makes sense for the notation $\frac{\text{d} f}{\text{d} x}$, as it is the computation of a tangent $\Delta y/\Delta x$ to a curve at a given point, by taking the limit $\Delta y\to 0$ and $\Delta x\to 0$. Hence it explains why the derivative is informing us on the rate of change of a function at a given point.

From this definition, you can for exemple compute the derivative of any functions. Try the two following exercices:

<details markdown="1">
  <summary><strong>Exercice:</strong> Using the definition of the derivative, proove that the derivative of $f=x+1$ is $\text{d}f/\text{d}x=1$.
</summary>


$$
\begin{aligned}
\frac{\text{d} f}{\text{d} x}
&=  \lim_{\epsilon\to0}\frac{(x+1+\epsilon)-(x+1)}{\epsilon}\\
&= \lim_{\epsilon\to0}\frac{x+1+\epsilon - x-1}{\epsilon} \\
&= \lim_{\epsilon\to0}\frac{\epsilon}{\epsilon} \\
&= \lim_{\epsilon\to0}1\\
&=1
\end{aligned}
$$

</details>

<details markdown="1">
  <summary><strong>Exercice:</strong> Using the definition of the derivative, proove that the derivative of $f=2x$ is $\text{d}f/\text{d}x=2$.
</summary>


$$
\begin{aligned}
\frac{\text{d} f}{\text{d} x}
&=  \lim_{\epsilon\to0}\frac{2(x+\epsilon)-2x}{\epsilon}\\
&\lim_{\epsilon\to0}\frac{2x+ 2\epsilon-2x}{\epsilon}\\
&\lim_{\epsilon\to0}\frac{2\epsilon}{\epsilon}\\
&\lim_{\epsilon\to0}2\\
&=2
\end{aligned}
$$

</details>

Another important example is $f(x)=x^2$. This would lead to:

$$\frac{\text{d}(f=x^2)}{\text{d} x}=2x$$

<details>
  <summary><strong>Exercice:</strong> Proove the above formula </summary>

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

<details markdown="1">
  <summary><strong>Proof:</strong> Prooving the sum rule
</summary>


$$
\begin{aligned}
\frac{\text{d}(f + g)}{\text{d} x}
&=  \lim_{\epsilon\to0}\frac{f(x+\epsilon) + g(x+\epsilon)-(f(x)+g(x))}{\epsilon}\\
&= \lim_{\epsilon\to0}\frac{f(x+\epsilon) + g(x+\epsilon)- f(x)+g(x)}{\epsilon}\\
&= \lim_{\epsilon\to0}\left(\frac{f(x+\epsilon) - f(x)}{\epsilon} + \frac{g(x+\epsilon) - g(x)}{\epsilon}\right)\\
&= \lim_{\epsilon\to0}\frac{f(x+\epsilon) - f(x)}{\epsilon} + \lim_{\epsilon\to0}\frac{g(x+\epsilon) - g(x)}{\epsilon}\\
&= \frac{\text{d}f}{\text{d}x} + \frac{\text{d}g}{\text{d}x} 
\end{aligned}
$$

Where we used here some properties that we did not yet proove but that might seem natural (as for example, the fact that the limit of a sum is the sum of limits).

</details>

For a product, things are a bit more complicated and the *product rule* is:

$$ \boxed{(fg)' = f'g + g'f} $$

Hence, for another example, if $f=x^3\sqrt{x}$, then $f'=3x^2\sqrt{x}+\frac{x^3}{2\sqrt{x}}$.

<details markdown="1">
  <summary><strong>Proof:</strong> Prooving the product rule
</summary>


$$
\begin{aligned}
\frac{\text{d} (fg)}{\text{d} x}
&=  \lim_{\epsilon\to0}\frac{f(x+\epsilon)g(x+\epsilon)-f(x)g(x)}{\epsilon}\\
&=  \lim_{\epsilon\to0}\frac{f(x+\epsilon)g(x+\epsilon) + f(x)g(x+\epsilon) - f(x)g(x+\epsilon) -f(x)g(x)}{\epsilon}\\
&=  \lim_{\epsilon\to0}\frac{f(x+\epsilon)g(x+\epsilon) -  f(x)g(x+\epsilon) + f(x)g(x+\epsilon)-f(x)g(x)}{\epsilon}\\
&=  \lim_{\epsilon\to0}\frac{f(x+\epsilon)g(x+\epsilon) -  f(x)g(x+\epsilon)}{\epsilon} +\lim_{\epsilon\to0}\frac{f(x)g(x+\epsilon)-f(x)g(x)}{\epsilon} \\
&=\lim_{\epsilon\to0}g(x+\epsilon)\lim_{\epsilon\to0}\frac{f(x+\epsilon) -  f(x)}{\epsilon} + \lim_{\epsilon\to0}f(x)\frac{g(x+\epsilon)-f(x)g(x)}{\epsilon}\\
&=g(x)\frac{\text{d}f}{\text{d}x} + f(x)\frac{\text{d}g}{\text{d}x} 
\end{aligned}
$$

Where we used implicitly again some simple properties of the limits that we will not proove here.

</details>

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

Combining all these rules, you can also find the expression for the derivative of a ratio as:

$$ \boxed{\left(\frac{f}{g}\right)' = \frac{f'g - g'f}{g^2}} $$

<details>
  <summary><strong>Proof:</strong> prooving the ratio rule </summary>

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

The quantity $\text{d}f$ is called the differential of $f$ and represents a small variation of $f(x,y,z,...)$ when all its variable are changed by a small amount $\text{d}x$,$\text{d}y$,$\text{d}z$...
It is expressed with the partial derivatives as 

$$\boxed{\text{d}f = \frac{\partial f}{\partial x}\text{d}x  + \frac{\partial f}{\partial y}\text{d}y + \frac{\partial f}{\partial z}\text{d}z + ... }$$

## Integrals

Another critical operation is given by $integrals$ of functions. They are noted as such 

$$ \boxed{I = \int_{x_A}^{x_B} f(x) \text{d}x} $$

They are a bit harder to compute and to get familiar with, but it will soon become a second nature through examples!
Here, you should think that "$I$ is the "sum of the function $f(x)$ between the values $x_A$ and $x_B$". Indeed the symbol $\int$ represent as "continuous" summation and $\text{d}x$ is the differential of $x$, hence it is a small variation of $x$. We will try to clarify what we mean by that in the next section.

Another import aspect of integrals, is that they are the "reverse" operation of the derivative:

$$ \int_{x_A}^{x_B} f'(x) \text{d}x = [f(x)]_{x_A}^{x_B}= f(x_B)-f(x_A) $$

where the notation $[...]_{x_A}^{x_B}$ means that we take the difference of the function under the brackets between the value at $x_B$ and the value at $x_A$.

### Illustration: back to the metal bar 

Integrals alows to compute the total change of a quantity between two points, from knowing the value of its rate of change. 

Going back to the metal bar example, imagine that you know only the value of $\frac{\text{d}T}{\text{d}x}$, that is, you know how much the temperature change at every point of the metal bar. Now imagine that, from this, you want to know the difference of temperature between two points $x_A$ and $x_B$, you will obtain it from the integral

$$\Delta T = T_B - T_A = \int_{x_A}^{x_B} \frac{\text{d}T}{\text{d}x}\text{d}x $$

This means that, the total change of temperature $\Delta T$ is obtained by summing the value of the rate of change of the temperature $\frac{\text{d}T}{\text{d}x}$ on each small portion of the metal bar $\text{d}x$ between $x_A$ and $x_B$.
As we said earlier, the formula for the integrals are "reverse" derivatives. Imagine then that $\frac{\text{d}T}{\text{d}x}=2x$. You migh remember that $(x^2)'=2x$. Hence, you will have

$$\Delta T = T_B - T_A = \int_{x_A}^{x_B} \frac{\text{d}T}{\text{d}x}\text{d}x = \int_{x_A}^{x_B}2x\text{d}x= x_B^2 - x_A^2$$


### Tables of integrals

Just take the table of derivatives and reverse it!

| $f$   |      $\int_{x_A}^{x_B} f(x) \text{d}x$ |
|----------|:-------------:|
| $a$ |  $[ax]_{x_A}^{x_B}$ |
| $x^n$ |  $[\frac{x^{n+1}}{n+1}]_{x_A}^{x_B}$ |
| $\cos(x)$ | $[\sin(x)]_{x_A}^{x_B}$ |
| $\sin(x)$ | $[-\cos(x)]_{x_A}^{x_B}$ |
| $e^{x}$ | $[e^{x}]_{x_A}^{x_B}$ |
| $\frac{1}{x}$ | $[\ln(x)]_{x_A}^{x_B}$ |

