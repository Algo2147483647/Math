[TOC]


# $Derivative$

## Define  
For unary [functions](./Function.md), the derivative is
$$
\begin{align*}
  \frac{df}{dx} &= \lim_{Δx \to 0}  \frac{ f(x + Δx) - f(x - Δx) }{ 2 Δx }  \tag{First derivative}\\
  \frac{d^n f}{dx^n} &= \lim_{Δx \to 0} \frac{ f^{(n - 1)}(x + Δx) - f^{(n - 1)}(x - Δx)} { 2 Δx }  \tag{$n$-order derivative}
\end{align*}
$$

For multi-variate functions, the partial derivative is

$$
\begin{align*}
  \frac{∂f}{∂x_i} &= \frac{f(...,x_i + Δx_i,...) -  f(..., x_i - Δx_i, ...)}{2 Δx_i}  \\
  \frac{∂^2 f}{∂x_i^2}  
  &= \frac{f'(..,x_i+Δx_i,..) -  f'(..,x_i-Δx_i,..)}{Δx_i}   \\
  &= \frac{f(..,x_i+Δx_i) - 2·f(..,x) + f(..,x_i-Δx_i)}{Δx_i^2}  \\
  \frac{∂^2 f}{∂x_j ∂x_i}  
  &= \frac{\partial}{\partial x_j} \left(\frac{\partial f}{\partial x_i} \right)
\end{align*}
$$

## Property

- 线性性
- 乘法法则
- 链式法则

## Problem : discrete numerical calculation of Derivative

- Algorithm : Finite difference, central difference formulas
  $$
  f'(x) = \frac{f(x+Δx) -  f(x-Δx)}{2 Δx} + \epsilon(f,Δx)
  $$
  截断误差: $\epsilon(f,Δx) = h² f^{(3)}(c) / 6 = O(h²)$  
  精度: O(h²)  
  $$
  f'(x) = \frac{-f(x+2Δx) + 8·f(x+Δx) - 8·f(x-Δx) + f(x-2Δx) }{12 Δx} + \epsilon(f,Δx)
  $$
  截断误差: $\epsilon(f,Δx) = h^4 f^{(5)}(c) / 6 = O(h^4)$  
  精度: $O(h^4)$  

## Include

### Gradient & Divergence & Curl

- Define  
  Gradient $\nabla (\cdot): (f: \mathbb R^{\dim} \to \mathbb R) \to (f: \mathbb R^{\dim} \to \mathbb R^{\dim})$, reflects the direction of the maximum rate of change for function $f$ at point $\boldsymbol x_0$.
  $$
  \nabla f = \sum_{i=1}^{\dim} \frac{∂f}{∂x_i} \hat{\boldsymbol x_i} = \left(\begin{matrix}\frac{∂f}{∂x_1} \\ \vdots \\ \frac{∂f}{∂x_{\dim}}\end{matrix}\right)  \tag{Gradient}
  $$
  
  Divergence $\nabla \cdot (\cdot): (f: \mathbb R^{\dim} \to \mathbb R^{\dim}) \to (f: \mathbb R^{\dim} \to \mathbb R)$. For a vector field $\boldsymbol f(\boldsymbol x)$, the divergence is defined as the limit of the redio of the surface integral of $\boldsymbol f$ out of the closed surface $S$ of a valume $V$ enclosing point $\boldsymbol x_0$, as $V$ shrinks to $0$. The divergence represents the volume density of the outward flux of a vector field from an infinitesimal volume around a given point.
  $$
  \nabla · \boldsymbol f = \lim_{|V| \to 0} \frac{1}{|V|} \oint_{S(V)} \boldsymbol f \cdot \hat {\boldsymbol n} \mathrm d S \tag{Divergence}
  $$
  $$
  \nabla · \boldsymbol f = \sum_{i=1}^{\dim} \frac{∂f_{i}}{∂x_i}  \tag{Cartesian coordinates}
  $$
  
  Curl $\nabla \times (\cdot): (f: \mathbb R^{3} \to \mathbb R^{3}) \to (f: \mathbb R^{3} \to \mathbb R)$. For a vector field in three-dimensional $\boldsymbol f(\boldsymbol x)$, the curl is defined as the limit of the redio of the line integral of $\boldsymbol f$ along the boundary $C$ of a area $A$ enclosing point $\boldsymbol x_0$, as $A$ shrinks to $0$. The curl represents the circulation density at each point of the field. 方向是旋转度最大的环量的旋转轴, 旋转的方向满足右手定则, 大小是绕该旋转轴旋转的环量与旋转路径围成的面元面积之比.
  $$
  \nabla \times \boldsymbol f = \lim_{A \to 0} \frac{1}{|A|} \oint_{C} \boldsymbol f \cdot \mathrm d \boldsymbol r \tag{Curl}
  $$
  $$
  \begin{align*}
    \nabla \times \boldsymbol f =& \left(\frac{∂f_z}{∂y} - \frac{∂f_y}{∂z} \right) \hat{\boldsymbol x} + \\
    & \left(\frac{∂f_x}{∂z} - \frac{∂f_z}{∂x} \right) \hat{\boldsymbol y}  +\\
    & \left(\frac{∂f_y}{∂x} - \frac{∂f_x}{∂y} \right) \hat{\boldsymbol z}  \tag{3D Cartesian coordinates}
  \end{align*}
  $$
  
- Property
  - $\nabla \times (\nabla \phi) = 0$, for any scalar field $\phi$.
  - $\nabla \cdot (\nabla \times \boldsymbol F) = 0$, for any vector field (in three dimensions) $\boldsymbol F$. 
  - $\nabla \cdot (\phi \boldsymbol F) = (\nabla \phi) \cdot \boldsymbol F + \phi (\nabla \cdot \boldsymbol F)$
  - $\nabla \times (\phi \boldsymbol F) = (\nabla \phi) \times \boldsymbol F + \phi (\nabla \times \boldsymbol F)$

# $Integral$

## Define  

$$
\int f(x) \mathrm d x  = F(x)  + const.\tag{Integral}
$$
Integral $f: (f: \mathbb R \to \mathbb R) \to (f: \mathbb R \to \mathbb R)$ represents the anti-derivative of a function $f(x)$. For a given function $f(x)$, an indefinite integral of $f(x)$ is another function $F(x)$ such that the derivative of $F(x)$ with respect to $x$ is equal to $f(x)$.


## Riemann Integra

$$
\int_a^b f(x) \mathrm d x = F(b) - F(a) \tag{Definite Integral}
$$

Definite Integral $f: (\mathbb R, \mathbb R, f: \mathbb R \to \mathbb R) \to \mathbb R$ of a function f(x) over an interval $[a, b]$ is the limit of a sum of rectangular areas as the width of the rectangles approaches zero. 


## Problem : discrete numerical calculation of Integral

- Algorithm : Newton–Cotes formulas
  $$
  \int_a^b f(x) \mathrm d x = (b - a) \sum_{k=0}^n  C_k^{n} f(x_i)
  $$
  $$
  C_k^{n} = (-1)^{n-k}(n·k!(n-k)!) \int_0^n \prod_{k≠j} (t-j) \mathrm d t
  $$
  $n = 1$: $C = \{\frac{1}{2}, \frac{1}{2}\}$  
  $n = 2$: $C = \{\frac{1}{6}, \frac{4}{6}, \frac{1}{6}\}$  
  $n = 4$: $C = \{\frac{7}{90}, \frac{32}{90}, \frac{12}{90}, \frac{32}{90}, \frac{7}{90}\}$   
  Newton–Cotes formulas 在 $n > 8$ 时不具有稳定性

- Algorithm : 复合求积法  
  将积分区间分成若干个子区间, 再在每个子区间使用低阶求积公式.

# $Differential\ Equation$

## Define
$$f \left(x, y, \frac{\mathrm d y}{\mathrm d x}, \frac{\mathrm d^2 y}{\mathrm dx^2}, ..., \frac{\mathrm d^n y}{\mathrm d x^n} \right) = 0  \tag{ODE}$$ 
Ordinary differential equation (ODE) is an equation that relates an unknown function $y$ to its derivatives with respect to a single independent variable $x$.  

$$f \left(D^k u(x), ... , D^2 u(x), u(x), x \right) = 0  \tag{PDE}$$
$$f: \mathbb R^{n^k} \times \mathbb R^{n^{k-1}} \times \mathbb R^n \times \mathbb R \times \Omega \to \mathbb R \quad; x \in \Omega; u: \Omega \to \mathbb R$$
Partial differential equation (PDE) is an equation that relates an unknown function $u$ of two or more variables to its partial derivatives with respect to those variables.

## Algorithm: Solving Ordinary Differential Equation

* Runge Kutta Method   
  - Process 
    Ordinary differential equations  
    $$\begin{align*}
      \boldsymbol y' &= f(\boldsymbol  x, \boldsymbol  y)  \\
      \boldsymbol  y(\boldsymbol  x_0) &= \boldsymbol  y_0
    \end{align*}$$
    Iterative solve Numerical solution for a point/interval of $\boldsymbol  y(x)$.
    $$\begin{align*}
      y(x + dx) &= y(x) + \frac{dx}{6} · (k_1 + 2 k_2 + 2 k_3 + k_4)  \\
      k_1 &= f \left(x_n , y_n \right)            \tag{Interval start slope}  \\
      k_2 &= f \left(x_n + \frac{dx}{2}, y_n + \frac{dx}{2}·k_1 \right)    \tag{Interval midpoint slope, through the Euler method $k_1$ determines $y$ at $x_n+\frac{dx}{2}$}  \\
      k_3 &= f \left(x_n + \frac{dx}{2}, y_n + \frac{dx}{2}·k_2 \right)    \tag{Interval midpoint slope,$k_2$ determines $y$ value}  \\
      k_4 &= f \left(x_n + dx, y_n + dx·k_3 \right)  \tag{Interval end slope}
    \end{align*}$$

  - Property  
    The RK4 method is a fourth order method, with each step error of order $h^4$, and the total cumulative error of order $h^5$

## Include

### Linear Differential Equation

- Define
  $$
  \sum_{k=0}^K a_k(x) u^{(k)}(x) = f(x)  \tag{Linear ODE}
  $$
  $$
  \sum_{k=0}^K a_k(x) D^k u(x) = f(x)  \tag{Linear PDE}
  $$

- Property
  - The solution set of a linear differential equation constitutes a linear space.

### Second Order Nonlinear Partial Differential Equation

- Define
  $$
  \sum_{ij} a_{ij}(x) \frac{∂^2 u}{∂ x_i ∂ x_j} + \sum_i b_i(x) \frac{∂ u}{∂ x_i} + c(x) u(x) = f(x)
  $$
  coefficient matrix $A(x) = (a_{ij}(x))_{m \times m}$

- Include
  * Elliptic Partial Differential Equation
    - Define  
      $A(x)$ is negative definite.

    - Include
      * Poisson's Equations
        - Define
          $$
          -\nabla^2 \phi = f
          $$
        * Laplace's Equations
          $$
          \nabla^2 \phi = 0
          $$

  * Hyperbolic Partial Differential Equation
    - Define  
      eigenvalue of $A(x)$ consists of a $0$ and other negative numbers

    - Include
      * Diffusion equation
        - Define
          $$
          \frac{∂u}{∂t} - a \nabla^2 u = f(x,t)
          $$

  * Parabolic Partial Differential Equation
    - Define
      eigenvalue of $A(x)$ consists of of a positive number and other negative numbers.

    - Include
      * Wave equation
        - Define
          $$
          \frac{∂^2 u}{∂t^2} - a \nabla^2 u = f(x,t)
          $$

### Semi-linear Partial Differential Equation

### Quasi-linear Partial Differential Equation

### Fully Nonlinear Partial Differential Equation