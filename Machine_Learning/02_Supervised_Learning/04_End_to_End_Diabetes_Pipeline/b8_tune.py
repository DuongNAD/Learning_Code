"""
Bước 8: Tinh Chỉnh Siêu Tham Số (Hyperparameter Tuning với GridSearchCV)
"""

import os
import sys
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from b4_split import y_train
from b5_feature import X_train_standard

print("=== BẮT ĐẦU TINH CHỈNH SIÊU THAM SỐ (GRIDSEARCHCV) ===")

# --- Tune Decision Tree ---
grid_dt = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    {"max_depth": [3, 5, 10, None], "min_samples_split": [2, 5, 10], "min_samples_leaf": [1, 2, 5]},
    cv=5, scoring="accuracy"
)
grid_dt.fit(X_train_standard, y_train)
print(f"Decision Tree best: {grid_dt.best_params_} | Score: {grid_dt.best_score_:.4f}")

# --- Tune Random Forest ---
grid_rf = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {"n_estimators": [50, 100, 150], "max_depth": [3, 5, 10, None], "min_samples_split": [2, 5, 10]},
    cv=5, scoring="accuracy"
)
grid_rf.fit(X_train_standard, y_train)
print(f"Random Forest best: {grid_rf.best_params_} | Score: {grid_rf.best_score_:.4f}")

# --- Tune KNN ---
grid_knn = GridSearchCV(
    KNeighborsClassifier(),
    {"n_neighbors": [3, 5, 7, 9, 11], "weights": ["uniform", "distance"]},
    cv=5, scoring="accuracy"
)
grid_knn.fit(X_train_standard, y_train)
print(f"KNN best:           {grid_knn.best_params_} | Score: {grid_knn.best_score_:.4f}")
