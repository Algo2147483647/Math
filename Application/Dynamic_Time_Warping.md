* Dynamic Time Warping , DTW
  - Purpose  
    $$\begin{align*}
      \min_P \quad& \sum_{(a_i, b_j) \in P} f((a_i, b_j))  \tag{DTW}\\
      s.t. \quad
      & \exists (a_i, \cdot), (\cdot, b_j) \in P , \forall a_i \in a, b_j \in b  \\
      & (a_1, b_1) \in P  \\
      & (a_{n_a}, b_{n_b}) \in P  \\
      & \text{if } i > j, (a_i, b_{i'}), (a_j, b_{j'}) \in P \Rightarrow i' \ge j'
    \end{align*}$$ 
    Dynamic Time Warping aims to calculates an optimal match of the minimum sum of measures between two given sequences $a, b$ with certain restriction,
    - Every index from $a$ must be matched with one or more indices from $b$, and vice versa
    - The first index from $a$ must be matched with the first index from $b$. And the last index from $a$ must be matched with the last index from $b$ (but it does not have to be its only match)
      $$a_1 \leftrightarrow b_1$$
      $$a_{n_a} \leftrightarrow b_{n_b}$$
    - The mapping of the indices from the first sequence to indices from the other sequence must be monotonically increasing, and vice versa.
      $$i > j, a_i \leftrightarrow b_{i'}, a_j \leftrightarrow b_{j'} \Rightarrow i' \ge j'$$

  - Process  
    Dynamic programming,
    $$f((a_i, b_j)) = d((a_i, b_j)) + \min(f((a_{i-1}, b_j)), f((a_i, b_{j-1})), f((a_{i-1}, b_{j-1})))$$
    $$f((a_1, b_1)) = d((a_1, b_1))  \tag{initial}$$
      