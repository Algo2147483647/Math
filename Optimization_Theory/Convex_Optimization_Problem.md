* Convex Optimization Problem
  - Define
    $$
    \begin{align*}
      \min \quad & f_0(x) \tag{$f_0$is Convex}\\ 
      s.t. \quad & f_i(x) ≤ 0 \tag{$f_i$is Convex}\\ 
        & a_i^T x = b_i  \tag{Affine function} 
    \end{align*}
    $$

  - Problem -- Solving Convex Optimization Problems

    - Problem -- Unconstrained Convex Optimization Problems
      $\min_{\boldsymbol x}\ f(\boldsymbol x)$
      其中$f(\boldsymbol x)$是可微凸函数

      最优性条件: $∇ f(\boldsymbol x^*) = 0$

      - Algorithm
        - Gradient Descent Method
          $$x_{k+1} = x_k - λ ∇ f(x_k)$$

        - Steepest Descent Method
          $$x_{k+1} = x_k + \arg\min \{ (∇ f(x_k))^T v\ |\ ||v|| = 1 \}$$

        - Newton Iteration Method
          $$x_{k+1} = x_k - \frac{1}{∇^2 f(x)} ∇ f(x_k)$$

        - Quasi-Newton Method

        - Block Coordinate Descent Method

    - Problem -- Solving Convex Optimization Problems with Equality Constraints

    - Algorithm
      * Interior Point Method

  - Include
    * Linear Programming
    * Linear Fractional Programming
      - Define
        $$
        \begin{align*}
          \min \quad & \frac{a^T x+ b}{c^T x + d}  \\
          s.t. \quad & Gx ⪯ 0  \\
            & Ax = b
        \end{align*}
        $$
        The problem can be equivalent to Linear Programming.

    * Quadratic Programming
      - Define
        $$
        \begin{align*}
          \min \quad & \frac{1}{2} x^T P x + q^T x + r  \\
          s.t. \quad & Gx ⪯ 0  \\
            & Ax = b
        \end{align*}
        $$

      - Example
        - Least Square Method
          $$\min ||Ax + b||_2^2$$

    * Quadratically Constrained Quadratic Programming ; QCQP
      - Define
        $$
        \begin{align*}
          \min \quad & \frac{1}{2} x^T P_0 x + q_0^T x + r_0  \\
          s.t. \quad & \frac{1}{2} x^T P_i x + q_i^T x + r_i ⪯ 0  \\
            & Ax = b
        \end{align*}
        $$

    * Quadratic Cone Programming
      - Define
        $$
        \begin{align*}
          \min \quad & f^T x  \\
          s.t. \quad & ||A_i x + b_i|| ≤ c_i^T + d_i  \\
            & Fx = g
        \end{align*}
        $$

    * Geometric Programming
      - Define
        $$
        \begin{align*}
          \min \quad & f_0(x)  \\
          s.t. \quad & f_i(x) ≤ 1  \\
            & h_i(x) = 1
        \end{align*}
        $$
        The natural form is not Convex, but can be transformed into a Convex Optimization Problem.
        
    * Semi-Definite Programming

    - Note
      $$Quadratic Cone Programming \supset \{Quadratic Programming \supset \{ Linear Programming \} , Quadratically Constrained Quadratic Programming\}$$
        