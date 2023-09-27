* Orthogonal Matching Pursuit
  - Purpose  
    $$\begin{align*}
      \hat x = \arg\min_{z \in \mathbb R^m} \quad & \|b - \boldsymbol A x\|_2  \\
      s.t. \quad & \|x\|_0 \le s  \tag{sparsity constraints}
    \end{align*}$$
    For the input $b, \boldsymbol A$, we want to solve $x$ to minimize errors and satisfy sparsity constraints.

  - Process  
    First, initial $r_0 = b, \Lambda_0 = \emptyset$, and normalize all columns of $\boldsymbol A$ to unit $L_2$ norm, remove duplicated columns in $\boldsymbol A$.

    For $k = 1, 2, ..., s$ do, 
    $$\lambda_k = \arg\max_{j \notin \Lambda_{k-1}}|a_j^T r_{k-1}|$$
    $$\Lambda_k = \Lambda_{k-1} \cup \{\lambda_k\}$$
    $$x_k (i \in \Lambda_k) = \arg\min_x \|\boldsymbol A_{\Lambda_k} x - b\|_2, \quad x_k (i \notin \Lambda_k) = 0$$
    $$r_k \gets b - \hat b_k = b - \boldsymbol A x_k$$

    The key principle behind the OMP algorithm is that by selecting the most correlated basis vectors $a_j$, the algorithm is able to gradually reduce the residual signal $r_k$ and improve the approximation. 
