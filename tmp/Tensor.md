# $Tensor$

[TOC]

## Define

A $(k,l)$-type tensor $T$ on an $n$-dimensional vector space is a multilinear map,
$$
T:V^*  \times \cdots \times V^* \times V \times \cdots \times V \to \mathbb R
$$

### **克里斯托弗符号**

有了克氏符的存在，我们就可以比较流形上不同位置的张量，而不是孤立地看待他们，因此克氏符也叫作**联络系数**。
$$
\var A^i = -\Gamma^i_{kl} A^k \mathrm{d} x^l
$$
Property
$$
\Gamma^k_{ij} = \frac{1}{2} g^{kl} \left( \frac{\partial g_{il}}{\partial x^j} + \frac{\partial g_{jl}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^l} \right)
$$
测地线方程
$$
\frac{d^2 x^k}{d\tau^2} + \Gamma^k_{ij} \frac{dx^i}{d\tau} \frac{dx^j}{d\tau} = 0
$$

