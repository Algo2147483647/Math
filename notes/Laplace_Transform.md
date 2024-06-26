# $Laplace\ Transform$

[TOC]

## Define

Laplace Transform $f: (f: \mathbb C \to \mathbb C) \times \mathbb C \to \mathbb C$
$$
\mathcal L_{f(t)}(s) = \int_0^{\infty} f(t) e^{-st} \mathrm d t
$$

$$
\mathcal L^{-1}_{F(s)}(t) = \frac{1}{2 \pi \mathrm i} \int_{\real(s) - \mathrm i \infty}^{\real(s) + \mathrm i \infty} F(s) e^{st} \mathrm d s  \tag{inverse Laplace transform}
$$

A type of [function](./Function.md)

## Include

### Fourier Transform

- Define  
  Fourier Transform is a function $f: (f:\mathbb R \to \mathbb R) \times \mathbb R \to \mathbb R$. Fourier Transform represents the original function $f(x)$ by a set of basis composed of trigonometric functions $e^{-\mathrm i 2 \pi x f}$ through calculate the inner product between them.
  $$
  \begin{align*}
  \mathcal F(f(t)) &= F(\omega) = \int_{-\infty}^{\infty} f(x) e^{-\mathrm i \omega x} \mathrm d x  \tag{Fourier transform}\\
  \mathcal F^{-1}(F(\omega)) &= f(x) = \int_{-\infty}^{\infty} F(\omega) e^{\mathrm i \omega x} \mathrm d f \tag{inverse Fourier transform}
  \end{align*}
  $$

### Wavelet Transform

- Define
  $$
  W(a, b) = \int_{-\infty}^{+\infty} f(t) \psi^* \left(\frac{t - b}{a}\right) \mathrm d t  \tag{Wavelet Transform}
  $$

  Wavelet Transform is a inner product of the original function $f(t)$ and the base function $\psi(\cdot)$ with scale parameter $a$ and translation parameter $b$ that controls the dilation and position of the wavelet function in time. $\cdot^*$ is the complex conjugate.

  The wavelet basis function $\psi(\cdot)$ should satisfy the following conditions,
  - Orthogonality, for $a\neq a' \text{ or } b\neq b'$,
    $$
    \left \langle \psi_{a,b}, \psi_{a',b'} \right \rangle = \int_{-\infty}^{+\infty} \psi_{a,b}(t) \psi_{a',b'}(t)\mathrm d t = 0
    $$
  - Zero-mean
    $$
    \int_{-\infty}^{+\infty} \psi_{a,b}(t) \mathrm d t = 0
    $$
  - Compact support, The wavelet basis functions $\psi_{a,b}(t)$ should have finite support. That is, they should be zero outside of a finite interval
    
  - Finite energy
    $$
    \|\psi_{a,b}\|^2 = \int_{-\infty}^{+\infty} |\psi_{a,b}(t)|^2 \mathrm d t < \infty
    $$
  - Smoothness, The wavelet basis functions should be smooth and differentiable.

  $$
  \psi_{jk}(x) = 2^{\frac{j}{2}} \psi(2^j x - k)
  $$
  $$
  c_{jk} =  W_{\phi, f}(2^{-j}, k 2^{-j})
  $$

### Z-Transform

- Define

  Z-transform $f: (f: \mathbb Z \to \mathbb C) \times \mathbb C \to \mathbb C$ converts a sequence of real or complex numbers, into a complex valued frequency-domain (the z-domain or z-plane) representation.
  $$
  X(z) = \mathcal Z(x[n]) = \sum_{n=-\infty}^{\infty} x[n]z^{-n}
  $$
  

