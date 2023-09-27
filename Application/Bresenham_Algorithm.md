* Bresenham Algorithm::Line
  - Problem  
    Input 2 points $\boldsymbol p^{(1)}, \boldsymbol p^{(2)} \in \mathbb Z^n$, if $\boldsymbol p \in \mathbb R^n$ in the line formed by $p^{(1)}$ and $p^{(2)}$, then

    $$\boldsymbol \delta = \boldsymbol p^{(2)} - \boldsymbol p^{(1)}$$

    $$a_i = \left(x_i - p^{(1)}_i \right) \prod_{j\in 1:n, j \neq i} \delta_j$$
    $$a_1 = a_2 = ... = a_n  \tag{line equation}$$

    we aim to find all Integer pixels $\boldsymbol p \in \mathbb Z^n$ that the line formed by $p_1$ and $p_2$ pass through.

  - Process  
    Bresenham algorithm aims to solve the problem without using any real number. We select the axis with maximum delta value as the reference axis, for each point in the line with $x_l = p_l^{(1)} + a, a \in \mathbb Z$, we have,
    $$l = \arg\max_{i} \delta_i$$

    $$x_l = p_l^{(1)} + a \quad\Rightarrow\quad x_i = p_i^{(1)} + \text{int}\left(\frac{\delta_{i}}{\delta_{l}} \cdot a \right)$$

    - Proof
      $$\begin{align*}
        \left(x_l - p_l^{(1)}\right) \delta_i &= \left(x_i - p_i^{(1)}\right) \delta_l  \\
        \left((x_l + 1) - p_l^{(1)}\right) \delta_i &= \left(x_i' - p_i^{(1)}\right) \delta_l \\
        \Rightarrow\quad x_i' - x_i &= \frac{\delta_i}{\delta_l}
      \end{align*}$$

* Bresenham Algorithm::Circle
  - Problem
    $$\begin{align*}
      x^2 + y^2 &= r^2  \tag{Circle, 2D}  \\
      x^2 + y^2 + z^2 &= r^2  \tag{Sphere, 3D} \\
      \|\boldsymbol p\|_2^2 = \sum_{i=1:\dim} p^{(i)2} &= r^2    \tag{any dimonsion}
    \end{align*}$$

    The target is to find all pixels $\boldsymbol p \in \mathbb Z^{\dim}$ that the boundary of Circle pass through,

  - Process   
    We only need to draw $\frac{1}{8}$ of a circle, and then we will get the whole circle through symmetry. If we start in $(0, r)$, then we draw in order  
    $$\left(\theta: \frac{\pi}{2} \to \frac{\pi}{4}, x: 0 \to \frac{r}{\sqrt{2}}, y: r \to \frac{r}{\sqrt{2}}, x \le y\right)$$  

    Therefore, the next position of each step is only $(x+1, y)$ and $(x+1, y-1)$. And, we only need to select the position with smaller error $\arg\min(\epsilon_1, \epsilon_2)$ by the positive and negative of $\delta$.

    $$\begin{align*}
      (x+1)^2 + y^2 - r^2 &= + \epsilon_1 \ge 0\\
      (x+1)^2 + (y-1)^2 - r^2 &= - \epsilon_2  \le 0
    \end{align*}$$

    $$\begin{align*}
      \delta &= + \epsilon_1 - \epsilon_2  \\
      &= ((x+1)^2 + y^2 - r^2) + ((x+1)^2 + (y-1)^2 - r^2)
    \end{align*}$$

    $$y \gets \left\{\begin{matrix}
        y \quad&; \delta_{x} < 0  \\
        y + 1 \quad&; \delta_{x} \ge 0
      \end{matrix}\right.$$

    Recursion formula and the initial value of $\delta$,

    $$\begin{align*}
      \delta_{(0,r)} &= 3 - 2 r  \\
      \delta_{x+1} &= \delta_{x} + \Delta \delta
    \end{align*}$$

    $$\begin{align*}
      \Delta \delta &= \delta_{x+1} - \delta_{x}  \\
      &= \left\{\begin{matrix}
        4 x + 6 \quad&; \delta_{x} < 0  \\
        4 x - 4 y + 10 \quad&; \delta_{x} \ge 0
      \end{matrix}\right.
    \end{align*}$$

    For higher dimensions, we only need to draw $\frac{1}{N}$ of a circle, through the positivity and negativity of axis $\frac{1}{2^{\dim}}$ and permutation of axis $\frac{1}{\dim !}$. And this area is divided by hyperplane $p^{(i)} = 0, p^{(i)} = p^{(j)}, \forall i, j \in \{1:\dim\}$.

    $$\frac{1}{N} = \frac{1}{2^{\dim} \cdot \dim !}$$

    We start from the initial point $(0, ..., 0, r)$, and satisfy:
    $$\begin{align*}
      \Delta p^{(i)} &\in \{0, +1\} \quad; \forall i \in \{1:\dim-1\}\\
      \Delta \boldsymbol p^{(1:\dim-1)} &\neq \boldsymbol 0  \\
      \Delta p^{(\dim)} &\in \{0, -1\}
    \end{align*}$$

    $$p^{(1)} \le p^{(2)} \le ... \le p^{(\dim)}$$

    Then, we search all feasible points satisfying $\epsilon \le r$ by ```queue``` and breadth-first search.

    $$\begin{align*}
    \Delta d &= \sqrt{\|p\|_2^2} - r \in \left[-\frac{\sqrt{\dim}}{2}, \frac{\sqrt{\dim}}{2}\right] \\
    \Rightarrow\quad \epsilon &= \left|\|p\|_2^2 - r^2 \right|  \\
    &= \left|(\Delta d + r)^2 - r^2\right|  \\
    &= \left|\Delta d^2 + 2 r \Delta d + r^2 - r^2\right|\\
    &= \left|\Delta d^2 + 2 r \Delta d\right|  \\
    &\in \left[0,r \sqrt{\dim}  +\frac{\dim}{4} \right] \\
    \end{align*}$$
