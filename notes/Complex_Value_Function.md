# $Complex\ Value\ Function$

[TOC]

## Define

$$
f: \mathbb C \to \mathbb C
$$

A complex function $f: \mathbb C \to \mathbb C$ is a [function](./Function.md) from [complex numbers](./Complex_Field.md) to complex numbers.

## Property

- Differentiability: Holomorphic functions (or analytic functions) are differentiable everywhere within their domain of definition. For complex functions, holomorphism and analyticity are equivalent. 

  Let $U$ be an open set in the complex plane $\mathbb C$ and let $f : U \to \mathbb C$ be a function. The function ,is said to be analytic (or holomorphic) on $U$ if for every $z_0 \in U$, there exists an open disk $D$ centered at $z_0$ such that $f$ is differentiable at every point in $D$.

### Residue & Residue Theorem
$$
\operatorname{Res}(f,a)  \tag{Residue}
$$
$$
\oint_C f(z)\,\mathrm{d}z=2\pi i\sum_{k=1}^n \operatorname{Res}(f,a_k)  \tag{Residue Theorem}
$$

For an analytic function $f(z)$ on an open set $D$ and a simple closed curve $C$ that encircles counterclockwise all the isolated singularities $a_1,a_2,\ldots,a_n$ of $f(z)$, then the integral of $f(z)$ along $C$ can be expressed as the sum of the residues of $f(z)$ at these singularities. And $\operatorname{Res}(f,a_k)$ denotes the residue of $f(z)$ at the point $a_k$.

## Include

### Analytic Function

- Define  
  $$
  f(z) = \sum_{n=0}^\infty c_n (z - z_0)^n  \tag{Analytic Function}
  $$
  
  Analytic function $f$ is a complex function on an open set $D$ in the real line if for any $x_0 \in D$, it can be expanded into a power series. Where the coefficients $a_i \in \mathbb R$.

### Holomorphic Function

- Define  
  A holomorphic function is a complex-valued function on an open set $U$ if it is complex differentiable at every point of $U$.

- Property
  
  - Holomorphic functions are differentiable everywhere within their domain of definition.
  
  - $$
    \frac{\partial f}{\partial \bar z} = 0
    $$
  
  * Cauchy-Riemann Equations
    
    For a complex function $f(z) = u(x,y) + i v(x,y)$ to be differentiable (and hence analytic) at a point, where $u(x,y)$ and $v(x,y)$ are real and imaginary part respectively, the partial derivatives of $u, v$ must satisfy the Cauchy-Riemann equations at that point:
    $$
    \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}  \\ \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \tag{Cauchy-Riemann Equations}
    $$

### Meromorphic Function

- Define  
  A meromorphic function on an open subset $D$ of the complex plane is a function that is holomorphic on all of $D$ except for a set of isolated points, which are poles of the function.




