# $Topological\ Space\ \&\ Open\ Set$

[TOC]

## Define

In a [metric space](./Metric_Space.md) $(M, d)$, an open set $A$ is a set that, if $\forall a \in A$, there $\exists\epsilon > 0$ such that $\forall b \in M$ satisfying $d(x, y) < \epsilon$, then $b \in A$.

Topological space $\tau$ is a collection of subsets of $S$, that is subsets of [power set](./Power_Set.md) $P(S)$, called the Open Sets, that satisfy certain axioms,

- The empty set and $S$ itself belong to $\tau$.
  $$\{\emptyset, S\} \subseteq \tau$$ 
- The intersection of any finite members of $\tau$ belongs to $\tau$.
- Any arbitrary (finite or infinite) union of members of $\tau$ belongs to $\tau$.

## Concept

* Closed Set
  - Define  
    Closed Set is the complementary set of Open Set.  

## Property

### Homeomorphism

- Define  
  A function $f: X \to Y$ between two topological spaces is a homeomorphism if it has the following properties,
  - $f$ is a bijection 
  - $f$ is continuous
  - the inverse function $f^{-1}$ is continuous ($f$ is an open mapping).

### Chart

- Define  
  Chart $(U, \phi)$ on a set is a bijection $\phi: U \subseteq M \to \phi(U) \subseteq \mathbb R^n$, where $U, \phi(U)$ is open.

  A chart $(U, \phi)$ is centered at $p$ for $p \in U$ if $\phi(p) = 0$.

### Borel $\sigma$-algebra 

### Genus
- Define  
Genus of a non-empty connected surface is defined as the maximum number of non-intersecting simple closed curves that can be drawn on the surface without dividing it into two disconnected pieces. The genus is a topological invariant that characterizes its "number of holes". 

Genus $g$ can be defined in terms of the Euler characteristic $\chi$, where $b$ is the number of boundary components.

$$
g = \frac{2 - \chi - b}{2}  \tag{Genus}
$$

### Euler Characteristic
- Define  
Euler Characteristic is a topological invariant and defined as an alternating sum of the ranks of the homology groups of the space.

In a polyhedra, the Euler characteristic was classically defined for surfaces of polyhedra with the numbers of vertices $V$ (corners), edges $E$ and faces $F$. Any convex polyhedron's surface has Euler characteristic $\chi = 2$.
$$
\chi = V - E + F  \tag{Euler Characteristic}
$$

## Include

### Hausdorff Space

- Define  
  Hausdorff Space $X$ is a topology space where, for any distinct points $x, y \in X$, there exist a neighborhood $U$ of $x$ and a neighborhood $V$ of $y$ such that $U$ and $V$ are disjoint.
  $$U \cap V = \emptyset$$ 

- Include
  * Metric Space  
  * Manifold
