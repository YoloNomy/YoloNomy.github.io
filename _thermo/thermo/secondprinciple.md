---
layout: default
title: Second law of thermodynamics
parent: thermo
nav_order: 1
---

# Second law of thermodynamics: entropy

When defining the [first principle](../firstprinciple/), we introduced a new state function, the internal energy $U$. The first principle was then the given of a rule, empirically valid, about how this energy should change when system witness transformations.

The second principle follows a similar direction. We also entroduce a new state function called the **entropy** $S$. This function is much more abstract than the internal energy. It associated with the "disorder" contained in the system, even though a finer understanding is more subtle. Explaining this in more details will be the topic of our more advanced [first lecture of statistical mechanics](../../statistical/entropy/). For now, consider $S$ as an abstract function, which can be computed for every system, and for which the specific expression in term of the state variables depend on each system considered.

Instead of being defined by its expression, $S$ is defined just like $U$ by the way it changes under a transformation of the system. $S$ 

$$\boxed{\text{d}S = \frac{\delta Q}{T}} $$

The **second principle of thermodynamics**, which you should understand here as an empirical fact that is always satisfied, is that the entropy of an isolated system always increase or stays the same in a transformation, that is:

$$\boxed{\text{d}S \geq 0}$$

This fact has very proufound roots, but for now we just need to accept it, as something that is always verified and that we can use to understand systems. 

## A consequence: heat flows from hot regions to cold regions

A consequence of the second principle, is that energy flows from hot to cold systems. To convince yourself, consider two systems $A$ and $B$ in contact with each others with different temperature $T_A$ and $T_B$. $A$ and $B$ can exchange energy. We expect them to gradually reach thermal equilibrium such that, after a while $T_A=T_B$.


During the transformation, we expect Entropies to be additives $S = S_A + S_B$. We also expect energy to be additive $U= U_A + U_B$ and energy is conserved through the transformation  $\text{d} U = \text{d}U_A + \text{d}U_B=0$, such that, for a transfer of energy solely through heat for two systems in contact: $\delta Q_A = -\delta Q_B$. 

Adding on top of that the second law, which we will assume to be true $\text{d}S_A + \text{d}S_B\geq0$.

$$ \text{d}S_A + \text{d}S_B\geq0 $$

$$ \frac{\delta Q_A}{T_A} + \frac{\delta Q_B}{T_B} \geq0 $$

$$ \frac{\delta Q_A}{T_A} - \frac{\delta Q_A}{T_B} \geq0 $$

Now, let's assume that the heat transfer goes from $B$ to $A$, that is, $A$ is receiving the heat ($\delta Q_A \geq 0$) and $B$ is loosing it ($\delta Q_B \leq 0$). As such:

$$ \frac{1}{T_A} - \frac{1}{T_B} \geq0 $$

$$ \frac{T_B-T_A}{T_A T_B} \geq 0$$

$T_A$ and $T_B$ are temperatures, as such $T_A, T_B \geq 0$ and hence

$$ T_B - T_A \geq 0 $$

$$ T_B \geq T_A $$

Hence, the heat transfer must go from the hot object $B$ to the colder one $A$!

## A consequence: irreversibility 
