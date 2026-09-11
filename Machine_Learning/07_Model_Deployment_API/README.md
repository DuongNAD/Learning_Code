# 🚀 Đóng Gói & Triển Khai Mô Hình (Model Serving & API Deployment)

Thư mục cung cấp giải pháp triển khai mô hình học máy vào thực tế thông qua RESTful API tốc độ cao với FastAPI và giao diện người dùng tương tác với Streamlit.

---

## 📂 Các Tập Tin Thành Phần

1. **`server.py`**:
   - Máy chủ API hiệu năng cao viết bằng FastAPI.
   - Tự động nạp các artifacts `model.pkl`, `scaler.pkl`, `threshold.pkl` khi khởi động.
   - Tích hợp chuẩn hóa dữ liệu đầu vào theo đúng cấu trúc khi huấn luyện.
   - Áp dụng ngưỡng xác suất đã được cân chỉnh ($0.27$) thay vì $0.5$ để tối ưu độ nhạy y khoa.
   - Tự động sinh tài liệu OpenAPI / Swagger UI tại đường dẫn `/docs`.

2. **`client.py`**:
   - Hỗ trợ 2 chế độ:
     - Chế độ dòng lệnh CLI test nhanh: `python3 client.py --cli`
     - Giao diện Web tương tác hoàn chỉnh: `streamlit run client.py`

3. **`inference.py`**:
   - Script chạy suy luận độc lập trực tiếp trong Python mà không cần mở server mạng.

4. **`model.pkl`, `scaler.pkl`, `threshold.pkl`**:
   - Các artifacts mô hình đã được đóng gói sẵn.

---

## 🛠️ Hướng Dẫn Khởi Động

### Bước 1: Khởi động FastAPI Server
```bash
python3 server.py
# Hoặc chạy bằng uvicorn:
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```
Kiểm tra tài liệu tương tác tại trình duyệt: [http://localhost:8000/docs](http://localhost:8000/docs)

### Bước 2: Thử nghiệm gửi dữ liệu từ Client
- **Cách 1: Kiểm thử nhanh CLI**:
```bash
python3 client.py --cli
```
- **Cách 2: Mở giao diện Streamlit**:
```bash
streamlit run client.py
```
- **Cách 3: Gọi trực tiếp qua Python**:
```bash
python3 inference.py
```
