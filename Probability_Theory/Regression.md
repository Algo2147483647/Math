* Regression
  - Purpose  
    Input: $\{y_i, \boldsymbol x_i\}_{i=1}^n, \boldsymbol x_i \in \mathbb R^{\dim}$

    Regression problems aim to study the relationship between the independent variable $\boldsymbol x$ and the dependent variable $y$ by finding a function form $y = f(\boldsymbol x, \boldsymbol w)$ and minimizing the error under certain criteria.  

    $$y_i = f(\boldsymbol x_i, \boldsymbol w) + \epsilon_i$$

    |Symbol|Significance|
    |---|---|
    | $\boldsymbol x$ | independent variable|
    | $y$| dependent variable|
    | $\boldsymbol w$| unknown parameter|
    | $\epsilon$| error|
    |||

  - Include
    * Linear Regression
    * Regularization Regression
    * Gaussian Process Regression

  - Problem -- Solve the parameters $\boldsymbol w$
    - Algorithm
      * Least Square Method  
        $$\min_{\boldsymbol w} \quad \sum_{i=0}^n (f(\boldsymbol x_i, \boldsymbol w) - y_i)^2$$
