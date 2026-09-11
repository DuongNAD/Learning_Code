"""
Bước 6 & 7: Thử Nghiệm Huấn Luyện Các Mô Hình Cơ Sở (Model Spot-Checking)
"""

import os
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from b4_split import y_train, y_test
from b5_feature import X_train_standard, X_test_standard

models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
}

print("=== ĐIỂM CHÍNH XÁC CÁC MÔ HÌNH CƠ SỞ (BASELINE) ===")
for name, model in models.items():
    model.fit(X_train_standard, y_train)
    score = model.score(X_test_standard, y_test)
    print(f"{name:<20}: {score:.4f}")
