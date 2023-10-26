# $Prime$

[TOC]

## Define  

$$
\nexists a \in (\mathbb N - \{1, p\}), \text{ let } a | p  \tag{Prime}
$$
Prime is a number $p$ that can only be divided by $1$ and itself.

## Property

### Fundamental Theorem of Arithmetic
Any integer $n$ greater than $1$ can be uniquely expressed in the form of prime $p_i$ product.   
$$
n = \prod_i p_i^{\alpha_i} \quad n \in \mathbb Z, n > 1
$$

### Fermat's Little Theorem

$$
a^{p-1} \equiv 1 \mod p
$$
Where $p$ is a prime and $a$ is an any integer that is not a multiple of $p$.

- Property
  $$
  \frac{a}{b} \mod p \equiv a \times b^{p-2} \mod p
  $$

  - Proof

      $$
      \frac{a}{b} \mod p = a \times b^{-1} \mod p  \\
      b^{p-1} \equiv 1 \mod p \\
      b \times b^{p-1} \equiv 1 \mod p  \\
      \Rightarrow \quad b^{-1} \equiv b^{p-2}  \mod p \\
      \Rightarrow \quad \frac{a}{b} \mod p \equiv a \times b^{p-2} \mod p
      $$

  

### *Q: Resolving prime factor*  

- Pollard Rho algorithm

### *Q: Filter Prime Number from a range of numbers?*

* Euler's Sieve
  - Purpose
    For a numbers range from $2$ to $n$, we aim to sift out all primes from them, through let each composite number be screened by its minimum prime factor.

  - Process
    First, We traverse the numbers $x$ range from $2$ to $n$, we join $x$ into prime set $S_p$ if $x$ is not marked as non-prime.

    Meanwhile, we traversing the current prime table $p \in S_p$, and mark $p x$ as non-prime. When $p | x$, we should stop traversing the prime table, because that the primes $p' \in S_p$ large than $p$ are no longer the minimum prime factor of $p' x$ ($p' x = p' p r$).

    ```py
    
    def EulerSieve(n):
      primes = []
      is_p = ones(n + 1)
    
      for i in range(2, n + 1):
          if (is_p[i]):
              primes.append(i)
    
          for p in primes:
              if (p * i > n):
                  break
    
              is_p[p * i] = 0
    
              if (i % p == 0):
                  break
      return primes
    ```

## Include

### Mersenne Prime

- Define 
  $$
  M_n = 2^n - 1  \tag{Mersenne number}
  $$
  Mersenne Prime is a prime number that is one less than a power of two.

- Property
  - example of mersenne primes
    |n|value|
    |:---:|---:|
    |2|3|
    |3|7|
    |5|31|
    |7|127|
    |13|8191| 
    |17|131071| 
    |19|524287| 
    |31|2147483647| 
    |61|2305843009213693951| 
    |89|618970019642690137449562111| 
    |107|162259276829213363391578010288127| 
    |127|170141183460469231731687303715884105727| 
    ||| 