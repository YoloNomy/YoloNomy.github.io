---
layout: default
title: connections
has_children: False
nav_order: 5
---

# Connections

Connections are certainly one of the most important notion of fundamental physics, as they allow to describe all the fundamental interactions that we know so far. These objects are rich, and can be defined in multiple ways. We will try to introduce them gradually here, with an increasing level of abstraction and shed some light on their importance in physics. For an history of the notion of connection, you can also have a look at the french essay here.

## Affine connections and Levi-Civita's connection

### Definition of the affine connections

Perhaps the most familiar connection for physicists is the so-called "Levi-Civita" connection $\Gamma$, appearing in general relativity. This connection, which can be expressed in term of the metric tensor $g$, can be used to compute the geodesic equations and the curvature of space-time which describes respectively the motion of particles in a gravitational field and the tidal forces due to gravity itself. As we will discuss here $\Gamma$ is the special case of an object called an "affine connection", which is itself a special case of the more general notion of connection. Let us start with rather abstract and formal definitions and try to put some intuition on it in the next sections.

An affine connection $\gamma$ on a manifold $M$ allows to define the derivation of vector fields $v\in TM$, living on the tangent bundle of a manifold $M$. $\nabla$ is a map which takes two vector fields $v,w\in TM$ and return a vector field $\nabla \to \nabla_wv: TM \times TM\to TM$ (Hence $\nabla \in TM^*\otimes {\rm End}(TM)$). The resulting vector field $\nabla_wv$ is called the covariant derivative of $v$ in the direction $w$.
Let $v,w,z \in TM$ be three vector fields, $f\in C^{\infty}(M)$ be a function on $M$ and $\alpha\in\mathbb{R}$ a real number. $\nabla$ is defined as a map satisfying the following properties:

- $\nabla_{fw}v= f\nabla_wv$ 
- $\nabla_w(\alpha v)= \alpha \nabla_w v$  
- $\nabla_{w+z}v= \nabla_wv + \nabla_zw$  
- $\nabla_w(v+z)= \nabla_wv + \nabla_wz$  
- $\nabla_w(fv)=  \text{d}f(v) + f\nabla_wv= v(f) + f\nabla_wv$ 

The four first properties are properties of linearity and associativity of $\nabla$ is linear with respect to its entries. The last property is a generalisation of the Leibniz rule, which allows to interpret $\nabla$ as a derivation operator.

Let us now take a natural choice of frame $e_\mu=\partial_\mu$ on $TM$ in which to decompose locally the vectors $v=v^\mu e_\mu$ and $w=w^\nu e_\nu$. As the covariant derivative takes a vector field, to give back a vector field, we can write

$$
\nabla_{e_\mu} e_\nu = \Gamma^\lambda_{\,\,\mu \nu}e_\lambda
$$ 

which define the coefficients $\Gamma^\lambda_{\,\,\mu \nu}$ called the *connection's coefficients* or the *christoffel symbols*.  $\Gamma^\lambda_{\,\,\mu \nu}$ are then the coordinates of the vector $\nabla_\mu e_\nu$ in the $e_\lambda$ basis. Put differently: $\Gamma^\lambda_{\,\,\mu \nu}$ express how to derivate the vector basis $e_\nu$ in the direction $e_\mu$.

Using all the properties above, we can express $\nabla_wv$ in a basis as

$$
\nabla_wv = w^\mu(\partial_\mu v^\nu+\Gamma^\nu_{\,\,\mu \lambda}v^\lambda)e_\nu,
$$


<details>
  <summary>Proof</summary>

$$
\begin{aligned}
\nabla_wv &=\nabla_{w^\mu e_\mu}(v^\nu e_\nu) \qquad && \text{Vector decomposition in a basis}\\
&=w^\mu \nabla_{e_\mu}(v^\nu e_\nu)  &&\text{Linearity in the first entry}\\
&=w^\mu\left(\text{d} v^\nu(e_\mu)e_\nu + \nabla_{e_\mu}(e_\nu)\right)  &&\text{Leibniz rule}\\
&=w^\mu\left(\partial_\mu v^\nu e_\nu + \nabla_{e_\mu}(e_\nu)\right) && \text{d}f=v(f)=v^\mu\partial_\mu f, \text{here $f=v^\nu$ and $v=e_\mu = \partial_\mu$} \\
&=w^\mu\left(\partial_\mu v^\nu e_\nu  + \Gamma^\lambda_{\,\,\mu \nu}e_\lambda\right)  &&\text{Definition of $\Gamma$}\\
&= w^\mu\left(\partial_\mu v^\nu + \Gamma^\nu_{\,\,\mu \lambda}\right)e_\nu && \text{Renaming the sommation indices $\lambda \to \nu$}
\end{aligned}
$$
</details>

Taking now $w$ to be a basis vector $w=e_\nu=\partial_\nu$, using the shorthand notation $\nabla_{\partial_\mu}=\nabla_\mu$ and considering only the coordinates in the $\partial_\nu$ frame, $\nabla_\mu v^\nu=(\nabla_\mu v)^\nu$:

$$
\nabla_\mu v^\nu = \partial_\mu v^\nu+\Gamma^\nu_{\,\,\mu\lambda}v^\lambda
$$

which is the famous formula for the covariant derivative, often used as a definition in general relativity.

### Levi-Civita connection

The Levi-Civita connection, central object of general relativity, is a special case of affine connection. It is the unique metric preserving and torsion free connection. Note that our above definition of an affine connection does not require at all the presence of a metric $g$ on the manifold, while the Levi-Civita connection does.
 
#### metric preserving

An affine connection $\nabla$ is said to be *metric preserving* if $\forall v,w,z \in TM$

$$v(g(w,z))=g(\nabla_vw,z)+g(w,\nabla_v z)$$

A metric satisfying this condition preserve the length of the vectors.

#### Torsion free

An affine connection $\nabla$ is said to be *torsion-free* $\forall v,w \in TM$

$$\nabla_vw-\nabla_wv=vw-wv$$

Symmetry over the indices:

$$\Gamma^\lambda_{\mu \nu}=\Gamma^\lambda_{\mu \nu}$$

Does not impact geodesic equations.

### Uniqueness and expression in coordinates

The Levi-Civita connection is unique and can be expressed solely in term of the metric and its derivatives as

$$
\Gamma^\lambda_{\,\,\mu\nu}= \frac{1}{2}g^{\lambda \kappa}(\partial_\mu g_{\nu\kappa} + \partial_{\nu}g_{\mu\kappa}-\partial_\kappa g_{\mu \nu})
$$

### The parallel transporter, parallel transport and projectors 

### Geodesics

Another notion which comes over and over in general relativity, is the notion of geodesic. Particles in a gravitational field follows geodesics of the Levi-Civita connexion.

A curve $\gamma(\tau)$ is sayed to be a geodesic of an affine connexion if it's tangent $u$ vector always satisfies 

$$\nabla_u u=0$$

$u$ is then said to be autoparallel.

With this definition, in a given coordinate chart $x^\mu$, we are able to recover the usual geodesic equation

$$
\frac{\partial^2 x^\lambda}{\partial \tau^2} = - \Gamma^{\lambda}_{\mu \nu}\frac{\partial x^\mu}{\partial \tau}\frac{\partial x^\nu}{\partial \tau}
$$

<details>
  <summary>Proof</summary>

In a given chart $u = \partial_\tau x^\mu \partial_\mu$ such that 

$$
\begin{aligned}
\nabla_u u &= 
\nabla_{(\partial_\tau x^\nu \partial_\nu)} (\partial_\tau x^\mu \partial_\mu) 
\\
&=\partial_\tau x^\nu\nabla_{\partial_\nu} (\partial_\tau x^\mu \partial_\mu) \\
&=\partial_\tau x^\nu\left(\partial_\nu\partial_\tau x^\mu \partial_\mu + \partial_\tau x^\mu \nabla(\partial_\mu) \right) \\
&=\partial_\tau x^\nu\left(\partial_\nu\partial_\tau x^\mu \partial_\mu + \partial_\tau x^\mu \Gamma^\lambda_{\nu \mu}\partial_\lambda \right) \\
&=\partial_\tau^2 x^\mu \partial_\mu + \partial_\tau x^\nu\partial_\tau x^\mu \Gamma^\lambda_{\nu \mu}\partial_\lambda \\
&=\left(\partial_\tau^2 x^\lambda+ \partial_\tau x^\nu\partial_\tau x^\mu \Gamma^\lambda_{\nu \mu} \right)\partial_\lambda 
\end{aligned}
$$
</details>

### Levi-Civita as a gauge connexion

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

Let $\partial_\mu$ be a basis of $TM$, we use the standard notation: $\nabla_{\mu}=\nabla_{\partial_\mu}$. Let $e_i$ be a local basis of sections of $E$ over $U \subseteq M$. $\nabla_\mu e_j$ is also a section of $E$ and can then be expressed as:

$$
\nabla_\mu e_j = A^i_{\mu j}e_i
$$ 

$A^i_{\mu j}$ are then the coordinates of $\nabla_\mu e_j$ in the $e_i$ basis. $A$ is called the *vector potential*. Using the properties listed above, we can then express the coordinates of the covariant derivative of any section $s=s^ie_i$ along $v=v^\mu\partial_\mu$ over $U$:

$$
\nabla_vs = v^\mu((\partial_\mu s^i)+A^i_{\mu j}s^j)e_i
$$

$A$ can be thaught as a $\text{End}(E)$ valued 1-form over $U$: $$A \in \text{End}(E\|_U)\otimes T^*U$$(that is a map $E\times TM \to E$):

$$
A = A^i_{\mu j} \text{d} x^\mu \otimes e_i \otimes e^j
$$

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