* Moment
  - Define  
    K-order Moment & K-order Central Moment:
    $$\begin{align*}
      \mathbb E(X^k) &= \sum_i x_i^k \mathbb P_X(x_i)  \tag{Moment (Discrete)}  \\
        &= \int_{-\infty}^\infty x^k f_X(x) \mathrm d x  \tag{Moment (Continuous)}  \\
      \mathbb E((X-\mu_x)^k) &= \sum_i (x_i-\mu_x)^k \mathbb P_X(x_i)  \tag{Central Moment (Discrete)}  \\
        &= \int_{-\infty}^\infty (x-\mu_x)^k f_X(x) \mathrm d x  \tag{Central Moment (Continuous)}
    \end{align*}$$

    Symbol: $\mu_x = \mathbb E(X)$
      
  - Include
    * Expectation
      - Define
        $$\begin{align*}
          \mathbb E(X) = \mu_x &= \sum x_i \mathbb P_X(x_i)  \tag{Discrete}  \\
            &= \int_{-\infty}^\infty x f_X(x) \mathrm d x  \tag{Continuous}  \\
          \mathbb E(\boldsymbol X) &= \left(\begin{matrix} \bar X_i \\ \vdots \end{matrix}\right) 
        \end{align*}$$

      - Property
        $$\begin{align*}
          \mathbb E(Y) &= \int_{-\infty}^\infty g(x) f_X(x) \mathrm d x  \\
          Y &= g(X)  \tag{$g$ is a measurable function}
        \end{align*}$$

    * Variance & Standard Deviation
      - Define
        $$\begin{align*}
          Var(X) = \sigma_x^2 &= \mathbb E((X - \mu_x)^2)  \tag{Variance}\\
          \sigma_x &= \sqrt{\mathbb E((X - \mu_x)^2)}  \tag{Standard Deviation}
        \end{align*}$$

      - Property
        - $Var(X) = \mathbb E((X - \mu_x)^2) = \mathbb E(X^2) - \mathbb E(X)^2$
  
    * Skewness  
      $$\mathbb E\left(\frac{(X - \mu_x)^3}{\sigma_x^3}\right)  \tag{3-order Central Moment}$$ 
      
    * Kurtosis  
      $$\mathbb E\left(\frac{(X - \mu_x)^4}{\sigma_x^4}\right)  \tag{4-order Central Moment}$$  

    * Mixed Moment  
      - Define  
        $$\begin{align*}
          &\mathbb E(X^i Y^j) \tag{$ij$-order Joint Moment}  \\
          &\mathbb E((X-\bar X)^i (Y-\bar Y)^j) \tag{$ij$-order Joint Central Moment}
        \end{align*}$$

      - Include
        * Correlation & Covariance  
          - Define 
            $$\begin{align*}
              Corr(X,Y) &= \mathbb E(X Y)  &\tag{Correlation}  \\

              Cov(X,Y) 
              &= \mathbb E((X-\bar X) (Y-\bar Y))   \tag{Covariance}  \\
              &= \mathbb E(X Y) - \mathbb E(X) \mathbb E(Y)  \\
              &= Corr(X,Y) - \mathbb E(X) \mathbb E(Y)  \\

              R_{\boldsymbol X\boldsymbol X} &= \mathbb E(\boldsymbol X \boldsymbol X^T)  \\
              &= \left(\begin{matrix} E(X_i X_j) & ... \\ \vdots & \ddots \end{matrix}\right)  \tag{AutoCorrelation matrix}  \\


              \boldsymbol \Sigma_{\boldsymbol X\boldsymbol X} &= \mathbb E((\boldsymbol X - \bar{\boldsymbol X}) (X - \bar{\boldsymbol X})^T)  \tag{AutoCovariance matrix}\\
              &= \left(\begin{matrix} E((X_i - \bar X_i) (X_j - \bar X_j)) & ... \\ \vdots & \ddots \end{matrix}\right)  
            \end{align*}$$

          - Include
            * Correlation Coefficient
              - Define
                $$\begin{align*}
                  \rho 
                  &= \frac{Cov(X,Y)}{Cov(X,X) Cov(Y,Y)}  \\
                  &= \frac{\mathbb E(XY) - \mathbb E(X) \mathbb E(Y)}{\sqrt{\mathbb E(X^2) - \mathbb E(X)^2} \sqrt{\mathbb E(Y^2) - \mathbb E(Y)^2}}
                \end{align*}$$

              - Property
                - $\rho_{XY} \in [-1, 1]$, Correlations equal to $+1$ or $-1$ correspond to data points lying exactly on a line.
                - $\rho_{XY} = \rho_{YX}$
                - $\rho_{XY} = \rho_{(a + b X)\ (c + d Y)} \quad; b, d > 0$  
                  it is invariant under separate changes in location and scale in the two variables.

          - Property
            - $Cov(X,Y) = Cov(Y,X)$
            - $Cov(X,X) = Var(X,X)$
            - relation between AutoCorrelation & AutoCovariance matrix
              $$\boldsymbol \Sigma_{\boldsymbol X\boldsymbol X} = \boldsymbol R_{\boldsymbol X\boldsymbol X} - \bar{\boldsymbol X} \bar{\boldsymbol X}^T$$
            - Autocovariance matrix $\Sigma_{\boldsymbol X\boldsymbol X}$ is a positive semi-definite matrix.
            - $\boldsymbol Y = \boldsymbol A \boldsymbol X \Rightarrow \boldsymbol \Sigma_{\boldsymbol Y\boldsymbol Y} = \boldsymbol A \boldsymbol \Sigma_{\boldsymbol X\boldsymbol X} \boldsymbol A^T$

