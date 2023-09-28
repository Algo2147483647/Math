# $Set$

[TOC]

## Define  
A set $S$ is a collection of distinct objects.

If an object $x$ is a member of a set $S$, we write $x \in S$. Otherwise, we write $x \notin S$.

## Property

* Cardinality & Counting
- relationship between sets
  * Subset & Proper Subset 
    $$
    A \subseteq B \quad\Leftrightarrow\quad x \in B, \forall x \in A \tag{Subset}
    $$
    If all the elements of set $A$ are contained in a set $B$, then we say $A$ is a subset of $B$.

    $$
    A \subset B \Leftrightarrow x \in B, \forall x \in A \text{ and } \exist x \notin A, x \in B \tag{Proper Subset}
    $$

    A set $A$ is a proper subset of $B$, if $A \subseteq B$, but not $A = B$.

  * Set::Equal  
    $$
    \begin{align*}
      A = B &\quad\Leftrightarrow\quad x \in B, \forall x \in A \text{ and } x \in A, \forall x \in B  \tag{equal}\\
      &\quad\Leftrightarrow\quad A \subseteq B, B \subseteq A
    \end{align*}
    $$
    Two sets are equal, if they contain the same elements.

  * Disjoint
    $$
    A, B \text{ is Disjoint } \quad\Leftrightarrow\quad A \cap B = \emptyset
    $$

- operations
  * Intersection
    - Define
      $$
      A \cap B = \{x \ |\ x \in A, x \in B\}  \tag{Intersection}
      $$

    - Property
      - idempotency law: $A \cap A = A$
      - commutative law: $A \cap B = B \cap A$  
      - associative law: $A \cap (B \cap C) = (A \cap B) \cap C$

  * Union
    - Define  
      $$
      A \cup B = \{x \ |\ x \in A \text{ or } x \in B \}  \tag{Union}
      $$

    - Property
      - idempotency law: $A \cup A = A$
      - commutative law: $A \cup B = B \cup A$  
      - associative law: $A \cup (B \cup C) = (A \cup B) \cup C$
    
  * Difference
    - Define
      $$
      A - B = \{x \ |\ x \in A \text{ and } x \notin B\}  \tag{Difference}
      $$

  * Complement of A Set
    - Define  
      $$
      \bar A = U - A = \{x \ |\ x \in U, x \notin A\}  \tag{Complement of A Set}
      $$

      For a universal set $U$, the complement of a set $A$ is $U - A$.

    - Property
      - $\bar{\bar A} = A$ 

  - Property
    - distributive laws 
      $$
      A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
      $$
      $$
      A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
      $$
    - absorption laws
      $$
      A \cap (A \cup B) = A
      $$
      $$
      A \cup (A \cap B) = A
      $$
    - DeMorgan's laws
      $$
      A - (B \cap C) = (A - B) \cup (A - C)
      $$
      $$
      A - (B \cup C) = (A - B) \cap (A - C)
      $$
      $$
      \overline{A \cap B} = \bar A \cup \bar B
      $$
      $$
      \overline{A \cup B} = \bar A \cap \bar B
      $$

- Special Operations
  * Cartesian Product
    - Define
      $$
      A \times B = \{(a, b) \ | a \in A \text{ and } b \in B\}
      $$
      For two sets $A, B$, cartesian product is the set of all ordered pairs such that the first element of the pair is an element of $A$ and the second one is from $B$.

    - Property
      - $\text{number}(A \times B) = \text{number}(A) \cdot \text{number}(B)$

    - Include
      * Binary Relation
        - Define  
          $$
          X \ R\ Y \subseteq X \times Y  \tag{Binary Relation}
          $$
          Binary Relation $R$ over set $X, Y$ is a subset of the Cartesian product $X \times Y$. The set $X$ is called the domain, and set $Y$ the codomain.

        - Include 
          * Mapping , Function 
          * Partial Order & Strict Partial Order

  * [Power Set](./Power_Set.md)

## Example

* Empty Set
  - Define 
    $$\emptyset = \{\}  \tag{Empty Set}$$
    Empty Set is a set without any element. 

  - Property 
    - $\emptyset \in S, \forall \text{ set } S$
    - $A \cap \emptyset = \emptyset$
    - $A \cup \emptyset = A$

* Ordered Set 
* [Algebra Structure](./Algebra_Structure.md)
* [Graph](./Graph.md)
