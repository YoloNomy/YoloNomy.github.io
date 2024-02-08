---
layout: default
title: Curvature
has_children: False
nav_order: 5
---

# Curvature

Curvature is a key concept of fundamental physics. While you are probably thinking about its role in general relativity, it is also central for gauge theories and have some applications in all branches of physics. 
As we will see, curvature is a subtle and deeply geometrical concept and you probably already have a rather good intuition of it. We will try to put some formal content on these intuitions and extend them to various types of abstract spaces.
While you might think that curvature is a property of a given space (i.e. of a manifold), it is actually a property of the connection.

## Curvature of an affine connection

Let us again start with a rather abstract definition. $R$ is an ${\rm End}(TM)$ valued 2-form. $R: TM\times TM\times TM \to TM$. It is defined by its action on three vector fields $v,w,z\in TM$ as

$$
\boxed{R(v,w)z = \left([\nabla_v,\nabla_w] - \nabla_{[v,w]}\right)v.}
$$

From this definition, we can express the coordinates of $R$ in a basis as

$$R= R^{\lambda}_{\,\,\mu\nu\rho} \partial_\lambda \otimes \text{d}x^\mu\otimes \text{d}x^\nu\otimes \text{d}x^\rho $$

with 

$$R^{\lambda}_{\,\,\mu\nu\rho}= \partial_\mu\Gamma^{\lambda}_{\,\,\nu\rho} - \partial_\nu\Gamma^{\lambda}_{\,\,\mu\rho} + \Gamma^{\tau}_{\,\,\nu\rho}\Gamma^{\lambda}_{\,\,\mu\tau} - \Gamma^{\tau}_{\,\,\mu\rho}\Gamma^{\lambda}_{\,\,\nu\tau}$$

$$R^{\lambda}_{\,\,\mu\nu\rho}$$ are called the *Riemann tensor* coefficients.

<details>
  <summary>Proof</summary>

Consider the action of $R$ on a frame basis $\partial_\mu$, $\partial_\mu$ and $\partial_\nu$

$$
\begin{aligned}
R(\partial_\mu,\partial_\nu)\partial_\rho &=  \left([\nabla_\mu,\nabla_\nu] - \nabla_{[\partial_\mu,\partial_\nu]}\right)\partial_\rho\\
&=\nabla_\mu \nabla_\nu\partial_\rho - \nabla_\nu\nabla_\mu\partial_\rho - \nabla_{[\partial_\mu,\partial_\nu]}\partial_\rho \\
&= \nabla_\mu \nabla_\nu\partial_\rho - \nabla_\nu\nabla_\mu\partial_\rho \qquad \qquad && \text{Partial derivative commutes $[\partial_\mu,\partial_\nu]=0$ (natural frame is orthonormal)}\\
&= \nabla_\mu \Gamma^{\lambda}_{\,\,\nu\rho}\partial_\lambda - \nabla_\nu\Gamma^{\lambda}_{\,\,\mu\rho}\partial_\lambda && \text{definition of the action of $\nabla$ on basis vectors}\\
&= \partial_\mu\Gamma^{\lambda}_{\,\,\nu\rho}\partial_\lambda + \Gamma^{\lambda}_{\,\,\nu\rho}\Gamma^{\tau}_{\,\,\mu\lambda}\partial_\tau - \partial_\nu\Gamma^{\lambda}_{\,\,\mu\rho}\partial_\lambda - \Gamma^{\lambda}_{\,\,\mu\rho}\Gamma^{\tau}_{\,\,\nu\lambda}\partial_\tau && \text{Leibniz rule ($\Gamma^{\lambda}_{\,\,\nu\rho}$ are functions)}\\
&= \left(\partial_\mu\Gamma^{\lambda}_{\,\,\nu\rho} - \partial_\nu\Gamma^{\lambda}_{\,\,\mu\rho} + \Gamma^{\tau}_{\,\,\nu\rho}\Gamma^{\lambda}_{\,\,\mu\tau} - \Gamma^{\tau}_{\,\,\mu\rho}\Gamma^{\lambda}_{\,\,\nu\tau}\right)\partial_\lambda
\end{aligned}
$$

From the decomposition in a basis $R= R^{\lambda}_{\,\,\mu\nu\rho} \partial_\lambda \otimes \text{d}x^\mu\otimes \text{d}x^\nu\otimes \text{d}x^\rho$, the above derivation should be 

$$ R(\partial_\mu,\partial_\nu)\partial_\rho = R^{\lambda}_{\,\,\mu\nu\rho} \partial_\lambda$$

Hence proving that

$$R^{\lambda}_{\,\,\mu\nu\rho}= \partial_\mu\Gamma^{\lambda}_{\,\,\nu\rho} - \partial_\nu\Gamma^{\lambda}_{\,\,\mu\rho} + \Gamma^{\tau}_{\,\,\nu\rho}\Gamma^{\lambda}_{\,\,\mu\tau} - \Gamma^{\tau}_{\,\,\mu\rho}\Gamma^{\lambda}_{\,\,\nu\tau}$$
</details>

## Holonomy and Gauss theorem

## Curvature of a Koszul connections 

Let $E$ be a vector bundle over $M$ equipped with a connection $\nabla$. The curvature $F$ is a End($E$) valued 2-form ($F \in \Omega^2(M)\otimes \text{End}(E)$), that is a map $TM \times TM \times \Gamma(E) \to \Gamma(E)$) quantifying the commutativity of $\nabla$ in two directions $v$ and $w$. It is defined by it's action on a pair of vectors $v,w\in TM$ and a section $s\in\Gamma(E)$ as

$$
\boxed{F(v,w)s = ([\nabla_v,\nabla_w] - \nabla_{[v,w]})s}
$$

We can check that $F$ is indeed a member of $\Omega^2(M)\otimes \text{End}(E)$ as it satisfies antisymetry and bilinearity.

Over a chart $U$ with coordinates $x^\mu$ and basis of the section bundle $e_i$ (i.e. a section of the principal bundle), $F$ can be understood as a tensor with components 

$$
F = F^i_{\,\, j\mu \nu} e_i \otimes e^j \otimes \text{d} x^\mu \otimes \text{d} x^\nu  
$$

Recalling that $\text{d} x^\mu \wedge \text{d} x^\nu$ is the basis of $\Omega^2(M)$ and $e_i \otimes e^j$ a basis of End($E$).

In term of the connexion 1-form, the components of $F$ can also be written as

$$
F^i_{\,\,j\mu \nu} = \partial_\mu A^{i}_{\,\,j\nu} - \partial_\nu A^{i}_{\,\,j\mu} + [A_{\mu}, A_{\nu}]^{i}_{\,\,j}
$$

This is called the second Cartan structure equation.

<details>
  <summary>Proof</summary>

Consider the action of $F$ on section of basis $e_j$, $\partial_\mu$ and $\partial_\nu$. Similarly to the proof for the Riemann's tensor coefficients:

$$
\begin{aligned}
F^{i}_{\,j\mu \nu}e_i=F(\partial_\mu,\partial_\nu)e_j&= ([\nabla_\mu,\nabla_\nu] - \nabla_{[\mu,\nu]} )e_j\nonumber\\
&= \nabla_\mu \nabla_\nu e_j -\nabla_\nu \nabla_\mu e_j - \nabla_{[\mu,\nu]}e_j\nonumber\\
&= \nabla_\mu(A^{i}_{\,\,j \nu}e_i) - \nabla_\nu (A^{i}_{\,\,j \mu}e_i)  - \nabla_{[\mu,\nu]}e_j\nonumber\\
&= \partial_\mu A^{i}_{\,\,j \nu}e_i + A^{i}_{\,\,j \mu}A^{k}_{\,\,i \nu}e_k -\partial_\nu A^{i}_{\,\,j \mu}e_i- A^{i}_{\,\,j \nu}A^{k}_{\,\,i \mu}e_k \nonumber\\
&=\left(\partial_\mu A^{i}_{\,\,j\nu} - \partial_\nu A^{i}_{\,\,j\mu} + (A^{k}_{\,\,j \mu}A^{i}_{k \nu}-A^{k}_{\,\,j \nu}A^{i}_{\,\,k \mu})\right)e_i \nonumber
\end{aligned}
$$

</details>


More generally, one writes 

$$
F = \text{d} A + [A \wedge A]_{\mathfrak{g}}
$$

with

$$
[A\wedge A](x,y)=[A(x),A(y)]_{\mathfrak{g}}
$$

In the litterature, this term is often written simply $A\wedge A$, which can be quite confusing. 


## Covariant exterior derivative

From the definition of a connection $\nabla$ on a vector bundle, it is possible to define the exterior covariant derivative $\text{d}^\nabla$, as a generalisation $\text{d}$ satisfying the condition

$$ d^{\nabla}s(v)=\nabla_v(s)$$

where $s\in \Gamma(E)$ and $v\in TM$.

## Curvature of Koszul connections from the covariant exterior derivative

While we defined the curvature of a Kozsul connection on a general vector bundle identically as we did for the affine connection, it is also possible to define it quite elegantly from the exterior covariant derivative as

$$\boxed{F = (d^{\nabla})^2}$$

When acting on vectors, this definition gives back our previous definition

$$ F_{\mu\nu}= [\nabla_\mu,\nabla_\nu] -\nabla_{[\mu,\nu]}$$

<details>
  <summary>Proof</summary>

</details>

And the components

$$
F^i_{\,j\mu\nu} = A^i_{\,k\mu}\wedge A^k_{\,j\nu} +\partial_\nu A^i_{\,j\mu}
$$

can be found back directly from the definition using the properties of $\text{d}^\nabla$.

<details>
  <summary>Proof</summary>

$$
\begin{aligned}
F(e_j) &= (\text{d}^\nabla)^2(e_j) \nonumber \\
&= \text{d}^\nabla(\nabla e_j) \nonumber \\
& = \text{d}^\nabla(e_i A^i_{\,j}) \nonumber \\
&= \text{d}^\nabla(e_i)\wedge A^i_{\,j} + (-1)^0 e_i \wedge \text{d} A^i_{\,j}\nonumber \\
&= e_k A^k_{\,i}\wedge A^i_{\,j} + e_i \text{d} A^i_{\,j}\nonumber \\
&= e_k(A^k_{\,i}\wedge A^i_{\,j} +\text{d} A^k_{\,j})\nonumber \\
\end{aligned}
$$
</details>

## Curvature of a Cartan connection from the $D$ operator

Let $\omega$ be a Cartan connection on a principal bundle $P$.
It's curvature is defined as

$$ F=D\omega$$

## Gauge curvature, electromagnetism and chromodynamics

### Electromagnetism

### Non-abelian gauge theories

In particle physics textbook, you will find different notations for the curvature, which are all equivalent

$$
\begin{aligned} (F_{\mu \nu})^{i}_{\,j}&= \partial_\mu A^\alpha_\nu (t_\alpha)^{i}_{\,j} - \partial_\nu A^\alpha_\mu (t_\alpha)^{i}_{\,j} + ig A^\alpha_\mu A^\beta\nu [t_\alpha,t_\beta]^{i}_{\,j}\\
&=\partial_\mu A^\alpha_\nu (t_\alpha)^{i}_{\,j} - \partial_\nu A^\alpha_\mu (t_\alpha)^{i}_{\,j} + ig A^\alpha_\mu A^\beta_\nu f^\gamma_{\alpha \beta} (t_\gamma)^{i}_{\,j}
\end{aligned}
$$

and the internal indices as well as the generators are often absorbed for more compact, but yes more opaque notations as

$$F_{\mu\nu}= \partial_\mu A_\nu -\partial_\nu A_\mu + ig [A_\mu,A_\nu]$$

$$ \mathcal{S}=\int \sqrt{-g} F_{\mu\nu}F^{\mu\nu} \text{d}^4x$$

$$\mathcal{S}=\int {\rm tr}_{\mathfrak{g}}(F \wedge \star F)$$

# Further readings

### For french speaker:

- F. Faure (2022) - [Introduction à la géométrie et la topologie des espaces
fibrés en physique](https://www-fourier.ujf-grenoble.fr/~faure/enseignement/geometrie_topologie_M2/cours.pdf)
- R. Coqueraux (2016) - [Espaces fibrés et connexions](https://www.cpt.univ-mrs.fr/~coque/EspacesFibresCoquereaux.pdf)

### In english:

- J.C. Baez and J.P. Munian (1994) - Gauge Fields, Knots and Gravity - World Scientific Publishing Company
- M. Nakahara (2003) - [Geometry topology and physics](http://alpha.sinp.msu.ru/~panov/LibBooks/GRAV/(Graduate_Student_Series_in_Physics)Mikio_Nakahara-Geometry,_Topology_and_Physics,_Second_Edition_(Graduate_Student_Series_in_Physics)-Institute_of_Physics_Publishing(2003).pdf) - IOP
- T. Frankel (2011) - The Geometry of Physics: An Introduction - Cambridge University Press
- S. Kobayashi and K. Nomizu (1996) - Foundations of Differential Geometry - John Wiley & Sons