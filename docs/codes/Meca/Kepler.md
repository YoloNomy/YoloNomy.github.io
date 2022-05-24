---
layout: default
title: Kepler laws
parent: codes
nav_order: 2
---

# Kepler laws

## The laws

- law 1: trajectories
- law 2: areas
- law 3: $$T^2/a^3$$

## History : from laws to theorem

# Why are they so important ?

# Examples

The mass of Sgr A* and the discovery of black holes.

Exoplanets

# Polar coordinates

As we discussed already (see ...), the first thing to do before studying a motion in mechanics, is to define both a *frame* (otherwise motion is meaningless) and a *coordinate system* (otherwise it is impossible to quantify anything).
So far we were only using *cartesian coordinates*, that is, perpendicular and fixed axis $(O,x,y,z)$. Cylindrical/Polar coordinates replace $x$ and $y$ by $r$ and $\theta$.

Using Pythagorian theorem (need figures):

$$ r = \sqrt{x^2 + y^2} $$

And from basic trigonometry (need figures):

$$ \theta = \arctan(y/x) $$

Also from basic trigonometry (need figures):

$$x = r \cos\theta $$

$$y = r \sin\theta $$

The unit vectors:

$$ \vec{u_r} = \cos\theta \vec{u_x} + \sin\theta \vec{u_y} $$ 

$$ \vec{u_\theta} = -\sin\theta \vec{u_x} + \cos\theta \vec{u_y} $$ 

While cartesian coordinates are fixed $ \dot{u_x}=0$ and $\dot{u_y}=0$ (We use the notation $ \dot{x} = \frac{\text{d}x}{\text{d}t}$.
). Polar coordinate vectors change with time.

$$ \frac{ \text{d}\vec{u_r}}{\text{d} \theta } = -\sin\theta \vec{u_x} + \cos\theta \vec{u_y} = \vec{u_\theta}  $$ 

$$ \frac{ \text{d}\vec{u_\theta}}{\text{d} \theta } = -\cos\theta \vec{u_x} - \sin\theta \vec{u_y} = - \vec{u_r} $$ 

$$ \dot{u_r} = \frac{\text{d} \theta}{\text{d} t}\frac{ \text{d}\vec{u_r}}{\text{d} \theta } = \dot{\theta} \vec{u_\theta}  $$ 

$$ \dot{u_\theta} = \frac{\text{d} \theta}{\text{d} t} \frac{ \text{d}\vec{u_\theta}}{\text{d} \theta } = -\dot{\theta} \vec{u_r}  $$ 

The position:

$$ \vec{r} = r \vec{u_r}$$

The velocity:

$$ \vec{v} = \dot{\vec{r}} = \dot{r}\vec{u_r} + r \dot{\vec{u_r}} =  \dot{r}\vec{u_r} + r \dot{\theta}\vec{u_\theta} $$

The acceleration:

$$ \vec{a} = \dot{\vec{v}} = \dot{r}\vec{u_r} + r \dot{\vec{u_r}} =  \ddot{r}\vec{u_r} + \dot{r}\dot{\theta}\vec{u_\theta} + \dot{r}\dot{\theta}\vec{u_\theta} - r\ddot{\theta}\vec{u_\theta} + r \dot{\theta}^2\vec{u_r} \\
= (\ddot{r} - r \dot{\theta}^2 )\vec{u_r} + ( r\ddot{\theta}\vec{u_\theta} - 2\dot{r}\dot{\theta})\vec{u_\theta}\\
= a_r \vec{u_r} + a_\theta\vec{u_\theta}
$$

# Proof of the second law

## The cross product 

Consider two vectors $\vec{u}$ and $\vec{v}$. How could you combine them? We already saw (see), that it is possible to make a number out of them using the scalar or dot product $\vec{u}\cdot\vec{v}$. This number quantify how much the two vectors are aligned and allows to calculate length. 

$\vec{w}=\vec{u} \times \vec{v}$ or $\vec{w}=\vec{u} \wedge \vec{v}$.

Right hand rule.

$$ |\vec{w}|=|\vec{u}|\vec{v}|\sin(\langle \vec{u},\vec{v}\rangle)$$

$$ \vec{u} \wedge \vec{v} = - \vec{v} \wedge \vec{u}$$ 

$$ a\vec{u} \wedge b\vec{v} = ab \, \vec{u} \wedge \vec{v}$$ 

## Newton and gravity

$$ \vec{F_G} = -\frac{GMm}{r^2}\vec{u_r} $$

## The angular momentum 

$$ \vec{L} = \vec{r} \wedge \vec{p} $$

$$ \frac{\text{d}\vec{L}}{\text{d} t} = \frac{\text{d}\vec{r}}{\text{d} t} \wedge \vec{p} + \vec{r} \wedge \frac{\text{d}\vec{p}}{\text{d} t} \\
 = m \vec{v} \wedge \vec{v} + \vec{r} \wedge \sum \vec{F} = \frac{GMm}{r}\vec{u_r} \wedge \vec{u_r}  = \vec{0} $$

At every moment $\vec{L}$ defines a single plane of rotation. Since it is conserved, the whole motion remains in a given plane.

We can calculate $\vec{L}$ in terms of the coordinates:

$$  \vec{L} = \vec{r} \wedge \vec{p} = r m \vec{u_r}\wedge  \vec{v} = mr^2 \dot{\theta}  \vec{u_r}\wedge  \vec{u_\theta} $$ 

$$ \vec{L} = mr^2 \dot{\theta} \vec{u_z} $$

$$ |\vec{L}| = mr^2 \dot{\theta} $$



## Proof of the second law

Remember that for a circle of radius $r$, the perimeter is $\ell=2\pi r$, corresponding to a full turn of the circle in radian $\theta=2\pi$. We conclude that for a small angle $d\theta$, $d \ell = Rd \theta$. Following the same logic, we know that for a disk, the full area is $S=\pi r^2$ and so an infinitesimal area is given by

$$ dS = \frac{r^2 \text{d}\theta}{2}$$

$$ \frac{dS}{dt} = \frac{r^2}{2} \dot{\theta} = \frac{|\vec{L}|}{2m}$$

$$ \Delta S = \int \frac{|\vec{L}|}{2m} dt = \frac{|\vec{L}|}{2m} \Delta t $$

For an ellipse, integrating over a full period gives:

$$ S_{\rm tot} = \pi ab = \frac{|\vec{L}|}{2m}  T$$

Giving the relation:

$$ \frac{|\vec{L}|}{2m} = \frac{\pi ab}{T} $$

So that the second law is simply given by:

$$ \boxed{\Delta S = \frac{\pi ab}{T} \Delta t} $$

# Presenting the first law

## conics

Conic polar equation:

$$r = \frac{p}{1+e\cos(\theta-\theta_0)}$$ 

# A warm-up: third law for spherical orbits

For a spherical orbit $r=R$ is a constant (thus $\dot{r} = 0$) and the angular velocity is a constant ($\ddot{\theta}=0$).

$$ \vec{v} = R \dot{\theta} \vec{u_\theta}$$

$$ \vec{a} = -R\dot{\theta}^2 \vec{u_r}= -\frac{v^2}{R} \vec{u_r} $$

$$ -\frac{GmM}{R^2} \vec{u_r} =  m \vec{a} = -\frac{m v^2}{R} \vec{u_r}$$

$$ v = \sqrt{\frac{GM}{R}} $$

Over a whole period $T$, the distance is $d= 2\pi R$. Since the volocity is constant 

$$v= \frac{d}{T}= \frac{2\pi R}{T}$$

Using the two expressions we get:

$$ \frac{4\pi^2 R^2}{T^2} = \frac{GM}{R} $$

$$ \frac{T^2}{R^3} = \frac{4\pi^2}{GM} $$

Which is the third Kepler law.

# General proof of the first law

Here comes the most technical aspect of our discussion. Hang on!

In the most general case, thes second Newton law is:

$$ \vec{F_G} = m \vec{a} $$

That we can project on the two polar basis vectors:

$$ -\frac{GMm}{r^2}\vec{u_r} = a_r\vec{u_r} $$

$$ 0 = a_\theta \vec{u_\theta}$$

Using the general expression for the accelaration in polar coordinates, one gets the system

$$ \ddot{r} - r\dot{\theta}^2 = -\frac{GM}{r^2}$$ 

$$ r\ddot{\theta} + 2\dot{r}\dot{\theta}=0$$

The second equation is just the conservation of angular momentum:

$$ \dot{|L|} = \frac{\text{d}(r^2\dot{\theta})}{\text{d}t} = 0 $$

While the first one really is the equation of motion.

To see more clearly what is happening, we will rewrite this equation in term of $u=1/r$. As we will show this will give us an harmonic oscillator equation that we can solve easily:

$$ u'' + u - \frac{1}{p} = 0$$


To see this, we first introduce the notation $x'= \frac{\text{d}x}{\text{d}\theta}$. Let's also not forget the cross-derivative relation: $x'= \frac{\text{d}x}{\text{d}t}\frac{\text{d}\theta}{\text{d}t} = \dot{x}\dot{\theta}$

We then have:

$$  \dot{u}= \dot{1/r} = -\frac{1}{r^2}\dot{r}
 \Rightarrow \dot{r} = -r^2 \dot{u} = -r^2\dot{\theta}u'$$

That is:

$$ \boxed{\dot{r} = \frac{-L}{m}u'}$$

Similarly:

$$ \ddot{r} = \frac{\text{d}}{\text{d}t}\left(-\frac{L}{m}u'\right)= -\frac{L}{m}\dot{\theta}u'' = -\frac{L^2}{m^2r^2}u''$$

So that:

$$ \boxed{\ddot{r} = \frac{-L^2}{m^2}u^2u'}$$

Inserting these expressions in the equation of motion, we have:

$$ -\frac{L^2}{m^2}u^2u'--\frac{L^2}{m^2}u^3 + GMu^2 =0$$

That we can finally rerwrite in the suggestive form:

$$ \boxed{u'' + u - \frac{1}{p} = 0}$$

With 

$$ \boxed{p= \frac{L^2}{GMm^2}}$$

The general solution of the harmonic oscillator (see harmonic oscillator) is

$$ u = \frac{1}{p} + c_1 \cos(\theta) + c_2 \sin(\theta)$$

or 

$$ u = \frac{1}{p} + e\cos(\theta - \theta_0) $$

Going back to r, we get:

$$\boxed{r = \frac{p}{1+e\cos(\theta-\theta_0)}}$$ 

# Third law for ellipses

$$S= \int dS = \pi ab$$

$$S = \int_T \frac{L}{2m} dt = \frac{L}{2m}T $$

$$ T^2 = \frac{4\pi^2 a^2b^2 m^2}{L^2}$$

$$ p = \frac{b^2}{a} $$

$$ p = \frac{L^2}{GMm^2} $$

$$ L^2 = \frac{GMm^2b^2}{a}$$

And so, we immediatly find back the third Kepler law:

$$ \frac{T^2}{a^3} = \frac{4\pi^2}{GM}$$

# Limits

See three bodies problem.
