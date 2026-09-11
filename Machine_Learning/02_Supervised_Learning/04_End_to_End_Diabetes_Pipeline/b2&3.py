"""
Bước 2 & 3: Tiền Xử Lý Dữ Liệu & Làm Sạch Giá Trị Bất Thường / Ngoại Lai
"""

import os
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "diabetes.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/diabetes/diabetes.csv")

df = pd.read_csv(DATA_PATH)
print(f"Kích thước ban đầu: {df.shape}")


def remove_outliers(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Lọc bỏ các giá trị ngoại lai dựa trên phương pháp biên tứ phân vị IQR."""
    q1 = data[column_name].quantile(0.25)
    q3 = data[column_name].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return data[(data[column_name] >= lower_bound) & (data[column_name] <= upper_bound)]


# 1. Loại bỏ các giá trị sinh học vô lý (bằng 0 đối với Glucose, BloodPressure, SkinThickness, Insulin, BMI)
df = df[
    (df["Glucose"] > 0)
    & (df["BloodPressure"] > 0)
    & (df["SkinThickness"] > 0)
    & (df["Insulin"] > 0)
    & (df["BMI"] > 0)
]
print(f"Kích thước sau khi lọc giá trị = 0: {df.shape}")

# 2. Loại bỏ outliers theo IQR
for col in ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]:
    df = remove_outliers(df, col)

print(f"Kích thước sau khi lọc ngoại lai IQR: {df.shape}")

output_path = os.path.join(CURRENT_DIR, "diabetes_cleaned.csv")
df.to_csv(output_path, index=False)
print(f"Đã lưu tập dữ liệu sạch tại: {output_path}")
