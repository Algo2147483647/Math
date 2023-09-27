# $Ring$

[TOC]

## Define  

$$
(G, +, \cdot)
$$

Ring is an algebraic structure, where $G$ is a set, $\cdot$ and $+$ are binary operations, and satisfy:  

- $(G, +)$ is a commutative group
- $(G, \cdot)$ is a monoid
  - $(G, \cdot)$ satisfies associative law, $a \cdot (b \cdot c) = (a \cdot b) \cdot c$
  - $(G, \cdot)$ exists multiplicative identity, $\exist 1: 1 \cdot x = x \cdot 1 = x, \forall x \in G$
- Distributive law: multiplication is distributive with respect to addition,
  $$
  \begin{align*}
    a \cdot (b + c) &= a \cdot b + a \cdot c  \\
    (b + c) \cdot a &= b \cdot a + c \cdot a
  \end{align*}
  $$

## Include

* Commutative Ring
  - Define  
    A Ring satisfying commutative law.
    $$
    a \cdot b = b \cdot a \quad; \forall a, b \in G
    $$

  - include
    * Integer Ring

* Field
  - Define  
    Field is a ring that satisfies the existence of multiplicative inverses for every nonzero element. 

  - Example
    * Real Field  
    * Complex Field 
