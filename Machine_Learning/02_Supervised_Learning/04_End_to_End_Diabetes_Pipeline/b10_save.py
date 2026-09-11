import joblib
from sklearn.ensemble import RandomForestClassifier
from b4_split import y_train
from b5_feature import X_train_standard, Standard_scaler

# 1. Train model tốt nhất (thông số từ B8)
best_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    min_samples_split=10,
    random_state=42
)
best_model.fit(X_train_standard, y_train)

# 2. Lưu model + scaler + ngưỡng
joblib.dump(best_model, "model.pkl")
joblib.dump(Standard_scaler, "scaler.pkl")
joblib.dump(0.27, "threshold.pkl")

print("Đã lưu: model.pkl, scaler.pkl, threshold.pkl")
