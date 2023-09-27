* Wavelet Transform
  - Define
    $$W(a, b) = \int_{-\infty}^{+\infty} f(t) \psi^* \left(\frac{t - b}{a}\right) \mathrm d t  \tag{Wavelet Transform}$$

    Wavelet Transform is a inner product of the original function $f(t)$ and the base function $\psi(\cdot)$ with scale parameter $a$ and translation parameter $b$ that controls the dilation and position of the wavelet function in time. $\cdot^*$ is the complex conjugate.

    The wavelet basis function $\psi(\cdot)$ should satisfy the following conditions,
    - Orthogonality, for $a\neq a' \text{ or } b\neq b'$,
      $$\left \langle \psi_{a,b}, \psi_{a',b'} \right \rangle = \int_{-\infty}^{+\infty} \psi_{a,b}(t) \psi_{a',b'}(t)\mathrm d t = 0$$  
    - Zero-mean
      $$\int_{-\infty}^{+\infty} \psi_{a,b}(t) \mathrm d t = 0$$   
    - Compact support, The wavelet basis functions $\psi_{a,b}(t)$ should have finite support. That is, they should be zero outside of a finite interval
      
    - Finite energy
      $$\|\psi_{a,b}\|^2 = \int_{-\infty}^{+\infty} |\psi_{a,b}(t)|^2 \mathrm d t < \infty$$  
    - Smoothness, The wavelet basis functions should be smooth and differentiable.

    $$\psi_{jk}(x) = 2^{\frac{j}{2}} \psi(2^j x - k)$$
    $$c_{jk} =  W_{\phi, f}(2^{-j}, k 2^{-j})$$

