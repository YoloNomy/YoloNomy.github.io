---
layout: default
title: Generating function
parent: thermo
nav_order: 1
---

# Bonus: A new take on $Z$ and ensembles

In this "bonus" lecture, we want to further reflect on $Z$, its role and propose alternative ways to derive the ensembles of statistical physics without calling for the maximisation of entropy.
This lecture is a bit technical (but enlightening!), and might be skipped on a first go through the class.
The statements in this lecture are very general and apply to both the discrete, the continuous and the quantum case, as you can convince yourself easily.

# Other derivations of the ensembles

It is sometimes stated that the
**fundamental postulate** of statistical physics, is that all accessible microstates of an isolated system at equilibrium are equiprobable, which is a result we found for the microcanonical ensemble. 
If multiple microstates $g(E_i)$ amongst the total number of $N$ possible microstates are associated with the same energy value, the probabily $p_i$ for the system to have an energy $E_i$ is:

$$p_i =  \frac{g(E_i)}{N}$$

Consider a large thermostat $\mathcal{S}$ and a smaller subsystem $\mathcal{s}$. The total system made by the large thermostat and the small subsystem have a total energy $E_{\rm tot}$. 
The small subsystem can be in various energy levels $E_i$ with degeneracy $g^{s}(E_i)$. 

$$g^{s}(E_i)g^{\mathcal{S}}_i(E_{\rm tot}-E_i)$$


$$p_i = \frac{g^{s}(E_i)g^{\mathcal{S}}_i(E_{\rm tot}-E_i)}{\sum_i g^{s}(E_i)g^{\mathcal{S}}_i(E_{\rm tot}-E_i)}$$

For [the continuous case](./phasespace.md), we saw that the degeneracy should be replaced by $\Omega(E)$ which are the volumes occupied in phase-space. Otherwise, the proof goes identically. This proof is often presented in the litterature as an alternative to the entropy maximisation. 

# Generating functions and $Z$

Now that we saw some fundamental principle on statistical physics, we can try to go a little deeper. The aim of this lecture is to get better insight on what is the partition function $Z$ and why it seems to be such a powerful tool. To do so, we will look at slightly advanced concepts of statistics: moments, cumulents and their generating functions.

## Moments

Moments vs centered moments

### Mean

$$ \langle X \rangle$$

Properties: linearity etc

$$ \langle aX + bY \rangle=  a\langle X \rangle + b\langle Y \rangle $$


$$ \langle XY \rangle =  \langle X \rangle \langle Y \rangle$$

<details>
  <summary><strong>Prooves:</strong> </summary>

</details>


### Variance


## A strange idea: putting moments in a polynomial 

$$p(x) = \mu_0 + \mu_1 x + \mu_2 x^2 + ... = \sum_i \mu_i x^i$$

$$Z(\beta) = \mu_0 - \mu_1 \beta + \frac{\mu_2}{2} \beta^2 -\frac{\mu_3}{6}\beta^3 + ... = \sum_i \frac{1}{\beta !}\mu_i (-\beta)^i$$

$$\mu_i = \left(\frac{\text{d}^i Z }{\text{d} \beta^i} \right)_{\beta=0}$$

Re-expressing the moments as $\mu_i=\langle X^i \rangle$, we get  

$$\mu_0 = \langle X^0 \rangle =1 $$

and 

$$Z(\beta) = 1 - \langle X \rangle \beta + \frac{\langle X^2 \rangle}{2} \beta^2 -\frac{\langle X^3 \rangle}{6}\beta^3 + ... = \sum_i \frac{1}{\beta !}\langle X^i \rangle (-\beta)^i$$

Now recalling that, for any variable $\alpha$, the exponential can be expressed as a polynomial (Taylor expansion) as

$$e^{\alpha} = 1 + X + \frac{1}{2}\alpha^2 +   \frac{1}{6}\alpha^3 + ...$$ 

we can notice that the generating function is almost an exponential for the variable $\alpha = -\beta X$. Using the fact that $\langle aX + bY \rangle = a\langle X \rangle + b \langle Y \rangle$, we can rewrite:

$$ Z(\beta) = \langle e^{-\beta X}\rangle$$

For to the continuous case, this is written

$$ Z(\beta) = \int p(x) e^{-\beta X} \text{d} x $$

Which is the so-called **Laplace transformation** of the function $p(x)$.

**Examples:** die, gaussian

### Central limit theorem

## Cumulents


## Going further: recommended readings

- Physique statistique (French) - 2nd edition (2024) - C. Texier, G. Roux - Dunod