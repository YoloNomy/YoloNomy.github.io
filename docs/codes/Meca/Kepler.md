---
layout: default
title: Kepler laws
parent: codes
nav_order: 2
---

# Kepler laws

- law 1: trajectories
- law 2: areas
- law 3: $$T^2/a^3$$

# Why are they so important ?

# Examples

The mass of Sgr A* and the discovery of black holes.

# Polar coordinates

$$ r = \sqrt{x^2 + y^2} $$
$$ \theta = \arctan(y/x) $$

$$x = r \cos\theta $$
$$y = r \sin\theta $$

$$ \vec{u_r} = \cos\theta \vec{u_x} + \sin\theta \vec{u_y} $$ 
$$ \vec{u_\theta} = -\sin\theta \vec{u_x} + \cos\theta \vec{u_y} $$ 

While cartesian coordinates are fixed $ \dot{u_x}=0$ and $\dot{u_y}=0$ (We use the notation $ \dot{x} = \frac{\text{d}X}{\text{d}t}$.
). Polar coordinate vectors changes with time.

$$ \frac{ \text{d}\vec{u_r}}{\text{d} \theta } = -\sin\theta \vec{u_x} + \cos\theta \vec{u_y} = \vec{u_\theta}  $$ 
$$ \frac{ \text{d}\vec{u_\theta}}{\text{d} \theta } = -\cos\theta \vec{u_x} - \sin\theta \vec{u_y} = - \vec{u_r} $$ 

$$ \dot{u_r} = \frac{\text{d} \theta}{\text{d} t}\frac{ \text{d}\vec{u_r}}{\text{d} \theta } = \dot{\theta} \vec{u_\theta}  $$ 
$$ \dot{u_\theta} = \frac{\text{d} \theta}{\text{d} t} \frac{ \text{d}\vec{u_\theta}}{\text{d} \theta } = -\dot{\theta} \vec{u_r}  $$ 

The position:

$$ \vec{r} = r \vec{u_r}$$

The velocity:

$$ \vec{v} = \dot{\vec{r}} = \dot{r}\vec{u_r} + r \dot{\vec{u_r}} =  \dot{r} $$

The acceleration:

# Proof of the second law

## The cross product 

Consider two vectors $\vec{u}$ and $\vec{v}$. 
$\vec{u} \times \vec{v}$ or $\vec{u} \wedge \vec{v}$.

Right hand rule.

$$ \vec{u} \wedge \vec{v} = - \vec{v} \wedge \vec{u}$$ 

$$ a\vec{u} \wedge b\vec{v} = ab \, \vec{u} \wedge \vec{v}$$ 

## Newton and gravity

$$ \vec{F_G} = -\frac{GMm}{r^2}\vec{u_r} $$

## The angular momentum 

$$ \vec{L} = \vec{r} \wedge \vec{p} $$

$$ \frac{\text{d}\vec{L}}{\text{d} t} = \frac{\text{d}\vec{r}}{\text{d} t} \wedge \vec{p} + \vec{r} \wedge \frac{\text{d}\vec{p}}{\text{d} t} $$
$$ = m \vec{v} \wedge \vec{v} + \vec{r} \wedge \sum \vec{F} = \frac{GMm}{r}\vec{u_r} \wedge \vec{u_r}  = \vec{0} $$


$$  \vec{L} = \vec{r} \wedge \vec{p} = r m \vec{u_r}\wedge  \vec{v} = mr^2 \dot{\theta}  \vec{u_r}\wedge  \vec{u_\theta} $$ 

$$ \vec{L} = mr^2 \dot{\theta} \vec{u_z} $$

## Proof of the second law

$$ dS = \frac{r^2 \text{d}\theta}{2}$$

$$ \frac{dS}{dt} = \frac{r^2}{2} \dot{\theta} = \frac{|\vec{L}|}{2m}$$

$$ \Delta S = \int \frac{|L|}{2m} dt = \frac{|L|}{2m} \Delta t $$

The planets orbit are in one single plane.

# Presenting the first law

## conics

# A warm-up: third law for spherical orbits

$$ \vec{v} = R \dot{\theta} \vec{u_\theta}$$

$$ \vec{a} = R\dot{\theta}^2 \vec{u_r}= -\frac{v^2}{R} \vec{u_r} $$

# General proof of the first law

# General proof of the third law

