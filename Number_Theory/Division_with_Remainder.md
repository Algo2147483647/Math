# $Division\ with\ Remainder\ \&\ Factor$

[TOC]

## Define    
For $a,b \in \mathbb Z, b \neq 0$, there are unique $q,r\in \mathbb Z, 0 ≤ r < b$ satisfy
$$
a = q \times b + r
$$

we called $q$ is Division, $r$ is Remainder.
$$
\begin{align*}
  a / b &= q  \tag{Division}\\
  a \% b &= r  \tag{Remainder}\\
  a &\equiv r \mod b
\end{align*}
$$

If $r = 0$, then we called the $q$ and $b$ is two Factors of $a$, and $b$ divides $a$, $b | a$. For any $a$, $1, a$ are always Factors of $a$.
$$
b | a \quad\Leftrightarrow\quad (\exists c \in \mathbb Z) a = b \times c
$$

## Concept

* Common Divisor & Common Multiple
* [Prime](./Prime.md)

## Property  

- /
  $$
  \begin{align*}
    (a + b) \% c &= (a \% c + b \% c) \% c  \\
    (a - b) \% c &= (a \% c - b \% c + c) \% c  \\
    (a · b) \% c &= ((a \% c) · (b \% c)) \% c  \\
    (a / b) \% c &= (a · b^{-1}) \% c = ((a \% c) · (b^{-1} \% c)) \% c  \tag{$b^{-1}$:$b$的逆元}
  \end{align*}
  $$

- Inverse element
  $(a · c) % b = 1$, 则$c$是$a$在$mod\ b$下的逆元$a^{-1}$

## Problem

* Linear Diophantine Equation
* Congruence Equation
  - Define  
    Solve the unknown $0 \le x < m, x \in \mathbb Z$ 
    $$
    f(x) \equiv b \mod m
    $$

  - Include
    * Linear Congruence Equation
      - Define  
        A type of Congruence Equation with $f(x) = a x$.
        $$
        a x \equiv b \mod m
        $$

      - Include
        * System of Linear Congruence Equations
          - Purpose
            $$
            \begin{align*}
              \left\{\begin{matrix} x \equiv a_1 \mod m_1 \\ \vdots \\ x \equiv a_n \mod m_n \end{matrix}\right.
            \end{align*}
            $$

            $$
            x = k \prod_{i=1}^n m_i + \sum_{i=1}^n a_i \left(\prod_{j=1, j≠i}^n m_j\right) \left(\prod_{j=1, j≠i}^n m_j\right)^{-1}
            $$

* Power Module
  - Purpose
    $$
    b = (a^k) \% m
    $$

  - Algorithm
    - 逐次平方法
      - 将 k 二进制展开
        $$k = \sum_{i=0}^r u_i·2^i$$

        - Note
          计算机里, k内存天然是二进制

      - 逐次平方制作模$m$的$a$幂次表, $i\in[0,r]$
        $$
        \begin{align*}
          a^{2^0} &= a = A_0 \% m  \\
          a^{2^i} &= (a^{2^{i-1}})^2 = A^{2(i-1)} = A_i % m
        \end{align*}
        $$

      - 乘积
        $$
        \prod_{i=0}^r A_i^{u_i} \% m
        $$
      
      - proof
        $$
        a^k = a^{\sum\limits_{i=0}^r u_i·2^i}
        $$
