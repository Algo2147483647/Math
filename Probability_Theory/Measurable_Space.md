* Measurable Space & Measure Space
  - Define  
    A Measurable Space is a pair $(E, \mathcal E)$, where $E$ is a set and $\mathcal E$ is its $\sigma$-algebra.

    A Measure Space is a pair $(E, \mathcal E, \mu)$, where $E$ is a set and $\mathcal E$ is its $\sigma$-algebra, $\mu$ is a Measure on $(E, \mathcal E)$  
    
  - Concept  
    * Measure  
      - Define  
        A Measure on a measurable space $(E, \mathcal E)$ is a function $\mu: \mathcal E \to [0, \infty)$ such that 
        - $\mu (\emptyset) = 0$
        - Countable additivity: For any disjoint sequence $(A_1, ..., A_n), A_i \in \mathcal E$, then
          $$\mu \left(\bigcup_i A_i\right) = \sum_i \mu(A_i)$$   

      - Include
        * Lebesgue Measure 
        * Probability

  - Include
    * Probability Space
