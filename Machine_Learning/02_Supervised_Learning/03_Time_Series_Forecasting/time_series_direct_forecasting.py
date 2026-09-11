"""
03_Time_Series_Forecasting: Direct Multi-Step Forecasting
=========================================================
Demonstrates direct multi-step forecasting strategy:
Instead of recursively feeding predictions back, train N independent regression models,
each predicting a specific future horizon (t+1, t+2, ..., t+H).
"""

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "co2.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/time_series/co2.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"co2.csv dataset not found at {DATA_PATH}")


def create_direct_data(data: pd.DataFrame, window_size: int = 5, target_size: int = 3) -> pd.DataFrame:
    """Tạo tập dữ liệu cho phương pháp dự báo trực tiếp đa bước (Direct Forecasting)."""
    df = data.copy()
    i = 1
    while i < window_size:
        df[f"co2_{i}"] = df["co2"].shift(-i)
        i += 1
    i = 0
    while i < target_size:
        df[f"target_{i}"] = df["co2"].shift(-window_size - i)
        i += 1
    df = df.dropna(axis=0).reset_index(drop=True)
    return df


print(f"Loading CO2 dataset for Direct Multi-Step Forecasting: {DATA_PATH}")
raw_data = pd.read_csv(DATA_PATH)
raw_data["time"] = pd.to_datetime(raw_data["time"], yearfirst=True)
raw_data["co2"] = raw_data["co2"].interpolate()

window_size = 5
target_size = 3
data = create_direct_data(raw_data, window_size, target_size)
targets = [f"target_{i}" for i in range(target_size)]
x = data.drop(["time"] + targets, axis=1)
y = data[targets]

train_size = 0.8
num_sample = len(x)
split_idx = int(num_sample * train_size)

x_train = x[:split_idx]
y_train = y[:split_idx]
x_test = x[split_idx:]
y_test = y[split_idx:]

regs = [LinearRegression() for _ in range(target_size)]
for i, reg in enumerate(regs):
    reg.fit(x_train, y_train[f"target_{i}"])

print("\n=== KẾT QUẢ DỰ BÁO TRỰC TIẾP ĐA BƯỚC (DIRECT MULTI-STEP) ===")
for i, reg in enumerate(regs):
    y_predict = reg.predict(x_test)
    step_r2 = r2_score(y_test[f"target_{i}"], y_predict)
    step_mae = mean_absolute_error(y_test[f"target_{i}"], y_predict)
    step_mse = mean_squared_error(y_test[f"target_{i}"], y_predict)
    step_rmse = np.sqrt(step_mse)
    horizon = window_size + i
    print(f"Bước tương lai t+{horizon:02d} | R²: {step_r2:7.4f} | MAE: {step_mae:6.4f} ppm | RMSE: {step_rmse:6.4f} ppm")
