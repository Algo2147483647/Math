# $Manifold$
[TOC]
## Define  
Manifold $M$ is a second countable [Hausdorff space](./Topological_Space.md) that is locally homeomorphic to a [Euclidean space](./Euclidean_Space.md).

- Hausdorff, $\forall x, y \in M$, there exists open neighborhoods $U_x, U_y \subseteq M$ with $x \in U_x, y \in U_y$ and $U_x \cap U_y = \emptyset$.   
- Second countable, there exits a countable collection $(U_n)_{n \in \mathbb N}$ of open set in $M$ such that for all $V \subseteq M$ open, and $p \in V$, there is some $n$ such that $p \in U_n \subseteq V$
- Locally homeomorphic to a Euclidean space, every point has a neighborhood $U$ homeomorphic $\phi: U \to V$ to an open subset $V$ of the Euclidean space $\mathbb R^n$ for some nonnegative integer $n$.

## Property

### Geodesic

A geodesic is a curve representing in some sense the shortest path between two points in a Riemannian manifold. 

## Include

### Differential manifold

#### Define

Differential manifold $M$ of dimension $n$ is a manifold and equipped with a differentiable structure.

- Differentiable Structure: There exists a collection of charts $\{(U_\alpha, \varphi_\alpha)\}$ such that the open sets $U_\alpha$ cover $M$ and the transition maps $\varphi_\beta\circ \varphi_\alpha^{-1}: \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$ are differentiable functions for all overlapping charts $(U_\alpha, \varphi_\alpha)$ and $(U_\beta, \varphi_\beta)$. This collection of charts is called an atlas.