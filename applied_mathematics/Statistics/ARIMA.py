import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class ARIMA:
    def __init__(self, order):
        self.p, self.d, self.q = order
        self.coefficients = {}

    def difference(self, series):
        """
        Apply d-th order differencing to the series
        """
        diff_series = series
        for i in range(self.d):
            diff_series = diff_series[1:] - diff_series[:-1]
        return diff_series

    def fit(self, series):
        """
        Fit the ARIMA model to the series
        """
        # Differencing
        diff_series = self.difference(series)
        
        # Create lagged matrix for AR(p)
        X = np.array([diff_series[i:-(self.p-i)] for i in range(self.p)]).T
        y = diff_series[self.p:]
        
        # Initial parameters
        initial_params = np.array([0] * (self.p + self.q))
        
        # Objective function to minimize (Least squares)
        def objective(params):
            ar_params = params[:self.p]
            ma_params = params[self.p:]
            
            # Calculate residuals
            residuals = y - X @ ar_params
            for i in range(self.q):
                residuals[i+1:] -= ma_params[i] * residuals[:-i-1]
                
            # Return sum of square of residuals
            return np.sum(residuals ** 2)

        # Minimize the objective function
        result = minimize(objective, initial_params, method='L-BFGS-B')
        
        self.coefficients['ar'] = result.x[:self.p]
        self.coefficients['ma'] = result.x[self.p:]

        return result.success

    def predict(self, series, steps):
        """
        Predict the next 'steps' steps of the series
        """
        # Differencing
        diff_series = self.difference(series)
        
        # Prepare the last known values for prediction
        last_known_values = list(diff_series[-self.p:])
        predictions = []
        
        # Predict future values
        for _ in range(steps):
            ar_term = np.dot(self.coefficients['ar'], last_known_values[-self.p:])
            ma_term = np.dot(self.coefficients['ma'], predictions[-self.q:]) if self.q > 0 else 0
            prediction = ar_term + ma_term
            predictions.append(prediction)
            last_known_values.append(prediction)
        
        # Reverse differencing
        for i in range(self.d):
            predictions = np.cumsum([series[-(i+1)], *predictions])[1:]
        
        return predictions
    
    def continuous_predict(self, series, new_data_points):
        """
        Continuously predict the next point given a series and new real data points.
        """
        predictions = []
        current_series = series.copy()
        
        for new_point in new_data_points:
            # Differencing
            diff_series = self.difference(current_series)
            
            # Prepare the last known values for prediction
            last_known_values = list(diff_series[-self.p:])
            last_known_values.extend(predictions[-self.q:])
            
            # Predict the next value
            ar_term = np.dot(self.coefficients['ar'], last_known_values[-self.p:])
            ma_term = 0
            if self.q > 0 and len(predictions) >= self.q:
                ma_term = np.dot(self.coefficients['ma'], predictions[-self.q:])
            
            prediction = ar_term + ma_term
            predictions.append(prediction)
            
            # Update the series with the new actual point
            current_series = np.append(current_series, new_point)
        
        # Reverse differencing
        final_predictions = []
        for pred in predictions:
            current_series = np.append(current_series, current_series[-1] + pred)
            final_predictions.append(current_series[-1])
        
        return final_predictions

# Let's test the ARIMA implementation with a made-up dataset
# Here we use a simple time series with a known pattern for demonstration purposes

# Generate a synthetic time series data
np.random.seed(42)
n = 100
p = 0.5
series = np.random.normal(size=n)
for i in range(2, n):
    series[i] += p * series[i - 1]

# Define and fit the ARIMA model
# For simplicity, we use order (1,0,0), which is equivalent to an AR(1) model
arima_order = (1, 0, 0)
arima_model = ARIMA(order=arima_order)
fit_success = arima_model.fit(series)

# Forecast the next 10 points
forecast_steps = 10
predictions = arima_model.predict(series, steps=forecast_steps)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(series, label='Original Series')
plt.plot(np.arange(n, n + forecast_steps), predictions, label='Predictions', color='red')
plt.legend()
plt.show()

np.random.seed(42)
n = 100  # 数据点数量
p = 0.5  # AR部分的系数
actual_series = np.random.normal(size=n)
for i in range(2, n):
    actual_series[i] += p * actual_series[i - 1]

# 将时间序列分为训练集和新的真实数据点
# 假设我们只有前80个点是已知的，剩下的20个点是我们将逐个接收的新真实数据点
known_series = actual_series[:80]
new_real_data_points = actual_series[80:]

# 定义ARIMA模型并拟合已知的时间序列
arima_order = (1, 0, 0)  # 为简单起见，这里使用AR(1)模型
arima_model = ARIMA(order=arima_order)
fit_success = arima_model.fit(known_series)

# 使用continuous_predict方法进行连续预测
# 这里每次只预测下一个点，然后添加新的真实数据点
predictions = arima_model.continuous_predict(known_series, new_real_data_points)

# 绘制结果
plt.figure(figsize=(12, 6))
plt.plot(actual_series, label='Actual Series')
plt.plot(range(80, 100), predictions, label='Continuous Predictions', marker='o')
plt.legend()
plt.title('ARIMA Continuous Prediction Test')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

# 输出拟合成功与否的状态和模型系数
print(f"Model fit was successful: {fit_success}")
print(f"Model coefficients: {arima_model.coefficients}")