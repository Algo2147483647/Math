* Linear Diophantine Equation
  - Define
    $$a x + b y = c$$
    where, $a, b, c \in \mathbb Z$ is ciefficient, $x, y  \in \mathbb Z$ is unknown number.

  - Property
    - $ax + by = c$ has a solution $\quad\Leftrightarrow\quad$ $\text{gcd}(a, b) \% c = 0$

  - Algorithm
    * Extended Euclidean Algorithm
      - Purpose  
        Solve the $x, y  \in \mathbb Z$ in equations:
        $$a x + b y = \text{gcd}(a, b)$$

      - Process  
        Start with two integers $a, b \in \mathbb Z$, where $a \ge b$.

        If $b \% a = 0$, return $gcd(a, b) = b$, $(x, y) = (0, 1)$, because of $0 \cdot a + 1 \cdot b = b$.

        If $b \% a \neq 0$, we solve $b x' + (a \% b) y' = gcd(b, a \% b)$, and
        $$\begin{align*}
          x &= y'\\
          y &= x' - \text{int}(a / b) \cdot y'
        \end{align*}$$

        ```c
        // a >= b
        int gcdExtended(int a, int b, int *x, int *y) {
            if (b == 0) { *gcd = a; *x = 1; *y = 0; return a; }

            int x1, y1, gcd = gcdExtended(b, a % b, &x1, &y1);
            *x = y1;
            *y = x1 - (a / b) * y1;
            return gcd;
        }
        ``` 

  - Include
    * System of Linear Diophantine Equations
      - Define  
        $$A X = C$$ 
        where, $A \in \mathbb Z^{m \times n}$ is a matrix of integers, $X \in \mathbb Z^n$ is a vector of unknowns and $C \in \mathbb Z^m$ is a vector of integers.

      - Include
        * Chinese Remainder Theorem
          - Purpose   
            Solve a class of linear Diophantine systems of equations: 
            $$\begin{align*}
              x - n_1 x_1 &= a_1  \\
              \vdots &= \vdots  \\
              x - n_k x_k &= a_k
            \end{align*}$$  
            
            where, $(n_1, ..., n_k \in \mathbb Z)$ are pairwise coprime integers greater than one, $(x, x_1, ..., x_k \in \mathbb Z)$ are unknowns.