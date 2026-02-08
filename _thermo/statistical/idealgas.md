---
layout: default
title: Ideal gas II
parent: thermo
nav_order: 1
---

# Classical ideal gas

### The energy of the particles

Let us now apply our understanding of phase space to rederive the ideal gas properties known from classical thermodynamics, which we discussed extensively [here](../thermo/idealgas.md). Consider a box of volume $V$ filled with $\mathcal{N}$ particles. These particles are free and non interacting. Furthermore, we assume for now that they have all the same mass i.e. that the gas has a single composition. Treating the particles classicaly in the context of Newtonian mechanics, we can write the energy of each particle as $mv^2/2 = \vec{p}^2/2m$ (see the [classical mechanics](../../_meca/Newton/Energy.md) lecture on this topic). In a three dimensional space $\vec{p}^2 = p_1^2 +p_2^2+p_3^2$, following the notations for the components of the momentum introduced in the previous lecture.  As such, the energy of a microstate, i.e. a particle configuration in the box associated to a point $\Gamma$ in phase space is the sum of each the energy of each individual particle, that is

$$E(\Gamma)=\frac{1}{2m}\sum_n^{\mathcal{N}}(\vec{p}^{(n)})^2$$

where we sum over all $\mathcal{N}$ independent (non-interacting) particles. Now, matching with the notation of the previous lecture, we realise that the energy of such a microstate is nothing else than what we called the Hamiltonian $E(\Gamma)=H(\Gamma)$. Furthermore, we can use our labelling of coordinates in phase space to write the sum over all particles and over all coordinates as a single sum:

$$H(\Gamma)= \frac{1}{2m}\sum_i^{\mathcal{3N}}p_i^2$$


### Partition function of the ideal gas

We recall from the previous lectures, that the partition function is a normalisation appearing in the expression for the probability of each microstate. It does not carry much physical intuition but it is a key quantity in order to derive the physical quantities of interest. We saw in the last lecture that, for case at hand of $\mathcal{N}$ classical particles, the partition function is written as an integral over the $6\mathcal{N}$ phase space:

$$Z=\int_{\Pi} e^{-\beta H(\Gamma)} \text{d}\Gamma $$

For the ideal gas, we simply replace the hamiltonian $H$ by the total kinetic energy of the non interacting particles, leading to:  

$$Z=\int_{\Pi} e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2} \text{d}\Gamma$$

Note here again that this is just a straightforward generalisation of the discrete "biased die" case $Z=\sum_i^N e^{-\beta E_i}$, where we replaced the sums over the $N$ possible microstates associated to the macrostate by a continuous integral over phase space, as discussed in the previous lecture. As a reminder, the integral here is done over all particle configurations, that is, over all of phase space. We can write

$$\text{d}\Gamma = \frac{\text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p}{\mathcal{N}!}  $$

where we added the $1/\mathcal{N}!$ in the Liouville measure in order to account for indistinguishable particles as discussed in the previous lecture.

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

$$Z=\int_{\Pi} e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2} \text{d}\Gamma = \int \int e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2}  \frac{\text{d}^{3\mathcal{N}}q\, \text{d}^{3\mathcal{N}}p}{\mathcal{N}!}$$

Since there is no dependence in $q$ in the energy function, we can factorize the integral over space. 

$$Z= \frac{1}{\mathcal{N}!}\int \text{d}^{3\mathcal{N}} q \int e^{-\frac{\beta}{2m}\sum_i^{\mathcal{3N}}p_i^2}   \text{d}^{3\mathcal{N}}p$$

Let's compute this first integral.
For a single particle, contained (and thus forced to move) within a container of gas of volume $V$, we expect:

$$\int_{\Pi} \text{d}^{3}q = \iiint\text{d}q_1\text{d}q_2\text{d}q_3 = V$$

For $\mathcal{N}$ particles, we have 

$$
\begin{align}
\int_{\Pi} \text{d}^{3\mathcal{N}}q &= \iiint \text{d}q_1\text{d}q_2\text{d}q_3\text{d}q_4\text{d}q_5\text{d}q_6 ... \text{d}q_{3\mathcal{N}-2}\text{d}q_{3\mathcal{N}-1}\text{d}q_{3\mathcal{N}}\\
 &=\iiint \text{d}q_1\text{d}q_2\text{d}q_3\iiint\text{d}q_4\text{d}q_5\text{d}q_6 ...\iiint \text{d}q_{3\mathcal{N}-2}\text{d}q_{3\mathcal{N}-1}\text{d}q_{3\mathcal{N}}
\end{align}
$$

where we should keep in mind that $q_1,q_2,q_3$ are the three coordinates of the first particle, $q_4,q_5,q_6$ are the three coordinates of the second particle and so on until the particle $\mathcal{N}$. As such, each of these integral will give again $V$, such that we will obtain $\mathcal{N}$ products of $V$. As such, we obtain

$$ \int_{\Pi} \text{d}^{3\mathcal{N}}q= V^{\mathcal{N}}$$

Our integral for the partition function thus becomes:

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

In the previous lecture, we learned to think in phase space. We saw that the concept of discrete probability of a microstate $p_i$ can be generalised to the one of probability density $\rho(\Gamma)$ defined on each point of phase space (i.e. for each configuration/microstate). We saw that, just like in the discrete case, $\rho$ could be inffered from a maximization of the entropy to be $\rho = \int e^{-\beta H}/Z\text{d}\Gamma$. 
In the case of the ideal gas, reusing the expressions we derived above, this gives:

$$\rho(\Gamma) = \left(\frac{\rho}{e}\right)^{\mathcal{N}}\left(\frac{1}{2m\pi k_BT}\right)^{\frac{3\mathcal{N}}{2}}e^{-\frac{\beta}{2m}\sum^{3\mathcal{N}}_i p^2_i}$$

As a reminder, $\rho$ allows to compute the probability $\text{d}p=\rho(\Gamma)\text{d}\Gamma$ that the particle configuration within the box is located in a given infinitesimal region of phase-space.

Now, we can ask ourselves about the probability density for a single particle of the gas to have a given velocity $v=\sqrt{v_1^2+v_2^2+v^2_3}$, where $v_i = p_i/m$. 

First, starting from $\rho(\Gamma)$, it is possible to show that the probability distribution for a particle to have the velocity vector $\vec{v}$ is:

$$\rho(\vec{v})= \left(\frac{m}{2\pi k_B T}\right)^{\frac{3}{2}}e^{-\frac{m\vec{v}^2}{2k_B T}}$$

with $\rho(\vec{v})= \rho(v_1,v_2,v_3)$.

<details>
 <summary><strong>Proof</strong></summary>

Before we go further, we should remind ourselves about **marginalisation**. If a probability density depends on multiple variables $\rho(x,y,...,z)$, it is possible to infer a probability density for a single variable $\rho(x)$ by integrating over all the other variables (all but $x$):

$$ \rho(x)= \int...\int\rho(x,y,z,.,z)\text{d}y...\text{d}z$$

$\rho(x)$ is called a marginal probability distribution.

We can use this trick here to derive the probability distribution of momentum associated to a single particle by marginalizing over the momenta and positions of all the other particles. We will end up with

$$\rho(\vec{v})= C e^{-\frac{\beta}{2m}\sum_i^3 p_i^2}$$

where $C$ is a gigantic integral of $\rho(\Gamma)$ over all dimensions of phase space but the momentum of the first particle, that is $p_1,p_2$ and $p_3$. Instead of suffering and computing $C$ explicitely (try to do it!), we can deduce it by reminding ourselves that $\rho(\vec{p})$ should be a probability distribution, and thus be normalized to one:

$$
\begin{align}
\int  C e^{-\frac{\beta}{2m}\sum_i^3 p_i^2} \text{d}p_i &= 1\\
 \left(\int e^{-\frac{\beta}{2m} p_1^2} \text{d}p_1\right)^3 &= 1/C \\
 \left(\sqrt{\frac{2m\pi}{\beta} }\right)^3 &= 1/C \\
 \left(\frac{1}{2\pi m k_B T}\right)^{3/2} &=C
\end{align}
$$

A similar result would have been obtained by considering a gas made of a single particle, which would give us the exact same expressions as for our total gas (without the Stirling approximation) with $\mathcal{N}=1$:

$$\rho(q_1,q_2,q_3,p_1,p_2,p_3) = \frac{1}{V} \left(\frac{1}{2m\pi k_B T}\right)^{3/2} e^{- \frac{\beta}{2m}\sum_i^3p_i^2}$$

and then marginalizing over position in order to get the probability for $\vec{p}$ only:

$$ 
\begin{align}
\rho(p_1,p_2,p_3)&= \iiint\rho(q_1,q_2,q_3,p_1,p_2,p_3) \text{d}^3q\\
& = \frac{1}{V}\iiint\text{d}^3q \left(\frac{1}{2m\pi k_B T}\right)^{3/2} e^{- \frac{\beta}{2m}\sum_i^3p_i^2}\\
&= \left(\frac{1}{2m\pi k_B T}\right)^{3/2} e^{- \frac{\beta}{2m}\sum_i^3p_i^2}
\end{align}
$$

Note that, even with a more complex spatial integral (like a potential in the Hamiltonian, which will be discussed in the next class), we will obtain the same result, as long as this potential depends only on position and not on momentum. This result is thus much more general than the case of the ideal gas only.

Once we have $\rho(\vec{p})$, we can easily obtain $\rho(\vec{v})$ by reminding ourselves how to go from a probability distribution of a variable to another.

The key is that the probability that the system is contained within a volume should be the same:

$$\text{d}p= \rho(p_1,p_2,p_3)\text{d}p_1\text{d}p_2\text{d}p_3=\rho(v_1,v_2,v_3)\text{d}v_1\text{d}v_2\text{d}v_3 $$

From which:

$$\rho(v_1,v_2,v_3) = \rho(p_1,p_2,p_3)\frac{\text{d}p_1}{\text{d}v_1}\frac{\text{d}p_2}{\text{d}v_2}\frac{\text{d}p_3}{\text{d}v_3}=m^3 \rho(p_1,p_2,p_3)$$

From which we get:

$$\rho(\vec{v})= \left(\frac{m}{2\pi k_B T}\right)^{\frac{3}{2}}e^{-\frac{m\vec{v}^2}{2k_B T}}$$

</details>

From this expression, we can find that the mean velocity vector of a particle in the gas is zero, traducing isotropy (no prefered direction and hence no "group velocity"):

$$\boxed{\langle \vec{v} \rangle =0 }$$

<details>
 <summary><strong>Proof</strong></summary>

The mean velocity vector is:

$$
\langle \vec{v} \rangle = \int_{\mathbb{R}^3} \vec{v} \, \rho(\vec{v}) \, \text{d}^3 v
$$

Since $f(\vec{v})$ is isotropic (depends only on $|\vec{v}|$) and each component $v_i$ is an odd function:

$$
\int_{-\infty}^{\infty} v_i \, e^{- m v_i^2 / 2 k_B T} \, \text{d} v_i = 0
$$

because the integrand is odd. By symmetry, this holds for all components \(i = x, y, z\). Therefore:

$$
\boxed{\langle \vec{v} \rangle = 0}
$$


</details>

We can translate the probability distribution on $\vec{v}$ into a probability on the modulus of the velocity $v$, to obtain:

$$\boxed{\rho(v)= \left(\frac{m}{2\pi k_B T}\right)^{\frac{3}{2}}4\pi v^2 e^{-\frac{mv^2}{2k_B T}}}$$

This curve is known as a **Maxwellian curve** and give us the probability distribution for the velocity of a single particle of the gas depending on the temperature.

<details>
 <summary><strong>Proof</strong></summary>

Start from the 3D Maxwell-Boltzmann velocity distribution:

$$
\rho(\vec{v}) = \left( \frac{m}{2 \pi k_B T} \right)^{3/2} \exp\Big(-\frac{m |\vec{v}|^2}{2 k_B T}\Big)
$$

The probability density for \(v = |\vec{v}|\) is obtained by integrating over the angular directions when expressing the velocity vector in spherical coordinates:

$$
\rho(v) = \int_{|\vec{v}|=v} \rho(\vec{v}) \, \sin(\theta)\text{d}\theta \text{d}\phi \, v^2 = \rho(\vec{v}) \cdot 4 \pi v^2
$$

Substituting \( \rho(\vec{v}) \):

$$
\rho(v) = \left( \frac{m}{2 \pi k_B T} \right)^{3/2} 4 \pi v^2 \exp\Big(-\frac{m v^2}{2 k_B T}\Big)
$$

\[
\boxed{\rho(v) = \left(\frac{m}{2\pi k_B T}\right)^{3/2} 4\pi v^2 e^{- \frac{m v^2}{2 k_B T}}}
\]


</details>

The Maxwellian is plotted below for different temperatures in the case of N$_2$ molecules, which are the main constituent of earth's atmosphere. The flattening of the curve with $T$ is symptomatic of the increase of the entropy, as discussed when we presented the [canonical ensemble](../statistical/canonical.md). 

![image](../images/Maxwell_Boltzmann.png){: width="100%"}
*Example of probability density for the speed of a single particle in the gas $\rho(v)$ associated with different temperatures. Computed with [this code](../codes/Maxwell_Boltzmann.py)*.


We also notice that, for usual room temperature ($\sim$ 300 K), we have a peak of the speed distribution around $\sim$ 300 m/s, which is close to the sound velocity. The peak of the curve can be recovered using the expression for the mean velocity:

$$ \boxed{\langle v \rangle = \sqrt{\frac{8k_B T}{\pi m}}}$$

<details>
 <summary><strong>Proof</strong></summary>

The Maxwell-Boltzmann speed distribution is:

$$
\rho(v) = 4 \pi \left( \frac{m}{2 \pi k_B T} \right)^{3/2} v^2 \exp\left(-\frac{m v^2}{2 k_B T}\right)
$$

The mean speed is:

$$
\langle v \rangle = \int_0^\infty v \rho(v) \, \text{d} v = 4 \pi \left( \frac{m}{2 \pi k_B T} \right)^{3/2} \int_0^\infty v^3 e^{-m v^2 / 2 k_B T} \, \text{d} v
$$

Using the substitution \(x = \frac{m v^2}{2 k_B T}\), \(dx = \frac{m v}{k_B T} \text{d} v\), we get:

$$
\int_0^\infty v^3 e^{-m v^2 / 2 k_B T} \text{d} v = \frac{2 (k_B T)^2}{m^2} \int_0^\infty x e^{-x} dx = \frac{2 (k_B T)^2}{m^2} \cdot 1!
$$

where we recognized the $\Gamma$ function:

$$ \Gamma(t) = \int_0^\infty x^{t-1}e^{-x}\text{d}x$$


for $t=2$, $\Gamma(2)=1$ (whish we shall admit here).

Multiplying by the prefactor:

$$
\langle v \rangle = 4 \pi \left( \frac{m}{2 \pi k_B T} \right)^{3/2} \frac{2 (k_B T)^2}{m^2} = \sqrt{\frac{8 k_B T}{\pi m}}
$$


</details>

As discussed in one the proof for $\rho(\vec{v})$, this result is much more general than the case of the ideal gas, and would be true for any classical gas with interactions dependent only on the position (because the integrals over $q$ disapear when marginalizing, in the proofs above).

