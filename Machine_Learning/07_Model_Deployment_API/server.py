"""
FastAPI Server for Diabetes Prediction Pipeline.
Supports calibrated probability thresholding and detailed diagnostic payloads.
"""

import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_DIR, "model.pkl")
SCALER_PATH = os.path.join(CURRENT_DIR, "scaler.pkl")
THRESHOLD_PATH = os.path.join(CURRENT_DIR, "threshold.pkl")

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

app = FastAPI(
    title="Diabetes Prediction & Clinical Decision Support API",
    version="2.0.0",
    description="Production-ready FastAPI endpoint serving calibrated Random Forest model."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load artifacts
model = None
scaler = None
threshold = 0.27

@app.on_event("startup")
def load_artifacts():
    global model, scaler, threshold
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise RuntimeError(f"Missing model or scaler in {CURRENT_DIR}")
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    if os.path.exists(THRESHOLD_PATH):
        threshold = joblib.load(THRESHOLD_PATH)
    print(f"Loaded model ({type(model).__name__}), scaler, and threshold ({threshold})")

class DiabetesInput(BaseModel):
    Pregnancies: float = Field(..., example=2.0, description="Số lần mang thai")
    Glucose: float = Field(..., example=120.0, description="Nồng độ Glucose huyết tương")
    BloodPressure: float = Field(..., example=70.0, description="Huyết áp tâm trương (mm Hg)")
    SkinThickness: float = Field(..., example=20.0, description="Độ dày nếp gấp da cơ tam đầu (mm)")
    Insulin: float = Field(..., example=100.0, description="Insulin huyết thanh 2 giờ (mu U/ml)")
    BMI: float = Field(..., example=29.3, description="Chỉ số khối cơ thể (kg/m^2)")
    DiabetesPedigreeFunction: float = Field(..., example=0.5, description="Hàm phả hệ bệnh tiểu đường")
    Age: float = Field(..., example=35.0, description="Tuổi (năm)")

class PredictionOutput(BaseModel):
    prediction: int
    probability: float
    threshold_applied: float
    meaning: str
    clinical_recommendation: str

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Diabetes Risk Inference Service",
        "docs": "/docs",
        "calibrated_threshold": threshold
    }

@app.post("/predict", response_model=PredictionOutput)
def predict_diabetes(data: DiabetesInput):
    global model, scaler, threshold
    if model is None or scaler is None:
        load_artifacts()

    input_dict = {
        "Pregnancies": data.Pregnancies,
        "Glucose": data.Glucose,
        "BloodPressure": data.BloodPressure,
        "SkinThickness": data.SkinThickness,
        "Insulin": data.Insulin,
        "BMI": data.BMI,
        "DiabetesPedigreeFunction": data.DiabetesPedigreeFunction,
        "Age": data.Age
    }
    
    df = pd.DataFrame([input_dict], columns=FEATURE_NAMES)
    scaled = scaler.transform(df)
    prob = float(model.predict_proba(scaled)[0, 1])
    is_positive = int(prob >= threshold)
    
    meaning = "Có nguy cơ tiểu đường cao" if is_positive == 1 else "Nguy cơ tiểu đường thấp / Bình thường"
    recommendation = (
        "Khuyến nghị làm xét nghiệm OGTT chuyên sâu và hội chẩn với bác sĩ chuyên khoa nội tiết."
        if is_positive == 1
        else "Duy trì chế độ dinh dưỡng và lối sống lành mạnh, tái khám định kỳ hàng năm."
    )
    
    return {
        "prediction": is_positive,
        "probability": round(prob, 4),
        "threshold_applied": threshold,
        "meaning": meaning,
        "clinical_recommendation": recommendation
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)