---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---

Let's now traduce the principle of maximum entropy in term of more familiar problems, as a large number of particles boucing in a box. We will be interested here in a system, like a gas, which has a discrete number of distinguishable microstates. For now, the exact physical system is not important, and the equations we will derive will be very general. The only thing that matters is that our system can access multiple microstates with different energy levels.

## The fair dice of nature: The microcanonical ensemble for isolated systems

Consider then a system, like a box of gas. All the atoms can be arranged in this box in a large number of different distinguishable configurations. Each configuration, labelled by the index $i$, is made of the data of all the positions and momentum of the particles. To each such configuration, one can associate an energy $E_i$. For simplicity, we assume here that the number of accessible microstates is discrete and finite (which is of course only a gross representation of a glass of water). It will be straightforward to generalize this to the continuous case in the next lectures by replacing sums with integrals and taking limits toward infinity but the discrete picture is much easier to understand. It will also prove to be very useful in the case of quantum systems, as you can probably imagine.

For now, you can think of this box of gas as a die with an extremely large number of faces (all the configurations of the particles). As times goes by, nature "rolls" automatically for you the dice again and again, and the system jumps from one microstate to another. The question is the following: what is the chance that, when you will observe it, the die will be in a given state $i$.

## Microstates and degeneracies

In the case where either nothing special is known about the system, or all of its properties are strictly fixed (for example imagine an isolated system of perfectly known properties: $T$, $V$, $n$) all possible microstates are equally accessible and none are prefered. This would simply be a generalisation of the fair die.

In this case, all possible particle configuration are equally probable, and thus, by maximizing the entropy, we would obtain, as in the previous lecture for the fair die:

$$\boxed{p_i = \frac{1}{N}}$$

associated with a single value for the entropy $$S = \ln(N)$$.
As $N$ is extremely large, each configuration of particle is treated equally and has an extremely low probability of occuring. What else is there to say for this very specific case?

Imagine that we have no informations at all about the system, but that the microstates can be distinguished by some property. They could have different energy $E_i$ or be associated with different observed colors or anything you might want.
Let $g_i$ be the **degeneracy** that is the number of possible microstates (particle configurations) amongst the $N$ associated with the same property, say the energy $E_i$. That is, for example $g(E_2)=3$ would mean that there exist three different particle configurations in the box with the same energy state $E_2$.

We have then, by construction:

$$
\sum_i g_i = N
$$

where, as a reminder, $N$ is the total number of microstates (which for the case of possible particle configurations could be extremely large, and even infinite) and $g_i$ is the number of such configurations with energy $E_i$.

It is clear now, that the probability $p(E_i)$ that the observed microstate has the energy $E_i$ should be $p(E_i)=p_i g_i$. Since $p_i=1/N$, we have:

$$\boxed{p(E_i) = \frac{g_i}{N}}$$

Note that even though they have similar names, $p_i$ and $p(E_i)$ are different quantities. The first is the probability that the system will be observed in the specific and unique configuration $i$, while the second is the probability that the state will be one of possibly many with energy $E_i$. Clearly, the more configurations (microstates) are associated with a specific energy state, the more probable this energy state will be.

Now, can we write the entropy of such system in an interesting way?

## Expressing and interpreting the entropy 

Recall from the [first lecture](../entropy/), that the entropy $S$ of a probability distribution $p_i$ is 

$$ S= -\sum_i p_i \ln(p_i)$$

Let's try to re-express it term of the degeneracy $g_i$.
To do so, we consider the number of possible ways to rearange the $N$ microstates into the possible allowed energy states with occupation numbers $g_i$, given by:

$$
C^g_N = C^{g_1,g_2,...}_N = \frac{N!}{\prod_i g_i!}
$$

$C^{g}_N$ thus tells you how you could redistribute $g_i$ degeneracies amongst the $N$ microstates.

Maximizing $C^g_N$ will give us the most probable configuration of the $g_i$. It can be shown that this maximum is very sharp, making other configurations almost impossible. 

If $N$ and $g_i \to \infty$, which is clearly the case for physical systems made of atoms, we can use the so called **Stirling approximation**:

$$ N! \sim N^N e^{-N} $$

<details>
  <summary>Proof</summary>
  
Recall first that $N! = 1\times 2 \times 3 ... \times N$ and that for two number $a$ and $b$, $ln(a \times b)=\ln(a)+\ln(b)$. Then $\ln(N!)= \ln(1\times 2 \times 3 ... \times N) = \ln(1)+ \ln(2) + ...+\ln(N)$. As such:

$$
\begin{aligned}
\ln(N!) &= \sum_{x=1}^N \ln(x)
\\ &\sim \int_1^N \ln(x) \qquad (N\to \infty) \text{d}x\\
&= [x \ln(x)-x ]_1^N \\
&= N\ln N -N
\end{aligned}
$$

If you do not recall the primitive of $\ln(x)$ ised in the above derivation, you can at least verify convince yourself that $\frac{d}{dx}(x\ln(x)-x = \frac{d}{dx}(x\ln(x)) - 1 = \ln(x) - \frac{x}{x} -1  = \ln(x)$. 

Then, one can recover $N!$ from the previous expression by taking its exponential, that is:

$$
N! \sim e^{N\ln N -N} = e^{\ln(N^N)}e^{-N} = N^N e^{-N}
$$

</details>

This approximation allows us to write the entropy $S$ in terms of $C^g_N$ as 

$$ 
S= \ln(C^g_N)/N
$$

<details>
  <summary>Proof</summary>

Using Stirling's approximation:

$$
C^g_N =  \frac{N!}{\prod_i g_i!} \sim \frac{N^N e^{-N}}{\prod_i g_i^{g_i}e^{-g_i}}
$$

Now $$\prod_i g_i^{g_i}e^{-g_i}= e^{-\sum_k g_i}\prod_i g_i^{g_i}$$, since $e^{-g_1}e^{-g_2}...= e^{-g_1-g_2-...}$. And since $\sum_k n_k =N$, we find that $\prod_i g_i^{g_i}e^{-g_i}= e^{-N}\prod_i g_i^{g_i}$. 

Thus:

$$
C^g_N \sim \frac{N^N}{\prod_i g_i^{g_i}}
$$

Taking now the logarithm (and recalling that $ln(a/b)=ln(a)-ln(b)$):

$$
\begin{aligned}
\ln(C^g_N)&= N\ln(N)- \sum_i g_i \ln(g_i)\\
&= Nln(N) - \sum_i p_i N \ln(p_iN)\\
& =  Nln(N) - \sum_i p_i N(\ln(p_i)+ \ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i)+ \sum_i N p_i\ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i) - N\ln(N)\\
& = N S
\end{aligned}
$$
</details>

From the previous expression, we understand that maximizing $C^g_N$ is equivalent to maximizing $S$ (as $N$ is fixed). Following our discussion of the [previous lecture](../entropy), doing so with the additional constraint that $\langle E \rangle$ is known is a powerful inference tool which will allow us to get the probability of each microstate $p_i$ while being fair and accounting for what we don't know. Thanks to our previous derivation, we also see that, since $S$ is proportional to $C^g_N$, doing so will give us the most probable particle configurations within the box associated to the most probable $g_i$ combinations amongst the $N$ possible macrostates. It solely depends on how frequently in time the system will be in a state of energy $E_i$ by randomly bouncing between all the configurations.

## The biased dice of nature: The canonical model and equilibrium with a heat bath

Let's now add an additional constraint, by considering that the system is constrained to have a specific value for its average energy $\langle E \rangle$, for exemple by being emmerged in a larger exterior with this energy. In other word, it is in thermal equilibrium with it as defined in this [lecture](../../thermo/equilibrium). We call such an exterior a heat bath. A good example would then be a glass of water standing in your kitchen.

As time goes by, the system might go from one microstate to another, and some are possible but will never be explored. In particular, we have the constraint imposed by the heat bath that the average energy (e.g. in time) should be, after waiting long enough, $\bar{E}=\langle E \rangle$. The energy of the system can thus varies (fluctuate) slightly, but the average will always remain the same. Some microstate could be very weird, as e.g. all the particles being located in one corner of the box, or half having very high energies and the other half having very low energies. However, the great majority of these microstates are made of particles being distributed randomly everywhere in the box with reasonable velocities. As such, these states will be incredibly more probable and contribute much more to the value of the entropy.

We will now do the entropy maximization in order to find the probability of each microstates $p_i$. For this, we will not need anything else than the defintion of the entropy. To maximizes $S$, we use the technique of **Lagrange multipliers** introduced in the [previous lecture](../entropy-max) and force on the maximisation the following constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i E_i &= \langle E \rangle \\
& \sum_i p_i  &= 1
\end{aligned}
\end{cases}
$$

that is, we are only asking respectively for the average energy of a particle to be given by $\langle E \rangle$ and the sum of probabilities to be equal to one.

Maximizing $S$ under such constraints follows the exact same procedure as for the biased die that we discussed [previously](../entropy-max). You should try to redo-it yourself! The second Lagrange multiplier $\lambda_2$ is very special and as such we will give him a special name: $\beta$.

We then obtain the probability for the microstate to have the energy $E_i$ as:

$$
\boxed{p_i = \frac{1}{Z}e^{-\beta E_i}}
$$

where we also introduce the **partition function**:

$$Z = \sum_i  e^{-\beta E_i}$$

We have now been able to express the probability of each configuration of particles $p_i$ solely in term of its energy $E_i$. Note that the sum over $i$ here goes over all accessible configuration, regardless of the fact that some can have the same energy level $E_i$. We will go back on degeneracies and the connections with the microcanonical model at the end of this page.
The only missing part is to find what could be this mysterious constant $\beta$, which was forced upon us as a Lagrange multiplier for the constraint that we know the average energy of the system. $\beta$ could be obtained numerically using Brent's method as we did in the [previous lecture](../entropy-max/) for $\lambda_1$. We will instead find a deeper meaning to this quantity and show that $\beta =1/T$, i.e. it is the inverse of the temperature of the system. This already tells us something profound about the nature of what temperature is. But what exactly? 

## Finding back physical quantities from $Z$

The average energy of our gas can then be re-expressed from $Z$ as

$$
\boxed{\langle E \rangle = -\frac{1}{Z}\frac{\partial Z}{\partial \beta} = -\frac{\partial{\ln Z}}{\partial \beta}}
\label{eq:E-of-Z}
$$

<details>
  <summary>Proof</summary>
 
Using the second constraints, we can relate $\langle E \rangle$ to $Z$ as:

$$
\sum_i p_i E_i = \sum_i \frac{1}{Z}e^{-\beta E_i}E_i= \langle E \rangle
$$

Seeing that:

$$
-\frac{1}{Z}\frac{\partial Z}{\partial\beta} = \sum_i \frac{E_i}{Z}e^{-\beta E_i}
$$

and so:

$$
\langle E \rangle = -\frac{1}{Z}\frac{\partial Z}{\partial \beta} = -\frac{\partial{\ln Z}}{\partial \beta}
$$
</details>

The entropy $S$ can also be rederived in terms of $Z$ as:

$$
\boxed{S = \beta \langle E \rangle + \ln Z}
$$

<details>
  <summary>Proof</summary>
 
$$
\begin{aligned}
S &= -\sum_i p_i \ln(p_i) \\
&= \sum_i\frac{1}{Z}e^{-\beta E_i}\left[ \beta E_i + \ln (Z)\right]\\
&= \beta \langle E \rangle + \ln (Z)\sum_i e^{-\beta E_i}
\end{aligned}
$$

And so:

$$
S = \beta \langle E \rangle + \ln Z
$$
</details>

While we got rid of $\alpha$, the second Lagrange multiplier $\beta$ can be expressed with respect to the temperature. To do so, we define the temperature as the change of energy associated with a change of entropy:

$$
\boxed{T := \frac{\partial \langle E \rangle}{\partial S}_{n,V}} 
\label{eq:defTemp}
$$

The next section will discuss why this definition is deep and connects with the intuitions you might have about temperature. With this definition

$$
\boxed{\beta = \frac{1}{T}}
$$

<details>
  <summary>Proof</summary>

$$
\text{d}S = \beta \text{d}\langle E\rangle + \langle E\rangle\text{d}\beta + \frac{\partial \ln Z}{\partial \beta}d\beta
$$

using the relation between $\langle E \rangle$ and the entropy aswell as the fact that $Z$ is a function of only one independant variable $\beta$ or $\langle E \rangle$ since both are not independant because of $\langle E \rangle$ can be expressed in terms of $Z$. Now using the expression of $\langle E \rangle$ in term of $Z$, we can see that the two last terms cancels out to give simply: $\text{d}S = \beta \text{d}\langle E\rangle$. With the definition of $T$:

$$
T = \frac{\partial \langle E \rangle}{\partial S}_{n,V}
$$

Whe have $\text{d}S = \frac{1}{T}\text{d}\langle E\rangle$, allowing us to conclude that:

$$
\beta = \frac{1}{T}
$$
</details>

Similarly, we define the pressure to be 

$$\boxed{P := -\frac{\partial{\langle E \rangle}}{\partial{V}}\Bigg|_S}$$

We will also justify such a definition in the next section.
As such, knowing $Z$ allows us to express all our state variable and state functions and relate them to the microscopic behaviour of the system. Note that we operate here a change of point of view compared to classical thermodynamics, where quantities such as $P,T$ are not only considered only as state variables which can be measured and of which we try to keep track of the evolution. They are clearly considered as emerging from the underlying microscopic probability distribution of the constituents of the system.

Let's now clarify all of this with an illustration: On the following figure, we represented some examples of $p_i(E_i)$ computed using all the formula we just derived.

![image](../images/canonical_boltzmann_beta_derived.png){: width="80%"}

*Example of distributions of $p_i(E)$ associated with different average energy, temperature and entropy (arbitrary units). Computed with [this code](../codes/Plot_boltzmann.py)*.

We can see on the graph the probability of each microstates of the system -- i.e. of each configuration of particles -- associated to each energy $p_i$. Each curve on the figure is associated with a different average energy $\langle E \rangle$, imposed to the system by the heat bath with which it is at thermal equilibrium. Each curve is also associated to a value of the entropy $S$, which is maximum (and more exactly, each $p_i$ curve is constructed such that $S$ is maximum under the constraint that the average energy should be $\langle E\rangle$ as we did above).
To each curve, one can associate a temperature $T$ by computing the derivative of $E$ with respect to $S$. We will explain this more in the next section. However, we see immediately that the macrostates with the biggest average energy (in red) are associated with the highest energy, as we would expected. They are also associated with the highest value for the entropy, which is something that we can understand as they becomre flatter and flatter as the entropy increased (i.e. less peaked on small values of $E_i$). States of high temperature are thus states which are more spread over the axis $E_i$, hence less known and more disordered, attributes which we understand as associated to larger values of $S$. 

# Crossing the bridge with standard thermodynamics

## On the definition of temperature

The temperature is defined above as the variation of energy with respect to entropy. While it is totally possible (and easy) to derive such an equation from the second principle in the context of classical thermodynamics, it is usually not considered as a definition of $T$ itself, but rather as a definition of $S$.

By reversing the order and defining $T$ in such a way, we change its status and consider it as a quantity emmerging from the underlying microscopic properties of our system. Doing so also provides us with a very general definition of $T$, which can virtually be assigned to any physical system which can be associated with a average energy and an entropy. Let's try to understand better the significance of such a definition.

On the above figure, we see indeed that probability distributions for the microstates are different depending only on the mean energy $\langle E \rangle$. As the average energy increase, the entropy of the macrostate also changes, traducing the fact that the probability distribution are getting more spread. By our definition, the temperature quantifies precisely how much an increase in the entropy of the macrostate can be associated with a change of the mean energy.

Quantitatively, considering a transformation which change the average energy of the heat bath by a small amout $\text{d}\langle E\rangle$ (for exemple heating it somehow, at fixed volume and number of particle, which we always assumed here).The change of average energy can be associated with a change of entropy of the probability distribution such as

$$ \text{d}\langle E\rangle = \frac{\partial \langle E\rangle}{\partial S}\Bigg|_{n,V} \text{d}S= T\text{d}S $$

You might recognize here some flavour of the definition of entropy variations used to introduce the [second principle of thermodynamics](../../thermo/secondprinciple/)!

On the above numerical exemple, we see that $S$ seems to always increase when $\langle E \rangle$ increases. This seems coherent intuitively, as states with more energy are understood as more "agitated" and hence more chaotic or disogranised, thus being able to explore more possibilities for their energies $E_i$ (Entropy also has to do with predictability of the evolution of the states, and hence chaos in a deeper rigorous sense, we will come back to it).

A consequence of this, is that $T$ thus defined will seemingly always be a positive quantity. This is also a good news for our proposition of definition. What sense could we make of a negative temperature anyway? Well, this interesting question will has a very nice answer: negative temperature systems can exists, and our definition allows for it. They are known as "forced systems", in which the entropy of the system dicreases when we imput more energy (i.e. the system becomes more organized when we inject energy in them). Such systems rarely exist spontaneously in nature and we'll discuss them and their importance later on.

With this definition, we also get the important property that hot flows from hot system to cold sytem, under the addition of the second principle of thermodynamics as discussed [here](../../thermo/secondprinciple/). We will come back to the second principle in the context of statistical physics [later](../principles/).

## On the definition of pressure

While we redefined the temperature to be the increase of energy when entropy changes, we also proposed above an alternative definition for the pressure of the system we are considering. 
Indeed, pressure is not only a force over a surface but it is equivalent, and more useful to think of it as an energy per unit of volume! Or as stated above:

$$ P = -\frac{\partial{\langle E\rangle}}{\partial{V}}\Bigg|_S$$

This is equivalent (but more convinient) that the the usual definition. Indeed, to convince yourself, imagine a small infinitessimal box of size $\text{d}x$,$\text{d}y$ and $\text{d}z$. The pressure exerted on the surface $\mathcal{S}=\text{d}y\text{d}z$ is 

$$P=\frac{\text{d} \vec{F}\cdot \vec{n}}{\text{d} \mathcal{S}}= \frac{\text{d} \vec{F}\cdot \vec{n}}{\text{d} \mathcal{S}}=\frac{\text{d}\vec{F}\cdot \vec{n}}{ \text{d}y\text{d}z}= \frac{\text{d} \vec{F}\cdot \text{d}\vec{x}}{ \text{d}y\text{d}z\text{d}x}=\frac{\text{d} \vec{F}\cdot\text{d}\vec{x}}{\text{d}V} $$

On the other hand, the energy transfered to a wall of the box due to the kinetic motion of the particle within the box, can be written $\text{d} \langle E \rangle= - \delta W=-\vec{F}\cdot\text{d}\vec{x}$.

From which 

$$ P = \frac{\text{d} \vec{F}\cdot\text{d}\vec{x}}{\text{d}V} =-\frac{\partial{ \langle E \rangle}}{\partial{V}}\Bigg|_S$$

Hence, knowing only the expression of the energy $E_i$ of each microstate, we are able to derive all the thermodynamically relevant quantities (the pressure $P$, the temperature $T$, the average energy $E$, the entropy $S$...) through the partition function $Z$, simply by asking for the maximization of the entropy.

## On thermodynamical potentials

We note here that maximising the entropy for the canonical case is equivalent to maximize the free energy $F$.

## On degeneracies and giving back the microcanonical model

$$ p(E_n) = \frac{1}{Z} g_n e^{-\beta E_n}$$

with 

$$ Z = \sum_n g_n e^{-\beta E_n} $$

When $T\to \infty$, $\beta = 1/T\to 0$ and

$$ p(E_n)= \frac{g_n}{N}$$

We find back the microcanonical model !

Assuming that $S$ and $E$ are suitable functions for the inverse derivative theorem (link), we can write

$$ \beta =  \frac{\partial S}{\partial E}$$

we see that at very high energy, $\beta=0$ and thus changing the energy does not impact the entropy anymore.
All the states become equally accessible and energy of the heat bath can not discriminate and prefer some states anymore. 

### Taking the continuous limit

Now, before we move on, we should understand how everything that we discussed here can be generalised in the case where there is not a countable number of microstates, but a continuous infinity.

## Going further: recommended readings and watching

- [Statistical mechanics, theoretical minimum lectures - L. Susskind (2013)](https://theoreticalminimum.com/courses/statistical-mechanics/2013/spring)
- An introduction to thermal physics - D. V. Schroeder (2000) - Addison-Wesley 
- Statistical physics Part 1 and 2 - L.D. Landau and E.M. Lifshitz (1995) - (several editions available)