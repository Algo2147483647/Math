* Topological Space & Open Set
  - Define  
    Topological space $\tau$ is a collection of subsets of $S$, called the Open Sets, that satisfy certain axioms,

    - The empty set and $S$ itself belong to $\tau$.
      $$\{\emptyset, S\} \subseteq \tau$$ 
    - The intersection of any finite members of $\tau$ belongs to $\tau$.
    - Any arbitrary (finite or infinite) union of members of $\tau$ belongs to $\tau$.

  - Concept
    * Closed Set
      - Define  
        Closed Set is the complementary set of Open Set.  

  - property
    * Homeomorphism
      - Define  
        A function $f: X \to Y$ between two topological spaces is a homeomorphism if it has the following properties,
        - $f$ is a bijection 
        - $f$ is continuous
        - the inverse function $f^{-1}$ is continuous ($f$ is an open mapping).
        
    * Chart
      - Define  
        Chart $(U, \phi)$ on a set is a bijection $\phi: U \subseteq M \to \phi(U) \subseteq \mathbb R^n$, where $U, \phi(U)$ is open.

        A chart $(U, \phi)$ is centered at $p$ for $p \in U$ if $\phi(p) = 0$.

    * Borel $\sigma$-algebra 

  - Include
    * Hausdorff Space
      - Define  
        Hausdorff Space $X$ is a topology space where, for any distinct points $x, y \in X$, there exist a neighborhood $U$ of $x$ and a neighborhood $V$ of $y$ such that $U$ and $V$ are disjoint.
        $$U \cap V = \emptyset$$ 

      - Include
        * Metric Space  
        * Manifold
          - Define  
            Manifold $M$ is a second countable Hausdorff space that is locally homeomorphic to a Euclidean space.
            - Hausdorff, $\forall x, y \in M$, there exists open neighborhoods $U_x, U_y \subseteq M$ with $x \in U_x, y \in U_y$ and $U_x \cap U_y = \emptyset$.   
            - Second countable, there exits a countable collection $(U_n)_{n \in \mathbb N}$ of open set in $M$ such that for all $V \subseteq M$ open, and $p \in V$, there is some $n$ such that $p \in U_n \subseteq V$
            - Locally homeomorphic to a Euclidean space, every point has a neighborhood $U$ homeomorphic $\phi: U \to V$ to an open subset $V$ of the Euclidean space $\mathbb R^n$ for some nonnegative integer $n$.