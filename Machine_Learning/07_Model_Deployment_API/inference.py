"""
Inference script for Diabetes Risk Prediction.
Loads model.pkl, scaler.pkl, and threshold.pkl produced by the training pipeline.
"""

import os
import joblib
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_DIR, "model.pkl")
SCALER_PATH = os.path.join(CURRENT_DIR, "scaler.pkl")
THRESHOLD_PATH = os.path.join(CURRENT_DIR, "threshold.pkl")

# Feature names exactly matching training pipeline
FEATURE_NAMES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

def load_artifacts():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("model.pkl or scaler.pkl not found in current directory.")
    
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    threshold = joblib.load(THRESHOLD_PATH) if os.path.exists(THRESHOLD_PATH) else 0.5
    return model, scaler, threshold

def predict(input_features: dict, model=None, scaler=None, threshold=None):
    if model is None or scaler is None or threshold is None:
        model, scaler, threshold = load_artifacts()

    # Convert to DataFrame to retain feature names
    df = pd.DataFrame([input_features], columns=FEATURE_NAMES)
    scaled_data = scaler.transform(df)
    
    proba = float(model.predict_proba(scaled_data)[0, 1])
    is_positive = int(proba >= threshold)
    
    return {
        "prediction": is_positive,
        "probability": round(proba, 4),
        "threshold_used": threshold,
        "risk_level": "Cao (Nguy cơ tiểu đường)" if is_positive == 1 else "Thấp (Bình thường)"
    }

if __name__ == "__main__":
    sample_patient = {
        "Pregnancies": 2.0,
        "Glucose": 150.0,
        "BloodPressure": 75.0,
        "SkinThickness": 25.0,
        "Insulin": 110.0,
        "BMI": 30.5,
        "DiabetesPedigreeFunction": 0.55,
        "Age": 42.0
    }
    
    print("--- Chạy dự đoán mẫu ---")
    result = predict(sample_patient)
    print("Thông số bệnh nhân:", sample_patient)
    print("Kết quả:", result)