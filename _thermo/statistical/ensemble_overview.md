---
layout: default
title: Grand canonical ensemble
parent: thermo
nav_order: 1
---

## Isobaric-Isothermal ensemble

Note that allowing other constraints (like volume fluctuation) would add new lagrange multipliers appearing in the exponential of the expression of $p_i$.

The **isobaric-isothermal** ensemble, where both $U$ and $V$ are constrained to a mean value. It is easy to show.

$$\boxed{p_i = \frac{1}{\Delta} e^{-\beta E_i + P V_i}}$$

Where $\Delta$ is the Isobaric-Isothermal partition function 

$$\boxed{\Delta=\sum_i e^{-\beta E_i + P V_i}}$$

We will not cover in detail this ensemble here, as all proof are very similar to the ones done for previous ensembles. 

## Overview of the ensembles

All ensembles have 

$$ p_i = \frac{\text{Weight}}{\text{Partition function}}$$



| Ensemble | Fixed Variables | Probability Weight ($p_i \propto \dots$) | Partition Function | Thermodynamic Potential |
| :--- | :--- | :--- | :--- | :--- |
| **Microcanonical** | $N, V, E$ | $1$ | $N$ or $\Omega$ | Energy $U$ or entropy $S =  \ln \Omega$|
| **Canonical** | $N, V, T$ | $e^{-\beta E_i}$ | $Z = \sum_i e^{-\beta E_i}$ | Free Energy: $A = - T \ln Z$ |
| **Grand Canonical** | $\mu, V, T$ | $e^{-\beta(E_i - \mu N_i)}$ | $\Xi = \sum_i e^{-\beta(E_i - \mu N_i)}$ | Grand Potential: $\Phi_G = - T \ln \Xi$ |
| **Isobaric-Isothermal** | $N, P, T$ | $e^{-\beta(E_i + PV_i)}$ | $\Delta = \sum_i e^{-\beta(E_i + PV_i)}$ | Gibbs Free Energy: $G = - T \ln \Delta$ |

Bla

| Ensemble  | Definition | Differential Form ($d\Phi$) |
| :--- | :--- | :--- | :--- | :--- |
| **Microcanonical** | $S =  \ln \Omega$ | $\text{d}S = \frac{1}{T}dU + \frac{P}{T}\text{d}V - \frac{\mu}{T}\text{d}\mathcal{N}$ |
| **Canonical** | $A = U - TS$ | $\text{d}A = -S\text{d}T - P\text{d}V + \mu \text{d}\mathcal{N}$ |
| **Grand Canonical** | $\Phi_G= A - \mu N$ | $\text{d}\Phi_G = -S\text{d}T - P\text{d}V - N\text{d}\mu$ |
| **Isobaric-Isothermal** | $G = A + PV$ | $\text{d}G = -S\text{d}T + V\text{d}P + \mu \text{d}\mathcal{N}$ |





## Legendre transform
