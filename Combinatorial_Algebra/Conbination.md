* Conbination
  - Define
    $$f_\text{Conbination}(S, k) = \{ X \ |\ X \subseteq S , |X| = k\}  \tag{Conbination}$$ 
    Conbination, is the selection of $k$ elements from a set of $n$ elements without any regard to the order in which they are chosen.

    The number of Conbination $C(n, r)$,
    $$C(n, r) = |f_\text{Conbination}(S, k)| = \frac{n!}{(n - m)! m!}  \tag{number of Conbination}$$

  - Property    
    - $C(n,r) = C(n-1,r-1) + C(n-1,r)$
    - $C(n,r) = C(n,n-r)$
    - The union of all conbination of a set $S$ is the power set $P(S)$ of the set $S$.
      $$\bigcup_{k=0}^n f_\text{Conbination}(S, k) = P(S)$$ 
      $$\begin{align*}
        \sum_{i=0}^n C(n,i) &= 2^n  \\
        \sum_{i=0}^n C(n,i)^2 &= C(2n, n)  \\
        \sum_{i=0}^n C(k+i,k)^2 &= C(n+k+1, k+1) 
      \end{align*}$$
 
