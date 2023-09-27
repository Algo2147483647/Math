* Adaptive Moment Estimation
  - Process
    $$\begin{align*}
      \theta_{t+1} &= \theta_{t} - \frac{\eta}{\sqrt{\hat v_t} + \epsilon} \hat m_t  \tag{update}\\
      m_t & = \beta_1 m_{t-1} + (1 - \beta_1) \nabla \hat L(\theta_t)  \tag{first-order moment estimation}\\
      v_t & = \beta_2 v_{t-1} + (1 - \beta_2) \left(\nabla \hat L(\theta_t) \right)^2  \tag{second-order moment estimation}\\
      \hat m_t &= \frac{m_t}{1 - \beta_1^t}  \tag{deviation correction}\\
      \hat v_t &= \frac{v_t}{1 - \beta_2^t}
    \end{align*}$$  

    Where, $m_t$ is the first-order moment estimation of gradient, $v_t$ is the second-order moment estimation of gradient, $\hat m_t, \hat v_t$ are deviation correction estimate of $m_t, v_t$.