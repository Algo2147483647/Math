* Lebesgue Measure
  - Deinfe  
    For a measurable subset $E \subseteq \mathbb{R}^n$, $E$ is Lebesgue measurable, if for any $\epsilon > 0$, there exist a finite number of open boxes $Q_1, Q_2, \ldots, Q_m$ and their volumes $\text{vol}(Q_i)$, such that
    $$E \subset \bigcup_{i=1}^m Q_i$$
    $$\sum_{i=1}^m \text{vol}(Q_i) < \text{vol}(E) + \epsilon  \tag{Lebesgue measurable}$$

    And Lebesgue measure $\text{m}(E)$ of a measurable subset $E$ is defined as,
    $$\text{m}(E) = \inf\left\{\sum_{i=1}^\infty \text{vol}(Q_i) \ \middle|\ E \subset \bigcup_{i=1}^\infty Q_i \right\}  \tag{Lebesgue Measure}$$