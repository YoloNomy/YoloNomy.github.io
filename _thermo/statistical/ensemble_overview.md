---
layout: default
title: Grand canonical ensemble
parent: thermo
nav_order: 1
---

## Isobaric-Isothermal ensemble

Note that allowing other constraints (like volume fluctuation) would add new lagrange multipliers appearing in the exponential of the expression of $p_i$.

## Overview of the ensembles

| Ensemble | Fixed Variables | Probability Weight ($p_i \propto \dots$) | Partition Function | Thermodynamic Potential |
| :--- | :--- | :--- | :--- | :--- |
| **Microcanonical** | $N, V, E$ | $1$ | $N$ or $\Omega$ | Energy $U$ or entropy $S =  \ln \Omega$|
| **Canonical** | $N, V, T$ | $e^{-\beta E_i}$ | $Z = \sum_i e^{-\beta E_i}$ | Free Energy: $A = - T \ln Z$ |
| **Grand Canonical** | $\mu, V, T$ | $e^{-\beta(E_i - \mu N_i)}$ | $\Xi = \sum_i e^{-\beta(E_i - \mu N_i)}$ | Grand Potential: $\Phi_G = - T \ln \Xi$ |
| **Isobaric-Isothermal** | $N, P, T$ | $e^{-\beta(E_i + PV_i)}$ | $\Delta = \sum_i e^{-\beta(E_i + PV_i)}$ | Gibbs Free Energy: $G = - T \ln \Delta$ |

Bla

| Ensemble  | Definition | Relation to Partition Function | Differential Form ($d\Phi$) |
| :--- | :--- | :--- | :--- | :--- |
| **Microcanonical** | $S =  \ln \Omega$ | $S =  \ln \Omega$ | $dS = \frac{1}{T}dU + \frac{P}{T}\text{d}V - \frac{\mu}{T}\text{d}\mathcal{N}$ |
| **Canonical** | $A = U - TS$ | $A = - T \ln Z$ | $dA = -S\text{d}T - P\text{d}V + \mu \text{d}\mathcal{N}$ |
| **Grand Canonical** | $J = U - TS - \mu N$ | $J = - T \ln \Xi$ | $dJ = -S\text{d}T - P\text{d}V - N\text{d}\mu$ |
| **Isobaric-Isothermal** | $G = U - TS + PV$ | $G = - T \ln \Delta$ | $dG = -S\text{d}T + V\text{d}P + \mu \text{d}\mathcal{N}$ |


## Legendre transformations