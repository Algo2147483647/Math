# $Fractal$
[TOC]
## Concept 

### Mandelbrot Set & Julia Set

- Define  
  $$
  Z_{n+1} = Z_n^2 + C
  $$
  
  $$
  \begin{align*}
    S_\text{Mandelbrot} &= \{ C \ |\ Z_{n+1} \text{ non-divergent }, Z_0 = 0 \}  \tag{Mandelbrot Set}\\
    S_\text{Julia, C} &= \{ Z_0 \ |\ Z_{n+1} \text{ non-divergent } \}  \tag{Julia Set}
  \end{align*}
  $$
  
  Mandelbrot set is the set of all complex numbers $C$ for which the Mandelbrot iteration remains bounded with $Z_0 = 0$. (non-divergent $\neq$ convergent, may jump back and forth at several different points)

  <img src="./assets/Mandel_zoom_00_mandelbrot_set.jpg" alt="img" style="zoom:10%;" />

  Julia set is the set of all complex numbers $Z_0$ for which the Mandelbrot iteration remains bounded with a given $C$.
  
  <img src="./assets/JSr07885.gif" alt="img" style="zoom: 40%;" />
  
- Property
  - $|Z_n|>2$ impossible to converge. Hence, Mandelbrot Set is in the circle with a radius of 2.

### Newton Fractal    

- Define  
  $$
  z_{n+1} = z_n - \frac{p(z_n)}{p'(z_n)}
  $$

  Newton fractal is a boundary set in the complex plane which is characterized by Newton's method applied to a fixed polynomial $p(z)$ or transcendental function. 
  
  <img src="./assets/Julia-set_N_z3-1.png" alt="img" style="zoom:12%;" />
