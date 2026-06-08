---
layout: default
title: Hamiltonian mechanics and symplectic geometry
parent: maths
nav_order: 1
---

## Phase space and the tautological form

Let's consider a physical system described by its **configuration space** $\mathcal{Q}$. We saw in the previous lecture that the evolution of the system on $\mathcal{Q}$ can be described by finding the extremum of its action functional, expressed as the time integral of the Lagrangian function $L(q,\dot{q})$ defined on the tangent space $T\mathcal{Q}$, on which velocities are defined. As a reminder, a point of $T\mathcal{Q}$ is a doublet $(q,v)$, where $q$ is a generalized position and $v$ a velocity/tangent vector.

Alternatively, it is possible to describe its evolution on the cotangent space of $\mathcal{Q}$, also known as the **phase space** $\mathcal{P} = T^{\*} \mathcal{Q}$. A point in phase space is given by the doublet of a point of $\mathcal{Q}$ and a covector, noted $p$, that we will identify with momentum. Hence $x=(q,p)\in \mathcal{P}$.

Working in phase space instead of tangent space has several advantages. The most important one being that it renders apparent a special geometrical structure of classical mechanics: **symplectic geometry**. This geometry allows to investigate general **quantization procedures**, looking for a general and rigorous path to go from classical to quantum systems. This is for example the case of the so-called **geometric quantization**. 

Before going through this lecture, we recommend to first have a look at our previous lectures on [Hamiltonian mechanics](../../_meca/Analytical/Hamiltonian.md) and [Phase space for statistical physics](../../_thermo/statistical/phasespace.md).

A general one form field on $\mathcal{Q}$ would be written $ P_i(q)\text{d}q^i \in \Gamma(T^{\*}\mathcal{Q})$ (here and everywhere below, if an index is repeated, it is summed over).
When thinking of $\mathcal{P}=T^{\*}\mathcal{Q}$ as its own independent space, we consider every possible values of $P_i(q)$ at each point $q$, and promote it to its own coordinate, that we name $p_i$.
More precisely: it is always possible to find local coordinates on a chart $U \subseteq \mathcal{Q}$ such that a point $q\in \mathcal{Q}$ is labeled by coordinates $q^i$. Once the $q_i$ are chosen, we label $p_i$ the associated one-form coordinate such that $q_i$ and $p_i$ form **canonical coordinates**. As such, a general point $x\in \mathcal{P}$ is given by the tuple $x=(q^1, ..., q^{3\mathcal{N}},p_1, ..., p_{3\mathcal{N}})$. Where $\mathcal{N}$ is the number of particles if $\Pi$ describes a set of point-like particles allowed to move in three dimensions.
A general one form field on $\mathcal{P}$ is written

$$\eta =  A_i(q,p)\text{d}q^i  +  B^i(q,p)\text{d}p_i$$

which is a section of $T^{\*}(\mathcal{P}) = T^{\*}(T^{\*}\mathcal{Q})$, $\eta \in \Gamma(T^{\*}(\mathcal{P}))$ and the coordinates $A_i$ and $B^i$ are functions of $C^{\infty}(\mathcal{P})$, (i.e. $A_i: \mathcal{P}\to\mathbb{R}$ and $B^i: \mathcal{P}\to\mathbb{R}$). Similarly, a general vector field on $\mathcal{P}$ is written as

$$Y= u^i(q,p) \partial_{q^i} +  v_i(q,p)\partial_{p_i}$$

with $Y\in \Gamma(T\mathcal{P})$ and the coordinates $u^i$, $v_i$ are functions of $C^{\infty}(\mathcal{P})$.

## Symplectic geometry

The phase space inherits a peculiar geometry through the existence of the so-called **tautological one-form**. It is also known as Liouville one-form, the Poincaré one-form, the canonical one-form, or the symplectic potential. 
Once a coordinate chart is chosen, the tautological one form is defined as the special choice of one form field with $A_i(q,p)=p_i$ and $B_i=0$, that is:

$$\boxed{\theta =  p_i \text{d} q^i}$$

As discussed below the value of $\theta$ is independent of the choice of local coordinates, and admits a coordinate independent definition.

<details markdown="1">
  <summary><strong>More details on the tautological form</strong></summary>

As a fiber bundle, $\mathcal{P}$ is equipped with a projection map $\pi$ to its base space:

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

Clearly, this definition does not depend on any choice of coordinatization of $\mathcal{P}$. 
Choosing local coordinates immediately gives

$$
\theta=p_i\,\mathrm dq^i.
$$

Indeed, consider a general vector at the point $q,p$:

$$X= u^i \partial_{q^i} +  v_i\partial_{p_i}$$

The pushforward is:

$$\pi_*(X) = u^i\partial_{q^i}$$

Now, the one-form $p_i\text{d}q^i \in T^*_q(\mathcal{Q})$ can act on it to give

$$p(\pi_*(X)) = p_i u^i$$

As subtle point: while $p=p_i\text{d}q^i$ is a one form on $\mathcal{Q}$, $$p \circ \pi_*= p_i \text{d}q^i + 0 \text{d}p_i$$ is a one form on $\mathcal{P}$. While both take the same form in coordinates, they are thus different objects.

</details>

A symplectic manifold is a pair $(M,\omega)$, with $M$ a smooth manifold and $\omega$ a symplectic form.
A 2-form field $\omega \in \Omega^2(\mathcal{P}_s)$ is said to be a **sympletic form** if

- $\omega$ is **closed** i.e. $\text{d}\omega = 0$.
- $\omega$ is **non-degenerate**: If there exist $X \in T\mathcal{\mathcal{P}}$ such that $\forall Y\in T\mathcal{\mathcal{P}}$, $\omega(X,Y)=0$, then $
X=0$.

$\theta$, already present necessarily on $\mathcal{P}$, endows the phase space with a symplectic structure. Indeed, taking its exterior derivative, one obtains the symplectic form defined as

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

If $F$ is a smooth function (observable) defined on $\mathcal{P}$, we can define the Hamiltonian vector field $X_F$ of $F$ as

$$
\begin{equation}
    \boxed{
\text{d} F = \Omega(X_F,\cdot)
    }
\end{equation}
$$

which is sometimes written equivalently using the interior derivative as $\text{d} F = i_{X_F} \Omega$.

In coordinates, the vector solving this equation takes the form:

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


## Poisson Bracket and Hamiltonian vector fields

As discussed before, physical observables are functions on the phase space manifold $\mathcal{P}$, noted $\mathcal{O}= C^{\infty}(\mathcal{P})$.
Let $F,G \in C^{\infty}(\mathcal{P})$ be two observables, we introduce the **Poisson bracket** product on them as

$$
\begin{equation}
\boxed{
\lbrace F,G\rbrace  := \Omega(X_F,X_G)}
\end{equation}
$$

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
- $[X_F,X_G]= X_{\lbrace F,G\rbrace }$. 

<details markdown="1">
  <summary><strong>Proof </strong></summary>

</details>

The Poisson bracket also obeys **Leibniz rule** for the product of functions, making it a sort of **differential operator**:

- $\lbrace FG, H\rbrace = F\lbrace G,H\rbrace + G \lbrace F,H\rbrace$
- $\lbrace F, FG \rbrace = g \lbrace F,H\rbrace + H\lbrace F,G \rbrace$

<details markdown="1">
  <summary><strong>Proof </strong></summary>

</details>

The Poisson bracket can be rewritten in several equivalent ways, highlighting some of these properties. For instance, using the definition of $X_F$ we also have 

$$
\begin{equation}
\lbrace F,G\rbrace  = \text{d} G(X_F) =  X_F(G) = \mathcal{L}_{X_F}G
\end{equation}
$$

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

Let's now consider the Lie algebra formed by the observables. Let's consider a generator $G$ which generates transformations of  any observable $f$ under a variation of another observable $F$ as $\delta f=e^{GF}f$. If the observable $G$ is a conserved quantity under variations of the observable $F$, then, one has, for any observable $f$:

$$
\begin{equation}
\boxed{
X_G(f) = \lbrace f,G\rbrace = \frac{\partial f }{\partial F}
}
\end{equation}
$$

We say that $G$ is the generator of the evolution of the system under variations of $F$. 

<details markdown="1">
  <summary><strong>Proof</strong></summary>

Under a variation of $F$, any observable $f$ transforms as
$$
\begin{equation}
\delta f = \frac{\partial f}{\partial q_i} \delta q_i + \frac{\partial f}{\partial p_i}\delta p_i
\end{equation} 
$$

where $\delta q_i$ and $\delta p_i$ are the changes of position in phase space due to a change of $F\to F+\delta F$.
Let's now assume that this change is generated by $G$ as $f=fe^{G F}$ such that $\delta f = G \delta F$.

Now if $G$ is conserved

$$
\begin{equation}
\delta G = \frac{\partial G}{\partial q_i}\frac{\partial q_i}{\partial F} + \frac{\partial G}{\partial p_i}\frac{\partial p_i}{\partial F} =0
\end{equation}
$$

such that
$$
\begin{equation}
\frac{\partial G}{\partial q_i}\frac{\partial q_i}{\partial F} = -\frac{\partial G}{\partial p_i}\frac{\partial p_i}{\partial F}
\end{equation}
$$

which is satisfied for

$$
\begin{equation}
\frac{\partial G}{\partial p_i} = \frac{\partial q_i}{\partial F} \qquad \frac{\partial G}{\partial q_i} = -\frac{\partial p_i}{\partial F}
\end{equation}
$$

approximating the derivatives as $\partial G \partial X \simeq \delta G/\delta X$, we find

$$
\begin{equation}
\delta q_i = \frac{\partial G}{\partial p_i}\delta F \qquad \delta p_i = -\frac{\partial G}{\partial q_i}\delta F
\end{equation}
$$

Re-inserting these expressions in our first expression for $\delta f$, we find that

$$
\begin{equation}
\delta f = \frac{\partial f}{\partial q_i}\frac{\partial G}{\partial p_i}\delta F - \frac{\partial f}{\partial p_i}\frac{\partial G}{\partial q_i}\delta F = \lbrace f,G\rbrace \delta F
\end{equation}
$$

such that

$$
\begin{equation}
\frac{\partial f}{\partial F}= \lbrace f,G\rbrace 
\end{equation}
$$

</details>

$X_G$ is then the gradient of $F$. Integral curves and vector flows

$$
\begin{equation}
\frac{\partial \phi^G}{\partial F} = X_G
\end{equation}
$$

As such, we have $\lbrace F,G\rbrace = \partial_F F = 1$. $F$ and $G$ are said to be **canonical variables**.

The generator is conserved under variations of $F$ as $\partial_FG=\lbrace G,G\rbrace = 0$.

Any observable $f$ such that $\lbrace f,G\rbrace =0$ is called a conserved quantity under variations of $F$, signifying that $f$ remains unchanged through the $F$ evolution of the system generated by $G$ ($\partial_F f=0$).

### Time evolution

The Hamiltonian function $H$ is defined as the observable generating time translations

$$
\begin{equation}
X_H(f) := \lbrace f, H\rbrace  = \frac{\partial f}{\partial t}
\end{equation}
$$

$H$ is the generator of the time $t$ evolution/translations and $\lbrace t,H\rbrace =1$.

This gives back Hamilton's equations of motion for $f=q_i$ and $f=p_i$:

$$
\begin{equation}
\frac{\partial q_i}{\partial t}= \frac{\partial H}{\partial p_i}\qquad \frac{\partial p_i}{\partial t}= -\frac{\partial H}{\partial q_i}
\end{equation}
$$

The symplectic product between two vectors is preserved by time evolution.

### Other observables

Position and momentum satisfy

$$
\begin{equation}
\lbrace q^i,p_j\rbrace =\delta^i_{j}
\end{equation}
$$

such that they are canonical variables for $i=j$.
We find that

$$
\begin{equation}
X_{p_i}=\lbrace f,p_i\rbrace = \frac{\partial f}{\partial q^i}
\end{equation}
$$

$p_j$ is thus the generator of the space $q^j$ translations. And the other way around

$$
\begin{equation}
X_{q_i}(f)=\lbrace f,q_i\rbrace = \frac{\partial f}{\partial p^i}
\end{equation}
$$

such that $q_i$ can be understood to generate space translations.

Similarly $L_i$ is the generator of the spatial rotations $\theta$ around the axis $i$.

$$
\begin{equation}
\lbrace f,L_i\rbrace = \frac{\partial f}{\partial \theta}
\end{equation}
$$

Similar considerations can be done for spin (quantum mechanics), boosts (special relativity) and gauge charge (gauge theories) later.

Of course, this discussion echoes strongly with our discussion of the [symmetries in quantum mechanics](../../_quantum/Quantum_advanced/Symmetry.md). As such, it is clear that the continuous symmetries present on the Hilbert space are deeply related with the symmetries on the classical phase space, where the commutator $[.,.]$ playing the role of the Poisson bracket $\lbrace .,.\rbrace$. Finding the exact connection between both is the whole topic of quantization procedures which will be the topic of later discussions.

## Phase space as a vector space

$$\Omega_{ij} = \begin{pmatrix} &0 &\mathbb{I}_n\\ &-\mathbb{I}_n &0 \end{pmatrix}  $$

$$\lbrace\Omega(y_1,.),\Omega(y_2,.)\rbrace = \Omega(y_1,y_2)$$

## Going from tangent to contangent space

The **action**:

$$S = \theta(X_H)$$