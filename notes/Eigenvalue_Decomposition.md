* Eigenvalue Decomposition & Singular Value Decomposition
  - Define  
    **Eigenvalue Decomposition**, for a square matrix $\boldsymbol A \in \mathbb R^{n \times n}$, 
    $$\begin{align*}
      \boldsymbol A 
      &= \boldsymbol Q \boldsymbol \Lambda \boldsymbol Q^{-1}  \\
      &= \boldsymbol Q \boldsymbol \Lambda \boldsymbol Q^{\mathrm T}  \\
    \end{align*}$$  

    where, $\boldsymbol Q$ is an orthogonal matrix $\boldsymbol Q^{\mathrm T} \boldsymbol Q = \boldsymbol I$ composed of eigenvectors $\boldsymbol v$, $\Lambda$ is composed of eigenvalues $\lambda$, 
    $$\begin{align*}
      \boldsymbol Q &= (\boldsymbol v_1, ..., \boldsymbol v_n)  \\
      \boldsymbol \Lambda &= \left(\begin{matrix} \lambda_1 && 0 \\ &\ddots \\ 0 && \lambda_n \end{matrix}\right)
    \end{align*}$$

    - Proof
      $$\boldsymbol A \boldsymbol v_i = \lambda_i \boldsymbol v_i$$
      $$\begin{align*}
        \Rightarrow \boldsymbol A (\boldsymbol v_1, ..., \boldsymbol v_n) &= (\boldsymbol v_1, ..., \boldsymbol v_n) \left(\begin{matrix} \lambda_1 && 0 \\ &\ddots \\ 0 && \lambda_n \end{matrix}\right)  \\
        \boldsymbol A &= (\boldsymbol v_1, ..., \boldsymbol v_n) \left(\begin{matrix} \lambda_1 && 0 \\ &\ddots \\ 0 && \lambda_n \end{matrix}\right) (\boldsymbol v_1, ..., \boldsymbol v_n)^{-1}  \\
        \boldsymbol A &= \boldsymbol Q \Lambda \boldsymbol Q^{-1}
      \end{align*}$$

    - Note  
      The geometric significance of Eigenvalue Decomposition is that a linear transformation $\boldsymbol A \boldsymbol x$ is equivalent to (1) $\boldsymbol Q^{-1} \boldsymbol x$, convert to a new coordinate system with eigenvectors of $\boldsymbol A$ as unit bases; (2)$\boldsymbol \Lambda (\boldsymbol Q^{-1} \boldsymbol x)$, a scale transform; (3)$\boldsymbol Q (\boldsymbol \Lambda \boldsymbol Q^{-1} \boldsymbol x)$, convert to original coordinate system.

    **Singular Value Decomposition**, for a matrix $\boldsymbol A \in \mathbb R^{m \times n}$,  
    $$\boldsymbol A = \boldsymbol U \left(\begin{matrix} \boldsymbol \Sigma & \boldsymbol 0 \\ \boldsymbol 0 & \boldsymbol 0 \end{matrix}\right) \boldsymbol V^{\mathrm H}$$

    where, $\boldsymbol U \in \mathbb R^{m \times m}, \boldsymbol V \in \mathbb R^{n \times n}$ are unitary matrixs $\boldsymbol U^{\mathrm H} \boldsymbol U = \boldsymbol I, \boldsymbol V^{\mathrm H} \boldsymbol V = \boldsymbol I$, $\boldsymbol \Sigma$ is composed of nonzero singular values.

    - Note
      $$\exists \text{Unitary Matrix} U, V \Rightarrow U^H A V = \left(\begin{matrix} Σ & 0 \\ 0 & 0 \end{matrix}\right)$$

  - Algorithm  
    $A^{\mathrm T} A$ 计算特征值 $λ$, 特征向量$v'$, 并归一化求得 $\boldsymbol V, \boldsymbol Σ, \boldsymbol U$,

    $$(\boldsymbol A^{\mathrm T} \boldsymbol A) \boldsymbol v'_i = \lambda_i \boldsymbol v'_i$$

    $$\begin{align*}
      \boldsymbol V &= \left(\frac{\boldsymbol v'_1}{\|\boldsymbol v'_1\|_2}, ... ,\frac{\boldsymbol v'_n}{\|\boldsymbol v'_n\|_2} \right)  \\
      \boldsymbol Σ &= \text{diag}\left(\sqrt{λ_1}, ... ,\sqrt{λ_n}\right)  \\
      \boldsymbol U' &= \boldsymbol A \boldsymbol V \boldsymbol Σ^{-1}  \\
      \boldsymbol U &= \left(\frac{\boldsymbol u'_1}{\|\boldsymbol u'_1\|_2}, ... ,\frac{\boldsymbol u'_n}{\|\boldsymbol u'_n\|_2} \right)  
    \end{align*}$$

  - Property
    $$
    \begin{align*}
      Range(A) &= Span(u_1, ..., u_r)  \\
      Null (A) &= Span(v_{r+1}, ... , v_n)  \\
      Range(A^{\mathrm T}) &= Span(v_1, ..., v_r)  \\
      Null (A^{\mathrm T}) &= Span(u_{r+1}, ... , u_m)  \\
      A &= \sum_{i=1}^{r} σ_i u_i v_i^H
    \end{align*}
    $$
    
    - Proof
      $$
      \begin{align*}
        A &= \left(\begin{matrix} U_{1:r} & U_{r+1:m} \end{matrix}\right) \left(\begin{matrix} Σ & 0 \\ 0 & 0 \end{matrix}\right) \left(\begin{matrix} V_{1:r}^H \\ V_{r+1:n}^H \end{matrix}\right)  \tag{定义式变形}  \\
          &= U_{1:r} Σ V_{1:r}^H
      \end{align*}
      $$

      $$
      \begin{align*}
        Range(A) &= \{y\ |\ A x = y\}  \\
          &= \{y\ |\ U_{1:r} (Σ V_{1:r}^H x) = y\}  \tag{代入}  \\
          &\subseteq Range(U_{1:r})  \\
        Range(U_{1:r}) &= \{y\ |\ U_{1:r} x = y\}  \\
          &= \{y\ |\ A (V_{1:r} Σ^{-1} x) = y\}  \tag{$U_{1:r} = A V_{1:r} Σ^{-1}$}  \\
          &\subseteq Range(A)
      \end{align*}
      $$

      $$
      \begin{align*}
        \Rightarrow Range(A) = Range(U_{1:r}) = Span(u_1, ..., u_r)
      \end{align*}
      $$