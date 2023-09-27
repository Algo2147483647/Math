* Stochastic Process  
  - Define  
    A Stochastic Process $X(t, \omega), \omega \in \Omega, t \in T$ is defined as a collection of random variables defined on a Probability Space $(Ω, \mathcal F, P)$, and these random variables indexed by set $T$.

    - Note
      - When the time $t$ is fixed, the random process degenerates into a random variable.
      - When the random sample $ζ$ is determined, the random process degenerates into a continuous time function

  - Property
    * Correlation Function & Covariance Function
      - Define  
        $$
        \begin{align*} 
          Corr(X(t_1), Y(t_2)) 
          &= \mathbb E(X(t_1) Y(t_2))  \tag{Correlation function}\\

          Corr(X(t_1), X(t_2)) 
          &= \mathbb E(X(t_1) X(t_2))  \tag{AutoCorrelation function}\\

          Cov(X(t_1), Y(t_2)) 
          &= \mathbb E((X(t_1) - \mu_X(t_1)) (Y(t_2) - \mu_Y(t_2)))  \tag{Covariance function}\\
          &= \mathbb E(X(t_1) X(t_2)) - \mu_X(t_1) \mu_Y(t_2)  \\
          &= Corr(X(t_1), Y(t_2)) - \mu_X(t_1) \mu_Y(t_2)  \\

          Cov(X(t_1), X(t_2)) 
          &= \mathbb E((X(t_1) - \mu(t_1)) (X(t_2) - \mu(t_2)))  \tag{AutoCovariance function}\\
          &= \mathbb E(X(t_1) X(t_2)) - \mu(t_1) \mu(t_2)  \\
          &= Corr(X(t_1), X(t_2)) - \mu(t_1) \mu(t_2) 
        \end{align*} 
        $$

      - Property  
        - $X, Y \ \text{Uncorrelated} \Leftrightarrow Cov(X(t_1), Y(t_2)) = 0, \quad \forall t_1, t_2$

        - $X, Y \ \text{Orthogonality} \Leftrightarrow Corr(X(t_1), Y(t_2)) = 0, \quad \forall t_1, t_2$

    - Independence

  - Include
    * Stationary Process & Weakly Stationary Process
      - Define  

        $$\mathbb P (x(t_1), ... , x(t_n)) = \mathbb P (x(t_1+\tau), ..., x(t_n+\tau)) \quad ;\forall \tau, t_1, ..., t_n \in \mathbb R, n \in \mathbb N  \tag{Stationary}$$
        Stationary process is a stochastic process in which the joint distribution of any set of time-indexed random variables is invariant to shifts in time (the statistical properties of the process are constant over time).

        $$R_{XX}(t_1 - t_2 ,0) = R_{XX}(t_1, t_2) \quad; \forall t_1, t_2 \in \mathbb R  \tag{Weakly Stationary}$$ 
        Weakly stationary process is a stochastic process in which the mean, variance and autocovariance (or autocorrelation) of the process are constant over time, but the joint distribution of the variables may depend on the time index.

  
      - Property
        - Power Spectral Density  
          Power Spectral Density is the Fourier transform of autocorrelation function of Weak-sense stationary process.  
          Power Spectral Density consists of real numbers greater than 0.

      - Problem: Test the Stationary
        * Unit Root Test 

    * Markov Process
    * Gaussian Process
    * Autoregressive Process
      - Define  
        $$X_t = \epsilon_t + \alpha_0 + \sum\limits_{i=1}^p \alpha_i X_{t-i}  \tag{Autoregressive}$$  

        Autoregressive Process is a discrete-time stochastic process in which the current value of a time series variable depends linearly on its past values. Where $p$ is the order of autoregressive process, which means the length of the associated historical value.

    * Martingale 
      - Define  
        Martingale is a discrete-time stochastic process that satisfies for any time $n$,
        $$\mathbb E(|X_n|) < \infty$$
        $$\mathbb E(X_{n+1} \ |\ X_1, ..., X_n) = X_n$$

        The second condition means that the conditional expected value of the next observation, given all the past observations, is equal to the most recent observation.

  - Example
    - Simple process
      $$X(t, ζ) = X(ζ) f(t)$$

    - Random Sine Wave
      $$X(t, ζ) = A(ζ) \sin(\omega_0 t + \Theta(ζ))$$

    * Stochastic Point Process

