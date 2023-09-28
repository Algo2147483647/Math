* Trigonometric Function & Hyperbolic Function
  - Define  
    Trigonometric functions $f: \mathbb R \to \mathbb R$ are a set of mathematical functions that relate angles $\theta$ to the ratios of the sides (opposite $a$, adjacent $b$, hypotenuse $c$) of a right-angled triangle. Where hypotenuse is the length of the side opposite the right angle, opposite represents the side opposite the given angle $\theta$, adjacent represents the side between the angle $\theta$ and the right angle.

    $$\begin{align*}
      \sin(\theta) &= \frac{a}{c}  \quad\in (-1, 1)\tag{sine}\\
      \cos(\theta) &= \frac{b}{c}  \quad\in (-1, 1)\tag{cosine}\\
      \tan(\theta) &= \frac{a}{b}  \quad\in (-\infty, +\infty)\tag{tangent}
    \end{align*}$$

    Hyperbolic Functions $f: \mathbb R \to \mathbb R$ are defined by hyperbola $x^2 - y^2 = 1$, where the angles $\theta$ refer to twice the included angle of the ray from zero point to the point in hyperbola and positive half of x-axis, $\sinh(\theta)$ is the coordinate value $x$ of the point, and $\cosh(\theta)$ is the coordinate value $y$ of the point.

    For the complex field $x \in \mathbb C$,
    $$\begin{align*}
      \sin(x)  &= \frac{e^{ix} - e^{-ix}}{2i}  \tag{sine}\\
      \cos(x)  &= \frac{e^{ix} + e^{-ix}}{2}  \tag{cosine}\\
      \tan(x)  &= \frac{e^{ix} - e^{-ix}}{ie^{ix} + ie^{-ix}}  \tag{tangent}\\
      \sinh(x) &= \frac{e^{x} - e^{-x}}{2}  \tag{hyperbolic sine}\\
      \cosh(x) &= \frac{e^{x} + e^{-x}}{2}  \tag{hyperbolic cosine}\\
      \sinh(x) &= \frac{e^{-x} - e^{x}}{e^{x} + e^{-x}}  \tag{hyperbolic tangent}\\
    \end{align*}$$

  - Property
    - Thigonometric functions are periodic functions. The period of $\sin(\cdot), \cos(\cdot)$ is $2 k \pi$, period of $\tan(\cdot)$ is $k \pi$, $k \in \mathbb Z$,
      $$\begin{align*}
        \sin(\theta + 2 k \pi) &= \sin(\theta)  \\
        \cos(\theta + 2 k \pi) &= \cos(\theta)  \\
        \tan(\theta + k \pi) &= \tan(\theta)  \\
      \end{align*}$$
      
    - 1
      $$\begin{align*}
        \sin(a \pm b) &= \sin(a) \cos(b) \pm \cos(a) \sin(b)  \\
        \cos(a \pm b) &= \cos(a) \cos(b) \mp \sin(a) \sin(b)  \\
        \tan(a \pm b) &= \frac{\tan(a) \pm  \tan(b)}{1 \mp \tan(a) \tan(b)}
      \end{align*}$$
      
    - The relationship between the addition and multiplication of two thigonometric functions,
      $$\begin{align*}
        \sin(a)\cos(b) &= \frac{\sin(a + b) + \sin(a - b)}{2}  \\
        \sin(a)\sin(b) &= \frac{\cos(a + b) - \cos(a - b)}{2}  \\
        \cos(a)\cos(b) &= \frac{\cos(a + b) + \cos(a - b)}{2}  \\
      \end{align*}$$

    - 1
      $$a \sin(\theta) + b \cos(\theta) = \sqrt{a^2 + b^2} \sin \left(\theta + \arctan\left(\frac{b}{a}\right) \right)$$
