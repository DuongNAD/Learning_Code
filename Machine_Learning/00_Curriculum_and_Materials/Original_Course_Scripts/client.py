# app.py

import streamlit as st
import requests


# =========================
# 1. Cấu hình giao diện
# =========================

st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)


# =========================
# 2. Tiêu đề app
# =========================

st.title("🩺 Diabetes Prediction App")

st.write("Nhập 8 thông tin bên dưới để dự đoán một người có nguy cơ bị tiểu đường hay không.")


# =========================
# 3. Form nhập dữ liệu
# =========================

Pregnancies = st.number_input("Pregnancies", min_value=0.0, value=2.0)
Glucose = st.number_input("Glucose", min_value=0.0, value=120.0)
BloodPressure = st.number_input("BloodPressure", min_value=0.0, value=70.0)
SkinThickness = st.number_input("SkinThickness", min_value=0.0, value=20.0)
Insulin = st.number_input("Insulin", min_value=0.0, value=100.0)
BMI = st.number_input("BMI", min_value=0.0, value=29.3)
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", min_value=0.0, value=0.5)
Age = st.number_input("Age", min_value=0.0, value=35.0)


# =========================
# 4. Gọi API khi bấm nút
# =========================

if st.button("Predict"):

    # Dữ liệu gửi sang FastAPI
    input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }

    try:
        # Gửi request sang FastAPI server
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=input_data
        )

        # Nếu gọi API thành công
        if response.status_code == 200:
            result = response.json()

            prediction = result["prediction"]
            meaning = result["meaning"]

            st.subheader("Kết quả dự đoán")

            if prediction == 1:
                st.error(f"Prediction = {prediction}: {meaning}")
            else:
                st.success(f"Prediction = {prediction}: {meaning}")

        # Nếu API trả về lỗi
        else:
            st.error("API trả về lỗi. Hãy kiểm tra lại FastAPI server.")

    except requests.exceptions.ConnectionError:
        st.error("Không kết nối được tới FastAPI server. Hãy chạy api.py trước.")