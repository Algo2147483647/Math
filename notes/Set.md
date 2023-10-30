# $Set$

[TOC]

## Define

$$
\{\cdot\}
$$



A set $S$ is a collection of distinct objects.

If an object $x$ is a member of a set $S$, we write $x \in S$. Otherwise, we write $x \notin S$.

## Property

### Cardinality & Counting

- Define  
  $$
  |S| = \text{number}(S)  \tag{Cardinality}
  $$
  Cardinality $|S|$ is the number of elements in a set $S$.

- Property
  * Addition theorem  
    for $S = \cap_{i=1}^n S_i, S_i \cap S_j = \emptyset (i ≠ j)$
    $$
    \Rightarrow |S| = \sum_{i=1}^n |S_i|
    $$

  * Multiplication theorem  
    for sets $S_A, S_B$, and
    $$
    \begin{align*}
      S &= \{(a, b) | a \in S_A, b \in S_B\}  \\
        &= S_A × S_B  \tag{Cartesian积}  \\
    \end{align*}
    $$
    $$
    \Rightarrow |S| = |S_A| × |S_B|
    $$

    - Proof
      $$
      \begin{align*}
        S 
        &= \{(a, b) | a \in S_A, b \in S_B\}  \\
        &= \bigcap_{a_i \in S_A} \{(a_i, b) | b \in S_B\}  \\
        \Rightarrow |S| &= \sum_{i=1}^{|S_A|} |S_B|  \tag{Addition theorem}  \\
        &= |S_A| × |S_B|  \\
      \end{align*}
      $$

  * Principle of Inclusion-Exclusion  
    for $A_1,...,A_n \subseteq S$
    $$
    \begin{align*}
      \left|\bigcup_{i=1}^n A_i\right| &= \sum_{k=1}^n \left((-1)^{k-1} \sum_{\substack{i_1,...,i_k \in 1:n \\ i_1≠...≠i_k}} \left|\bigcup_{i\in\{i_1,...,i_k\}} A_i\right|\right)
    \end{align*}
    $$

  - Special Counting Sequence
    * Catalan Numbers 
      - Define  
        $$
        \begin{align*}
          f_n 
          &= \frac{C(2n, n)}{n+1}\quad, n \ge 0  \\
          &= C(2n, n) - C(2n, n - 1)  \\
          &= C(2n, n) - C(2n, n + 1)  \\
          &= \frac{(2n)!}{(n+1)! n!}\\
          &= \left\{\begin{matrix}
            \sum\limits_{i=1}^n f_{i-1}f_{n-i}  & n \ge 2\\
            1 & n = 0, 1
          \end{matrix}\right. \tag{recurrence form}\\
          &= \frac{4n-2}{n+1} f_{n-1}
        \end{align*}
        $$
        Catalan Numbers are a sequence of natural numbers.
      
  * Pigeonhole Principle  
    for $A_1, ..., A_n \subseteq A, |A| = n + 1$, $\Rightarrow \exists A_i, |A_i| ≥ 2$.

### Relationship between sets

* Subset & Proper Subset 
  $$
  A \subseteq B \quad\Leftrightarrow\quad x \in B, \forall x \in A \tag{Subset}
  $$
  If all the elements of set $A$ are contained in a set $B$, then we say $A$ is a subset of $B$.

  $$
  A \subset B \Leftrightarrow x \in B, \forall x \in A \text{ and } \exist x \notin A, x \in B \tag{Proper Subset}
  $$

  A set $A$ is a proper subset of $B$, if $A \subseteq B$, but not $A = B$.

* Equal  
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

### Operations

#### Intersection

- Define
  $$
  A \cap B = \{x \ |\ x \in A, x \in B\}  \tag{Intersection}
  $$

- Property
  - idempotency law: $A \cap A = A$
  - commutative law: $A \cap B = B \cap A$  
  - associative law: $A \cap (B \cap C) = (A \cap B) \cap C$

#### Union

- Define  
  $$
  A \cup B = \{x \ |\ x \in A \text{ or } x \in B \}  \tag{Union}
  $$

- Property
  - idempotency law: $A \cup A = A$
  - commutative law: $A \cup B = B \cup A$  
  - associative law: $A \cup (B \cup C) = (A \cup B) \cup C$

#### Difference

- Define
  $$
  A - B = \{x \ |\ x \in A \text{ and } x \notin B\}  \tag{Difference}
  $$

#### Complement of A Set

- Define  
  $$
  \bar A = U - A = \{x \ |\ x \in U, x \notin A\}  \tag{Complement of A Set}
  $$

  For a universal set $U$, the complement of a set $A$ is $U - A$.

- Property
  - $\bar{\bar A} = A$ 

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

### Cartesian Product

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

### [Power Set](./Power_Set.md)

## Example
### Ordered Pair

- Define
  $$
  (a, b) = \{\{a\}, \{a, b\}\}
  $$
  Ordered pair $(a, b)$ is a pair of two elements $a, b$ in which order matters.
  
### Empty Set
  - Define 
    $$
    \emptyset = \{\}  \tag{Empty Set}
    $$
    Empty Set is a set without any element. 

  - Property 
    - $\emptyset \in S, \forall \text{ set } S$
    - $A \cap \emptyset = \emptyset$
    - $A \cup \emptyset = A$

### [Ordered Set ](./Ordered_Set.md)
### [Algebra Structure](./Algebra_Structure.md)
### [Graph](./Graph.md)
