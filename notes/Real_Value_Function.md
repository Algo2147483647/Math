* Real-Value Function & Complex-Value Function
  - Define
    $$f: \mathbb R \to \mathbb R  \tag{Real-Value Function}$$  
    $$f: \mathbb C \to \mathbb C  \tag{Complex-Value Function}$$  

  - Property
    * Function::Limit
      - Property
        - Uniqueness
        - Boundedness
        - 保号性
    * Derivative
    * Integral 
    * Kolmogorov-Arnold Representation Theorem  
      $$f(\boldsymbol x) = f(x_1, ..., x_n) = \sum_{q=0}^{2n} \Phi_q\left( \sum_{p=1}^n \phi_{q, p}(x_p) \right)$$
      Kolmogorov-Arnold representation theorem states that every multivariate continuous function can be represented as a superposition of the two-argument addition of continuous functions of one variable. 

  - Include
    * Analytic Function
      - Define  
        $$f(z) = \sum_{n=0}^\infty c_n (z - z_0)^n  \tag{Analytic Function}$$

        Analytic function $f$ is a complex function on an open set $D$ in the real line if for any $x_0 \in D$, it can be expanded into a power series. Where the coefficients $a_i \in \mathbb R$.

    * Holomorphic Function
      - Define  
        A holomorphic function is a complex-valued function on an open set $U$ if it is complex differentiable at every point of $U$.

      - Property
        - $$\frac{\partial f}{\partial \bar z} = 0$$
        * Cauchy-Riemann Equations
          - Describe  
            For a complex function $f(z) = u(x,y) + i v(x,y)$, where $u(x,y)$ and $v(x,y)$ are real and imaginary part respectively. 

            $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \tag{Cauchy-Riemann Equations}$$

    * Meromorphic Function
      - Define  
        A meromorphic function on an open subset $D$ of the complex plane is a function that is holomorphic on all of $D$ except for a set of isolated points, which are poles of the function.

      - Property 
        * Residue & Residue Theorem
          - Define
            $$\operatorname{Res}(f,a)  \tag{Residue}$$
            $$\oint_C f(z)\,\mathrm{d}z=2\pi i\sum_{k=1}^n \operatorname{Res}(f,a_k)  \tag{Residue Theorem}$$

              For an analytic function $f(z)$ on an open set $D$ and a simple closed curve $C$ that encircles counterclockwise all the isolated singularities $a_1,a_2,\ldots,a_n$ of $f(z)$, then the integral of $f(z)$ along $C$ can be expressed as the sum of the residues of $f(z)$ at these singularities.And $\operatorname{Res}(f,a_k)$ denotes the residue of $f(z)$ at the point $a_k$.

  - Example 
    * Polynomial Function 
    * Trigonometric Function & Hyperbolic Function

  - Problem
    * Differential Equation