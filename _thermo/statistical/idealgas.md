---
layout: default
title: Ideal gas II
parent: thermo
nav_order: 1
---

# Classical ideal gas

### The energy of the particles

Let us now apply our understanding of phase space to rederive the ideal gas properties known from classical thermodynamics. Consider a box filled with $\mathcal{N}$ particles. These particles are free and non interacting. Furthermore, we assume for now that they have all the same mass i.e. that the gas has a single composition. Treating the particles classicaly in the context of Newtonian mechanics, we can write the energy of each particle as $mv^2/2 = \vec{p}^2/2m$ (see the [classical mechanics](../../_meca/Newton/Energy.md) lecture on this topic). In a three dimensional space $\vec{p}^2 = p_1^2 +p_2^2+p_3^2$, following the notations for the components of the momentum introduced in the previous lecture.  As such, the energy of a microstate, i.e. a particle configuration in the box associated to a point $\Gamma$ in phase space is the sum of each the energy of each individual particle, that is

$$E(\Gamma)=\frac{1}{2m}\sum_n^{\mathcal{N}}(\vec{p}^{(n)})^2$$

where we sum over all $\mathcal{N}$ independent (non-interacting) particles. Now, matching with the notation of the previous lecture, we realise that the energy of such a microstate is nothing else than what we called the Hamiltonian $E(\Gamma)=H(\Gamma)$. Furthermore, we can use our labelling of coordinates in phase space to write the sum over all particles and over all coordinates as a single sum:

$$H(\Gamma)= \frac{1}{2m}\sum_i^{\mathcal{3N}}p_i^2$$


### Partition function of the ideal gas

We recall from the previous lectures, that the partition function is a normalisation appearing in the expression for the probability of each microstate. It does not carry much physical intuition but it is a key quantity in order to derive the physical quantities of interest. We saw in the last lecture that, for case at hand of $\mathcal{N}$ classical particles, the partition function is written as an integral over the $6\mathcal{N}$ phase space:

$$Z=\int_{\Pi} e^{-\beta H(\Gamma)} \text{d}\Gamma $$

For the ideal gas, we simply replace the hamiltonian $H$ by the total kinetic energy of the non interacting particles, leading to:  

$$Z=\int_{\Pi} e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2} \text{d}\Gamma$$

Note here again that this is just a straightforward generalisation of the discrete "biased die" case $Z=\sum_i^N e^{-\beta E_i}$, where we replaced the sums over the $N$ possible microstates associated to the macrostate by a continuous integral over phase space, as discussed in the previous lecture. As a reminder, the integral here is done over all particle configurations, that is, over all of phase space. We can write

$$\text{d}\Gamma = \text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p  $$

It is possible to drastically simplify the previous integral to obtain the much nicer expression for $Z$:

$$ \boxed{Z=\left(\frac{e}{\rho}\right)^\mathcal{N}\left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}}$$

where $\rho = \mathcal{N}/V$ is the number density of particles.

To obtain it, we must first know the following property of **Gaussian integral**:

$$\int e^{-\alpha x^2} \text{d}x = \sqrt{\frac{\pi}{\alpha}} $$

for $\alpha\in \mathbb{R}$. This is a classic mathematical result (which hides a lot of subtelties in it). We will simply admit it here. You can have a look at any classical textbook for a proof.

We will also need the the so called **Stirling approximation**:

$$ \mathcal{N}! \sim \mathcal{N}^\mathcal{N} e^{-\mathcal{N}} $$

valid when $\mathcal{N} \to \infty$, which is typically our case for a gas made of a huge number of particles.

<details>
  <summary><strong>Proof</strong></summary>
  
Recall first that $\mathcal{N}! = 1\times 2 \times 3 ... \times \mathcal{N}$ and that for two number $a$ and $b$, $ln(a \times b)=\ln(a)+\ln(b)$. Then $\ln(\mathcal{N}!)= \ln(1\times 2 \times 3 ... \times N) = \ln(1)+ \ln(2) + ...+\ln(\mathcal{N})$. As such:

$$
\begin{aligned}
\ln(\mathcal{N}!) &= \sum_{x=1}^\mathcal{N} \ln(x)
\\ &\sim \int_1^\mathcal{N} \ln(x)\text{d}x \qquad (\mathcal{N}\to \infty) \\
&= [x \ln(x)-x ]_1^\mathcal{N} \\
&= \mathcal{N}\ln \mathcal{N} -\mathcal{N}
\end{aligned}
$$
</details>

We are now ready to demonstrate the above simple formula for $Z$, in the proof below.

<details>
  <summary><strong>Proof</strong></summary>

$$Z=\int_{\Pi} e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2} \text{d}\Gamma = \int \int e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2}  \text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p$$

Since there is no dependence in $x$ in the energy function, we can factorize the integral over space. As discussed in the previous lecture, it gives

$$\int \text{d}q^{3\mathcal{N}}=\frac{V^\mathcal{N}}{\mathcal{N}!}$$

where the $\mathcal{N}!$ is here to traduce the fact that particles are distinguishable and avoid double conting same particle configurations with different labeling.

We are then left with

$$Z=\frac{V^\mathcal{N}}{\mathcal{N}!}\int e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2} \text{d}^{3\mathcal{N}}p$$

Now, we have to compute the Gaussian integral. We notice that 

$$e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2} = \prod_i^{3\mathcal{N}} e^{-\frac{\beta}{2m}p_i^2}$$

so, the Gaussian integral becomes the product of $3\mathcal{N}$ times the same integral!

$$Z=\frac{V^\mathcal{N}}{\mathcal{N}!}\prod_{i}^{3\mathcal{N}}\int e^{-\frac{\beta}{2m}p_i^2} \text{d}p_i$$

each give a contribution of $\sqrt{\beta\pi/2m}=(\beta\pi/2m)^{1/2}$ from the Gaussian integral formula above. As such, we end up with:

$$Z=\frac{V^\mathcal{N}}{\mathcal{N}!}\left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}$$

Using Stirling's approximation, we can rewrite 

$$
\begin{align}
\frac{V^\mathcal{N}}{\mathcal{N}!} &\sim\frac{V^\mathcal{N}}{\mathcal{N}^\mathcal{N}e^{-\mathcal{N}}} \\
&=  \frac{e^{\mathcal{N}}V^\mathcal{N}}{\mathcal{N}^\mathcal{N}}\\
&= \left(\frac{e}{\rho}\right)^{\mathcal{N}}
\end{align}
$$

with $\rho= \mathcal{N}/V$. Replacing, we obtain the final result:

$$Z=\left(\frac{e}{\rho}\right)^{\mathcal{N}} \left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}$$

</details>

### Internal energy of the ideal gas

Now that we have an expression for $Z$, we are able to derive the physical quantities. For example, we are able to derive the mean energy, recalling from the previous lecture that

$$ \langle E \rangle  = -\frac{\partial \ln(Z)}{\partial \beta}$$

Now $\langle E \rangle$ is the mean energy of the gas as it evolves through phase space (macrostate). In a thermodynamical context, this quantity would be called the **internal energy** $U$ (as discussed already previously). So, we note $\langle E \rangle  = U$.

From $Z$ above, it is easy to derive:

$$ \boxed{U = \frac{3}{2}\mathcal{N}k_B T}$$

We thus recover the property that $U=U(T)$ for an ideal gas, known as the first **Joules' law** in classical thermodynamics. 

<details>
 <summary><strong>Proof</strong></summary>

Start by computing $\ln(Z)$:

$$\begin{aligned}
\ln(Z)&=\ln\left(\left(\frac{e}{\rho}\right)^\mathcal{N}\left(\frac{2m\pi}{\beta}\right)^{\frac{3\mathcal{N}}{2}}\right) \\
&= \mathcal{N}\ln\left(\frac{e}{\rho}\right)+\frac{3\mathcal{\mathcal{N}}}{2}\left(\ln(2m\pi)-\ln(\beta)\right)\\
\end{aligned}
$$

Such that:

$$
\begin{aligned}
U&=-\frac{\partial \ln(Z)}{\partial \beta}\\
&= -\frac{3\mathcal{N}}{2}\frac{\partial}{\partial \beta}\left(-\ln(\beta)\right) \\
&= \frac{3\mathcal{N}}{2} \frac{1}{\beta}\\
&= \frac{3\mathcal{N}}{2} k_B T
\end{aligned}
$$

where we re-introduced the units through $\beta=1/(k_BT)$.

</details>

### Entropy of the ideal gas

We can compute the entropy of the gas, recalling from the previous lecture that:

$$S =  \beta U + \ln(Z)$$

we are able to derive easily from the previous expressions:

$$\boxed{S = \mathcal{N}\left(\frac{5}{2} - \ln(\rho) + \frac{3}{2}\ln(2\pi mk_B T)\right)}$$

<details>
 <summary><strong>Proof</strong></summary>

From the proof of the expression for $U$, we already computed both

$$\begin{aligned}
\ln(Z) = \mathcal{N}\ln\left(\frac{e}{\rho}\right)+\frac{3\mathcal{N}}{2}\left(\ln(2m\pi)-\ln(\beta)\right)\\
\end{aligned}
$$

and 

$$ 
U = \frac{3}{2}\mathcal{N}k_BT
$$

Puting everything together, we obtain

$$
\begin{align}S &= \frac{3}{2}\mathcal{N} +  \mathcal{N}\ln\left(\frac{e}{\rho}\right)+\frac{3\mathcal{N}}{2}\left(\ln(2m\pi)+\ln(k_B T)\right)\\
&= \frac{3}{2}\mathcal{N} + \mathcal{N} - \mathcal{N}\ln(\rho) + \frac{3}{2}\mathcal{N}\ln(2m\pi) + \frac{3}{2}\mathcal{N}\ln(k_B T)\\
&= \mathcal{N}\left(\frac{3}{2} + 1 - \ln(\rho) + \ln(2\pi mk_B T)\right) \\
&= \mathcal{N}\left(\frac{5}{2} - \ln(\rho) + \frac{3}{2}\ln(2\pi mk_B T)\right)
\end{align}
$$

</details>

### Pressure of the ideal gas

Finally, we can also compute the pressure of the macrostate from the expression of $Z$, recalling that:

$$\boxed{
P=\frac{1}{\beta}\frac{\partial \ln(Z)}{\partial V}\Bigg|_{T}
}
$$

using the previous expression for $Z$, we obtain:

$$P = \rho k_B T = \frac{\mathcal{N}}{V}k_B T$$

<details>
 <summary><strong>Proof</strong></summary>
We know that

$$\begin{aligned}
\ln(Z) &= \mathcal{N}\ln\left(\frac{e}{\rho}\right)+\frac{3\mathcal{N}}{2}\left(\ln(2m\pi)-\ln(\beta)\right)\\
&= \mathcal{N} \left( 1 - \ln(\mathcal{N}) + \ln(V)\right) + \text{const}(T)
\end{aligned}
$$

From which: 

$$
\frac{\partial \ln(Z)}{\partial V}\Bigg|_{T}= \frac{\mathcal{N}}{V} = \rho
$$

and then 

$$ P = \rho \beta =\rho k_B T  $$
</details>

which, might look familiar. Indeed, introducing the number of particles in mole $n= N_A\mathcal{N}$ and the ideal gas constant $\mathcal{R}= k_B/ N_A$, we find:

$$\boxed{PV = n \mathcal{R}T}$$

that is, we derived back the ideal gas law! As such, only by assuming that particles were not interacting i.e. that the energy of a microstate is given by the sum of the kinetic energy of each particle $E(\Gamma)=\sum^{\mathcal{N}} E_c^{(n)}$, using the Newtonian expressions for $E_c$ and asking for the entropy to be maximal, we derived back one of the most important relation of classical thermodynamics.

### The Maxwell-Boltzmann speed distribution of speed

In the previous lecture, we learned to think in phase space. We saw that the concept of discrete probability of a microstate $p_i$ can be generalised to the one of probability density $\rho(\Gamma)$ defined on each point of phase space (i.e. for each configuration/microstate).

We saw that, just like in the discrete case, $\rho$ could be inffered from a maximization of the entropy. In the case of the ideal gas, we obtain:

$$\rho(\Gamma) = \frac{1}{Z}e^{-\frac{\beta m}{2}\sum^{3\mathcal{N}_i p^2_i}}$$
