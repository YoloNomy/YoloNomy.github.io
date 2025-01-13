---
layout: default
title: Work and Energy
parent: Newton
nav_order: 2
---
**PAGE STILL UNDER CONSTRUCTION**

# Work and Energy: integrals and the dot product

The apparently very practical notion of *work*, defining how "efficient" a force is to move a body, will lead us to the very abstract notion of *energy*, which is one of the most important notion of all physics. In order to introduce the work quantity, we however need a new tool: the dot product, which allows to multiply two vectors to obtain a number.

## "Multiplying vectors" : the dot product

We will now define a way to take any two vectors, say $\vec{A}$ and $\vec{B}$ and "multiply" them in order to obtain a number, noted $\vec{A}\cdot \vec{B}$. Why on earth would be want to do that? What is of interest for us as physicist, will be to find a way to measure how aligned or "perpendicular vectors are.

- It is minimal and equal to zero when the two vectors are perpendicular. Hence, if you obtain $\vec{A}\cdot \vec{B}=0$, you can safely conclude that there is a right angle between $\vec{A}$ and $\vec{B}$.

- It is maximal and equal to the product of the lengths $\|\vec{A}\|\|\vec{B}\|$ when the two vectors are aligned i.e. pointing in the same or opposite direction.

It allows to compute the length of the vectors and basically how a vector "project" to another. 

Choosing a 3 dimensional orthonormal basis of space in which to express two vectors as

$$\vec{A}=\begin{pmatrix}x_A\\y_A\\z_A\end{pmatrix} \qquad \qquad \vec{B}=\begin{pmatrix}x_B\\y_B\\z_C\end{pmatrix}$$

Is defined as

$$\boxed{\vec{A}\cdot\vec{B}= x_Ax_B + y_Ay_B + z_Az_C}$$

While this definition requires the choices of an orthonormal basis $(x,y,z)$ in which to decompose the vectors, however, it can be proven to be independent of the choice of orthonormal basis i.e. it doesn't change if you rotate your basis.

<details>
  <summary>Proof of the basis independence of the dot product</summary>

Let $(x,y,z)$ be a choice of basis in which the two vectors $\vec{A}$ and $\vec{B}$ are expressed by the triplets $(x_A,y_A,z_A)$ and $(x_B,y_B,z_B)$. Consider another basis, $(x',y',z')$ rotated from the first one by an angle $\theta$ in which the two vectors $\vec{A}$ and $\vec{B}$ are expressed by the triplets $(x'_A,y'_A,z'_A)$ and $(x'_B,y'_B,z'_B)$.

Then:
$$\vec{A}\cdot\vec{B}= x_Ax_B + y_Ay_B + z_Az_C $$

</details>

However it requires that the coordinates are necessarily expressed in an orthonormal basis to be properly defined.

Another way to define the dot product, is given by the geometric definition:

$$\vec{A}\cdot\vec{B}=|\vec{A}||\vec{B}|\cos(\theta)$$

where $\theta$ is the angle between $\vec{A}$ and $\vec{B}$ when there bases are brought to the same point in order to compare them. This geometric definition can be proven to be equivalent to the coordinate one.

<details>
  <summary>Proof of the equivalence of the two definitions</summary>

For simplicity let's start by assuming that the geometrical definition is true and try to recover the original definition from it.
Choosing an orthonormal basis of vectors $(\vec{e}_x,\vec{e}_y, ...)$, in which to express the two vectors with basis at the same point as $\vec{A}=\sum_i A^i\vec{e}_i$ and $\vec{B}=\sum_i B^i\vec{e}_i$. Then, we have, by the geometrical definition
$$\vec{A}\cdot\vec{e}_i = |\vec{A}||\vec{e}_i|\cos(\theta_i)=A^i$$, where $|\vec{e}_i|=1$ because the basis is orthonormal and $|\vec{A}|\cos(\theta_i)=A^i$ using trigonometry in a right triangle (add figure).

Then, we can re-express the total dot product between $\vec{A}$ and $\vec{B}$ as
$$ \vec{A}\cdot\vec{B}= \sum_i B^i\vec{A}\cdot\vec{e_i}=\sum_i B^iA^i$$.
In which we used the property of the dot product $\vec{A}\cdot(a\vec{B})=a\vec{A}\cdot\vec{B}$, where $a\in \mathbb{R}$ is a number.
</details>

The length of a vector is actually properly defined by using the dot product as

$$\left|\vec{A}\right|=\sqrt{\vec{A}\cdot\vec{A}}$$

From which we recover easily what pythagorian theorem would give you, that is $\left\|\vec{A}\right\|=\sqrt{x_A^2+y_A^2+z_A^2}$. We often simply write $A=\left\|\vec{A}\right\|$ and $A^2$ or $\vec{A}^2=\vec{A}\cdot\vec{A}$.   

Another reason why the dot product is so much needed, is that, while we know how to derivate a vector, we still haven't define what it could mean to "integrate" a vector.

## Work

The *work* produced by a constant force $\vec{F}$ on a straight distance $\vec{AB}$ is defined as

$$
W_{AB} = \vec{F}\cdot\vec{AB}  
$$


$$
\delta W=\vec{F}\cdot\text{d}\vec{\ell}
$$

$$W_{A\to B} = \int_A^B\delta W$$

## Kinetic energy

You might know that the kinetic energy of a body going at velocity $v$ is given by the "famous" formula:

$$E_C=\frac{1}{2}mv^2$$

Let us now understand why and where this comes from. It actually is nothing else but work!

To do so, let us consider what is the total work made by all the forces acting on a body during it's motion from a point $A$ to a point $B$:

$$
\begin{aligned}
W_{A\to B}= &\int_A^B\delta W=\int_A^B\sum\vec{F}\cdot\text{d}\vec{\ell}
\end{aligned}
$$

Now, we can use Newton's second law defining what a force is as $\sum\vec{F}=m\vec{a}$ such that

$$
\begin{aligned}
W_{A\to B}= &\int_A^Bm\vec{a}\cdot\text{d}\vec{\ell}\\
=&m\int_A^B\frac{\text{d}\vec{v}}{\text{d}t}\cdot\text{d}\vec{\ell}
\end{aligned}
$$

In which we remembered the definition of acceleration, and put the constant $m$ in front of the integral. Now, the velocity vector $\vec{v}$ is, by definition, the distance $\text{d}\vec{\ell}$ divided by the time it took to travel this distance $\text{d} t$, such that we can simply write

$$ \vec{v}=\frac{\text{d}\vec{\ell}}{\text{d} t} \Rightarrow \text{d}\vec{\ell}= \vec{v}\,\text{d} t$$

Putting this in our calculation for the work, we get

$$
\begin{aligned}
W_{A\to B}= &m\int_A^B\frac{\text{d}\vec{v}}{\text{d}t}\cdot\text{d}\vec{\ell}\\
=&m\int_{t_A}^{t_B}\frac{\text{d}\vec{v}}{\text{d}t}\cdot\vec{v}\,\text{d} t\\
=&m\int_{v_A}^{v_B}\text{d}\vec{v}\cdot\vec{v}
\end{aligned}
$$

In which we "simplified" the $\text{d} t$ as is allowed by the rules of derivatives. Now, there are several ways to think about this integral, but let us detail it fully to be sure to understand as we are not yet familiar with the properties of the dot product  (even though this might be a bit overkill!). To do so, we compute completly the dot product by decomposing the vectors in a coordinate basis $(x,y,z)$, such that $\vec{v}=(v_x,v_y,v_z)$ and hence $\text{d}\vec{v}=(\text{d}v_x,\text{d}v_y,\text{d}v_z)$. As such, using the rule of the dot product, we obtain

$$
\begin{aligned}
W_{A\to B}= m\int_{v_A}^{v_B}v_x\text{d}v_x+ v_y\text{d}v_y+ v_z\text{d}v_z
\end{aligned}
$$

which we can split in three integrals

$$
\begin{aligned}
W_{A\to B}= 
&=m\left(\int_{v_{x,A}}^{v_{x,B}}v_x\text{d}v_x+ \int_{v_{y,A}}^{v_{y,B}}v_y\text{d}v_y+ \int_{v_{z,A}}^{v_{z,B}}v_z\text{d}v_z\right)
\end{aligned}
$$

Now things are much easier than what you might think! These are just integrals of the type $\int_A^B x \,\text{d}x$ which each gives $[x^2/2]_A^B$. You can find this either by remembering the simple rule $(x^2)'=2x$ and that the integral is sort of the "opposite" of the derivate, or if you know by heart the very important and always useful rule for integrals $\int_A^Bx^n\,\text{d}x=[x^{n+1}/(n+1)]_A^B$. Computing the integrals in the expression of $$W_{A\to B}$$, we thus obtain

$$
\begin{aligned}
W_{A\to B}= m \left([v_x^2/2]_A^B+ [v_y^2/2]_A^B+ [v_z^2/2]_A^B\right)
\end{aligned}
$$

in which we recognize the dot product of $\vec{v}$ with itself $\vec{v}^2=\vec{v}\cdot\vec{v}=v_x^2+v_y^2+v_z^2$. After all these derivations, we can find that $$W_{A\to B}$$ is simply given by

$$
\begin{aligned}
W_{A\to B}=\frac{m}{2}[\vec{v}^2]_A^B= \frac{m}{2}(v_B^2-v_A^2)
\end{aligned}
$$

We thus define the kinetic energy $E_C$ of a moving body as

$$
E_C= \frac{1}{2}mv^2
$$

This is a quantity that can be associated to a moving body of mass $m$ and velocity $v$ at any point of its trajectory. We will see that it turns out to be a crucial quantity for all of physics as we know it! So far, it is just a 
convinient trick to rewrite the work between two points $A$ and $B$ as

$$ W_{A\to B} = E_C^B - E_C^A = \Delta E_C $$

Remembering that the linear momentum $p=mv$ is an important quantity (as we discussed in lesson 1), $E_C$ can also be expressed as

$$ E_C = \frac{\vec{p}^2}{2m} $$

We saw that in the abscence of forces, $\vec{p}$ was a conserved quantity. As such, $E_C$ is also conserved in that case. This is our first glimps at the overwhelmingly important conservation of energy.

## Potential energy and conservative forces

### Weight

Let us now consider the work done by the force of gravity. Assume for now that we are close to earth, and that a body of mass $m$ moves on a path from $A$ to $B$ while being subject to the action of its own weight $\vec{P}=-mg\vec{u}_z$. What will the work done by $\vec{P}$ along that path?

$$
\begin{aligned}
W_{A\to B}&= \int_A^B \vec{P}\cdot\text{d}\vec{\ell}\\
& = \int_A^B \begin{pmatrix}0\\0\\-mg\end{pmatrix}\cdot \begin{pmatrix}\text{d} x\\\text{d} y\\ \text{d} z\end{pmatrix}\\
&=  -\int_A^B mg \text{d} z\\
&= -mg(z_B - z_A)
\end{aligned}
$$

Curious! So the work does not depend at all on the choice of path but simply on the difference of altitude. 
Defining the function $V=mgz$, we can simply write

$$W_{A\to B}=V(z_A)-V(z_B)= -\Delta V$$

Just as $E_c$, $V$ can be interpreted as a form of energy, called the potential energy of weight.
It is easy to see that the force $\vec{P}$, can be derived from $V$ as

$$\vec{P}=-\frac{\text{d}V}{\text{d}z}\vec{u}_z$$

Now how to interpret all of this?

![image](../images/weight-energy.png){: width="100%"}
*Left: gravitational potential $V$, Middle: $\frac{\text{d}V}{\text{d}z}$, Right: $\vec{P}$. Done using a simple [code](../codes/energy.py).*

### Gravitational force

$$ \vec{F}_G= -\frac{GmM}{r^2}\vec{u}_r$$

Polar coordinates $(r,\theta,z)$ such that $\text{d}\vec{\ell}=(\text{d}r,r\text{d}\theta,\text{d}z)$.

$$
\begin{aligned}
W_{A\to B}&= \int_A^B -\frac{GmM}{r^2}\vec{u}_r\cdot {\rm d}\vec{\ell}\\
&=\int_A^B -\frac{GmM}{r^2}\begin{pmatrix}1\\0\\0\end{pmatrix}\cdot \begin{pmatrix}\text{d} r\\r\text{d} \theta\\ \text{d} z\end{pmatrix}\\
&=\int_A^B -\frac{GmM}{r^2}\text{d} r\\
&= -GmM \int_A^B r^{-2}\text{d} r\\
&= GmM\left(\frac{1}{r_B} -  \frac{1}{r_A}\right)
\end{aligned}
$$

Introducing again 

$$V=-\frac{GMm}{r},$$

allow us to write 

$$W_{A\to B}=-\Delta V$$

and 

$$F_G= -\frac{\text{d} V}{\text{d} r}\vec{u_r}$$

![image](../images/grav-energy.png){: width="100%"}
*Left: gravitational potential $V$, Middle: $\frac{\text{d}V}{\text{d}z}$, Right: $\vec{F_G}$. (the $\log_{10}$ value of the vector's lenght has been taken). Done using a simple [code](../codes/energy.py).*

### Conservative forces

Some forces, called conservatives, can be derived from a potential energy $V$ as

$$\vec{F}=-\vec{\nabla}V$$

$\vec{\nabla}$ will be further explored in electromagnetism. All you need to know for now, is that it reads, in a Cartesian frame

$$\vec{\nabla}V = \frac{\partial V}{\partial x}\vec{u}_x+ \frac{\partial V}{\partial y}\vec{u}_y+\frac{\partial V}{\partial z}\vec{u}_z$$

Hence it creates a vector $\vec{\nabla}V(x,y,z)$ associated to each point $(x,y,z)$ from a function $V(x,y,z)$. We talk about a vector field. The length of these vectors indicate how strongly $V(x,y,z)$ varies in space, and the direction points towards the increasing values of $V$.

Along a single direction things are simpler:

$$ \vec{F}= -\frac{\partial V}{\partial x}\vec{u}_x $$

For conservative forces, work is independent of the trajectory.

## Energy conservation

They are called conservative as the total energy $E= E_c + V$ is a conserved quantity when they are acting. 

We saw this already as $W=\Delta E_c=-\Delta V$ and hence $\Delta E = \Delta E_c+ \Delta V =0$.
Just to practice a bit, let us demonstrate this in a more general fashion. Considering motion only in one dimension $x$:

$$\begin{aligned}
\frac{\text{d}E}{\text{d}t}&=\frac{\text{d}}{\text{d}t}(E_c+V)\\
&=\frac{\text{d}E_c}{\text{d}t}+ \frac{\text{d}V}{\text{d}t}\\
&=\frac{\text{d}}{\text{d}t}\left(\frac{mv^2}{2}\right)+ \frac{\text{d}x}{\text{d}t}\frac{\text{d}V}{\text{d}x} \qquad \qquad \qquad {\rm chain\,rule}\\
&= \frac{m}{2}\frac{\text{d}v^2}{\text{d}t} - vF \qquad \qquad \qquad \qquad F:=-\text{d}V/\text{d}x\\
&= \frac{m}{2}2v\frac{\text{d}v}{\text{d}t}- vF \qquad \qquad \qquad \qquad  (u^2)'=2u'u\\
&= mva - vF\\
&= vF - vF =0 
\end{aligned}
$$

You can simply show that the proove olds in 3D using partial derivatives.

## Application: Escaping the black hole!

The idea of black holes is already hidden in Newtonian mechanics. 

Indeed, imagine you are in a starship of mass $m$, on the surface of a planet of mass $M$ and radius $R$. If you want to leave the planet, you will have to go fast enough to escape gravity. To do so, you will need a kinetic energy $T$ that is large enough to compensate the gravitational potential energy $V$ of the planet. That is $T \geq -V$.
Using the corresponding mathematical expressions, you have the condition:

$$ \frac{1}{2}mv^2 \geq \frac{GMm}{R}  $$

The minimal speed satisfying this condition $v_l$, is called the escape velocity

$$ v_l = \sqrt{\frac{2GM}{R}}$$

On earth it is $\sim 11$ km/s and this is the speed at which rockets are launched in space. The value will change depending on the ratio $M/R$ of the planet i.e. its density. On the moon it is 2,4 km/s while escaping from the sun would require a speed of 617,5 km/s (even though you would probably have other problems being on the surface of the sun ...).

Now, a natural question arise: what if $v \geq c$, that is, what if light itself could not be fast enough to escape the gravity of the planet?

Such a strange star, called a "black star" would have a radius given by

$$r_s = \frac{2GM}{c^2}$$

The french astronomer Pierre-Simon de Laplace asked himself this question in 1796.

## Applications: astrophysics

If you are curious, you have now the very basics to have a look at some applications to astrophysics in the dedicated section, as [there](../../_cosmo/cosmo/stars-form.md)!
