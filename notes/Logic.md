# $Logic$

[TOC]

## Concept

### Proposition

A proposition is a declarative sentence that can be judged true or false, but cannot be both true and false.

#### Axioms

An axiom is a statement that is taken to be true, to serve as a premise or starting point for further reasoning and arguments. 

#### Theorems

Theorems are propositions obtained using axioms and inference rules. Once a proposition is proven as a theorem, it can also be used as a basis for further reasoning.


### Logical connective

Logical connective can be used to connect logical formulas. 

- Negation (not)
- Conjunction (and)
- Disjunction (or)
- Implication (if...then)
- Equivalence (if and only if)

<img src="assets/Logical_connectives_Hasse_diagram.svg" alt="Logical_connectives_Hasse_diagram" style="zoom: 33%;" />

#### Predicate

Predicates are symbols or expressions used to describe object attributes or relationships between objects.

#### Quantifier

- Universal quantifier (for all) $\forall$
- Existential quantifier (there exists) $\exists$ 

### Axiomatic system

Axiom system is composed of a set of axioms (basic, unproven true statements) and a set of inference rules. It provides a framework that enables us to derive new true statements (theorems) from axioms and inference rules.

## Property

- Consistency: A system of axioms is consistent, and both if and only if there is no proposition and its negation can be proven from the axioms of that system.

- Completeness: A system of axioms is complete if and only if every true proposition of the system can be proven from its axioms.

- Gödel's incompleteness theorems: 
  - First Incompleteness Theorem: Any consistent formal system F within which a certain amount of elementary arithmetic can be carried out is incomplete; i.e., there are statements of the language of F which can neither be proved nor disproved in F.
  - Second Incompleteness Theorem: For any consistent system F within which a certain amount of elementary arithmetic can be carried out, the consistency of F cannot be proved in F itself.
