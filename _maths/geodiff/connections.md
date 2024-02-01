---
layout: default
title: connections
has_children: False
nav_order: 5
---

# Connections

Connections are certainly one of the most important notion of fundamental physics, as they allow to describe all the fundamental interactions that we know so far. These objects are rich, and can be defined in multiple ways. We will try to introduce them gradually here, with an increasing level of abstraction and shed some light on their importance in physics.

## Connection on a vector bundle (Koszul connexion)

Recall here that a vector bundle attaches $E$ a vector space, of dimension $d$ and field $\mathcal{F}\in\{\mathbb{R},\mathbb{C}\}$, at every point of a manifold $M$. A point of $E$ is given locally by a pair $(x,s)$, where $x\in M$ is a point of space-time and $s\in V$ is a vector associated to $x$.  The tangent bundle is hence a special case of vector bundle, associating $\mathbb{R}^d$ to each point of a manifold of dimension $d$.

Let $E$ be a $\mathcal{F}$-vector (associated) bundle over $M$. A *connection* $\nabla$ can be defined as a map: $TM \times \Gamma(E) \to\Gamma(E)$, that associate $\nabla_v s \in \Gamma(E)$ to the pair $v \in TM$ and $s \in \Gamma(E)$, obeying the following properties:

- $\nabla_{fv}s= f\nabla_vs$ 
- $\nabla_v(\alpha s)= \alpha \nabla_v s$  
- $\nabla_{v+w}s= \nabla_vs + \nabla_ws$  
- $\nabla_v(s+t)= \nabla_vs + \nabla_vt$  
- $\nabla_v(fs)= v(f)s + f\nabla_vs$ 

$\forall v,w \in  TM$, $s,t \in \Gamma(E)$, $f\in C^\infty(M)$ and $\alpha \in \mathcal{F}$. The four first properties simply states that $\nabla$ is a linear and distributive map with respect to both of its entry. The last rule is the more interesting, as it generalizes the Leibniz's law of derivatives. As such, defining $\nabla$ allows to define a proper way to do derivations on $E$. We will interpret $\nabla_vs$ as the derivative of the section $s$ in the direction pointed by the vector $v$. In fact, $\nabla_vs$ is called the *covariant derivative* of $s$ in the direction $v$.

Now, locally, we can choose a basis of the tangent space and of the vector bundle, such that we can write $v=v^\mu\partial_\mu$ and $s=s^ie_i$.

## The parallel transporter

## Affine connections and Levi-Civita's connection

### metric preserving

### Torsion free

### Parallel transport and projectors 

### Levi-Civita as a gauge connexion

## Connection on a principal bundle (Ehresman connection)

## Connexion 1-form on a principal bundle (Cartan connection)

## connection inherited from a principal bundle

### Simple approach

### Horizontal lift and covariant derivative

# Further readings

- Faure
- Baez
- Coqueraux
- Nakahara
- Kobayashi Nomizu