---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---
$$ 
\newcommand{\bra}[1]{\langle#1|}
\newcommand{\ket}[1]{|#1\rangle} 
\newcommand{\braket}[2]{ \langle #1 | #2 \rangle} 
$$

# Statistical physics in general

## Statistical physics, microstates and macrostates

# Maximizing the entropy

Let $i$ label a discrete number of $N$ possible states for a system. Let $p_i$ be the probability for the system to be in the state $i$, such that $\sum_i p_i = 1$. We define the entropy of the system $S$ as:

$$
\boxed{
S = -\sum_i p_i\ln{p_i} = \langle \ln(p_i)\rangle}
$$

For a system where all states are equiprobable, $p_i=1/N$ and:

$$
S = -\frac{1}{N}\sum_i^N\ln\left(\frac{1}{N}\right)= \ln(N)
$$

If there is a single state that is perfectly known, the entropy is then $N=1$ and $S=0$.


# Classical statistics up to the ideal gas

### Derivation of the probabilities of maximal entropy in the canonical ensemble ($N$ fixed).

Let's consider a system of $N$ distinguishable interacting particles in thermal equilibrium with a eat bath. Let's label by $i$ the possible energy states that a subsystem can be in. To each state is associated a energy $E_i$. Let $n_i$ be the occupation number that is the number of particles that can be with energy $E_i$ at a given time. In the large $N$ limit, we have:

$$
\sum_i n_i = N
$$

The probability of the system to be in the state $i$ is:

$$
p_i = \frac{n_i}{N}
$$

Leading naturally from the above equation to

$$
\sum_i p_i = \sum_i \frac{n_i}{N} = 1
$$


The average energy of a particle is:

$$
\langle E \rangle  = \sum_i p_i E_i = \sum_i \frac{n_i}{N} E_i
$$


The number of ways to rearange the $N$ particles into the possible energy states with occupation numbers $n_i$ is given by:

$$
C = \frac{N!}{\prod_i n_i!}
$$

Maximizing $C$ will give us the most probable configuration of the $n_i$. It can be shown that this maximum is very sharp, making other configurations almost impossible.

If $N$ and $n_i \to \infty$, we can use the *Stirling approximation*:

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

This approximation allows us to calculate:

$$ 
\ln(C)= NS
$$

<details>
  <summary>Proof</summary>

$$
\begin{aligned}
\ln(C)&= N\ln(N)- \sum_i n_i \ln(n_i)\\
&= Nln(N) - \sum_i p_i N \ln(p_iN)\\
& =  Nln(N) - \sum_i p_i N(\ln(p_i)+ \ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i)+ \sum_i N p_i\ln(N))\\
&= Nln(N) - \sum_i N p_i\ln(p_i)+ - N\ln(N))\\
& = N S
\end{aligned}
$$
</details>

Maximizing $C$ is equivalent to maximizing $S$ with the following constraints:

$$
\begin{cases}
\begin{aligned}
&\sum_i p_i E_i &= \langle E \rangle \\
& \sum_i p_i  &= 1
\end{aligned}
\end{cases}
$$

<details>
  <summary>Lagrange multipliers</summary>
  
</details>

Maximizing $S$... Lagrange multipliers
giving us the probability for a single particle to be in the state of energy $E_i$:

$$
\boxed{p_i = \frac{1}{Z}e^{-\beta E_i}}
$$

With $Z$ the *partition function*:

$$
Z := e^{1+\alpha}
$$

It can be expressed by asking for the normalization of probabilities:

$$
\sum_i p_i = \sum_i \frac{1}{Z}e^{-\beta E_i} =1 
$$

Leading to:

$$
\boxed{Z = \sum_ie^{-\beta E_i}}
$$

The energy of the system can then be re-expressed from $Z$ as

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

We can now express $\beta$ with respect to the temperature. To do so, we define the temperature as the change of energy associated with a change of entropy:

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


### On the definition of temperature

The temperature is above by Eq.\ref{eq:defTemp}.

Why is it a good definition:
- direction of heatflows
- broadening of $p(E)$ with increasing $\langle E \rangle$

### Defining Pressure

Pressure is not only a force over a surface but also a energy per unit of volume!

$$ P = \frac{\partial{E}}{\partial{V}}\Bigg|_S$$

Hence, knowing only the expression of the energy $E_i$ of each microstate, we are able to derive all the thermodynamically relevant quantities (the pressure $P$, the temperature $T$, the mean energy $E$, the entropy $S$...) through the partition function $Z$, simply by asking for the maximization of the entropy.
