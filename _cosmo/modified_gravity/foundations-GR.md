---
layout: default
title: Foundations of general relativity
parent: cosmo
---

# What to modify? Foundations of general relativity

If we want to study modified gravity, we must first understand what is there to modify. Our best description of gravity so far is given by general relativity (GR). As we will further see, GR is at the heart of modern cosmology. From its formulation in 1915 to the first direct detection of gravitational waves a century later, it has proven to be a remarkably successful theory, with applications ranging from solar system dynamics to the large-scale structure of the universe. At its core lies a beautiful geometric picture: spacetime curvature governs the motion of matter, and matter in turn shapes the curvature of spacetime.
As we will see however, despite its beauty, GR is only one of many possible theories of gravity, and some alternatives might be preferred either from theoretical grounds, or forced on us by future experiments. 
Let us try to unpack the conceptual foundations of GR and try to identify a minimal set of axioms at its base. These axioms will be the natural candidates to drop if we want to look for alternative theories of gravitation beyond general relativity. 

## Some conceptual motivations for GR

Before stating a list of fundamental axioms of general relativity, we must first review some of the conceptual and experimental motivations for this theory that lead to the geometrisation of space-time. 

### What to ask of a gravity theory?

Before getting too technical, let's first list some simple and intuitive requirements that we should ask to a theory that pretend to describe gravity. These are inspired from the so-called "Dicke framework" discussed in [Will (2018)](https://www.cambridge.org/core/books/theory-and-experiment-in-gravitational-physics/8A5923C93E43FAFDEC17C3E0FD01A623).
Let's then say that gravitation, at minimum, should be described in our theory as:

- A **long range** force.
- It should act between **masses**.
- It should be **attractive**.
- It should reproduce **Newton law of gravitation** under some suitable limits:

  $$\boxed{V_{\rm int}(r) = -\frac{G m_1m_2}{r}}$$

  where $G$ is the so-called **Newton gravitational constant**, measured to be $G=6.674300(15) \times 10^{-11}$ m$^{3}$kg$^{−1}$⋅s$^{−2}$ (Value from [Codata 2022](https://physics.nist.gov/cgi-bin/cuu/Value?bg)).
- it should reproduce **special relativity** when turned off.
- It should be **self-consistent** (one should not lead to two contradictory statements or predictions from the same principles).

Newtonian mechanics does not fulfill all these criteria, simply because it does not reproduce special relativity when gravitation is turned off.
GR is one of the theories that satisfy all these criteria, but as we will see, it is not the only one.

### The Einstein equivalence principle

On top of the previous requirements, we can ask that gravity should not only act between masses, but that it should act **universally** between them, that is, it should induce a motion on all massive objects, independently of the value of their mass. Such an additional constraint is forced on us by experiment, and can be promoted to a principle as we will discuss now. Actually, at least three different principles can be built out of this universality statement, known as "equivalence principles".

An equivalence principle is a building block of a theory (principle are like "axioms" in mathematics, they can not be proven and the whole theory is built on them) stating the equivalence between two apparently different concepts or physical situations.

First, let's start with a well known experimental fact, which represent the main motivation for the introduction of equivalence principles:

- **Universality of free-fall (UFF)**: as far as our measurements can go, we witness that all free test bodies fall identically in a gravitational field, independently of their shape, state or composition. 

Every word is important in this statement:
By **test particle** here, we mean a particle small and light enough such that its own gravitational field can be neglected, as well as tidal forces which could be applied to it. By **free** we mean that no other force than gravity is applied on the test body. By **state** here, we mean any possible self-motion, like spinning on itself or properties as electric charge.

We will discuss in another lecture how this empirical fact can be verified up to a very high accuracy using a great variety of experiments.

If we accept that the UFF is exactly true, and we decide to make it a principle to construct a theory, we introduce the

- **Weak equivalence principle (WEP):** UFF is always satisfied.

While UFF and WEP are sometimes conflated, we create here a distinction between the UFF as an experimental fact, and the WEP as a principle.

If we use the WEP in the context of Newtonian theory, we can assert the equivalence between the inertial mass (appearing in $\sum_i\vec{F}=m_i\vec{a}$) and the gravitational mass (appearing in the weight $\vec{P}=m_g\vec{g}$) . This equivalence of concept translates into a mathematical equality $m_i=m_g$, such that the second law for a free-falling body gives exactly $\vec{a}=\vec{g}$ for any body, no matter its composition.

The WEP can be extended with other principles in order to build the so-called **Einstein equivalence principle (EEP)**, which is a useful extension for relativistic theories. The EEP is composed of three different assertions:

1. **Weak equivalence principle (WEP)** is valid.
2. **Local position invariance (LPI):** The outcome of any local non-gravitational experiment is independent of where and when in the Universe it is performed. As such, there is no "preferred" event in space-time in which laws of physics would be different.
2. **Local Lorentz invariance (LLI):** the outcome of any local non-gravitational experiment (i.e. any "small scale" experiment in an inertial/free falling frame) is independent of the velocity of the reference frame in which it is performed. Thus, inertial frames are all equivalent. 

It can be shown that the EEP implies the local equivalence of an accelerated frame upward and a frame at rest in a gravitational field. Furthermore, it implies the local equivalence of a free-fall frame with an inertial frame of special relativity. This is one of the well known intuition that lead Einstein to formulate general relativity, by asserting that gravity is some kind of "inertial force".

The emphasis on "local non-gravitational experiment" in the definition of LPI and LLI might seem cumbersome, but it is actually necessary. Dropping it would lead to a stronger principle, known as the strong equivalence principle (which we will discuss below).

The three "sub-principles" of the EEP are related through **Schiff's conjecture** which is the hypothesis that any self-consistent theory of gravity that embodies WEP necessarily embodies LPI and LLI and thus the full EEP (See [Schiff 1960](https://einstein.stanford.edu/content/sci_papers/papers/Schiff-Expt_Tests_GR-AJP-1960.pdf) and [Cooley 1982](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.49.853)). So far, it as not been proven.
[Ni 2015](https://arxiv.org/abs/1512.08426).

<!-- <details markdown="1">
  <summary><strong>Discussion of Schiff's conjecture</strong></summary>

</details> -->

### General covariance, diffeomorphisms and relativity principle

One of the motivation often invoked for general relativity, is the desire to generalize the results of special relativity not only to inertial frames, but to any possible frames, and especially to accelerated frames. 

Indeed, the ambition of special relativity was already to treat all inertial frames, that is all frames related to one another by linear motion at constant velocity, as equivalent. 

- **relativity principle**: The laws of physics should be independent of the frames in which they are formulated.

The relativity principle applied to inertial frames lead to the conclusion that the speed of light must be the same in all frames, such that it is impossible to say whether or not we are in **absolute motion**. Furthermore, it lead to the conclusion that space and time should be merged into a single realm: space-time equipped with an invariant length given by the rigid Minkowski metric $\eta$ which allows to compute the length of any four dimensional vector $v$ as $$\eta(v,v)= -(v^0)^2 + \sum_i (v^i)^2$$.

The big revelation is then that the EEP states the (local) equivalence between gravitational frames and accelerated motions, and as such, a theory that can handle acceleration, should handle gravity. Furthermore, the EEP allows to identify free-falling frames with the frames of special relativity.

Hence, one would ask for equations -- that is relations between physical quantities -- that remain valid, not only in all inertial frames (as in special relativity) but in all frames, including non-linear and accelerated ones.  

The requirement of general covariance takes a very practical meaning:

- The relevant physical quantities should be expressed by scalars and tensors, such that their relations remain valid in any arbitrary coordination of space-time.

While general covariance was a powerful guide in order historically to build GR, its status of a foundational block is largely contested. It might be that any theory can be rewritten in a way that display general covariance, making it an empty physical requierement. For more discussion on this topic, see for example [Norton 1993](https://sites.pitt.edu/~jdnorton/papers/decades.pdf) and [Ryckman 2024](https://plato.stanford.edu/entries/genrel-early/).

General covariance should not be confused with the closely related concept of **diffeomorphism invariance**, which is itself a deep feature of general relativity. It is the invariance of transformations of space-time itself.

## From motivations to axioms

Now, if EEP is true and added on top of our basic requirements for a theory of gravitation, we should be able to interpret gravitation as the motion of bodies on a curved space-time as follows:

- Space-time is endowed with a symmetric metric $g$, that is, at every point there exist a way to compute (four dimensional) "length" of any vectors as well as angles between vectors. As such $g$ defines a geometry at each point of space-time.
- The trajectories of freely falling test bodies are geodesics of that metric, that is they are the curves that minimizes (or maximize) the length given by $g$.
- In local freely falling reference frames, which are identified with the **inertial frames** of special-relativity, the non-gravitational laws of physics are those of special relativity. As such, in these frames the metric $g$ must be $\eta$.

Every theory of gravity, which satisfy EEP and which can thus be interpreted geometrically as such, are called the
**metric theory of gravity**. As we will see, GR is only one of many metric theories of gravity.

## A set of axioms for general relativity

### Structure:

So, if GR is only one possible theory of gravity, and even more, one of the restricted classes of **metric theory** of gravity, what makes it so special?
Let us try to introduce a list of "axioms" which would be sufficient to uniquely define general relativity.

- (S1): Space-time is a smooth **four dimensional manifold** $M$.
- (S2): $M$ is equipped with a **Lorentzian metric tensor** $g$ at each point, allowing to define length and angles of tangent vectors.
- (S3): $M$ is equipped with a **connection** $\Gamma$ defining parallel transport of tangent vectors. $\Gamma$ is assumed to be **metric compatible** (S3a) and **torsion free** (S3b). It can be proved that such a choice leads to a **unique Levi-Civita connection**, which can be fully expressed in terms of the metric $g$ and its coordinate derivatives. All other geometrical objects which could be associated to matter fields (i.e. spinors and tensors) are also transported through generalizations of $\Gamma$.

We will discuss later how these hypothesis encode the EEP. 

<details markdown="1">
  <summary><strong>Complements: useful definitions and reminders</strong></summary>

- A smooth **manifold**:
- A **metric tensor**:
- A **Lorentzian metric**:
- A **connection**:
- **metric compatibility**:
- **torsion free**:
</details>

### Dynamics:

- (D1): Energy is related to geometry, through the **Einstein equation**:
   
    $$\boxed{R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu} - \Lambda g_{\mu\nu}}$$

  where the **Ricci tensor** is the contraction of the Riemann tensor on its first and third indices,

  $$R_{\mu\nu} = R^{\rho}{}_{\mu\rho\nu},$$

  and the **Ricci scalar** is its trace with respect to the metric,

  $$R = g^{\mu\nu} R_{\mu\nu}.$$

  The **Riemann curvature tensor** $R^{\rho}{}_{\sigma\mu\nu}$ associated to the connection $\Gamma$ is defined by

  $$R^{\rho}{}_{\sigma\mu\nu} = \partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} + \Gamma^{\rho}{}_{\mu\lambda}\Gamma^{\lambda}{}_{\nu\sigma} - \Gamma^{\rho}{}_{\nu\lambda}\Gamma^{\lambda}{}_{\mu\sigma}.$$

  For further discussion, it is also convenient to define the left-hand side of the Einstein equation (D1) as the **Einstein tensor**,

  $$G_{\mu\nu} = R_{\mu\nu} - \tfrac{1}{2} R\, g_{\mu\nu}.$$

- (D2): Matter fields obey their special-relativistic field equations in any local inertial frame (minimal coupling). 

D1 and D2 can also be recovered through extremalization of the **Einstein-Hilbert action**:

$$\boxed{S = \int\sqrt{-|g|}\left(\frac{1}{16 \pi G}(R - 2\Lambda) + \mathcal{L}_m(\psi)\right) \text{d}^4x}$$

where $$\vert g \vert$$ is the determinant of the metric $g$ allowing to define the volume form $\sqrt{-\vert g\vert}\text{d}^4x$. This action encodes both Einstein equations (D1) when varying with respect to $g$ and the equation of matter of fields (D2) when varying with respect to $\psi$. 

<details markdown="1">
  <summary><strong>Proof</strong></summary>

The action is stationnary if 

$$\delta S = S(g_{\mu\nu}) - S(g_{\mu\nu}+\delta g_{\mu\nu}) =0$$

We will assume the formula 

$$\delta(\sqrt{-|g|}) = -\frac{1}{2}\sqrt{-|g|}g_{\mu\nu}\delta g^{\mu\nu} $$

$$ \delta(\sqrt{-|g|}R)= \sqrt{-|g|}\left(R_{\mu\nu}-\frac{1}{2}Rg_{\mu\nu}\right)\delta g^{\mu\nu}+ \text{B.C.}$$

the proof of which can be found in most standard textbook on general relativity.

$$T_{\mu\nu} = -\frac{2}{\sqrt{|-g|}}\frac{\delta S_m}{\delta g^{\mu\nu}}$$

</details>

<details markdown="1">
  <summary><strong>A sidenote on the stress-energy tensor</strong></summary>

We defined in the previous derivation the **stress-energy tensor** as:

$$T_{\mu\nu} = -\frac{2}{-\sqrt{|g|}}\frac{\delta S_m}{\delta g^{\mu\nu}}$$

For $g=\eta$ this gives back the stress-energy tensor which is the conserved charge associated to Noether theorem for space-time translation invariance.

For a point particle $T^\mu_{\nu} =\rho u^\mu u_\nu $.

For a perfect fluid, we have $$T^\mu_{\nu} = \text{diag}(-\rho, P,P,P)= (\rho + P)u^\mu u_\nu + Pg^{\mu}_\nu $$. It gives back Navier-Stokes equations.

$$T^\mu_{\nu} = \frac{\partial \mathcal{L}}{\partial (\partial_\mu\psi)} \partial_\nu \psi - \delta^{\mu}_\nu \mathcal{L}$$

</details>

The EEP is also encoded in these axioms as we will see in the next section. 

Natural consequences of D1 and D2:

- The **continuity equation**: $$\nabla_\mu T^{\mu\nu}=0$$, which comes from the reunion of Einstein equations with the Bianchi identity $\nabla_\mu G^{\mu\nu}=0$.
- The **geodesic equation** for a point like particle $u^\mu\nabla_\mu u^\nu=0$. This equation is a special case of the continuity equation for a free (massive or massless) particle with energy momentum $T^{\mu\nu}=\rho u^\mu u^\nu$.

<details markdown="1">
  <summary><strong>Discussion of continuity and geodesic equations</strong></summary>

</details>

## Requierements for a theory of gravity, EEP and GR

First of all, we find that, in the context of general relativity, gravity is as desired, a long range attractive force between masses with $$V(r)=-Gm_1m_2/r$$ in the limit of small velocities. We find back special relativity when gravity is turned of ($g\to \eta$), and it can be shown to be self-consistent. As such all the basic requierements we asked for at the beggining of this class are satisfied by GR!

<details markdown="1">
  <summary><strong>Proof and discussion</strong></summary>

</details>

Furthermore, the EEP is carefully encoded in the axioms we used to build GR.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

## Strong equivalence principle 

Like EEP but includes also gravitational effects, such that "gravity gravitates".

In a sense EEP, tells us that there is a single metric $g$ appearing in the matter action, to which all fields are coupled:

$$S_{m}= \int\sqrt{-|g|}\mathcal{L}_m(\psi,g_{\mu\nu})\text{d}^4x$$

This allows to interpret that all matter fields live and evolve on the same geometry, dictated by $g$.

By excluding the gravitational experiments from the EEP, we are blind to the metric appearing in the action of gravity

$$S_{\rm g} = \int\sqrt{-|g^*|} \frac{R_{*}}{16 \pi G}\text{d}^4x$$

The Strong equivalence principle (SEP) states that the same metric appears in both actions:

$$\boxed{g^*= g}$$

Exploring various theories which violate SEP is an interesting exercise, which we will explore in this class.

A noticeable consequence of the SEP is that Newton's constant $G$ must be the same everywhere in space and time. We will come back to this point in a later lecture.

- Recall that: any theory satisfying the EEP is called a **metric theory of gravitation**. GR is only one of them.
- However, GR is the unique theory satisfying the SEP, which makes it a much more restrictive condition.

# Further reading

- [C.M. Will -The Confrontation between General Relativity and Experiment - 2014 - Living reviews in relativity ](https://blackholes.tecnico.ulisboa.pt/gritting/pdf/gravity_and_general_relativity/Clifford-Will_The-Confrontation-between-General-Relativity-and-Experiment.pdf) 
- [C. M. Will - theory and experiment in gravitational physics - second edition 2018 - Cambridge University Press.](https://www.cambridge.org/core/books/theory-and-experiment-in-gravitational-physics/8A5923C93E43FAFDEC17C3E0FD01A623)
- Caroll - Spacetime and Geometry
- R. M. Wald - general relativity 
- Misner, Thorne, Wheeler - Gravitation