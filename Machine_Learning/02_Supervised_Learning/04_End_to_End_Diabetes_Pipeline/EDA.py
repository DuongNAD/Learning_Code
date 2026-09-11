"""
Bước 1: Khám Phá Dữ Liệu Ban Đầu (Exploratory Data Analysis - EDA)
"""

import os
import matplotlib
if not os.environ.get("DISPLAY") and not os.environ.get("MPLBACKEND"):
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "diabetes.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/diabetes/diabetes.csv")

df = pd.read_csv(DATA_PATH)

print("=== 1. HÌNH DẠNG & THÔNG TIN DỮ LIỆU ===")
print("Kích thước bảng:", df.shape)
print("\nTên các cột:", df.columns.tolist())
print("\nKiểu dữ liệu:")
print(df.dtypes)

print("\n=== 2. KIỂM TRA GIÁ TRỊ THIẾU (NULL) ===")
print(df.isnull().sum())

print("\n=== 3. THỐNG KÊ MÔ TẢ (DESCRIPTIVE STATS) ===")
print(df.describe())

print("\n=== 4. PHÂN BỐ LỚP MỤC TIÊU (OUTCOME) ===")
print(df["Outcome"].value_counts())
print("\nTỷ lệ phần trăm:")
print(df["Outcome"].value_counts(normalize=True).apply(lambda x: f"{x*100:.2f}%"))

# Vẽ và lưu biểu đồ phân bố tần suất
fig = df.hist(figsize=(12, 8), bins=20)
plt.tight_layout()
plot_path = os.path.join(CURRENT_DIR, "eda_distribution.png")
plt.savefig(plot_path, dpi=150)
plt.close()
print(f"\nĐã lưu biểu đồ phân phối tại: {plot_path}")
