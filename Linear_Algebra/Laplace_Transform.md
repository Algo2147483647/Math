* Laplace Transform
  - Define
    $$\mathcal L_{f(t)}(s) = \int_0^{\infty} f(t) e^{-st} \mathrm d t$$

    $$\mathcal L^{-1}_{F(s)}(t) = \frac{1}{2 \pi \mathrm i} \int_{\real(s) - \mathrm i \infty}^{\real(s) + \mathrm i \infty} F(s) e^{st} \mathrm d s  \tag{inverse Laplace transform}$$

  - Include
    * Fourier Transform
      - Define  
        Fourier Transform is a function $f: ((f:\mathbb R \to \mathbb R) \times \mathbb R) \to \mathbb R$. Fourier Transform represents the original function $f(x)$ by a set of basis composed of trigonometric functions $e^{-\mathrm i 2 \pi x f}$ through calculate the inner product between them.

        $$F(f) = \int_{-\infty}^{\infty} f(x) e^{-\mathrm i 2 \pi x f} \mathrm d x$$
        $$f(x) = \int_{-\infty}^{\infty} F(f) e^{\mathrm i 2 \pi x f} \mathrm d f \tag{inverse Fourier transform}$$