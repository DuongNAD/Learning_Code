"""
03_Time_Series_Forecasting: Recursive Sliding Window Forecasting
================================================================
Demonstrates lag feature engineering for univariate time series (Mauna Loa CO2 dataset):
- Interpolation of missing timestamps
- Recursive lag feature construction (window_size = 5)
- Train/Test chronological split (preventing lookahead bias)
- Multi-metric evaluation (MAE, MSE, RMSE, R2)
- Visualizing and saving time series forecast curves
"""

import os
import matplotlib
# If running without interactive display, use Agg backend
if not os.environ.get("DISPLAY") and not os.environ.get("MPLBACKEND"):
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "co2.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/time_series/co2.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"co2.csv dataset not found at {DATA_PATH}")


def create_recursive_data(data: pd.DataFrame, window_size: int = 5) -> pd.DataFrame:
    """Tạo các đặc trưng trễ (lag features) cho chuỗi thời gian."""
    df = data.copy()
    i = 1
    while i < window_size:
        df[f"co2_{i}"] = df["co2"].shift(-i)
        i += 1
    df["target"] = df["co2"].shift(-window_size)
    df = df.dropna(axis=0).reset_index(drop=True)
    return df


print(f"Loading CO2 time-series dataset from: {DATA_PATH}")
raw_data = pd.read_csv(DATA_PATH)
raw_data["time"] = pd.to_datetime(raw_data["time"], yearfirst=True)
raw_data["co2"] = raw_data["co2"].interpolate()

window_size = 5
data = create_recursive_data(raw_data, window_size)
x = data.drop(["target", "time"], axis=1)
y = data["target"]

train_size = 0.8
num_sample = len(x)
split_idx = int(num_sample * train_size)

x_train = x[:split_idx]
y_train = y[:split_idx]
x_test = x[split_idx:]
y_test = y[split_idx:]

print(f"Train samples: {len(x_train)} | Test samples: {len(x_test)}")

model = RandomForestRegressor(n_estimators=100, random_state=1009)
model.fit(x_train, y_train)
y_predict = model.predict(x_test)

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predict)

print("\n=== KẾT QUẢ DỰ BÁO CHUỖI THỜI GIAN CO2 ===")
print(f"MAE  (Mean Absolute Error):  {mae:.4f} ppm")
print(f"MSE  (Mean Squared Error):   {mse:.4f}")
print(f"RMSE (Root Mean Sq Error):   {rmse:.4f} ppm")
print(f"R²   (Coefficient of Det):   {r2:.4f}")

# Vẽ và lưu biểu đồ dự báo
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data["time"][:split_idx], y_train, label="Train (Thực tế)", color="blue", alpha=0.7)
ax.plot(data["time"][split_idx:], y_test, label="Test (Thực tế)", color="green", alpha=0.8)
ax.plot(data["time"][split_idx:], y_predict, label="Prediction (Dự báo RF)", color="red", linestyle="--")
ax.set_xlabel("Năm")
ax.set_ylabel("Nồng độ CO2 (ppm)")
ax.set_title("Dự Báo Chuỗi Thời Gian CO2 Bằng Random Forest (Recursive Sliding Window)")
ax.legend()
ax.grid(True, linestyle=":", alpha=0.6)

plot_save_path = os.path.join(CURRENT_DIR, "time_series_forecast.png")
fig.savefig(plot_save_path, dpi=150, bbox_inches="tight")
print(f"Đã lưu biểu đồ dự báo tại: {plot_save_path}")
plt.close(fig)
