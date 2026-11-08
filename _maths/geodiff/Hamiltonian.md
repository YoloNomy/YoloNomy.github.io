---
layout: default
title: Hamiltonian mechanics and symplectic geometry 
parent: maths
nav_order: 1
---

## Phase space and its symplectic geometry

Let's consider a physical system described by its **configuration space** $\mathcal{Q}$. We saw in the previous lecture that the evolution of the system on $\mathcal{Q}$ can be described by finding the extremum of its action functional, expressed as the time integral of the Lagrangian function $L(q,\dot{q})$ defined on the tangent space $T\mathcal{Q}$, on which velocities are defined. As a reminder, a point of $T\mathcal{Q}$ is a doublet $(q,v)$, where $q$ is a generalized position and $v$ a velocity/tangent vector.

Alternatively, it is possible to describe its evolution on the cotangent space of $\mathcal{Q}$, also known as the **phase space** $\mathcal{P} = T^{\*} \mathcal{Q}$. A point in phase space is given by the doublet of a point of $\mathcal{Q}$ and a covector, noted $p$, that we will identify with momentum. Hence a point $x$ of phase space is labelled as $x=(q,p)\in \mathcal{P}$.

Working in phase space instead of tangent space has several advantages. The most important one being that it renders apparent a special geometrical structure of classical mechanics: **symplectic geometry**. This geometry allows to understand deep parallels between classical and quantum mechanics and thus investigate general **quantization procedures**, looking for a general and rigorous path to go from classical to quantum systems. This is for example the case of the so-called **geometric quantization**. 

Before going through this lecture, we recommend to first have a look at our previous lectures on [Hamiltonian mechanics](../../_meca/Analytical/Hamiltonian.md) and [Phase space for statistical physics](../../_thermo/statistical/phasespace.md).

### Phase space: thinking the cotangent bundle as a manifold of its own

A one-form field $\alpha$ on $\mathcal{Q}$ is an object that takes a vector and returns a number in each point, or put differently it takes a vector field $$v \in T\mathcal{Q}$$ and returns a function $$f = \alpha(v)$$. One forms act **linearly** $$\alpha(a v_1+b v_2)=a \alpha(v_1) + b\alpha(v_2)$$ for $a,b \in \mathbb{R}$ and $v_1,v_2\in T\mathcal{Q}$ (Contrarily, for example, to the lagrangian $L(q,v)$ which takes a vector and return a number but is not linear). Consider now a chart on $\mathcal{Q}$, $q\to q^i: U \to \mathbb{R}^n$. Locally, a general one form field on $\mathcal{Q}$ can be written as $\alpha= P_i(q)\text{d}q^i \in \Gamma(T^{\*}\mathcal{Q})$ (here and everywhere below, if an index is repeated, it is summed over). It acts on a vector field $v= v^i \partial_{q_i}$ as $$\alpha(v) = P_iv^i$$.
When thinking of $\mathcal{P}=T^{\*}\mathcal{Q}$ as its own independent space, we consider every possible values of $P_i(q)$ at each point $q$, and promote it to its own coordinate, that we name $p_i$.
More precisely: it is always possible to find local coordinates on a chart $U \subseteq \mathcal{Q}$ such that a point $q\in \mathcal{Q}$ is labeled by coordinates $q^i$. Once the $q_i$ are chosen, we label $p_i$ the associated one-form coordinate such that $q_i$ and $p_i$ form **canonical coordinates** (What does it mean?). As such, a general point $x\in \mathcal{P}$ is given by the tuple $x=(q^1, ..., q^{3\mathcal{N}},p_1, ..., p_{3\mathcal{N}})$. Where $\mathcal{N}$ is the number of particles if $\Pi$ describes a set of point-like particles allowed to move in three dimensions. The data of a point $x\in \mathcal{P}$ is called a **classical state**.

A general one form field on $\mathcal{P}$ is written

$$\eta =  A_i(q,p)\text{d}q^i  +  B^i(q,p)\text{d}p_i$$

which is a section of $T^{\*}(\mathcal{P}) = T^{\*}(T^{\*}\mathcal{Q})$, $\eta \in \Gamma(T^{\*}(\mathcal{P}))$ and the coordinates $A_i$ and $B^i$ are functions of $C^{\infty}(\mathcal{P})$, (i.e. $A_i: \mathcal{P}\to\mathbb{R}$ and $B^i: \mathcal{P}\to\mathbb{R}$). Similarly, a general vector field on $\mathcal{P}$ is written as

$$Y= u^i(q,p) \partial_{q^i} +  v_i(q,p)\partial_{p_i}$$

with $Y\in \Gamma(T\mathcal{P})$ and the coordinates $u^i$, $v_i$ are functions of $C^{\infty}(\mathcal{P})$.

### Tautological and symplectic forms

The phase space inherits a peculiar geometry through the existence of the so-called **tautological one-form**. It is also known as Liouville one-form, the Poincaré one-form, the canonical one-form, or the symplectic potential. 
Once a coordinate chart is chosen, the tautological one form is defined as the special choice of one form field with $A_i(q,p)=p_i$ and $B_i=0$, that is:

$$\boxed{\theta =  p_i \text{d} q^i}$$

As discussed below the value of $\theta$ is independent of the choice of local coordinates, and admits a coordinate independent definition.

<details markdown="1">
  <summary><strong>More details on the tautological form</strong></summary>

Let's assume that the phase space $\mathcal{P}$ is indeed the cotangent bundle $T^*\mathcal{Q}$ of some configuration space $\mathcal{Q}$. As a fiber bundle, $\mathcal{P}$ is equipped with a projection map $\pi$ to its base space:

$$
\pi:T^*\mathcal Q\to\mathcal Q
$$

For a point $(q,p)\in T^*\mathcal Q$, we consider a tangent vector of phase space at this point:

$$
X\in T_{(q,p)}(T^*\mathcal Q),
$$

Using the **pushforward** $$\pi_*:T(T^*\mathcal Q)\to T\mathcal Q$$, it is possible to obtain a vector $\pi_*(X)$ on $T_q\mathcal{Q}$ from the vector $X \in T\mathcal{P}$. Once pushed forward on the configuration space, the one-form $p:T\mathcal{Q}\to \mathbb{R}$ -- coresponding to the original phase-space coordinate where $X$ was defined -- can act on it to give a number as $$p(\pi_*(X))$$. As such, the tautological one-form is defined by

$$
\boxed{
\theta_{(q,p)}(X)
=
p\bigl(\pi_*X\bigr)
}
$$

Or, equivalently: 

$$\boxed{\theta_{(q,p)} = p \circ \pi_*}$$

Computing this value at every point $x=(q,p)$ of $\mathcal{P}$, one obtain a 1-form field.

Clearly, this definition does not depend on any choice of coordinatization of $\mathcal{P}$. Indeed, careful, here $p$ is not $p_i$! $p$ labels a point of $\mathcal{P}$ which is itself a covector on $\mathcal{Q}$, there is no need yet to introduce local charts.

Choosing local coordinates $$(q_i,p_i)$$ allows to express the tautological form as  

$$
\theta=p_i\,\mathrm dq^i.
$$

Indeed, consider a general vector at the point $q,p$:

$$X= u^i \partial_{q^i} +  v_i\partial_{p_i}$$

The pushforward is:

$$\pi_*(X) = u^i\partial_{q^i}$$

Now, the one-form $p_i\text{d}q^i \in T^*_q(\mathcal{Q})$ can act on it to give

$$\theta(X)=p(\pi_*(X)) = p_i u^i$$
 
which correspond to the coordinate expression given above using $$\theta = p_i\,\mathrm dq^i$$.
As subtle point: while $p=p_i\text{d}q^i$ is a one form on $\mathcal{Q}$, $$p \circ \pi_*= p_i \text{d}q^i + 0 \text{d}p_i$$ is a one form on $\mathcal{P}$. While both take the same form in coordinates, they are thus different objects.

</details>

A symplectic manifold is a pair $(M,\omega)$, with $M$ a smooth manifold and $\Omega$ a symplectic form.
A 2-form field $\omega \in \Omega^2(\mathcal{P}_s)$ is said to be a **sympletic form** if

- $\omega$ is **closed** i.e. $\text{d}\omega = 0$.
- $\omega$ is **non-degenerate**: If there exist $X \in T\mathcal{\mathcal{P}}$ such that $\forall Y\in T\mathcal{\mathcal{P}}$, $\omega(X,Y)=0$, then $
X=0$.

$\theta$, already present necessarily on $\mathcal{P}$, endows the phase space with a symplectic structure. Indeed, taking its exterior derivative, one obtains the **symplectic form** defined as

$$\boxed{\Omega := -\text{d}\theta}$$

The minus sign is inserted here only by convention, in order to recover expressions more familiar to physicists (several textbook use instead the opposite convention $\Omega=\text{d}\theta$ and one should be careful about it, as it will change the sign of multiple expressions below). $\Omega$ can be expressed in local coordinates as

$$\boxed{\Omega=\text{d}q^i\wedge \text{d}p_i}$$

The pair $(\mathcal{P},\Omega)$ is a symplectic manifold.

<details markdown="1">
  <summary><strong>Proof that $\Omega$ is a symplectic form</strong></summary>

**On the definition of $\Omega$:**

First, we recall that, by definition of $\text{d}$, for $p$-form $\alpha$ and a $k$ form $\beta$:

$$\text{d}(\alpha \wedge \beta) =  \text{d}\alpha \wedge \beta + (-1)^k \alpha \wedge \text{d}\beta $$

Hence 

$$
\begin{align}
\text{d}\theta &= \text{d}( p_i \text{d}q^i)\\
&= \text{d}( p_i \wedge \text{d}q^i)\\
&= \text{d}p_i\wedge \text{d}q^i -  p_i \wedge \text{d}^2q^i\\
&=  \text{d}p_i\wedge \text{d}q^i 
\end{align}
$$

Because $\text{d}^2=0$.
Then 

$$
\begin{align}
\Omega &= -\text{d}\theta\\
&= - \text{d}p_i\wedge \text{d}q^i \\
&= \text{d}q^i\wedge \text{d}p_i
\end{align}
$$

From the antisymmetry of the wedge product ($\alpha \wedge \beta = -\beta \wedge \alpha$). 

**$\Omega$ is closed:**

Now, $\Omega$ is clearly closed by being the exterior derivative of a form (of the form $-\theta$) and from the defining property $\text{d}^2=0$.

**$\Omega$ is non-degenerate:**

Let $X=A_i \partial_{q^i} + B^i \partial_{p_i}$. 

Hence $\Omega$ is non-degenerate.

</details>

As a two-form, $\Omega$ defines a product between two vectors $X,Y \in T\mathcal{P}$ as $\Omega(X,Y)$. In coordinates, if $X=A^i\partial_{q^i}+ B_i\partial_{p_i}$ and $Y=  u^i\partial_{q^i} +  v_i\partial_{p_i}$, we have 

$$\boxed{\Omega(X,Y)=  A^i v_i - B_iu^i.}$$ 

From this equation, we see that, when applied to a unique vector, we obtain $\Omega(X,X)=0$.
Hence $\Omega$ plays an analogous role as the metric $g$ on Riemannian space, endowing it with a very different geometric structure (which is anti-symmetric instead of symmetric and gives a zero "length" to vectors. Compare for example to the simplest Euclidian metric which would give instead $g(X,Y)=A^iu^i + B_iv_i$). 

<details markdown="1">
  <summary><strong>Proof</strong></summary>

$$
\begin{align}
    \Omega(X,Y) &= (\text{d}q^i\wedge \text{d}p_i)(X,Y) \nonumber \\
    &= (\text{d} q^i \otimes \text{d} p_i -\text{d} p_i \otimes \text{d} q^i)(X_F,Y) \nonumber \\
    &= ( \text{d} q^i \otimes \text{d} p_i)(X,Y) - ( \text{d} p_i \otimes \text{d} q^i)(X,Y)\nonumber \\
    & = \text{d} q^i(X) \text{d} p_i(Y) -  \text{d} p_i(X) \text{d} q^i(Y) \nonumber \\
    &= A^i v_i - B_iu^i
\end{align}
$$

Recalling that, from the definition of the exterior derivative, $\text{d}f(v)=v(f)$, and thus, for example:

$$
\begin{align}
\text{d}q^i(X) = X(q^i) &= (A^i\partial_{q^i}+ B_i \partial_{p_i})(q^i) \\
&= A^i \frac{\partial q^i}{\partial q^i} + B_i \frac{\partial q^i}{\partial p_i}\\
&= A_i 
\end{align}
$$

</details>

### Musical isomorphisms 

Now, in Riemannian geometry, $g$ can be used to "lower" or "raise" indices, that is, it can be used to associate a covector field to every vector field and vice versa. In physicist language, we would write this, for example, $v_a = g_{ab}v^b$ or $v^a = g^{ab}v_b$. The proper way to do this without coordinates is to introduce the so-called **musical isomorphisms** $$\flat: TM \to T^*M$$, defined by $$v^\flat = g(v,\cdot)$$, and its inverse $\sharp: T^*M\to TM$, defined by
$$g(\alpha^\sharp,X)= \alpha(X) \quad \text{for all } X$$
$\sharp$ is the inverse of $\flat$. Indeed, for every vector $X$,
$$g\big((v^\flat)^\sharp, X\big) = v^\flat(X) = g(v, X),$$
where the first equality is the definition of $\sharp$ applied to $\alpha = v^\flat$, and the second is the definition of $\flat$. Hence $$g\big((v^\flat)^\sharp - v, X\big) = 0$$ for all $X$, and since $g$ is non-degenerate, $(v^\flat)^\sharp = v$. Similarly, $(\alpha^\sharp)^\flat(X) = g(\alpha^\sharp, X) = \alpha(X)$ for all $X$, so $(\alpha^\sharp)^\flat = \alpha$.

In components, $$(v^\flat)_a = g_{ab}v^b$$ and $$(\alpha^\sharp)^a = g^{ab}\alpha_b$$, where $$g^{ab}$$ is the inverse matrix of $g_{ab}$, i.e. $g^{ab}g_{bc} = \delta^a_{\ c}$. This recovers the physicist's notation.

Note that the only properties of $g$ used here are that it is **bilinear** and **non-degenerate**; symmetry played no role. The same construction therefore works for the symplectic form $\Omega$, which is bilinear, non-degenerate, but *antisymmetric*. 
We define $$\flat : T\mathcal{Q} \to T^*\mathcal{Q}$$ such that $$v^\flat = \Omega(v,\cdot)$$ and its inverse $\sharp : T^*\mathcal{Q} \to T\mathcal{Q}$, defined by $$\Omega(\alpha^\sharp, X) = \alpha(X) \quad \text{for all } X .$$. As such, $\Omega$ can also be used to "lower" or "raise" the indices, that is to associate to every vector on phase space a one-form and vice-versa: $$v_a= \Omega_{ab}v^b $$ and $$v^a = \Omega^{ab}v_b$$.

While a metric measures lengths of vectors and angles between them, the symplectic product measures **oriented areas in phase space**: for a single degree of freedom, $\Omega(X,Y)$ is the oriented area of the parallelogram spanned by $X$ and $Y$ in the $(q,p)$ plane, and for several degrees of freedom it is the sum of the oriented areas of its projections onto the planes $(q^i,p_i)$. Applied to the basis vectors, the formula for $\Omega(X,Y)$ gives

$$
\begin{align}
&\Omega(\partial_{q^i},\partial_{p_j}) = \delta^i_j\\
&\Omega(\partial_{q^i},\partial_{q^j})= \Omega(\partial_{p_i},\partial_{p_j})= 0\\
&\Omega(\partial_{q^i},\cdot) = \text{d}p_i\\
&\Omega(\partial_{p_i},\cdot) = -\text{d}q^i
\end{align}
$$

From the two last equalities, we see that $\Omega$ "mixes" the $q$ and $p$ components: the one-form associated with a $q$ direction is the differential of the conjugate $p$, and vice versa.

### Hamiltonian vector fields 

If $F$ is a smooth function (observable) defined on $\mathcal{P}$, we can define the Hamiltonian vector field $X_F$ of $F$ as

$$
\begin{equation}
    \boxed{
\text{d} F = \Omega(X_F,\cdot)
    }
\end{equation}
$$

which is sometimes written equivalently using the interior derivative as $\text{d} F = i_{X_F} \Omega$.

Using the musical isomorphisms previously defined, the Hamiltonian vector field of an observable $f$ is then simply the "raised" differential of $f$

$$\boxed{X_F = (\text{d} F)^\sharp}$$

In components, this reads $X_F^{\,a} = \Omega^{ab}\partial_b F := \partial^b F$. Hence, $X_F$ is nothing else than i) taking the differential $\text{d}F$ of the function $F$ to obtain a one-form field, and then ii) use the "inverse symplectic metric" to obtain a vector field out of it. We could say that $X_F$ is the **symplectic gradient** of $F$. What is nice with vector fields, is that they then act back on functions, and thus on observables. Hence $X_F$ is a **classical operator** constructed out of an observable $F$ that can act on any other observable, say $G$, to create a third observable $X_F(G)$.

In canonical coordinates, the vector solving this equation takes the form:

$$
\begin{equation}
    \boxed{
    X_F = \frac{\partial F}{\partial p_i}\partial_{q^i}- \frac{\partial F}{\partial q^i}\partial_{p_i}}
\end{equation}
$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Let $X_F = (A^i \partial_{q^i} + B_i \partial_{p_i})$. We want to find $A^i$ and $B_i$ such that $\text{d} F = i_{X_F} \Omega$. 
Let $Y= (u^i \partial_{q^i} + v_i \partial_{p_i})$ be an arbitrary vector. We have

$$
\begin{align}
i_{X_F} \Omega(Y) &= \Omega(X_F,Y) = \text{d} F(Y)
\end{align}
$$

From the symplectic product formula derived previously, we find that the left hand side gives:

$$
\begin{align}
    \Omega(X_F,Y) = A^iv_i - B_i u^i
\end{align}
$$

The right hand side gives:

$$
\begin{align}
    \text{d} F(Y)& =  \left(\frac{\partial F}{\partial q^i} \text{d} q^i + \frac{\partial F}{\partial p_i} \text{d} p_i\right)(u^i \partial_{q^i} + v_i \partial_{p_i}) \nonumber \\
    &= \frac{\partial F}{\partial q^i} u^i +  \frac{\partial F}{\partial p_i} v_i
\end{align}
$$

Equating the two sides, we find that $A^i = \frac{\partial F}{\partial p_i}$ and $B_i = -\frac{\partial F}{\partial q^i}$ and hence

$$
\begin{equation}
    X_F = \frac{\partial F}{\partial p_i}\partial_{q^i}- \frac{\partial F}{\partial q^i}\partial_{p_i}
\end{equation}
$$

</details>

The coordinates $q_i$ and $p^i$ are maps from $$U \subseteq \mathcal{Q} \to \mathbb{R}$$ and are thus observables (at least on a patch of $\mathcal{Q}$). They can be called **local observables**. As such, from the previous expression it is possible to associate to them the classical operators:

$$X_{q^i} =  - \partial_{p_i} \qquad X_{p_i} = \partial_{q_i}$$

### Poisson Bracket and Lie algebra structures

As discussed before, physical observables are functions on the phase space manifold $\mathcal{P}$, noted $\mathcal{O}= C^{\infty}(\mathcal{P})$.
Let $F,G \in C^{\infty}(\mathcal{P})$ be two observables, we introduce the **Poisson bracket** product on them as

$$
\begin{equation}
\boxed{
\lbrace F,G\rbrace  := \Omega(X_F,X_G)}
\end{equation}
$$

That is, **the poisson bracket of two observables $F$ and $G$ is the symplectic product of their two associated Hamiltonian vector fields $X_F$ and $X_G$**.

Interestingly, it can be rewritten as 

$$\boxed{\lbrace F,G\rbrace  = X_G(F)}$$

hence **the Poisson bracket between $F$ and $G$ is a third observable constructed by making the Hamiltonian vector field of $G$, $X_G$ act on $F$**.

<details markdown="1">
  <summary><strong> Proof </strong></summary>

$$\begin{align}
\lbrace F,G\rbrace &= \Omega(X_F,X_G)\\
&=\Omega(X_F,.)(X_G)\\
&= \text{d}F(X_G)
&= X_G(F)
\end{align}
$$

</details>


The Poisson bracket satisfies many interesting properties. First, it is clearly an anti-symmetric operation, that is:

- $\lbrace F,F\rbrace =0$.
- $\lbrace F,G\rbrace =-\lbrace G,F\rbrace$. 

which follows directly from the anti-symmetry of $\Omega$.

<details markdown="1">
  <summary><strong>Proof </strong></summary>

- $\lbrace F,F\rbrace =0$ directly follows from the
fact that $\Omega$ is a 2-form, and hence an antisymmetric tensor.  From the expression of the symplectic product in coordinates, we see immediately that for a vector $X_F=A^i\partial_{q^i}+ B_i\partial_{p^i}$, $\Omega(X_F,X_F)= A^iB_i - A^iB_i= 0$. If you just want to train, you can verify again that:

    $$
    \begin{align}
    \lbrace F,F\rbrace &= \Omega(X_F,X_F)\\
    &= (\text{d} q^i \wedge \text{d} p_i)(X_F,X_F)\\
    &= (\text{d} q^i \otimes \text{d} p_i - \text{d} p_i \otimes \text{d} q^i)(X_F,X_F)\\
    &= \text{d} q^i(X_F) \text{d} p_i(X_F)- \text{d} p_i(X_F)\text{d} q^i(X_F)\\
    &=0
    \end{align}
    $$

- $\lbrace F,G\rbrace =-\lbrace G,F\rbrace $ also follows immediatly from the fact that $\Omega$ is a two-form and hence antisymmetric $\Omega(X_F,X_G) = -\Omega(X_G,X_F)$. It is apparent from the symplectic formula, but one can check again that

    $$\begin{align}
    \Omega(X_F,X_G) &= \text{d} q^i(X_F) \text{d} p_i(X_G)- \text{d} p_i(X_F)\text{d} q^i(X_G)\\
    \end{align}
    $$

    and 
    
    $$\begin{align}
    \Omega(X_G,X_F) &= \text{d} q^i(X_G) \text{d} p_i(X_F)- \text{d} p_i(X_G)\text{d} q^i(X_F)= -\Omega(X_F,X_G)\\
    \end{align}
    $$
</details>

Furthermore, the existence of the Poisson bracket equips the observable space $\mathcal{O}$ with a **Lie algebra** structure as it satisfies:

- $\lbrace F, G+H\rbrace = \lbrace F, G \rbrace + \lbrace F, H\rbrace$
- $\lbrace \alpha F , \beta G\rbrace = \alpha\beta \lbrace F,G\rbrace$
- $\lbrace F, \lbrace G, H\rbrace \rbrace + \lbrace G, \lbrace H, F\rbrace \rbrace + \lbrace H, \lbrace F, G \rbrace \rbrace = 0$ (known as the **The Jacobi identity**).

<details markdown="1">
  <summary><strong>Proof </strong></summary>

</details>

Furthermore, it satisfies:

- $$X_{\lbrace F,G\rbrace }= -[X_F,X_G]$$. 

This last expression is very interesting as it shows that the map $F\to X_F$ transports the Lie algebra structure of $$(\mathcal{O},\{.,.\})$$ to $$(\mathcal{X},[.,.])$$, where $$\mathcal{X}$$ is the space of all the Hamiltonian vector fields associated to every possible observable. The map $F\to X_F$ is a Lie algebra (anti)-homomorphism. Hence **the classical operators $X_F$ with the vector field bracket $[.,.]$ forms a Lie Algebra**.

The Poisson bracket also obeys **Leibniz rule** for the product of functions, making it a sort of **differential operator**:

- $\lbrace FG, H\rbrace = F\lbrace G,H\rbrace + G \lbrace F,H\rbrace$
- $\lbrace F, FG \rbrace = G \lbrace F,H\rbrace + H\lbrace F,G \rbrace$

In terms of vector field, these relations become more readable as:

- $$v_h(fg) = v_h(f)g + fv_g(g)$$

<details markdown="1">
  <summary><strong>Proof </strong></summary>

</details>

The Poisson bracket can be rewritten in several equivalent ways, highlighting some of these properties. For instance, using the definition of $X_F$ we also have 

$$
\begin{equation}
\lbrace F,G\rbrace  = \text{d} F(X_G) =  X_G(F) = \mathcal{L}_{X_F}G
\end{equation}
$$

The last equality, showing that the Poisson bracket $\lbrace F,G\rbrace$ is equivalent to the Lie derivative of $G$ along $X_F$ shows explicitly why it is, indeed, a derivative.

<details markdown="1">
  <summary><strong> Proof of the different expressions </strong></summary>

First recall again, that a vector $v$ is an object that "eats" a function to give a number $v(f)$ and that the exterior derivative of $\text{d}f$ is a one form, which "eats" a vector to give a number $\text{d}f(v)$ such that:

$$ \text{d}f(v) = v(f) $$

The Lie derivative applied on a function has the exact same expression (they differ when applied on other objects):

$$\mathcal{L}_vf = v(f)$$

So it will be straightforward to prove the last expression involving it.

Now, we recall that, by definition of $X_F$:

$$\text{d}F = \Omega(X_F,.) $$

Hence, it is easy to see that:

$$\text{d}F(X_G) = \Omega(X_F,X_G)$$

which is the definition of $\lbrace F, G \rbrace $ and prooves our first expression.

Furthermore, from the definition of $\text{d}$ above, we immediately get the second expression:

$$\text{d}F(X_G) =X_G(F)$$

We also note that, from the anti-symmetry of $\Omega$ discussed previously, we also have the two other expressions:

$$\lbrace F,G \rbrace = - X_F(G) = - \text{d}G(X_F) $$

</details>

In local coordinates, the Poisson bracket takes the form:

$$
\begin{equation}
\boxed{
\lbrace F,G\rbrace  = \frac{\partial F}{\partial q^i}\frac{\partial G}{\partial p_i} - \frac{\partial F}{\partial p_i}\frac{\partial G}{\partial q^i}
}
\end{equation}
$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

We saw previously that 

$$X_F = \frac{\partial F}{\partial p_i}\partial_{q^i}- \frac{\partial F}{\partial q^i}\partial_{p_i}$$

and similarly 

$$X_G = \frac{\partial G}{\partial p_i}\partial_{q^i}- \frac{\partial G}{\partial q^i}\partial_{p_i}$$

Hence, using again the formula for the symplectic product:

$$
\begin{align}
\lbrace F, G\rbrace &= \Omega(X_F,X_G)\\
&= -\frac{\partial F}{\partial p_i}\frac{\partial G}{\partial q^i} + \frac{\partial F}{\partial q^i}\frac{\partial G}{\partial p_i} \\
&= \frac{\partial F}{\partial q^i}\frac{\partial G}{\partial p_i} - \frac{\partial F}{\partial p_i}\frac{\partial G}{\partial q^i}
\end{align}
$$

</details>

## The other way around: from Poisson algebra to symplectic forms

Let us repeat and summarize what we have so far, from a different angle. This also allows us to understand that the full algebra that we just constructed on observables is a much more general structure that can be studied for itself: a **Poisson algebra**.

#### The observable algebra

Let us try to "forget" for a moment what we said before and restart from scratch.
Our starting point is a manifold $\mathcal{P}$, the **phase space** (which is itself, for most physical applications, the cotangent bundle $$T^\ast\mathcal{Q}$$ of another manifold $\mathcal{Q}$, the configuration space). 

Functions on phase space are the **observables**. They form a space $\mathcal{O}=C^\infty(\mathcal{P})$. 

$\mathcal{O}$ is equipped with two operations: multiplication by real numbers $\lambda \in \mathbb{R}$, $\lambda,F\to \lambda F$, and addition $F,G \to F+G$. With these two operations, $\mathcal{O}$ forms a vector space.

$\mathcal{O}$ is also equipped with a product, the pointwise product between functions $.:\mathcal{O}\times \mathcal{O} \to \mathcal{O}$, $F,G \to F.G$, with $(F.G)(x)=F(x)G(x)$ at every point $x\in\mathcal{P}$. This product is commutative $F.G=G.F$ and associative $F.(G.H)=(F.G).H$. With this third operation, $(\mathcal{O},.)$ becomes a **commutative and associative algebra**.

#### Building a Lie algebra from observables

This is more or less all we can get "for free" by considering the space of all possible real functions on a manifold. We now add an additional structure and equip $\mathcal{O}$ with a fourth product $\lbrace.,.\rbrace$ called the **Poisson bracket**. This is the structure from which all of classical mechanics will follow. We ask for this bracket to be bilinear and to satisfy three properties P1 to P3. First, we ask for this Poisson bracket to be a **Lie bracket**, such that $(\mathcal{O}, \lbrace.,.\rbrace)$ forms a Lie algebra. That is, it should be bilinear with respect to addition and scalar multiplication (see above) and satisfy jointly:

- (P1): **Antisymmetry** $$\lbrace F,G \rbrace = - \lbrace G,F\rbrace$$.
- (P2): **Jacobi identity** $\lbrace F, \lbrace G, H\rbrace \rbrace + \lbrace G, \lbrace H, F\rbrace \rbrace + \lbrace H, \lbrace F, G \rbrace \rbrace = 0$ 

Applying P1 a few times, the Jacobi identity (P2) can be rewritten as $$\lbrace F, \lbrace G, H\rbrace \rbrace = \lbrace G, \lbrace F, H\rbrace \rbrace + \lbrace \lbrace F, G \rbrace,  H \rbrace $$. This is very important, as it shows us that **we can naturally construct a derivation of the Lie bracket**. First, consider an algebra $A$ with an operation $\star$. A **derivation of $\star$** is a linear map $D: A \to A$, that satisfies the **Leibniz rule**: $$D(a\star b) = D(a)\star b + a \star D(b)$$. Now, considering one element $F\in \mathcal{O}$, we introduce the **adjoint map** $\text{ad}_F : \mathcal{O} \to \mathcal{O}$ defined as $\text{ad}_F = \lbrace F,.\rbrace $. The Jacobi identity becomes

$$\text{ad}_F(\lbrace G,H \rbrace) = \lbrace \text{ad}_F(G),H \rbrace + \lbrace G,\text{ad}_F(H)\rbrace.$$

Hence $\text{ad}_F$ is a **derivation of the Lie bracket**. This is true for every element of the Lie algebra (and for every Lie algebra). The adjoint maps define a way for the **algebra to act on itself**.

Furthermore, working out a bit the Jacobi identity again (moving the first term of the right-hand side to the left, and renaming $(F,G,H)\to(G,H,F)$), we can write, for every $F$: $$\lbrace G, \lbrace H, F\rbrace \rbrace - \lbrace H, \lbrace G, F\rbrace \rbrace = \lbrace \lbrace G, H \rbrace,  F \rbrace$$. In terms of the adjoint map, this is: 

$$[\text{ad}_G,\text{ad}_H] = \text{ad}_{\lbrace G,H\rbrace}$$

where, on the left-hand side, $$[A,B]=A\circ B-B\circ A$$ is the **commutator** of two linear maps $$A,B:\mathcal{O}\to\mathcal{O}$$, $\circ$ denoting composition. Be careful: this commutator is *not* a Poisson bracket, since $$\text{ad}_G$$ and $$\text{ad}_H$$ are operators acting on observables, not observables.

The map $\text{ad}$ preserves the Lie bracket: it turns the Poisson bracket of two observables into the commutator of the corresponding operators. A linear map with this property is called a **representation** of the Lie algebra, and $\text{ad}$ is the **adjoint representation**. This representation is extremely important in physics (but we will not discuss it further here). More details are given in the expandable box below for the curious reader.
Given P1, we have thus three equivalent ways of writing the same identity: the cyclic form (P2), the derivation form, and the representation form.

<details markdown="1">
  <summary><strong>More on Jacobi identity and adjoint maps in physics</strong></summary>

The Jacobi identity is powerful. In its cyclic form (P2) it looks like an arbitrary rule, but the derivation form tells us what it really means: **every element of a Lie algebra generates an infinitesimal symmetry of the algebra itself**. This idea appears everywhere in physics.

**Lie group, Lie algebra and exponential.** A **Lie group** $\mathcal{G}$ is a group of transformations which depend continuously on some parameters. Our favorite example as physicists is the rotation group $$SO(3)$$: the $3\times3$ matrices $R$ such that $$R^TR=1$$ (they preserve lengths and angles) and $$\det R=1$$ (they preserve orientation: reflections are excluded). A rotation acts on a vector $v$ as $$v\to Rv$$, and it depends on three parameters: a unit axis $\vec n$ (two parameters) and an angle $\theta$.

The **Lie algebra** $\mathfrak{g}$ associated to $\mathcal{G}$ is made of the infinitesimal transformations. Close to the identity, a rotation by a small angle $\theta$ can be written $$R\approx1+\theta X$$. Inserting this in $$R^TR=1$$ and keeping the terms of order $\theta$ gives $$X^T+X=0$$: the Lie algebra $$\mathfrak{so}(3)$$ is made of the **antisymmetric matrices**. Such a matrix has three independent entries, so it can be labelled by a vector $\vec a$, and it acts on vectors as

$$X_{\vec a}\,v=\vec a\times v$$

$$X_{\vec a}\,v$$ is the small displacement of $v$ under a small rotation around $\vec a$. A basis is given by $$X_x,X_y,X_z$$, the infinitesimal rotations around the three axes; for instance $$X_z=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}$$, with $$X_zv=\hat z\times v=(-v_y,v_x,0)$$.

Conversely, the **exponential** builds finite transformations from infinitesimal ones: $$e^{\theta X}=1+\theta X+\tfrac{\theta^2}{2}X^2+\dots$$. For $X_z$, one finds $$X_z^3=-X_z$$, so that the series reorganizes into the series of $$\cos\theta$$ and $$\sin\theta$$:

$$e^{\theta X_z}=\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}$$

which is the rotation by the angle $\theta$ around $\hat z$. More generally, for a unit vector $\vec n$, $$R_{\vec n}(\theta)=e^{\theta X_{\vec n}}$$ is the rotation by $\theta$ around $\vec n$. The angle $\theta$ is not part of the structure: it measures how much of the transformation $$X_{\vec n}$$ we perform. The curve $$\theta\to e^{\theta X_{\vec n}}$$ starts at the identity ($$R_{\vec n}(0)=1$$); rotating by $\varphi$ and then by $\theta$ around the same axis is rotating by $$\theta+\varphi$$ ($$R_{\vec n}(\theta)R_{\vec n}(\varphi)=R_{\vec n}(\theta+\varphi)$$); and its velocity at $\theta=0$ is the generator ($$\frac{d}{d\theta}R_{\vec n}(\theta)\big\vert_{\theta=0}=X_{\vec n}$$). (In quantum mechanics, the same rotation is written $$e^{-i\theta\,\vec n\cdot\hat{\vec J}/\hbar}$$: with this convention, $$X_{\vec n}$$ corresponds to $$-i\,\vec n\cdot\hat{\vec J}/\hbar$$.)

**The group acts on its own Lie algebra.** The exponential goes from $\mathfrak{g}$ to $\mathcal{G}$. There is a second, different operation: a rotation $R$ transforms an infinitesimal rotation $X$ into another infinitesimal rotation, $$RXR^{-1}$$. Here is the idea. "Undo $R$, rotate by $\theta$ around $\vec n$, then redo $R$" is again a rotation by the angle $\theta$, but around the rotated axis $$R\vec n$$. Indeed, it leaves $$R\vec n$$ fixed: $$Re^{\theta X_{\vec n}}R^{-1}(R\vec n)=Re^{\theta X_{\vec n}}\vec n=R\vec n$$. In formulas, $$Re^{\theta X}R^{-1}=e^{\theta\,RXR^{-1}}$$ (expand the exponential and use $$(RXR^{-1})^k=RX^kR^{-1}$$), with

$$RX_{\vec n}R^{-1}=X_{R\vec n}$$

The rotation $R$ thus sends the Lie algebra element $X$ to

$$\text{Ad}_R(X)=RXR^{-1}$$

(with $$R^{-1}=R^T$$). This is called **conjugation**, or the **adjoint action** of the group on its Lie algebra. Physically, $$\text{Ad}_R(X)$$ is the same infinitesimal rotation, seen from a frame rotated by $R$: the angle is unchanged, and the axis is rotated. Note that $$\text{Ad}_R$$ is a linear map from $$\mathfrak{so}(3)$$ to $$\mathfrak{so}(3)$$: it acts on infinitesimal rotations, not directly on the vectors $v$.

**The bracket comes from the group.** Now take a rotation by a small angle, $$R=e^{\theta X}$$, and look at how another element $Y$ of the Lie algebra changes. To first order, $$e^{\theta X}\approx1+\theta X$$ and $$e^{-\theta X}\approx1-\theta X$$, so that

$$\text{Ad}_{e^{\theta X}}(Y)=e^{\theta X}Ye^{-\theta X}=Y+\theta[X,Y]+O(\theta^2)$$

where $$[X,Y]=XY-YX$$ is the commutator, and $$O(\theta^2)$$ denotes terms of order two and higher in $\theta$. The Lie bracket $$[X,Y]$$ is therefore the rate at which $Y$ changes when the frame is rotated infinitesimally by $X$. This is exactly the adjoint map $$\text{ad}_X(Y)=[X,Y]$$: $$\text{ad}_X$$ is the infinitesimal version of $$\text{Ad}_R$$. For rotations, rotating the axis $\vec a$ by a small angle $\theta$ around $\vec n$ gives $$\vec a+\theta\,\vec n\times\vec a+O(\theta^2)$$, hence

$$[X_{\vec n},X_{\vec a}]=X_{\vec n\times\vec a}$$

The bracket of two infinitesimal rotations is the infinitesimal rotation around the cross product of their axes. For instance, $$[X_x,X_y]=X_z$$: rotating the $y$ axis slightly around $x$ tilts it toward $z$. The bracket also measures the familiar fact that rotations do not commute: to second order in the angles, $$e^{\theta X_x}e^{\varphi X_y}-e^{\varphi X_y}e^{\theta X_x}=\theta\varphi\,[X_x,X_y]+\dots=\theta\varphi\,X_z+\dots$$. Conversely, applying $$\text{ad}_X$$ by a finite amount $\theta$ gives back conjugation, $$e^{\theta\,\text{ad}_X}(Y)=e^{\theta X}Ye^{-\theta X}$$ (here $$e^{\theta\,\text{ad}_X}$$ is the exponential of a linear map acting on $$\mathfrak{so}(3)$$, not a rotation matrix). To summarize, three different maps are involved:

| Map | From | To | Meaning | For rotations |
|---|---|---|---|---|
| $$X\to e^{\theta X}$$ | $$\mathfrak{so}(3)$$ | $$SO(3)$$ | build a finite transformation from an infinitesimal one | $$X_{\vec n}\to$$ rotation by $\theta$ around $\vec n$ |
| $$\text{Ad}_R:Y\to RYR^{-1}$$, for each $$R\in SO(3)$$ | $$\mathfrak{so}(3)$$ | $$\mathfrak{so}(3)$$ | see $Y$ from a frame rotated by $R$ | $$X_{\vec a}\to X_{R\vec a}$$: the axis is rotated |
| $$\text{ad}_X:Y\to[X,Y]$$, for each $$X\in\mathfrak{so}(3)$$ | $$\mathfrak{so}(3)$$ | $$\mathfrak{so}(3)$$ | infinitesimal version of $$\text{Ad}$$: $$\text{Ad}_{e^{\theta X}}=e^{\theta\,\text{ad}_X}$$ | $$X_{\vec a}\to X_{\vec n\times\vec a}$$ |

**Automorphisms and derivations.** An **automorphism** of a Lie algebra is an invertible linear map $\Phi$ from the Lie algebra to itself which preserves the bracket: $$\Phi([Y,Z])=[\Phi(Y),\Phi(Z)]$$. Each $$\text{Ad}_R$$ is an automorphism. Indeed, inserting $$R^{-1}R=1$$ in the middle of each product:

$$R[Y,Z]R^{-1}=RYR^{-1}\,RZR^{-1}-RZR^{-1}\,RYR^{-1}=[RYR^{-1},RZR^{-1}]$$

In words: changing the frame does not change the relations between infinitesimal rotations. In terms of axes, using $$[X_{\vec a},X_{\vec b}]=X_{\vec a\times\vec b}$$ and $$\text{Ad}_R(X_{\vec a})=X_{R\vec a}$$, this is the familiar statement $$R(\vec a\times\vec b)=(R\vec a)\times(R\vec b)$$: rotating the cross product of two vectors is the same as taking the cross product of the rotated vectors.

Consider now a family of automorphisms $$\Phi_\theta$$, which depends smoothly on $\theta$ and starts from the identity map $\text{id}$ of $\mathfrak{g}$, $$\Phi_0=\text{id}$$. For small $\theta$, we can write $$\Phi_\theta=\text{id}+\theta D+O(\theta^2)$$, where the linear map $$D=\frac{d\Phi_\theta}{d\theta}\big\vert_{\theta=0}$$ is called the **generator** of the family. Inserting this expansion in the automorphism condition, and using the bilinearity of the bracket, we get

$$[Y,Z]+\theta\,D([Y,Z])+O(\theta^2)=[Y,Z]+\theta\left([D(Y),Z]+[Y,D(Z)]\right)+O(\theta^2)$$

Comparing the terms proportional to $\theta$ gives $$D([Y,Z])=[D(Y),Z]+[Y,D(Z)]$$: the generator of a family of automorphisms is always a **derivation**. Derivations are infinitesimal automorphisms.

Let us apply this to the family $$\Phi_\theta=\text{Ad}_{e^{\theta X}}$$. It starts from the identity map, since $$\text{Ad}_1(Y)=Y$$, and its generator is $$\text{ad}_X$$. We obtain

$$[X,[Y,Z]]=[[X,Y],Z]+[Y,[X,Z]]$$

which is the Jacobi identity, in its derivation form. For rotations, with $$X=X_{\vec n}$$, $$Y=X_{\vec a}$$ and $$Z=X_{\vec b}$$, it reads $$\vec n\times(\vec a\times\vec b)=(\vec n\times\vec a)\times\vec b+\vec a\times(\vec n\times\vec b)$$: the infinitesimal version of $$R(\vec a\times\vec b)=(R\vec a)\times(R\vec b)$$. **The Jacobi identity is the infinitesimal version of the fact that changing the frame by a group element preserves the bracket.** This is why every Lie algebra coming from a group satisfies it.

**Observables.** As discussed in the main text, classical observables, with the Poisson bracket, also form a Lie algebra. Each observable $F$ generates a transformation of phase space: solve Hamilton's equations with $F$ in place of the Hamiltonian, so that every observable changes as $$\frac{dG}{d\theta}=\lbrace G,F\rbrace=-\text{ad}_F(G)$$, and follow this motion for an amount $\theta$. For rotations, take $$F=\vec n\cdot\vec L$$, with $$\vec L=\vec q\times\vec p$$ the angular momentum. Then $$\lbrace\vec q,\vec n\cdot\vec L\rbrace=\vec n\times\vec q$$ and $$\lbrace\vec p,\vec n\cdot\vec L\rbrace=\vec n\times\vec p$$: this is exactly $$X_{\vec n}$$ acting on $\vec q$ and $\vec p$. Following this motion for an amount $\theta$ therefore rotates positions and momenta by the angle $\theta$ around $\vec n$: it is the classical counterpart of $$e^{\theta X_{\vec n}}$$ (and of $$e^{-i\theta\,\vec n\cdot\hat{\vec J}/\hbar}$$ in quantum mechanics). The angular momenta also have the same brackets as the infinitesimal rotations, $$\lbrace L_x,L_y\rbrace=L_z$$ like $$[X_x,X_y]=X_z$$: they are the **charges** of rotations. For $$F=H$$, the same construction gives time evolution, with $\theta$ replaced by the time $t$.

The Jacobi identity says that $$\text{ad}_F$$ is a derivation for every $F$, and so is its opposite: $$\lbrace\lbrace G,K\rbrace,F\rbrace=\lbrace\lbrace G,F\rbrace,K\rbrace+\lbrace G,\lbrace K,F\rbrace\rbrace$$. The transformation generated by $F$ therefore differentiates Poisson brackets with the product rule, and its finite version preserves them. For instance, for observables without explicit time dependence, $$\frac{d}{dt}\lbrace G,K\rbrace=\lbrace\dot G,K\rbrace+\lbrace G,\dot K\rbrace$$. One difference with matrices: classically, this preservation is not automatic (there is no "insert $$R^{-1}R=1$$"), and the Jacobi identity is precisely the condition that guarantees it.

**Center and Casimir**

Some elements generate no transformation at all. The **center** of a Lie algebra is the set of elements $c$ that commute with every element, $$[c,x]=0$$ for all $x$. Equivalently, $$\text{ad}_c=0$$: the center is the **kernel** of the adjoint map, i.e. the set of elements it sends to zero. When all the brackets of a Lie algebra vanish, the algebra is called **abelian**; every element is then in the center, and $\text{ad}=0$.

In the observable algebra, the elements of the center are called **Casimir functions**: $C$ is a Casimir if $$\lbrace C,F\rbrace=0$$ for every observable $F$. A Casimir is conserved whatever the Hamiltonian, since $$\dot C=\lbrace C,H\rbrace=0$$ for every $H$: its conservation does not come from a symmetry of a particular system, but from the structure of phase space itself. Conversely, adding a Casimir to the Hamiltonian, $$H\to H+C$$, does not change the equations of motion $$\dot G=\lbrace G,H\rbrace$$. The simplest Casimirs are the constants, which is why energy is only defined up to an additive constant. For the canonical bracket on a connected phase space, they are in fact the only ones, since $$\lbrace q^i,C\rbrace=\partial C/\partial p_i$$ and $$\lbrace C,p_i\rbrace=\partial C/\partial q^i$$ must all vanish.

Non-trivial Casimirs appear for other Poisson brackets. On the space of angular momenta $$(L_1,L_2,L_3)$$, with the bracket $$\lbrace L_i,L_j\rbrace=\varepsilon_{ijk}L_k$$ (which describes the rotation of a rigid body; $$\varepsilon_{ijk}$$ is the Levi-Civita symbol defined in the next paragraph), the function $$C=L_1^2+L_2^2+L_3^2$$ is a Casimir. Using the Leibniz rule (P3, introduced below), $$\lbrace C,L_1\rbrace=2L_2\lbrace L_2,L_1\rbrace+2L_3\lbrace L_3,L_1\rbrace=-2L_2L_3+2L_3L_2=0$$, and similarly for $L_2$ and $L_3$. The length of the angular momentum is thus conserved for any rigid-body Hamiltonian. (On the full phase space of a particle, $$L^2$$ is not a Casimir, since it does not commute with $\vec q$ or $\vec p$: it only commutes with the $$L_i$$.) In quantum mechanics, the operator $$\hat L^2$$ commutes with all the $$\hat L_i$$, and its eigenvalue $$\ell(\ell+1)\hbar^2$$ labels the representations of the rotation algebra: it is the prototype of a **Casimir operator**. We will meet the center again below, with constant terms in the algebra of charges and with the charge of the photon.

**Charges**

Consider now a Lie group of symmetries $\mathcal{G}$, whose Lie algebra $\mathfrak{g}$ has a basis $$T_a$$ and **structure constants** $$f_{ab}{}^{c}$$, defined by $$[T_a,T_b]=f_{ab}{}^{c}T_c$$ (Einstein convention: repeated indices are summed). In classical mechanics, each symmetry is generated by a conserved **charge** $$Q_a\in\mathcal{O}$$ (momentum $$P_i$$ for translations, angular momentum $$L_i$$ for rotations): the infinitesimal transformation of an observable is $$\delta_a F=\text{ad}_{Q_a}(F)=\lbrace Q_a,F\rbrace$$. For instance, $$\lbrace P_i,F\rbrace=-\partial F/\partial q^i$$: momentum generates (infinitesimal) translations. The link between symmetry and conservation is then immediate: $$\delta_a H=\lbrace Q_a,H\rbrace=\dot Q_a$$, so the Hamiltonian is invariant under the transformation generated by $$Q_a$$ if and only if $$Q_a$$ is conserved. This is Noether's theorem in Hamiltonian form. The representation form of the Jacobi identity gives

$$[\text{ad}_{Q_a},\text{ad}_{Q_b}] = \text{ad}_{\lbrace Q_a,Q_b\rbrace}$$

In words: the commutator of two symmetry transformations (applying the transformation generated by $$Q_b$$ then the one generated by $$Q_a$$, minus the opposite order) is the transformation generated by the Poisson bracket of the two charges. If the charges close, $$\lbrace Q_a,Q_b\rbrace=f_{ab}{}^{c}Q_c$$, the transformations they generate reproduce the Lie algebra $\mathfrak{g}$: the charges provide a realization of the abstract symmetry algebra on phase space. Angular momentum is the standard example: $$\lbrace L_i,L_j\rbrace=\varepsilon_{ijk}L_k$$, where $$\varepsilon_{ijk}$$ is the Levi-Civita symbol ($+1$ if $(i,j,k)$ is a cyclic permutation of $(1,2,3)$, $-1$ for an anticyclic one, $0$ if two indices are equal). One can check it directly from $$\vec L=\vec q\times\vec p$$, e.g. $$\lbrace L_x,L_y\rbrace=L_z$$. This is the Lie algebra of rotations: rotating by a small angle around $x$ then around $y$, minus the opposite order, gives a small rotation around $z$.

Note that $$\text{ad}_c=0$$ for a constant function $c$, since all the derivatives of a constant vanish: constants are in the center. Consequently $$\text{ad}_{Q+c}=\text{ad}_Q$$: two charges differing by a constant generate exactly the same transformation. The charges may therefore close only up to constants, without spoiling the closure of the transformations.

This happens for the Galilean group. Consider first a single particle of mass $m$ on a line, with $$\lbrace q,p\rbrace=1$$. Translations are generated by $p$, which shifts the position and leaves the momentum unchanged. A **Galilean boost** describes the same system seen from a reference frame moving at constant velocity $u$ with respect to the original one: $$q\to q+ut$$ and $$p\to p+mu$$. It is generated by $$K=mq-tp$$: indeed $$\lbrace K,q\rbrace=t$$ and $$\lbrace K,p\rbrace=m$$. The bracket $$\lbrace K,p\rbrace=m$$ measures how much a boost changes the momentum (mass times velocity, hence the mass): it is a nonzero constant, so the charges do not Poisson-commute. Yet, as transformations, boosts and translations commute: translating by $a$ and then boosting by $u$ gives $$q\to q+a+ut$$, $$p\to p+mu$$, exactly as boosting first and translating afterwards. The adjoint representation translates this as $$[\text{ad}_K,\text{ad}_p]=\text{ad}_{\lbrace K,p\rbrace}=\text{ad}_m=0$$. 
Thus, at the level of charges, $$\lbrace K,p\rbrace=m\neq0$$, while at the level of transformations $$[\text{ad}_K,\text{ad}_p]=0$$. The two levels can disagree because the map $$Q\to\text{ad}_Q$$, which sends a charge to the transformation it generates, forgets constants: $$\text{ad}_{Q+c}=\text{ad}_Q$$. The charges $K$ and $K+c$ are different observables (they take different values), but they generate exactly the same boost.
The algebra of charges therefore contains one more element than the algebra of transformations: the constant $m$, which Poisson-commutes with every observable. In the algebra of transformations (the Lie algebra of the Galilean group), boosts and translations commute; in the algebra of charges, their bracket gives the mass. A Lie algebra obtained by adding to another one some central elements (elements that commute with everything), and which gives back the original one once these central elements are set to zero, is called a **central extension**. The algebra of charges is a central extension of the Lie algebra of the Galilean group, and the mass is its **central charge**. This extension cannot be removed by redefining the charges: replacing $K$ by $K+c$ and $p$ by $p+c'$, with $c$ and $c'$ constants, does not change their bracket, $$\lbrace K+c,p+c'\rbrace=\lbrace K,p\rbrace=m$$. The mass is thus not an accident of our choice of charges, but a genuine feature of how Galilean symmetry acts on phase space. In fact, at $t=0$ we have $K=mq$, and $$\lbrace K,p\rbrace=m$$ is nothing but $m$ times $$\lbrace q,p\rbrace=1$$: the charges $p$, $K$ and the constants form the same algebra as $q$, $p$ and the constants, called the **Heisenberg algebra**, whose quantum version is $$[\hat q,\hat p]=i\hbar$$.

In a **gauge theory** (electromagnetism with $\mathcal{G}=U(1)$, chromodynamics with $\mathcal{G}=SU(3)$), the symmetry parameter becomes a function of space, $$\varepsilon(\vec x)=\varepsilon^a(\vec x)T_a\in\mathfrak{g}$$: one can perform a different transformation at each point. Electromagnetism is the simplest case. Its Lie algebra is one-dimensional, so $$\varepsilon(\vec x)$$ is just a real function, and the gauge transformation multiplies a matter field $\psi$ of electric charge $q$ by a phase that depends on the point, $$\psi(\vec x)\to e^{iq\varepsilon(\vec x)}\psi(\vec x)$$. Because this phase depends on $\vec x$, the derivatives of $\psi$ pick up a term proportional to $$\vec\nabla\varepsilon$$, and the vector potential $\vec A$ must transform too, in order to compensate it.

In the Hamiltonian formulation, the fields play the role of positions and momenta. At each point $\vec x$, the vector potential $$A_i(\vec x)$$ plays the role of a position, and the electric field $$E_i(\vec x)$$ plays (up to a sign) the role of its conjugate momentum: $$\lbrace A_i(\vec x),E_j(\vec y)\rbrace=-\delta_{ij}\,\delta^3(\vec x-\vec y)$$, where $$\delta^3$$ is the Dirac delta, the continuous version of the Kronecker delta (sums over degrees of freedom become integrals over space). What is then the **charge** that generates gauge transformations? It is built from Gauss's law. At each point, we have one quantity $$C(\vec x)=\vec\nabla\cdot\vec E(\vec x)-\rho(\vec x)$$, with $\rho$ the charge density of matter (for a non-abelian group, there is one such quantity $$C_a(\vec x)$$ for each direction $a$ of the Lie algebra). A generator must be a single function on phase space, so we combine all these quantities, weighted by the parameter: $$C[\varepsilon]=\int d^3x\,\varepsilon^a(\vec x)\,C_a(\vec x)$$. For electromagnetism, integrating by parts (with $\varepsilon$ vanishing far away), $$C[\varepsilon]=-\int d^3x\,\vec\nabla\varepsilon\cdot\vec E-\int d^3x\,\varepsilon\rho$$, and the bracket above gives $$\lbrace C[\varepsilon],\vec A\rbrace=-\vec\nabla\varepsilon$$. So $$C[\varepsilon]$$ generates the familiar transformation of the potential, $$\vec A\to\vec A-\vec\nabla\varepsilon$$, while its matter part $$-\int\varepsilon\rho$$ generates the phase rotation of charged matter (up to a sign that depends on conventions). Two facts show that this transformation is not a physical change. First, it leaves all measurable quantities unchanged: $$\vec E$$ is untouched (the $$E_i$$ Poisson-commute with each other and with matter), $$\vec B=\vec\nabla\times\vec A$$ changes by $$-\vec\nabla\times\vec\nabla\varepsilon=0$$, and $$\vert\psi\vert^2$$ is insensitive to a phase. Second, its charge vanishes: Gauss's law $$\vec\nabla\cdot\vec E=\rho$$ is one of Maxwell's equations, so $$C[\varepsilon]=0$$ for every physical configuration. Unlike the momentum $p$ or the boost charge $K$ of the Galilean example, which can take any value, the charge of a gauge transformation is a **constraint**: an observable which is identically zero on physical states. Two configurations related by a gauge transformation are two descriptions of the same physical state: gauge symmetry is a redundancy of the description.

The brackets of the constraints reproduce the gauge algebra, $$\lbrace C[\varepsilon_1],C[\varepsilon_2]\rbrace=C[[\varepsilon_1,\varepsilon_2]]$$ (up to a sign that depends on conventions). For electromagnetism, $$[\varepsilon_1,\varepsilon_2]=0$$ and all these brackets vanish: two gauge transformations commute, and give $$\vec A\to\vec A-\vec\nabla\varepsilon_1-\vec\nabla\varepsilon_2$$ in either order. For a non-abelian group, $$[\varepsilon_1,\varepsilon_2]\neq0$$, and by the identity above, the commutator of two gauge transformations is again a gauge transformation, of parameter $$[\varepsilon_1,\varepsilon_2]$$. This closure is what makes the redundancy consistent. A gauge transformation must map a physical configuration (where all the constraints vanish) to another physical configuration. Under the transformation generated by $$C[\varepsilon_2]$$, a constraint $$C[\varepsilon_1]$$ changes by $$\lbrace C[\varepsilon_2],C[\varepsilon_1]\rbrace$$, which is again a constraint, hence zero on physical configurations: the constraints stay satisfied. If the bracket of two constraints produced anything that does not vanish on physical configurations, gauge transformations would take us out of the physical states, and the theory would be inconsistent.

The fact that $U(1)$ is abelian means that the charge of the photon has to be zero. Indeed, a field is charged when the gauge transformation rotates it: the variation of a matter field, $$\delta\psi=iq\varepsilon\psi$$, is proportional to the field itself, and the coefficient $q$, which measures how fast its phase turns, is its charge. For a field $\phi$ valued in the Lie algebra, this rotation is $$\delta\phi=[\varepsilon,\phi]=\text{ad}_\varepsilon(\phi)$$, the infinitesimal conjugation discussed above. The gauge field $$A_\mu$$ transforms as $$\delta_\varepsilon A_\mu=-\partial_\mu\varepsilon+[\varepsilon,A_\mu]$$ (with the conventions of the next paragraph; for $U(1)$, its spatial part reduces, up to conventions, to the transformation $$\vec A\to\vec A-\vec\nabla\varepsilon$$ found above). The first term is a pure shift, independent of $$A_\mu$$: it is the gauge redundancy itself. The second term is $$\text{ad}_\varepsilon(A_\mu)$$: a rotation of the gauge field by its own symmetry. For the abelian $U(1)$, the whole algebra is its own center, $\text{ad}=0$, and the second term is absent: the photon is shifted but never rotated, so it is not charged under its own symmetry. Consequently, only matter appears as a source in Gauss's law, Maxwell's equations in vacuum are linear (two solutions can be superposed: two light beams cross without affecting each other), and photons do not interact directly with each other (at the quantum level, a tiny indirect interaction remains, through virtual charged particles). For the non-abelian $SU(3)$, $\text{ad}\neq0$: the gluons themselves carry colour charge. This appears in two places. First, Gauss's law becomes $$\sum_i\left(\partial_iE_i+[A_i,E_i]\right)=\rho$$ (up to conventions): this is the non-abelian version of $$\vec\nabla\cdot\vec E=\rho$$, and the extra term means that the gluon field itself contributes to the colour charge density. Second, the term $$[A_\mu,A_\nu]$$ in the field strength below makes the equations non-linear: gluons interact with each other.

**Bianchi identity**

The same identity appears one level up, in the geometry of gauge fields. Let $$x^\mu$$ ($$\mu=0,1,2,3$$) be spacetime coordinates, $$\partial_\mu=\partial/\partial x^\mu$$, and $$A_\mu(x)$$ the gauge field, valued in $\mathfrak{g}$. The **covariant derivative** of a matter field $\psi$ is $$D_\mu\psi=\partial_\mu\psi+A_\mu\psi$$: it is the derivative adapted to local symmetries, which transforms as $$D_\mu\psi\to gD_\mu\psi$$ when $$\psi\to g\psi$$, even if $g$ depends on $x$ (the ordinary derivative $$\partial_\mu\psi$$ does not, because $g$ gets differentiated too). The **field strength** is the commutator $$F_{\mu\nu}=[D_\mu,D_\nu]=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$$; for electromagnetism, it contains the electric and magnetic fields $\vec E$ and $\vec B$. (Here the coupling constant is absorbed in $$A_\mu$$; physics textbooks often write $$D_\mu=\partial_\mu-igA_\mu^a t_a$$ with Hermitian generators $$t_a$$.)

Operators acting on fields form a Lie algebra under the commutator, and for them the Jacobi identity holds automatically, because composition of operators is associative (expanding the three nested commutators gives twelve products of three operators, which cancel in pairs). Its derivation form, with $$\text{ad}_{D_\mu}=[D_\mu,.]$$, reads

$$[D_\mu,[D_\nu,D_\rho]]=[[D_\mu,D_\nu],D_\rho]+[D_\nu,[D_\mu,D_\rho]]$$

For any $\mathfrak{g}$-valued field $X$ acting by multiplication, commuting with $$D_\mu$$ gives its covariant derivative. Indeed, $$D_\mu(X\psi)=(\partial_\mu X)\psi+X\partial_\mu\psi+A_\mu X\psi$$ and $$XD_\mu\psi=X\partial_\mu\psi+XA_\mu\psi$$, so that, subtracting, $$[D_\mu,X]\psi=(\partial_\mu X+[A_\mu,X])\psi\equiv(D_\mu X)\psi$$: commuting with $$D_\mu$$ is the covariant derivative in the adjoint representation (yet another derivation). Using $$[D_\nu,D_\rho]=F_{\nu\rho}$$ and $$F_{\mu\rho}=-F_{\rho\mu}$$, the left-hand side becomes $$D_\mu F_{\nu\rho}$$, the first term on the right $$[F_{\mu\nu},D_\rho]=-D_\rho F_{\mu\nu}$$, and the second term on the right $$[D_\nu,F_{\mu\rho}]=-D_\nu F_{\rho\mu}$$. Moving everything to the left, we obtain the **Bianchi identity**

$$D_\mu F_{\nu\rho}+D_\nu F_{\rho\mu}+D_\rho F_{\mu\nu}=0$$

In electromagnetism, $$[A_\mu,A_\nu]=0$$ and it reduces to $$\partial_\mu F_{\nu\rho}+\partial_\nu F_{\rho\mu}+\partial_\rho F_{\mu\nu}=0$$, which contains $$\vec\nabla\cdot\vec B=0$$ (taking the three indices spatial) and $$\vec\nabla\times\vec E+\partial_t\vec B=0$$ (taking one index equal to time). Half of Maxwell's equations, and their non-abelian generalization, are therefore not dynamical laws but consequences of the Jacobi identity.

</details>

#### Building a Poisson algebra from observables

Now, this Lie algebra structure on observables is not yet enough to build classical mechanics. We have to ask for another very important property on **how $\lbrace.,.\rbrace$ and $.$ act together**.

- (P3): $\lbrace.,.\rbrace$ must act as a derivation with respect to $.$: $$\lbrace F, G.H \rbrace = \lbrace F,G\rbrace .H + G.\lbrace F,H\rbrace$$

In other words, $$\text{ad}_F$$ must be a derivation of **both** products: of the Lie bracket (this was P2) and of the product of functions (this is P3). Thanks to P1, the same rule holds in the first slot: $$\lbrace G.H, F \rbrace = \lbrace G,F\rbrace .H + G.\lbrace H,F\rbrace$$.

If $\lbrace .,.\rbrace$ satisfies P1 and P2 it is a Lie bracket, with the addition of P3 it becomes called a **Poisson bracket**. 

Derivative operators on functions are vector fields. More precisely, every derivation $D$ of the algebra $(\mathcal{O},.)$ is of the form $$D(F)=X^i\partial_i F$$ for a unique vector field $$X=X^i\partial_i$$ on $\mathcal{P}$, where $$x^i$$ are local coordinates on $\mathcal{P}$, $$\partial_i=\partial/\partial x^i$$, and the components are simply $$X^i=D(x^i)$$. So we can define the **Hamiltonian vector field** of $F$, $X_F= \lbrace .,F\rbrace = - \text{ad}_F$ (the minus here being simply a physicist friendly sign convention: time evolution then reads $$\dot G=\lbrace G,H\rbrace=X_H(G)$$, the system flows along $$X_H$$).

Since $$X_F=-\text{ad}_F$$, the two minus signs cancel in the representation form of the Jacobi identity:

$$[X_F,X_G]=[\text{ad}_F,\text{ad}_G]=\text{ad}_{\lbrace F,G\rbrace}=-X_{\lbrace F,G\rbrace}$$

The commutator of two Hamiltonian vector fields is again a Hamiltonian vector field, the one of $$\lbrace G,F\rbrace$$. With our sign convention, $$F\to X_F$$ reverses the order of the bracket: it is a Lie algebra **anti-homomorphism** (books using the opposite convention get a homomorphism). The functions with $$X_F=0$$, i.e. those that Poisson-commute with every observable, are called **Casimir functions**. On a connected cotangent bundle $$T^\ast\mathcal{Q}$$ with its usual bracket, they are just the constants.

The whole structure $(\mathcal{O}, ., \lbrace.,.\rbrace)$ with the three properties above is called a **Poisson algebra**, and a manifold whose functions carry such a bracket is a **Poisson manifold**.

#### Poisson bivector and Symplectic form 

The Poisson bracket $\lbrace .,.\rbrace$ is a **biderivation**: by P3 and P1, it is a derivation in each slot. This has a strong consequence: the bracket of any two observables is entirely fixed by the brackets of the coordinates. Let us see it in two steps, in local coordinates $$x^i$$ on $\mathcal{P}$:

1. For fixed $G$, the map $$F\to\lbrace F,G\rbrace=X_G(F)$$ is a vector field, so it only involves first derivatives of $F$: $$\lbrace F,G\rbrace = \partial_i F\,\lbrace x^i,G\rbrace$$.
2. By the same argument in the second slot, $$G\to\lbrace x^i,G\rbrace$$ is a vector field: $$\lbrace x^i,G\rbrace = \partial_j G\,\lbrace x^i,x^j\rbrace$$.

Putting both together:

$$\lbrace F,G\rbrace=\pi^{ij}\,\partial_i F\,\partial_j G,\qquad \pi^{ij}=\lbrace x^i,x^j\rbrace$$

The functions $$\pi^{ij}$$ are the components of a tensor field $$\pi=\tfrac{1}{2}\pi^{ij}\,\partial_i\wedge\partial_j$$, antisymmetric by P1: a 2-vector (or **bivector**) $\pi$ must exist, called the **Poisson bivector**. Intrinsically, $$\lbrace F,G\rbrace=\pi(dF,dG)$$: the bivector eats the differentials of the two observables. Conversely, any antisymmetric bivector field defines, through this formula, a bracket satisfying P1 and P3.

P2 is not automatic. One can check that the Jacobiator $$J(F,G,H)=\lbrace F, \lbrace G, H\rbrace \rbrace + \lbrace G, \lbrace H, F\rbrace \rbrace + \lbrace H, \lbrace F, G \rbrace \rbrace$$ is itself a derivation in each slot, so it vanishes as soon as it vanishes on coordinates. Using $$\lbrace x^i,f\rbrace=\pi^{il}\partial_l f$$, the Jacobi identity becomes a condition on $\pi$:

$$\pi^{il}\partial_l\pi^{jk}+\pi^{jl}\partial_l\pi^{ki}+\pi^{kl}\partial_l\pi^{ij}=0$$

Intrinsically, this condition is written $$[\pi,\pi]=0$$, with $$[.,.]$$ the Schouten–Nijenhuis bracket of multivector fields. Two examples:

- **Canonical bracket.** With coordinates $$x=(q^1,\dots,q^n,p_1,\dots,p_n)$$ and $$\pi=\sum_i\partial_{q^i}\wedge\partial_{p_i}$$, i.e. $$\lbrace q^i,p_j\rbrace=\delta^i_j$$ and all other brackets of coordinates vanishing, we recover the usual bracket $$\lbrace F,G\rbrace=\sum_i\left(\partial_{q^i}F\,\partial_{p_i}G-\partial_{p_i}F\,\partial_{q^i}G\right)$$. The components $$\pi^{ij}$$ are constant, so the Jacobi condition holds trivially: this is the quickest proof of the Jacobi identity for the canonical bracket.
- **Lie–Poisson bracket.** On $\mathbb{R}^3$ with coordinates $$(L_1,L_2,L_3)$$, take $$\pi^{ij}=\lbrace L_i,L_j\rbrace=\varepsilon_{ijk}L_k$$. The components are linear in the coordinates, and the Jacobi condition on $\pi$ is exactly the Jacobi identity of the cross product. More generally, for any Lie algebra with structure constants $$c_{ij}{}^{k}$$, the linear bracket $$\lbrace x_i,x_j\rbrace=c_{ij}{}^{k}x_k$$ is a Poisson bracket, and its Jacobi identity is equivalent to the one of the Lie algebra.

Suppose now that the matrix $$\pi^{ij}$$ is invertible at every point: the Poisson structure is **non-degenerate**. Its inverse defines a 2-form $$\omega=\tfrac12\omega_{ij}\,dx^i\wedge dx^j$$, with $$\omega_{ij}\pi^{jk}=-\delta_i^k$$ (the sign is a convention, chosen so that the canonical bracket gives $$\omega=\sum_i dq^i\wedge dp_i$$). Its symplectic inverse is $\omega$, and:

- The Hamiltonian vector field is characterized by $$\iota_{X_F}\omega=dF$$, where $$\iota_X\omega=\omega(X,.)$$ inserts $X$ in the first slot, and $$\lbrace F,G\rbrace=\omega(X_F,X_G)$$. In the canonical case, $$\iota_{X_H}\omega=dH$$ is exactly Hamilton's equations $$\dot q^i=\partial_{p_i}H$$, $$\dot p_i=-\partial_{q^i}H$$.
- The Jacobi identity (P2) is equivalent to $$d\omega=0$$. A closed non-degenerate 2-form is called a **symplectic form**, and $$(\mathcal{P},\omega)$$ a **symplectic manifold**.
- **Darboux's theorem**: around every point there exist coordinates in which $$\omega=\sum_i dq^i\wedge dp_i$$. Locally, all symplectic manifolds look like the canonical phase space.

But a Poisson bivector need not be invertible, so a Poisson manifold is more general than a symplectic one. The Lie–Poisson bracket on $\mathbb{R}^3$ is the simplest example: $$\pi^{ij}$$ is a $3\times3$ antisymmetric matrix, and every antisymmetric matrix of odd size has zero determinant. The function $$C=L_1^2+L_2^2+L_3^2$$ is a Casimir function, $$\lbrace C,F\rbrace=0$$ for every $F$, so every motion stays on a sphere $$C=\text{const}$$. On each sphere of nonzero radius, the restricted bracket is non-degenerate and defines a symplectic form (proportional to the area form). This is a general fact: every Poisson manifold is foliated by **symplectic leaves**, on which the Poisson structure is symplectic, and a connected symplectic manifold is simply a Poisson manifold with a single leaf.

## Symmetries and conservation

Let's now see why the Lie algebra formed by the observables and the classical operators is so relevant for physics. The key idea is that every observable $G$ plays a double role: it is a quantity that can be measured in a classical state $x$, giving a number $G(x)$, and it **generates a transformation** of phase space through its Hamiltonian vector field $X_G$. To make this precise, we first need to recall how a vector field defines a transformation.


### Reminder: integral curves and flows

**Notation.** Parentheses always mean that the map on the left is applied to the object inside: $f(y)$ is the number given by the function $f$ at the point $y$, $\gamma(\lambda)$ is the point given by the curve $\gamma$ at the parameter $\lambda$, and $v(f)$ is the number given by the vector $v$ acting on the function $f$. Since vectors act on functions, the value of a vector-valued object at a point is never written with parentheses, but with a bar: $X\vert_y$ is the vector given by the vector field $X$ at the point $y$. The bar is also used for a derivative evaluated at a value of the parameter. Square brackets are only used for grouping.

**Velocity of a curve.** Let $M$ be a manifold and $\gamma : I\to M$ a smooth curve, where $I\subseteq\mathbb{R}$ is an open interval. For any smooth function $f:M\to\mathbb{R}$, the composition $f\circ\gamma : I\to\mathbb{R}$ is an ordinary real function of the real variable $\lambda$: it is the value of $f$ seen by the moving point. We can thus differentiate it. The **velocity** of the curve at the parameter $\lambda$ is the tangent vector $\gamma'\vert_\lambda\in T_{\gamma(\lambda)}M$ defined by its action on functions:

$$\gamma'\vert_\lambda(f) := \frac{\text{d}}{\text{d}\lambda}(f \circ \gamma)\Big\vert_\lambda$$

For a fixed $\lambda$, $\gamma'\vert_\lambda$ is a single vector, attached to the point $\gamma(\lambda)$. Letting $\lambda$ vary, $\gamma'$ is a vector field **along the curve**: it is defined only at the points of the curve, not on the whole of $M$.

In local coordinates $x^a$, the real functions $$x^a\circ\gamma$$ are the coordinates of the moving point. The chain rule gives, for every $f$,

$$\frac{\text{d}}{\text{d}\lambda}(f \circ \gamma) = \frac{\text{d}}{\text{d}\lambda}(x^a \circ \gamma)\,\cdot\,[\partial_a f]\circ\gamma$$

hence

$$\gamma'\vert_\lambda = \frac{\text{d}}{\text{d}\lambda}(x^a \circ \gamma)\Big\vert_\lambda\;\partial_a\big\vert_{\gamma(\lambda)}$$

The components of the velocity are the derivatives of the coordinates of the moving point. Physicists write them $\frac{\text{d}x^a}{\text{d}\lambda}$, leaving the composition with $\gamma$ implicit.

**Integral curves.** Let now $X$ be a vector field on $M$: at each point $y\in M$, it gives a tangent vector $X\vert_y\in T_yM$. An **integral curve** of $X$ is a curve whose velocity is, at every instant, the value of the vector field at the point where the curve is:

$$
\begin{equation}
\gamma'\vert_\lambda = X\vert_{\gamma(\lambda)}\qquad\forall\lambda\in I
\end{equation}
$$

In coordinates, writing $X = X^a\partial_a$ with component functions $X^a : M\to\mathbb{R}$, this is a system of ordinary differential equations, each one being an equality between real functions on $I$:

$$\frac{\text{d}}{\text{d}\lambda}(x^a \circ \gamma) = X^a\circ\gamma$$

By the Cauchy–Lipschitz theorem, for each point $y\in M$ there is a unique maximal integral curve starting at $y$. We note it $\gamma_y$, so that $\gamma_y(0) = y$. A vector field thus has infinitely many integral curves, one through each point, and two integral curves that meet coincide up to a shift of $\lambda$.

**Flow.** The **flow** of $X$ collects all the integral curves:

$$
\begin{equation}
\phi_\lambda(y) := \gamma_y(\lambda)
\end{equation}
$$

It is the point reached at parameter $\lambda$ by the integral curve starting at $y$. It can be read in two ways. At fixed $y$, letting $\lambda$ vary, we follow the curve $\gamma_y$: the trajectory of one point. At fixed $\lambda$, $\phi_\lambda : M\to M$ is a map moving all the points of $M$ at once. Since each $\gamma_y$ is an integral curve starting at $y$:

$$
\begin{equation}
\gamma_y'\vert_\lambda = X\vert_{\phi_\lambda(y)}\quad \forall y\in M,\qquad \phi_0 = \mathrm{Id}
\end{equation}
$$

Acting on any function $f$, this reads $\frac{\partial}{\partial\lambda}(f\circ\phi_\lambda) = X(f)\circ\phi_\lambda$, an equality between functions on $M$. Here $f\circ\phi_\lambda$ is the function $f$ after the motion, whose value at each point $y$ is $$[f\circ\gamma_y](\lambda)$$, and $X(f)$ is the function defined in the last paragraph below.

Following the flow for a parameter $\mu$ and then for a parameter $\lambda$ is the same as following it for $\lambda+\mu$ (this follows from the uniqueness of integral curves):

$$
\begin{equation}
\phi_\lambda \circ \phi_\mu = \phi_{\lambda+\mu}, \qquad \phi_0 = \mathrm{Id}, \qquad \phi_{-\lambda} = \phi_\lambda^{-1}
\end{equation}
$$

The flow is thus a **one-parameter group of diffeomorphisms** of $M$ (smooth maps $M\to M$ with a smooth inverse), and $X$ is called its **infinitesimal generator**. It is recovered from the flow as the velocity, at $\lambda=0$, of the integral curve starting at each point:

$$
\begin{equation}
X\vert_y = \gamma_y'\vert_0
\end{equation}
$$

Strictly speaking, $\phi_\lambda$ is defined on the whole of $M$ for all $\lambda\in\mathbb{R}$ only if $X$ is *complete*, i.e. if every maximal integral curve is defined on $I=\mathbb{R}$. This is the case for instance when $M$ is compact. Otherwise, each $\gamma_y$ is only defined on some interval around $0$, which depends on $y$.

**Rate of change of a function.** Moving a point along the flow changes the value of any function $f$. Applying the vector $X\vert_y = \gamma_y'\vert_0$ to $f$ gives a number:

$$
\begin{equation}
X\vert_y(f) = \frac{\text{d}}{\text{d}\lambda}(f\circ\gamma_y)\Big\vert_0
\end{equation}
$$

It is the rate of change of $f$ seen by the point starting at $y$: the directional derivative of $f$ along $X$ at $y$. Doing this at every point defines a new function $X(f) : y\mapsto X\vert_y(f)$, which in coordinates is

$$
\begin{equation}
X(f) = X^a\,\partial_a f
\end{equation}
$$

It is also called the Lie derivative $\mathcal{L}_Xf$ of $f$ along $X$. We recover in this way why a vector field is a first-order differential operator acting on functions, and thus, on phase space, on observables.

### Symplectic vector fields and Liouville's theorem

We saw that $\Omega$, similarly to a metric $g$, defines a product between vectors, $\Omega(X,Y) = A^iv_i - B_iu^i$. 

A vector field $X$ whose flow preserves the symplectic product between any two vectors $X,Y$,

$$
\begin{equation}
\Omega(\phi_{\lambda*}X,\phi_{\lambda*}Y) = \Omega(X,Y) \quad \text{for all } \lambda,
\end{equation}
$$

is said to be a **symplectic vector field**. Here $\phi_{\lambda*}$ denotes the pushforward of vectors by the flow. The maps $\phi_\lambda$ are then called **symplectic** (or **canonical**) **transformations**. Infinitesimally, this condition is equivalent to the vanishing of the Lie derivative of $\Omega$ along $X$, and, $\Omega$ being closed, to the closedness of $i_X\Omega$:

$$
\begin{equation}
\boxed{\mathcal{L}_X\Omega = 0 \quad \Longleftrightarrow \quad \text{d}(i_X\Omega) = 0}
\end{equation}
$$

In particular, **every Hamiltonian vector field is symplectic**: the transformations generated by observables preserve the symplectic structure of phase space.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

We use Cartan's formula, which gives the Lie derivative of a differential form along a vector field $X$:

$$\mathcal{L}_X = \text{d}\, i_X + i_X\, \text{d}$$

Applied to $\Omega$, and using that $\Omega$ is closed ($\text{d}\Omega=0$):

$$\mathcal{L}_X\Omega = \text{d}(i_X\Omega) + i_X(\text{d}\Omega) = \text{d}(i_X\Omega)$$

For a Hamiltonian vector field, $i_{X_G}\Omega = \text{d}G$ by definition, hence

$$\mathcal{L}_{X_G}\Omega = \text{d}(\text{d}G) = 0$$

because $\text{d}^2=0$.

</details>

Conversely, a symplectic vector field is always Hamiltonian locally: since $i_X\Omega$ is closed, the Poincaré lemma ensures that locally $i_X\Omega=\text{d}G$ for some function $G$. Globally, this can fail when phase space has "holes", such as the angle of a pendulum.

An important consequence is **Liouville's theorem**. Since the flow of a symplectic vector field preserves $\Omega$, it also preserves the volume form $\Omega^n/n!$ built from it. Phase-space volumes are therefore conserved: a cloud of states can be deformed by the flow, but its volume does not change, like an incompressible fluid. This is the key property used in [statistical physics](../../_thermo/statistical/phasespace.md).

### Observables as generators

Let $G$ be an observable, which we call the **generator**. Its Hamiltonian vector field $X_G$ defines a flow $\phi^G_\lambda : \mathcal{P} \to \mathcal{P}$, a one-parameter group of symplectic transformations labelled by a real parameter $\lambda$:

$$
\begin{equation}
(\phi^G_\lambda(x))' = X_G, \qquad \phi^G_0 = \mathrm{Id}.
\end{equation}
$$

Using the expression of $X_G$ in canonical coordinates obtained previously, these are simply Hamilton's equations, with $G$ playing the role of the Hamiltonian and $\lambda$ the role of time:

$$
\begin{equation}
\frac{\text{d}q^i}{\text{d}\lambda} = \frac{\partial G}{\partial p_i}, \qquad \frac{\text{d} p_i}{\text{d}\lambda} = -\frac{\partial G}{\partial q^i}.
\end{equation}
$$

<details markdown="1">
<summary><strong>Proof</strong></summary>

We saw that in a canonical coordinate frame:

$$X_G = \frac{\partial G}{\partial p_i} \partial_{q^i} - \frac{\partial G}{\partial q^i} \partial_{p_i} $$

On the other hand, in a coordinate frame $U\to \mathbb{R}^{2n}$, $x^i:(q,p)\to (q^i,p_i)$, the curve given by the flow starting at $x$, $\phi^G_\lambda(x)$ can be used to build the map $$ x^i \circ \phi^G_\lambda : [0,1]\times M\to U \to \mathbb{R}^{2n}$$ such that $$\lambda \to \phi^G_\lambda(x) \to (q^i(\lambda), p_i(\lambda)) $$ where we wrote $$p_i(\lambda):=p_i(\phi^G_\lambda(x))$$ and $$q^i(\lambda):=q^i(\phi^G_\lambda(x))$$. The tangent vector of the curve is then:

$$ (\phi^G_\lambda(x))' = \frac{\partial q^i}{\partial \lambda}\partial_{q^i} +\frac{\partial p_i}{\partial \lambda}\partial_{p_i}  $$

Equating the two vectors, one finds:

$$
\begin{equation}
\frac{\text{d}q^i}{\text{d}\lambda} = \frac{\partial G}{\partial p_i}, \qquad \frac{\text{d} p_i}{\text{d}\lambda} = -\frac{\partial G}{\partial q^i}.
\end{equation}
$$

</details>

Along this flow, any observable $F$ changes at the rate

$$
\begin{equation}
\boxed{
\frac{dF}{d\lambda} = X_G(F) = \lbrace F,G\rbrace
}
\end{equation}
$$

We say that $G$ is the **generator** of the transformation. This gives a first physical meaning to the Poisson bracket: $\lbrace F,G\rbrace$ is the rate of change of $F$ under the transformation generated by $G$.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Along the flow, $F$ depends on $\lambda$ through $q^i(\lambda)$ and $p_i(\lambda)$. By the chain rule and the equations of the flow,

$$
\begin{equation}
\frac{dF}{d\lambda} = \frac{\partial F}{\partial q^i}\frac{dq^i}{d\lambda} + \frac{\partial F}{\partial p_i}\frac{dp_i}{d\lambda}
= \frac{\partial F}{\partial q^i}\frac{\partial G}{\partial p_i} - \frac{\partial F}{\partial p_i}\frac{\partial G}{\partial q^i}
= \lbrace F,G\rbrace,
\end{equation}
$$

where we recognize the expression of the Poisson bracket in local coordinates.

</details>

The finite transformation is obtained by "exponentiating" the infinitesimal one. Formally, it is given by the Lie series

$$
\begin{equation}
F(\lambda) = e^{\lambda X_G} F = F + \lambda \lbrace F,G\rbrace + \frac{\lambda^2}{2!}\lbrace \lbrace F,G\rbrace ,G\rbrace + \dots
\end{equation}
$$

which converges for analytic $F$ and small enough $\lambda$.

### Canonically conjugate variables

When can the parameter $\lambda$ be identified with an observable? Suppose there is an observable $Q$ such that

$$
\begin{equation}
\lbrace Q,G\rbrace = 1 .
\end{equation}
$$

Then $dQ/d\lambda = 1$: along the flow of $G$, the value of $Q$ increases exactly like the parameter, $Q(\phi^G_\lambda(x)) = Q(x) + \lambda$. If moreover $Q$ and $G$ are part of a system of canonical coordinates, with $Q$ playing the role of a position and $G$ that of its conjugate momentum, then $X_G$ is simply the partial derivative with respect to $Q$, all other canonical coordinates being held fixed:

$$
\begin{equation}
\boxed{
X_G(F) = \lbrace F,G\rbrace = \frac{\partial F}{\partial Q}
}
\end{equation}
$$

$Q$ and $G$ are then called **canonically conjugate variables**, and $G$ is said to **generate translations of $Q$**. Note that the partial derivative $\partial/\partial Q$ only makes sense once the full coordinate system is specified, since it depends on which other coordinates are held fixed.

### Conservation laws and Noether's theorem

An observable $F$ is **conserved along the flow of $G$** if it does not change under the transformation generated by $G$:

$$
\begin{equation}
\frac{dF}{d\lambda} = \lbrace F,G\rbrace = 0 .
\end{equation}
$$

In particular, a generator is always conserved along its own flow, since $\lbrace G,G\rbrace = 0$.

Because the Poisson bracket is antisymmetric, $\lbrace F,G\rbrace = 0$ is equivalent to $\lbrace G,F\rbrace = 0$, that is, $X_G(F) = 0$ is equivalent to $X_F(G) = 0$. This innocent remark has an important consequence:

> $F$ is conserved along the flow of $G$ **if and only if** $G$ is conserved along the flow of $F$.

Taking $F = H$, the Hamiltonian (see below), this is the Hamiltonian form of **Noether's theorem**: an observable $G$ is conserved in time if and only if the Hamiltonian is invariant under the transformation generated by $G$. Conserved quantities and continuous symmetries are two faces of the same object.

### Time evolution

The **Hamiltonian** $H$ is the observable that generates time evolution: the parameter of its flow is the time $t$. For an observable $F$ with no explicit time dependence,

$$
\begin{equation}
\boxed{
\frac{dF}{dt} = X_H(F) = \lbrace F, H\rbrace
}
\end{equation}
$$

$X_H=\lbrace ., H\rbrace$ is thus the classical operator generating the time evolution of classical states. It is sometimes notes $\mathcal{L}$ and called the **Liouville operator**.
If $F$ depends explicitly on time, one has instead $\frac{dF}{dt} = \lbrace F,H\rbrace + \frac{\partial F}{\partial t}$. For $F = q^i$ and $F = p_i$, this gives back Hamilton's equations of motion:

$$
\begin{equation}
\frac{dq^i}{dt}= \frac{\partial H}{\partial p_i}, \qquad \frac{dp_i}{dt}= -\frac{\partial H}{\partial q^i}.
\end{equation}
$$

Like every Hamiltonian flow, time evolution is symplectic: it preserves the symplectic product of any two vectors, $$\Omega(\phi_{t*}u, \phi_{t*}v) = \Omega(u,v)$$, and hence phase-space volumes (Liouville's theorem). Moreover, applying the previous section with $G=H$, the energy is conserved, $$\frac{dH}{dt}=\lbrace H,H\rbrace=0$$.

Note that time is not an observable: $t$ is the parameter of the flow of $H$, not a function on phase space. One sometimes writes $\lbrace t,H\rbrace = 1$, but this only makes sense in the *extended* phase space, where time is promoted to a coordinate conjugate to the energy.

### Other generators

The coordinates $q^i$ and $p_i$, seen as local observables, are canonically conjugate:

$$
\begin{equation}
\lbrace q^i,p_j\rbrace =\delta^i_j .
\end{equation}
$$

We already obtained their classical operators, $X_{p_i} = \partial_{q^i}$ and $X_{q^i} = -\partial_{p_i}$. We can now read them as generators of transformations:

- **Momentum generates translations in space:**
$$
\begin{equation}
X_{p_j}(F) = \lbrace F,p_j\rbrace = \frac{\partial F}{\partial q^j}.
\end{equation}
$$
By Noether's theorem, if $H$ does not depend on $q^j$, the momentum $p_j$ is conserved.

- **Position generates translations in momentum**, with the opposite sign:
$$
\begin{equation}
X_{q^j}(F) = \lbrace F,q^j\rbrace = -\frac{\partial F}{\partial p_j}.
\end{equation}
$$
The flow of $q^j$ shifts the momentum $p_j$ in the negative direction, like an impulsive kick.

- **Angular momentum generates rotations.** For a particle with position $(x,y,z)$ and momentum $(p_x,p_y,p_z)$, the component $L_z = x\,p_y - y\,p_x$ is the momentum conjugate to the polar angle $\varphi$ around the $z$ axis, so that
$$
\begin{equation}
\lbrace F,L_z\rbrace = \frac{\partial F}{\partial \varphi}.
\end{equation}
$$
More generally, $L_i$ generates rotations around the axis $i$, and, by Noether's theorem, it is conserved whenever $H$ is invariant under these rotations.

Similar considerations apply to spin, to boosts in special relativity and to charges in gauge theories, as we will see later.

### Complete sets of observables

A set of observables $\lbrace F_i\rbrace$ is called **complete** if the only observables that Poisson-commute with all of them are the constants:

$$
\begin{equation}
\lbrace F_i,G\rbrace = 0 \ \text{for all } i \quad \Longrightarrow \quad G = \text{constant}.
\end{equation}
$$

Since $\lbrace F_i,G\rbrace = -X_{F_i}(G)$, this means that no non-constant observable is conserved along all the transformations generated by the $F_i$. Intuitively, by combining these transformations, one can move from any state to any nearby state. This is the classical analogue of the *irreducibility* of a set of operators in quantum mechanics. For instance, $\lbrace q^i, p_i\rbrace$ is complete, since the translations in $q$ and $p$ that it generates reach every state.

A complete set should not be confused with the **complete set of commuting observables** (CSCO) used in quantum mechanics: the observables of a complete set generally do *not* Poisson-commute with each other. Classically, $n$ Poisson-commuting observables (on a $2n$-dimensional phase space) only determine the orbit on which the state lies, not the state itself.

To individuate a state $x$ from the values $F_i(x)$, one needs a stronger condition: at each point, the differentials $\text{d}F_i$ must span the whole cotangent space, so that suitable $F_i$ can be used as local coordinates. Completeness alone does not guarantee this, but a set that is closed under the Poisson bracket and *transitive* (the $X_{F_i}$ span the tangent space at every point) does.

Of course, this discussion strongly echoes our discussion of [symmetries in quantum mechanics](../../_quantum/Quantum_advanced/Symmetry.md). The continuous symmetries of the Hilbert space are deeply related to the symmetries of the classical phase space, with the commutator $[\cdot,\cdot]$ playing the role of the Poisson bracket $\lbrace \cdot,\cdot\rbrace$. Finding the exact connection between the two is the whole topic of quantization procedures, which will be discussed in later lectures.

## Phase space as a vector space

Other formulations of symplectic geometry can be useful (Wald QFT in curved space-time)

$$\Omega_{ij} = \begin{pmatrix} &0 &\mathbb{I}_n\\ &-\mathbb{I}_n &0 \end{pmatrix}  $$

$$\lbrace\Omega(y_1,.),\Omega(y_2,.)\rbrace = \Omega(y_1,y_2)$$

## Going from tangent to contangent space

The **action**:

$$L_f = \theta(X_f) - f$$

## Further reading 

- V. Arnold - Mathematical Methods of Classical Mechanics.
- G. Catren -  Quantic fibers for classical systems: an introduction to geometric quantization 