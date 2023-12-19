---
layout: default
title: Kepler laws
parent: Newton
nav_order: 2
---

**PAGE STILL UNDER CONSTRUCTION**

# Kepler laws: cross product and polar coordinates

Our goal here will be to understand and demonstrate the three Kepler laws from Newton laws with an increasing level of complexity. Codes will be provided to help you getting familiar.

## The laws

Kepler laws are three statements allowing to predict the motion of celestial bodies in the case of a two body system with one much larger than the other. A typical case is then given by the motion of a planet around a star. They can be stated as follow:

- **Law 1:** Trajectories of planets are conics (circles, ellipses, parabola or hyperbola) with the star at one of the focci.
- **Law 2:** A line connecting the planet and its star sweeps out equal areas during equal intervals of time. 
- **Law 3:** If the trajectory is an ellipse, the ratio of the period $$T$$ squared and the semi axis $$a$$ cubed is a constant, that is $$T^2/a^3 = \text{cst} = 4\pi^2/(GM) $$. Where the period $$T$$ is the time taken by the planet to realize a full orbit around the star of mass $$M$$ ($$G$$ is the gravitational constant) and $$a$$ is the maximal distance on the ellipse between the star and the planet.

As we will see, these three laws were first deduced from observations by the german astronomer Joannes Kepler, who understood them as fundamental laws of nature. They were then rederived from deeper and more abstract principles by Isaac Newton.

### History : from laws to theorem

Discovered by Joannes Kepler and published between 1609 and 1619 from Tycho Brahe's measurements. Part of the great changes giving birth to modern astronomy with Galileo's observations (1605) and Copernician's revolution.

At the time they were indeed understood as *laws* that is fundamental rules of nature that can not be proven. However, they can be fully derived from geometrical consideration and Newton *laws* of mechanics. Proven in 1687 by Newton.

### Why are they so important ?

Despite several technical complexities, the period $$T$$ (time to realize a full orbit) and semi-axis $$a$$ (star-planet maximal distance) of an orbit can be directly measured. Using the third law, $$ a^3/T^2 \propto M$$, one can hence recover the mass $$M$$ of the star which would be otherwise very difficult to measure.

- Knowing the moon-earth distance and it's period ($$\sim$$ 1 month), it is hence possible to calculate the mass of our planet!
- Kepler laws can be used to infer informations about orbits of exoplanets, that is planets orbiting around stars other than the sun.
- Observing the orbit of stars around our galaxy center allowed us to spot an extremely massive object. This lead to the only possible conclusion that a supermassive blackhole was inhabiting the center of our Milky Way.

## Polar coordinates

<p align="center">
<img src="../images/polar.png" alt="image" width="49%" height="auto">
</p>

As we discussed already, the first thing to do before studying a motion in mechanics, is to define both a *frame* (otherwise motion is meaningless) and a *coordinate system* (otherwise it is impossible to quantify anything).
So far we were only using *cartesian coordinates*, that is, perpendicular and fixed axis $(O,x,y,z)$. Cylindrical/Polar coordinates replace $x$ and $y$ by $r$ and $\theta$.

<img src="../images/polar_pyth.png" alt="image" width="49%" height="auto"><img src="../images/polar_trigo.png" alt="image" width="49%" height="auto">

Using [Pythagorian theorem](extra-maths/right-triangles.md) in the red triangle

$$ r = \sqrt{x^2 + y^2} $$


And from [basic trigonometry](extra-maths/right-triangles.md)

$$ {\rm tan}(\theta) = y/x \Rightarrow \theta = \arctan(y/x) $$

Also from [basic trigonometry](extra-maths/right-triangles.md) in the red triangle

$$\begin{cases} 
x &= r \cos\theta\\
y &= r \sin\theta 
\end{cases}
$$

<p align="center">
<img src="../images/polar_unitvec.png" alt="image" width="49%" height="auto"><img src="../images/unit-vectors.png" alt="image" width="20%" height="auto">
</p>

Similar geometrical considerations can be done with the units vectors by bringing the two frame at the same point (as done on the right part of the figure above). As such, the new unit vectors in term of the cartesian ones as

$$
\begin{cases}
\vec{u_r} & = \cos\theta \vec{u_x} + \sin\theta \vec{u_y}\\  
\vec{u_\theta} &= -\sin\theta \vec{u_x} + \cos\theta \vec{u_y} 
\end{cases}
$$ 

If you can't find these relations immediately, remember to draw right triangles and look for the trigonometric relations.

While cartesian coordinates are fixed, i.e. the units vectors don't change with time: $\dot{\vec{u_x}}=0$ and $\dot{\vec{u_y}}=0$ (We use the notation $\dot{x} = \frac{\text{d}x}{\text{d}t}$), the unit vectors of polar coordinates change with time along the trajectory of the studied object.
Remembering the rule for the derivative of trigonometric functions, we can immediately derive

$$
\begin{cases}
\frac{ \text{d}\vec{u_r}}{\text{d} \theta } &= -\sin\theta \vec{u_x} + \cos\theta \vec{u_y} = \vec{u_\theta}  \\
\frac{ \text{d}\vec{u_\theta}}{\text{d} \theta } &= -\cos\theta \vec{u_x} - \sin\theta \vec{u_y} = - \vec{u_r} 
\end{cases}
$$ 

Such that, with the [chain rule](extra-maths/derivatives.md)

$$ 
\begin{cases}
\dot{u_r} &= \frac{\text{d} \theta}{\text{d} t}\frac{ \text{d}\vec{u_r}}{\text{d} \theta } = \dot{\theta} \vec{u_\theta}\\ 
 \dot{u_\theta} &= \frac{\text{d} \theta}{\text{d} t} \frac{ \text{d}\vec{u_\theta}}{\text{d} \theta } = -\dot{\theta} \vec{u_r}  
\end{cases}
$$ 

Now that we know how to go back and forth between cartesian and polar coordinates, we can look at the relevant quantities for kinematics, that are position, velocity and acceleration.
The position vector is simply given by

$$ \vec{r} = r \vec{u_r} $$

The velocity vector is then given by its derivative

$$ \vec{v} = \dot{\vec{r}} = \dot{r}\vec{u_r} + r \dot{\vec{u_r}} =  \dot{r}\vec{u_r} + r \dot{\theta}\vec{u_\theta} $$

And we need to derive another time to get the acceleration vector

$$ \vec{a} = \dot{\vec{v}} = \dot{r}\vec{u_r} + r \dot{\vec{u_r}} =  \ddot{r}\vec{u_r} + \dot{r}\dot{\theta}\vec{u_\theta} + \dot{r}\dot{\theta}\vec{u_\theta} - r\ddot{\theta}\vec{u_\theta} + r \dot{\theta}^2\vec{u_r} \\
= (\ddot{r} - r \dot{\theta}^2 )\vec{u_r} + ( r\ddot{\theta}\vec{u_\theta} - 2\dot{r}\dot{\theta})\vec{u_\theta}\\
= a_r \vec{u_r} + a_\theta\vec{u_\theta}
$$

We are now equipped with mathematical expression to fully describe the point like motion of any object in polar coordinate as a planet orbiting its star.

## Proof of the second law

### The wonderful cross product 

Before moving to the Kepler laws, we still need a bit of patience and introduce a new very powerful tool. This tool is a new way to multiply two vectors to get a third one that can encompass all the informations about the rotation of an object. It is hence easy to understand why this tool will be so usefull when describing planetary orbits.

Consider two vectors $\vec{u}$ and $\vec{v}$. How could you combine them? You might already be familiar with one way to combine vectors together? Indeed, it is possible to build a number out two vectors using the scalar or dot product $\vec{u}\cdot\vec{v}$. The resulting number tells you how much the two vectors are aligned and allows to calculate lengths. There exist however, another way to multiply two vectors. 

In order to study rotations, it will indeed be useful to define another product, called the *cross product*, allowing this time to get a third vector $\vec{w}$ from two vectors $\vec{u}$ and $\vec{v}$. It is usually noted $\vec{w}=\vec{u} \times \vec{v}$ or $\vec{w}=\vec{u} \wedge \vec{v}$.

Contrary to the dot product, this product quantifies how perpendicular the two original vectors are. Since it gives back a vector and not a simple number, it has a lot of geometry hidden in it. We'll see that, while the scalar product defines lengths, the cross product defines surfaces from the original vectors.

- This third vector is always orthogonal to the plane defined by $\vec{u}$ and $\vec{v}$ and thus always tells you in which plane the two original vectors lies.

- You can find it's direction using the right hand rule. 
From this, you can see that it is *antisymetric* (or non commutative)

$$ \vec{u} \wedge \vec{v} = - \vec{v} \wedge \vec{u}$$ 

- It's length gives the area of the parallelogram that can be built out of $\vec{u}$ and $\vec{v}$ 

$$ \|\vec{w}\|=\|\vec{u}\|\|\vec{v}\|\sin(\langle \vec{u},\vec{v}\rangle)$$

Which is indeed the area of a rectangle $\|\vec{w}\|=S_{\rm rect} = \|\vec{u}\|\|\vec{v}\|$ with $\langle \vec{u},\vec{v}\rangle=90^{\circ}$.

A very useful property coming from this, is that any numbers multiplying the vectors can be put in front of the product

$$ (a\vec{u}) \wedge (b\vec{v}) = ab \, (\vec{u} \wedge \vec{v})$$ 

This is especially usefull when expressing vectors in term of unit vectors. Using the right-hand rule and the above definitions we can get

$$ \vec{u_r} \wedge \vec{u_\theta} = \vec{u_z}$$

$$ \vec{u_z} \wedge \vec{u_\theta} = -\vec{u_r}$$

$$ \vec{u_z} \wedge \vec{u_r} = -\vec{u_\theta}$$

### Newton and gravity

We will take here for granted the universal law of gravitation between two bodies of masses $M$ and $m$ proposed by Newton in his principias. Let $M\gg m$ be the mass of the star, then

$$ \vec{F_G} = -\frac{GMm}{r^2}\vec{u_r} $$

### The angular momentum 

We now make use of the new tool of cross product to define the *angular momentum* as the vector given by
$$ \vec{L} = \vec{r} \wedge \vec{p} $$

This quantity can fully describe a rotation since it gives you at any-time
- A single plane of rotation
- A single direction of rotation
- A "strength of rotation", greater if the speed is orthogonal to the radius $\|\vec{L}\|= \|\vec{r}\|\|\vec{p}\|\sin(\langle \vec{r},\vec{p}\rangle)$

Now let us look at how this quantity changes with time for a planet under the influence of gravity:

$$ \frac{\text{d}\vec{L}}{\text{d} t} = \frac{\text{d}\vec{r}}{\text{d} t} \wedge \vec{p} + \vec{r} \wedge \frac{\text{d}\vec{p}}{\text{d} t} \\
 = m \vec{v} \wedge \vec{v} + \vec{r} \wedge \sum \vec{F} = \frac{GMm}{r}\vec{u_r} \wedge \vec{u_r}  = \vec{0} $$

This is a wonderful result! $$\vec{L}$$ does not change with time: it is a conserved quantity. As such, when other effects as tidal forces or interactions with other planets are neglected, the planet will always rotate identically, with a constant value of $$\vec{L}$$[^1]. As $\vec{L}$ defines a single plane of rotation, this implies that the planet's motion must remain in a given plane.

[^1]: Note that in practice, this is never the cases. As planets are not ideal point particles but have a volume, they loose energy due to tidal forces, leading to a change of $$\vec{L}$$. As such, the moon is getting further and further away from us at about 3-4 cm/yr while the rotation of earth on itself is slowing down (by about one second every 50,000 years) due to their moon/earth interactions. In remote past, as e.g. the Cambrian when the first large animals were roaming in our oceans, the moon was thus bigger in the sky and the days were shorter! This process ends when bodies have syncroneous rotations i.e. both have the same period and are constantly facing one another, as this is the case of Pluton and its large moon Charon for example.

For convinience, we can express $\vec{L}$ in terms of the polar coordinates defined before as

$$  \vec{L} = \vec{r} \wedge \vec{p} = r m \vec{u_r}\wedge  \vec{v} = mr^2 \dot{\theta}  \vec{u_r}\wedge  \vec{u_\theta}= mr^2 \dot{\theta} \vec{u_z} $$ 

In which we used all the properties of the cross product defined above. As such, the length of the angular momentum vector is simply given by

$$ \|\vec{L}\| = mr^2 \dot{\theta} $$

## Proof of the second law

We now have all the tools required to proof the second Kepler law!
Remember that for a circle of radius $r$, the perimeter (i.e. the total length) is $\ell=2\pi r$, corresponding to a full turn of the circle in radian $\theta=2\pi$. We conclude that for a general angle $\theta$, the associated perimeter must be $\ell=r\theta$, recovering the correct expression for a full turn $\theta=2\pi$. Following the same logic, we know that for a disk, the full area is $S=\pi r^2$, such that the area of a slice of angle $\theta$ must be given by $S=\theta r^2/2$ in order to recover the correct expression for the full circle ($\theta=2\pi$). As such an infinitesimal area covered by $\vec{OM}$ on an orbit, associated with a small rotation $\text{d}\theta$ and approximated locally as a circle of radius $r$, can be written as

$$ \text{d}S = \frac{r^2 \text{d}\theta}{2},$$

which can also be find by considering the area of a small triangle on the orbit. Dividing by $\text{d}t$, we deduce that

$$ \frac{\text{d}S}{\text{d}t} = \frac{r^2}{2} \frac{\text{d}\theta}{\text{d} t} = \frac{r^2}{2} \dot{\theta} = \frac{\|\vec{L}\|}{2m}$$

Since $m$ is a constant and $\vec{L}$ is a conserved quantity, we already proved the second law! Since the derivative of the area $S$ with respect to time is constant, it means that $S$ always changes identically with time no matter where we are on the orbit. 
To see this more clearly, let us integrate this equation as

$$ \Delta S = \int \frac{\|\vec{L}\|}{2m} t = \frac{\|\vec{L}\|}{2m} \Delta t $$

For an ellipse, integrating over a full period ($\Delta t=T$ and $\Delta S=\pi ab$) gives

$$ S_{\rm tot} = \pi ab = \frac{\|\vec{L}\|}{2m}  T$$

Such that
$$ \frac{\|\vec{L}\|}{2m} = \frac{\pi ab}{T} $$

The second law can thus be expressed as

$$ \boxed{\Delta S = \frac{\pi ab}{T} \Delta t} $$

On a given orbit, (think for example at the earth motion) $a,b$ and $T$ are constants. Hence in a given time $$\Delta t$$ (say 1 day), the planet covers the same area $$\Delta S$$. One then understands that, in order to do so, the planet needs to go way faster when close to its star than when far away.

![my image](../images/kepler2.gif  "my image")

# A warm-up: third law for spherical orbits

For a spherical orbit $r=R$ is a constant (thus $\dot{r} = 0$) and the angular velocity is a constant ($\ddot{\theta}=0$). This allow us to simplify drastically the expression for the speed and the acceleration in polar coordinates as

$$ \vec{v} = R \dot{\theta} \vec{u_\theta}$$

and

$$ \vec{a} = -R\dot{\theta}^2 \vec{u_r}= -\frac{v^2}{R} \vec{u_r} $$

Note that you can of course recover these expressions from scratch by deriving the position vector $\vec{OM}=R \vec{u_r}$, or more lengthly in cartesian coordinates by deriving with respect to time the pair $x=R\cos(\theta)$ and $y=R\sin(\theta)$. This is a good exercice to check your understanding of the mathematical tools we have been using!

As such, the second Newton law $\vec{F}_G=m\vec{a}$ takes the form

$$ -\frac{GmM}{R^2} \vec{u_r} =  m \vec{a} = -\frac{m v^2}{R} \vec{u_r}$$

there is thus no component along $\theta$, $a_\theta=0$. Rearanging the terms, one find the important relationship

$$ v = \sqrt{\frac{GM}{R}} $$

As such, for a circular orbit, knowing the altitude $R$ and the mass of the orbiting object is enough to know its speed.

Over a whole period $T$, the distance travelled by the planet is $d= 2\pi R$. Since the volocity is constant, we can use the elementary definition of the velocity as 

$$v = \frac{d}{T}= \frac{2\pi R}{T}$$

Combining the two expressions for $v$, we can derive

$$ \frac{4\pi^2 R^2}{T^2} = \frac{GM}{R} $$

$$ \frac{T^2}{R^3} = \frac{4\pi^2}{GM} $$

Which is the third Kepler law in the particular case of circular orbits.

# Presenting the first law

## Conics

The first law states that the orbit of astronomical objects bounded by gravity are conics. To better understand this, we should thus first understand more fully what are conics. Conics are obtained from 1D slices of a 2D cone. 

**Add picture Blender?**

They are defined in the 2D plane by the following equation in polar coordinates

$$r(\theta) = \frac{p}{1+e\cos(\theta-\theta_0)}$$ 

In which $e$ is called the *eccentricity* and $p$ has the sweet name of semi-latus rectum.

**Add plot conics python + code**

# General proof of the first law

Here comes the most technical aspect of our discussion. Hang on!

For a general orbit, the second Newton law implying only gravity can be written as

$$ \vec{F_G} = m \vec{a} $$

Writing again $\vec{F_G}= -\frac{GMm}{r^2} \vec{u_r}$ and $\vec{a}=a_r \vec{u_r}+a_\theta \vec{u}_\theta$, we can project on the two polar basis vectors

$$
\begin{cases}
\vec{F_G}_r &= m a_r \\
\vec{F_G}_\theta &= a_\theta
\end{cases}$$

$$\begin{cases}
 -\frac{GM}{r^2}&= a_r \\
 0 &= a_\theta 
\end{cases}$$

Using the general expression for the accelaration in polar coordinates, one gets the system

$$ \ddot{r} - r\dot{\theta}^2 = -\frac{GM}{r^2}$$ 

$$ r\ddot{\theta} + 2\dot{r}\dot{\theta}=0$$

The second equation is just the conservation of angular momentum

$$ \dot{\|\vec{L}\|} = \frac{\text{d}(r^2\dot{\theta})}{\text{d}t} = 0 $$

While the first one really is the equation of motion.

To see more clearly what is happening, we will rewrite this equation in term of $u=1/r$. As we will show this will give us an harmonic oscillator equation that we can solve easily

$$ u'' + u - \frac{1}{p} = 0$$


To see this, we first introduce the notation $x'= \frac{\text{d}x}{\text{d}\theta}$. Let's also not forget the cross-derivative relation
$\dot{x}= \frac{\text{d}x}{\text{d}\theta}\frac{\text{d}\theta}{\text{d}t} = x'\dot{\theta}$

We then have

$$  \dot{u}= \dot{1/r} = -\frac{1}{r^2}\dot{r}
 \Rightarrow \dot{r} = -r^2 \dot{u} = -r^2\dot{\theta}u'$$

That is

$$ \boxed{\dot{r} =-\frac{\|\vec{L}\|}{m}u'}$$

Similarly

$$ \ddot{r} = \frac{\text{d}}{\text{d}t}\left(-\frac{\|\vec{L}\|}{m}u'\right)= -\frac{\|\vec{L}\|}{m}\dot{\theta}u'' = -\frac{\|\vec{L}\|^2}{m^2r^2}u''$$

So that

$$ \boxed{\ddot{r} = -\frac{\|\vec{L}\|^2}{m^2}u^2u'}$$

Inserting these expressions in the equation of motion, we have

$$ -\frac{\|\vec{L}\|^2}{m^2}u^2u'-\frac{\|\vec{L}\|^2}{m^2}u^3 + GMu^2 =0$$

That we can finally rerwrite in the suggestive form

$$ \boxed{u'' + u - \frac{1}{p} = 0}$$

With 

$$ \boxed{p= \frac{\|\vec{L}\|^2}{GMm^2}}$$

The general solution of the harmonic oscillator (see harmonic oscillator) is

$$ u = \frac{1}{p} + c_1 \cos(\theta) + c_2 \sin(\theta)$$

or 

$$ u = \frac{1}{p} + e\cos(\theta - \theta_0) $$

Going back to r, we get

$$\boxed{r = \frac{p}{1+e\cos(\theta-\theta_0)}}$$ 

# Third law for ellipses

$$S= \int \text{d}S = \pi ab$$

$$S = \int_T \frac{\|\vec{L}\|}{2m} \text{d}t = \frac{\|\vec{L}\|}{2m}T $$

$$ T^2 = \frac{4\pi^2 a^2b^2 m^2}{L^2}$$

$$ p = \frac{b^2}{a} $$

$$ p = \frac{\|\vec{L}\|^2}{GMm^2} $$

$$ \|\vec{L}\|^2 = \frac{GMm^2b^2}{a} $$

And so, we immediatly find back the third Kepler law

$$ \frac{T^2}{a^3} = \frac{4\pi^2}{GM} $$

# Limits

Keep the same form even when dropping the assumption that $$M\gg m$$, introducing the *reduced mass* $$\mu$$.

$$ \frac{T^2}{a^3} = \frac{4\pi^2}{G(M+m)} $$

Can only be applied to a two body system.

See three bodies problem.

Assumes Newtonian gravitation, general relativity is required for strong fields.