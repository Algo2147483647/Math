* Integer Ring
  - Define
    $$(\mathbb Z, +, \cdot)$$
    $$\forall a, b \in \mathbb Z, a \cdot b = 0 \quad\Rightarrow\quad  (a = 0 \vee b = 0)  \tag{no zero divisor}$$
    Integral ring is a nonzero commutative ring in which the product of any two nonzero elements is nonzero.

  - Property
    * Division with Remainder & Factor
    * Multiplicative Function
      - Define  
        A mapping $f: \mathbb Z \to \mathbb R$, such that
        $$f(a \times b) = f(a) f(b) \quad \text{when}\ a, b \in \mathbb Z, gcd(a, b) = 1$$

      - Property
        - $f(1) = 1$

      - Example
        * Eular Function
          - Define  
            The number of coprimes with $n$ in positive integers less than $n$.
            $$\phi(n) = \text{number}(\{i\ |\ i \in 1:n, \text{GCD}(i, n) = 1\})$$

          - Property
            $$\begin{align*}
              n &= \prod_i p_i^{k_i}  \\
              \phi(n) &= n \prod_{p|n} (1 - 1/p)  
            \end{align*}$$

        * Möbius Function