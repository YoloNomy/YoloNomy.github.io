---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---
# Derivation of the probability of microstates by maximizing the entropy

We now want to justify that the principle of maximum entropy is a powerful tool to find the probability distribution associated to microstates of a system. To do so, we will introduce the Lagrange multiplier technique, which is a powerful mathematical tool to find the $p_i$ associated to the maximal value of $S$, under some additional constraints. We will illustrate this principle and this tool on the case of fair dice and of a biased die.

## Maximising the entropy: the Lagrange multipliers

Recall from the [previous lecture](../entropy/), that the entropy $S$ of a probability distribution $p_i$ is given by

$$ S= -\sum_i p_i \ln(p_i)$$

$S$ quantifies our ignorence about the system. For example, if our system is a box of gas, $i$ can label all the possible microscopic configurations of the large number of particles contained in the box. $p_i$ would be the probability that, at this exact moment, the particles are in this exact configuration. In theory, we could measure many many times $N$ the system, write down the number of times that it was observed in a given configuration $n_i$, and estimate these probabilities in a frequentist way using $p_i=n_i/N$ as described in the previous lecture. Unfortunately, most of the time this is simply impossible. For exemple, there is something like $10^{25}$ particles of water in a glass. It would simply be impossible to measure the position and velocity of each of them, not even a single time.

We argued in the previous lecture that a powerful way to estimate $p_i$ is to find the configuration (that is all the values $p_1$,$p_2$ ...) which maximizes $S$. Doing so, we maximizes our ignorance and find the most agnostic probability distribution given what we know. This will reveal to be an extremely powerful tool.

Now, we might know some things about the system. For exemple, we might do some measurements, or infer something from the physics of the system. This will provide us with some informations about mean quantities, like average energy, or average number of particles. If we want a fair estimation of the $p_i$, one that is as close as possible to what we would obtain if we could estimate these probabilities from measures, we should take these informations into account. 

The proper way to do so, is to maximize the entropy under some constraints. That is, maximize the entropy but asking for some specific conditions to be satisfied. The proper way to do so is to use the so called **Lagrange multipliers**. These are rather advanced -- but unavoidable -- tools.

We will present them here only as a general receipt in order to maximize the entropy under constraints, without further justifications. More details about the justification and the mathematics of lagrange multipliers can be found in the following note.

The receipe goes as follows: let say that we want to maximize $S(p_i)$ under some constraint $C(p_i)$. We should write the constraint $C(p_i)$ in the form of an equation that is equal to zero. For exemple, we can (and should!) ask as a constraint that the sum of the probabilities adds up to one: $\sum_i p_i =1$. As a constraint, this would become $C(p_i)=\sum_i p_i -1= 0$.  We can also ask for other constraints, such as constraints on measured mean values. Each constraint will be labeled as $C_k$.

Then, we consider the function:

$$\mathcal{L}(p_i) = S(p_i) + \sum_k\lambda_k C_k(p_i)$$

where $C_k$ are our different constraints and $\lambda_k$ are some undefined constants, one per constraint, called the **Lagrange multipliers**.

The way to obtain the distribution $p_i$ which maximizes the entropy $S$ under the constraints $C_i$, is to write the two equations:

$$
\begin{cases}
\begin{aligned}
&\frac{\partial \mathcal{L}}{\partial p_i}=0 \\
&\frac{\partial \mathcal{L}}{\partial \lambda_k}=0
\end{aligned}
\end{cases}
$$

compute explicitely the derivatives and isolate $p_i$. Note here that the first equation should be interpreted as one equation for each variable $p_i$ ($p_1,p_2,p_3 ...$).
The numbers $\lambda_k$ can be re-expressed in term of the relevant quantities using the second equation (which just give back the constraints $C_k=0$). This receipe might seem very abstract and unjustified for now, but we will illustrate it on many exemple below! 

<details markdown="1">
  <summary> <strong>Supplements:</strong> Remarks, justification and details about Lagrange multipliers</summary>

Consider a function $f$ on a multidimentional space of dimension $N$, as e.g. $f:\mathbb{R}^N\to \mathbb{R}, x_i \to f(x_i)$. Here again, we should understand the $x_i$ as a list dimensions like $x,y,z$ if $f$ was a function over space, that is $f(x_i)= f(x_1,x_2,x_3..., x_N)$.

In generality finding the extremums of a function $f(x_i)$ consist of solving together the equations 

$$
\begin{cases}
\begin{aligned}
&\frac{\partial f(x_i)}{\partial x_1}= 0\\
&\frac{\partial f(x_i)}{\partial x_2}= 0\\
& \dots\\
& \frac{\partial f(x_i)}{\partial x_N}= 0
\end{aligned}
\end{cases}
$$

simply condensed in a single equation as

$$ \frac{\partial f(x_i)}{\partial x_i}= 0$$

Finding the $x_i$ solution of these equations gives us point where the derivative cancels in all directions, that is the function behaves locally as a constant function in all directions at that point. This extremum point can be a maximum or minimum of the function. Its exact nature is given by the sign of the second derivatives, which quantifies the curvature of the function at that point.

The previous equation can also be interpreted as the cancellation of all the components of the [gradient vector](../../../meca/Newton/Energy/) of $f$ in the $x_i$ space:

$$ \vec{\nabla}f= 0$$

Now, what if we want to add on top of this the constraint that some other function $g$ on the same space must be null i.e. $g(x_i)=0$? That is, we want to find the maximum value of $f$, but staying on the region in the space where the condition $g(x_i)=0$ is true.

![image](../images/LagrangeMultipliers2D.svg){: width="80%"}

*Countours level of some function f(x,y) (dashed ellipses), with gradients (dashed arrows). The maximum of $f$ is found when the gradient is zero (where all gradient vectors meet). An additional constraint is required by asking to find the maximum of $f$ within a specific region where another function, $g(x,y)$ obeys a specific condition $g(x,y)=c$ (red curve). The gradient of the red curve is drawn with dashed red arrows. This point is found where the gradient of $f$ is inversely proportional to the gradient of $g$ (in opposite direction). [From author Nexcis, contribution to Wikimedia commons](https://en.wikipedia.org/wiki/Lagrange_multiplier#/media/File:LagrangeMultipliers2D.svg).*


The way to do so, is to consider the new function $\mathcal{L}$:

$\mathcal{L}(x_i) = f(x_i)-\lambda g(x_i)$

And looking for the point satisfying the condition:

$$ \vec{\nabla}\mathcal{L}=0$$

Which can be explicited as:

$$\vec{\nabla}f = -\lambda\vec{\nabla}g$$

As sketched on the figure above, this means that the gradient of $g$ is inversely proportional to the gradient of $f$. As such, we are located on a point in space satisfying $g=0$ and $f$ has its maximum value. Perhaps the figure is enough to convince you that this is the case.

</details>

### Compute the probabilities for a fair die

Now that we introuced Lagrange multipliers, we will prove the claim made in our [first lecture](.//entropy) that, without any information on the system, maximizing the entropy leads to equiprobable probability distributions.

Consider for this a dice with six faces. All the microstates $i$ are within the set $\Omega=\\{1,2,3,4,5,6\\}$ of length $N=6$. You can roll it as many times as you want, and you will always get one of these states $i\in X$. Now, how to obtain the probability $p_i$ associated with each $i$?

First, as claimed earlier, we should maximize the entropy in order to be as fair as possible about our ignorance. What else do we know? Well not much. All the faces seems to play an identical role in the system. None is favored. We say that they are related by a symmetry transformation.

The only thing that we know is that:

$$\sum_i p_i=1$$ 

This can be written 

$$C(p_i) = \sum_i p_i - 1 =0$$

Applying the procedure described in the above section, we obtain

$$\boxed{p_i =  \frac{1}{6}}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

We write: 

$$
\begin{align}
\mathcal{L} &=  S(p_i) - \lambda C(p_i)\\
&= -\sum^6_i p_i \ln(p_i) - \lambda (\sum^6_i p_i -1)
\end{align}
$$

Now the derivatives are:

$$
\begin{align}
&\frac{\partial \mathcal{L}}{\partial p_i} = -\ln(p_i) - \frac{1}{p_i}p_i - \lambda = - \ln(p_i) - 1 - \lambda \\
&\frac{\partial \mathcal{L}}{\partial \lambda} =  -(\sum^6_i p_i -1) 
\end{align}
$$

In case this might be unclear: the first equation should be understood as 6 different equations $\partial \mathcal{L}/\partial p_1, \partial \mathcal{L}/\partial p_2 ... \partial \mathcal{L}/\partial p_6$. As such, terms as $\sum^6_i p_i = p_1 + p_2 + ... + p_6$ are derivated six times with respect to the six values of $p_i$, always leading to 1.

Now we must set these two equations to zero. The second equation is just giving back that the sum of probabilities are equal to one. Isolating $p_i$ in the first equation, we obtain

$$
\begin{align}
-&\ln(p_i) - 1 - \lambda =0\\
-&\ln(p_i) = \lambda + 1\\
&\ln(p_i) = -\lambda - 1\\
& p_i = e^{-\lambda - 1}
\end{align}
$$

So, we found that each microstate $i$ has the same probability (since $\lambda$ is a constant). Now, how could we get rid of this $\lambda$? To do so, we re-apply the condition on the sum of probabilities (our second equation), and we obtain 

$$
\begin{align}
\sum_i^6 p_i &= 1\\
\sum_i^6  e^{-\lambda - 1} &= 1\\
 6 e^{-\lambda - 1} &= 1\\
e^{-\lambda - 1} = \frac{1}{6}
\end{align}
$$

Since the summing six times a constant gives ... six times that constant! Replacing this expression in the expression for $p_i$, we get

$$
p_i= \frac{1}{6} 
$$

Obviously, we considered here a dice with six faces, but quite obviously, for a dice with $N$ faces, we would have obtained $p_i=1/N$. We found that all microstates are equiprobable.
</details>

Note that the constant $\lambda$ which was used to do this trick completely disapeared from the final result.

This is indeed the best we can say about our dice, for which all the faces are equivalent (i.e. they are related by a symmetry transformation) for which there is no reason to prefer one face over the other.


### Compute the probabilities for a biased die

Now assume that someone gave you a dice and when throwing it a few time, it does not seem quite right. It looks like some numbers appear more often than other. It is biased. $p_i=1/6$ seemed like a reasonable assumption, but clearly it doesn't match the reality of your system. What could you do?

The answer, you guessed it, is to maximise the entropy, but with some additional constraint. The additional conditions we want to impose are now

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i i &= \langle i \rangle \\
&\sum_i p_i  &= 1
\end{aligned}
\end{cases}
$$

Where $\langle i \rangle$ is the mean value of $i$ that can be obtained by a large number of measurements (in this case, we thus consider that our empricial mean is a good approximation of the statistical average, that is $\bar{i}=\langle i \rangle$). As discussed in our [previous lecture](../entropy), $\langle i \rangle=3.5$ for a fair die, so we expect here the value to be anything different.

Our conditions translate in terms of constraints as:

$$
\begin{cases}
\begin{aligned}
&C_1 = \sum_i^6 p_i i -\langle i \rangle \\
&C_2 = \sum_i^6 p_i-1
\end{aligned}
\end{cases}
$$

Using the Lagrange multiplier technique, we obtain

$$ 
\boxed{p_i = \frac{e^{-\lambda_1 i}}{\sum_i^6 e^{-\lambda_1 i}}}
$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>
We write: 

$$
\begin{align}
\mathcal{L} &=  S(p_i) - \lambda_1 C_1(p_i)- \lambda_2 C_2(p_i)\\
&= -\sum^6_i p_i \ln(p_i) - \lambda_1 (\sum^6_i i p_i - \langle i \rangle)  - \lambda_2 (\sum^6_i p_i -1)
\end{align}
$$

Now the derivatives are:

$$
\begin{align}
&\frac{\partial \mathcal{L}}{\partial p_i} = - \ln(p_i) - 1 - \lambda_1 i - \lambda_2    \\
&\frac{\partial \mathcal{L}}{\partial \lambda_1} =  -(\sum^6_i i p_i - \langle i \rangle)
&\frac{\partial \mathcal{L}}{\partial \lambda_2} =  -(\sum^6_i p_i -1) 
\end{align}
$$

Setting the first equation to 0, we get

$$
\begin{align}
&- \ln(p_i) - 1 - \lambda_1 i - \lambda_2 =0 \\
&p_i= e^{- 1 - \lambda_1 i - \lambda_2} \\
&p_i = e^{- 1 - \lambda_2}e^{-\lambda_1 i}
\end{align}
$$

The sum of probabilities equal to one leads to 

$$
\begin{align}
&\sum_i^6 e^{- 1 - \lambda_2}e^{-\lambda_1 i}=1 \\
&e^{- 1 - \lambda_2} = \frac{1}{\sum_i e^{-\lambda_1 i}}
\end{align}
$$

Re-injecting in the expression of $p_i$, we get

$$p_i = \frac{1}{\sum_i^6 e^{-\lambda_1 i}}e^{-\lambda_1 i} $$

</details>

We realise now that the probability of the state depends on $i$. Thus, by asking for our constraints, we are not in a state of equiprobability anymore: some states will be more probable and some less.

We also see that we could not get rid easily of the Lagrange multiplier $\lambda_1$ associated with our constraint on the mean $C_1$, as it still appear in our expression. Replacing the value of $p_i$ in the mean value constraint, we obtain:

$$\langle i \rangle =  \frac{\sum^6_i i e^{-\lambda_1 i}}{\sum_i^6 e^{-\lambda_1 i}}$$

This equation fully determines $\lambda_1$ but is quite difficult to solve! There are several ways to do it. Here we propose to simply use a numerical function of scipy to obtain it, based on a method named "Brent’s method". We will not explain it in detail here (check online if you are curious). You can find a code obtaining $\lambda_1$ for any value of $\langle i \rangle$ [here](../codes/biased_dice.py). Note that in the case where $\lambda_1=0$, we obtain:

$$\langle i \rangle =  \frac{\sum_i^6 i}{\sum_i^6 1} = \frac{1+2+3+4+5+6}{6} = 3.5$$

recovering the case of the fair dice.

Once $\lambda_1$ is obtained, we have all the informations to get $p_i$ for each state $i$.
We plotted below the probability distribution maximizing the entropy with the constraint that $\langle i \rangle=4.5$. We see, as expected, that the dice is biased and prefers higher values. Our probability distribution reflects this fact. For $\langle i \rangle = 3.5$, we obtain exactly $\lambda_1=0$, thus finding back the case of the fair die. As such, this new probability distribution encompases and generalizes the one of the fair die. Try other values of $\langle i \rangle$ and see for yourself! 

![image](../images/biased_dice.png){: width="80%"}

*Maximum entropy solution for the biased die problem with a mean of 4.5. Plotted using [this code](../codes/biased_dice.py).*


<details markdown="1">
<summary><strong>Exercice :</strong> think about other observational constraints you could add to the biased die to refine the estimation of it's probability distribution. Try to add them in the code and see how it changes the figure of $p_i$  </summary>

For the case of a biased die, we can not look at other observables than $i$ to constraint their average value. 

The statistical variance of the observable $i$, with mean $\langle i \rangle$, can be computed as:

$$
\begin{aligned}
 {\rm Var}(i)&= \langle i^2\rangle - \langle i \rangle^2\\
 &= \sum_i p_i i^2 - \langle i \rangle^2
 \end{aligned}
$$

The variance quantifies the average deviation of $i$ around it's average value. In other word, it quantifies the scatter of $i$ around $\langle i \rangle$.

Adding the constraint on the variance with it's own Lagrange multiplier can be done and further specify the shape of $p_i$ as done in [this code](../codes/biased_dice_var.py).
However, one should be careful, as doing so might force the probability distribution to look like a bell curve. It should thus be done only when justified, in order to avoid biaising what we think $p_i$ look like with unjustified a priori.

![image](../images/biased_dice_var.png){: width="80%"}

*Maximum entropy solution for the biased die problem with a mean of 4.5 and a variance of 0.5. Plotted using [this code](../codes/biased_dice_var.py).*

</details>

<details markdown="1">
  <summary><strong>Exercice :</strong> Consider the same exercice for the sum of two dice, fair and biased. </summary>


*Maximum entropy solution for the biased die problem with a mean of 4.5 and a variance of 0.5. Plotted using [this code](../codes/biased_dice_var.py).*

</details>

## Going further: recommended readings and watching

- [Probability distributions and maximum entropy - K. Konrad (2010)](https://kconrad.math.uconn.edu/blurbs/analysis/entropypost.pdf)
- [Entropic inference: Some pitfalls and paradoxes we can avoid - A. Caticha (2012) - arXiv:1212.6967](https://arxiv.org/abs/1212.6967)