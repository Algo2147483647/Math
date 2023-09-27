* Stochastic Point Process
  - Define  
    Stochastic Point Process is a collection of random variables $\{X(t) : t \ge 0\}$, where $X(t)$ represents the location or time of occurrence of a point at time $t$. 

  - Include
    * Poisson Point Process
      - Define  
        Poisson point process is a stochastic process that models the random spatial distribution of events in a continuous space, which satisfies,
          - Spatial homogeneity. For any region $A$, the value of the number of events occurring in the region $N(A)$ depends only on the size of the Lebesgue measure  (such as area, volume) of $A$ and is independent of the position and shape of $A$. 
          - Independent. For any disjoint measurable regions $A_1, A_2, \ldots, A_n$, the random variables $N(A_1), N(A_2), \ldots, N(A_n)$ are independent of each other.
          - The average rate of occurrence of events is constant throughout the space. And, $N(A)$ follows a Poisson distribution with constant intensity $\lambda> 0$. Where $\mu_A$ is the Lebesgue measure of $A$,
            $$\mathbb P(N(A) = n) = \frac{\lambda \cdot \mu_A}{n!} e^{\lambda \cdot \mu_A}$$ 
            $$\mathbb E(N(A)) = \lambda \cdot \mu_A$$