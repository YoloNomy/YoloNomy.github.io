---
layout: default
title: Probability spaces
parent: maths
nav_order: 1
---

We will now define the key concepts of topology. These concepts might seem at first very abstract, but they will reveal to be extremely powerful. We will try to provide examples which will hopefully clarify all of this little by little.
The key to topology is to associate structures to a set which will allow to distinguish between points of the sets, local properties such as proximity and continuity.

## Topology and topological spaces

### Definition

Let $M$ be a [set](tbd). Let $\mathcal{P}(M)$ be the [power-set](tbd) of $M$. A **topology** $\tau \subseteq \mathcal{P}(M)$ on $M$ is a collection of subsets of $M$, called **open sets**, such that:

- The **original set** itself and the **empty set** are open sets.
- The union of (finitely or infinitely many) open sets, is also an open set. $\tau$ is said to be **closed under finite and infinite unions**
- The intersection of finitely many open sets is an open set. $\tau$ is said to be **closed under finite intersections**.

More formally, we rewrite these conditions as:

- $M\in \tau$ and $\varnothing \in \tau$
- For any sequence $\mathbb{N}\to \tau$ with an finite or infinite number of terms: $U_1, U_2, ... = \\{U_n\\}_{n\in \mathbb{N}}$, 
 
  $$\bigcup_{n=1} U_n \in \tau$$.

- Let $k\in \mathbb{N}$. For any finite sequence $\mathbb{N}\to \tau$ containing $k$ terms, $U_1, U_2, ..., U_k = \\{U_n\\}_{n\leq k\in \mathbb{N}}$, 
 
  $$\bigcap_{n=1}^k U_n \in \tau$$.

The pair $(M, \tau)$ is called a **topological space**. We note $U^c = U \backslash M$ the complement of the set $U$. A set $V$ is called a **closed set** if its complement $V^c$ is an open space.

### Examples

- The set $\tau_{0} = \\{\varnothing, M \\}$ is a topology and $(M,\tau_0)$ is a topological space. This is the simplest possible topology, called the **trivial topology**, the **indiscrete topology** or the **chaotic topology**. 

### Consequences of the definition

1. Openness and closeness are not mutually exclusive conditions! For example, $M$ and $\varnothing$ are both open and closed spaces sets in any topology. Sometimes it is said that such spaces are "clopen".

<details markdown="1">
  <summary><strong>Proofs</strong></summary>
 
1. By definition of the topology $M\in \tau$ and $\varnothing \in \tau$, both spaces are thus open. But $M^c = \varnothing$ and $\varnothing^c=M$, so the complement of both spaces are also open, hence they must also be closed.

</details>


### Remarks:

- Different from a [$\sigma$-algebra](../measure_theory/sigma_algebra.md).


## Further reading and watching

- [Geometry, topology and physics - M. Nakahara (2003) - IOP Publishing](http://www.stat.ucla.edu/~ywu/GTP.pdf)
