* Cardinality & Counting
  - Define  
    $$|S| = \text{number}(S)  \tag{Cardinality}$$ 
    Cardinality $|S|$ is the number of elements in a set $S$.

  - Property
    * Addition theorem  
      for $S = \cap_{i=1}^n S_i, S_i \cap S_j = \emptyset (i ≠ j)$
      $$\Rightarrow |S| = \sum_{i=1}^n |S_i|$$

    * Multiplication theorem  
      for sets $S_A, S_B$, and
      $$\begin{align*}
        S &= \{(a, b) | a \in S_A, b \in S_B\}  \\
          &= S_A × S_B  \tag{Cartesian积}  \\
      \end{align*}$$
      $$\Rightarrow |S| = |S_A| × |S_B|$$

      - Proof
        $$\begin{align*}
          S 
          &= \{(a, b) | a \in S_A, b \in S_B\}  \\
          &= \bigcap_{a_i \in S_A} \{(a_i, b) | b \in S_B\}  \\
          \Rightarrow |S| &= \sum_{i=1}^{|S_A|} |S_B|  \tag{Addition theorem}  \\
          &= |S_A| × |S_B|  \\
        \end{align*}$$

    * Principle of Inclusion-Exclusion  
      for $A_1,...,A_n \subseteq S$
      $$\begin{align*}
        \left|\bigcup_{i=1}^n A_i\right| &= \sum_{k=1}^n \left((-1)^{k-1} \sum_{\substack{i_1,...,i_k \in 1:n \\ i_1≠...≠i_k}} \left|\bigcup_{i\in\{i_1,...,i_k\}} A_i\right|\right)
      \end{align*}$$

    - Special Counting Sequence
      * Catalan Numbers 
        - Define  
          $$\begin{align*}
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
          \end{align*}$$
          Catalan Numbers are a sequence of natural numbers.
        
    * Pigeonhole Principle  
      for $A_1, ..., A_n \subseteq A, |A| = n + 1$, $\Rightarrow \exists A_i, |A_i| ≥ 2$.
