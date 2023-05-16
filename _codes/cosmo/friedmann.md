---
layout: default
title: Friedmann equations and evolution of the Universe
parent: codes
nav_order: 3
---
# Friedmann equations and evolution of the Universe
## The building blocks of cosmology


Cosmology is a science that studies the universe as a whole, including its origin, nature, evolution and structure.  Promoting cosmology as a branch of natural sciences has been made possible only recently with the discovery of the Universe's expansion by Hubble in 
<a href="https://ui.adsabs.harvard.edu/abs/1926ApJ....64..321H/abstract/">Hubble 1926</a>
[^hubble], showing that it was a dynamic entity (hence it becomes possible to predict its behavior and the discovery of its very first light with the cosmic microwave background (CMB) by <a href="https://ui.adsabs.harvard.edu/abs/1965ApJ...142..419P/abstract/">Penzias and Wilson 1965</a>[^penziaswilson], implying that its history might have had a beginning. As cosmology depends on our current pieces of knowledge, it may evolve in the near future. The **standard cosmological model**, $\Lambda$-CDM  (Cold Dark Matter with a cosmological constant), has been widely adopted since the end of the 1990s and seems to fit current observations. It's important to define a model to question it in the future, testing its limits is one of the roles of current research. The three building blocks of modern cosmology are the following:

1. **Cosmological principle**: The Universe is homogeneous (invariant under translation) and isotropic (invariant under rotation, on large scales, everything we observe is similar in every direction). This principle constrains the possible geometry of our Universe.

2. **Content**: The content of the universe is given by the various species of particle physics and an additional unknown component called cold dark matter (CDM). These species can be sorted into two categories depending on their mass: matter (heavy and cold) and radiation (light and hot). The following are the current proportions of each componant.
	- *Baryonic matter*: Contains standard model particles such as fermions and bosons that can be found [here](% link_ui) : $\sim$ 5 %
	- *Dark matter:* From a non-baryonic origin, composed of massive and cold particles. Currently, its nature is only an hypothesis: $\sim$ 25 %
	- *Radiation:* Relativistic matter with little mass (photons, for example), that has low dynamic influence today but was much more significant in the early Universe: $< 1$  %
	- *Dark Energy:* Energy that fills the Universe and may be responsible for for the "recent" acceleration of its expansion: $\sim$ 70 %

3.  **Gravity**: [General relativity]({% link _codes/cosmo/black-holes.md %}) is used to describe the theory of gravity on large scales and the expansion of the Universe is quantified by the non-zero cosmological constant $\Lambda$, which gives us the most simple model of dark energy.

## The scale factor a(t)

A major turning point for cosmology in the last centuries was the discovery of the expansion of the Universe, which was first modeled by the **Hubble Law** for nearby galaxies: The Universe expands and galaxies are moving away from one another at speed proportional to their distance apart. We define the Hubble constant $H_0$ which is the proportionality factor between the distance and recession speed of galaxies today, as deduced from observations. Its value is still a subject of study and debate among researchers, see <a href="https://ui.adsabs.harvard.edu/abs/2014EPJC...74.3160V/abstract/">Velten et al., 2014</a> [^velten]. We get $v\sim H_0*d$.

Therefore, we try to model a possible contraction or expansion. We aim to understand how the Universe will evolve with time, from its early instants to its far future. To do so, we fix arbitrarily the coordinates of galaxies, considering they're the same independently of the Universe's evolution. We must make the coordinate system evolve instead. This is done by using the **comoving frame** $r, \theta, \phi, t$., which characterizes the distance between two objects, ignoring expansion. Here, comoving time is the time that would be measured by an observer who is moving along with the expansion and does not experience any local time dilation, as time is relative in relativity. The scale factor, represented by $a$, is used to express the distance between galaxies and is the proportionality factor between the comoving distance and real distance, as $d = a(t) \times r$. By definition, it is fixed nowadays as $a_0 = a(t_0)=1$ where $t_0=13.6$ Gigayears.

<a name="fig1"></a>

![scalefactor](../images/scalefactor.png "The scale factor a(t).") 

> Figure 1 : The scale factor a(t). Galaxies’ size does not change as opposed to the distance between them.

Let's define $\dot a = \frac{da}{dt}$ as the Universe's expansion speed. $H=\frac{\dot a}{a}$ is the Hubble parameter which quantifies the evolution. Fundamentally, as we consider the Universe homogeneous and isotropic, it will evolve similarly in every direction, so $a$ is independent of spatial coordinates and is only a function of time.


## The FLRW metric

The principal solution of Einstein's equations satisfying the constraints given by the cosmological principle is described by the FLWR-metric. A metric allows us to depict a distance element in space-time like a 4-Dimensions Pythagorean Theorem : 3 space coordinates and one of time. We have : 

<a name="eq1"></a>


$$
\text{d}s^2 = -c^2\text{d}t^2 + a(t)^2\left( \frac{\text{d}r^2}{1 - kr^2}  + r^2\text{d}\Omega^2\right) 
$$

- $s$ stands as a spacetime interval
- $c$ is the speed of light in vacuum, hereafter we fix it equal to 1,
- $\text{d}\Omega^2 = sin^2\theta  \text{d}  \phi  \text{d} \theta$,
- $a(t)$ is the *scale factor*,
- $k$ stands as *spatial curvature* which can suits the cosmological principle if it's uniform. Indeed, it seems to impose an additional constraint on the geometry of the Universe. It is important to note that curvature does not prevent homogeneity, as the density of matter is the same everywhere. Only the three following cases projected in 2D suit with the cosmological principle.

![3univ](../images/3univ.PNG) 



But actually, observations as <a href="https://ui.adsabs.harvard.edu/abs/2020A%26A...641A...6P/abstract/">Planck Collaboration et al., 2020</a> [^planckcollab] suggest that if the Universe is curved, it is so close to being flat that it appears to be, leading to the common assumption of $k=0$. An interesting point is that this assumption is something debated in cosmology, as we can see e.g.  <a href="hhttps://ui.adsabs.harvard.edu/abs/2020NatAs...4..196D/abstract/">Di Valentino et al., 2020</a> [^divalentino].

## Universe content and perfect fluids

The cosmological principle also gives strong constraints on the possible behavior of the content in the universe. Since no overall preferred direction should exist, the fluids/matter distribution in the universe must itself be homogeneous without any resulting velocity. We talk about perfect fluid. The general form of their stress-energy tensor is given by:

$$ T_{\mu \nu}=\rho u_\mu u_\nu + p (g_{\mu\,\nu}+ u_\mu u_\nu)= {\rm diag}(\rho,p,p,p)
$$

More simply, such a fluid should obey the equation of state:

$$
p=w\rho
$$

One could think about an [ideal gas](% link_ui) where $w = k_B T$. Note that, due to homogeneity, $\rho$ and $p$ have always the same value at every point in space.

The continuity equation $\nabla_\mu T^{\mu \nu} = 0$

equivalent to fluid mechanics (mass) conservation/continuity equation: $\frac{\partial \rho}{\partial t}= - \vec{\nabla}\cdot\vec{j}$

In the FLRW metric, the continuity equation can be written as:
$$
\frac{\partial\rho}{\partial t} + 3 H(1 + w)\rho =0
$$
Integrating it, we obtain the evolution of the density (i.e. the dilution of a given species) through the evolution of the Universe:
$$
\rho(a) =  \rho_0 a^{-3(1+w)}
$$
We will assume that:

- All heavy elements are slow and have a null pressure. $w=0$. This includes matter and dark matter.
- All light and relativistic elements (photons and neutrinos) have $w=1/3$, see [statitical physics](% link_ui).
- The existence of a cosmological constant is equivalent to an energy vacuum of negative pressure with $w=-1$.

So in the case of a cold and heavy matter, we have  $\rho>>P$. The matter density $\rho_m(t)$ can be represented as the sum of baryonic matter $\rho_b(t)$ and cold dark matter $\rho_{cdm}(t)$, which is equal to $\rho_{0,m}a^{-3}$. The amount of matter remains constant as the Universe expands, and it cannot be created or destroyed. Instead, it becomes diluted in all three dimensions of space, hence the $a^{-3}$  which accounts for the same amount of matter occupying a growing volume. As described by $E=mc^2$, the energy density is proportional to the particle density.

In the case of radiation, we have $P\sim \rho$ as photons and neutrinos have zero or negligible mass, so we have $\rho_r(t)=\rho_{0,r}a^{-4}$. The energy is described by $E=\frac{hc}{\lambda}$, energy's density is no longer proportional to particle density. It becomes necessary to note that the densities $\rho_i(t)$ represent the energy ones. Radiation also has associated particles (photons, neutrinos) that dilute in  a-3 and an additional factor because radiation also dilutes in space too. Still, it expands with the Universe too due to the increasing wavelength ($\lambda$), leading to a decrease in energy and additional dilution.


## The Friedmann equation

Cosmology is made by a few fundamental equations. In this part, we interess ourselves at the first Friedmann-Lemaître equation which describes the evolution of the Universe depending on its density, based on the general relativity equations and by application of the cosmological principle :

The fundamental equation of general relativity is Einstein's equation, which can be rewritten as:
$$     R^{\mu \nu} = 8 \pi G \left( T^{\mu \nu} - \frac{1}{2}g^{\mu \nu} T_{\ \sigma}^{\sigma}\right) $$

Inserting FLRW for $g$ and perfect fluids for $T$, one gets the *Friedmann-Lemaître* equation:

$$H^2=\frac{8 \pi G}{3} \sum_i \rho_i + \frac{\Lambda}{3} - \frac{k}{a^2} $$

and the Raychaudaury or acceleration equation:
$$
\frac{\ddot{a}}{a} = H^2 + \dot{H} = \frac{4 \pi G}{3}(\rho+3p).
$$

If you know what the content of the Universe $\rho$ is and its geometry $k$, you are entirely able to predict its evolution.

We can see geometrical elements ($k$ for spatial curvature and $\Lambda$ for the cosmological constant), and we reformulate them as densities : 
$$\rho_{\Lambda}=\frac{\Lambda}{8 \pi G} \text{and}
\rho_k= - \frac{3k}{8 \pi G}$$

So one gets :

- $\rho_r(t)=\rho_{0,r}a^{-4}$
- $\rho_m(t)=\rho_{0,m}a^{-3}$
- $\rho_k(t)=\rho_{0,k}a^{-2}$
- $\rho_{\Lambda}=\rho_{0,\Lambda}$


Rewriting the Friedmann-Lemaître equation treating geometrical terms as densities, we get  :

 $$3H^2= 8\pi G \sum_{i} \rho_i$$

 Introducing critical density $\rho_{c}=\frac{3H_0^2}{8\pi G}$ and the **density parameters**: 
 $$\Omega_i^0=\frac{\rho_{0,i}}{\rho_{0,c}}=\frac{8\pi G \rho_{0,i}}{3H_0^2}$$ 

So we'll use :

- $\Omega_r^0$ the density parameter for radiation
- $\Omega_m^0$ the density parameter for cold matter
- $\Omega_{\Lambda}^0$ the density parameter for the cosmological constant
- $\Omega_k^0$  the density parameter for spatial curvature

Using the continuity equation, we can rewrite the equation as:

<a name="eqfriedmann"></a>

$$\frac{H^2}{H_0^2}=\sum_i \Omega_i a^{-3(1+w_i)}$$

We obtain:

<a name="eq2"></a>


$$H=\frac{\dot a}{a}=H_0\sqrt{\Omega_r^0 a^{-4}+\Omega_m^0 a^{-3}+\Omega_k^0 a^{-2}+\Omega_\Lambda^0}$$

As we fixed $a(t)=1$ today, we get the **closure equation** $\Omega_r^0+\Omega_m^0+\Omega_{\Lambda}^0+\Omega_k^0=1$, which allows us to interpret $\Omega_i^0$ as fractions. We will now numerically integrate this equation to observe the evolution of our Universe depending on its components.

## The evolution of our Universe

<a name="fig2"></a>

![EvolUniv](../images/EvolUniv.png "Modelisation of Friedmann's equation under Python") 

> Figure 2 : Modelisation of Friedmann's equation under Python


  So our goal is to plot the evolution of the scale factor $a(t)$ depending on comoving time for different scenarios. We will accomplish it by integrating the equation using the function *odeint* in the **scipy** python module [^virtanen]. After specifying the time range and the proportion of each component $\Omega_{i}$, we'll define a function containing the equation and another to integrate it. We obtain [Fig. 2](#fig2). It allows us to observe the impact of each component on Universe's evolution. To discuss our program and to introduce a few models, we'll compare our plots to those given by analytical solution.

  *The program can be found here,
 <a href="https://github.com/YoloNomy/Friedmann">here</a>,  using Jupyter Notebook :* 


### Einstein-De-Sitter model :

<a name="fig3"></a>

![radonly](../images/RadOnly.png "Solutions comparison for radiation only") 

> Figure 3 : Solutions comparison for radiation only


<a name="fig4"></a>

![EdS](../images/EdS.png "Solutions comparison for Einstein-De-Sitter model") 

> Figure 4 : Solutions comparison for Einstein-De-Sitter model



In the case where only one component appears in the Friedmann equation [Eq. 2] (#eq2) with $w>-1$, we obtain by integration:
%
$$
t = \frac{1}{\sqrt{\Omega_i}H_0} \int_{0}^a a^{\frac{3}{2} (1+w)-1} \d a =  \frac{2a^{\frac{3}{2}(1+w)}}{3(1+w)H_0\sqrt{\Omega_i}} 
$$

This occurs when only one component exists or when she clearly dominates the other ones. If our Universe is only composed of radiation or matter, we have the analytical solutions:

<a name="eq2a"></a>

$$w=0 \Longrightarrow a(t) = \left(\frac{3 H_0 t \sqrt{\Omega_m}}{2}\right)^{\frac{2}{3}} $$

<a name="eq2b"></a>

$$w=\frac{1}{3} \Longrightarrow a(t) = \left(\frac{4 H_0 t \sqrt{\Omega_r}}{2}\right)^{\frac{1}{2}}$$ 



In both cases, we may report that our Universe would have been born much earlier. Let's take a closer look at the Einstein-De-Sitter Universe [fig. 4](#fig4), corresponding to a case where energy density is equal to the critical one. Proposed in 1932, <a href="https://ui.adsabs.harvard.edu/abs/1932CoMtW...3...51E/abstract/">Einstein and de Sitter, 1932</a> [^einsteindesitter] describe a minimalistic Universe with a Euclidian geometry; that contains only baryonic and dark matter ($\Omega_m$=1). To use this model, the autors recall that the cosmological constant $\Lambda$ was introduced to explain the existence of a finite mean density in a static Universe, but that the case of a dynamic Universe can be achieved without $\Lambda$. This model is called  the *SCDM (Standard Cold Dark Matter)*. However, observations indicate that dark matter density is at least 3 times lower than critical density. Some objects in the observable Universe are much older than the 10 Gyr that the SCDM Model suggests as a birth of the Universe. As a result, this model was quickly abandoned in favor of models with a lower dark matter density, such as $\Lambda$ CDM, which adds a proportion of dark energy.


### $\Lambda$-CDM model :


<a name="fig5"></a>

![stdmodel](../images/stdmodel.png "Solutions comparison for $\Lambda$ CDM model") 
![stdmodelex](../images/stdmodelex.png "Solutions comparison for $\Lambda$ CDM model, exponential zoom") 

> Figure 5 : Solutions comparison for $\Lambda$ CDM model


According to <a href="https://ui.adsabs.harvard.edu/abs/2020A%26A...641A...6P/abstract}/">Planck Collaboration et al., 2020</a> [^planckcollab] , we can consider with the combination of different cosmological instruments that $\Omega_k \simeq 0$, $\Omega_m \simeq 0.3$,$\Omega_\Lambda \simeq 0.7, \Omega_r \simeq 0$. This case corresponds to the most concordant values with the observations for the $\Lambda$CDM model. $\Omega_r$ value is chosen very small, as we know its weakness nowadays but that she was important in the past. Thus, we can take $\Omega_r$=0 to fit with the analytical solution, even if the standard model describes $\Omega_r=10^{-4}$, as we can see on the purple line of [Fig. 2](#fig2). If we consider that the Universe only contains matter and $\Lambda$, we get: 

<a name="eqOlOm"></a>

$a(t)= \left(\frac{\Omega_m}{\Omega_{\Lambda}} \right)^{\frac{1}{3}}\left(\sinh\left(\frac{3}{2}\sqrt{\Omega_{\Lambda}}H_0t\right)\right)^{\frac{3}{2}}$

On [Fig.5](#fig5), we compare it with the numeric solution.
 Graphically, we notice the birth of our Universe to have occurred approximately 14 Gyr ago. We can even extrapolate the evolution of the scale factor ($a$) beyond current observations, which are limited to the Cosmic Microwave Background (CMB). In the beginning, when radiation rules  $a$ rapidly increase, as said by the [Eq. 2a](#eq2a). Radiation is quickly diluted due to the $a^{-4}$ factor. This is followed by an era dominated by matter, as predicted by [Eq. 2b](#eq2b) leading to a more linear expansion. Once matter is sufficiently diluted, the influence of $\Lambda$ becomes dominant. Indeed, it'll never dilute (being a constant). It results in an accelerated expansion of the universe that will continue indefinitely. Expansion isn't stopped anymore and $a$ is faster and faster. The plot illustrates this dominance around 60 Gyr. It allows us  to predict the future of our Universe. At this moment, it will become a De-Sitter Universe.


### De-Sitter model :

<a name="fig6"></a>

![deS](../images/DeS.png "Solutions comparison for De-Sitter model") 

> Figure 6 : Solutions comparison for De-Sitter model



In the scenario where only dark energy sustains, the only contribution to the energy density is the $\Lambda$ one. The Universe is empty of matter, then we have: $$a(t) \propto e^{Hot\sqrt{\Omega_{\Lambda}}}$$
In this model, $a(t)$ increases so rapidly that no event can have an impact on any location that lies beyond the event horizon, defined as $c*H^{-1}$. This phenomenon can also be observed in the case of inflation.

### Hyperbolic Universe :

Until the mid-1990s, we  were considering the hypothesis of the Big Crunch, which wondered if there was enough matter in the Universe to stop its expansion and cause it to contract again. In the case where $\Omega_k < 0$, the spatial curvature is $k=+1$, we're in a hyperbolic space. Depending on parameters, we may observe a crunch of the Universe in the distant future. Friedmann's equation is thus slightly different, as the term under the square root becomes negative. We have to configure our program differently to avoid errors. Therefore, we have : 


<a name="fig7"></a>

![hyperbolic](../images/hyperbolic.png "Modelisation of Friedmann Equation for a Hyperbolic Universe") 

> Figure 7 : Modelisation of Friedmann Equation for a Hyperbolic Universe

## Final modelization : 

It may also be useful to plot the scenarios previously enounced on the same graph for comparison purposes. Depending on parameters, the birth of the Universe can be more or less distant, and its evolution will differ. The future of our Universe is directly impacted by the parameters that determine its density and as a result its expansion, constancy, or crunch.


<a name="fig8"></a>

![complete](../images/complete.png "Modelisation of Friedmann's equation under Python") 


> Figure 8 : Modelization of Friedmann's equation under Python

## Bibliographie 


[^hubble]: Hubble, E. P. (1926). Extragalactic nebulae. ApJ, 64:321–369.

[^penziaswilson]: Penzias, A. A. and Wilson, R. W. (1965). A Measurement of Excess Antenna Temperature at 4080 Mc/s. ApJ, 142:419–421.

[^velten]: Velten, H. E. S., vom Marttens, R. F., and Zimdahl, W. (2014). Aspects of the cosmological “coincidence problem”. European Physical Journal C, 74:3160.

[^planckcollab]: Planck Collaboration, Aghanim, N., Akrami, Y., Ashdown, M., Aumont, J., Baccigalupi, C., Ballardini, M., Banday, A. J., Barreiro, R. B., Bartolo, N., Basak, S., Battye, R., Benabed, K., Bernard, J. P., Bersanelli, M., Bielewicz, P., Bock, J. J., Bond, J. R., Borrill, J., Bouchet, F. R., Boulanger, F., Bucher, M., Burigana, C., Butler, R. C., Calabrese, E., Cardoso, J. F., Carron, J., Challinor, A., Chiang, H. C., Chluba, J., Colombo, L. P. L.,Combet, C., Contreras, D., Crill, B. P., Cuttaia, F., de Bernardis, P., de Zotti, G., Delabrouille, J., Delouis, J. M., Di
Valentino, E., Diego, J. M., Dor ́e, O., Douspis, M., Ducout, A., Dupac, X., Dusini, S., Efstathiou, G., Elsner, F., Enßlin, T. A., Eriksen, H. K., Fantaye, Y., Farhang, M., Fergusson, J., Fernandez-Cobos, R., Finelli, F., Forastieri, F., Frailis, M., Fraisse, A. A., Franceschi, E., Frolov, A., Galeotta, S., Galli, S., Ganga, K., G ́enova-Santos, R. T., Gerbino, M., Ghosh, T., Gonz ́alez-Nuevo, J., G ́orski, K. M., Gratton, S., Gruppuso, A., Gudmundsson, J. E., Hamann, J., Handley, W., Hansen, F. K., Herranz, D., Hildebrandt, S. R., Hivon, E., Huang, Z., Jaffe, A. H., Jones, W. C., Karakci, A., Keih ̈anen, E., Keskitalo, R., Kiiveri, K., Kim, J., Kisner, T. S., Knox, L., Krachmalnicoff, N., Kunz, M., Kurki-Suonio, H., Lagache,
G., Lamarre, J. M., Lasenby, A., Lattanzi, M., Lawrence, C. R., Le Jeune, M., Lemos, P., Lesgourgues, J., Levrier, F., Lewis, A., Liguori, M., Lilje, P. B., Lilley, M., Lindholm, V., L ́opez-Caniego, M., Lubin, P. M., Ma, Y. Z., Mac ́ıas-P ́erez,
J. F., Maggio, G., Maino, D., Mandolesi, N., Mangilli, A., Marcos-Caballero, A., Maris, M., Martin, P. G., Martinelli, M., Mart ́ınez-Gonz ́alez, E., Matarrese, S., Mauri, N., McEwen, J. D., Meinhold, P. R., Melchiorri, A., Mennella, A., Migliaccio, M., Millea, M., Mitra, S., Miville-Deschˆenes, M. A., Molinari, D., Montier, L., Morgante, G., Moss, A., Natoli, P., Nørgaard-Nielsen, H. U., Pagano, L., Paoletti, D., Partridge, B., Patanchon, G., Peiris, H. V., Perrotta, F., Pettorino, V., Piacentini, F., Polastri, L., Polenta, G., Puget, J. L., Rachen, J. P., Reinecke, M., Remazeilles, M., Renzi, A., Rocha, G., Rosset, C., Roudier, G., Rubi ̃no-Mart ́ın, J. A., Ruiz-Granados, B., Salvati, L., Sandri, M., Savelainen, M., Scott, D., Shellard, E. P. S., Sirignano, C., Sirri, G., Spencer, L. D., Sunyaev, R., Suur-Uski, A. S., Tauber, J. A.,Tavagnacco, D., Tenti, M., Toffolatti, L., Tomasi, M., Trombetti, T., Valenziano, L., Valiviita, J., Van Tent, B., Vibert,
L., Vielva, P., Villa, F., Vittorio, N., Wandelt, B. D., Wehus, I. K., White, M., White, S. D. M., Zacchei, A., and Zonca,A. (2020). Planck 2018 results. VI. Cosmological parameters. A&A, 641:A6.


[^divalentino]:Di Valentino, E., Melchiorri, A., and Silk, J. (2020). Planck evidence for a closed Universe and a possible crisis for cosmology. Nature Astronomy, 4:196–203.

[^virtanen]: Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., Burovski,E., Peterson, P., Weckesser, W., Bright, J., van der Walt, S. J., Brett, M., Wilson, J., Millman, K. J., Mayorov, N.,Nelson, A. R. J., Jones, E., Kern, R., Larson, E., Carey, C. J., Polat,  ̇I., Feng, Y., Moore, E. W., VanderPlas, J., Laxalde, D., Perktold, J., Cimrman, R., Henriksen, I., Quintero, E. A., Harris, C. R., Archibald, A. M., Ribeiro, A. H., Pedregosa,F., van Mulbregt, P., and SciPy 1.0 Contributors (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computingin Python. Nature Methods, 17:261–272.

[^einsteindesitter]: Einstein, A. and de Sitter, W. (1932). On the Relation between the Expansion and the Mean Density of the Universe. Contributions from the Mount Wilson Observatory, 3:51–52.



> Written by Jehanne Delhomelle, Léo Vacher, 2023