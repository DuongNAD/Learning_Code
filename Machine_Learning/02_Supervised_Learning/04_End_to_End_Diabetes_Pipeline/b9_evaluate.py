"""
Bước 9: Đánh Giá Mô Hình Toàn Diện & Tối Ưu Hóa Ngưỡng Quyết Định (Threshold Tuning)
"""

import os
import sys
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from b4_split import y_train, y_test
from b5_feature import X_train_standard, X_test_standard

# ====== Model gốc (không chỉnh) ======
print("=" * 50)
print("MODEL GỐC (ngưỡng 0.5, không balanced)")
print("=" * 50)

model_v1 = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=10,
    random_state=42
)
model_v1.fit(X_train_standard, y_train)
y_pred_v1 = model_v1.predict(X_test_standard)

print(classification_report(y_test, y_pred_v1))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_v1))

y_proba_v1 = model_v1.predict_proba(X_test_standard)[:, 1]
print(f"ROC-AUC: {roc_auc_score(y_test, y_proba_v1):.4f}")

# ====== Cách 1: class_weight='balanced' ======
print("\n" + "=" * 50)
print("CÁCH 1: class_weight='balanced'")
print("=" * 50)

model_v2 = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=10,
    random_state=42,
    class_weight="balanced"
)
model_v2.fit(X_train_standard, y_train)
y_pred_v2 = model_v2.predict(X_test_standard)

print(classification_report(y_test, y_pred_v2))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_v2))

y_proba_v2 = model_v2.predict_proba(X_test_standard)[:, 1]
print(f"ROC-AUC: {roc_auc_score(y_test, y_proba_v2):.4f}")

# ====== Cách 2: Tối ưu ngưỡng từ 0.20 → 0.35 ======
print("\n" + "=" * 50)
print("CÁCH 2: QUÉT NGƯỠNG XÁC SUẤT TỪ 0.20 → 0.35")
print("=" * 50)

print(f"{'Ngưỡng':<10} {'Precision':<12} {'Recall':<10} {'F1':<10}")
print("-" * 42)

best_threshold = 0.5
best_f1 = 0.0

for t in np.arange(0.20, 0.36, 0.01):
    y_pred_t = (y_proba_v1 >= t).astype(int)
    p = precision_score(y_test, y_pred_t, zero_division=0)
    r = recall_score(y_test, y_pred_t, zero_division=0)
    f = f1_score(y_test, y_pred_t, zero_division=0)
    if f > best_f1:
        best_f1 = f
        best_threshold = round(t, 2)
    print(f"{t:<10.2f} {p:<12.4f} {r:<10.4f} {f:<10.4f}")

print(f"\n-> Ngưỡng tối ưu đạt F1 cao nhất: {best_threshold:.2f} (F1 = {best_f1:.4f})")
