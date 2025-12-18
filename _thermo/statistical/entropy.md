---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---

# The statistical entropy

## Statistical physics, microstates and macrostates

The idea laying behind statistical mechanics will be to explain the observed behavior of macroscopic systems as the result of a large number underlying microscopic subsystems. For exemple, we will be able to retrieve quite elegantly the ideal gas law, which was central in our first thermodynamics class, by interpreting a volume of gas as being composed of a large number of free bouncing microscopic particles.

Statistical mechanics lies on the distinction between macrostates and microstates:

- The **macrostate** of a system corresponds to the state as described in classical thermodynamics. It is what you would measure about the system here and now: its temperature, pressure, volume etc

- The **microstate** of a system is the complete description of the system in term of its microscopic constituents.

As such, **several *microstates* can correspond to the same *macrostate***: you can think of an infinite amount of different ways to put particles of gas in a box which will give you the same measured pressure, temperature and volume. As time passes, the system will explore different microstates while remaining in the same macrostate.

Each microstate $i$ can be associated with a probability of occuring $p_i$. The challenge of statistical mechanics is to find the right way to estimate this probability. This will be done by  maximizing a quantity, known as the statistical entropy $S$. We will see that $S$ can be identified with the quantity appearing in the second principle of thermodynamics discussed in the [thermodynamics class](../../thermo/secondprinciple/). The entropy can easily be treated as one of the most profound and most subtle concept of modern physics.

## Preliminary review of basic probability theory for the discrete case and the challenge of statistical mechanics
   
As a very simple reminder, recall that for a discrete set of possible events, which we will label by the index $i$, the probabilties represent the "chance" for this event to occur, expressed in as fractions of one ($0 \leq p_i \leq 1$). For exemple, considering rolling a dice, the possible results would be $i\in \Omega = \{1,2,3,4,5,6}$ and $p_i = 1/6 \simeq 0.1667$, for each $i$ (in a more fancy way, we can call $\Omega$  can say that $p$, is a function, and more precisely as a measure, such that $p:\Omega \to [0,1]$, $i \to p_i$).

Probability is also a highly subtle concept, which can be defined and introduced in a great number of way, with different level of abstraction and fundamental depth. For a in depth introduction of this concept, you can have a look at our [measure theory lectures](../../maths/measure_theory/probability_space). For For now, perhaps the simplest and most intuitive way to think of them, is the so-called **frequentist approach**, stating that if one could repeat a very large number of time $N$ a specific event (like rolling a dice), the probability of $i$ would be the fraction of the number of time $n_i$ that $i$ occured over $N$ that is:

$$p_i = \frac{n_i}{N}$$

Note again here that this is just one of the multiple approaches to understand the concept of probabilities. One could also raise the obvious question of wether these probabilities are objective quantities i.e. fundamental properties of the physical system, or subjective number reflecting the partial knowledge of human operators on the system. The answer could also be "a bit of both" or "none of the two". We leave here this question open and refer the curious reader to [A., Hájek (2023)](https://plato.stanford.edu/entries/probability-interpret/).

Thus $p_i$ would be the fraction of time that $i$ occured in the $N$ experiments we did.

Considering all the possible outcome of an event, the sum of all probabilities should be equal to one, translating that all possible eventualities are represent, no more, no less. That is:

$$\sum_i p_i=1$$

Suppose that a quantity $X$ can be associated to each event $i$ to give a number $X_i= X(i)$ (That is there is a function $X: \Omega \to \mathbb{R}$). For exemple, this could be the value appearing on the dice for each roll. The **average** of the quantity $X$ is defined as

$$\langle X \rangle = \sum_i p_i X_i,$$

For the dice, we would thus get the average number appearing of the dice to be $\langle X \rangle = 3.5 $. All these are very basic ideas, but that is all we will need for now in order to move forward.

<details markdown="1">
  <summary>A sidenote on the empirical mean value </summary>

To connect that with perhaps more familiar concepts, if an experiment was repeated a large number of times $N$, one would obtain a sequence of experimental results $x_n$ (that is $x_n: \mathbb{N}\to \Omega$). For exemple by rolling a dice, one could obtain $x_n= 4,2,4,1,5 ...$. The **mean** of this experiment would be defined as 

$$\overline{X} = \frac{\sum_i^N X(x_n)}{N} = \frac{\sum_i^N n_i X_i}{N}$$ 

where $n_i$ is the number of time that $i$ occurs. When $N\to \infty$, we expect that $\overline{X}=\langle X \rangle$, translating that our experiment and  $\overline{X}$ reflects the underlying probability distribution, in agreement with our "frequentist approach":

$$\langle X \rangle = \lim_{N\to \infty}\overline{X} = \lim_{N\to \infty}\frac{\sum_i^N n_i X_i}{N} \to \sum_i^N p_i X_i$$ 

</details>

Let us repeat and rephrase again the challenge of statistical physics here. Imagine that we have a physical system (e.g. a box of gas or a star), from which we observe a given macrostate, by operating some measure on it. This observation could lead us to know the average value of some quantities for example the mean energy $\langle E \rangle$ or mean number of particles $\langle N \rangle$, as well as some physical properties as the volume $V$. Now, we know that this object is composed of a very large number of particles, which could be arranged in multiple different ways to explain the mactostate we observe. These configurations are all the different microstates $i$ that can be associated to our macrostate. Reasonably, if we believe in "reductionism", we have hope that our macrostate must emmerge from the properties of these microstates i.e. we should be able to understand and interpret the macroscopic/observable properties of our system from its microscopic properties.
Now the challenge is this one, can we estimate the probability $p_i$ associated to each specific configuration (microstate) without knowing anything else than some average values?

For exemple, in the case of our dice, could we infer that each number has a probability $p_i=1/6$ to be rolled, just by being able to measure that the average value of the rolls are $3.5$? The solution, we shall argue, lies in the use of the mysterious statistical entropy function $S$.

## Defining the entropy

Let $i$ label a discrete number of $N$ possible microstates associated with the macrostate of a system. Let $p_i$ be the probability for the system to be in the microstate $i$, such that $\sum_i p_i = 1$. We define the  **statistical entropy** $S$ of the macrostate as:

$$
\boxed{
S = -\sum_i^N p_i\ln{p_i} = \langle \ln(1/p)\rangle}
$$

The fundamental principle of statistical mechanics, which will be at the core of all this lecture, is that when analysing a system we should always take $S$ to be maximum. This is the **maximum entropy principle**. From this principle, it becomes possible to obtain the expression of the probability $p_i$ for each possible microstate $i$, such that $S$ is maximum in the above expression.

Now, as such a principle is at the basis of all our future derivations, we should find a way to properly justify it and understand why it should be valid. This can be done by two different lines of reasoning. One coming from information theory, for which maximizing $S$ is the most "agnostic" way to recover the $p_i$ when no other information is known about the system, and the second one from a deeper physical level, viewing the maximimisation of entropy as a fundamental property of systems in nature. We will discuss these two arguments below, after a presentation of some properties of $S$.

## Properties of the entropy function

Entopy is often reffered to as a quantification of the **uncertainty** or of the **disorder** of a system. Let us clarify why this is true.

### Quantifying uncertainty 

Consider a system in a given macrostate associated with many possible microstates of probabilities $p_i$. There is a strong sense, rooted in information theory, in which $S$ quantifies the amount of things we do not know about the system.

It is possible to show (and we will in the next lecture) that maximizing $S$ assuming that we have $N$ accessible microstates and under the only constraints that $\sum_i p_i=1$ leads to 

$$p_i = \frac{1}{N}$$

This is the most agnostic possible inference we can make about probability of each states given what we know: all states are **equiprobable**, because we have no reason to believe that we should prefer one microstate over another.  

For such a system where all states are equiprobable, the entropy becomes:

$$
S = -\frac{1}{N}\sum_i^N\ln\left(\frac{1}{N}\right)= \ln(N)
$$

Thus $S$ grows logarithmically with the number of microstates. The more different configurations (microstates) can explain what we observe (macrostate), the less we **know** about it.
As such, if there is a single microstate $N=1$ explaining the whole macrostate, then the system is perfectly known and correspondingly the entropy is $S=\ln(1)=0$. This would also be the case if for exemple $p_1 = 1$ and $p_{i>1}=0$, that is, if only one single configuration could explain what we see, and the others are excluded. If we start to believe that other states could explain what we see, the entropy would grow gradually.
As such, we can convince ourselves that $S$ quantifies the information we have about the system.
In practice, there could be different ways to define $S$ and quantify this knowledge. In fact, the definition above is Shanon entropy, but other types of entropy exist. Besides being 0 when the system is perfectly known and growing with our ignorance, it can be showed that Shanon entropy is the only such function satisfying some specific and desirable mathematical properties. 

One important property which justifies the use of logarithms is that entropies become **additive**. That is, if we have two systems with entropies $S_1$ and $S_2$, and we consider the larger system made by their union, this larger system will have a total entropy $S_1+S_2$. Intuitively, this property emmerges directly from probabilities. It is a basic probability rule that, when combining two different events, the probability for both to occur is their product. In other words: probabilities multiply. Since $S$ is constructed from the logarithm of probabilities, and since $\ln(ab)= \ln(a)+\ln(b)$, entropies must add (a more rigorous proof can be found in the following note).

<details markdown="1">
  <summary>The properties of the entropy function</summary>

Here is a discussion of the mathematical properties that must satisfy $S$ as suggested by
[Shannon (1948)](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf). Feel free to ignore this part for now, which is quite technical, if you are not interested by these details.

Specifically, one might argue that:

- $S$ must be continuous in $p_i$. This implies that $S$ is "well behaved" and infinitesimally small changes in $p_i$ can not lead to gigantic changes in $S$.
- $S$ must be maximum for equiprobable configurations
- $S$ must be additive

</details>

### Quantifying disorder 

It is also often stated that $S$ quantifies the disorder, but what can be meant by this? There is a sense in which disorder is linked to knowledge. Think about a pack of cards containing 10 cards with numbers going from 1 to 10. There is only one way to organise it in a way such that all the cards are ordered by increasing value. In a sense, such a "macrostate" for the pile of card is perfectly known, and has $S=0$. We would also agree to say that it is very well "ordered" or "organised".
On the other hand, if we wanted to look at the macrostate "the pile of card after a random reshuffle". It is clear that a huge number of microstates with equal probability correspond to this macrostate. It is much less known, with a larger value of $S$ and is also much more disordered.
Such considerations also apply for physical systems such as a filled glass of water vs a spilled glass of water or a box containing randomly bouncing particles vs a bow where all particles are located in one corner. Hence, using the maximum entropy principle and assuming that the macrostate we observe is the one that maximises $S$ is assuming that we are in a situation which maximizes disorder.
There is also a sense in which, as we will see, systems evolve spontenously towards states of increasing entropy and hence increasing disorder (You might guess that this has to do with the [second principle of thermodynamics](../../thermo/secondprinciple/)). 

## Justifying the maximisation of entropy as a fundamental principle

When facing a problem in statistical mechanics, we will always resolve it by maximising the entropy of the system and as we said already, this will reveal exteremly powerful, allowing us to derive some experimentally verified facts (as the ideal gas law or the blackbody radiation) from microscopic properties. This maximisation is done under some constraints, for exemple forcing some mean values to be equal to the one we measure/know, as $\langle E \rangle$.

There are usually two lines of thought in order to justify the effectiveness of this approach:

- **The subjective approach**: when approaching a problem in statistical physics, we should try to infer the probability of the microstates $p_i$ by considering only what is known about the system. Maximizing the entropy gives us the most agnostic way to do so, without introducing any biais. We thus make the most honest possible thinking: maximizing our uncertainty, considering only what we know for certain. The additional constraints are then additional informations we must account for. 
- **The objective approach**: in a system, the particles can be re-arranged in a very large number of ways.  Statistically, nature will almost always occupy the state with the largest number of possible microstate, hence it will sponteneously evolve towards the larger value of $S$. The additional constraints are physical constraints forced upon the system, limiting the possible available configurations. 

These two points are in fact complementary and do not contradict one another. The first one justifies the methodology we will use to study systems, the seconds tells us about how systems evolve, why they are generally found in larger entropy states and is more linked to dynamical considerations. We will come back to all of this again and again in the class. For now, it might be preferable to bear in mind the (maybe less appealing) subjective approach, especially for the next classes. We will gradually understand why and how the objective approach is sensible and how it connects with the first.
Understanding all the consequences and meaning of entropy maximisation is a difficult and subtle task, and numerous open questions are still not resolve about it. You can find many more discussions of this topic in the litterature of physics, as well as of philosophy of physics, mathematics and information theory. Some recommanded references can be found at the bottom of this page.

## Going further: recommended readings

- [Information Theory and Statistical Mechanics - E.T. James (1957) - P.R. Vol 106, N. 4. 620-630 ](https://bayes.wustl.edu/etj/articles/theory.1.pdf)
- [Interpretations of Probability - A. Hájek (2023) - The Standford encyclopedia of philosophy](https://plato.stanford.edu/entries/probability-interpret/)
- [Philosophy of Statistical Mechanics - R. Frigg and C. Werndl (2024) - The Standford encyclopedia of philosophy](plato.stanford.edu/entries/information-entropy/). (See also all related entries contained in this page.)
- [A Mathematical Theory of Communication - C.E. Shannon (1948) - The Bell System Technical Journal,Vol. 27, pp. 379–423, 623–656](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)
