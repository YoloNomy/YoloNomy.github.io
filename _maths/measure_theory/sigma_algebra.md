--- 
layout: default 
title: Sigma algebras
parent: maths  
nav_order: 1  
--- 

We will now define key concepts that are central to probability theory. Just as for topology, this might seem at first very abstract and will reveal useful later. The challenge is to define general spaces, the $\sigma$-algebra, on which it will be possible to define a notion of measure and measurability. This measure will match the intuition that we have of notions such as **surfaces** or **volumes**. Such notions will thus intersect in a subtle way with concepts of topology and differential geometry. In particular, they will allow us to define a powerful and modern way to understand integration (the Lebesgue integral), which itself rely on the given of a measure.

We will also see that, in this context, **probability** can be interpreted as a specific kind of measure on the space of possibilities, which is itself a specific kind of $\sigma$-algebra. Measure theory thus also provides a modern and powerful way to understand such a subtle concept.

## Sigma Algebra and measurable spaces

### Definition

Let $M$ be a [set](tbd). Let $\mathcal{P}(M)$ be the [power-set](tbd) of $M$. A $\sigma$-algebra on $M$ is a subset $\Sigma \subseteq \mathcal{P}(M)$ (i.e. a collection of subsets of $M$), such that $\Sigma$ is non-empty and:

- If a set $A$ is in the $\sigma$-algebra, then it's complement is also in the $\sigma$-algebra. We say that $\Sigma$ is **closed under complements**.
- The infinite union of members of the $\sigma$-algebra is also a member of the $\sigma$-algebra. We say that $\Sigma$ is **closed under infinite countable unions**.

More formally, we rewrite these conditions as:

- If $A \in \Sigma$, then $A^c \in \Sigma$, where $A^c= A\backslash M$ note the complement of $A$. 
- For any sequence $\mathbb{N}\to \Sigma$ with an infinite number of terms $A_1, A_2, ... = \\{A_n\\}_{n\in \mathbb{N}}$, 
    
    $$\bigcup_{n=1}^\infty A_n \in \Sigma$$.

A **measurable space** is a pair $(M,\Sigma)$ where $M$ is a set and $\Sigma$ is a $\sigma$-algebra on $M$. 

### Examples

- The entire power-set $\mathcal{P}(M)$ of a set $M$ is a $\sigma$-algebra, and $(M,\mathcal{P})$ is a measurable space. 

### Consequences of the definition

1. For any sequence $\\{A_n\\}_{n\in \mathbb{N}}$, 
    
    $$\bigcap_{n=1}^{\infty} A_n \in \Sigma$$ 
    
    We say that $\Sigma$ is **closed under (infinite) countable intersections**.

2. $\Sigma$ is also closed under finite countable unions and intersections. That is, for any sequence $A_n$, for all $k\in \mathbb{N}$, $\bigcup_{i=1}^k A_n \in \Sigma$ and $\bigcap_{i=1}^{k} A_n \in \Sigma$. 
3. The original set $M$ is always a member of the $\sigma$-algebra: $M\in \Sigma$.
4. The empty set is a always a member of the $\sigma$-algebra:  $\varnothing \in \Sigma$

<details markdown="1">
  <summary><strong>Proofs</strong></summary>
 
1. To prove this, we assume [De Morgan’s laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws) from set theory, allowing us to transform unions into intersections:

    $$
    \bigcup_{i=1}^{\infty} A_i^c = \left(\bigcap_{i=1}^{\infty} A_i\right)^c
    $$

    Using this law, we can write:
    
    $$
    \bigcup_{i=1}^{\infty} A_i = \bigcup_{i=1}^{\infty} (A_i^c)^c=\left(\bigcap_{i=1}^{\infty} A_i^c \right)^c
    $$

    Each $E_i^c$ are in $\Sigma$ (closed under complements). $ \bigcap_{i=1}^{\infty} A_i^c$ is also in $\Sigma$ (closed under countable unions). And $\left(\bigcap_{i=1}^{\infty} A_i^c \right)^c$ is in $\Sigma$ (closed under complements). So $\bigcup_{i=1}^{\infty} A_i \in \Sigma$.
2. Let $A_n$ be an infinite sequence in $\mathbb{N}$ and $k \in \mathbb{N}$. Let $B_n= A_n$ for $0\leq n\leq k$ and $B_n=\varnothing$ for $n>k$. $$\{B_n\}_{n \in \mathbb{N}}$$ is a sequence in $\Sigma$. Then, since $\Sigma$ is closed under infinite countable unions and intersection : $\bigcup_{n=1}^\infty B_n \in \Sigma$ and $\bigcap_{n=1}^\infty B_n \in \Sigma$. 

    $$\bigcup_{n=1}^\infty B_n =\left(\bigcup_{n=1}^k B_n\right) \cup \left(\bigcup_{n=k+1}^\infty B_n\right) = \bigcup_{n=1}^k B_n \in \Sigma$$

    $$\bigcap_{n=1}^\infty B_n = \left(\bigcap_{n=1}^k B_n\right) \cap \left(\bigcap_{n=k+1}^\infty B_n\right) = \bigcap_{n=1}^k B_n \in \Sigma$$

    So, $\Sigma$ is closed under finite unions and intersections.
3. Let $A \in \Sigma$. $\Sigma$ is closed under complements, so $A^c \in \Sigma$. $A$ is also closed under countable unions, so $A \cup A^c \in \Sigma$ (from 2.). Since $M= A \cup A^c$, $M \in \Sigma$.
4. From 1., $M\in \Sigma$. Since $\Sigma$ is closed under countable unions, $M^c = M \backslash M = \varnothing \in \Sigma$

</details>

### Remarks:

- Similar but different from a [topology](../geodiff/topology.md).
- Is not an algebra in the sence of vector spaces.


<details markdown="1">
  <summary><strong> Supplement:</strong> Differences with a topology</summary>
 
</details>

## Measure and measure space

### Definition

Let $(M,\Sigma)$ be a measurable set. A **measure** $\mu$ on $(M,\Sigma)$ is a function: 

$$\mu : \Sigma \to [0, \infty] $$

Such that:

- The measure of the empty set is zero, that is:
    $$\mu(\varnothing)=0$$
- Consider a sequence $\mathbb{N}\to \Sigma$, $\\{A_n\\}_{n\in \mathbb{N}}$, such that $A_i \cap A_j=\varnothing$,$\forall i \neq j$. Such a sequence is said to be **pairwise disjoint**. Then:
  
  $$ \mu\left(\bigcup_{n=1}^\infty A_n \right)= \sum_{n=1}^\infty \mu(A_n)$$

## Further reading and watching

- [An introduction to measure theory - Terrence Tao - American Mathematical Society](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf)
- [Probability primer - mathematicalmonk - Youtube videos](https://www.youtube.com/playlist?list=PL17567A1A3F5DB5E4)
- [Lectures on Quantum Theory - F. P. Schuller -  Youtube videos](https://www.youtube.com/playlist?list=PLPH7f_7ZlzxQVx5jRjbfRGEzWY_upS5K6)