"""
Bước 10: Đóng Gói và Xuất Bản Các Tệp Trọng Số Mô Hình (Artifact Serialization)
"""

import os
import sys
import joblib
from sklearn.ensemble import RandomForestClassifier

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from b4_split import y_train
from b5_feature import X_train_standard, Standard_scaler

# 1. Huấn luyện model tối ưu nhất
best_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=10,
    random_state=42
)
best_model.fit(X_train_standard, y_train)

# 2. Lưu model + scaler + ngưỡng vào đúng thư mục hiện hành
model_path = os.path.join(CURRENT_DIR, "model.pkl")
scaler_path = os.path.join(CURRENT_DIR, "scaler.pkl")
threshold_path = os.path.join(CURRENT_DIR, "threshold.pkl")

joblib.dump(best_model, model_path)
joblib.dump(Standard_scaler, scaler_path)
joblib.dump(0.27, threshold_path)

print(f"Đã lưu thành công các artifacts tại {CURRENT_DIR}:")
print(f" - Model:     {model_path}")
print(f" - Scaler:    {scaler_path}")
print(f" - Threshold: {threshold_path} (0.27)")
