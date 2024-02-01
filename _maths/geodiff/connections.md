---
layout: default
title: connections
has_children: False
nav_order: 5
---

# Connections: general relativity and gauge theories

Connections are certainly one of the most important notion of fundamental physics, as they allow to describe all the fundamental interactions that we know so far. These objects are rich, and can be defined in multiple ways. We will try to introduce them gradually here, with an increasing level of abstraction and shed some light on their importance in physics. For an history of the notion of connection in maths and in physics, you can also have a look at the essay in french available [here](https://leovacher.github.io/).

Connections are introduced to solve the following major problem: in order to define the derivative of geometrical objects such as vectors or tensors, we should be able compare two such objects living at different points of the manifold, to be able to quantify how much they changed. But there are no immediate way to do so. In principle, two tangent spaces are independent vector spaces, and there are no canonical way to say that two vectors associated to different points are "the same" or "different in such a way" (the same reasoning applies between two fibers on a fiber bundle). Connections hence define an identification between different points in nearby tangent spaces (or fibers). Hence their names: they "connect" different spaces living at different points of a manifold.

## Affine connections and Levi-Civita's connection

### Definition of the affine connections

Perhaps the most familiar connection for physicists is the so-called "Levi-Civita" connection, appearing in general relativity. This connection, which can be expressed in term of the metric tensor $g$, can be used to compute the geodesic equations and the curvature of space-time which describes respectively the motion of particles in a gravitational field and the tidal forces due to gravity itself. As we will discuss here, this connection is the special case of an object called an "affine connection", which is itself a special case of the more general notion of connection. Let us start with rather abstract and formal definitions and try to put some intuition on it in the next sections.

An affine connection $\Gamma$ on a manifold $M$ allows to define the derivation of vector fields $v\in TM$, living on the tangent bundle of a manifold $M$. $\nabla$ is a map which takes two vector fields $v,w\in TM$ and return a vector field $\nabla \to \nabla_wv: TM \times TM\to TM$ (Hence $\nabla \in TM^*\otimes {\rm End}(TM)$). The resulting vector field $\nabla_wv$ is called the covariant derivative of $v$ in the direction $w$.

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
&= w^\mu\left(\partial_\mu v^\nu + \Gamma^\nu_{\,\,\mu \lambda}\right)e_\nu && \text{Renaming the summation indices $\lambda \to \nu$}
\end{aligned}
$$
</details>

Taking now $w$ to be a basis vector $w=e_\nu=\partial_\nu$, using the shorthand notation $\nabla_{\partial_\mu}=\nabla_\mu$ and considering only the coordinates in the $\partial_\nu$ frame, $\nabla_\mu v^\nu=(\nabla_\mu v)^\nu$:

$$
\boxed{\nabla_\mu v^\nu = \partial_\mu v^\nu+\Gamma^\nu_{\,\,\mu\lambda}v^\lambda}
$$

which is the famous formula for the covariant derivative, often used as a definition in general relativity.

### Levi-Civita connection

The Levi-Civita connection, central object of general relativity, is a special case of affine connection. It is the unique metric preserving and torsion free connection. Note that our above definition of an affine connection does not require at all the presence of a metric $g$ on the manifold, while the Levi-Civita connection does.
 
#### Metric preserving

An affine connection $\nabla$ is said to be *metric preserving* if $\forall v,w,z \in TM$ if

$$\boxed{v(g(w,z))=g(\nabla_vw,z)+g(w,\nabla_v z)}$$

A metric satisfying this condition preserve the length of the vectors.

#### Torsion free

An affine connection $\nabla$ is said to be *torsion-free* $\forall v,w \in TM$ if

$$\boxed{\nabla_vw-\nabla_wv=[v,w]}$$

where $[v,w]$ is the Lie bracket for vectors, acting on functions as $\[v,w\](f)=v(f)w(f)-w(f)v(f)$.

When applying this condition on basis vectors, we find that $\Gamma$ must respect a symmetry condition on its indices:

$$\Gamma^\lambda_{\,\,\mu \nu}=\Gamma^\lambda_{\,\,\nu \mu}$$

<details>
  <summary>Proof</summary>

Choosing again a natural frame $e_\mu=\partial_\mu$, we must have $[e_\mu,e_\nu]=0$ as 

$$[e_\mu,e_\nu](f)=\partial_\mu f\partial_\nu f-\partial_\nu f\partial_\mu f=0$$.

Hence, the torsion-free condition becomes

$$
\begin{aligned}
&\nabla_{e_\mu}e_\nu-\nabla_{e_\nu}e_\mu=0\\
&\Gamma^{\lambda}_{\,\,\mu\nu}e_\lambda - \Gamma^{\lambda}_{\,\,\nu\mu}e_\lambda=0\\
&\Gamma^{\lambda}_{\,\,\mu\nu}-\Gamma^{\lambda}_{\,\,\nu\mu}=0\\
&\Gamma^\lambda_{\,\,\mu \nu}=\Gamma^\lambda_{\,\,\nu \mu}
\end{aligned}
$$

</details>


### Uniqueness and expression in coordinates

The Levi-Civita connection is uniquely determined by the metric $g$ and can be expressed in a natural frame solely in term of the metric and its derivatives as

$$
\boxed{\Gamma^\lambda_{\,\,\mu\nu}= \frac{1}{2}g^{\lambda \kappa}(\partial_\mu g_{\nu\kappa} + \partial_{\nu}g_{\mu\kappa}-\partial_\kappa g_{\mu \nu}),}
$$

which is again a familiar formula for the physicist.

<details>
  <summary>Proof</summary>

Consider again a natural frame $e_\mu$ in which the metric compatibility condition reads

$$\begin{aligned}
&e_\mu(g(e_\nu,e_\lambda))=g(\nabla_{e_\mu}e_\nu,e_\lambda)+g(e_\nu,\nabla_{e_\mu} e_\lambda)\\
&\partial_\mu g_{\nu\lambda}= g(\Gamma^\kappa_{\mu\nu}e_\kappa,e_\lambda)+ g(e_\nu,\Gamma^\sigma_{\mu\lambda}e_\sigma)\\
&\partial_\mu g_{\nu\lambda}= \Gamma^\kappa_{\,\,\mu\nu}g_{\kappa\lambda}+\Gamma^\sigma_{\,\,\mu\lambda} g_{\lambda\sigma}
\end{aligned}
$$

From this, and using the symmetry property $\Gamma^\lambda_{\,\,\mu\nu}=\Gamma^\lambda_{\,\,\nu\mu}$, it is possible to derive that:

$$\begin{aligned}
\partial_\mu g_{\nu\kappa} + \partial_{\nu}g_{\mu\kappa}-\partial_\kappa g_{\mu \nu} &= 
g_{\lambda \kappa }\Gamma^{\lambda}_{\,\, \mu \nu}
+g_{\nu \lambda }\Gamma^{\lambda}_{\,\, \mu \kappa}
+g_{\lambda \nu }\Gamma^{\lambda}_{\,\, \nu \mu}
g_{\mu \lambda }\Gamma^{\lambda}_{\,\, \nu \kappa}
-g_{\lambda \nu }\Gamma^{\lambda}_{\,\, \kappa \mu}
-g_{\mu \lambda }\Gamma^{\lambda}_{\,\, \kappa \nu}\\
&=2g_{\lambda \kappa }\Gamma^{\lambda}_{\,\, \mu \nu}
\end{aligned}
$$

which can be inverted to find

$$\Gamma^\lambda_{\,\,\mu\nu}= \frac{1}{2}g^{\lambda \kappa}(\partial_\mu g_{\nu\kappa} + \partial_{\nu}g_{\mu\kappa}-\partial_\kappa g_{\mu \nu})$$

</details>

### Geodesics

Another notion which comes over and over in general relativity, is the notion of geodesic. Particles in a gravitational field follows geodesics of the Levi-Civita connexion.

A curve $\gamma(\tau)$ is sayed to be a geodesic of an affine connexion if it's tangent $u$ vector always satisfies 

$$\boxed{\nabla_u u=0}$$

$u$ is then said to be autoparallel.

With this definition, in a given coordinate chart $x^\mu$, we are able to recover the usual geodesic equation

$$
\frac{\partial^2 x^\lambda}{\partial \tau^2} = - \Gamma^{\lambda}_{\mu \nu}\frac{\partial x^\mu}{\partial \tau}\frac{\partial x^\nu}{\partial \tau}
$$

<details>
  <summary>Proof</summary>

In a given chart $u = \partial_\tau x^\mu \partial_\mu$, where $x^\mu(\tau)$ is the coordinate expression of $\gamma(\tau)$, such that 

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

Hence 

$$
\begin{aligned}
&\nabla_u u = 0\\
&\partial_\tau^2 x^\lambda+ \Gamma^\lambda_{\nu \mu}\partial_\tau x^\nu\partial_\tau x^\mu=0\\
&\frac{\partial^2 x^\lambda}{\partial \tau^2} = - \Gamma^{\lambda}_{\mu \nu}\frac{\partial x^\mu}{\partial \tau}\frac{\partial x^\nu}{\partial \tau}
\end{aligned}
$$
</details>

Torsion does not impact geodesic equations.

Geodesics of the Levi-Civita connection are curves which extremalize the length on a Riemannian manifold. Indeed consider the total length $\mathcal{S}$ of a curve $\gamma(\tau)$ relating two points on the manifold defined as

 $$\mathcal{S}=\int \text{d}s = \int \sqrt{g(u,u)}\text{d}\tau$$

where $u=\gamma'$ is the tangent vector of the curve. In a coordinate frame, the length interval $\text{d}s$ in the above expression can be directly linked to the familiar expression used in General relativity:

$$ \text{d}s^2=g_{\mu\nu}\text{d}x^\mu\text{d}x^\nu$$

<details>
  <summary>Proof</summary>

From the above integral:

$$ \text{d}s^2 = g(u,u)\text{d}\tau^2$$

Now, in a local natural frame $u=\partial_\tau x^\mu\partial_\mu$, where $x^\mu(\tau)$ is the coordinate expression of $\gamma(\tau)$. Hence

$$ 
\begin{aligned}
\text{d}s^2 &= g(\partial_\tau x^\mu\partial_\mu,\partial_\tau x^\nu\partial_\nu)\text{d}\tau^2\\
&= \partial_\tau x^\mu \partial_\tau x^\nu g(\partial_\mu,\partial_\nu)\text{d}\tau^2\\
&=g_{\mu \nu}\partial_\tau x^\mu \partial_\tau x^\nu \text{d}\tau\text{d}\tau\\
&=g_{\mu\nu}\text{d}x^\mu\text{d}x^\nu
\end{aligned}
$$

where we used the shortcut

$$\text{d}x^\mu=\partial_\tau x^\mu \text{d}\tau = \frac{\partial x^\mu}{\partial \tau}\text{d}\tau $$

correct as here $x$ is not the general coordinate frame but the expression of the coordinates of $\gamma(\tau)$. It hence depends only on $\tau$.

</details>


Extremalizing $\mathcal{S}$ thus correspond to find the path $\gamma(\tau)$ extramalizing the metric distance between two points, which is commonly defined as a geodesic curve. We can show that doing this extremalization gives back the geodesic equation above associated with the definition of $\Gamma$ in term of $g$ as the Levi-Civita connection.

<details>
  <summary>Proof</summary>

</details>

### The parallel transporter, parallel transport and projectors 

Let us now better understand the links between the connections just defined and the standard derivative of vectors.

$$\nabla_u u =\frac{\nabla u}{\text{d} \tau} = P_{\gamma(\tau)}\frac{\text{d}u}{\text{d}\tau}$$

### Levi-Civita as a gauge connexion

## Connection on a vector bundle (Koszul connexion)

Recall here that a vector bundle $E$ attaches a vector space $V$, of dimension $d$ and field $\mathcal{F}\in\{\mathbb{R},\mathbb{C}\}$, at every point of a manifold $M$. A point of $E$ is given locally by a pair $(x,s)$, where $x\in M$ is a point of space-time and $s\in V$ is a vector associated to the point $x\in M$. The tangent bundle is hence a special case of vector bundle, associating $\mathbb{R}^d$ to each point of a manifold of dimension $d$. As such, we can generalize the notion of the affine connection on the tangent bundle to a connection on any vector bundle.

Let $E$ be a $\mathcal{F}$-vector (associated) bundle over $M$. A *connection* $\nabla$ can be defined as a map: $TM \times \Gamma(E) \to\Gamma(E)$, that associate $\nabla_v s \in \Gamma(E)$ to the pair $v \in TM$ and $s \in \Gamma(E)$, obeying the following properties:

- $\nabla_{fv}s= f\nabla_vs$ 
- $\nabla_v(\alpha s)= \alpha \nabla_v s$  
- $\nabla_{v+w}s= \nabla_vs + \nabla_ws$  
- $\nabla_v(s+t)= \nabla_vs + \nabla_vt$  
- $\nabla_v(fs)= v(f)s + f\nabla_vs$ 

$\forall v,w \in  TM$, $s,t \in \Gamma(E)$, $f\in C^\infty(M)$ and $\alpha \in \mathcal{F}$. As such, defining $\nabla$ allows to define a proper way to do derivations on $E$. We will again interpret $\nabla_vs$ as the derivative of the section $s$ in the direction pointed by the vector $v$. $\nabla_vs$ is again called the *covariant derivative* of $s$ in the direction $v$ and $\nabla$ is sometimes called a *Koszul connection*.

Let $\partial_\mu$ be a basis of $TM$, we use the standard notation: $\nabla_{\mu}=\nabla_{\partial_\mu}$. Let $e_i$ be a local basis of sections of $E$ over $U \subseteq M$. As $\nabla_\mu e_j$ is also a section of $E$, it can be expressed as:

$$
\nabla_\mu e_j = A^i_{\,\,\mu j}e_i
$$ 

$A^i_{\mu j}$ are then the coordinates of $\nabla_\mu e_j$ in the $e_i$ basis. $A$ is called the *vector potential*. Using the properties listed above, we can then express the coordinates of the covariant derivative of any section $s=s^ie_i$ along $v=v^\mu\partial_\mu$ over $U$:

$$
\nabla_vs = v^\mu(\partial_\mu s^i+A^i_{\,\,\mu j}s^j)e_i
$$

$A$ can be thaught as a $\text{End}(E)$ valued 1-form over $U$: $$A \in \text{End}(E\|_U)\otimes T^*U$$ (that is a map $E\times TM \to E$). In a basis, it can be decomposed as

$$
A = A^i_{\,\,\mu j} \text{d} x^\mu \otimes e_i \otimes e^j
$$

Hence, affine connections are just a special case of Koszul connections defined on the tangent bundle.  

### Gauge/Yang-Mills fields: gauge invariance

## Connection on a principal bundle (Ehresman connection)

Let $P$ be a principal bundle $P\xrightarrow{\pi} M$ with structural group $G$. For all the discussion that will follow, it is useful to think of $P$ as the bundle of all the possible frames of a vector space at every point of $M$. Each frame is connected to another by a transformation of the Lie group $G$. For the tangent bundle, $P=LM$ is the set of all the bases $e_\mu$ on which the vectors can be expressed, linked to one another by transformations of the group $G={\rm GL}(n)$. Locally, a point $p=(e,x)\in P$ is a set $e$ above a point $x\in M$. 

Let $\mathfrak{g}$ be the Lie algebra of $G$. Let $T_pP$ be the tangent space of $P$ at $p$. The tangent vectors $X_p\in T_pP$ can be thought as infinitesimal frame transformations. The projection map $\pi: P\to M$, $\pi(p)=x$ gives back the point $x\in M$ to which the frame $e$ is associated. Identically, $\pi$ can be used to obtain a vector $v\in TM$ above $x$ from the vector $X_p \in T_pP$ as $\pi_*(X_p)=v\in TM$ using the pushforward.

<details>
  <summary>Reminder: pullback and pushforwards</summary>

</details>

Using this map, it is possible to define the vertical subspace $V_pP\subseteq T_pP$ at the point $p$ as

$$
\begin{aligned}
V_pP&= {\rm ker}((\pi_*)_p)\\
&=\{X^\xi\in T_pP \, /\, (\pi_*)_p(X_p)=0\}
\end{aligned}
$$

In our "frame bundle" reading, $V_pP$ corresponds to all the frame transformations which are "pure rotations" (vertical motions in the fiber $G$), which are not associated to translation of the frame over $M$. For each $X^\xi\in V_pP$, we can associate an element of the Lie algebra $\xi$ of $\mathfrak{g}=T_eG$ acting on functions on $P$ as

$$
X^\xi_pf=\frac{\text{d}}{\text{d}t}(f(pe^{t\xi}))\Bigg|_{t=0} = \mathbb{I}(\xi)(f)
$$

where we defined the map $\mathbb{I}:\mathfrak{g}\to T_pP$, $\xi\to X^\xi_p$.

A *Ehresmann connection* on $P$ at $p$ is the choice of an horizontal subspace $H_p\subset T_pP$ such that

$$\boxed{T_pP = H_pP+ V_pP,}$$

and satisfying $\forall g\in G, p\in P$ and $X_p \in H_pP$: $g_* X_p \in H_{pg}P$, i.e. acting with $g$ on an horizontal vector $X_p$ at the point $p$ gives back an horizontal vector at the point $pg$. Once such a choice is made, every vector $X_p\in T_pP$ can be written as

$$X_p = {\rm Ver}(X_p)+ {\rm Hor}(X_p)$$

with ${\rm Ver}(X_p)\in V_pP$ and ${\rm Hor}(X_p)\in H_pP$. A word of caution here, even if $V_pP$ is given by $\pi$ and does not depend on the connection choice, the value of ${\rm Ver}(X_p)$ and ${\rm Hor}(X_p)$ both depends on the connection choice. 

As such, defining a connection defines the notion of horizontality associated to the translations of frames over $M$ and their parallel transport, by identifying locally points of infinitely close nearby fibers. The notion of verticality being intrinsically defined on $P$ by the group action i.e. the "rotations" of the frames on themselves at a given point of $M$.
 
## Connection 1-form on a principal bundle (Cartan connection)

A *Cartan connection* is a 1-form valued in $\mathfrak{g}$, $\omega:TP\to \mathfrak{g}$ satisfying

- $\forall p\in P, \omega_p: T_pP\to \mathfrak{g}$ is an isomorphism of vector spaces.
- $\forall g \in G\,:\, g^*\omega = {\rm Ad}(g^{-1})\omega$.
- $\forall \xi\in \mathfrak{g}, \omega(X^\xi)=\xi$.

with the adjoint application defined as the action of the group on itself as ${\rm Ad}(g):G\to G, h\to ghg^{-1}$.

From an Ehresmann connection, it is possible to associate a Cartan connection as the $\mathfrak{g}$-valued 1-form satisfying 

- $\omega(X^\xi)=\xi$ si $X^\xi\in V_pP$
- $\omega(X)=0$ si $X\in H_pP$


or by using the application $\mathbb{I}: \mathfrak{g}\to T_pP$, $\mathbb{I}(\xi)\to X_p^\xi$ introduced above:

$$
\omega_p(X_p) = \mathbb{I}^{-1}({\rm Ver}(X_p))$$

$H_pP$ can be recovered from $\omega$ as $H_pP={\rm ker}(\omega_p)$.


## Connection on a vector bundle inherited from a principal bundle

### Spin connection and spinors

### Gauge/Yang-Mills fields: gauge invariance

### Shortcut: using representations

### Longer path: horizontal lift and covariant derivative

# Further readings

### For french speakers:

- F. Faure (2022) - [Introduction à la géométrie et la topologie des espaces
fibrés en physique](https://www-fourier.ujf-grenoble.fr/~faure/enseignement/geometrie_topologie_M2/cours.pdf)
- R. Coqueraux (2016) - [Espaces fibrés et connexions](https://www.cpt.univ-mrs.fr/~coque/EspacesFibresCoquereaux.pdf)

### In english:

- J.C. Baez and J.P. Munian (1994) - Gauge Fields, Knots and Gravity - World Scientific Publishing Company
- M. Nakahara (2003) - [Geometry topology and physics](http://alpha.sinp.msu.ru/~panov/LibBooks/GRAV/(Graduate_Student_Series_in_Physics)Mikio_Nakahara-Geometry,_Topology_and_Physics,_Second_Edition_(Graduate_Student_Series_in_Physics)-Institute_of_Physics_Publishing(2003).pdf) - IOP
- T. Frankel (2011) - The Geometry of Physics: An Introduction - Cambridge University Press
- S. Kobayashi and K. Nomizu (1996) - Foundations of Differential Geometry - John Wiley & Sons