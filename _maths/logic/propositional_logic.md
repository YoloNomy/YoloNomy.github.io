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

Binary operations are operations that you can make by taking two propositions $p$ and $q$, to make a new one.

One that is easy to understand would be the **and** operation known as the **conjuction** and usually noted $\wedge$ or $\&$. $p$ and $q$, noted $p\wedge q$ is thus a new proposition, which can be either true or false. Following the intuition that we have of "and", we can say that "and" is true when both $p$ and $q$ are true, and false otherwise. Indeed think of the sentence "the book is blue and the table is red". It is clear that this sentence would be true only if each part of it is. This can be summarized in a truth table as:

| $p$     | $q$ | $p \wedge q$ |
|-------|------------|
| T  | T      | T
| F | F      | F
| T | F      | F
| F | T     | F

If you think hard about it again, you will notice that there are 16 possible binary operations. An other one you can think of is the **or** operation, known as the **disjunction**. It is usually noted $\lor$. Such operator could appear in sentences like "the book is blue or the table is red". Clearly, such a sentence would be true if either of its part is true, or both. We thus define or as:

| $p$     | $q$ | $p \lor q$ |
|-------|------------|
| T  | T      | T
| F | F      | F
| T | F      | T
| F | T     |  T

You could have the feeling that "or" must be false when both sentences are true. If so, you might be thinking of sentences like "do you want a tea or a coffee?". Clearly this "or" does not have the same meaning as the previous one, as you usually do not expect that "both tea and coffee" can be a correct answer to the question.

It is possible to use another, distinct operation to express this second "or", known as the **exclusive disjunction**, noted $\oplus$:

| $p$     | $q$ | $p \oplus q$ |
|-------|------------|
| T  | T      | F
| F | F      | F
| T | F      | T
| F | T     |  T

An interesting thing we can note at that point, is that operations can be combined to make new ones. That is, we could but we do not need to create 16 different operations with different thruth tables.

For example it is possible to rewrite the proposition 

$$p \oplus q $$ 

as

$$(p \wedge \lnot q) \lor ( \lnot p ∧ q)$$

Parenthesis are here to indicate that we should first do the two binary operations $p \wedge \lnot q$ and $\lnot p ∧ q$. If it helps, we could assign new names to these two propositions, say $r$ and $s$. Then, one proceeds by doing the final binary operation $r\lor s$.

Thus $\oplus$ can be expressed as a combination of $\wedge$ and $\lnot$. You can convince yourself that this is true by combining truth tables togethers. We do so explicitely in the following "proof" note.

<details markdown="1">
  <summary><strong>Proof</strong></summary>

By definition of $\lnot$, we know that

| $q/p$     | $\lnot q/p$ |
|-------|------------|
| T  | F      |
| F | T       |

The definition of and is

| $p$     | $q$ | $p \wedge q$ |
|-------|------------|
| T  | T      | T
| F | F      | F
| T | F      | F
| F | T     | F

Combining these two tables, we get:

| $p$     | $q$ |   $\lnot p$ | $\lnot q$ | $p \wedge q$ | $p \wedge \lnot q$ | $ \lnot p \wedge q$ |
|-------|------------|
| T  | T  | F | F    | T |  F| F
| F | F   | T  |T  |   F | F | F
| T | F   | F  |T   | F | T | F
| F | T   | T | F    | F |  F| T

Try to convince yourself that this table is correct, and why! The general idea is the following: consider the table of $p\and q$. It is always false, except when both $p$ and $q$ are true. Now replace $q$ by $\lnot q$. It will be false when $q$ is true, thus $p\wedge \lnot q$ can not be true anymore when $p$ and $q$ are true (as $\lnot q$ would be false). However $\lnot q$ is true when $q$ is false. Thus $p\wedge \lnot q$ must be true when $q$ is false.  We will show later some techniques to do this quickly, but with a bit of training it will all go much quickly! Try yourself.

Now, we recall the definition of $\lor$:

| $p$     | $q$ | $p \lor q$ |
|-------|------------|
| T  | T      | T 
| F | F      | F
| T | F      | T
| F | T     |  T

from which, we can write:

| $p$     | $q$ | $p \wedge \lnot q$ | $ \lnot p \wedge q$ | $(p \wedge \lnot q) \lor ( \lnot p ∧ q)$|
|-------|------------|
| T  | T  | F   | F  |  F
| F | F   |  F | F  |  F
| T | F   |  T | F  | T
| F | T   |  F|  T  | T

This is exactly the table we proposed for $\oplus$. We just prooved that the two propositions are the same.

</details>


Another extremely important binary operation is the **implication**, noted $\to$. The proposition $p\to q$ is an attempt to formalize sentences as "**if** it rains, **then** the ground is wet". We can understand why this operation is so important, as it try encompass logical implication. 
The consensus is to define implication by asking the only following condition: "something true can not imply something false". Indeed, a sentence like "If it rains, unicorns exist" will seem incorrect.

| $p$     | $q$ | $p \to q$ |
|-------|------------|
| T  | T      | T
| F | F      | T
| T | F      | T
| F | T     |  F



Just as for $\oplus$, it is possible to rewrite $\to$ in term of other binary operations. Indeed, it is possible to show that $p \to q$ is the same operation as $ \lnot p \lor q$.

<details markdown="1">
  <summary><strong>Exercice:</strong> proove that  $p \to q$ is the same operation as $ \lnot p \lor q$ using truth tables</summary>
</details>

**equivalence**:

| $p$     | $q$ | $p \leftrightarrow q$ |
|-------|------------|
| T  | T      | T
| F | F      | T
| T | F      | F
| F | T     |  F




## A bit more formality

Propositions are variables over the space $\Omega=\\{0,1\\}$. $N$-arry operations are maps $\Omega \times \Omega ...$($N$ times)$... \times \Omega \to \Omega$.

## Further reading

- [Franks, Curtis, "Propositional Logic", The Stanford Encyclopedia of Philosophy (Winter 2024 Edition), Edward N. Zalta & Uri Nodelman (eds.)](https://plato.stanford.edu/archives/win2024/entries/logic-propositional/)
- [Truth table page of wikipedia](https://en.wikipedia.org/wiki/Truth_table#Binary_operations)
