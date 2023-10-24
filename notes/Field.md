# $Field$

[TOC]

## Define
Field is a [ring](./Ring.md) that satisfies the existence of multiplicative inverses for every nonzero element.

## Property

 ### Field extension

- Define

  A field extension is a pair of fields $E$ and $F$ such that the operations of $F$ are those of $E$ restricted to $F$. In other words, $F$ is a subset of $E$, and the addition and multiplication of elements of $F$ in $E$ coincide with their addition and multiplication in $F$. When $F$ is a subfield of $E$, we often say that $E$ is an extension of $F$ and write $E/F$.


## Example
### Real Field  

#### Define

$$
\mathbb R
$$

The set of real numbers, denoted $\mathbb{R}$, together with the operations of addition and multiplication, is called the field of real numbers if the following axioms are satisfied:

**Field Axioms**:
- (A1) $a + b = b + a$ for all $a, b \in \mathbb{R}$ (Commutativity of Addition).
- (A2) $a + (b + c) = (a + b) + c$ for all $a, b, c \in \mathbb{R}$ (Associativity of Addition).
- (A3) There exists an element $0 \in \mathbb{R}$ such that $a + 0 = a$ for all $a \in \mathbb{R}$ (Existence of Additive Identity).
- (A4) For every $a \in \mathbb{R}$, there exists an element $-a \in \mathbb{R}$ such that $a + (-a) = 0$ (Existence of Additive Inverse).
- (M1) $a \cdot b = b \cdot a$ for all $a, b \in \mathbb{R}$ (Commutativity of Multiplication).
- (M2) $a \cdot (b \cdot c) = (a \cdot b) \cdot c$ for all $a, b, c \in \mathbb{R}$ (Associativity of Multiplication).
- (M3) There exists an element $1 \in \mathbb{R}$, $1 \neq 0$, such that $a \cdot 1 = a$ for all $a \in \mathbb{R}$ (Existence of Multiplicative Identity).
- (M4) For every $a \in \mathbb{R}$ with $a \neq 0$, there exists an element $a^{-1} \in \mathbb{R}$ such that $a \cdot a^{-1} = 1$ (Existence of Multiplicative Inverse).
- (D) $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$ for all $a, b, c \in \mathbb{R}$ (Distributive Law).

**Order Axioms**:
- (O1) For every $a, b \in \mathbb{R}$, exactly one of the following holds: $a < b$, $a = b$, $a > b$.
- (O2) If $a < b$ and $b < c$, then $a < c$.
- (O3) If $a < b$ and $c > 0$, then $a \cdot c < b \cdot c$.
- (O4) If $a < b$ and $c < 0$, then $a \cdot c > b \cdot c$.
  

#### Property

### Complex Field 

#### Define

$$
\mathbb C
$$

The set of complex numbers, denoted $\mathbb{C}$, consists of all ordered pairs of real numbers $(a, b)$. Each such number is usually written as $a + bi$, where $a$ is called the real part, $b$ is called the imaginary part, and $i$ is the imaginary unit with the property that $i^2 = -1$.
$$
\mathbb C = \{a + b i \ |\ a, b \in \mathbb R ,i^2  = 1\}
$$
The operations of addition and multiplication are defined as:
- Addition: $(a + bi) + (c + di) = (a + c) + (b + d)i$.
- Multiplication: $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$.

The set $\mathbb{C}$ with these operations forms a field that satisfies all the field axioms (A1-A4, M1-M4, D). It also has the property that every non-constant polynomial equation with coefficients in $\mathbb{C}$ has a root in $\mathbb{C}$ (this is the statement of the Fundamental Theorem of Algebra).

#### Property
- module and argument
$$
\begin{align*}
r &= |z| = \sqrt{a^2 + b^2}  \tag{module}\\
\theta &= \arg(z) = \arctan(b/a)  \tag{argument}
\end{align*}
$$
$$
z = a + b i = r (\cos \theta + i \sin \theta) = r e^{i \theta}
$$

- Fundamental theorem of algebra

  Every non-constant single-variable polynomial with complex coefficients has at least one complex root.

- sub & div
$$
\begin{align*}
z_1 - z_2 &= (a - b i) + (c - d i) = (a - b) + (c - d) i  \tag{sub}\\
\frac{z_1}{z_2} &= \frac{a - b i}{c - d i} = \frac{a c + b d}{c^2 + d^2} + \frac{b c + a d}{c^2 + d^2} i  \tag{div}
\end{align*}
$$
- conjugate: 

$$
\bar z = a - b i  \tag{conjugate}
$$
- power: 

$$
z^p = r^p (\cos θ + i \sin θ)^p = r^p (\cos (p θ) + i \sin(p θ))  \tag{De Moiver's theorem}
$$
