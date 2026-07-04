---
layout: default
title: Scalar fields
parent: cosmo
---

### Why scalar fields?


Scalar field models propose to add one or several new dynamical entities given by a frame independent value of a real or complex number at every point of space-time. They are very common in the cosmological literature and are so often invoked because:
- They are easy to implement consistently without breaking the general covariance of the theory. As such, they allow to build phenomenological "toy models" providing simple solutions to most of the cosmological puzzles as the $H_0$ tension, dark matter, inflation and so on. From the point of view of effective field theory (EFT), they can also reproduce the effective behavior of a more complicated underlying dynamics. They thus provides both simple and consistent modeling in order to seek for effects going beyond the SM, as varying dark energy, modification of gravity or possible variations of the fundamental constants of nature. 
- Due to Lovelock theorem, we know adding new fields represent one of our only options to go beyond GR. Moreover, multiple higher order terms modifications of the action of gravity. can be shown to be equivalent to the addition of one or several scalar fields coupled to gravity. Furthermore, the addition of new compact dimensions to space-time gives rise to scalar degrees of freedom in the higher dimensional metric. Overall, multiple phenomenological routes beyond GR thus lead to scalar fields. 
- Furthermore, scalar fields appear as theoretical necessities in multiple high energy physics models beyond the SM as Kaluza-Klein or string theory. They indeed appear in dimensional compactification (scalar degrees of freedom appearing in dimensional reduction are called the radions and moduli fields in Kaluza-Klein and string theory respectively) but also as fundamental fields like members of the string spectra (as the string dilaton). As such, fundamental routes from deeper principles tend also to lead to the existence of scalar fields.
- We know for a fact that they can be part of nature's building blocks as proved by the discovery of the Higgs boson, which is itself a complex scalar field.

However, if the presence of such a field were ever detected on cosmological scales, a change of high energy physics paradigm would have to be considered, in order to understand where this new entity could fit in the realm of gauge theories over curved space-time, as well as how this new field can remain yet undetected in local/particle physics experiments.

### Field Lagrangian

If one wants to add a new entity present in the cosmological space-time, the most rigorous way to do so is to introduce it at the Lagrangian level.
The standard Lagrangian density for a real scalar field in flat space-time is

$$\boxed{\mathcal{L}_\phi = -\frac{1}{2}\partial_\mu \phi \partial^\mu \phi - V(\phi)}$$

which is the standard difference between a kinetic and a potential term. The expression for the kinetic term can be justified in multiple ways. It is the most general term that can be included being Lorentz invariant and is second order in derivatives. The minus sign in front of the kinetic term is a signature of our metric choice $(-,+,+,+)$, common in general relativity but uncommon for the particle physicist. This Lagrangian can also be derived by considering coupled harmonic oscillators and taking the continum and covariant limit, or by trying to obtain a relativistic form for the Schrödinger equation.

Its generalisation to curve space-time is straightforward. The standard procedure is to replace standard derivatives $\partial_\mu$ with covariant derivatives $\nabla_\mu$. However, these have no impact on scalar fields so $\mathcal{L}$ remains unchanged.

The action is given by the integral with the volume form:

$$\boxed{S_\phi = \int \sqrt{-|g|} \mathcal{L}_\phi \text{d}^4x}$$

where $\vert g\vert$ is the determinant of the metric. 

## Stress-energy in flat and curved space-time

Now, we can wonder what would be the energy density and the pressure that such a field would exert on cosmological scales. These two ingredients are crucial, as we saw that they are appearing in the Friedman equations, driving the time evolution of the scale factor. As for every other component of the universe, the pressure and energy density are encoded in the **stress energy tensor** of the field.

As we discussed already, the stress-energy-tensor is the Noether current associated with the invariance of $\mathcal{L}$ under space-time translations, that is a change $x^\mu \to x^\mu + \epsilon^\mu$. It is expressed as

$$(T^{\phi})^{\mu}_{\,\nu} = \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}\partial_\nu \phi - \delta^{\mu}_{\nu}\mathcal{L}$$

In General relativity, it is defined alternatively as:

$$T^{\phi}_{\mu\nu} = \frac{2}{\sqrt{-|g|}}\frac{\delta S}{\delta g^{\mu\nu}}$$

Both expression lead

$$\boxed{T^{\phi}_{\mu\nu}= \partial_\mu \phi \partial_\nu \phi + \delta_{\mu\nu}\left(\frac{1}{2}g^{\rho \sigma}\partial_\rho \phi \partial_\nu \phi + V(\phi)\right)}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>

From this we find that, if the field is isotropic:

$$
\boxed{
  \begin{align}
  \rho_\phi &= \frac{1}{2}\dot{\phi}^2 + V(\phi)\\
  p_\phi &= \frac{1}{2}\dot{\phi}^2 - V(\phi)
\end{align}
}
$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

</details>


## Equations of motion: 

Applying Euler-Lagrange to the Lagrangian gives the **Klein-Gordon** equation describing the evolution of the field with the expansion

$$\boxed{\partial_\mu\partial^\mu \phi + \partial_\mu\ln\left(\omega\right)\partial^\mu \phi + \omega \partial_\mu(g^{\mu\nu})\partial_\nu \phi = \frac{\partial V}{\partial \phi}}$$

where we noted the **volume form** $\omega=\sqrt{-\vert g\vert}$ and the **d'Alembertian** $\partial_\mu\partial^\mu \phi$ is sometimes noted $\Box \phi$.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

The Euler-Lagrange equation extremizing the action for fields in curved space-time is:

$$\partial_\mu \left(\frac{\partial (\omega\mathcal{L})}{\partial (\partial_\mu \phi)}\right) = \frac{\partial (\omega\mathcal{L})}{\partial \phi}$$

where, as a reminder, we defined $\omega=\sqrt{-\vert g\vert}$.

Now, in our case, we have for the left-hand side:

$$
\partial_\mu \left(\frac{\partial (\omega\mathcal{L})}{\partial (\partial_\mu \phi)}\right) = -\frac{1}{2}\partial_\mu \left(\omega\frac{\partial( \partial_\nu \phi \partial^\nu \phi)}{\partial (\partial_\mu \phi)}\right) 
$$

where we renamed the dummy summation index $\nu$ to distinguish it from the derivative index $\mu$. Now, the product rules gives: 

$$
\frac{\partial(\partial_\nu \phi \partial^\nu \phi)}{\partial (\partial_\mu \phi)} = \frac{\partial (\partial_\nu \phi)}{\partial (\partial_\mu \phi)}\partial^\nu \phi + \partial_\nu \phi \frac{\partial(\partial^\nu \phi)}{\partial (\partial_\mu \phi)} 
$$

We can then use the metric to rewrite $\partial^\nu \phi = g^{\nu \sigma}\partial_\sigma\phi$. We get:

$$
\begin{align}
&\frac{\partial(\partial_\nu \phi)}{\partial     (\partial_\mu \phi)}\partial^\nu \phi + \partial_\nu \phi \frac{\partial(\partial^\nu \phi)}{\partial (\partial_\mu \phi)}  \\
&=\frac{\partial(\partial_\nu \phi)}{\partial (\partial_\mu \phi)}\partial^\nu \phi + \partial_\nu \phi \frac{\partial(g^{\nu \sigma}\partial_\sigma\phi)}{\partial (\partial_\mu \phi)}  \\
&=  \delta_{\nu\mu} \partial^\nu \phi + \partial_\nu\phi g^{\nu \sigma} \delta_{\sigma\mu} \\
&= \delta_{\nu,\mu} \partial^\nu \phi + \partial_\nu\phi g^{\nu \sigma} \delta_{\sigma\mu} \\
&= \partial^\mu \phi + \partial^\mu\phi\\
&= 2 \partial^\mu \phi
\end{align}
$$

Putting this back in our original expression for the left-hand side of the Euler-Lagrange equation, we get:

$$
\begin{align}
\partial_\mu \left(\frac{\partial (\omega\mathcal{L})}{\partial (\partial_\mu \phi)}\right) &= -\frac{1}{2}\partial_\mu \left(\omega\frac{\partial( \partial_\nu \phi \partial^\nu \phi)}{\partial (\partial_\mu \phi)}\right) \\
&= -\partial_\mu \left(\omega g^{\mu\nu} \partial_\nu \phi\right)\\
&=  -\left(\partial_\mu(\omega)\partial^\mu \phi + \omega \partial_\mu\partial^\mu \phi + \omega\partial_\mu(g^{\mu\nu})\partial_\nu \phi\right)
\end{align}
$$

Now, the right-hand side is simply:


$$\frac{\partial (\omega\mathcal{L})}{\partial \phi} = -\omega\frac{\partial V}{\partial \phi}$$

as $V$ is the only part of $\mathcal{L}$ that depends on $\phi$ itself. Equating both sides in the Euler-Lagrange equation, we get:

$$ 
\begin{align}
\partial_\mu(\omega)\partial^\mu \phi + \omega \partial_\mu\partial^\mu \phi + \omega\partial_\mu(g^{\mu\nu})\partial_\nu \phi & = \omega\frac{\partial V}{\partial \phi}\\
\partial_\mu\partial^\mu \phi + \frac{1}{\omega}\partial_\mu(\omega)\partial^\mu \phi+ \partial_\mu(g^{\mu\nu})\partial_\nu \phi   &= \frac{\partial V}{\partial \phi} \\
\partial_\mu\partial^\mu \phi + \partial_\mu\ln\left(\omega\right)\partial^\mu \phi + \partial_\mu(g^{\mu\nu})\partial_\nu \phi  &= \frac{\partial V}{\partial \phi}
\end{align}
$$


</details>

In flat space-time, the metric is the Minkowski metric ($g=\eta$) and hence $\mu=1$ and the whole term is zero. However, if we consider the FLRW metric and a field that is isotropic $\phi(t)$, we get:

$$\boxed{\ddot{\phi} + 3H \dot{\phi} = -\frac{\partial V}{\partial \phi}}$$

where dots denote time derivatives and $H=\dot{a}/a = \text{d}\ln(a)/\text{d}t$.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

We consider now a [FLRW space-time](FLRW.md) in some co-moving coordinates, such that the field can be expressed locally as a function $\phi(t,x,y,z)$ and the metric as $g_{\mu\nu}=\text{diag}(-1,a^2,a^2,a^2)$ and $g^{\mu\nu}=\text{diag}(-1,1/a^2,1/a^2,1/a^2)$. If we now assume that the field is isotropic (or that its variations in space are so small that they can be neglected) it is represented by a function of time only, $\phi(t)$. Hence 

$$\partial_\mu\partial^\mu\phi = g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = -(\partial_t)^2\phi + (\partial_x/a)^2\phi + (\partial_y/a)^2\phi + (\partial_z/a)^2\phi = -(\partial_t)^2\phi = -\ddot{\phi}.$$

Furthermore, in the FLRW metric $\vert-g \vert=-a^6$ (recall that the determinant of a diagonal matrix is just the product of all of its entries). Hence, $\omega = \sqrt{-\vert g \vert}= a^3$ and $\ln(\omega)=3\ln(a)$. Thus 

$$\partial_\mu\ln(\omega)\partial^\mu \phi=3 \partial_t\ln(a)g^{00}\dot{\phi}= -3H\dot{\phi}.$$

Furthermore, 

$$\partial_\mu(g^{\mu\nu})\partial_\nu \phi = \partial_t(-1)\partial_t\phi + \partial_x\left(\frac{1}{a^2(t)}\right)\partial_x\phi + \partial_y\left(\frac{1}{a^2(t)}\right)\partial_y\phi + \partial_z\left(\frac{1}{a^2(t)}\right)\partial_z\phi =0$$

Putting everything together, we get:

$$\partial_\mu\partial^\mu \phi + \partial_\mu\ln\left(\omega\right)\partial^\mu \phi + \partial_\mu(g^{\mu\nu})\partial_\nu \phi = -\ddot{\phi} - 3H \dot{\phi}$$

which in the Klein-Gordon equation gives

$$\begin{align}
-\ddot{\phi} - 3H \dot{\phi}&= \frac{\partial V}{\partial \phi}\\
 \ddot{\phi} + 3H \dot{\phi} &= -\frac{\partial V}{\partial \phi}
\end{align}
$$

</details>

The same result can be reached from the continuity equation using the expression for $\rho_\phi$ and $P_\phi$ or using the two Friedmann equations.

<details markdown="1">
  <summary><strong>Deriving the Klein-Gordon equation from the continuity equation</strong></summary>

In a [previous lecture](./thermo_cosmo.md), we saw that the energy density $\rho$ of a component evolved in the FLRW metric as:

$$\dot{\rho} + 3H(1+w)\rho = 0$$

For the scalar field $\rho_\phi = \dot{\phi}^2/2 + V$ and thus

$$\begin{align}
1+w &= 1+\frac{p_\phi}{\rho_\phi}\\
&= 1 + \frac{\dot{\phi}^2/2 - V}{\dot{\phi}^2/2 + V}\\
&= \frac{\dot{\phi}^2/2 + V}{\dot{\phi}^2/2 + V} + \frac{\dot{\phi}/2 - V}{\dot{\phi}^2/2 + V}\\
&= \frac{\dot{\phi}^2}{\dot{\phi}^2/2 + V}
\end{align}
$$

As such, the continuity equation for a field is:

$$
\begin{align}
&\dot{\rho} + 3H(1+w)\rho = 0\\
& \frac{\text{d}}{\text{d}t}\left(\dot{\phi}^2/2 + V\right) + 3H \frac{\dot{\phi}^2}{\dot{\phi}^2/2 + V} \left(\dot{\phi}^2/2 + V\right)=0\\
& 2\dot{\phi}\ddot{\phi}/2 + \dot{V}   3H \dot{\phi}^2 = 0\\
& \dot{\phi}\ddot{\phi} + \frac{\partial V}{\partial \phi}\dot{\phi} + 3H \dot{\phi}^2 =0\\
&\ddot{\phi} + 3H \dot{\phi} = -\frac{\partial V}{\partial \phi}
\end{align}
$$

</details>


<details markdown="1">
  <summary><strong>Deriving the Klein-Gordon equation from the Friedmann equations</strong></summary>

The first Friedmann equation is

$$H^2 = \frac{8\pi G}{3}\rho $$

in the case where a scalar field dominates the expansion, we get

$$H^2 = \frac{8\pi G}{3}(\dot{\phi}^2/2+V)$$

Taking the time derivative of this equation, we obtain

$$2H\dot{H} = \frac{8\pi G}{3}(\dot{\phi}\ddot{\phi}+\frac{\partial V}{\partial \phi}\dot{\phi})$$

Furthermore, the acceleration equation is

$$ \dot{H} + H^2 = -\frac{4\pi G}{3}(\rho + 3p)$$

which, for a scalar field alone is:

$$\begin{align}
\dot{H} + H^2 &= -\frac{4\pi G}{3}(\dot{\phi}^2/2+V + 3\dot{\phi}^2/2 - 3V)\\
&= -\frac{4\pi G}{3}(2\dot{\phi}^2 -2V)\\
&= -\frac{8\pi G}{3}(\dot{\phi}^2 -V) \\
\end{align}
$$

and thus

$$\begin{align}
\dot{H}  &= -\frac{8\pi G}{3}(\dot{\phi}^2 -V) - H^2\\
&= -\frac{8\pi G}{3}(\dot{\phi}^2 -V) - \frac{8\pi G}{3}(\dot{\phi}^2/2+V)\\
& = -\frac{8\pi G}{3} \frac{3}{2}  \dot{\phi}^2\\
& = -4\pi G \dot{\phi}^2
\end{align}
$$

Inserting this in the left hand-side of our previous derivation, we obtain

$$\begin{align}
2\dot{H}H &= \frac{8\pi G}{3}(\dot{\phi}\ddot{\phi}+\frac{\partial V}{\partial \phi}\dot{\phi})\\
- 8\pi G H\dot{\phi}^2 &= \frac{8\pi G}{3}(\dot{\phi}\ddot{\phi}+\frac{\partial V}{\partial \phi}\dot{\phi})\\
-3H\dot{\phi} &= \ddot{\phi} + \frac{\partial V}{\partial \phi}\dot{\phi}
\end{align}
$$ 

Which is our Klein-Gordon equation!

</details>

## Potentials

### Mass

The potential $V(\phi)$ can have different forms depending of the kind-of field.

$$V_m = \frac{1}{2}m^2\phi^2$$

$$\boxed{m^2 = \frac{\partial^2 V}{\partial \phi^2}}$$
