---
layout: default
title: Classical thermo
parent: thermo
nav_order: 1
---

# Seeing classical thermodynamics emerging from the statistics

We made a lot of progress in the previous lectures, by understanding how the maximisation of entropy can help us finding the probability distribution. However, this first part of the lectures might seems very abstract and for a good reason: it is! Statistical mechanics is not an easy subject.
Let us now try to reconnect, gradually, with the language of classical thermodynamics and emmerge out of abstraction.

### A little summary of where we are

As it does not hurt to repeat oneself, let's start with a big picture summary of where we stand. We considered a system like a box containing many particles as moving through time between different configurations of energy $E_i$ and with probability $p_i$. For now we assumed that these possibilities (microstates) were discrete. As such, the system can be thought as a die being rolled over and over again and showing randomly one face or another.

We convinced ourselves that a good way to evaluate the $p_i$ of each microstate (particle configuration) was to maximize the entropy function

$$S=-\sum_i p_i\ln(p_i)$$

quantifying our ignorance about the details of the system. Doing so can be done under some constraints. For example we can ask that the mean energy of the system is forced by a thermostat to have a value of $\langle E \rangle$. Adding these constraints is similar to looking for the probabilities of a biased die, which have a specific mean value for the number it displays.
The maximisation of entropy under the constraints of mean energy leads to 

$$p_i = \frac{1}{Z}e^{- \frac{E_i}{T}}$$

where $Z=\sum_i e^{E_i/T}$ is the partition function and
where the temperature $T$ tells us how much the mean energy has to change if we want to increase the entropy of the $p_i$ distribution.

We found that $Z$ plays a crucial role in recovering the physical quantities that one can observe about the system, for example:

$$\langle E \rangle = -\frac{\partial \ln(Z)}{\partial \beta}  $$

and

$$P = \frac{1}{\beta}\frac{\partial \ln(Z)}{\partial V}\Bigg|_T$$

In reading all this, one should keep in mind that:

- Entropy maximisation here is not yet related to 2nd principle. It is a way to derive $p_i$, coming from information theory. If you are skeptical about this, we will look much later at at other ways to derive $p_i$ without using $S$.
- We assumed a discrete set of accessible energy level which is of course a simplification. We will gradually go beyond this simplification in the next lectures. However, the logic and the formula we derive above will remain extremely important.

### Restoring physical units

Up to this point, we have deliberately ignored physical units. This implicitly corresponds to working in natural units where the Boltzmann constant is set to unity, $k_B = 1$.

The Boltzmann constant is defined as
$$
k_B = 1.380\,649 \times 10^{-23}\ \mathrm{J\,K^{-1}},
$$
and acts as a conversion factor between temperature, measured in kelvin, and energy, measured in joules. Thermal energies (per particle and degree of freedom)are therefore typically written as (see our classical thermodynamics class on [ideal gas](../thermo/idealgas.md))
$$
E_{\mathrm{th}} \sim k_B T.
$$
Because $k_B$ is numerically very small, the energy associated with thermal excitation is usually a small quantity when expressed in joules.

The constant $k_B$ also fixes the physical units of entropy. In statistical mechanics, entropy is first introduced as a dimensionless quantity derived from a probability distribution,

$$
S = - \sum_i p_i \ln p_i
$$

The corresponding thermodynamic entropy is obtained by

$$
S_{\mathrm{th}} = k_B\, S,
$$

which has units of $\mathrm{J\,K^{-1}}$. This is the entropy that appears in classical thermodynamics, for instance in the second law written (for reversible processes) as

$$
\mathrm{d}S_{\mathrm{th}} = \frac{\delta Q_{\mathrm{rev}}}{T}.
$$

Another ubiquitous appearance of $k_B$ is in the Lagrange multiplier $\beta$ associated with the energy constraint in equilibrium statistical mechanics:

$$\beta = \frac{1}{k_B T}.$$

In what follows, we will freely alternate between expressions written in thermodynamic units and those written in units where $k_B = 1$. With the relations summarized above, it should always be straightforward to reinstate physical units when needed.

## Zeroth principle and equilibrium

The notion of **thermal equilibrium** was a bit hidden so far, and we should be explicit on how it appears in our model. 
In this class, we are now exclusively concerned with systems in thermal equilibrium. The fact that we can define unambigiously a single temperature $T$ to our system is a clear sign that we are in such a situation here.
The assumption of thermal equilbrium is hidden behind the fact that the probability distribution $p_i$ does not change with time. The system moves around its microstates, but the probability of each microstate always remain the same. After a long enough time, it will have explored all of it's accessible microstates, allowing us to assume ergodicity (see supplement on the mean value in this [lecture](./entropy.md)). 
When considering transformations (as in the following section), we always consider transition from one state of equilibrium to another one.

Quantities such as $n$,$V$, $P$ and $T$ were state variables in classical thermodynamics, that is quantities that could be measured, defining the state of the system. In a statistical context, they are better understood as mean quantities caracterising the thermal equilibrium, emmerging from the averaged and uniform underlying microscopic properties (e.g. mean momentum for $P$ an mean energy for $T$), as well as quantities characterizing how the system would transform if he went from one state of equilibrium to another ($P$ and $T$ characterizing changes of $\langle E \rangle$ and of the underlying $p_i$ if $V$ or $S$ change).

## Energy conservation and the first principle 

The mean energy $\langle E \rangle$ of the system, is nothing else than the internal energy $U$ in the context of classical thermodynamics. As such, and from now on, we will use the two notations interchangably. As a reminder:

$$ U = \langle E \rangle = \sum_i p_i E_i $$ 

Now, it is instructive to look at the differential of $U$:

$$\text{d} U = \sum_i E_i\text{d}p_i + \sum_i p_i \text{d}E_i $$

### Heat

We see a first term corresponding to how the mean energy change if the probability associated to each microstate were to change, keeping each energy level fixed. This correspond to what we define as a heat injection:

$$\boxed{\delta Q = \sum_i E_i\text{d}p_i }$$

Indeed, if heat is injected, the possible microstates remain the same, but the ones of higher energy become more populated. This means shifting the probability distribution towards higher entropy (and energy) equilibrium distributions on the figure plotted in the [previous lecture](./canonical.md).

We can convince ourselves -- using only our most primitive concepts -- that this transformation correspond indeed to the classical definition of heat:

$$\sum_i E_i\text{d}p_i =  T\text{d}S$$

<details>
  <summary><strong>Proof</strong></summary>

Recall that


$$p_i= \frac{e^{-\beta E_i}}{Z}$$ 

and hence:

$$E_i = -\ln(Zp_i)/\beta = -(\ln(Z)+\ln(p_i))/\beta$$

Furthermore

$$\sum_i p_i =1$$

implies 

$$\sum_i \text{d}p_i = 0$$ 

and as such (remember that $\text{d}(\ln(x))= \text{d}x/x$):

$$
\begin{align}
\text{d}S &= -\text{d}\left(\sum_i p_i \ln(p_i)\right)\\
&=-\sum_i \ln(p_i)\text{d}p_i - \sum_i p_i \text{d}p_i/p_i\\
&= -\sum_i \ln(p_i)\text{d}p_i - \sum_i\text{d}p_i\\
&=  -\sum_i \ln(p_i)\text{d}p_i
\end{align}
$$

As such:

$$
\begin{align}
\delta Q &=\sum_i E_i\text{d}p_i\\
&= -\frac{1}{\beta}\sum_i(\ln(Z)+\ln(p_i))\text{d}p_i\\
&= -\frac{\ln(Z)}{\beta}\sum_i \text{d}p_i - \sum_i \frac{\ln(p_i)}{\beta}\text{d}p_i\\
&= T \text{d}S
\end{align}
$$ 

Note that, by restablishing the units as indicated previously $\beta = 1/(k_B T)$ and $S_{\rm th}=k_B S$, such that boltzmann constants simplify!
</details>

That is, a heat injection always comes with an increase in entropy of the system of 

$$\boxed{\text{d}S = \frac{\delta Q}{T}}$$

as discussed in classical thermodynamics. Let us repeat again that this increase in $S$ comes from the broadening of the probability distribution by populating the higher energy microstates, associated with a larger value of $U=\langle E \rangle$ (from the first principle equation).

### Work

The second term in the transformation of $U$ is corresponding to how the mean energy change if the energy level associated to each microstate were to change, keeping the probabilities fixed. This correspond to what we define as work:

$$\boxed{\delta W =  \sum_i p_i \text{d}E_i}$$

we note that this definition of work is very general and implies **any phenomenon** which would change the value of the energy of the microstates $E_i$ (as a e.g. magnetic field). 

In the case where a force is applied that change the volume of the system (compression/decompression) by an infinitesimal amount $\text{d}V$, we can show similarly using our basic principles that:

$$\boxed{\delta W = - P \text{d}V}$$


<details>
  <summary><strong>Proof</strong></summary>

For a change of volume, the mean energy $U$ changes as 

$$
\begin{align}
\frac{\text{d}U}{\text{d}V} &=\frac{\text{d}(\sum_i p_i E_i)}{\text{d}V}    \\
&= \sum_i p_i \frac{\text{d}E_i}{\text{d} V} + \sum_i E_i \frac{\text{d}p_i}{\text{d} V}
\end{align}
$$

The second term is clearly heat generated by the change of volume, which we know will change the entropy. The second term however, is at constant entropy (since $\text{d}S$ only depends on $\text{d}p_i$ and not on $E_i$ from the previous proof on heat). Now, recall the definition of the pressure:

$$P = -\frac{\partial U}{\partial V}\Bigg|_{S} $$

and hence 

$$P = -\sum_i p_i \frac{\text{d}E_i}{\text{d} V} $$

The work can then be written as:

$$
\begin{align}
\delta W &= \sum_i p_i \text{d}E_i\\
&= \sum_i p_i \frac{\partial E_i}{\partial V} \text{d}V \\
&= - P \text{d} V
\end{align}
$$

</details>


### On the generality of the concepts used so far

Before concluding this class, let us note that so far, we made very few assumptions about the physical nature of our system, simply assuming discrete accessible microstates and using the familiar picture of a "box of gas" and the analogy with a die that can be biased or not. This implies that all the notions we are using now (temperature, heat, work ...) are much more general than what is usually considered in classical thermodynamics, and can be applied to a great variety of physical systems.
