# $Linear\ Space$

[TOC]

## Define  
$$
(\mathbb R, V, +, \cdot)  \tag{Linear Space}
$$
Linear Space is non empty set $V$ with addition and scalar multiplication ([Module](./Algebra_Structure.md)), and satisfying:

|Axiom|Meaning|
|---|---|
| 加法封闭 | $x+y \in V$ |
| 数乘封闭 | $k x \in V$ |
| Identity element of vector addition | $x+0=x$ |
| Inverse elements of vector addition | $x+(-x) = 0$ |
| Identity element of scalar multiplication | $1x = x$ |
| Commutativity of vector addition | $x+y = y+x$ |
| Associativity of vector addition | $x+(y+z) = (x+y) +z$ |
| Compatibility of scalar multiplication with field multiplication | $a(bx) = (a b)x$ |
| Distributivity of scalar multiplication with respect to vector addition | $a(x+y) = a x + a y$ |
| Distributivity of scalar multiplication with respect to field addition | $(a+b)x = ax+bx$ |
|||

addition,
$$
\boldsymbol A_{m \times n} + \boldsymbol B_{m \times n} = \boldsymbol C_{m \times n}  \tag{addition}
$$
$$
c_{ij} = a_{ij} + b_{ij}
$$

scalar multiplication,
$$
k \boldsymbol A_{m \times n} = (k a_{ij})_{m \times n}  \tag{scalar multiplication}
$$

## Concept

* Vector
  - Define
    $$
    \mathbb R^{n}, n \in \mathbb Z
    $$

* Matrix 
  - Define
    $$
    \mathbb R^{m \times n}, m, n \in \mathbb Z
    $$
    
  - Operation
    - multiplication
      $$
      \boldsymbol A_{m \times n} \times \boldsymbol B_{n \times p} = \boldsymbol C_{m \times p}
      $$
      $$
      c_{ij} = \sum_{k \in 1:n} a_{ik} b_{kj}
      $$

    - multiplication of elements, Hadamard product
      $$
      \boldsymbol A_{m \times n} \odot \boldsymbol B_{m \times n} = \boldsymbol C_{m \times n}
      $$
      $$
      c_{ij} = a_{ij} b_{ij}
      $$

  - Property

    - Algorithm: computer matrix mutiplication
      * General Matrix Multiplication

## Property

* Linear Independence & Linear Dependence
  - Define  
    For a vector group $(\boldsymbol x_1, ... , \boldsymbol x_n)$, we said  

    Linear Independence,
    $$
    \nexists\ \boldsymbol a ≠ \boldsymbol 0 \Rightarrow \sum_{i=1}^n a_i \boldsymbol x_i = \boldsymbol 0
    $$

    Linear Dependence,
    $$
    \exists\ \boldsymbol a ≠ \boldsymbol 0 \Rightarrow \sum_{i=1}^n a_i \boldsymbol x_i = \boldsymbol 0
    $$

- Dimension  
  In linear space, the maximum number of vectors contained in a linearly independent vector group.

* Base 
  - Define
    $$
    \begin{align*}
      \boldsymbol v 
      &= \sum_{i=1}^n a_i \boldsymbol x_i \quad, \forall \boldsymbol v \in V  \\
      &= \boldsymbol X \boldsymbol a
    \end{align*}
    $$
    Base is a linearly independent vector group $\boldsymbol X = (\boldsymbol x_1, ... , \boldsymbol x_n)$, All vectors in the linear space are linear combinations of the vector group.

    Symbol:
    - $\boldsymbol x_i$: Base vector
    - $a_i$: coordinate

  - Property 
    - Base Transformation & Coordinate Transformation  
      Base transformation, is a transformation between new bases $\boldsymbol Y$ and old bases $\boldsymbol X$, where $\boldsymbol C$ is the Transformation Matrix.
      $$
      \boldsymbol Y = \boldsymbol X \boldsymbol C
      $$
      
      Coordinate Transformation, is solving a new coordinate $\boldsymbol a_y$ in new base $\boldsymbol Y$ from old coordinate $\boldsymbol a_x$ in old base $\boldsymbol X$.
      $$
      \boldsymbol a_x = \boldsymbol C \boldsymbol a_y
      $$
      
      
      - Proof
        $$
        \begin{align*}
          \boldsymbol v 
          &= \boldsymbol X \boldsymbol a_x  \\
          &= \boldsymbol Y \boldsymbol a_y  \\ 
          &= \boldsymbol X \boldsymbol C \boldsymbol a_y  \\ 
          \Rightarrow \boldsymbol a_x &= \boldsymbol C \boldsymbol a_y
        \end{align*}
        $$

      - Property  
        The base transformation matrix $\boldsymbol C$ is nonsingular.

    - Span
      $$
      Span(\boldsymbol x_1,...,\boldsymbol x_n) = \left\{\boldsymbol v | \boldsymbol v = \sum_{i=1}^n a_i \boldsymbol x_i \right\}
      $$
      A representation of a linear space given by a basis vector.

* Linear Subspace
  - Define  
    A nonempty set in a linear space that is closed to linear operations.
    - 加法封闭 $x,y\in V_1 ,\quad x+y \in V_1$
    - 数乘封闭 $x \in V_1, k x \in V_1$

* [Linear Transformation](./Linear_Transformation.md)

## Include

* Normed Linear Space

## Problem
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