---
layout: default
title: Foundations of general relativity
parent: cosmo
---

# What to modify? Foundations of general relativity

If we want to study modified gravity, we must first understand what is there to modify. Our best description of gravity is general relativity, the foundation of modern cosmology. From its formulation in 1915 to the first direct detection of gravitational waves a century later, it has proven to be a remarkably successful theory, with applications ranging from solar system dynamics to the large-scale structure of the universe. At its core lies a beautiful geometric picture: spacetime curvature governs the motion of matter, and matter in turn shapes the curvature of spacetime.

## Some conceptual motivations for GR

### General covariance, diffeomorphisms and relativity principle

### Einstein equivalence principle

**Universality of free-fall (UFF)**: experimental fact, all bodies fall identically in a gravitational field.

**Einstein equivalence principle (EEP)**:
- (LPI):
- (LLI):
- (WEP):

While UFF and WEP are sometimes identified, we can consider UFF as an experimental fact, while WEP is a principle.

## From motivations to axioms

## Axioms of general relativity:

### Structure:

- (S1): Space-time is a smooth **four dimensional manifold** $M$.
- (S2): $M$ is equipped with a **Lorentzian metric tensor** $g$ at each point, allowing to define length and angles of tangent vectors.
- (S3): $M$ is equipped with a **connection** $\Gamma$ defining parallel transport of tangent vectors. $\Gamma$ is assumed to be **metric compatible** (S3a) and **torsion free** (S3b). It can be proved that such a choice leads to a **unique Levi-Civita connection**, which can be fully expressed in terms of the metric $g$ and its coordinate derivatives. All other geometrical objects which could be associated to matter fields (i.e. spinors and tensors) are also transported through generalizations of $\Gamma$.

<details markdown="1">
  <summary><strong>Complements: useful definitions and reminders</strong></summary>

- A smooth **manifold**:
- A **metric tensor**:
- A **Lorentzian metric**:
- A **connection**:
- **metric compatibility**:
- **torsion free**:
</details>

### Dynamics:

- (D1): Energy is related to geometry, through the **Einstein equation**:

    $$\boxed{R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu} - \Lambda g_{\mu\nu}}$$

    where $R_{\mu\nu}$ and $R$ are contractions of the Riemann curvature associated to $\Gamma$ defined as $R=$.

- (D2): Matter fields obey their special-relativistic field equations in any local inertial frame (minimal coupling).

D1 and D2 can also be recovered through extremalization of the **Einstein-Hilbert Lagrangian** density:

$$\boxed{\mathcal{L} = \sqrt{-g}\left(\frac{1}{16 \pi G}(R - 2\Lambda) + \mathcal{L}_m\right)}$$

which encodes both Einstein equations (D1) when varying with respect to $g$ and the equation of matter of fields (D2) when varying with respect to them.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

Natural consequences of D1 and D2:

- The **continuity equation**: $$\nabla_\mu T^{\mu\nu}=0$$, which comes from the reunion of Einstein equations with the Bianchi identity $\nabla_\mu G^{\mu\nu}=0$.
- The **geodesic equation** for a point like particle $u^\mu\nabla_\mu u^\nu=0$. This equation is a special case of the continuity equation for a free (massive or massless) particle with energy momentum $T_{\mu\nu}=\rho u^\mu u^\nu$.

# Further reading

- Caroll - Spacetime and Geometry
- R. M. Wald - general relativity 
- Misner, Thorne, Wheeler - gravitation