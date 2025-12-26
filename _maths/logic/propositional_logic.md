---
layout: default
title: propositional logic
parent: maths
nav_order: 1
---

# Propositional logic

## Propositions

The simplest elements of logic are called **propositions**. They are objects, which we will note $p,q,r,...$ which can take only two possible values, noted either 'True' (T) or 'False' (F), $0$ and $1$ or 'yes' and 'no'. This value is called the **truth value** of the proposition. In standard propositional logic, one consider that truth values are **mutually exclusive** that is $p$ can be either true or false, but not both or neither. This is called the **bivalence principle**. We will see much later that going beyond this principle allows to define [alternative logic](./alternative_logic.md).

Logic takes its origin in philosophy, where it is mostly concerned about the structure of reasoning and the validity of some inferences. In this context, propositions could be sentences as $p =$"The book is blue". $p$ can thus be either true or false. The goal of logic will not be to estimate wether $p$ is, in fact, true or false but instead to see how to combine sentences such as $p$ with other propositions in order to build more complicated structures. One would then study the consequence of the truness or falsness of $p$ on the whole network of propositions in which it is embedded and study wether logical arguments containing $p$ can be considered as valid, or not (if this seems very abstract, we will try to illustrate it better later on). 

Mathematics and informatics built on the philosopher's logic to build the fundations of their discipline. In this context, a proposition which can take only two values $0/1$ or 'yes'/'no', represents a minimal amount of information (a bit). By connecting together such minimal structures, one can construct much complex objects, such as sets and numbers for mathematics and computers for informatics!

## Unary operations

We will now define operations acting on propositions which transform their truth values and give back other propositions. Perhaps the simplest operation of the sort is the negation "not", noted $\lnot$. $\lnot$ acts on a proposition $p$ and reverse its truth value. That is, if $p$:'the book is blue' is true, $\lnot p$, would be false and could be phrased as 'the book is not blue'. Similarly, if $p$ is false, then $\lnot p$ would be true.

In logic, it is common to summarise the actions of an operator using a so-called **truth table**:

| $p$     | $\lnot p$ |
|-------|------------|
| T  | F      |
| F | T       |

On the left column are noted the possible truth values of $p$, and on the right column are noted the corresponding truth values of $\lnot p$ (T for True and F for False). 

If you think hard about it and try to make all the possible combinations, you will realise that there are only four possible unary operations. That is, we are missing three of them.

One is trivial, it is the **identity** operation, which does not change anything on the truth values of $p$, Id($p$):

| $p$     | Id($p$) |
|-------|------------|
| T  | T     |
| F | F      |

Another possible one, returns 'true' no matter what is the truth value of $p$. It is the **Tautology** $\top p$:

| $p$     | $\top(p)$ |
|-------|------------|
| T  | T      |
| F | T      |


Finally, one can think of an operation returning 'false' no matter what is the truth value of $p$. It is the **Antilogy** or **contradiction**, $\bot p$:

| $p$     | $\bot(p)$ |
|-------|------------|
| T  | F      |
| F | F      |

## Binary operations

There are 16 binary operations.

and:

| $p$     | $q$ | $p \wedge q$ |
|-------|------------|
| T  | T      | T
| F | F      | F
| T | F      | F
| F | T     | F

or: 

| $p$     | $q$ | $p \lor q$ |
|-------|------------|
| T  | T      | T
| F | F      | F
| T | F      | T
| F | T     |  T

implication:

| $p$     | $q$ | $p \to q$ |
|-------|------------|
| T  | T      | T
| F | F      | T
| T | F      | T
| F | T     |  F

equivalence:

| $p$     | $q$ | $p \leftrightarrow q$ |
|-------|------------|
| T  | T      | T
| F | F      | T
| T | F      | F
| F | T     |  F

## A bit of formality

Propositions are variables over the space $\Omega=\\{0,1\\}$. $N$-arry operations are maps $\Omega \times \Omega ...$($N$ times)$... \times \Omega \to \Omega$.