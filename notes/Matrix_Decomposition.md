* Matrix Decomposition
  - Include
    * LU decomposition
      - Define
        $$A = L R$$
        The matrix $A$ is decomposed into the product of upper triangular matrix $R$ and lower triangular matrix $L$.

    * 上下三角对角分解
      - Define  
        将矩阵A化成上三角矩阵R, 对角矩阵D, 下三角矩阵L的乘积.$A = L D R$

    * 对称三角分解  
      - Define  
        $$A = G G^T$$
        将对称正定矩阵化成对称的两个上下三角矩阵.

      - Algorithm
        - first LU decomposition
          Because symmetric positive definite matrix
          $$A = L D U = L D L^T$$
          $$
          \begin{align*}
            A &= L (\sqrt{D})^2 L^T  \\
              &= (L \sqrt{D}) (\sqrt{D} L^T)  \\
              &= (L \sqrt{D}) (L \sqrt{D})^T  \\
              &= G G^T
          \end{align*}
          $$

    * QR decomposition
      - Define  
        $$A = Q R$$
        The nonsingular matrix A is decomposed into the product of orthogonal matrix Q and nonsingular upper triangular matrix R

      - Algorithm
        - Schmidt Orthogonalization method
          - $A = (a_1, ..., a_n)$
          - Schmidt Orthogonalization
            $$b_i = a_i - \sum_{k=1}^{i-1} \frac{<a_i,b_j>}{<b_j,b_j>}b_j$$
            
            $$
            \begin{align*}
              Q &= ( \frac{b_1}{|b_1|}, ... , \frac{b_n}{|b_n|} )  \\
              R &= \left(\begin{matrix} |b_1|\\ & \ddots\\ && |b_n| \end{matrix}\right) \left(\begin{matrix} 1 & k_{21} & ... & k_{n1} \\ & 1 & ... & k_{n2} \\& & \ddots & \vdots \\& & & 1 \end{matrix}\right) \quad; k_{ij} = \frac{<a_i,b_j>}{<b_j,b_j>}  \\
              A &= Q R
            \end{align*}
            $$

        - 初等旋转变换方法
          - 对第1列, 初等旋转变换使其变为 $T_i a_1 = (b_{11}, 0,...,0)$
          - $T_i = \prod_{i=0}^{n-1} T_{i(n-1-j)}$
          - 重复上面步骤, 直至将 $A_i$ 化为上三角矩阵
            $$
            \begin{align*}
              R &= A_{n-1}
              Q &= \left(\prod_{i=0}^{n-1} T_{n-1-i} \right)^T
              A &= Q R
            \end{align*}
            $$

        - 初等反射变换方法
          - 对第1列, 初等旋转变换使其变为 $H_i a_1 = (b_{11}, 0,...,0)$
            $$
            \begin{align*}
              u_i &= \frac{b_i - |b_i|}{| b_i - |b_i| |}
              H_i &= I - 2 u u^T
              A_{i+1} &= H_i A_i
            \end{align*}
            $$

          - Repeat the above steps, until $A_i$ into upper triangular matrix
            $$
            \begin{align*}
              R &= A_{n-1}
              Q &= \left(\prod_{i=0}^{n-1} H_{n-1-i} \right)^T
              A &= Q R
            \end{align*}
            $$

    * Full Rank decomposition
      - Define  
        $$A = F G$$

        - Proof  
          $$A =P^{-1} B = \left(\begin{matrix} F & S \end{matrix}\right) \left(\begin{matrix} G\\ 0 \end{matrix}\right) = F G$$
          
      - Algorithm  
        $$A = F G$$  
        初等行变换, 取A左侧rank(A)列作为F, 则
        $$A \to \left(\begin{matrix} G \\ 0 \end{matrix}\right)$$

    * Eigenvalue Decomposition & Singular Value Decomposition