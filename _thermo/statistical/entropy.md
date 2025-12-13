---
layout: default
title: Statistical physics
parent: thermo
nav_order: 1
---

# The statistical entropy

## Statistical physics, microstates and macrostates

The idea laying behind statistical mechanics will be to explain the observed behavior of large systems as the result of underlying microscopic subsystems. For exemple, we will be able to retrieve quite elegantly the ideal gas law, which was central in our first thermodynamics class, by interpreting a volume of gas as being composed of a large number of free bouncing microscopic particles.

Statistical mechanics lies on the distinction between macrostates and microstates:

- The **macrostate** of a system corresponds to the state as described in classical thermodynamics. It is what you would measure about the system here and now: its temperature, pressure, volume etc

- The **microstate** of a system is the complete description of the system in term of its microscopic constituents.

As such, **several *microstates* can correspond to the same *macrostate***: you can think of an infinite amount of different ways to put particles of gas in a box which will give you the same measured pressure, temperature and volume. As time passes, the system will explore different microstates while remaining in the same macrostate.

Each microstate $i$ can be associated with a probability of occuring $p_i$. The challenge of statistical mechanics is to find the right way to estimate this probability. This will be done by  maximizing a quantity, known as the statistical entropy $S$. We will see that $S$ can be identified with the quantity appearing in the second principle of thermodynamics discussed in the [thermodynamics class](../../thermo/secondprinciple/). The entropy can easily be treated as one of the most profound and most subtle concept of modern physics.


## Preliminary review of basic probability theory for the discrete case and the challenge of statistical mechanics
   
As a very simple reminder, recall that for a discrete set of possible events, which we will label by the index $i$, the probabilties represent the "chance" for this event to occur, expressed in percentage ($p_i \leq 1$). For exemple, considering rolling a dice, the possible results would be $i=\{1,2,3,4,5,6}$ and $p_i = 1/6$, for each $i$. 

Probability is also a highly subtle concept, which can be defined and introduced in a great number of way, with different level of abstraction and fundamental depth. Perhaps the simplest and most intuitive way to think of them, is the so-called frequentist approach, stating that if one could repeat a very large number of time $N$ a specific event (like rolling a dice), the probability of $i$ would be the fraction of the number of time $n_i$ that $i$ occured over $N$ that is:

$$p_i = \frac{n_i}{N}$$

One could also raise the obvious question of wether these probabilities are objective quantities i.e. fundamental properties of the physical system, or subjective number reflecting the partial knowledge of human operators on the system. The answer could also be "a bit of both" or "none of the two". We leave here this question open and refer the curious reader to [A., Hájek (2023)](https://plato.stanford.edu/entries/probability-interpret/).

Thus $p_i$ would be the fraction of time that $i$ occured in the $N$ experiments we did.

Considering all the possible outcome of an event, the sum of all probabilities should be equal to one, translating that all possible eventualities are represent, no more, no less. That is:

$$\sum_i p_i=1$$

Suppose that a quantity can be associated to each event $i$. For exemple, this could be the value appearing on the dice for each roll. The **average** of the quantity $X_i$ is defined as

$$\langle X \rangle = \sum_i p_i X_i$$

For the dice, we would thus get the average number appearing of the dice to be $\langle X \rangle = 3.5 $. All these are very basic ideas, but that is all we will need for now in order to move forward.

Let us repeat and rephrase again the challenge of statistical physics here. Imagine that we have a physical system (e.g. a box of gas or a star), from which we observe a given macrostate, by operating some measure on it. This observation could lead us to know the average value of some quantities for example the mean energy $\langle E \rangle$ or mean number of particles $\langle N \rangle$, as well as some physical properties as the volume $V$. Now, we know that this object is composed of a very large number of particles, which could be arranged in multiple different ways to explain the mactostate we observe. These configurations are all the different microstates $i$ that can be associated to our macrostate. Reasonably, if we believe in "reductionism", we have hope that our macrostate must emmerge from the properties of these microstates i.e. we should be able to understand and interpret the macroscopic/observable properties of our system from its microscopic properties.
Now the challenge is this one, can we estimate the probability $p_i$ associated to each specific configuration (microstate) without knowing anything else than some average values?

For exemple, in the case of our dice, could we infer that each number has a probability $p_i=1/6$ to be rolled, just by being able to measure that the average value of the rolls are $3.5$? The solution, we shall argue, lies in the use of the mysterious statistical entropy function $S$.

## Defining the entropy

Let $i$ label a discrete number of $N$ possible microstates associated with the macrostate of a system. Let $p_i$ be the probability for the system to be in the microstate $i$, such that $\sum_i p_i = 1$. We define the  **statistical entropy** $S$ of the macrostate as:

$$
\boxed{
S = -\sum_i^N p_i\ln{p_i} = -\langle \ln(p_i)\rangle}
$$

The fundamental principle of statistical mechanics, which will be at the core of all this lecture, is that when analysing a system we should always take $S$ to be maximum. This is the **maximum entropy principle**. From this principle, it becomes possible to obtain the expression of the probability $p_i$ for each possible microstate $i$, such that $S$ is maximum in the above expression.

Now, as such a principle is at the basis of all our future derivations, we should find a way to properly justify it and understand why it should be valid. This can be done by two different lines of reasoning. One coming from information theory, for which maximizing $S$ is the most "agnostic" way to recover the $p_i$ when no other information is known about the system, and the second one from a deeper physical level, viewing the maximimisation of entropy as a fundamental property of systems in nature. We will discuss these two arguments below, after a presentation of some properties of $S$.

## Properties of the entropy function

Entopy quantifies **uncertainty**.

Entropy quantifies **disorder**.

For a system where all states are equiprobable, $p_i=1/N$ and:

$$
S = -\frac{1}{N}\sum_i^N\ln\left(\frac{1}{N}\right)= \ln(N)
$$

As such, if there is a single microstate $N=1$ explaining the whole macrostate, then the system is perfectly known and correspondingly the entropy is $S=0$. The more microstates $N$ associated to a macrostate, the bigger the entropy, as desired. The entropy hence quantifies how probable a macrostate is in term of its microstates. 

## Justifying the maximisation of entropy

When facing a problem in statistical mechanics, we will always resolve it by maximising the entropy of the system and as we said already, this will reveal exteremly powerful, allowing us to derive some experimentally verified facts (as the ideal gas law or the blackbody radiation) from microscopic properties. This maximisation is done under some constraints, for exemple forcing some mean values to be equal to the one we measure/know, as $\langle E \rangle$.

There are usually two lines of thought in order to justify the effectiveness of this approach:

- **The subjective approach**: when approaching a problem in statistical physics, we should try to infer the probability of the microstates $p_i$ by considering only what is known about the system. Maximizing the entropy gives us the most agnostic way to do so, without introducing any biais. We thus make the most honnest possible thinking: maximizing our uncertainty, considering only what we know for certain. The additional constraints are then additional informations we must account for. 
- **The objective approach**: in a system, the particles can be re-arranged in a very large number of ways. Statistically, nature will always occupy the state with the largest number of possible microstate. The additional constraints are physical constraints forced upon the system, limiting the possible available configurations.

Understanding all the consequences and meaning of entropy maximisation is a difficult and subtle task, and numerous open questions are still not resolve about it. You can find many more discussions of this topic in the litterature of physics, as well as of philosophy of physics, mathematics and information theory. Some recommanded references can be found at the bottom of this page.

## A remark: the conservation of information and the principle zero of thermodynamics

## Going further: recommended readings

- [Information Theory and Statistical Mechanics - E.T. James (1957) - P.R. Vol 106, N. 4. 620-630 ](https://bayes.wustl.edu/etj/articles/theory.1.pdf)
- [Interpretations of Probability - A. Hájek (2023) - The Standford encyclopedia of philosophy](https://plato.stanford.edu/entries/probability-interpret/)
- [Philosophy of Statistical Mechanics - R. Frigg and C. Werndl (2024) - The Standford encyclopedia of philosophy](plato.stanford.edu/entries/information-entropy/). (See also all related entries contained in this page.)

