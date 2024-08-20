# $Power\ Set$

[TOC]

## Define  
$$
P(S) = \{X \ |\ X \subseteq S\}  \tag{Power Set}
$$
The Power Set of a set $S$ is the set of all subset of $S$, including $\emptyset$ and $S$ itself.

<img src="./assets/Hasse_diagram_of_powerset_of_3.svg" alt="Hasse_diagram_of_powerset_of_3" style="zoom: 40%;" />

## Property

- The number of elements in the power set of a set $S$ is $2^n$, where $n$ is the number of elements in the set $S$.
  $$
  |P(S)| = 2^{|S|}
  $$

## Include

### $\sigma$-algebra

- Define  
  $$
  \Sigma \subseteq P(S)  \tag{$\sigma$-algebra}
  $$
  For a set $S$ and its power set $P(S)$, a $\sigma$-algebra $\Sigma$ is a subset of power set such that
  - $S \in \Sigma$, and $S$ is considered to be the universal set in the following context.
  - $\Sigma$ closed under complementation, i.e. $A \in \Sigma$ implies that $A^C = S - A \in \Sigma$. Meanwhile, base on the $S \in \Sigma$ (1) we have $\emptyset \in \Sigma$. 
  - $\Sigma$ is closed under countable unions, i.e. for any sequence $(A_1, ..., A_n), A_i \in \Sigma$, we have that 
    $$
    \bigcup_i A_i \in \Sigma
    $$

- Property
  - The maximum $\sigma$-algebra is Power Set of $S$,  
    The minimum $\sigma$-algebra is $\{\emptyset, S\}$

  - Countable intersection set closure, if $A_1, ... , A_n \in Σ$, then $\bigcap_i A_i  \in Σ$
    - Proof  
      De Morgan's law

- Include
  * Borel $\sigma$-algebra
    * Define  
      $$\mathcal B(X) = \sigma(\mathcal O)  \tag{Borel $\sigma$-algebra}$$ 
      The Borel $\sigma$-algebra on a topological space $X$ is the smallest $\sigma$-algebra containing all the open subsets of $X$. Where $\mathcal O$ denote the collection of all open subsets of $X$.

### Combination

- Define
  $$
  f_\text{Conbination}(S, k) = \{ X \ |\ X \subseteq S , |X| = k\}  \tag{Conbination}
  $$
  Combination, is the selection of $k$ elements from a set of $n$ elements without any regard to the order in which they are chosen.

  The number of Combination $C(n, r)$,
  $$
  C(n, r) = |f_\text{Conbination}(S, k)| = \frac{n!}{(n - m)! m!}  \tag{number of Conbination}
  $$

- Property    
  - $C(n,r) = C(n-1,r-1) + C(n-1,r)$
  - $C(n,r) = C(n,n-r)$
  - The union of all Combination of a set $S$ is the power set $P(S)$ of the set $S$.
    $$
    \bigcup_{k=0}^n f_\text{Conbination}(S, k) = P(S)
    $$
    $$
    \begin{align*}
      \sum_{i=0}^n C(n,i) &= 2^n  \\
      \sum_{i=0}^n C(n,i)^2 &= C(2n, n)  \\
      \sum_{i=0}^n C(k+i,k)^2 &= C(n+k+1, k+1) 
    \end{align*}
    $$

