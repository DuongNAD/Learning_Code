"""
02_Classification: Diabetes Classification with Random Forest
============================================================
Demonstrates supervised classification pipeline:
- Feature scaling with StandardScaler
- Hyperparameter tuning with GridSearchCV (optimizing F1-score)
- Model serialization with pickle
- In-depth evaluation via Confusion Matrix and Classification Report
"""

import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Dynamic path resolution
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "diabetes.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/diabetes/diabetes.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Diabetes dataset not found at {DATA_PATH}")

print(f"Loading Diabetes dataset from: {DATA_PATH}")
data = pd.read_csv(DATA_PATH)
target = "Outcome"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=1009,
    stratify=y
)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

params = {
    "n_estimators": [50, 100],
    "criterion": ["gini", "entropy"],
    "max_depth": [5, 10, None]
}

print("Bắt đầu huấn luyện Random Forest với GridSearchCV (cv=5)...")
model = GridSearchCV(
    RandomForestClassifier(random_state=100),
    param_grid=params,
    cv=5,
    scoring="f1",
    verbose=0,
    n_jobs=-1
)

model.fit(x_train_scaled, y_train)
print(f"\nĐiểm F1 tốt nhất (Cross-Validation): {model.best_score_:.4f}")
print(f"Siêu tham số tối ưu: {model.best_params_}")

# Lưu mô hình và scaler
model_save_path = os.path.join(CURRENT_DIR, "model.pkl")
with open(model_save_path, "wb") as file:
    pickle.dump([model, scaler], file)
print(f"Đã lưu mô hình & scaler tại: {model_save_path}")

y_predict = model.predict(x_test_scaled)

print("\n=== MA TRẬN NHẦM LẪN (CONFUSION MATRIX) ===")
print(confusion_matrix(y_test, y_predict))

print("\n=== BÁO CÁO PHÂN LOẠI (CLASSIFICATION REPORT) ===")
print(classification_report(y_test, y_predict))
