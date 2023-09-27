* Regularization Regression
  - Define
    $$\min_{f}\quad \sum_{i=1}^n \text{Loss}(f(\boldsymbol x_i), y_i) + \alpha R(f)$$ 

    Regularization Regression add a regularization term $R(f)$ to a loss function $\text{Loss}(\cdot)$, where $R(f)$ is typically chosen to impose a penalty on the complexity of $f$.

  - Include
    * L0 Regularization Regression, Sparse Regression
      - Define
        $$\min_{\boldsymbol \omega}\quad \sum_{i=1}^n \text{Loss}(f(\boldsymbol x_i), y_i) + \alpha \|\boldsymbol \omega\|_0$$ 

      - Algorithm
        * Orthogonal Matching Pursuit 

    * L1 Regularization Regression
      - Define
        $$\min_{\boldsymbol \omega}\quad \sum_{i=1}^n \text{Loss}(f(\boldsymbol x_i), y_i) + \alpha \|\boldsymbol \omega\|_1$$ 

    * L2 Regularization Regression, Ridge Regression
      - Define
        $$\min_{\boldsymbol \omega}\quad \sum_{i=1}^n \text{Loss}(f(\boldsymbol x_i), y_i) + \alpha \|\boldsymbol \omega\|_2^2$$ 

    * ElasticNet Regression
      - Define
        $$\min_{\boldsymbol \omega}\quad \sum_{i=1}^n \text{Loss}(f(\boldsymbol x_i), y_i) + \alpha \|\boldsymbol \omega\|_1 + \frac{\alpha (1 - \rho)}{2} \|\boldsymbol \omega\|_2^2$$ 
        