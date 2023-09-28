# $Group$

[TOC]

## Define  

$$
(G, \cdot)
$$

Group is an algebraic structure, where $G$ is a set, $\cdot$ is a binary operation, and satisfy:

- closure: $a, b \in G \Rightarrow a \cdot b \in G$
- associative law $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
- exists identity element, $\exists 1: x \cdot 1 = 1 \cdot x = x$
- exists inverse element, $\exists x^{-1}: x \cdot x^{-1} = x^{-1} \cdot x = 1$



## Property

- $1$ is unique
  - Proof  
    $$
    1_1 = 1_1 \cdot 1_2 = 1_2
    $$
- The inverse of each element is unique.
- Absorbing Element
  $$
  x \cdot 0 = 0 \cdot x = 0  \quad; \forall x \in G  \tag{absorbing element}
  $$
- 1 
  - $\forall a \in G, (a^{-1})^{-1} = a$
  - $\forall a,b \in G, (a \cdot b)^{-1} = b^{-1} \cdot a^{-1}$
  - $\forall a,b,c \in G, a\cdot b = a \cdot c  \quad\Rightarrow\quad b = c$
  - $\forall a,b,c \in G, b\cdot a = c \cdot a  \quad\Rightarrow\quad b = c$ 

* Subgroup
  - Define  
    $$
    H \subseteq G, H \neq \emptyset, (H, \cdot) \text{ is group } \quad\Rightarrow\quad H \le G  \tag{Subgroup}
    $$

    For a group $(G, \cdot)$ and a nonempty subset $H$ of $G$, if $(H, \cdot)$ is also group, then $(H, \cdot)$ is a subgroup of $(G, \cdot)$.

  - Property  
    - $1 \le G, G \le G$

    * Coset
      - Define  
        For a subgroup $H$ of the group $G$ and an element $g \in G$, the left cosets of $H$ in $G$ are the sets obtained by multiplying each element of $H$ by a fixed element $g$ (where $g$ is the left factor).
        $$
        gH = \{gh \ |\ h \in H\} \quad, \text{for } g \in G  \tag{left cosets}
        $$

        The right cosets are defined similarly, except that the element g is now a right factor.
        $$
        Hg = \{hg \ |\ h \in H\} \quad, \text{for } g \in G  \tag{right cosets}
        $$

      - Property
        * Quotient Group
  
  - Include
    * Normal Subgroup
      - Define
        $$
        H \lhd G \quad\Leftrightarrow\quad  g^{-1}hg \in H, \forall h \in H \le G, g \in  G \tag{Normal Subgroup}
        $$
        Normal Subgroup is a subgroup $H \le G$ if it is invariant under conjugation, that is, $\forall h \in H, g \in G$, we have $g^{-1}hg \in H$.

      - Property
        * Quotient Group

* Group Homomorphism
  - Define
    $$
    f: G \to H
    $$
    Group Homomorphism is a function $f$ from a group $(G, \cdot)$ to another group $(H, *)$ such that for all $u, v \in G$ it hold that,
    $$
    f(u \cdot v) = f(u) * f(v) \quad, \forall u, v \in G
    $$

  - Property
    * Isomorphism of Groups  
      If Group Homomorphism of $G, H$ is a Bijection, the groups $G, H$ are called isomorphic.

## Include

* Commutative Group , Abelian Group
  - Define   
    Commutative Group is a Group satisfied commutative law,
    $$
    a \cdot b = b \cdot a
    $$

## Example 

* Symmetric Group
  - Define  
    $$
    S_n = (\{f: X \to X\}, \circ)
    $$
    Symmetric group on a finite set $X$ is the group whose elements are all bijective functions $f: X \to X$ and whose group operation is that of function composition $f_1 \circ f_2 = f_1(f_2(\cdot))$. Where $n$ is the degree of symmetric group, that is, the number of elements in set $X$.

  - Property
    - Cayley's theorem: every group $G$ is isomorphic to a subgroup of a symmetric group.

  - Example 
    * Permutation Group
      - Define  
        Permutation group is a group $G$ whose elements are permutations of a given set $M$ and whose group operation is the composition of permutations in $G$ (which are thought of as bijective functions from the set $M$ to itself).  

      - Property
        - every group is isomorphic to some permutation group.