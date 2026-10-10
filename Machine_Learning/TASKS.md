---
document_type: project_task_board
project: Machine Learning
version: 2.0.0
last_updated: 2026-09-23
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
focus_board: file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md
central_tasks: file:///D:/02_Learning_Knowledge/TASKS.md
rfc2119_compliance: strict
emoji_policy: none
---

# Machine Learning - Task Board

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
Active Focus Board: [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md)
System Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md)
Project Overview: [README.md](file:///D:/02_Learning_Knowledge/Machine_Learning/README.md)
Agent Directives: [GEMINI.md](file:///D:/02_Learning_Knowledge/Machine_Learning/GEMINI.md) | [AGENTS.md](file:///D:/02_Learning_Knowledge/Machine_Learning/AGENTS.md)

## Task Maintenance Rules (RFC 2119)
- Standardized Schema: All tasks MUST follow the tag format `- [ ] [Deadline: YYYY-MM-DD HH:mm] [Priority: P0/P1/P2] Description`.
- Task Preservation: AI agents MUST NEVER delete existing tasks.
- Status Transitions: Task status MUST ONLY be transitioned between `[ ]` and `[x]`, and status change to completed MUST occur ONLY IF verification criteria are met.
- Task Placement: Newly identified micro-tasks MUST be appended to the end of the appropriate section.
- Local Authority: Local operations within this project directory MUST update this file directly.

## 1. Supervised Learning Algorithms
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Thiết lập bài toán Linear Regression và Gradient Descent trên tập [StudentScore.xls](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning/01_Regression/StudentScore.xls).
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Triển khai Logistic Regression cho phân loại nhị phân trên tập [diabetes.csv](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning/02_Classification/diabetes.csv).
- [ ] [Deadline: 2026-09-26 23:59] [Priority: P1] Cài đặt thuật toán Ridge và Lasso Regularization, phân tích hiện tượng Co-efficient Shrinkage trong [01_Regression](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning/01_Regression).
- [ ] [Deadline: 2026-09-27 23:59] [Priority: P1] Cài đặt Decision Tree Classifier và phân tích tiêu chí Information Gain / Gini Impurity trên tập dữ liệu [car.csv](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning/02_Classification/car.csv).
- [ ] [Deadline: 2026-09-28 23:59] [Priority: P1] Triển khai thuật toán K-Nearest Neighbors (KNN) từ scratch và so sánh với Scikit-learn.
- [ ] [Deadline: 2026-09-29 23:59] [Priority: P2] Xây dựng mô hình Random Forest và Gradient Boosting (XGBoost/LightGBM) cho bài toán tabular classification.
- [ ] [Deadline: 2026-09-30 23:59] [Priority: P2] Phát triển mô hình dự báo chuỗi thời gian cơ bản trong [03_Time_Series_Forecasting](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning/03_Time_Series_Forecasting).
- [ ] [Deadline: 2026-10-02 23:59] [Priority: P2] Hoàn thiện End-to-End Pipeline hoàn chỉnh trong [04_End_to_End_Diabetes_Pipeline](file:///D:/02_Learning_Knowledge/Machine_Learning/02_Supervised_Learning/04_End_to_End_Diabetes_Pipeline).

## 2. Model Evaluation & Hyperparameter Tuning
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Triển khai bộ tính toán metric: Confusion Matrix, Accuracy, Precision, Recall, F1-Score, ROC-AUC trong [model_evaluation_metrics.py](file:///D:/02_Learning_Knowledge/Machine_Learning/04_Model_Evaluation_Tuning/model_evaluation_metrics.py).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Xây dựng và thực thi test suite tự động [test_evaluation_tuning.py](file:///D:/02_Learning_Knowledge/Machine_Learning/04_Model_Evaluation_Tuning/test_evaluation_tuning.py).
- [ ] [Deadline: 2026-09-28 23:59] [Priority: P1] Thực thi Hyperparameter Tuning với K-Fold Cross-Validation, GridSearchCV và RandomizedSearchCV trong [hyperparameter_tuning_suite.py](file:///D:/02_Learning_Knowledge/Machine_Learning/04_Model_Evaluation_Tuning/hyperparameter_tuning_suite.py).
- [ ] [Deadline: 2026-09-29 23:59] [Priority: P2] Phân tích và xử lý Imbalanced Data: SMOTE, Class Weighting và Precision-Recall Curve tuning.
- [ ] [Deadline: 2026-09-30 23:59] [Priority: P2] Phân tích Outlier detection và threshold tuning trên tập dữ liệu [diabetes_cleaned.csv](file:///D:/02_Learning_Knowledge/Machine_Learning/04_Model_Evaluation_Tuning/diabetes_cleaned.csv).
- [ ] [Deadline: 2026-10-01 23:59] [Priority: P2] Xây dựng bảng đối chuẩn hiệu năng đa mô hình trong [model_benchmark_comparison.py](file:///D:/02_Learning_Knowledge/Machine_Learning/04_Model_Evaluation_Tuning/model_benchmark_comparison.py).
- [x] [Deadline: 2026-09-26 23:59] [Priority: P1] Xây dựng tài liệu chuyên sâu chẩn đoán Overfitting, phòng tránh lỗi ML thực chiến và liên hệ Regularization trong [05_overfitting_and_ml_pitfalls_guide.md](file:///D:/02_Learning_Knowledge/Machine_Learning/04_Model_Evaluation_Tuning/05_overfitting_and_ml_pitfalls_guide.md).

## 3. Kaggle & Real-world Dataset Experiments
- [ ] [Deadline: 2026-10-03 23:59] [Priority: P2] Thực hiện EDA toàn diện và làm sạch dữ liệu trong [06_Datasets_Kaggle/csgo](file:///D:/02_Learning_Knowledge/Machine_Learning/06_Datasets_Kaggle/csgo).
- [ ] [Deadline: 2026-10-04 23:59] [Priority: P2] Xây dựng pipeline phân loại nguy cơ đột quỵ trên tập dữ liệu [06_Datasets_Kaggle/stroke](file:///D:/02_Learning_Knowledge/Machine_Learning/06_Datasets_Kaggle/stroke).
- [ ] [Deadline: 2026-10-05 23:59] [Priority: P2] Xây dựng baseline phân loại chữ số viết tay trên tập dữ liệu [06_Datasets_Kaggle/mnist](file:///D:/02_Learning_Knowledge/Machine_Learning/06_Datasets_Kaggle/mnist).
- [ ] [Deadline: 2026-10-06 23:59] [Priority: P2] Xây dựng mô hình Collaborative Filtering cơ bản trên tập dữ liệu [06_Datasets_Kaggle/movie_lens](file:///D:/02_Learning_Knowledge/Machine_Learning/06_Datasets_Kaggle/movie_lens).
- [ ] [Deadline: 2026-10-07 23:59] [Priority: P2] Đóng gói mô hình bằng Joblib/Pickle và kiểm thử suy luận qua REST API trong [07_Model_Deployment_API](file:///D:/02_Learning_Knowledge/Machine_Learning/07_Model_Deployment_API).

## 4. Roadmap v2 Milestones ([ROADMAP.md](file:///D:/02_Learning_Knowledge/Machine_Learning/Roadmaps/ROADMAP.md))
- [ ] [Deadline: 2026-10-18 21:00] [Priority: P1] M1 + M2.1: Tự cài hồi quy tuyến tính (normal equation + gradient descent) trên StudentScore, khớp LinearRegression (sai khác < 1e-3).
- [ ] [Deadline: 2026-10-25 21:00] [Priority: P1] M2.2 + M3.1: Logistic regression từ đầu trên diabetes và chọn ngưỡng theo chi phí (c_FN = 5 c_FP).
- [ ] [Deadline: 2026-11-01 21:00] [Priority: P1] M2.3: Tính tay Gini nút gốc trên car.csv (Auto MPG, nhãn origin) khớp DecisionTreeClassifier; ghi chú 4 tham số LightGBM.
- [ ] [Deadline: 2026-11-08 21:00] [Priority: P1] M3.2: Thí nghiệm leakage với SelectKBest và so DecisionTree, RandomForest, HistGradientBoosting bằng 5-fold stratified CV (mean ± std).
- [ ] [Deadline: 2026-11-15 21:00] [Priority: P1] M3.3a: Ridge/Lasso coefficient path, chọn alpha bằng CV trên StudentScore (thay task Ridge/Lasso hạn 2026-09-26).
- [ ] [Deadline: 2026-11-22 21:00] [Priority: P1] M3.3b: Validation curve của max_depth; so GridSearchCV với RandomizedSearchCV cho RandomForest.
- [ ] [Deadline: 2026-11-29 21:00] [Priority: P1] M4.1: K-Means và PCA (SVD) từ đầu trên diabetes, khớp scikit-learn.
- [ ] [Deadline: 2026-12-06 21:00] [Priority: P1] M5: co2.csv với naive, seasonal naive, lag + Ridge, TimeSeriesSplit 5 fold (bảng MAE mean ± std).
- [ ] [Deadline: 2027-01-10 21:00] [Priority: P1] Capstone A: pipeline phân loại đột quỵ lệch lớp + model card.
- [ ] [Deadline: 2027-03-21 21:00] [Priority: P2] M9: giải lại 7 chặng 09_LLM_From_Scratch từ file trắng, test pass rồi mới tick.
