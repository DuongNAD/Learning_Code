# api.py

from fastapi import FastAPI
from pydantic import BaseModel
import pickle


# =========================
# 1. Load model và scaler
# =========================

# File model.pkl cần nằm cùng thư mục với file api.py
with open("model.pkl", "rb") as file:
    model, scaler = pickle.load(file)


# =========================
# 2. Tạo FastAPI app
# =========================

app = FastAPI()


# =========================
# 3. Định nghĩa dữ liệu đầu vào
# =========================

class DiabetesInput(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float


# =========================
# 4. API kiểm tra server
# =========================

@app.get("/")
def home():
    return {
        "message": "Diabetes Prediction API is running"
    }


# =========================
# 5. API dự đoán tiểu đường
# =========================

@app.post("/predict")
def predict_diabetes(data: DiabetesInput):

    # Chuyển dữ liệu người dùng nhập thành list 2 chiều
    input_data = [[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]]

    # Scale dữ liệu giống như khi train model
    input_data_scaled = scaler.transform(input_data)

    # Dự đoán
    prediction = model.predict(input_data_scaled)[0]

    # Trả kết quả về client
    return {
        "prediction": int(prediction),
        "meaning": "Có nguy cơ tiểu đường" if int(prediction) == 1 else "Không có nguy cơ tiểu đường"
    }