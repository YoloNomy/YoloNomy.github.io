---
layout: default
title: Boltzmann equations
parent: cosmo
nav_order: 1
---


## Evolution of the distribution function

Any function (observable) on [phase space](../../_thermo/statistical/phasespace.md) evolves in time with the time evolution operator, or the **Liouville operator**:

$$\frac{\text{d}}{\text{d}t} = \frac{\partial}{\partial t} + \frac{\partial q}{\partial t} \frac{\partial}{\partial q} +  \frac{\partial p}{\partial t}\frac{\partial}{\partial p}$$

<details markdown="1">
  <summary><strong>A sidenote on the Liouville operator</strong></summary>

The time evolution operator, or Liouville operator is given by the Poisson bracket with the Hamiltonian:

$$\frac{\text{d}}{\text{d}t} = \{.,H\} $$

Using Hamilton's equation, we can rewrite:

$$
\begin{align}
\frac{\text{d}}{\text{d}t} 
&= \frac{\partial}{\partial t} + \frac{\partial q}{\partial t} \frac{\partial}{\partial q} +  \frac{\partial p}{\partial t}\frac{\partial}{\partial p}\\
&= \frac{\partial}{\partial t} + \frac{\partial H}{\partial p} \frac{\partial}{\partial q} -  \frac{\partial H}{\partial q}\frac{\partial}{\partial p}\\
\end{align}
$$

Where we recognize the Hamilton vector:

$$\frac{\text{d}}{\text{d}t} =\{.,H\}=X_H$$

</details>

On the cosmological space-time, we note the coordinate $q=x$. Consider now the distribution function $f(x,p,t)$ that we consider in our [previous class](./thermo_cosmo.md). We now allow it to depend on cosmic time $t$ and try to understand how it will evolve and change through cosmic history.

We get 

$$\begin{align}
\frac{\text{d}f}{\text{d}t} &= \frac{\partial f}{\partial t} + \frac{\partial x}{\partial t} \frac{ \partial f}{\partial x} +  \frac{\partial p}{\partial t}\frac{\partial f}{\partial p} \\
&= \frac{\partial f}{\partial t} + v\cdot \frac{ \partial f}{\partial x} +  F\cdot\frac{\partial f}{\partial p}  
\end{align}$$


Where we identified $F= \partial p /\partial t$ as a force and $v=\partial x /\partial t$ as a velocity. If we assume the universe isotropic then $\partial f/\partial x=0$, hence the velocity term disappears. Furthermore, we saw in our class on the [FLRW metric](./FLRW.md) that the geodesic equation gives $\partial p/\partial t= -Hp$, and hence:

$$\boxed{\frac{\partial f}{\partial t} - Hp \frac{\partial f}{\partial p} = \mathcal{C}}$$

$\mathcal{C}$ is the *interaction term*. It can couple different modes $\vec{p}$ and $\vec{p}'$ and thus change the shape of the energy distribution.
