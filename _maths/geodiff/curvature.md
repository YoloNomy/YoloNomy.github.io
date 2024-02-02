---
layout: default
title: Connexions
has_children: False
nav_order: 5
---

# Curvature

## Curvature of an affine connection

$$
R_{v,w}z = \left([\nabla_v,\nabla_w] - \nabla_{[v,w]}\right)v.
$$

$$R^{\lambda}_{\,\,\mu\nu\rho}= $$

## Holonomy and Gauss theorem

## Defining curvature

Let $E$ be a vector bundle over $M$ equipped with a connection $\nabla$. The curvature $F$ is a End($E$) valued 2-form ($F \in \Omega^2(M)\otimes \text{End}(E)$), that is a map $TM \times TM \times \Gamma(E) \to \Gamma(E)$) quantifying the commutativity of $\nabla$ in two directions $v$ and $w$. It is defined by it's action on a pair of vectors $v,w\in TM$ and a section $s\in\Gamma(E)$ as

$$
F(v,w)s = ([\nabla_v,\nabla_w] - \nabla_{[v,w]} )s
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

Consider the action of $F$ on section of basis $e_j$, $\partial_\mu$ and $\partial_\nu$

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
F = \text{d} A + [A \wedge A]
$$

with

$$
[A\wedge A](x,y)=[A(x),A(y)]_{\mathfrak{g}}
$$

In the litterature, this term is often confusingly written $A\wedge A$. 


## Covariant exterior derivative

From the definition of a connection $\nabla$ on a vector bundle, it is possible to define the exterior covariant derivative $\text{d}^\nabla$, as a generalisation $\text{d}$ satisfying the condition

$$ d^{\nabla}s(v)=\nabla_v(s)$$

where $s\in \Gamma(E)$ and $v\in TM$.

## Defining the curvature

$$ F = (d^{\nabla})^2$$

Which gives back

$$
F^i_{\,j\mu\nu} = A^i_{\,k\mu}\wedge A^k_{\,j\nu} +\partial_\nu A^i_{\,j\mu}
$$

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

Another way to define curvature

$$ F=D\omega$$



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