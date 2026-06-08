---
layout: default
title: Lagrangian mechanics
parent: Analytical 
nav_order: 2
--- 


## Euler-Lagrange equations

$$S = \int_{t_i}^{t_f} L(q,\dot{q}) \text{d}t$$

$$\frac{\text{d}}{\text{d}t}\frac{\partial L}{\partial \dot{q}}= \frac{\partial L}{\partial q}$$

<details markdown="1">
  <summary><strong>Proof</strong></summary>

$$\delta S = S(q,\dot{q}) - S(q+\delta q , \dot{q}+\delta(\dot{q}))=0$$

where $\delta q = \epsilon(t)$ is a function of time.

The Lagrangian transforms as:

$$L(q+\delta q , \dot{q}+\delta(\dot{q})) = L(q,\dot{q}) + \delta L $$

$$\delta L = \frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial \dot{q}}\delta(\dot{q})$$

We assume the following:

$$\delta(\dot{q})= \dot{\delta q}$$

$$\delta q(t_i)= \delta q(t_f)=0$$

Now, we can compute:

$$\begin{align}
\delta S &= \int_{t_1}^{t_2} \delta L\\
&= \int_{t_1}^{t_2}  \frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial \dot{q}}(\dot{\delta q})\text{d}t
\end{align}$$

We can integrate by part, (i.e. integrate the product rule). We recall here that:

$$\frac{\text{d}}{\text{d}t}(uv) = u\frac{\text{d}v}{\text{d}t} + \frac{\text{d}v}{\text{d}t}u $$

Thus:

$$ [uv]_{t_a}^{t_b} = \int_{t_a}^{t_b} u\frac{\text{d}v}{\text{d}t} \text{d}t +  \int_{t_a}^{t_b}\frac{\text{d}v}{\text{d}t}u \text{d}t$$

and 

$$\int_{t_a}^{t_b} u\frac{\text{d}v}{\text{d}t} \text{d}t = [uv]_{t_a}^{t_b} - \int_{t_a}^{t_b}\frac{\text{d}v}{\text{d}t}u \text{d}t $$

Applied here with $u = \frac{\partial L}{\partial \dot{q}} $ $v= \delta q$, we obtain

$$\begin{align}
\delta S &= \int_{t_1}^{t_2}  \frac{\partial L}{\partial q}\delta q \text{d}t + \int_{t_1}^{t_2} \frac{\partial L}{\partial \dot{q}}(\dot{\delta q})\text{d}t\\
&= \int_{t_1}^{t_2}  \frac{\partial L}{\partial q}\delta q \text{d}t + [\frac{\partial L}{\partial \dot{q}} \delta q]_{t_1}^{t_2} - \int_{t_1}^{t_2} \frac{\text{d}}{\text{d}t}\frac{\partial L}{\partial \dot{q}}\delta q\text{d}t\\
&= [\frac{\partial L}{\partial \dot{q}} \delta q]_{t_1}^{t_2} + \int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}- \frac{\partial L}{\partial \dot{q}}\right)\delta q\text{d}t\\
&= \int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}- \frac{\partial L}{\partial \dot{q}}\right)\delta q\text{d}t =0
\end{align}$$

Where we used the boundary conditions ($\delta q (t_1) = \delta q (t_2)=0$).

We use the theorem:

If

$$\int f(t)g(t) \text{d}t =0  f(t) =0$$

for all values of $g(t)$, then $f(t)=0$$.

Hence, we find the Euler-Lagrange equations:

$$\frac{\partial L}{\partial q}- \frac{\partial L}{\partial \dot{q}}=0$$ 


</details>