import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3]])
y = np.array([1.0, 2.0, 2.0])
reg = LinearRegression().fit(x, y)
print("coef:", np.round(reg.coef_, 4), "intercept:", np.round(reg.intercept_, 4))
print("sum residuals:", np.round(np.sum(y - reg.predict(x)), 6))
