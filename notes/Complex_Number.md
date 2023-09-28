* Complex Field
  - Define
    $$\mathbb C = \{a + b i \ |\ a, b \in \mathbb R ,i^2  = 1\}\tag{complex field}$$  

    Complex numbers are defined as a linear polynomial in $i$ with two real coefficients $a, b \in \mathbb R$.
    $$\begin{align*}
    z_1 + z_2 &= (a + b i) + (c + d i) = (a + b) + (c + d) i  \tag{addition}\\
    z_1 \cdot z_2 &= (a - b i) \cdot (c - d i) = (a c - b d) + (a d + b c) i  \tag{multiply}
    \end{align*}$$

  - Property
    - module and argument
      $$\begin{align*}
        r &= |z| = \sqrt{a^2 + b^2}  \tag{module}\\
        \theta &= \arg(z) = \arctan(b/a)  \tag{argument}
      \end{align*}$$
      $$z = a + b i = r (\cos \theta + i \sin \theta) = r e^{i \theta}$$

    - operation
      $$\begin{align*}
      z_1 - z_2 &= (a - b i) + (c - d i) = (a - b) + (c - d) i  \tag{sub}\\
      \frac{z_1}{z_2} &= \frac{a - b i}{c - d i} = \frac{a c + b d}{c^2 + d^2} + \frac{b c + a d}{c^2 + d^2} i  \tag{div}
      \end{align*}$$
      conjugate: 
      $$\bar z = a - b i  \tag{conjugate}$$
      power: 
      $$z^p = r^p (\cos θ + i \sin θ)^p = r^p (\cos (p θ) + i \sin(p θ))  \tag{De Moiver's theorem}$$
        