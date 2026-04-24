---
layout: default
title: Classical thermo
parent: thermo
nav_order: 1
---

We already encountered **state functions**, that is functions describing the system and expressed in terms of states variables. Each of the two first principle of thermodynamics introduces a state function and describe its evolution through transformations, namely the **internal energy** $U(P,V,T,N)$ and the **entropy** $S(P,V,T,N)$

## Thermodynamics potentials:

### Helmmholtz free energy

$$ A = U - TS$$

### Enthalpy 

It's the energy it would take to create an object out of nowhere on earth and push the atmosphere to make room for it:

$$ H = U + PV$$

It is thus an interesting quantity for systems exposed to a constant pressure (for example in earth's atmosphere).

Indeed, for a constant pressure process:

$$ \Delta H = \Delta U + P\Delta V$$

Changes in enthalpy occurs for two reasons: either the internal enery can change or the system can change size and work is done to push or get compressed by the atmosphere. 

Adding the first principle, we get that at constant pressure, the change in enthalpy is just the pressure $\Delta H = Q$.

### Gibbs free energy

$$U + pV - TS$$

## Analogy with mechanics and Legendre transforms

$$\text{d}E = \vec{F}\cdot \text{d}\vec{l}$$

A change in energy is the product of a force and a displacement. 

$$ \text{d}U = T\text{d}S -p \text{d}V + \mu \text{d}\mathcal{N}$$

Conjugate variables are understood as a pair of thermodynamic forces and thermodynamics displacements, which product give an energy.

To each potentials are associated conjugate pairs. To $U$, "Legendre conjugates"
to $S$ Lagrange conjugates, which will become clear in the context of statistical mechanics.

Extensive variables, $S,V,\mathcal{N}$ thus act as directions of a manifold in which the system can evolve. Intensive variables, $T,P,\mu$ on the other hand, are more analogous to momentum.

The full analogy in a mathematical language is discussed in [this lecture](../../_maths/geodiff/thermodynamics.md)