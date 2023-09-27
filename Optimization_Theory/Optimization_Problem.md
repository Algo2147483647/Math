* Optimization Problem
  - Purpose  
    $$
    \begin{align*}
      \min \quad & f_0(x)  \tag{objective Function}\\
      s.t. \quad & f_i(x) ≤ 0  \tag{Inequality Constraint}\\
            & h_i(x) = 0  \tag{Equality Constraint}
    \end{align*}
    $$

    $$p^*= \inf \{f_{0}(x) | f_i(x) ≤ 0, h_i(x) = 0 \}  \tag{Optimal solution}$$

    Optimization Problem aims to find the minimal values called optimal solution $p^*$ of objective function $f_0(\cdot)$, subject to the constraints $f_i(\cdot), h_i(\cdot)$.

  - Include
    * Feasibility Problem
      - Define
        $$
        \begin{align*}
          \min_x \quad & const. \\
          s.t. \quad & f_i(x) ≤ 0  \\
                & h_i(x) = 0
        \end{align*}
        $$

        If the objective function is equal to a constant, the optimal solution is 0 (Feasible set is not empty) or $\infty$ (Feasible set is empty).

    * Convex Optimization Problem
    * Integer Programming & Mixed Integer Programming
    * Nonconvex Optimization Problem

  - Property
    * Lagrange Function
    * Lagrange Dual function, Dual Problem

  - Problem: Solving unconstrained optimization problems
    * Descent Method
      - Include 
        * Gradient Descent Method  
          $$\boldsymbol x_{k+1} = x_k - \alpha_k \nabla f(\boldsymbol x_k)$$

          - Inlcude
            * Steepest Descent Method
              $$\boldsymbol x_{k+1} = \boldsymbol x_k + \alpha_k \cdot \arg\min \{ (\nabla f(\boldsymbol x_k))^T \boldsymbol v \ |\ ||\boldsymbol v|| = 1 \}$$

            * Stochastic Gradient Descent

            * Adaptive Moment Estimation

        * Newton-Raphson Method
          $$\boldsymbol x_{k+1} = \boldsymbol x_k - \alpha_k (\nabla^2 f(\boldsymbol x_k))^{-1} \nabla f(\boldsymbol x_k)$$

        * Quasi-Newton Method
          $$\boldsymbol x_{k+1} = \boldsymbol x_k - \alpha_k B_k^{-1} \nabla f(\boldsymbol x_k)$$

          Where, $B_k^{-1}$ is an approximate Hessian matrix to simplify the time consuming calculation of the Hessian matrix.


  
    