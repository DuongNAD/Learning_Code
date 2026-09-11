"""
Bước 5: Kỹ Thuật Chuẩn Hóa Đặc Trưng (Feature Scaling)
"""

import os
import sys
from sklearn.preprocessing import StandardScaler, MinMaxScaler

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from b4_split import X_train, X_test

MinMax_scaler = MinMaxScaler()
Standard_scaler = StandardScaler()

MinMax_scaler.fit(X_train)
X_train_minmax = MinMax_scaler.transform(X_train)
X_test_minmax = MinMax_scaler.transform(X_test)

Standard_scaler.fit(X_train)
X_train_standard = Standard_scaler.transform(X_train)
X_test_standard = Standard_scaler.transform(X_test)

if __name__ == "__main__":
    print("=== CHUẨN HÓA ĐẶC TRƯNG HOÀN TẤT ===")
    print(f"X_train_standard mean: {X_train_standard.mean(axis=0).round(2)}")
    print(f"X_train_standard std:  {X_train_standard.std(axis=0).round(2)}")
