* Polyhedron
  - Define  
    $$\{\boldsymbol x \ |\ \boldsymbol a_j^T \boldsymbol x ≤ b_j, j = 1,...,m,\ \boldsymbol c_j^T \boldsymbol x = d_j, j = 1,...,p\}$$

    Polyhedron is the intersection of a finite hyperplane and a half space.

  - Property
    - Polyhedron is a convex set.

  - Include
    * Simplex
      - Define  
        $$C = \text{conv} (\{v_1, ..., v_k\}) = \left\{\sum_{i=1}^k \theta_i v_i \ |\ \theta ⪰ 0, \boldsymbol 1^T \theta=1 \right\}$$

        Simplex is a tpye of polyhedron with $n+1$ vertices in $n$-dimensional space. Where $\{v_1, ..., v_k \ |\ k = n + 1\}$ are affinely independent points.

      - Include 
        * Point
        * Line Segment
        * Triangle
          - Define 
          - Property
            - judge whether a point is inside the triangle

              We assume that the order of input vertices of the triangle $(\boldsymbol a, \boldsymbol b, \boldsymbol c)$ is counter clockwise.

              $$\left.\begin{matrix}
              (\boldsymbol b-\boldsymbol a) \times (\boldsymbol p-\boldsymbol b) > 0\\
              (\boldsymbol c-\boldsymbol b) \times (\boldsymbol p-\boldsymbol c) > 0\\
              (\boldsymbol a-\boldsymbol c) \times (\boldsymbol p-\boldsymbol a) > 0\\
              \end{matrix} \right\} \Leftrightarrow \boldsymbol p \text{ is in Triangle}(\boldsymbol a, \boldsymbol b, \boldsymbol c)$$ 

          - Helen's formula
              $$S = \sqrt{q(q-a)(q-b)(q-c)}$$
              $$q = \frac{a + b + c}{2}$$ 

        * Tetrahedron
