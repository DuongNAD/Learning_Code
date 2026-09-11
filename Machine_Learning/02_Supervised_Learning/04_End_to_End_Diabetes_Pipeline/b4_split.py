"""
Bước 4: Phân Chia Tập Dữ Liệu Huấn Luyện / Kiểm Thử (Train/Test Split)
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "diabetes_cleaned.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/diabetes/diabetes_cleaned.csv")

df = pd.read_csv(DATA_PATH)
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

if __name__ == "__main__":
    print("=== PHÂN CHIA TẬP DỮ LIỆU ===")
    print("Train shape:", X_train.shape)
    print("Test shape: ", X_test.shape)
    print("Phân bố nhãn train:\n", y_train.value_counts())
    print("Phân bố nhãn test:\n", y_test.value_counts())
