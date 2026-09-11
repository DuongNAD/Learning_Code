import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def create_recursive_data(data, window_size=5):
    i = 1
    while i < window_size:
        data["co2_{}".format(i)] = data["co2"].shift(-i)
        i += 1
    data["target"] = data["co2"].shift(-window_size)
    data = data.dropna(axis=0)
    return data

data = pd.read_csv("./co2.csv")
data["time"] = pd.to_datetime(data["time"], yearfirst=True)
data["co2"] = data["co2"].interpolate()

# fig, ax = plt.subplots()
# ax.plot(data["time"], data["co2"])
# ax.set_xlabel("Time")
# ax.set_ylabel("CO2")
# plt.show()

window_size = 5
data = create_recursive_data(data, window_size)
x = data.drop(["target", "time"], axis=1)
y = data["target"]
# print(data.drop("time", axis=1).corr())

train_size = 0.8
num_sample = len(x)

x_train = x[:int(num_sample * train_size)]
y_train = y[:int(num_sample * train_size)]
x_test = x[int(num_sample * train_size):]
y_test = y[int(num_sample * train_size):]

model = RandomForestRegressor(random_state=1009)
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print("MAE: {}".format(mean_absolute_error(y_test, y_predict)))
print("MSE: {}".format(mean_squared_error(y_test, y_predict)))
print("R2: {}".format(r2_score(y_test, y_predict)))

fig, ax = plt.subplots()
ax.plot(data["time"][:int(num_sample * train_size)], y_train, label="train")
ax.plot(data["time"][int(num_sample * train_size):], y_test, label="test")
ax.plot(data["time"][int(num_sample * train_size):], y_predict, label="prediction")
ax.set_xlabel("Time")
ax.set_ylabel("CO2")
ax.legend()
ax.grid()
plt.show()
