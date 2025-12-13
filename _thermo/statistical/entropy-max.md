---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---
# Derivation of the probabilities of maximal entropy in the canonical ensemble.

Let's now traduce the principle of maximum entropy in term of the familiar problem of particles in a box. Consider then a closed system, like a gas, with mean energy $\langle E\rangle$ (its macrostate). The system is "forced" to keep this mean energy, for exemple by being emmerged in a larger exterior with this energy. We call such an exterior a heat bath. A good example would then be a glass of water standing in your kitchen. 

Assume that there exist $N$ distinguishable possible ways to re-arange the particles inside the box to give the same mean energy ($N$ possible microstate associated with the macrostate). For simplicity, we assume here that the number of microstates is discrete and finite (which is of course only a gross representation of a glass of water). It will be straightforward to generalize this to the continuous case by replacing sums with integrals and taking limits toward infinity but the discrete picture is much easier to understand.

Let's label by $i$ the possible microstates, that is the possible particle configurations giving back the mean energy $\langle E\rangle$. To each microstate is associated a specific energy $E_i$. As time goes by, the system might go from one microstate to another. It's energy can thus vary slightly, but the mean will always remain the same. Some microstate could be very weird, as e.g. all the particles being located in one corner of the box, or half having very high energies and the other half having very low energies. However, the great majority of these microstates are made of particles being distributed randomly everywhere in the box with average energies. As such, these states will contribute much more to the entropy calculation and will be incredibly more probable.

Let $n_i$ be the occupation number that is the number of possible microstates (particle configurations) associated with the same energy $E_i$.

We have:

$$
\sum_i n_i = N
$$

The probability of the configuration of particles to be in a state $i$ of energy $E_i$ can be then simply written as:

$$
p_i = \frac{n_i}{N}
$$

Leading naturally from the above equation to

$$
\sum_i p_i = \sum_i \frac{n_i}{N} = 1
$$

The average energy of the macrostate is then expressed in term of the microstates as:

$$
\langle E \rangle  = \sum_i p_i E_i = \sum_i \frac{n_i}{N} E_i
$$

The number of possible ways to rearange the $N$ microstates into the possible allowed energy states with occupation numbers $n_i$ is given by:

$$
C^n_N = \frac{N!}{\prod_i n_i!}
$$

Maximizing $C^n_N$ will give us the most probable configuration of the $n_i$. It can be shown that this maximum is very sharp, making other configurations almost impossible.

If $N$ and $n_i \to \infty$, which is clearly the case for physical systems made of atoms, we can use the so called **Stirling approximation**:

$$ N! \sim N^N e^{-N} $$

<details>
  <summary>Proof</summary>
  
$$
\begin{aligned}
\ln(N!) &= \sum_{x=1}^N \ln(x)
\\ &\sim \int_1^N dx \ln(x) \qquad (N\to \infty)\\
&= [x \ln(x)-x ]_1^N \\
&= N\ln N -N
\end{aligned}
$$

(One can verify easily that $\frac{d}{dx}(x\ln(x)-x=\ln(x)$). And then:

$$
N! \sim e^{N\ln N -N} = e^{\ln(N^N)}e^{-N} = N^N e^{-N}
$$

</details>

This approximation allows us to bring the entropy as:

$$ 
\ln(C^n_N)= NS
$$

<details>
  <summary>Proof</summary>

$$
\begin{aligned}
\ln(C)&= N\ln(N)- \sum_i n_i \ln(n_i)\\
&= Nln(N) - \sum_i p_i N \ln(p_iN)\\
& =  Nln(N) - \sum_i p_i N(\ln(p_i)+ \ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i)+ \sum_i N p_i\ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i) - N\ln(N))\\
& = N S
\end{aligned}
$$
</details>

Maximizing $C^n_N$ is thus equivalent to maximizing $S$. This will give us the most probable particle configurations within the box associated to the most probable $n_i$ combinations amongst the $N$ possible macrostates. As all this is very abstract, let us rephrase again exactly what we are doing here. You are having a gas and say that you are measuring one way or another that its mean energy is $\langle E\rangle$. Then you are thinking of the gas as made of particles, and you consider what are the most probable ways that these particles are arranged within the box. Particle configurations are classified by their energy $E_i$ and a number of corresponding configurations $n_i$ leading to this energy. Now in order to find the probability $p_i$, we will maximize the entropy, under constraints.

We will now do the entropy maximization using the so-called **Lagrange multipliers** and asking for the following constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i E_i &= \langle E \rangle \\
& \sum_i p_i  &= 1
\end{aligned}
\end{cases}
$$

asking respectively for the mean energy of a particle to be given by $\langle E \rangle$ and the sum of probabilities to be conserved.

<details>
  <summary>Lagrange multipliers</summary>
  
</details>

Once $S$ is maximized, we can obtain the probability for the microstate to have the energy $E_i$:

$$
\boxed{p_i = \frac{1}{Z}e^{-\beta E_i}}
$$

With $Z$ the *partition function*:

$$
Z := e^{1+\alpha}
$$

and $\alpha$ and $\beta$ are the two Lagrange multipliers associated to our two constraints.

$Z$ can be simplified by re-inserting it again in the normalization of probabilities:

$$
\sum_i p_i = \sum_i \frac{1}{Z}e^{-\beta E_i} =1 
$$

Leading to:

$$
\boxed{Z = \sum_ie^{-\beta E_i}}
$$

The mean energy of our gas can then be re-expressed from $Z$ as

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
-\frac{1}{Z}\frac{\partial Z}{\partial\beta}= \sum_i \frac{E_i}{Z}e^{-\beta E_i}
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
\boxed{T := \frac{\partial \langle E \rangle}{\partial S}} 
\label{eq:defTemp}
$$

The next section will discuss why this definition is deep and connects with the intuitions you might have about temperature. With this definition

$$
\boxed{\beta = \frac{1}{T}}
$$

<details>
  <summary>Proof</summary>
 

$$
dS = \beta d\langle E\rangle + \langle E\rangle d\beta + \frac{\partial \ln Z}{\partial \beta}d\beta
$$

(using Eq.\ref{eq:entropy-of-E} and the fact that $Z$ is a function of only one independant variable $\beta$ or $\langle E \rangle$ since both are not independant because of Eq.\ref{eq:E-of-Z}. Now using Eq.\ref{eq:E-of-Z}, we can see that the two last terms cancels out to give simply: $dS = \beta d\langle E\rangle$. With the definition of $T$:

$$
T = \frac{\partial \langle E \rangle}{\partial S}
$$

Whe have $dS = \frac{1}{T}d\langle E\rangle$, allowing us to conclude that:

$$
\beta = \frac{1}{T}
$$
</details>

# Crossing the bridge with standard thermodynamics

## On the definition of temperature

The temperature is defined above by Eq.\ref{eq:defTemp}.

Why is it a good definition:
- direction of heatflows
- broadening of $p(E)$ with increasing $\langle E \rangle$

## On the definition of pressure

Pressure is not only a force over a surface but also a energy per unit of volume!

$$ P = -\frac{\partial{E}}{\partial{V}}\Bigg|_S$$

This is equivalent (but more convinient) that the the usual definition. Indeed, to convince yourself, imagine a small infinitessimal box of size $\text{d}x$,$\text{d}y$ and $\text{d}z$. The pressure exerted on the surface $\mathcal{S}=\text{d}y\text{d}z$ is 

$$P=\frac{\text{d} \vec{F}\cdot \vec{n}}{\text{d} \mathcal{S}}= \frac{\text{d} \vec{F}\cdot \vec{n}}{\text{d} \mathcal{S}}=\frac{\text{d}\vec{F}\cdot \vec{n}}{ \text{d}y\text{d}z}= \frac{\text{d} \vec{F}\cdot \text{d}\vec{x}}{ \text{d}y\text{d}z\text{d}x}=\frac{\text{d} \vec{F}\cdot\text{d}\vec{x}}{\text{d}V} $$

. On the other hand, the energy transfered to a wall of the box due to the kinetic motion of the particle within the box, can be written $\text{d} E= - \delta W=-\vec{F}\cdot\text{d}\vec{x}$.

From which 

$$ P = \frac{\text{d} \vec{F}\cdot\text{d}\vec{x}}{\text{d}V} =-\frac{\partial{E}}{\partial{V}}\Bigg|_S$$

Hence, knowing only the expression of the energy $E_i$ of each microstate, we are able to derive all the thermodynamically relevant quantities (the pressure $P$, the temperature $T$, the mean energy $E$, the entropy $S$...) through the partition function $Z$, simply by asking for the maximization of the entropy.

## The three principles of thermodynamics in a statistical context

### First principle 

$$ U = \langle E \rangle = \sum_i p_i E_i $$ 

$$\text{d} U = \sum_i E_i\text{d}p_i + \sum_i p_i \text{d}E_i $$

### Second principle

### Third principle

## Taking the continuous limit

## Going further: recommended readings and watching

- [Statistical mechanics, theoretical minimum lectures - L. Susskind (2013)](https://theoreticalminimum.com/courses/statistical-mechanics/2013/spring)
- Statistical physics Part 1 and 2 - L.D. Landau and E.M. Lifshitz (1995) - (several editions available)