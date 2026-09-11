"""
Client for Diabetes Prediction API.
Dual-mode:
1. CLI test mode: `python3 client.py --cli`
2. Streamlit Web App: `streamlit run client.py`
"""

import sys
import requests

DEFAULT_URL = "http://127.0.0.1:8000/predict"

def run_cli_test():
    sample_payload = {
        "Pregnancies": 3.0,
        "Glucose": 155.0,
        "BloodPressure": 78.0,
        "SkinThickness": 28.0,
        "Insulin": 120.0,
        "BMI": 32.4,
        "DiabetesPedigreeFunction": 0.62,
        "Age": 45.0
    }
    print("Sending POST request to FastAPI server...")
    try:
        res = requests.post(DEFAULT_URL, json=sample_payload, timeout=5)
        if res.status_code == 200:
            print("Response from server:", res.json())
        else:
            print(f"Server responded with status {res.status_code}: {res.text}")
    except requests.exceptions.ConnectionError:
        print(f"Could not connect to {DEFAULT_URL}. Make sure server.py is running via uvicorn!")

if "--cli" in sys.argv:
    run_cli_test()
    sys.exit(0)

# Streamlit mode
try:
    import streamlit as st
    st.set_page_config(page_title="Hệ Thống Dự Đoán Tiểu Đường", page_icon="🩺", layout="centered")
    st.title("🩺 Hệ Thống Hỗ Trợ Chẩn Đoán Nguy Cơ Tiểu Đường")
    st.markdown("Mô hình Machine Learning (Random Forest) được chuẩn hóa và cân bằng ngưỡng tối ưu.")

    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input("Số lần mang thai (Pregnancies)", min_value=0.0, max_value=25.0, value=2.0)
        Glucose = st.number_input("Chỉ số đường huyết (Glucose, mg/dL)", min_value=0.0, max_value=300.0, value=120.0)
        BloodPressure = st.number_input("Huyết áp (Blood Pressure, mm Hg)", min_value=0.0, max_value=200.0, value=70.0)
        SkinThickness = st.number_input("Độ dày da (Skin Thickness, mm)", min_value=0.0, max_value=100.0, value=20.0)
    with col2:
        Insulin = st.number_input("Chỉ số Insulin (mu U/ml)", min_value=0.0, max_value=900.0, value=100.0)
        BMI = st.number_input("Chỉ số BMI (kg/m²)", min_value=0.0, max_value=70.0, value=29.3)
        DiabetesPedigreeFunction = st.number_input("Chỉ số di truyền (Pedigree)", min_value=0.0, max_value=3.0, value=0.5, step=0.05)
        Age = st.number_input("Tuổi (Age)", min_value=1.0, max_value=120.0, value=35.0)

    if st.button("🚀 Dự Đoán Nguy Cơ", use_container_width=True):
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
            resp = requests.post(DEFAULT_URL, json=input_data, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                st.subheader("📊 Kết Quả Phân Tích")
                if data["prediction"] == 1:
                    st.error(f"⚠️ **{data['meaning']}** (Xác suất: {data['probability']*100:.1f}%)")
                else:
                    st.success(f"✅ **{data['meaning']}** (Xác suất: {data['probability']*100:.1f}%)")
                st.info(f"💡 **Khuyến nghị lâm sàng**: {data['clinical_recommendation']}")
            else:
                st.error("API trả về lỗi: " + resp.text)
        except requests.exceptions.ConnectionError:
            st.error("Không thể kết nối tới server. Vui lòng khởi động `python3 server.py` trước!")
except ImportError:
    pass