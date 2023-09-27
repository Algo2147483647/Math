* Common Divisor & Common Multiple
  - Define  
    A Common Divisor $c$ of two number $a, b \in \mathbb Z$ is a number such that 
    $$a = k_a \times c, \quad b = k_b \times c$$

    A Common Multiple $c$ of two number $a, b \in \mathbb Z$ is a number such that 
    $$c = k_a \times a, k_b \times b$$

  - Property
    * Greatest Common Divisor & Least Common Multiple
      - Define  
        Greatest Common Divisor is the maximum Common Divisor of two number $a, b \in \mathbb Z$ except $1$. 

        $$gcd(a, b) = \arg\max_c\ c \quad s.t.\ c | a, c | b$$

        Least Common Multiple is the minimum Common Multiple of two number $a, b \in \mathbb Z$.

        $$lcm(a, b) = \arg\min_c\ c \quad s.t.\ a | c, b | c$$
        
      - Property
        - /
          $$\begin{align*}
            gcd(a, b) &= gcd(b, a)  \\
            gcd(a, b) &= gcd(a - b, b) \quad;(a ≥ b)  \\
            gcd(a, b) &= gcd(a \% b, b)  \\
            gcd(k a, k b) &= gcd(k a, b)  \\
          \end{align*}$$

        - $lcm(a, b) = \frac{a \times b}{gcd(a, b)}$

        - $c | a, c | b \Rightarrow c | (u a + v b)$ 
          - proof
            $$\begin{align*}  
              u a + v b 
              &= u \times k_a \times c + v \times k_b \times c \\
              &= k \times c
            \end{align*}$$

        - $gcd(a, b) = gcd(b, a \% b)$
          - proof  
            For $a = q \times b + r$,  
            $$\begin{align*}  
              gcd(a, b) = gcd(b, a \% b) \Leftrightarrow \left\{\begin{matrix}
              c | a, c | b &\Rightarrow  c | r  &\text{(1)}\\
              c | b, c | r &\Rightarrow  c | a  &\text{(2)}
              \end{matrix}\right.
            \end{align*}$$


            For (1), 
            $$\begin{align*}
              \Rightarrow\quad k_a \times c &= k_b \times c \times q + r  \\
              \Rightarrow\quad r &= (k_b \times q - k_a) \times c  
            \end{align*}$$

            For (2), 
            $$\begin{align*}
              \Rightarrow\quad a 
              &= k_b \times c \times q + k_r  \times c  \\
              &= (k_b \times q + k_r)  \times c
            \end{align*}$$

      - Algorithm: Euclid's Algorithm -- finding Greatest Common Divisor
        $$\begin{align*}
          a = q \times b + r &\Rightarrow gcd(a, b) = gcd(b, a \% b)  \\
          a = q \times b &\Rightarrow gcd(a, b) = b
        \end{align*}$$

        ```cpp
        int gcd(int a, int b) { return b == 0 ? a : gcd(b, a %b); }
        ```
