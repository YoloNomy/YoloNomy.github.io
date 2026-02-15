---
layout: default
title: Generating function
parent: thermo
nav_order: 1
---

# Bonus: A new take on $Z$ and the canonical ensemble

In this "bonus" lecture, we want to further reflect on $Z$, its role and propose alternative ways to derive the ensembles of statistical physics without calling for the maximisation of entropy.
This lecture is a bit technical (but enlightening!), and might be skipped on a first go through the class.
The statements in this lecture are very general and apply to both the discrete, the continuous and the quantum case, as you can convince yourself easily.

# Other derivations of the canonical ensemble

## From microstates of the reservoir

It is sometimes stated that the
**fundamental postulate** of statistical physics, is that all accessible microstates of an isolated system at equilibrium are equiprobable, which is a result we found by maximizing the entropy for the microcanonical ensemble. We can use this as a starting point to rederive the $p_i$ for the other ensembles, without using the entropy maximisation technique. This approach is the most commonly found in standard textbooks on statistical physics.

As we saw, the canonical ensemble is used when one consider a small system $s$ in contact with a large reservoir $R$, constraining $s$ to have a mean energy $\langle E \rangle$.
One can consider the total system $s+R$ as being isolated and as such, any configuration of this total system must be equiprobable. 
Since it is isolated, the total system has a fixed energy $E=E_R + E_s$, where both $E_R$ and $E_s$ can change with time (but not $E$).
Let's assume that the small system has $N_s$ possible microstates and that the reservoir has $N_R$ possible microstates. The total number of microstates for $s+R$ will be $N_{s+R}=N_s N_R$ to account for all possible combination of both.

Now, if the small system $s$ is in one the microstate $i$ with an energy $E_s=E_i$, the reservoir $R$ must be in one of the its $g_R(E-E_i)$ possible configuration with energy $E- E_R$. For now we assume that there is a unique microstate with energy $E_i$ (ignoring degeneracies, which would simply require to multiply everything by $g_s$). Then, the probability that $s$ is in its microstates $i$ is equal to the probability that $R$ is in a microstate of energy $E-E_i$, that is:

$$\boxed{p_i = \frac{g_R(E_i - E)}{N_{s+R}}}$$

We will leave it to you to decide whether you are more convinced by this proof for the canonical ensemble derivation, or by the maximum entropy approach. Both are undoubtly complementary.

For the [continuous case](../statistical/phasespace.md), an absolutely identical argumentation can be pursued using ratios of volumes in phase space:

$$\rho = \frac{\Omega(E-E_i)}{\Omega}$$

but you will need the next lecture to properly understand this! 

## Using the properties of the exponential function

Energy is only defined up to a constant:

$$\frac{P(E_n)}{P(E_m)}= \frac{P(E_n+C)}{P(E_m+C)} $$

The only continuous function satisfying this constraint is of the form:

$$P(E_n) \propto e^{-\beta E_n}$$


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

$$Z(\lambda) = \mu_0 - \mu_1 \lambda + \frac{\mu_2}{2} \lambda^2 -\frac{\mu_3}{6}\lambda^3 + ... = \sum_i \frac{1}{\lambda !}\mu_i (-\lambda)^i$$

$$\mu_i = \left(\frac{\text{d}^i Z }{\text{d} \lambda^i} \right)_{\beta=0}$$

Re-expressing the moments as $\mu_i=\langle X^i \rangle$, we get  

$$\mu_0 = \langle X^0 \rangle =1 $$

and 

$$Z(\lambda) = 1 - \langle X \rangle \lambda + \frac{\langle X^2 \rangle}{2} \lambda^2 -\frac{\langle X^3 \rangle}{6}\lambda^3 + ... = \sum_i \frac{1}{\lambda !}\langle X^i \rangle (-\lambda)^i$$

Now recalling that, for any variable $\alpha$, the exponential can be expressed as a polynomial (Taylor expansion) as

$$e^{\alpha} = 1 + X + \frac{1}{2}\alpha^2 +   \frac{1}{6}\alpha^3 + ...$$ 

we can notice that the generating function is almost an exponential for the variable $\alpha = -\lambda X$. Using the fact that $\langle aX + bY \rangle = a\langle X \rangle + b \langle Y \rangle$, we can rewrite:

$$ Z(\lambda) = \langle e^{-\lambda X}\rangle$$

For to the continuous case, this is written

$$ Z(\lambda) = \int p(x) e^{-\lambda X} \text{d} x $$

Which is the so-called **Laplace transformation** of the function $p(x)$.

**Examples:** die, gaussian

### Central limit theorem

### Cumulents

### Partition function and moments

Adding constraints on the mean value of multiple variables $X^{(j)}$ and maximizing the entropy always lead:

$$p_i = \frac{1}{Z} e^{-\sum_j \lambda_j X^{(j)}_i} $$

$$ Z= \sum_i e^{-\sum_j \lambda_j X^{(j)}_i}$$

where $\lambda_i$ are the Lagrange multipliers associated to the variable $X^{(j)}$.

$$\langle X_i \rangle =-\frac{\partial \ln(Z)}{\partial \lambda_i} $$

$$\frac{\partial^2 \ln(Z)}{\partial \lambda_j \lambda_k} = \langle X_jX_j\rangle -  \langle X_j\rangle \langle X_j\rangle $$

For the case of energy, in the canonical model:

$${\rm Var}(E)= \frac{\partial^2 \ln(Z)}{\partial \beta^2}$$

and any higher order cumulents with higher derivatives of $\ln(Z)$. Defining

$$C_v := \frac{\partial U}{\partial T} $$

we find the expression:

$${\rm Var}(E)= -\frac{\partial U}{\partial \beta} = k_B T^2\frac{\partial U}{\partial T} = k_B T^2 C_v$$

Thus, fluctuations in energy within a microscopic system grows as $T^2$.

## Going further: recommended readings

- Elements of Statistical Mechanics: With an Introduction to Quantum Field Theory and Numerical Simulation - I. Sachs, S. Sen, J. Sexton (2006) -  Cambridge University Press 
- Physique statistique (French) - 2nd edition (2024) - C. Texier, G. Roux - Dunod