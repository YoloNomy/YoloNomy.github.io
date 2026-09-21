---
layout: default
title: CMB polarisation
parent: cosmo
nav_order: 1
---

# The CMB polarisation as a playground for differential geometry and group theory

We will see that the CMB polarisation provides a wonderful playground to apply and understand ideas of Riemannian geometry, differential geometry and group theory. Many striking parallels will arise with quantum mechanics, highlighting the depth and generality of the mathematical concepts considered.

*Warning: this class is dedicated for amateurs of mathematics, you can safely skip it if you do not care about these tools.*
 
## The sky as the Riemannian manifold $S^2$

### The sky as a set

Imagine you are sitting in empty space, or on board a satellite, ready to observe the CMB.

Look at a star. What reaches your eye is a stream of photons, all travelling along one and the same straight line. You label that star by the direction from which that line arrives.

As a side note, notice that the label does not care about the photons themselves: a red photon and a blue photon emitted by the same star travel along the *same* line, carrying different energies but arriving from the same place on the sky. **A point of the sky is a light ray — a direction. Rescaling the energy of the light changes nothing about it.** In spacetime language one says that all photons propagate along **null** geodesics (directions along
which the spacetime interval vanishes), and that multiplying a photon's four-momentum by any positive number leaves the ray unchanged. We will not need this language for a while; it is quoted here only so that the word "null" is not a surprise later. That all photons follow the same rays whatever their frequency is a one of the aspects of equivalence principles at the eart of general relativity; see our [dedicated lecture](../modified_gravity/foundations-GR.md).

Now stand still and point your arm at each star in turn. The set of directions your arm can take
is the set of unit vectors of ordinary three-dimensional space. So the sky is **the set of all directions**. Such a set clearly forms a sphere, which we could simply define abstractly as such. This would be the proper mathematical way to go. However, to build some intuition, we will create the sphere as a two-dimensional space embedded in our three-dimensional one. This will help us build an intuition and apply basic notions of topology. However, keep in mind that, in the end, nothing depends on this embedding and the sphere could simply be defined abstractly.

Consider then the set $$\mathbb{R}^3$$ as all the collection of triplets $$(x,y,z)$$, each labelling a point in space. The triplet $$(0,0,0)$$, which is a member of this set, represents the position of the observer (you!) in space. Now, all the directions can be labelled by an "arrow of length one" pointing in the direction (this seems to imply notions such as norm and angles, but we will try not to use them now).

The set of all directions is thus characterized by all the points at distance one from the center of $$\mathbb{R}^3$$, that is

$$
\boxed{\ S^2=\{(x,y,z)\in\mathbb{R}^3 \;:\; x^2+y^2+z^2=1\}\ }
$$

Note that the choice of length one is of course totally arbitrary, as a vector of any length would point in the same direction. In other word: the **celestial sphere** is a sphere at which you are at the center, but we do not care at all about its size (we intuitively imagine it as gigantic, but it has no size really). Hence, while this definition might seems to use the notion of distance in $$\mathbb{R}^3$$, it then forgets about it.
The description above uses three numbers, $x$, $y$ and $z$, but they are not independent: they
must satisfy the one equation $x^2+y^2+z^2=1$. One equation removes one degree of freedom, which
leaves two. Each element of this set is labelled by two real numbers. These two numbers could be $x$ and $y$, then would then be fixed by $$z=\sqrt{1-y^2-x^2}$$. We see already that this equation has two solutions, corresponding to two opposite orientations. This already hints at a deeper problem we will encounter later, but we leave this for the next sections. These two numbers to label every point of the set will come back as the most practical notions of the two angles $\varphi$ and $\theta$.

That is pretty much all we can say about the sky as a **set**: it is just a collection of points that can be thought as points in $$\mathbb{R}^3$$ at a distance 1 from the observer, even though this mental image already invoke implicitely other notions that will be defined below. A set has no notion of "near", so at this stage we cannot yet say that two stars are close together, nor that a planet moves *continuously* across the sky. Supplying the missing notion will require topology.

### The sky as a topological space

A **topology** on a set $M$ is a collection $\mathcal{T}$ of subsets of $M$ — its members are called the **open sets** — such that

 1. $\varnothing\in\mathcal{T}$ and $M\in\mathcal{T}$;
 2. any union (finite or infinite) of open sets is open;
 3. any **finite** intersection of open sets is open.

The pair $(M,\mathcal{T})$ is a **topological space**. As said already a set $U\in \mathcal{T}$ is called an open set. A said $A\subseteq M$ is said to be closed if its complement $$A^c = M-A$$ is open. A set can be both open and close (clopen) in a given topology. This is the case of $\varnothing$ and $M$ for any topology.

A topology is the minimal structure that lets one say two points are *close*, without saying
*how* close. It is exactly what is needed to define continuity, and nothing more: a topological
space has no notion of distance, angle, length or volume. All of that arrives only later. A topology is a rule specifying the *neighbourhoods* of each point, that is, all the open sets containing that point. More precisely a neighborhood $$N \subseteq M $$ of a point $p \in M$ is a subset containing at least one open set $U$ at which $p$ belong. If $N$ is also open it is said to be an **open neighborhood**.

Another key definition we will need is that a map $f:M\to N$ between topological spaces is **continuous** if the preimage

$$
{\rm Preim}_f(V)=\{x\in M \;:\; f(x)\in V\}
$$

of every open set $V\subseteq N$ is open in $M$. A map takes every element of $M$ and returns an element of $Y$. For our next discussion, we define **curves** as a special type of map, going from the interval $[0,1]\subset \mathbb{R}$ to our space of interest (here $S^2$). $$\gamma: [0,1]\to S^2, t \to \gamma(t)$$. A curve is thus continuous if, for every open set of $S^2$ allowed by our topology, the set of times at which the curve sits inside it is an open set of $[0,1]$.

<details markdown="1">
<summary><strong>A warning (to read once you've learn about induced topologies)</strong></summary>

One warning on that last phrase, which is a classic trap. The interval $[0,1]$ is not itself $\mathbb{R}$, and it carries the topology *induced* from $\mathbb{R}$ — the general construction is in the box below. Its open sets are the intersections with $[0,1]$ of the open sets of $\mathbb{R}$, so that $[0,\tfrac12)$ counts as open in $[0,1]$ even though it is not open in $\mathbb{R}$. This is not a detail we can skip: a curve is inside some open set of $S^2$ at the initial time $t=0$, and the corresponding set of times will typically look like $[0,\delta)$. Asking for openness in $\mathbb{R}$ rather than in $[0,1]$ would declare almost every curve discontinuous.

</details>

#### The topology of the celestial sphere: induced standard topology or a beam topology

Now, what topology should we propose for the celestial sphere? We would like the topology to match our intuition: a curve on the sky, for example the trajectory of a planet, should be continuous if we can "draw it without dropping the pen". In three dimensions, this is exactly what is provided by the **standard, or open ball, topology** on $\mathbb{R}^3$. The **standard topology on $\mathbb{R}^n$** is generated by the open balls. An open ball of radius $r$ centred at a point $p=(p_1,\dots,p_n)$ is

$$B_r(p)=\Big\{ (q_1,\dots,q_n)\in\mathbb{R}^n\ \Big\vert\ \sum_{i=1}^n (q_i-p_i)^2 <r^2\Big\}.$$

A set $U\subseteq\mathbb{R}^n$ is open in the standard topology when every point of $U$ has some ball around it entirely contained in $U$. In other words

$$\mathcal{T}_s = \{U \subseteq \mathbb{R}^n \ \vert\ \forall p \in U,\ \exists r \in \mathbb{R}^+ : B_r(p) \subseteq U\}.$$

Why does this topology capture the "not dropping the pen" intuition of continuity? Consider a curve in space $$\gamma : [0,1]\to \mathbb{R}^3$$. If you consider an open ball somewhere where there is no curve, it's preimage under $$\gamma$$ is $$\varnothing$$, which is open in $[0,1]$. Fine. Now consider a large open ball that contains all the curve, it's pre-image is the whole interval $$[0,1]$$, which is also open. Now if the curve is really one single curve (drawn without dropping the pen), each open ball you can draw on it, will be associated to an open set in $[0,1]$, even if it contains its extremities (because $$[0,a)$$, and $$(a,1]$$ are open in $[0,1]$). However, if the curve makes a "jump", an open ball containing one of the intermediate extremities will be associated to a set $$(a,b]$$ or $$[a,b)$$, which are not open.

Made precise, the topological definition and the $\varepsilon$–$\delta$ definition of continuity you already know are one and the same statement.

<details markdown="1">
<summary><strong>The topological and the $\varepsilon$–$\delta$ definitions agree</strong></summary>

Let $$\gamma:[0,1]\to\mathbb{R}^n$$. The classical undergraduate definition of continuity says that $\gamma$ is continuous at $t$ when, for every $$\varepsilon>0$$, there exists $$\delta>0$$ such that every $$s\in[0,1]$$ with $$\vert s-t\vert<\delta$$ satisfies $$\vert\gamma(s)-\gamma(t)\vert<\varepsilon$$, that is $$\gamma(s)\in B_\varepsilon(\gamma(t))$$. This is now understood as just a restricted application of the broader concept of continuity defined on topological spaces.

Assume this holds at every $t$, and let $$U\subseteq\mathbb{R}^n$$ be open. Take any $t$ in ${\rm Preim}_\gamma(U)$. Since $U$ is open and contains $\gamma(t)$, there is an $$\varepsilon>0$$ with $$B_\varepsilon(\gamma(t))\subseteq U$$. The $$\varepsilon$$–$$\delta$$ property supplies a $\delta>0$ for which $$(t-\delta,t+\delta)\cap[0,1]$$ is mapped inside $$B_\varepsilon(\gamma(t))$$, hence inside $U$. So every point of $${\rm Preim}_\gamma(U)$$ has an open interval of $[0,1]$ around it still inside $${\rm Preim}_\gamma(U)$$, which is precisely the statement that $${\rm Preim}_\gamma(U)$$ is open in $[0,1]$.

Conversely, assume preimages of open sets are open, and fix $t$ and $\varepsilon>0$. The ball $$B_\varepsilon(\gamma(t))$$ is open, so $$\text{Preim}_\gamma\big(B_\varepsilon(\gamma(t))\big)$$ is open in $$[0,1]$$ and contains $t$. By the definition of the induced topology it therefore contains a set of the form $(t-\delta,t+\delta)\cap[0,1]$ for some $\delta>0$, and that is exactly the $\varepsilon$–$\delta$ condition.

Notice where the balls were used: in the first half to produce an $\varepsilon$ from an open set, in the second half to produce an open set from an $\varepsilon$. The equivalence is really the statement that the balls *generate* the standard topology.

</details>

The natural solution is then to say that $S^2$ inherits its topology from $\mathbb{R}^3$ — the **subspace topology** or **induced topology**, defined in the box below.

<details markdown="1">
<summary><strong>The subspace topology</strong></summary>

$S^2$ is a subset of $\mathbb{R}^3$, but the balls of $\mathbb{R}^3$ are not subsets of $S^2$, so
$S^2$ does not automatically inherit open sets. The following rule supplies them.

Let $(M,\mathcal{T})$ be a topological space and $A\subseteq M$. The
**subspace topology** (also *induced* or *relative* topology) on $A$ is
 $$\mathcal{T}_A=\{\,U\cap A \;:\; U\in\mathcal{T}\,\}.$$
The open sets of $A$ are the traces on $A$ of the open sets of $M$.

*This really is a topology.* Set-theoretic distributivity does all the work:
$\varnothing=\varnothing\cap A$ and $A= M\cap A$; then

$$\bigcup_{i\in I}(U_i\cap A)=\Big(\bigcup_{i\in I}U_i\Big)\cap A,
\qquad
\bigcap_{i=1}^{n}(U_i\cap A)=\Big(\bigcap_{i=1}^{n}U_i\Big)\cap A,$$

and the right-hand sides are of the required form because $\mathcal{T}$ is a topology.

Clearly, "open in $A$" and "open in $M$" are *different* statements.
The spherical cap $C=\{x\in S^2 : z>\tfrac12\}$ is open in $S^2$, since
$C=S^2\cap\{z>\tfrac12\}$ and $\{z>\tfrac12\}$ is open in $\mathbb{R}^3$. But $C$ is **not**
open in $\mathbb{R}^3$: any three-dimensional ball centred on a point of $C$ contains points off the sphere. The interval $[0,1]$ used above is the same phenomenon: $[0,\tfrac12)$ is open in $[0,1]$ and not in $\mathbb{R}$.

Now, why should we use this topology and not another? Because it is the **coarsest** topology on $A$ — the one with the fewest open sets — for which the inclusion $\iota:A\hookrightarrow M$, $\iota(a)=a$, is
continuous. It therefore adds nothing and removes nothing: it is precisely the structure $A$
already had by sitting inside $M$.

</details>

This intuition matches a "beam topology". Any real instrument points somewhere with a finite beam. It never reports "the source is exactly at $\hat n$"; it reports "the source lies within $\epsilon$ of $\hat n$". The primitive
observational statements about the sky are therefore exactly the **beams**

$$
B_\epsilon(\hat n)=\{\hat m \in S^2 \;:\; \text{angle}(\hat m,\hat n)<\epsilon\},
$$

the open spherical caps. We declare a subset of the sky open when every direction in it has a
whole beam around it still inside the set, however small that beam may need to be. A set containing a single point is then not open, since no beam, however narrow, consists of one single direction. **Thus, the topology of the celestial sphere is the topology generated by beams.** Choosing it amounts to asserting that the only meaningful statements about a direction are statements of finite angular precision.

This is not a second, competing proposal: the beams *are* the traces on $S^2$ of the balls of $\mathbb{R}^3$, so the two constructions give the very same open sets.

<details markdown="1">
<summary><strong>Beams are exactly the traces of balls</strong></summary>

Let $p\in S^2$. Intersecting a ball of $\mathbb{R}^3$ centred on $p$ with the sphere gives

$$
S^2\cap B_r(p)=\{q\in S^2 \;:\; \sum_i^3 (q_i-p_i)^2<r^2\},
$$

a ball measured with the straight-line, or *chordal*, distance rather than with the angle. The two are related: writing $\Delta$ for the angle between $\vec{p}$ and $\vec{q}$, both being unit vectors pointing in directions on the sphere, 

$$\|q-p\|^2=(\vec{q}-\vec{p})\cdot (\vec{q}-\vec{p})= 2-2\cos\Delta=4\sin^2(\Delta/2)$$

so the distance in $\mathbb{R}^3$$ between $p$ and $q$ is

$$
\|q-p\|=2\sin\big(\Delta/2\big).
$$

The function $t\mapsto2\sin(t/2)$ is continuous and strictly increasing from $$[0,\pi]$$ onto $$[0,2]$$, so the condition $$\vert q-p \vert <r$$ is the *same* condition as $\Delta<2\arcsin(r/2)$. Every trace of a ball centred on the sphere is therefore a beam, and every beam is such a trace, with the radii merely relabelled.

The topology cannot tell "chord" from "arc"; only a metric will be able to, and that is still several sections away. It is a first, small instance of the fact that a topology forgets distances while retaining nearness.

</details>

Two extreme alternatives show that the axioms are doing real work.

- If *every* subset were open (infinitely sharp beams, the **discrete** topology), no curve would be continuous, or more precisely the only continuous curves left would be the ones that never move. A planet crossing the sky would fail to be continuous.
- If only $\varnothing$ and $S^2$ were open (infinitely broad beams, the **indiscrete** topology, also called trivial or coarse), then no two stars could be separated by disjoint neighbourhoods, and *every* map whatsoever would be continuous — including one that teleports instantly from one star to another, since the only preimages to check are $\varnothing$ and $[0,1]$, both open. Continuity would tell us nothing at all.

<details markdown="1">
<summary><strong>In the discrete topology, only constant curves are continuous</strong></summary>

Suppose $S^2$ carries the discrete topology, in which *every* subset is open, and let
$\gamma:[0,1]\to S^2$ be a continuous curve.

Every singleton $\{x\}$ of $S^2$ is then open, so continuity forces every preimage
${\rm Preim}_\gamma(\{x\})$ to be open in $[0,1]$. For the directions the curve never visits this
says nothing, the preimage being empty and the empty set being open; the content lies in the
directions actually attained. For those, recall what "open in $[0,1]$" means: every instant in the
set must have a whole interval of $[0,1]$ around it still inside the set. A single instant $\{a\}$ is therefore never open. **The curve cannot visit a direction for one isolated instant: whenever it is at $x$, it must remain at $x$ for a whole interval of time.**

This is already enough to forbid any *transition*. Suppose the curve did move, and look at the first instant at which it has left its starting direction. Just before that instant the curve sits at $\gamma(0)$; at that instant it sits somewhere else; and the preimage of the new direction, being open, must contain an interval reaching back to *before* that instant. The two preimages would then share instants, which is impossible, since a curve cannot be at two directions at once. There is no
room for the transition to happen.

Made precise, write $x_0=\gamma(0)$ and $A={\rm Preim}_\gamma(\{x_0\})$, and set

$$t^\ast=\sup\big\{t\in[0,1] \;:\; [0,t]\subseteq A\big\}.$$

The set on the right is not empty: $A$ is open and contains $0$, so it contains $[0,\delta)$ for some
$\delta>0$. Hence $t^\ast$ exists, by the least-upper-bound property of the real numbers.

If $$\gamma(t^\ast)=x_0$$, then $$t^\ast$$ belongs to $A$, and since $A$ is open it contains a whole
interval around $t^\ast$. That would contradict the definition of the supremum, unless $t^\ast=1$; so
$t^\ast=1$, the whole of $[0,1]$ lies in $A$, and the curve is constant.

If instead $$\gamma(t^\ast)=x_1\neq x_0$$, then $$B={\rm Preim}_\gamma(\{x_1\})$$ is open and contains
$t^\ast$, so it contains an interval of the form $$(t^\ast-\eta,\,t^\ast]$$. But by construction every
instant strictly below $t^\ast$ lies in $A$, so those instants would lie in $A$ and in $B$ at once.
Since $x_0\neq x_1$ the two preimages are disjoint, and this is a contradiction.

Only the first case survives, so $\gamma$ is constant.

Two remarks are worth keeping. The argument used nothing but the least-upper-bound property of
$\mathbb{R}$, and it is in fact the standard proof that $[0,1]$ is **connected**, that is, cannot be
written as the union of two disjoint non-empty open sets. Granting that, the whole proof collapses to
one line: the preimages ${\rm Preim}_\gamma(\{x\})$ are open, pairwise disjoint and cover $[0,1]$, so
exactly one of them is non-empty.

And notice where the domain did the work. Had the curve been defined on $[0,1]\cup[2,3]$ instead, a
map equal to one direction on the first piece and to another on the second would have open preimages,
would be perfectly continuous, and would not be constant. The theorem is a statement about the
interval quite as much as about the discrete topology.

</details>

The practical payoff of the choice we made is the one we want. The beam topology makes continuous exactly those curves that can be drawn without lifting the pen: no fewer, as the discrete topology would, and no more, as the indiscrete one would.

#### Additional topological properties

The sky now has a topology, and with it come four properties that we shall draw on repeatedly. It is
worth being honest about their status. The first two are entirely unremarkable: *every* subset of
$\mathbb{R}^n$ has them, and the sphere inherits them without doing anything. That is precisely why
they are worth recording — we get them for free, and they are exactly the two hypotheses that the
definition of a manifold will demand of us later. The last two are genuine features of the sphere, and they are the ones that will do real work.

Each of the four answers a question you can ask about the sky in plain words. Can two distinct stars
always be told apart? Is a countable catalogue of observations enough to describe everything? Can
anything run away to a place we cannot see? Is the sky all in one piece?

**Definition.** A topological space $M$ is **Hausdorff** if any two distinct points can be separated by
disjoint open sets: for all $p\neq q$ in $M$ there exist open sets $U$ and $V$ with $p\in U$, $q\in V$
and $U\cap V=\varnothing$.

On the sky this says something an observer takes for granted: two distinct directions can always be
resolved. Point two beams, each narrower than half the angle between the two stars, and no direction
whatsoever lies in both. If the property failed, then however finely you narrowed your instrument the
two stars would always leak into one another's beams, and no observation of finite precision could ever
separate them.

It is worth seeing that the property can genuinely fail, because otherwise the definition looks like an
empty formality. Take two copies of the real line and glue them together at every point *except* the
origin, leaving two distinct origins $0_a$ and $0_b$. Away from the origins the open sets are the usual
ones; a neighbourhood of $0_a$ is a set of the form $(-\delta,0)\cup\{0_a\}\cup(0,\delta)$, and likewise
for $0_b$. This is a perfectly good topological space, and near any of its points it is
indistinguishable from $\mathbb{R}$. Yet any neighbourhood of $0_a$ and any neighbourhood of $0_b$ share
the punctured intervals $(-\delta,0)$ and $(0,\delta)$, so they always intersect: the space is not
Hausdorff. The damage is concrete — the sequence $1/n$ converges to $0_a$ *and* to $0_b$, so limits are
no longer unique, and the phrase "the direction the planet is heading towards" would cease to have a
single meaning.

<details markdown="1">
<summary><strong>Proof: the sky is Hausdorff</strong></summary>

We prove two statements, and then combine them.

**The space $\mathbb{R}^n$ with its standard topology is Hausdorff.** Recall the triangle inequality,
$\|u+w\|\le\|u\|+\|w\|$, valid for the Euclidean norm. Let $p\neq q$ and put $d=\|p-q\|$, a strictly
positive number since the two points differ. Consider the two balls $B_{d/2}(p)$ and $B_{d/2}(q)$,
which are open by the definition of the standard topology and contain $p$ and $q$ respectively. Suppose
some point $y$ belonged to both. Writing $p-q=(p-y)+(y-q)$ and applying the triangle inequality,

$$
d=\|p-q\|\ \le\ \|p-y\|+\|y-q\|\ <\ \frac{d}{2}+\frac{d}{2}\ =\ d ,
$$

where the strict inequality is precisely the statement that $y$ lies in both balls. We have obtained
$d<d$, which is absurd, so no such $y$ exists and the two balls are disjoint.

**Any subspace of a Hausdorff space is Hausdorff.** Let $M$ be Hausdorff and $A\subseteq M$, equipped
with the subspace topology. Take $p\neq q$ in $A$. Since they are in particular distinct points of $M$,
there are disjoint open sets $U\ni p$ and $V\ni q$ of $M$. Their traces $U\cap A$ and $V\cap A$ are open
in $A$, by the very definition of the subspace topology; they contain $p$ and $q$, which lie in $A$;
and they are disjoint, since $(U\cap A)\cap(V\cap A)\subseteq U\cap V=\varnothing$.

Applying the second statement with $A=S^2$ inside $M=\mathbb{R}^3$ gives the result. The separating sets
are exactly the beams promised above: intersecting a small ball of $\mathbb{R}^3$ centred on a direction
with the sphere produces a spherical cap.

</details>

**Definition.** A **basis** of a topology on $M$ is a collection $\mathcal{B}$ of open sets such that every open set of $M$ is a union of members of $\mathcal{B}$. The members of $\mathcal{B}$ are the building blocks from which all open sets are assembled. Clearly, the set of all open balls $$B_r(p)$$ forms a basis for the standard topology on the set $$\mathbb{R}^d$$. Hence, the standard topology can be defined alternatively as the topology where open sets are open balls as well as their unions and finite intersections. 

**Definition.** A set is **countable** if it is finite, or if its elements can be listed in an infinite sequence indexed by the natural numbers. The integers are countable, and so are the rationals: one enumerates the fractions $p/q$ by increasing $$\vert p\vert+q$$, which exhausts them all. A finite product of countable sets is again countable, by interleaving the lists.

**Definition.** A topological space is **second countable** if it admits a basis with countably many members.

The observational reading is direct. It says that one fixed, countable catalogue of beams is enough to express any open statement about the sky whatsoever: every measurement of finite angular precision, no matter how it was pointed, can be assembled from beams taken from that list. It is a statement that the space is not unmanageably large.

Here too the property can fail, and the failure is one we have already met. Give the sky the discrete topology, in which every subset is open. Any basis must then contain every singleton $\{x\}$: writing $\{x\}$ as a union of basis elements requires at least one non-empty basis element contained in $\{x\}$, and the only such set is $\{x\}$ itself. So a basis has at least as many members as there are directions in the sky, which is uncountably many. The discrete topology — the topology of infinitely sharp beams — is not second countable, and this is a second, independent reason for rejecting it.

<details markdown="1">
<summary><strong>Proof: the sky is second countable</strong></summary>

Again we prove two statements and combine them. One preliminary definition is needed.

**Definition.** A subset $D$ of $\mathbb{R}^n$ is **dense** if every ball, however small, contains a
point of $D$. The rationals are dense in $\mathbb{R}$: given a real $t$ and $\varepsilon>0$, choose an
integer $N$ with $1/N<\varepsilon$ and take the largest integer $m$ with $m/N\le t$, so that
$|t-m/N|<1/N<\varepsilon$. It follows that $\mathbb{Q}^n$ is dense in $\mathbb{R}^n$: approximate each
of the $n$ coordinates of a point $p$ to within $\varepsilon/\sqrt{n}$ by a rational, and the resulting
rational point $x$ satisfies $\|x-p\|^2<n\cdot(\varepsilon^2/n)=\varepsilon^2$.

**The space $\mathbb{R}^n$ is second countable.** Take as candidate basis

$$
\mathcal{B}=\big\{B_q(x)\ :\ x\in\mathbb{Q}^n,\ q\in\mathbb{Q},\ q>0\big\},
$$

the balls with rational centre and rational radius. This family is countable, being indexed by
$\mathbb{Q}^n\times\mathbb{Q}^{+}$, a finite product of countable sets.

It is a basis. Let $U$ be open and let $p$ be any point of $U$. By the definition of the standard
topology there is $r>0$ with $B_r(p)\subseteq U$. Choose a rational $q$ with $0<q<r/2$, which exists
because the rationals are dense, and then a rational point $x$ with $\|x-p\|<q$, which exists because
$\mathbb{Q}^n$ is dense. Two things follow. First $p\in B_q(x)$, directly from $\|x-p\|<q$. Second
$B_q(x)\subseteq B_r(p)$, because any $y\in B_q(x)$ satisfies

$$
\|y-p\|\ \le\ \|y-x\|+\|x-p\|\ <\ q+q\ =\ 2q\ <\ r .
$$

So every point $p$ of $U$ sits inside a member $B_q(x)$ of $\mathcal{B}$ which is itself contained in
$U$, and $U$ is therefore the union of all such members. That is what it means for $\mathcal{B}$ to be
a basis.

**Any subspace of a second countable space is second countable.** Let $\mathcal{B}$ be a countable basis of $M$ and let $A\subseteq M$. The family $$\{B\cap A : B\in\mathcal{B}\}$$ consists of open sets of $A$ and is countable, being indexed by $\mathcal{B}$. It is a basis: any open set of $A$ has the form $U\cap A$ with $U$ open in $M$, and writing $U=\bigcup_i B_i$ as a union of basis elements gives $$U\cap A=\bigcup_i(B_i\cap A)$$, a union of members of the new family.

Applying this to $S^2$ inside $\mathbb{R}^3$ gives the result. Concretely, the beams centred on
directions with rational coordinates and having rational angular radii already generate the whole
topology of the sky.

</details>


The remaining two properties are not inherited from the ambient space in the cheap way above; they are
properly characteristic of the sphere.

**Definition.** An **open cover** of a space $M$ is a collection of open sets whose union is all of $M$.
A **subcover** is a subcollection which still covers $M$. The space is **compact** if every open cover
of it admits a *finite* subcover.

This definition looks arbitrary the first time one meets it, so it is worth saying plainly what it is
for. Three readings help.

**Compact means "finite, as far as topology can tell".** Nearly every statement that is trivially true
for a finite set remains true for a compact one, and fails in general otherwise. A finite set of real
numbers has a largest element; so does a compact one. A finite set is bounded; so is a compact one. A
continuous function on a finite set is bounded and attains its bounds; on a compact set it still does.
Compactness is the topological surrogate for finiteness.

**It is a machine for turning local statements into global ones.** This is the deeper reading. Most
properties in analysis are local: at each point there is *some* $\delta$, *some* neighbourhood, *some*
bound. To make a statement about the whole space you would like to take the smallest of those
$\delta$'s — and an infinite family of strictly positive numbers can perfectly well have infimum zero,
which ruins the argument. A *finite* family cannot: its minimum is one of its members, hence strictly
positive. That single observation is the reason the definition insists on a finite subcover. The
textbook illustration is that on a compact space continuity upgrades to uniform continuity, and the
proof is precisely "extract a finite subcover, then take the minimum of finitely many $\delta$'s".

**The two ways it fails are the two ways a space can be defective.** Cover $\mathbb{R}$ by the intervals
$(-n,n)$ for $n=1,2,3,\dots$; no finite subfamily covers it, because any finite collection has a largest
$n$ and leaves everything beyond it uncovered. The space escapes to infinity. Now cover the half-open
interval $(0,1]$ by the intervals $(1/n,2)$; again no finite subfamily works, for the same reason, and
this time the space is running into a missing edge at $0$. So compactness says: nowhere to run away to,
and no absent boundary. For the sky, you cannot walk off it and it has no rim. Note in passing — this
will matter greatly when we come to masked skies — that removing the Galactic plane as an open set
leaves a sky with exactly the second defect, and destroys compactness.

One may reasonably ask why we do not simply say "closed and bounded", which is the description one
learns first. The reason is that boundedness is not a topological statement at all: it needs a distance,
and it is not preserved by homeomorphism. The map $$t\mapsto t/(1+\vert t\vert)$$ is a homeomorphism from
$\mathbb{R}$ onto $(-1,1)$, so a bounded space and an unbounded one can be topologically identical.
Compactness, phrased purely in terms of open sets, is preserved — and is therefore the honest notion.
The theorem of Heine and Borel then states that in $\mathbb{R}^n$, and only there, compactness happens
to coincide with being closed and bounded. We shall not invoke it; the chain below proves what we need
from scratch, resting only on the least-upper-bound property of the real numbers, which is part of the
definition of $\mathbb{R}$ rather than a theorem about it.

<details markdown="1">
<summary><strong>Proof: a closed interval is compact</strong></summary>

This is the only place where real work happens; everything else is bookkeeping.

Let $\mathcal{U}$ be an open cover of $[a,b]$, and consider

$$
S=\big\{x\in[a,b]\ :\ [a,x]\ \text{is covered by finitely many members of}\ \mathcal{U}\big\}.
$$

The set $S$ is not empty: some $U_0\in\mathcal{U}$ contains $a$, and the single set $U_0$ covers
$[a,a]=\{a\}$, so $a\in S$. It is bounded above by $b$. By the least-upper-bound property of the real
numbers it therefore possesses a supremum $c$, with $a\le c\le b$.

Some member $U\in\mathcal{U}$ contains $c$, since $\mathcal{U}$ covers the interval, and $U$ is open, so
there is $\delta>0$ with $(c-\delta,c+\delta)\cap[a,b]\subseteq U$. Because $c$ is the *least* upper
bound, the number $c-\delta$ is not an upper bound, so there exists $x\in S$ with $x>c-\delta$. Let
$U_1,\dots,U_k$ be a finite subfamily covering $[a,x]$.

Now take any $y\in[a,b]$ with $y<c+\delta$. The finite family $U_1,\dots,U_k,U$ covers $[a,y]$: the part
$[a,x]$ is covered by the first $k$ sets, and the remaining part $[x,y]$ lies inside
$(c-\delta,c+\delta)$, hence inside $U$.

Taking $y=c$ shows that $c$ itself belongs to $S$. And if $c$ were strictly smaller than $b$, taking
$y=\min\{b,\,c+\delta/2\}$, which is strictly larger than $c$, would put a point larger than $c$ into
$S$ — contradicting the fact that $c$ is an upper bound of $S$. Hence $c=b$, and $b\in S$: the whole
interval is covered by finitely many members of $\mathcal{U}$.

</details>

<details markdown="1">
<summary><strong>Proof: a continuous image of a compact space is compact</strong></summary>

Let $f:M\to N$ be continuous and onto, with $M$ compact, and let $\{V_i\}$ be an open cover of $N$.

Each preimage ${\rm Preim}_f(V_i)$ is open in $M$, by the definition of continuity. Together they cover
$M$: any $x\in M$ has $f(x)$ somewhere in $N$, hence in some $V_i$, hence $x\in{\rm Preim}_f(V_i)$.
Compactness of $M$ now supplies finitely many indices $i_1,\dots,i_n$ such that
${\rm Preim}_f(V_{i_1}),\dots,{\rm Preim}_f(V_{i_n})$ already cover $M$.

The corresponding $V_{i_1},\dots,V_{i_n}$ then cover $N$. Indeed, let $y\in N$. Since $f$ is onto there
is $x\in M$ with $f(x)=y$; that $x$ lies in some ${\rm Preim}_f(V_{i_j})$; and therefore
$y=f(x)\in V_{i_j}$.

</details>

<details markdown="1">
<summary><strong>Proof: a rectangle is compact</strong></summary>

Let $R=K\times L$ with $K$ and $L$ compact subsets of $\mathbb{R}$, seen inside $\mathbb{R}^2$ with the
subspace topology.

We first record that the **open boxes**, that is products $A\times B$ of two open intervals, generate the
topology of $\mathbb{R}^2$: every ball $B_r(p)$ contains the box of half-side $r/\sqrt{2}$ centred on
$p$, since a point of that box is at distance at most $\sqrt{2}\cdot r/\sqrt{2}=r$ from $p$; and
conversely every box contains, around each of its points, the ball of radius the distance to the nearest
side. So an open set of $\mathbb{R}^2$ is a union of boxes, and an open set of $R$ is a union of traces
of boxes.

Now let $\mathcal{W}$ be an open cover of $R$, and fix a point $x\in K$. For every $y\in L$ choose a
member of $\mathcal{W}$ containing $(x,y)$, and inside it a box $A_y\times B_y$ with $x\in A_y$ and
$y\in B_y$. The sets $B_y$ form an open cover of $L$, so by compactness of $L$ finitely many of them,
$B_{y_1},\dots,B_{y_m}$, already cover $L$. Set

$$
A^{(x)}=A_{y_1}\cap\dots\cap A_{y_m},
$$

a finite intersection of open sets, hence open, and containing $x$. The whole strip $A^{(x)}\times L$ is
then covered by the $m$ corresponding members of $\mathcal{W}$: any point $(u,v)$ of the strip has
$v\in B_{y_j}$ for some $j$, and $u\in A^{(x)}\subseteq A_{y_j}$, so $(u,v)$ lies in
$A_{y_j}\times B_{y_j}$ and hence in the member of $\mathcal{W}$ that box was chosen inside.

This is the crux, and it is the local-to-global machine at work: compactness of $L$ has converted a
covering that was chosen point by point along the vertical line above $x$ into a covering of a strip of
*uniform* width $A^{(x)}$.

Now let $x$ range over $K$. The sets $A^{(x)}$ form an open cover of $K$, so finitely many of them,
$A^{(x_1)},\dots,A^{(x_p)}$, suffice. Gathering the finite families of members of $\mathcal{W}$ attached
to each of these $p$ strips gives a finite subfamily covering all of $R$.

</details>

<details markdown="1">
<summary><strong>Proof: the sky is compact</strong></summary>

Consider the map

$$
f:[0,\pi]\times[0,2\pi]\longrightarrow\mathbb{R}^3,\qquad
f(\theta,\varphi)=\big(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta\big).
$$

Its three components are built from sines, cosines and products, so $f$ is continuous. Its values lie on
the sphere, since $\sin^2\theta(\cos^2\varphi+\sin^2\varphi)+\cos^2\theta=\sin^2\theta+\cos^2\theta=1$.

It is onto the sphere. Given $(x,y,z)\in S^2$ we have $z^2\le1$, so $\theta=\arccos z$ is a well-defined
element of $[0,\pi]$ and $\cos\theta=z$. Then $x^2+y^2=1-z^2=\sin^2\theta$. If $\sin\theta\neq0$ the pair
$(x,y)/\sin\theta$ has unit length in the plane and therefore equals $(\cos\varphi,\sin\varphi)$ for some
$\varphi\in[0,2\pi]$, giving $f(\theta,\varphi)=(x,y,z)$. If $\sin\theta=0$ the point is one of the two
poles, reached by $\theta=0$ or $\theta=\pi$ with any $\varphi$ whatsoever.

The rectangle $[0,\pi]\times[0,2\pi]$ is compact, being a product of two closed intervals, each compact.
Its continuous image is compact. Hence $S^2$ is compact.

Two remarks. The map $f$ is not a chart: it is not injective, since every $\varphi$ gives the same pole,
and its domain is not open. That does not matter, because compactness travels along any continuous
surjection, chart or not. And notice that the only genuinely non-trivial input in the whole chain was the
least-upper-bound property of the real numbers, used exactly once.

</details>

**Definition.** A space $M$ is **connected** if it cannot be written as the union of two disjoint
non-empty open sets. A splitting $M=U\cup V$ with $U,V$ open, disjoint and both non-empty is called a
*disconnection*.

**Definition.** A space is **path-connected** if any two of its points can be joined by a continuous
curve lying in it.

The intuition is the obvious one: the space is a single piece, and one can travel from anywhere to
anywhere without leaving it. Two directions on the sky are always joined by an arc of great circle.
Again the property is not automatic, and again the masked sky is the cautionary example: a cut removing
a band around the Galactic plane leaves two polar caps with no path between them, and the observed
region is disconnected.

<details markdown="1">
<summary><strong>Proof: the sky is connected</strong></summary>

We show first that a path-connected space is connected, and then that the sphere is path-connected.

**Path-connected implies connected.** Suppose $M$ is path-connected and admits a disconnection
$M=U\cup V$. Pick $p\in U$ and $q\in V$, and a continuous curve $\gamma:[0,1]\to M$ with $\gamma(0)=p$
and $\gamma(1)=q$. Then ${\rm Preim}_\gamma(U)$ and ${\rm Preim}_\gamma(V)$ are open in $[0,1]$ by
continuity, are disjoint because $U$ and $V$ are, are non-empty because they contain $0$ and $1$
respectively, and their union is all of $[0,1]$ because $U\cup V$ is all of $M$. That is a disconnection
of $[0,1]$, so it suffices to show that the interval admits none.

**The interval $[0,1]$ is connected.** Suppose $[0,1]=U\cup V$ were a disconnection, and say $0\in U$.
Consider

$$
A=\big\{t\in[0,1]\ :\ [0,t]\subseteq U\big\}.
$$

Since $U$ is open and contains $0$, it contains $[0,\delta_0)$ for some $\delta_0>0$, so $A$ is
non-empty; it is bounded above by $1$; let $c$ be its supremum. The point $c$ lies either in $U$ or in
$V$, and we rule out both possibilities except one.

Suppose $c\in V$. Since $V$ is open there is $\delta>0$ with $(c-\delta,c+\delta)\cap[0,1]\subseteq V$.
As $c$ is the least upper bound of $A$, there is $t\in A$ with $t>c-\delta$. That $t$ satisfies
$[0,t]\subseteq U$, so in particular $t\in U$; but $t$ also lies in $(c-\delta,c+\delta)$, hence in $V$.
So $t\in U\cap V=\varnothing$, which is absurd.

Therefore $c\in U$. Since $U$ is open there is $\delta>0$ with $(c-\delta,c+\delta)\cap[0,1]\subseteq U$,
and there is $t\in A$ with $t>c-\delta$. Then $[0,t]\subseteq U$ and $[t,y]\subseteq U$ for every
$y\in[0,1]$ with $y<c+\delta$, so $[0,y]\subseteq U$ and $y\in A$. If $c$ were strictly less than $1$,
choosing $y=\min\{1,\,c+\delta/2\}>c$ would place a point above $c$ in $A$, contradicting that $c$ is an
upper bound. Hence $c=1$, and taking $y=1$ gives $[0,1]\subseteq U$, so $V$ is empty — contradicting the
assumption that the splitting was a disconnection.

**The sphere is path-connected.** Let $p\neq q$ be two directions. If $q\neq-p$, write
$q=\alpha p+\beta w$ with $w$ a unit vector perpendicular to $p$, and let $\Delta=\arccos(p\cdot q)$; the
curve $\gamma(t)=\cos(t\Delta)\,p+\sin(t\Delta)\,w$ for $t\in[0,1]$ has unit length at all times, since
$p$ and $w$ are perpendicular unit vectors, so it lies on the sphere, and it joins $p$ to $q$. Its
components are continuous functions of $t$, hence it is continuous. If $q=-p$, join them through any
third direction in two such steps.

Notice the structure of the argument: a question about the sphere was transported back to a question
about the interval, where the least-upper-bound property of the real numbers settled it. That is the same
manoeuvre used for compactness, and we shall use it again.

</details>

None of the above properties is idle. Hausdorff and second countability are, word for word, the two
conditions appearing in the definition of a manifold, which we come to next. They are there to exclude
pathologies such as the line with two origins, locally indistinguishable from $\mathbb{R}$ and yet
without unique limits, and such as the discrete sky, whose topology is too fine to be built from any
countable list of observations.

Compactness and connectedness will both be used immediately afterwards, in the proof that the sky cannot
be covered by a single coordinate system. Compactness will then return much later in a wholly different
guise: it is the reason the multipole index $\ell$ takes discrete values, so that the CMB possesses a
spectrum of separate multipoles rather than a continuum of wavenumbers. And when we finally come to
observing only part of the sky, it is exactly compactness and connectedness that a mask destroys.

### The sky as a smooth manifold 

Topology gave us continuity, and that is already something: we can say that the track of a planet
across the sky does not jump. It does not give us differentiation. Nothing so far allows us to speak of the gradient of the CMB temperature, of the velocity of a curve, or of a smooth field of
polarisation directions. And differentiation is not a notion a topology can supply, because
differentiating means comparing a function at nearby points and dividing by their separation — and a topology has no clear notion of separation.

The way out is not to invent differentiation from scratch but to **import it from $\mathbb{R}^n$**, where we already have it, patch by patch. Let's start with a few definitions:

- A map $f:M\to N$ between topological spaces is a **homeomorphism** if it is a continuous bijection whose inverse $f^{-1}$ is also continuous. Two spaces related by a homeomorphism have literally the same open sets, relabelled; they are the same topological space.

- A **chart** on a topological space $M$ is a pair $(U,x)$ where $U\subseteq M$ is open and $x:U\to x(U)\subseteq\mathbb{R}^n$ is a homeomorphism onto an open subset of
$\mathbb{R}^n$. The map $x$ is called a **coordinate function**. A chart is a *local coordinate system*: it attaches $n$ real numbers to each point of $U$, continuously and without ambiguity.

- An **atlas**  $\mathcal{A}$ on $M$ is a collection of charts whose domains cover $M$, so that
every point of $M$ has at least one coordinate system available around it. i.e. $$\mathcal{A} = \{(U_\alpha,x_\alpha) \vert \alpha \in A\}$$ such that $$\bigcup_{\alpha\in A}^n U_\alpha = M $$, where $A$ is a finite set of indices.

-  A **topological manifold of dimension $n$** is a topological
space that is Hausdorff, second countable, and admits an atlas of $n$-dimensional charts.

The two point-set conditions are there to exclude pathologies rather than to do positive work.
*Hausdorff* — distinct points have disjoint open neighbourhoods — is what guarantees that a sequence
cannot converge to two different points at once; without it one can build a "line with two origins",
locally identical to $\mathbb{R}$ everywhere yet with no unambiguous limits. *Second countable* — all
open sets are unions taken from one countable family — keeps the space from being unmanageably large,
and is what allows the local constructions to be glued into global ones. Both were inherited by the
sky from $\mathbb{R}^3$ when we gave it the subspace topology, so we have them at no cost.

Where two charts $$(U_1,x_1)$$ and $$(U_2,x_2)$$ overlap, the same point receives two sets of coordinates, and the dictionary between them is the **transition map**

$$
x_2\circ x_1^{-1}\ :\ x_1(U_1\cap U_2)\ \longrightarrow\ x_2(U_1\cap U_2),
$$

a map between two open subsets of $\mathbb{R}^n$ — an object we know perfectly well how to
differentiate. This is the hinge of the whole construction.

**Definition (smooth manifold).** A **smooth manifold of dimension $n$** is a topological manifold of dimension $n$ together with an atlas all of whose transition maps are infinitely differentiable, that is, admit partial derivatives of every order, all continuous.

Nothing has been said about differentiating on $M$ itself; the smoothness requirement is imposed
entirely on maps between pieces of $\mathbb{R}^n$. Its whole purpose is to make the following
definitions consistent.

**Definition (smooth function, smooth curve).** A function $f:M\to\mathbb{R}$ on a smooth manifold is **smooth** if the ordinary function $f\circ x^{-1}$ is smooth on $x(U)\subseteq\mathbb{R}^n$, for every chart $(U,x)$. A curve $\gamma:I\to M$, with $I$ an interval of $\mathbb{R}$, is **smooth** if the ordinary curve $x\circ\gamma$ is smooth for every chart whose domain it meets.

In words: read the object in coordinates, and ask the question you already know how to answer. The danger is obvious — the answer might depend on which coordinates you read it in, in which case the definition would be worthless. It does not, and that is exactly what the transition maps were required to be smooth for.

<details markdown="1">
<summary><strong>Proof: smoothness does not depend on the chart</strong></summary>

Let $(U_1, x_1)$ and $(U_2, x_2)$ be two charts, and suppose $f\circ x_1^{-1}$ is smooth. On the
part of $\mathbb{R}^n$ corresponding to the overlap we may write

$$
f\circ  x_2^{-1}=\big(f\circ x_1^{-1}\big)\circ\big( x_1\circ  x_2^{-1}\big),
$$

since $ x_1^{-1}\circ x_1$ is the identity on $U_1\cap U_2$. The right-hand side is a composition
of two maps between open subsets of Euclidean spaces: the first is smooth by hypothesis, the second is
a transition map and is smooth by the definition of a smooth manifold. A composition of smooth maps is
smooth, by the chain rule, so $f\circ  x_2^{-1}$ is smooth as well.

The same manipulation works for curves, in the other order:

$$
  x_2\circ\gamma=\big(  x_2\circ x_1^{-1}\big)\circ\big( x_1\circ\gamma\big).
$$

Notice what would go wrong with a merely topological manifold. The transition maps would then only be
homeomorphisms, and a homeomorphism can be very rough — $u\mapsto u^{1/3}$ is one on $\mathbb{R}$ —
so a function smooth in one chart could be non-differentiable in another, and the word "smooth" would
refer to the chart rather than to the manifold.

</details>

#### A single chart cannot cover the sphere

We now exhibit an atlas for the sky, and then show that no smaller one exists.

The two charts we use are the **stereographic projections**. Place the sphere in $\mathbb{R}^3$ and
take the north pole $N=(0,0,1)$. For any point $p\neq N$ of the sphere, the straight line through $N$
and $p$ meets the equatorial plane $z=0$ at exactly one point, and that point is $\sigma_N(p)$.
Parametrising the line as $N+t\,(p-N)$ and asking for the vanishing of its third component gives
$t=1/(1-z)$, hence

$$
\sigma_N(x,y,z)=\Big(\frac{x}{1-z},\ \frac{y}{1-z}\Big),
\qquad
\sigma_S(x,y,z)=\Big(\frac{x}{1+z},\ \frac{y}{1+z}\Big),
$$

the second being the same construction from the south pole $S=(0,0,-1)$. Each is defined on the sphere
minus one point, each maps onto the whole plane, and each is a homeomorphism, with inverse

$$
\sigma_N^{-1}(u,v)=\frac{1}{1+u^2+v^2}\big(2u,\ 2v,\ u^2+v^2-1\big).
$$

Together their domains cover $S^2$, since the two missing points are different. So the sky is a
topological manifold of dimension two, and the two numbers we were promised at the very beginning are
now legitimately in hand.

<details markdown="1">
<summary><strong>Computation: the transition map, and why the sphere is a smooth manifold</strong></summary>

Write $r^2=u^2+v^2$. From the expression for $\sigma_N^{-1}$ we read
$z=(r^2-1)/(r^2+1)$, hence $1+z=2r^2/(r^2+1)$, and therefore

$$
\frac{x}{1+z}=\frac{2u}{1+r^2}\cdot\frac{r^2+1}{2r^2}=\frac{u}{r^2},
$$

and likewise for the second component. The transition map is thus

$$
\sigma_S\circ\sigma_N^{-1}(u,v)=\Big(\frac{u}{u^2+v^2},\ \frac{v}{u^2+v^2}\Big),
$$

the inversion in the unit circle. It is defined on $\mathbb{R}^2\setminus\{(0,0)\}$ — the point
removed being the image of the south pole, which the first chart covers and the second does not — and
on that set the denominator never vanishes, so both components are quotients of polynomials with
non-vanishing denominator, hence infinitely differentiable. The same holds for the inverse transition,
which is the very same map.

The atlas is therefore smooth, and

$$
\boxed{\ S^2 \text{ is a smooth manifold of dimension } 2 .\ }
$$

Identifying $\mathbb{R}^2$ with the complex plane through $\zeta=u+iv$, the transition map reads
$$\zeta\mapsto \zeta/\vert\zeta\vert^2=1/\bar\zeta$$. Composing $\sigma_S$ with the reflection
$(u,v)\mapsto(u,-v)$ turns it into the holomorphic $\zeta\mapsto1/\zeta$; that second convention is the
one that makes the sphere a complex manifold, the Riemann sphere, and it is the form in which we shall
meet it again when we look at aberration.

</details>

Two charts suffice. One does not, and this is not a failure of ingenuity.

**Theorem.** There is no single chart covering all of $S^2$.

<details markdown="1">
<summary><strong>Proof</strong></summary>

Suppose there were one, a homeomorphism $x:S^2\to U$ onto an open set $U\subseteq\mathbb{R}^2$.

The sphere is compact, and a continuous image of a compact space is compact, so $U$ is compact. A
compact subset of $\mathbb{R}^2$ is closed, so $U$ is at once open and closed in $\mathbb{R}^2$. But
$\mathbb{R}^2$ is connected, and its only subsets that are simultaneously open and closed are
$\varnothing$ and $\mathbb{R}^2$ itself; as $U$ is not empty, $U=\mathbb{R}^2$. And $\mathbb{R}^2$ is
not compact, which contradicts the first sentence.

The argument used only two of the properties we collected when giving the sky its topology, and
nothing about spheres in particular: it rules out a single chart on any compact space.

</details>

This is a lesson we shall invoke constantly. **There is no global coordinate system on the sky.** Any
set of numbers attached to a direction — and, much later, this will include the Stokes parameters $Q$
and $U$ — is attached relative to a chart, and is local by construction. It is the sharp form of the
sign ambiguity we met when trying to label the sphere by $x$ and $y$ alone.

For explicit computations we shall nevertheless not use the stereographic charts but the familiar
**spherical coordinates**,

$$
x(\theta,\varphi)=\big(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta\big),
\qquad \theta\in(0,\pi),\ \varphi\in(0,2\pi).
$$

Strictly this is the *inverse* of a chart: it takes coordinates and returns a point, whereas a chart
goes the other way. Its domain is the sphere with one meridian and both poles removed, so it is a
perfectly legitimate chart of a genuinely smaller region — and by the theorem just proved, no honest
choice could have done better.

#### Tangent vectors

Two things force us to introduce vectors. The first is the physics: polarisation is a direction
*along the sky, at a point of the sky*, so we need, at each direction of observation, a plane of
"directions along the sky there". We will come back to this later. The second is that a metric, which is what we are building towards, measures vectors — it has nothing else to act on. So defining what a "length" and an "orientation" are, which are the content of the metric, requires first to define what vectors are.

A vector at a point of the sphere cannot be an arbitrary arrow of $\mathbb{R}^3$: an arrow sticking radially outwards does not point *along* the sky. The right notion comes from motion. Let $\gamma$ be a smooth curve drawn on the sphere, that is a smooth map
$\gamma:[0,1]\to S^2\subset\mathbb{R}^3$ with $\gamma(0)=p$. Because $\gamma$
takes its values in $\mathbb{R}^3$, its velocity $\dot\gamma(0)$ is an ordinary vector of
$\mathbb{R}^3$, and it is by construction a direction in which one can travel while staying on the sphere. Collecting all of them gives the object we want.

The **tangent plane** to the sphere at $p$ is the set of velocities at $p$ of curves drawn on the sphere,

$$
T_pS^2=\big\{\dot\gamma(0) \;:\; \gamma \text{ a smooth curve on } S^2 \text{ with } \gamma(0)=p\big\}.
$$

<details markdown="1">
<summary><strong>Proof: the tangent plane is the plane perpendicular to $p$</strong></summary>

We show that $T_pS^2=\{v\in\mathbb{R}^3 : v\cdot p=0\}$, and in particular that it is a
two-dimensional vector space.

Take any curve $\gamma$ on the sphere through $p$. Lying on the sphere means
$\gamma(t)\cdot\gamma(t)=1$ for every $t$. Differentiating this identity at $t=0$ and using the
product rule gives $2\,\dot\gamma(0)\cdot\gamma(0)=0$, that is $\dot\gamma(0)\cdot p=0$. So every
velocity is perpendicular to $p$.

Conversely, let $v$ be any vector with $v\cdot p=0$. If $v=0$, take the constant curve. Otherwise set
$u=v/\|v\|$ and consider

$$
\gamma(t)=\cos\big(\|v\|t\big)\,p+\sin\big(\|v\|t\big)\,u ,
$$

the great circle through $p$ in the direction $u$. Since $p$ and $u$ are perpendicular unit vectors,
$$\gamma(t)\cdot\gamma(t)=\cos^2+\sin^2=1$$, so the curve lies on the sphere; it passes through $p$ at
$t=0$; and its velocity there is $$\dot\gamma(0)=\|v\|\,u=v$$. So every perpendicular vector is a
velocity.

The two inclusions give the equality. The set $$\{v : v\cdot p=0\}$$ is the solution set of one linear
equation in $\mathbb{R}^3$, hence a plane through the origin, of dimension two.

</details>

The tangent space at $p$ forms a vector space. A **vector space** is ...

<details markdown="1">
<summary><strong>Proof</strong></summary>

</details>

A basis of the vector space is given by differential operators.

In the spherical chart we can produce a basis of each tangent plane. Letting $\theta$ increase with
$\varphi$ held fixed traces a curve on the sphere, whose velocity is a tangent vector, and likewise
for $\varphi$. Differentiating $x(\theta,\varphi)$,

$$
\mathbf{e}_\theta(x) \equiv \partial_\theta x=\big(\cos\theta\cos\varphi,\ \cos\theta\sin\varphi,\ -\sin\theta\big),
$$

$$
\mathbf{e}_\varphi(x) \equiv \partial_\varphi x=\big(-\sin\theta\sin\varphi,\ \sin\theta\cos\varphi,\ 0\big).
$$

These are linearly independent wherever $\sin\theta\neq0$, so they form a basis of $T_pS^2$ there, and
every tangent vector can be written $$v=v^\theta\mathbf{e}_\theta+v^\varphi\mathbf{e}_\varphi$$. The two
numbers $(v^\theta,v^\varphi)$ are the **components of $v$ in this chart**, and they mean nothing
outside it.

Finally, a **vector field** on the sphere is a choice of tangent vector at every point, varying
continuously: a field of little arrows drawn flat on the sphere. One theorem about them will be used
repeatedly.

**Theorem (you cannot comb a hairy ball).** Every continuous vector field on $S^2$ vanishes at at
least one point.

This is a topological obstruction, of the same nature as the impossibility of covering the sphere with
a single chart, and no cleverness evades it. The standard proof counts the zeros of a vector field with
signs and shows the total to be a topological invariant of the surface, equal to two for the sphere and
zero for the torus, which *can* be combed; a short self-contained proof is in Milnor, *Topology from the
Differentiable Viewpoint*. The consequence we shall need is that a **frame** — a pair of vector fields
that are everywhere perpendicular and of unit length, a choice of local axes on the sky — cannot exist
globally, since it is in particular a pair of nowhere-vanishing vector fields.

### The sky as a Riemannian manifold

#### Defining a Riemannian metric

We now need to measure. So far we can say that a track across the sky is continuous, that a field on its smooth, and which way a vector points at each direction — but nothing yet lets us say that two stars are three degrees apart, that one patch of sky is larger than another, or that two polarisation directions are perpendicular. Supplying all of this at once is the job of a single object.

It is worth noticing in advance that this is the first layer which is not forced upon us. The set, the topology, the smooth structure and the tangent planes each followed from the one before with no choice to make. The metric will not: we shall have to choose it, and the next section shows that the choice belongs to the observer.

A **Riemannian metric** $g$ assigns to each point $p$ an inner
product on the tangent plane, that is a map $g_p:T_pM\times T_pM\to\mathbb{R}$ which is
 - **bilinear**: linear in each argument separately;
 - **symmetric**: $g_p(v,w)=g_p(w,v)$;
 - **positive definite**: $g_p(v,v)>0$ for every $v\neq0$;

and which varies smoothly with $p$. The pair $(M,g)$ is a **Riemannian manifold**.

From it come the three quantities an astronomer measures. The **length** of a tangent vector is
$$\|v\|=\sqrt{g_p(v,v)}$$. The **angle** $\alpha$ between two tangent vectors at the same point is given by $$\cos\alpha=g_p(v,w)/(\|v\|\|w\|)$$. The **length of a curve** is
$$L(\gamma)=\int \vert\dot\gamma(t)\vert,\mathrm{d}t$$, and the **distance** between two points is the smallest length of a curve joining them — on the sphere, the great-circle arc.

#### The metric depends on the observer!

Here comes a huge subtlety before defining a metric: it depends on the observer, and precisely on its velocity. **Now, what is an observer?**
An **event** is a point of spacetime: a place *and* a moment, "here, now". An **observer** is not just a place; it is something with a **state of motion**, a history drawn in spacetime as a curve called a *worldline*. At a given event the observer is characterised by the direction its worldline is heading in spacetime, a unit vector called the **four-velocity** $u$ — in plain words, how fast and in which direction it is moving. Crucially, **two different observers can sit at the same event**: picture yourself on the pavement and a rocket flying past at half the speed of light, at the precise instant you cross. Same place, same moment, same event; different states of motion.

**So "fixing an observer" means "choosing a state of motion", nothing else.** Where and when are
already fixed; what remains free is the velocity. It matters because each observer carries their own notion of "space right now", defined relative to their own worldline — and each uses their own to
measure the angle between two stars.

**Aberration.** You have met the classical version. Walk through vertically falling rain: it seems to
come from in front of you, and tilts further forward the faster you walk. The rain has not changed;
what changed is that "apparent direction" is a statement made in *your* frame.

Light does the same. If an observer at rest sees a star at angle $\theta$ from some axis and you move
along that axis with speed $\beta=v/c$, you see the same star at $\theta'$ with

$$
\cos\theta' \;=\; \frac{\cos\theta+\beta}{1+\beta\cos\theta}\ ,
$$

and $\theta'<\theta$: the star has moved *towards* your direction of motion. As $\beta\to1$ the whole sky crowds into a small patch straight ahead.

<details markdown="1">
<summary><strong>Proof</strong></summary>

Let $S$ be the frame of the observer at rest and $S'$ that of the moving observer, travelling with
speed $\beta$ along the $x$-axis. Write $\hat n$ for the direction in which the telescope is
*pointed*, so that the photon travels along $-\hat n$, and let $\theta$ be the angle between $\hat n$
and the $x$-axis. A photon of energy $E$ then has four-momentum

$$
k^\mu=E\big(1,\ -\cos\theta,\ -\sin\theta,\ 0\big)
$$

in $S$, the minus signs recording that it moves opposite to the pointing direction. The Lorentz boost
to $S'$ acts on the first two components as

$$
E'=\gamma\big(E-\beta k^x\big),\qquad k'^x=\gamma\big(k^x-\beta E\big),
\qquad \gamma=(1-\beta^2)^{-1/2},
$$

so that, substituting $k^x=-E\cos\theta$,

$$
E'=\gamma E\big(1+\beta\cos\theta\big),
\qquad
k'^x=-\gamma E\big(\cos\theta+\beta\big).
$$

In $S'$ the same photon is described by $k'^\mu=E'(1,-\cos\theta',-\sin\theta',0)$, so
$k'^x=-E'\cos\theta'$. Equating the two expressions and dividing by $E'$,

$$
\cos\theta'=\frac{\gamma E(\cos\theta+\beta)}{\gamma E(1+\beta\cos\theta)}
=\frac{\cos\theta+\beta}{1+\beta\cos\theta}.
$$

That the star moves forward follows from

$$
\cos\theta'-\cos\theta=\frac{(\cos\theta+\beta)-\cos\theta(1+\beta\cos\theta)}{1+\beta\cos\theta}
=\frac{\beta\sin^2\theta}{1+\beta\cos\theta}>0
$$

for $0<\theta<\pi$ and $\beta>0$: the cosine increases, hence the angle decreases.

Two by-products will be used below. Taking $1-\cos\theta'$ and $1+\cos\theta'$ from the formula, both
acquire the same denominator $1+\beta\cos\theta$, which cancels in their ratio, and the half-angle
identity $\tan^2(\theta/2)=(1-\cos\theta)/(1+\cos\theta)$ turns the whole relation into the far simpler

$$
\tan\frac{\theta'}{2}=k\,\tan\frac{\theta}{2},\qquad k=\sqrt{\frac{1-\beta}{1+\beta}} .
$$

And subtracting $\cos^2\theta'$ from one gives, after the same cancellation,

$$
\sin\theta'=\frac{\sin\theta}{\gamma\,(1+\beta\cos\theta)} .
$$

</details>

**What changes and what does not.** Two observers at the same event agree on which directions exist,
and even on which sphere they live. They disagree on the angles between them.

| Structure | Observer-dependent? |
|---|---|
| the set of directions | no |
| the topology | no — aberration is a homeomorphism |
| the smooth structure | no — aberration is smooth, with smooth inverse |
| the tangent planes | no |
| **the metric $g$** | **yes** |

$$
\boxed{\ \text{There is no canonical metric on the sky until an observer has been named.}\ }
$$

This is the sharpest form of "a topology forgets distances", and it is why every layer before the
metric could be built without ever mentioning who is looking.

**What survives: angles at a crossing.** Aberration is not an arbitrary scrambling. Draw two curves on
the sky — two satellite tracks — crossing at a point. Aberration moves the crossing point and
stretches the picture around it, but **the angle at which the two curves cross is unchanged**: angles
between vectors *within one tangent plane* are preserved, even though distances across the sphere are
not.

<details markdown="1">
<summary><strong>Proof</strong></summary>

Aberration leaves the azimuth untouched and sends $\theta$ to $\theta'=f(\theta)$, so as a map of the
sphere it is $(\theta,\varphi)\mapsto(f(\theta),\varphi)$. The moving observer measures with the round
metric of *their* sky, $\mathrm{d}\theta'^2+\sin^2\theta'\,\mathrm{d}\varphi'^2$. Expressing that in
terms of our coordinates, with $\mathrm{d}\theta'=f'(\theta)\,\mathrm{d}\theta$ and
$\mathrm{d}\varphi'=\mathrm{d}\varphi$, gives the metric they impose on our sky,

$$
\tilde g = f'(\theta)^2\,\mathrm{d}\theta^2+\sin^2 f(\theta)\,\mathrm{d}\varphi^2 .
$$

This is a rescaling of $g=\mathrm{d}\theta^2+\sin^2\theta\,\mathrm{d}\varphi^2$ by a single function,
rather than a genuine distortion, exactly when the two coefficients are rescaled by the same amount,
that is when

$$
f'(\theta)=\frac{\sin f(\theta)}{\sin\theta}.
$$

Check it on the half-angle form $\tan(f/2)=k\tan(\theta/2)$ obtained above. Differentiating both sides,
$\tfrac12\sec^2(f/2)\,f'=\tfrac{k}{2}\sec^2(\theta/2)$, so
$f'=k\cos^2(f/2)/\cos^2(\theta/2)$. On the other hand, using $\sin u=2\sin(u/2)\cos(u/2)$ twice,

$$
\frac{\sin f}{\sin\theta}
=\frac{\tan(f/2)}{\tan(\theta/2)}\cdot\frac{\cos^2(f/2)}{\cos^2(\theta/2)}
=k\,\frac{\cos^2(f/2)}{\cos^2(\theta/2)} ,
$$

which is the same thing. Hence $\tilde g=A^2 g$ with

$$
A=\frac{\sin\theta'}{\sin\theta}=\frac{1}{\gamma\,(1+\beta\cos\theta)} ,
$$

the last equality being the second by-product of the previous box.

Angles survive such a rescaling because they are ratios. For two tangent vectors at the same point,

$$
\cos\tilde\alpha=\frac{\tilde g(v,w)}{\sqrt{\tilde g(v,v)}\sqrt{\tilde g(w,w)}}
=\frac{A^2\,g(v,w)}{A\sqrt{g(v,v)}\;A\sqrt{g(w,w)}}=\cos\alpha ,
$$

the factor cancelling between numerator and denominator. Lengths, which involve $A$ once and not twice,
do not survive.

One remark, because it is more than a curiosity. The boost computation gave
$E'=\gamma E(1+\beta\cos\theta)$, so the conformal factor is exactly $A=E/E'$: the rescaling of the sky
and the Doppler shift of the light are one and the same number, inverted. Aberration and the dipole
below are not two effects but one, looked at twice.

</details>

A map with this property is called **conformal**. A Mercator projection of the Earth is conformal:
Greenland's rivers meet its coastline at the correct angles, even though Greenland's size is wildly
wrong. In terms of the metric, a conformal change is $g_{\mu\nu}\mapsto A^2g_{\mu\nu}$ for a positive function $A$: all
lengths at a point are rescaled by the same factor, so ratios of lengths, hence angles, survive. The
same transformation appears in [modified gravity](../modified_gravity/mod_grav.md); there it rescales
lengths in spacetime, here it rescales lengths on the sky, which are angles between objects.

#### The Moebius group and the Lorentz group

## Functions on the sky

### Functions

### Spherical harmonics and SO(3)

## Fields on the sky

### Vector fields on the sky

Connections 

### Tensor fields on the sky

## The Hodge theorem

### For vector fields

### For tensor fields

### For any tensor and form

Use Hodge star, differential and co-differential 

## Received power and polarisation

### E modes B modes


### Further reading and watching

- [F.P. Schuller - Winter school on gravity and light]
- [Nakahara ]
- [Frankel ]
- [Coqueraux ]
