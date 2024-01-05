---
layout: default
title: Work and Energy
parent: Newton
nav_order: 2
---
# Work and Energy: integrals and the dot product

The apprently very practical notion of *work*, defining how "efficient" a force is to move a body, will lead us to the very abstract notion of *energy*, which is one of the most important notion of all physics.

## "Multiplying vectors" : the dot product

## Work

$$
W_{AB} = \vec{F}\cdot\vec{AB}  
$$

$$
\delta W=\vec{F}\cdot\text{d}\vec{\ell}
$$

## Kinetic energy

You might know that the kinetic energy of a body going at velocity $v$ is given by the "famous" formula:

$$E=\frac{1}{2}mv^2$$

Let us now understand why and where this comes from. It actually is nothing else but work!

To do so, let us consider what is the total work made by all the forces acting on a body during it's motion from a point $A$ to a point $B$:

$$
\begin{aligned}
W= &\int_A^B\delta W=\int_A^B\sum\vec{F}\cdot\text{d}\vec{\ell}
\end{aligned}
$$

Now, we can use Newton's second law defining what a force is as $\sum\vec{F}=m\vec{a}$ such that

$$
\begin{aligned}
W= &\int_A^Bm\vec{a}\cdot\text{d}\vec{\ell}\\
=&m\int_A^B\frac{\text{d}\vec{v}}{\text{d}t}\cdot\text{d}\vec{\ell}
\end{aligned}
$$

In which we remembered the definition of acceleration, and put the constant $m$ in front of the integral. Now, the velocity vector $\vec{v}$ is, by definition, the distance $\text{d}\vec{\ell}$ divided by the time it took to travel this distance $\text{d} t$, such that we can simply write

$$ \vec{v}=\frac{\text{d}\vec{\ell}}{\text{d} t} \Rightarrow \text{d}\vec{\ell}= \vec{v}\,\text{d} t$$

Putting this in our calculation for the work, we get

$$
\begin{aligned}
W= &\int_A^Bm\vec{a}\cdot\text{d}\vec{\ell}\\
=&m\int_{t_A}^{t_B}\frac{\text{d}\vec{v}}{\text{d}t}\cdot\vec{v}\,\text{d} t\\
=&m\int_{v_A}^{v_B}\text{d}\vec{v}\cdot\vec{v}
\end{aligned}
$$

In which we "simplified" the $\text{d} t$ as is allowed by the rules of derivatives. Now, there are several ways to think about this integral, but let us detail it fully to be sure to understand as we are not yet familiar with the properties of the dot product  (even though this is might be a bit overkill!). To do so, we compute completly the dot product by decomposing the vectors in a coordinate basis $(x,y,z)$, such that $\vec{v}=(v_x,v_y,v_z)$ and hence $\text{d}\vec{v}=(\text{d}v_x,\text{d}v_y,\text{d}v_z)$. As such, using the rule of the dot product, we obtain

$$
\begin{aligned}
W= m\int_{v_A}^{v_B}v_x\text{d}v_x+ v_y\text{d}v_y+ v_z\text{d}v_z
\end{aligned}
$$

which we can split in three integrals

$$
\begin{aligned}
W= 
&=m\left(\int_{v_{x,A}}^{v_{x,B}}v_x\text{d}v_x+ \int_{v_{y,A}}^{v_{y,B}}v_y\text{d}v_y+ \int_{v_{z,A}}^{v_{z,B}}v_z\text{d}v_z\right)
\end{aligned}
$$

Now things are much easier than what you might think! These are just integrals of the type $\int_A^B x \,\text{d}x$ which each gives $[x^2/2]_A^B$. You can find this either by remembering the simple rule $(x^2)'=2x$ and that the integral is sort of the "opposite" of the derivate, or if you know by heart the very important and always useful rule for integrals $\int_A^Bx^n\,\text{d}x=[x^{n+1}/(n+1)]_A^B$. Computing the integrals in the expression of $W$, we thus obtain

$$
\begin{aligned}
W= 
&=m \left([v_x^2/2]_A^B+ [v_y^2/2]_A^B+ [v_z^2/2]_A^B\right)
\end{aligned}
$$

in which we recognize the dot product of $\vec{v}$ with itself $\vec{v}^2=\vec{v}\cdot\vec{v}=v_x^2+v_y^2+v_z^2$. After all these derivations, we can find that $W$ is simply given by

$$
\begin{aligned}
W= 
&=\frac{m}{2}[\vec{v}^2]_A^B
\end{aligned}
$$

## Potential energy and gradient


## Energy conservation

$W=\Delta E_c=-\Delta V$ and hence $\Delta E = \Delta E_c+ \Delta V =0$. Just to practice a bit, let us demonstrate this in a more general fashion. Considering motion only in one dimension $x$:

$$\begin{aligned}
\frac{\text{d}E}{\text{d}t}&=\frac{\text{d}}{\text{d}t}(E_c+V)\\
&=\frac{\text{d}E_c}{\text{d}t}+ \frac{\text{d}V}{\text{d}t}\\
&=\frac{\text{d}}{\text{d}t}\left(\frac{mv^2}{2}\right)+ \frac{\text{d}x}{\text{d}t}\frac{\text{d}V}{\text{d}x} \qquad \qquad \qquad {\rm chain\,rule}\\
&= \frac{m}{2}\frac{\text{d}v^2}{\text{d}t} - vF\\
&= \frac{m}{2}2v\frac{\text{d}v}{\text{d}t}- vF \qquad \qquad \qquad \qquad  (u^2)'=2u'u\\
&= mva - vF\\
&= vF - vF =0
\end{aligned}
$$

You can simply show that the proove olds in 3D using partial derivatives.

## Application: Escaping the black hole!

## Application: Forming a star