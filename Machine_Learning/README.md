# 🧠 Machine Learning & AI Mastery Hub (DeepTutor Powered)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-orange.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![DeepTutor](https://img.shields.io/badge/DeepTutor-AI%20Mentor-7928CA.svg)](file:///Volumes/KINGSTON/02_Learning_Knowledge/Machine_Learning/GEMINI.md)

Không gian tự học và thực chiến Học Máy & Trí Tuệ Nhân Tạo toàn diện, được tích hợp sư phạm hóa bởi **DeepTutor AI Mentor**. Không gian này tích hợp toàn bộ kho tài liệu 18 bài học chuyên sâu, hệ thống bài tập thực hành trực quan tương tác, pipeline học máy chuẩn công nghiệp end-to-end và máy chủ triển khai mô hình thời gian thực.

---

## 🗂️ Bản Đồ Kiến Trúc Hệ Thống (Directory Architecture)

```
Machine_Learning/
├── 00_Curriculum_and_Materials/        # Giáo trình 18 bài, Slide tương tác KaTeX, PDF, Transcripts
│   ├── AI_ML_Mastery_Slides.html       # Bộ slide bài giảng hỗ trợ offline
│   ├── GIAO_TRINH_CHI_TIET_...md       # Đề cương chi tiết và chuẩn năng lực
│   ├── Data Science_Machine...pdf      # Giáo trình chuyên khảo hoàn chỉnh
│   └── Transcripts/                    # 18 file phụ đề bài giảng (.vi.vtt)
├── 01_Math_Foundations/                # Nền tảng Toán học & Thuật toán cơ sở
│   ├── math_primer.py                  # Code thực hành 4 trụ cột toán học ML
│   ├── Ex1_Python_Math_Algorithms/     # 8 bài tập gốc + 16 bài tập mở rộng + Web Hub trực quan
│   └── Ex2_NLP_Text_Probability/       # NumPy cơ bản & Phân tích tần suất ngôn ngữ
├── 02_Supervised_Learning/             # Học có giám sát (Hồi quy, Phân loại, Chuỗi thời gian)
│   ├── 01_Regression/                  # Hồi quy tuyến tính & đa thức (StudentScore.xls)
│   ├── 02_Classification/              # Cây quyết định, Random Forest, NLP Job Classification
│   ├── 03_Time_Series_Forecasting/     # Dự báo chuỗi thời gian nồng độ CO2
│   └── 04_End_to_End_Diabetes_Pipeline/# Pipeline 10 bước chuẩn y tế dự đoán tiểu đường
├── 03_Unsupervised_Learning/           # Học không giám sát & Hệ gợi ý
│   ├── Clustering_and_Dimensionality...# K-Means, Elbow method, Silhouette Score, PCA 2D
│   └── Recommender_Systems/            # Gợi ý phim MovieLens theo Content-Based Filtering
├── 04_Model_Evaluation_Tuning/         # Thẩm định mô hình, Tối ưu ngưỡng & Hyperparameters
│   ├── model_evaluation_metrics.py     # Thư viện đo lường phân loại/hồi quy, tối ưu ngưỡng F1/Youden
│   ├── hyperparameter_tuning_suite.py  # So sánh Grid vs Random Search & Chẩn đoán Overfitting
│   ├── model_benchmark_comparison.py   # Bảng xếp hạng benchmark đa mô hình tự động
│   └── diabetes_tuning_case_study.py   # Case study thực chiến tối ưu ngưỡng trên tập dữ liệu tiểu đường
├── 05_Deep_Learning_Basics/            # Nhập môn Học sâu & Mạng nơ-ron
│   ├── perceptron_from_scratch.py      # Thuật toán Perceptron từ đầu & Nghịch lý XOR
│   ├── mlp_backprop_numpy.py           # Mạng MLP 2 tầng & Backpropagation giải quyết XOR
│   ├── pytorch_mnist_demo.py           # Huấn luyện mô hình PyTorch nhận dạng số viết tay (>96%)
│   └── mnist.npz                       # Bộ dữ liệu offline 70,000 ảnh MNIST
├── 06_Datasets_Kaggle/                 # Kho dữ liệu tập trung (Data Lake)
│   ├── diabetes/, csgo/, stroke/, movie_lens/, time_series/, student_score/, mnist/, job_classification/, car/
│   └── README.md                       # Từ điển dữ liệu và mô tả chi tiết từng bộ dataset
├── 07_Model_Deployment_API/            # Đóng gói & Triển khai ứng dụng thực tế
│   ├── server.py                       # FastAPI Production Server (Tự động tải model, scaler, threshold)
│   ├── client.py                       # CLI Test Client & Giao diện người dùng Streamlit
│   └── inference.py                    # Script suy luận trực tiếp không cần mạng
├── Roadmaps/                           # Lộ trình học tập cá nhân hóa do DeepTutor sinh ra
├── Quizzes/                            # 5 bộ đề kiểm tra chẩn đoán nhận thức & phân tích bẫy
├── Notes/                              # Sổ tay công thức, Cẩm nang tiền xử lý & Ma trận chọn thuật toán
├── .agents/skills/deeptutor-tutor/     # Kỹ năng sư phạm DeepTutor cho trợ lý Antigravity
├── AGENTS.md / GEMINI.md               # Chỉ thị kích hoạt chế độ gia sư Socratic 5 tầng
└── requirements.txt                    # Danh sách thư viện cần thiết toàn diện
```

---

## ⚡ Bắt Đầu Nhanh (Quickstart)

### 1. Chạy Toàn Bộ Test Suites (Unit Tests)
```bash
pytest 01_Math_Foundations/Ex1_Python_Math_Algorithms/test_all.py
```

### 2. Khởi Chạy Giao Diện Web Lab Trực Quan (Interactive Hub)
```bash
cd 01_Math_Foundations/Ex1_Python_Math_Algorithms
python3 launch_hub.py
# Trình duyệt sẽ tự động mở giao diện mô phỏng thuật toán SVG, ReLU, Decision Trees, BFS!
```

### 3. Huấn Luyện Mạng Nơ-Ron Nhận Dạng Chữ Số MNIST (PyTorch)
```bash
python3 05_Deep_Learning_Basics/pytorch_mnist_demo.py
```

### 4. Khởi Chạy FastAPI Server Phục Vụ Dự Đoán
```bash
cd 07_Model_Deployment_API
python3 server.py
```
- Mở tài liệu API tương tác: [http://localhost:8000/docs](http://localhost:8000/docs)
- Chạy thử client:
```bash
python3 client.py --cli
```

---

## 🤖 Kết Nối DeepTutor AI Mentor Trong Thư Mục Này

Không gian làm việc này được tích hợp sâu với **DeepTutor AI Mentor**:
- **Chế độ Socratic 5 tầng**: Antigravity sẽ đóng vai trò người thầy dẫn dắt, không spoil code giải hộ mà đặt câu hỏi gợi mở trực giác toán học.
- **Tự động lưu trữ**: Mọi ghi chú học tập, lộ trình cá nhân hóa và bài thi trắc nghiệm được lưu trữ ngăn nắp vào các thư mục `Roadmaps/`, `Quizzes/`, `Notes/`.
