* Random Variable & Random Vector
  - Define  
    Random Variable:
    $$X: Ω \to \mathbb R  \tag{Random Variable}$$
    a random variable $X$ is a function from a sample space $Ω$ to the real numbers $\mathbb R$.

    Symbol:
      - $Ω$: sample space
      - $\mathbb R$: the field of real numbers

    - Note  
      event set $\{ζ | X(ζ) ≤ x\}$, shorthand as $\{X ≤ x\}$.

    Random Vector ; Multivariate random variable:
    $$\boldsymbol X = (X_1, ... , X_n)^T  \tag{Random Vector}$$ 

  - Property
    * Probability Mass Function  
      - Define   
        for a discrete Random Variable $X$
        $$\mathbb P(X = x)$$

      - Property
        - Nonnegative
          $$\mathbb P(X = x) > 0$$

        - Sums to 1
          $$\sum_i \mathbb P(X = x_i) = 1$$ 

    * Cumulative Distribution Function
      - Define  
        $$
        \begin{align*}
          F_X(x) &= \mathbb P(X ≤ x)  \\
          F_{\boldsymbol X}(x) &= \mathbb P(X_1 ≤ x_1, ..., X_n ≤ x_n) = \mathbb P(\boldsymbol X ≤ \boldsymbol x)
        \end{align*}
        $$

    * Probability Generating Function
      - Define  
        For a discrete random variable $X$ taking values in the non-negative integers $x \in \mathbb Z$, the Probility Generating Function is  
        $$G(z) = \mathbb E(z^x) = \sum_{i=0}^\infty z^x \mathbb P(x)$$ 

      - Property
        - $G(1) = 1$
        - $\mathbb P(X = x) = \frac{G^{(k)}(0)}{x!}$
        - $\mathbb E(X) = G'(1)$
        - $Var(X) = G''(1) + G'(1)(1 - G'(1))$ 
        - $\mathbb E(X^k) = \left(z \frac{\partial }{\partial z}\right) G(z)|_{z = 1}$

    * Probability Density Function
      - Define  
        $$
        \begin{align*}
          f_X(x) &= \frac{\mathrm d F_X(x)}{\mathrm d x}  \\
          f_{\boldsymbol X}(\boldsymbol x) &= \frac{∂^n F_{\boldsymbol X}(x)}{∂ x_1 ... ∂ x_n}  \\
          f_{X_i}(x_i) &= \int_{-\infty}^\infty ... \int_{-\infty}^\infty f_{\boldsymbol X}(\boldsymbol x) \mathrm d x_1 ... \mathrm d x_j ... \mathrm d x_n |_{j ≠ i}  \tag{Marginal Probability Density}
        \end{align*}
        $$

    * Moment
     
  - Problem: generation of random number
    * Mersenne Twister 