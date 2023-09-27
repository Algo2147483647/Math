* Convex Set
  - Define  
    $$\forall \boldsymbol x_i \in C, θ_i \in [0,1], \sum θ_i = 1 \quad \text{, then}\quad \sum θ_i x_i \in C$$

    A comvex set is a set such that the line segment between any two points in the set is still in the set.

  - Property  
    - Convex Set $C$的任意边界点, 均存在支撑超平面.

    * Convex Hull
      - Define  
        $$\text{conv}(C) = \left\{\sum θ_i x_i\ |\ x_i\in C, θ_i \in [0,1], \sum θ_i = 1 \right\}$$

        A convex hull is a set of points is the smallest convex polygon that contain all the input points.

        The set of convex combinations of all points in the set constitutes a convex hull This convex hull is also the smallest Convex Set containing all points in a given set.

        $$\mathcal X_{\text{Convex\ Hull}} \subseteq \mathcal X_{\text{input}}$$
        $$\mathcal X_{\text{input}} \subseteq \text{Polygon}(\mathcal X_{\text{Convex\ Hull}})$$

  - Include
    * Hyperplane & Half-Space
      - Define  
        $$\begin{align*}
          \{\boldsymbol x \ |\ \boldsymbol a^T \boldsymbol x = b\}  \tag{Hyperplane}\\
          \{\boldsymbol x \ |\ \boldsymbol a^T \boldsymbol x ≤ b\}  \tag{Half-Space}
        \end{align*}$$
      
      - Property
        - is Convex Set

    * Polyhedron