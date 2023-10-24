# $Real\ Value\ Function$

[TOC]

## Define

$$
f: \mathbb R \to \mathbb R
$$

A complex function $f: \mathbb R \to \mathbb R$ is a [function](./Function.md) from real numbers to real numbers.

## Property

### Limitation

- Define

for a function $f: R \to R$ defined on some open interval that contains the number $a$, except possibly at $a$ itself. We say that the limit of $f(x)$ as $x$ approaches $a$ is equal to $L$: If and only if for any given positive number $\epsilon > 0$ there exists a number $\delta > 0$ such that whenever $0 < |x- a|< \delta$ (which means $x$ is within $\delta$ units of $a$ but not equal to a), it follows that $| f(a) - L|< \epsilon$.
$$
\lim\limits_{x\to a} f(x) = L
$$

- Property
  - Uniqueness
  - Boundedness
  - 保号性

### Derivative

- Define
  $$
  \begin{align*}
    \frac{df}{dx} &= \lim_{Δx \to 0}  \frac{ f(x + Δx) - f(x - Δx) }{ 2 Δx }  \tag{First derivative}\\
    \frac{d^n f}{dx^n} &= \lim_{Δx \to 0} \frac{ f^{(n - 1)}(x + Δx) - f^{(n - 1)}(x - Δx)} { 2 Δx }  \tag{$n$-order derivative}
  \end{align*}
  $$

Let $f: \mathbb{R} \to \mathbb{R}$ be a function. The derivative of $f$ at a point $x$ in its domain, if it exists, is given by the limit as mentioned above . If this limit exists, we say that $f$ is differentiable at $x$. The function $f'$ that assigns to each $x$ the value $f'(x)$ (where it exists) is called the derivative of $f$.

### Integral 

- Define

$$
\int f(x) \mathrm d x  = F(x)  + const. \tag{Integral}
$$
Integral $f: (f: \mathbb R \to \mathbb R) \to (f: \mathbb R \to \mathbb R)$ represents the anti-derivative of a function $f(x)$. The indefinite integral of a function $f$ is a family of functions $F$ such that for all $x$ in the domain of $f$, $F'(x) = f(x)$. Where $const.$ is an arbitrary constant, reflecting the fact that the process of differentiation loses constant information.

- Riemann Integra

$$
\int_a^b f(x) \mathrm d x = F(b) - F(a) \tag{Definite Integral}
$$

Definite Integral $f: (\mathbb R, \mathbb R, f: \mathbb R \to \mathbb R) \to \mathbb R$ of a function f(x) over an interval $[a, b]$ is the limit of a sum of rectangular areas as the width of the rectangles approaches zero. 

### Kolmogorov-Arnold Representation Theorem  

$$
f(\boldsymbol x) = f(x_1, ..., x_n) = \sum_{q=0}^{2n} \Phi_q\left( \sum_{p=1}^n \phi_{q, p}(x_p) \right)
$$
Kolmogorov-Arnold representation theorem states that every multivariate continuous function can be represented as a superposition of the two-argument addition of continuous functions of one variable. 


## Problem

* Differential Equation