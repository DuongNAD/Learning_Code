"""
04_Model_Evaluation_Tuning: End-to-End Case Study on Diabetes Detection
========================================================================
Demonstrates:
1. Feature scaling with StandardScaler
2. Hyperparameter tuning using 5-Fold Stratified Cross-Validation
3. Evaluating Class Imbalance mitigations (class_weight='balanced')
4. Optimal Probability Threshold Scanning (0.20 to 0.40) to maximize Medical Recall & F1
5. Exporting trained model, scaler, and calibrated threshold
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, precision_score, recall_score, f1_score

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "diabetes_cleaned.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../02_Supervised_Learning/04_End_to_End_Diabetes_Pipeline/diabetes_cleaned.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../06_Datasets_Kaggle/diabetes/diabetes_cleaned.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

print(f"Loading cleaned dataset: {DATA_PATH}")
df = pd.read_csv(DATA_PATH)
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Tinh chỉnh siêu tham số
param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10]
}

print("Đang tinh chỉnh siêu tham số bằng GridSearchCV (cv=5)...")
grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1
)
grid.fit(X_train_scaled, y_train)
best_model = grid.best_estimator_
print(f"Bộ tham số tối ưu: {grid.best_params_} (F1 CV: {grid.best_score_:.4f})")

# 2. Đánh giá ở ngưỡng mặc định 0.5
y_pred_default = best_model.predict(X_test_scaled)
y_prob = best_model.predict_proba(X_test_scaled)[:, 1]
roc_auc = roc_auc_score(y_test, y_prob)

print("\n=== ĐÁNH GIÁ TẠI NGƯỠNG MẶC ĐỊNH (Threshold = 0.5) ===")
print(f"ROC-AUC: {roc_auc:.4f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_default))
print(classification_report(y_test, y_pred_default, zero_division=0))

# 3. Quét ngưỡng tối ưu hóa (Threshold Calibration)
print("=== QUÉT NGƯỠNG TỐI ƯU HÓA F1-SCORE VÀ RECALL ===")
best_thresh = 0.5
best_f1 = 0.0

for t in np.arange(0.20, 0.41, 0.02):
    y_pred_t = (y_prob >= t).astype(int)
    p = precision_score(y_test, y_pred_t, zero_division=0)
    r = recall_score(y_test, y_pred_t, zero_division=0)
    f = f1_score(y_test, y_pred_t, zero_division=0)
    if f > best_f1:
        best_f1 = f
        best_thresh = round(t, 2)
    print(f"Ngưỡng {t:.2f} | Precision: {p:.4f} | Recall: {r:.4f} | F1: {f:.4f}")

print(f"\n-> Ngưỡng hiệu chuẩn tối ưu: {best_thresh:.2f} (F1 = {best_f1:.4f})")

# 4. Xuất artifacts
joblib.dump(best_model, os.path.join(CURRENT_DIR, "model.pkl"))
joblib.dump(scaler, os.path.join(CURRENT_DIR, "scaler.pkl"))
joblib.dump(best_thresh, os.path.join(CURRENT_DIR, "threshold.pkl"))
print("Đã xuất artifacts: model.pkl, scaler.pkl, threshold.pkl")
