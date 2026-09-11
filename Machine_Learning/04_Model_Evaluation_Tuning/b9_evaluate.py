import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from b4_split import y_train, y_test
from b5_feature import X_train_standard, X_test_standard

# ====== Model gốc (không chỉnh) ======
print("=" * 50)
print("MODEL GỐC (ngưỡng 0.5, không balanced)")
print("=" * 50)

model_v1 = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    min_samples_split=10,
    random_state=42
)
model_v1.fit(X_train_standard, y_train)
y_pred_v1 = model_v1.predict(X_test_standard)

print(classification_report(y_test, y_pred_v1))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_v1))

y_proba_v1 = model_v1.predict_proba(X_test_standard)[:, 1]
print("ROC-AUC:", roc_auc_score(y_test, y_proba_v1))

# ====== Cách 1: class_weight='balanced' ======
print("\n" + "=" * 50)
print("CÁCH 1: class_weight='balanced'")
print("=" * 50)

model_v2 = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    min_samples_split=10,
    random_state=42,
    class_weight='balanced'  # phạt nặng khi bỏ sót class 1
)
model_v2.fit(X_train_standard, y_train)
y_pred_v2 = model_v2.predict(X_test_standard)

print(classification_report(y_test, y_pred_v2))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_v2))

y_proba_v2 = model_v2.predict_proba(X_test_standard)[:, 1]
print("ROC-AUC:", roc_auc_score(y_test, y_proba_v2))

# ====== Cách 2: Hạ ngưỡng từ 0.5 → 0.3 ======
print("\n" + "=" * 50)
print("CÁCH 2: THỬ NGƯỠNG TỪ 0.20 → 0.30")
print("=" * 50)

from sklearn.metrics import precision_score, recall_score, f1_score

print(f"{'Ngưỡng':<10} {'Precision':<12} {'Recall':<10} {'F1':<10}")
print("-" * 42)

for t in np.arange(0.20, 0.31, 0.01):
    y_pred_t = (y_proba_v1 >= t).astype(int)
    p = precision_score(y_test, y_pred_t)
    r = recall_score(y_test, y_pred_t)
    f = f1_score(y_test, y_pred_t)
    print(f"{t:<10.2f} {p:<12.4f} {r:<10.4f} {f:<10.4f}")

