* Linear Programming
  - Define
    $$\begin{align*}
      \min \quad & c^T x + d  \tag{Linear Programming}\\
      s.t. \quad & G x ⪯ h  \\
        & A x = b
    \end{align*}$$
    A optimization problem, which both objective function and constraint function are affine function.
    
    - Standard form
      $$\begin{align*}
        \min \quad & c^T x  \tag{Standard form}\\
        s.t. \quad & A x = b  \\
          & x ⪰ 0
      \end{align*}$$
    - Inequality form
      $$\begin{align*}
        \min \quad & c^T x  \\
        s.t. \quad & A x ⪯ b  \\
      \end{align*}$$

  - Property
    - The feasible region of a linear programming problem is a polyhedron, and the equipotential curve is a hyperplane orthogonal to the vector $c^T$. The optimal solution is the vertex in the polyhedron that is farthest in the direction of $-c^T$.
    - If there are two optimal solutions to a linear programming problem, there must be an infinite number of optimal solutions
    - fundamental theorem of linear programming  
      For a linear programming problem, if the maximum or minimum value of its objective function exists, then its optimal solution must be on a vertex or boundary of a convex polyhedron. 
  
  - Algorithm: Convert linear programming to standard form
    - Process  
      Introducing Relaxation Variables into Inequalities
      $$\begin{align*}
        \min \quad & c^T x + d  \\
        s.t. \quad & G x + s = h  \\
          & A x = b  \\
          & s ⪰ 0
      \end{align*}$$

      Express $x$ as the difference between two non negative variables $x = x^+ - x^-, x^+ ⪰ 0, x^- ⪰ 0$, just substitute.
      $$\begin{align*}
        \min \quad & c^T x^+ - c^T x^- + d  \\
        s.t. \quad & G x^+ - G x^- + s = h  \\
          & A x^+ - A x^- = b  \\
          & s ⪰ 0, x^+ ⪰ 0, x^- ⪰ 0
      \end{align*}$$

  - Algorithm: Solving Linear Programming
    * Simplex Method

      Due to the feasible solution set of linear programming is a high-dimensional simplex (the simplest polyhedron), and the optimal solution is on the vertex or boundary of the polyhedron, not inside the polyhedron. Therefore, we can find the optimal solution by walking along each vertex of the simplex.
