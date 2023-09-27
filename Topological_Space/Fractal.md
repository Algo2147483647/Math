* Fractal
  - Concept 
    * Mandelbrot Set & Julia Set
      - Define  
        $$Z_{n+1} = Z_n^2 + C$$
        
        $$\begin{align*}
          S_\text{Mandelbrot} &= \{ C \ |\ Z_{n+1} \text{ non-divergent }, Z_0 = 0 \}  \tag{Mandelbrot Set}\\
          S_\text{Julia, C} &= \{ Z_0 \ |\ Z_{n+1} \text{ non-divergent } \}  \tag{Julia Set}
        \end{align*}$$  
        
        Mandelbrot set is the set of all complex numbers $C$ for which the Mandelbrot iteration remains bounded with $Z_0 = 0$. (non-divergent $\neq$ convergent, may jump back and forth at several different points)

        Julia set is the set of all complex numbers $Z_0$ for which the Mandelbrot iteration remains bounded with a given $C$.

      - Property
        - $|Z_n|>2$ impossible to converge. Hence, Mandelbrot Set is in the circle with a radius of 2.

    * Newton Fractal   
