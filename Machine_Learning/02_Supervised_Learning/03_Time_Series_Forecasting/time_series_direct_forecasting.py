import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def create_direct_data(data, window_size=5, target_size=3):
    i = 1
    while i < window_size:
        data["co2_{}".format(i)] = data["co2"].shift(-i)
        i += 1
    i = 0
    while i < target_size:
        data["target_{}".format(i)] = data["co2"].shift(-window_size-i)
        i += 1
    data = data.dropna(axis=0)
    return data

data = pd.read_csv("./co2.csv")
data["time"] = pd.to_datetime(data["time"], yearfirst=True)
data["co2"] = data["co2"].interpolate()

window_size = 5
target_size = 3
data = create_direct_data(data, window_size, target_size)
targets = ["target_{}".format(i) for i in range(target_size)]
x = data.drop(["time"]+targets, axis=1)
y = data[targets]
# print(data.drop("time", axis=1).corr())

train_size = 0.8
num_sample = len(x)

x_train = x[:int(num_sample * train_size)]
y_train = y[:int(num_sample * train_size)]
x_test = x[int(num_sample * train_size):]
y_test = y[int(num_sample * train_size):]

regs = [LinearRegression() for _ in range(target_size)]
i = 0
for i, reg in enumerate(regs):
    reg.fit(x_train, y_train["target_{}".format(i)])

r2 = []
mae = []
mse = []

for i, reg in enumerate(regs):
    y_predict = reg.predict(x_test)
    r2.append(r2_score(y_test["target_{}".format(i)], y_predict))
    mae.append(mean_absolute_error(y_test["target_{}".format(i)], y_predict))
    mse.append(mean_squared_error(y_test["target_{}".format(i)], y_predict))

print("R2 score: {}".format(r2))
print("MAE: {}".format(mae))
print("MSE: {}".format(mse))


