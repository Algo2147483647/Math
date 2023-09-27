* Filtered Probability Space & Filtration
  - Define  
    $$(\Omega, \mathcal F, (\mathcal F_i)_{i \in I}, P)  \tag{Filtered Probability Space}$$ 
    Filtered Probability Space is a probability space with Filtration.

    $$(\mathcal F_i)_{i \in I}  \tag{Filtration}$$
    Filtration $(\mathcal F_i)_{i \in I}$ is a sequence of $\sigma$-algebra in a probability space $(\Omega, \mathcal F, P)$ and a index set $I$ with a total order $\le$, such that 
    $$\mathcal F_i \subseteq \mathcal F_j \quad, \forall i \le j$$

  - Problem
    * Stopping Time
      - Define  
        Stopping Time $\tau$ is a random variable defined on the filtered probability space $(\Omega, \mathcal F, (\mathcal F_n)_{n \in \mathbb N}, P)$ with value in $T = [0, +\infty)$, such that 
        $$\{\tau \le t\} \in \mathcal F_t \quad, \forall t \in T$$