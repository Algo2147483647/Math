# $Bipartite\ Graph$

[TOC]

## Define
$$
(X, Y, E)  \tag{Bipartite Graph}
$$
$$
X, Y \subset V, X \cup Y = V  \tag{vertex sets}
$$
$$
E = \{(x_i, y_j) \ |\ x_i \in X, y_j \in Y\}  \tag{edge set}
$$

For a Bipartite Graph, The vertex set $V$ of a graph is divided into two disjoint subsets $X, Y$. And, edges in Bipartite Graph only exist between point sets $X, Y$, not within them.

## Property
- Representation, a bipartite graph can be represented by a matrix $M \in \mathbb R^{m \times n}$ with each value $M_{ij}$ refer to the edge weight between $x_i$ and $y_j$, where $m$ is the element number of $X$ and $n$ is that of $Y$.
  $$
  f:(X \times Y) \to \mathbb R \quad\Rightarrow\quad \mathbb R^{m \times n}
  $$

- *Q: Search Maximum Matching*
  
  - Property
    - The maximum matching of bipartite graphs equivalents to a network flow model.
      Connect the source point to all points on the left and all points on the right to the sink, with a capacity of $1$. The original edge is connected from left to right, with a capacity of $1$. The maximum flow is the maximum match. 

  * Hungarian Algorithm , Kuhn-Munkres Algorithm
    - Process

  - Hopcroft-Karp Algorithm
