# GIÁO TRÌNH TOÀN TẬP: AI, DATA SCIENCE & MACHINE LEARNING NÂNG CAO
> **Nguồn tư liệu:** Toàn bộ 18 bài giảng video (Khóa 21 ML/DL/CV Nâng cao - GV. Việt Nguyễn), hệ thống slide bài giảng (Phần 1 & Phần 2), bộ mã nguồn thực hành và các tập dữ liệu dự án trong thư mục `Learning_AI_VietNguyen`.

---

## MỤC LỤC TỔNG QUAN

1. [Tổng quan khóa học & Bản đồ lộ trình kiến thức](#tổng-quan-khóa-học--bản-đồ-lộ-trình-kiến-thức)
2. [Lesson 01: Nhập môn AI, Data Science & Machine Learning](#lesson-01-nhập-môn-ai-data-science--machine-learning)
3. [Lesson 02: Phân loại Dữ liệu & Quy trình Huấn luyện Mô hình](#lesson-02-phân-loại-dữ-liệu--quy-trình-huấn-luyện-mô-hình)
4. [Lesson 03: Hàm mất mát (Loss Function) & Bộ chỉ số đánh giá (Evaluation Metrics)](#lesson-03-hàm-mất-mát-loss-function--bộ-chỉ-số-đánh-giá-evaluation-metrics)
5. [Lesson 04: Tiền xử lý dữ liệu (Data Preprocessing & Feature Engineering)](#lesson-04-tiền-xử-lý-dữ-liệu-data-preprocessing--feature-engineering)
6. [Lesson 05: Phân tích Tương quan & Thuật toán Tuyến tính (Linear & Logistic Regression)](#lesson-05-phân-tích-tương-quan--thuật-toán-tuyến-tính-linear--logistic-regression)
7. [Lesson 06: Thuật toán Cây quyết định (Decision Tree) & Support Vector Machine (SVM)](#lesson-06-thuật-toán-cây-quyết-định-decision-tree--support-vector-machine-svm)
8. [Lesson 07: K-NN, K-Means, Ensemble Learning (Random Forest) & Khám phá dữ liệu (EDA)](#lesson-07-k-nn-k-means-ensemble-learning-random-forest--khám-phá-dữ-liệu-eda)
9. [Lesson 08: Thực hành Xây dựng Pipeline Phân loại hoàn chỉnh (Classification Project)](#lesson-08-thực-hành-xây-dựng-pipeline-phân-loại-hoàn-chỉnh-classification-project)
10. [Lesson 09: Xử lý Mất cân bằng dữ liệu & Pipeline Hồi quy phức hợp (Regression Project)](#lesson-09-xử-lý-mất-cân-bằng-dữ-liệu--pipeline-hồi-quy-phức-hợp-regression-project)
11. [Lesson 10: Tối ưu Pipeline với GridSearchCV & Nhập môn Xử lý Ngôn ngữ Tự nhiên (NLP)](#lesson-10-tối-ưu-pipeline-với-gridsearchcv--nhập-môn-xử-lý-ngôn-ngữ-tự-nhiên-nlp)
12. [Lesson 11: Kỹ thuật Xử lý Văn bản Chuyên sâu (Text Preprocessing & TF-IDF)](#lesson-11-kỹ-thuật-xử-lý-văn-bản-chuyên-sâu-text-preprocessing--tf-idf)
13. [Lesson 12: Dự án Phân loại Tin tuyển dụng (Job Classification & Feature Selection)](#lesson-12-dự-án-phân-loại-tin-tuyển-dụng-job-classification--feature-selection)
14. [Lesson 13: Bản chất Dự báo Chuỗi thời gian (Time Series Forecasting Fundamentals)](#lesson-13-bản-chất-dự-báo-chuỗi-thời-gian-time-series-forecasting-fundamentals)
15. [Lesson 14: Thực hành Dự báo Đa bước (Recursive & Direct Multi-step Forecasting)](#lesson-14-thực-hành-dự-báo-đa-bước-recursive--direct-multi-step-forecasting)
16. [Lesson 15: Giảm chiều Dữ liệu (Curse of Dimensionality, PCA & Feature Selection)](#lesson-15-giảm-chiều-dữ-liệu-curse-of-dimensionality-pca--feature-selection)
17. [Lesson 16: Xây dựng Hệ thống Gợi ý Phim (Content-Based Recommendation System)](#lesson-16-xây-dựng-hệ-thống-gợi-ý-phim-content-based-recommendation-system)
18. [Lesson 17: Triển khai Ứng dụng Thực tế (Deployment với FastAPI, Streamlit & Docker)](#lesson-17-triển-khai-ứng-dụng-thực-tế-deployment-với-fastapi-streamlit--docker)
19. [Lesson 18: Tổng kết Khóa học, Trade-off Bias/Variance & Lộ trình Nâng cao](#lesson-18-tổng-kết-khóa-học-trade-off-biasvariance--lộ-trình-nâng-cao)

---

## TỔNG QUAN KHÓA HỌC & BẢN ĐỒ LỘ TRÌNH KIẾN THỨC

Khóa học trang bị cho học viên tư duy kỹ thuật thực chiến, loại bỏ cách học vẹt lý thuyết bằng cách đi sâu vào 4 trụ cột cốt lõi:
1. **Data Engineering & EDA:** Khám phá bản chất phân phối của dữ liệu, nhận diện ngoại lai (outliers), giá trị thiếu (missing values), tương quan (correlation).
2. **Machine Learning Algorithms & Optimization:** Nắm vững toán học đằng sau các thuật toán từ tuyến tính (Linear/Logistic) đến phi tuyến (Trees, Random Forest, SVM, KNN, Naive Bayes), cơ chế Bagging/Boosting, kỹ thuật đánh giá chéo (Cross Validation), siêu tham số (Hyperparameter Tuning).
3. **Chuyên đề Ứng dụng Nâng cao:** 
   - Xử lý ngôn ngữ tự nhiên (NLP / Text Classification).
   - Dự báo chuỗi thời gian (Time-series Forecasting).
   - Hệ thống gợi ý (Recommendation Systems).
   - Giảm chiều dữ liệu (PCA & Feature Selection).
4. **Production Deployment:** Đóng gói mô hình thành REST API với FastAPI, giao diện trực quan với Streamlit, và container hóa ứng dụng với Docker.

```
+----------------------------------------------------------------------------------------------------+
|                                    BẢN ĐỒ QUY TRÌNH HỌC MÁY (ML PIPELINE)                           |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  [Dữ liệu thô] --> [EDA & Làm sạch] --> [Feature Engineering] --> [Train/Val/Test Split]           |
|                                         (Impute, Scale, Encode)           |                        |
|                                                                            v                        |
|  [Đóng gói App] <-- [Đánh giá Metric] <-- [Tối ưu Siêu tham số] <-- [Huấn luyện Mô hình]           |
|  (FastAPI + UI)      (F1, ROC, R2)         (GridSearchCV)             (RF, SVM, Linear,...)        |
+----------------------------------------------------------------------------------------------------+
```

---

## LESSON 01: NHẬP MÔN AI, DATA SCIENCE & MACHINE LEARNING

### 1. Bối cảnh & Lý do tự huấn luyện mô hình trong kỷ nguyên LLM (ChatGPT, Claude, Gemini)
* **Vì sao vẫn phải tự huấn luyện mô hình truyền thống?**
  1. **Dữ liệu & nghiệp vụ đặc thù:** Doanh nghiệp sở hữu dữ liệu nội bộ bảo mật, bài toán riêng biệt (dự đoán churn rate, rủi ro tín dụng ngân hàng, chuỗi thời gian nồng độ khí thải) mà các LLM tổng quát không thể tiếp cận hoặc không tối ưu.
  2. **Tránh Overkill (Lãng phí tài nguyên):** Gọi API LLM cho các bài toán phân loại nhị phân hàng triệu lượt/giây tiêu tốn chi phí khổng lồ và độ trễ (latency) cao. Các mô hình ML truyền thống (nhẹ, nhanh chỉ vài mili-giây) là lựa chọn tối ưu trong sản xuất.
  3. **Khả năng giải thích (Interpretability):** Trong y tế, tài chính, pháp lý, mô hình bắt buộc phải giải thích được tại sao đưa ra quyết định (feature importance, coefficients), điều mà các mô hình hộp đen khổng lồ rất khó chứng minh.

### 2. Phân biệt các khái niệm cốt lõi
* **Trí tuệ nhân tạo (AI - Artificial Intelligence):** Vùng bao trùm lớn nhất, là bất kỳ hệ thống máy tính nào có khả năng mô phỏng hành vi thông minh của con người (bao gồm cả hệ chuyên gia dựa trên luật if-else).
* **Học máy (Machine Learning - ML):** Tập con của AI, nơi hệ thống tự "học" các quy luật từ dữ liệu trong quá khứ thông qua các thuật toán thống kê/tối ưu hóa mà không cần phải lập trình cứng các luật (hard-coded rules).
* **Khoa học dữ liệu (Data Science - DS):** Ngành khoa học liên ngành sử dụng toán, thống kê, phân tích dữ liệu và thuật toán máy học để rút trích tri thức kinh doanh hữu ích từ dữ liệu có cấu trúc và phi cấu trúc.

### 3. Phân loại dữ liệu & Bài toán Học có giám sát vs Không giám sát
* **Dữ liệu có nhãn (Labeled Data):** Mỗi mẫu dữ liệu đầu vào $\mathbf{x}$ đi kèm với một nhãn kết quả thực tế $y$ (Ground Truth).
* **Dữ liệu không nhãn (Unlabeled Data):** Dữ liệu chỉ có tập đặc trưng $\mathbf{x}$ mà không có nhãn chỉ dẫn $y$.
* **Học có giám sát (Supervised Learning):**
  - **Hồi quy (Regression):** Đầu ra $y$ là một giá trị liên tục (Continuous variable), ví dụ: dự đoán giá nhà, điểm thi học sinh, nồng độ CO2.
  - **Phân loại (Classification):** Đầu ra $y$ là một nhãn danh mục (Discrete class), ví dụ: phân loại email Spam/Không Spam (nhị phân), chẩn đoán 4 nhóm bệnh lý (đa lớp).
* **Học không giám sát (Unsupervised Learning):** Tìm cấu trúc ẩn, nhóm cụm (Clustering như K-Means) hoặc giảm chiều dữ liệu (PCA) từ dữ liệu không nhãn.

---

## LESSON 02: PHÂN LOẠI DỮ LIỆU & QUY TRÌNH HUẤN LUYỆN MÔ HÌNH

### 1. Phân loại đặc trưng (Feature Types)
* **Đặc trưng số (Numerical Features):**
  - *Liên tục (Continuous):* Đo lường được dưới dạng số thực vô hạn khoảng (chiều cao, cân nặng, diện tích nhà, thời gian).
  - *Rời rạc (Discrete):* Các giá trị số đếm nguyên (số phòng ngủ, số lượt click, số lần nhập viện).
* **Đặc trưng danh mục (Categorical Features):**
  - *Định danh (Nominal):* Không có thứ tự hơn kém (giới tính: Nam/Nữ, thành phố: HN/HCM/ĐN, màu sắc: Đỏ/Xanh).
  - *Thứ bậc (Ordinal):* Có thứ tự cấp bậc rõ ràng nhưng khoảng cách giữa các bậc không đo lường chính xác bằng số học (trình độ học vấn: Cấp 3 < Đại học < Thạc sĩ < Tiến sĩ; mức độ hài lòng: Kém < Bình thường < Tốt).

### 2. Kiến trúc chia tập dữ liệu (Train / Validation / Test Split)
* **Tập huấn luyện (Training Set):** Chiếm ~70-80%, dùng để mô hình học các trọng số/quy luật ($w, b$).
* **Tập kiểm tra (Testing Set):** Chiếm ~20%, đóng vai trò như bài thi cuối kỳ độc lập, mô hình chưa từng được thấy trong quá trình học.
* **Nguyên tắc vàng chống Data Leakage (Rò rỉ dữ liệu):**
  - **CẤM** chuẩn hóa dữ liệu hoặc điền giá trị thiếu trên toàn bộ tập dữ liệu trước khi chia Train/Test.
  - Mọi thao tác `fit()` (tính mean, std, median, bộ từ vựng TF-IDF) chỉ được thực hiện trên tập `Train`. Sau đó dùng nguyên các tham số đó để `transform()` trên tập `Test`.

### 3. Phân biệt Loss Function vs Evaluation Metric
* **Hàm mất mát (Loss / Objective Function):** Công thức toán học có tính khả vi (differentiable), dùng trực tiếp trong quá trình tối ưu hóa thuật toán (Gradient Descent) để phạt sai số và cập nhật trọng số (ví dụ: MSE, Binary Cross-Entropy).
* **Chỉ số đánh giá (Evaluation Metric):** Thước đo nghiệp vụ được con người dùng để đánh giá chất lượng mô hình sau khi dự đoán (ví dụ: Accuracy, F1-Score, ROC-AUC, MAE, R2). Metric không nhất thiết phải khả vi.

---

## LESSON 03: HÀM MẤT MÁT (LOSS FUNCTION) & BỘ CHỈ SỐ ĐÁNH GIÁ (EVALUATION METRICS)

### 1. Bộ chỉ số cho bài toán Hồi quy (Regression)
Cho $y_i$ là giá trị thực tế, $\hat{y}_i$ là giá trị dự đoán, $N$ là số mẫu:
* **Sai số tuyệt đối trung bình (MAE - Mean Absolute Error):**
  $$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$$
  - *Ý nghĩa:* Dễ diễn giải cùng đơn vị đo lường, không quá nhạy cảm với ngoại lai.
* **Sai số toàn phương trung bình (MSE - Mean Squared Error):**
  $$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$
  - *Ý nghĩa:* Phạt rất nặng các sai số lớn do bình phương. Nhạy cảm với outliers.
* **Căn bậc hai của MSE (RMSE):** $\text{RMSE} = \sqrt{\text{MSE}}$, đưa đơn vị sai số về cùng đơn vị với biến mục tiêu.
* **Hệ số xác định ($R^2$ Score / Coefficient of Determination):**
  $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$
  - $R^2 = 1$: Dự đoán hoàn hảo.
  - $R^2 = 0$: Mô hình chỉ dự đoán bằng giá trị trung bình $\bar{y}$.
  - $R^2 < 0$: Mô hình tệ hơn cả việc đoán bừa bằng trung bình cộng.

### 2. Bộ chỉ số cho bài toán Phân loại (Classification)
Xây dựng dựa trên **Ma trận nhầm lẫn (Confusion Matrix)**:

| | Dự đoán Dương (Predicted Positive) | Dự đoán Âm (Predicted Negative) |
| :--- | :---: | :---: |
| **Thực tế Dương (Actual Positive)** | **TP** (True Positive) | **FN** (False Negative) |
| **Thực tế Âm (Actual Negative)** | **FP** (False Positive) | **TN** (True Negative) |

* **Độ chính xác toàn cục (Accuracy):**
  $$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$$
  > **CẢNH BÁO QUAN TRỌNG:** Accuracy hoàn toàn vô nghĩa khi dữ liệu bị mất cân bằng (Imbalanced Data). Ví dụ: tập dữ liệu có 98 người khỏe mạnh và 2 người nhiễm bệnh hiểm nghèo. Một mô hình "ngu ngốc" luôn dự đoán "Khỏe mạnh" sẽ đạt Accuracy = 98%, nhưng bỏ sót 100% bệnh nhân!

* **Độ chính xác trên dự đoán dương (Precision):**
  $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
  - *Ý nghĩa:* Trong số các ca mô hình gắn cờ "Dương tính", có bao nhiêu ca thực sự đúng? (Ưu tiên khi chi phí cho FP rất cao, ví dụ: bộ lọc Spam email không được lọc nhầm email công việc quan trọng).
* **Độ nhạy / Thu hồi (Recall / Sensitivity):**
  $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
  - *Ý nghĩa:* Trong tổng số ca thực sự "Dương tính", mô hình tìm được bao nhiêu ca? (Ưu tiên tuyệt đối trong y tế, chẩn đoán ung thư, phát hiện gian lận ngân hàng: thà bắt nhầm còn hơn bỏ sót!).
* **Điểm F1 (F1-Score):** Trung bình điều hòa giữa Precision và Recall:
  $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$
* **Đường cong ROC và chỉ số AUC (Area Under Curve):**
  - Đồ thị biểu diễn tương quan giữa **TPR** (True Positive Rate = Recall) và **FPR** (False Positive Rate = $\frac{\text{FP}}{\text{FP} + \text{TN}}$) trên tất cả các ngưỡng quyết định (thresholds từ 0 đến 1).
  - $\text{AUC} = 1.0$: Bộ phân loại hoàn hảo.
  - $\text{AUC} = 0.5$: Tương đương tung đồng xu ngẫu nhiên.

---

## LESSON 04: TIỀN XỬ LÝ DỮ LIỆU (DATA PREPROCESSING & FEATURE ENGINEERING)

### 1. Xử lý giá trị bị khuyết (Missing Values Imputation)
* **Phát hiện:** `data.isnull().sum()` hoặc trực quan hóa bằng `missingno`.
* **Phương pháp điền khuyết:**
  - *Số học (Numerical):* Điền bằng Mean (nếu phân phối chuẩn không có ngoại lai) hoặc Median (nếu dữ liệu bị lệch/có ngoại lai).
  - *Danh mục (Categorical):* Điền bằng Mode (giá trị có tần suất cao nhất) hoặc tạo một danh mục mới `"Unknown"`.
  - *Nâng cao:* Sử dụng `KNNImputer` (điền dựa trên $k$ mẫu lân cận có đặc trưng tương đồng) hoặc `IterativeImputer`.

### 2. Phát hiện & Xử lý Điểm ngoại lai (Outliers)
* **Phương pháp Khoảng tứ phân vị (IQR - Interquartile Range):**
  - $\text{IQR} = Q_3 - Q_1$
  - Ngưỡng dưới: $\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}$
  - Ngưỡng trên: $\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$
  - Mọi điểm nằm ngoài khoảng $[\text{Lower Bound}, \text{Upper Bound}]$ bị coi là ngoại lai.
* **Phương pháp Z-Score:** Điểm ngoại lai là điểm có $|z| > 3$ ($z = \frac{x - \mu}{\sigma}$).
* **Cách xử lý:** Cắt tỉa (Trimming), giới hạn trần/sàn (Winsorization/Capping), hoặc biến đổi logarit ($\log(1+x)$) để thu hẹp độ lệch của phân phối.

### 3. Chuẩn hóa tỷ lệ đặc trưng (Feature Scaling)
* **MinMaxScaler (Đưa về đoạn $[0, 1]$):**
  $$x_{\text{scaled}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
* **StandardScaler (Chuẩn hóa Z-score về trung bình 0, độ lệch chuẩn 1):**
  $$x_{\text{std}} = \frac{x - \mu}{\sigma}$$
* **Khi nào BẮT BUỘC phải scale?**
  - Các thuật toán tính khoảng cách hình học: KNN, SVM, K-Means.
  - Các thuật toán tối ưu hóa bằng Gradient Descent: Linear Regression, Logistic Regression, Neural Networks.
  - **Lưu ý:** Các thuật toán dựa trên cây (Decision Tree, Random Forest, XGBoost) hoàn toàn **KHÔNG** bị ảnh hưởng bởi tỷ lệ scale đặc trưng!

### 4. Mã hóa biến danh mục (Categorical Encoding)
* **One-Hot Encoding:** Chuyển mỗi giá trị danh mục thành một cột nhị phân (0/1). Dành cho biến Nominal (không có thứ bậc).
  - *Bẫy Đa cộng tuyến (Dummy Variable Trap):* Nếu một biến có $K$ giá trị, chỉ giữ lại $K-1$ cột nhị phân (hoặc dùng `drop='first'`) khi huấn luyện các mô hình tuyến tính.
* **Ordinal Encoding:** Gán nhãn số nguyên theo đúng thứ tự logic định sẵn (`categories=[['Thấp', 'Trung bình', 'Cao']]`). Dành riêng cho biến Ordinal.

---

## LESSON 05: PHÂN TÍCH TƯƠNG QUAN & THUẬT TOÁN TUYẾN TÍNH (LINEAR & LOGISTIC REGRESSION)

### 1. Phân tích tương quan & Hiện tượng Đa cộng tuyến (Multicollinearity)
* **Hệ số tương quan Pearson ($r$):** Đo mức độ quan hệ tuyến tính giữa 2 biến, nhận giá trị trong $[-1, 1]$.
* **Đa cộng tuyến:** Hiện tượng 2 hoặc nhiều đặc trưng đầu vào phụ thuộc tuyến tính mạnh mẽ vào nhau ($|r| > 0.85$ hoặc $\text{VIF} > 5$).
  - *Hậu quả:* Khiến ma trận nghịch đảo không ổn định, phương sai của trọng số $\mathbf{w}$ tăng vọt, mô hình không thể giải thích chính xác vai trò của từng đặc trưng độc lập.

### 2. Thuật toán Hồi quy Tuyến tính (Linear Regression)
* **Phương trình dự đoán:** $\hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b = \mathbf{w}^T \mathbf{x} + b$
* **Hàm mất mát OLS (Ordinary Least Squares):**
  $$J(\mathbf{w}, b) = \frac{1}{2N} \sum_{i=1}^{N} (y_i - (\mathbf{w}^T \mathbf{x}_i + b))^2$$
* **Thuật toán Gradient Descent cập nhật trọng số:**
  $$w_j \leftarrow w_j - \alpha \frac{\partial J}{\partial w_j} = w_j - \frac{\alpha}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i) x_{ij}$$
* **Hạn chế lớn:** Cực kỳ nhạy cảm với ngoại lai (Outliers) vì sai số bị bình phương, kéo lệch đường hồi quy về phía điểm dị biệt.

### 3. Thuật toán Hồi quy Logistic (Logistic Regression)
* **Ý tưởng:** Dành cho bài toán phân loại nhị phân. Đưa giá trị tuyến tính $z = \mathbf{w}^T \mathbf{x} + b$ qua **Hàm Sigmoid** để ép giá trị đầu ra về khoảng xác suất $[0, 1]$:
  $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
* **Hàm mất mát Binary Cross-Entropy (Log-Loss):**
  $$J(\mathbf{w}) = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$
* **Ngưỡng quyết định (Decision Threshold):** Thông thường lấy $0.5$ (nếu $\hat{y} \ge 0.5 \Rightarrow 1$, ngược lại $0$). Trong bài toán y tế/gian lận, ta chủ động hạ threshold xuống $0.2$ hoặc $0.3$ để tăng Recall.

---

## LESSON 06: THUẬT TOÁN CÂY QUYẾT ĐỊNH (DECISION TREE) & SUPPORT VECTOR MACHINE (SVM)

### 1. Thuật toán Naive Bayes Classifier
* **Định lý Bayes:** $P(y|\mathbf{x}) = \frac{P(\mathbf{x}|y) P(y)}{P(\mathbf{x})}$
* **Giả định "Ngây thơ" (Naive):** Toàn bộ các đặc trưng $x_1, x_2, \dots, x_n$ hoàn toàn độc lập với nhau khi biết nhãn $y$:
  $$P(\mathbf{x}|y) = \prod_{i=1}^{n} P(x_i|y)$$
* **Multinomial Naive Bayes:** Rất hiệu quả cho phân loại văn bản (dựa trên tần suất đếm từ trong túi từ BoW).

### 2. Cây quyết định (Decision Tree)
* **Cơ chế hoạt động:** Phân chia không gian dữ liệu bằng các phép so sánh nhị phân liên tiếp theo hình cây phân cấp.
* **Tiêu chí chọn đặc trưng phân nhánh (Splitting Criteria):**
  - **Chỉ số Gini Impurity (Dùng trong CART):**
    $$\text{Gini} = 1 - \sum_{i=1}^{C} p_i^2$$
    (Đo độ tinh khiết của tập dữ liệu tại một nút; $\text{Gini} = 0$ khi tất cả các mẫu thuộc về duy nhất 1 lớp).
  - **Entropy & Độ lợi thông tin (Information Gain - dùng trong ID3, C4.5):**
    $$\text{Entropy}(S) = -\sum_{i=1}^{C} p_i \log_2(p_i)$$
    $$\text{Information Gain} = \text{Entropy}(S) - \sum \frac{|S_v|}{|S|} \text{Entropy}(S_v)$$
* **Nhược điểm lớn nhất:** Rất dễ bị **Overfitting** nếu để cây phát triển quá sâu (`max_depth=None`). Cần tỉa cành (pruning) bằng `max_depth`, `min_samples_split`, `min_samples_leaf`.

### 3. Máy học Vector hỗ trợ (Support Vector Machine - SVM)
* **Mục tiêu:** Tìm một siêu phẳng (Hyperplane) phân tách các lớp dữ liệu sao cho **Khoảng cách lề (Margin)** giữa 2 lớp là lớn nhất có thể.
* **Support Vectors:** Các điểm dữ liệu nằm sát siêu phẳng quyết định nhất. Chỉ các điểm này mới quyết định vị trí của siêu phẳng!
* **Kernel Trick (Bí thuật Kernel):** Khi dữ liệu không thể phân tách tuyến tính ở không gian chiều hiện tại, SVM chiếu dữ liệu lên không gian chiều cao hơn thông qua các hàm nhân mà không cần tính toán tọa độ tường minh:
  - *Linear Kernel:* Phân tách tuyến tính đơn giản.
  - *RBF (Radial Basis Function) Kernel:* Chiếu lên không gian vô hạn chiều, xử lý biên quyết định phi tuyến phức tạp.

---

## LESSON 07: K-NN, K-MEANS, ENSEMBLE LEARNING (RANDOM FOREST) & KHÁM PHÁ DỮ LIỆU (EDA)

### 1. K-Nearest Neighbors (K-NN) & K-Means Clustering
* **K-NN (Phân loại có giám sát):**
  - "Gần mực thì đen, gần đèn thì rạng". Dự đoán nhãn cho mẫu mới bằng cách bầu chọn đa số từ $K$ mẫu lân cận có khoảng cách Euclidean gần nhất:
    $$d(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}$$
  - $K$ nhỏ $\Rightarrow$ Dễ bị nhiễu (Overfitting); $K$ quá lớn $\Rightarrow$ Biên quyết định mờ nhạt (Underfitting).
* **K-Means (Phân cụm không giám sát):**
  - Khởi tạo ngẫu nhiên $K$ tâm cụm (centroids).
  - Lặp lại 2 bước: Gán mỗi điểm vào tâm cụm gần nhất $\rightarrow$ Cập nhật tọa độ tâm cụm bằng trung bình cộng các điểm trong cụm đó.

### 2. Kỹ thuật Học kết hợp (Ensemble Learning) & Rừng ngẫu nhiên (Random Forest)
* **Ý tưởng cốt lõi:** Kết hợp sức mạnh của nhiều mô hình yếu (Weak Learners) để tạo thành một mô hình mạnh (Strong Learner).
* **Bagging (Bootstrap Aggregating):**
  - Lấy mẫu ngẫu nhiên có hoàn lại (Bootstrap Sampling) từ tập train gốc để tạo ra $B$ tập con huấn luyện.
  - Huấn luyện độc lập $B$ mô hình cây trên các tập con này.
  - Dự đoán bằng cách lấy biểu quyết đa số (Majority Voting cho Classification) hoặc trung bình cộng (Averaging cho Regression).
* **Random Forest = Bagging + Random Feature Subsampling:**
  - Tại mỗi nút rẽ nhánh, cây không xét toàn bộ các đặc trưng mà chỉ chọn ngẫu nhiên một tập con đặc trưng (thường là $\sqrt{n}$ với phân loại).
  - Kỹ thuật này giúp các cây trong rừng **không bị tương quan hóa (uncorrelated trees)**, giảm triệt để phương sai (Variance) và ngăn chặn Overfitting hoàn hảo.

### 3. Thực hành EDA với `ydata-profiling`
- Trong bài giảng, giảng viên hướng dẫn tạo báo cáo phân tích tự động `ProfileReport` xuất ra HTML để kiểm tra nhanh phân phối biến, giá trị khuyết và ma trận tương quan chỉ bằng 2 dòng code.

---

## LESSON 08: THỰC HÀNH XÂY DỰNG PIPELINE PHÂN LOẠI HOÀN CHỈNH (CLASSIFICATION PROJECT)

Mã nguồn triển khai chuẩn mực trong bài giảng (`Learning_AI_VietNguyen/Scripts/classification.py`):

```python
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from lazypredict.Supervised import LazyClassifier

# 1. Đọc dữ liệu
data = pd.read_csv("diabetes.csv")
target = "Outcome"
X = data.drop(target, axis=1)
y = data[target]

# 2. Chia tập huấn luyện / kiểm tra (80/20) với random_state cố định
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1009, stratify=y
)

# 3. Chuẩn hóa đặc trưng (Scale)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Đánh giá nhanh hàng loạt mô hình với LazyClassifier
# clf = LazyClassifier(verbose=0, ignore_warnings=True)
# models, predictions = clf.fit(X_train_scaled, X_test_scaled, y_train, y_test)

# 5. Tối ưu siêu tham số với GridSearchCV
params = {
    "n_estimators": [100, 500, 1000],
    "criterion": ["gini", "entropy", "log_loss"],
    "max_depth": [None, 5, 10]
}

grid_model = GridSearchCV(
    RandomForestClassifier(random_state=100),
    param_grid=params,
    cv=6,
    scoring="f1",
    verbose=1,
    n_jobs=-1
)
grid_model.fit(X_train_scaled, y_train)

print(f"Best F1 Score: {grid_model.best_score_:.4f}")
print(f"Best Params: {grid_model.best_params_}")

# 6. Đánh giá trên tập kiểm tra
y_pred = grid_model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

# 7. Lưu trữ mô hình và scaler để phục vụ triển khai
with open("model.pkl", "wb") as f:
    pickle.dump([grid_model.best_estimator_, scaler], f)
```

---

## LESSON 09: XỬ LÝ MẤT CÂN BẰNG DỮ LIỆU & PIPELINE HỒI QUY PHỨC HỢP (REGRESSION PROJECT)

### 1. Kỹ thuật xử lý mất cân bằng lớp (Imbalance Data Handling)
* **Undersampling:** Bỏ bớt mẫu ở lớp đa số $\rightarrow$ Nguy cơ mất thông tin quan trọng.
* **Oversampling ngẫu nhiên (RandomOverSampler):** Nhân bản mẫu ở lớp thiểu số $\rightarrow$ Dễ Overfitting.
* **SMOTE (Synthetic Minority Over-sampling Technique):**
  - Sinh mẫu tổng hợp mới nằm trên đoạn thẳng nối giữa một mẫu thiểu số và các láng giềng gần nhất của nó.
  - Đối với dữ liệu danh mục/văn bản: Sử dụng biến thể **`SMOTEN`**.

### 2. Xây dựng Pipeline xử lý dữ liệu phức hợp với `ColumnTransformer`
Mã nguồn triển khai trong bài toán dự đoán điểm học sinh (`StudentScore.xls`):

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("StudentScore.xls")
target = "math score"
X = data.drop(target, axis=1)
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1009)

# 1. Pipeline cho đặc trưng số học: Điền khuyết bằng median + Scale chuẩn hóa
num_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# 2. Pipeline cho đặc trưng định danh (Nominal): Điền mode + One-Hot Encoding
nom_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(sparse_output=False, handle_unknown="ignore"))
])

# 3. Pipeline cho đặc trưng thứ bậc (Ordinal): Mã hóa theo thứ tự logic
education_levels = [
    "some high school", "high school", "some college", 
    "associate's degree", "bachelor's degree", "master's degree"
]
ord_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[education_levels]))
])

# Gom toàn bộ vào ColumnTransformer
preprocessor = ColumnTransformer(transformers=[
    ("num_features", num_pipeline, ["reading score", "writing score"]),
    ("nom_features", nom_pipeline, ["race/ethnicity", "gender", "lunch"]),
    ("ord_features", ord_pipeline, ["parental level of education"])
])

# Pipeline hoàn chỉnh từ dữ liệu thô đến dự đoán mô hình
full_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=1009))
])

full_pipeline.fit(X_train, y_train)
print(f"R2 Test Score: {full_pipeline.score(X_test, y_test):.4f}")
```

---

## LESSON 10: TỐI ƯU PIPELINE VỚI GRIDSEARCHCV & NHẬP MÔN XỬ LÝ NGÔN NGỮ TỰ NHIÊN (NLP)

### 1. Tối ưu Siêu tham số toàn diện cho cả Pipeline
Trong Scikit-learn, ta có thể điều chỉnh siêu tham số của cả bước Tiền xử lý lẫn bước Mô hình cùng lúc trong một lưới tìm kiếm:
```python
params = {
    "preprocessor__num_features__imputer__strategy": ["mean", "median"],
    "regressor__n_estimators": [50, 100, 200],
    "regressor__criterion": ["squared_error", "absolute_error"]
}
grid_search = GridSearchCV(full_pipeline, param_grid=params, cv=5, scoring="r2", n_jobs=-1)
```

### 2. Bước chuyển sang NLP & Mô hình Túi từ (Bag of Words - BoW)
* Văn bản là dữ liệu phi cấu trúc mà máy tính không thể hiểu trực tiếp dưới dạng số học.
* **Ý tưởng Bag of Words:** Bỏ qua cấu trúc ngữ pháp và thứ tự từ, chỉ coi văn bản như một "túi" chứa các từ.
* **CountVectorizer:**
  1. Thu thập toàn bộ các từ duy nhất trong tất cả các tài liệu để tạo thành bộ từ vựng (Vocabulary).
  2. Biểu diễn mỗi văn bản thành một vector có độ dài bằng kích thước Vocabulary, với giá trị tại mỗi phần tử là số lần từ đó xuất hiện trong văn bản.

---

## LESSON 11: KỸ THUẬT XỬ LÝ VĂN BẢN CHUYÊN SÂU (TEXT PREPROCESSING & TF-IDF)

### 1. Quy trình Tiền xử lý văn bản chuẩn mực
1. **Chuyển về chữ thường (Lowercasing):** Giúp "Học", "học", "HỌC" được coi là cùng một từ vựng.
2. **Loại bỏ ký tự đặc biệt & Dấu câu (Remove Punctuations):** Loại bỏ `.,!?:;"'()[]{}...`
3. **Phân tách từ (Tokenization):** Tách đoạn văn bản thành các đơn vị từ độc lập.
4. **Loại bỏ từ dừng (Stopwords Removal):** Các từ xuất hiện quá nhiều nhưng mang ít thông tin ngữ nghĩa (tiếng Anh: `is`, `the`, `a`, `and`, `you`; tiếng Việt: `thì`, `là`, `mà`, `ở`).
5. **Đưa từ về dạng gốc (Stemming vs Lemmatization):**
   - *Stemming (Rút gọn gốc từ):* Cắt xén đuôi từ theo quy tắc thô sơ (ví dụ Porter Stemmer: `running`, `runs` $\rightarrow$ `run`; nhưng `studies` $\rightarrow$ `studi`).
   - *Lemmatization (Phân tích từ vựng):* Sử dụng từ điển hình thái học để đưa từ về dạng nguyên thể có nghĩa thực tế (`studies` $\rightarrow$ `study`, `better` $\rightarrow$ `good`).

### 2. Trọng số TF-IDF (Term Frequency - Inverse Document Frequency)
BoW gặp nhược điểm: từ nào xuất hiện nhiều sẽ nhận điểm cao, bất kể nó có đóng góp vào việc phân loại tài liệu hay không. **TF-IDF** giải quyết triệt để vấn đề này:
* **Tần suất từ (Term Frequency - $TF$):** Tần suất từ $t$ xuất hiện trong văn bản $d$:
  $$TF(t, d) = \frac{\text{Số lần từ } t \text{ xuất hiện trong } d}{\text{Tổng số từ trong } d}$$
* **Nghịch đảo tần suất tài liệu (Inverse Document Frequency - $IDF$):** Phạt nặng các từ xuất hiện phổ biến ở hầu hết mọi tài liệu:
  $$IDF(t, D) = \log\left(\frac{\text{Tổng số tài liệu } |D|}{1 + \text{Số tài liệu chứa từ } t}\right)$$
* **Chỉ số TF-IDF:**
  $$\text{TF-IDF}(t, d) = TF(t, d) \times IDF(t, D)$$
  - Từ có điểm TF-IDF cao là từ xuất hiện nhiều trong văn bản hiện tại nhưng hiếm khi xuất hiện trong các văn bản khác (từ mang tính đặc trưng cốt lõi).

### 3. Kỹ thuật N-grams
* Ghép $N$ từ đi liền nhau thành một cụm để bảo tồn ngữ cảnh:
  - *Unigram (N=1):* `"not"`, `"good"` (mất ngữ cảnh phủ định).
  - *Bigram (N=2):* `"not good"`, `"very fast"`.

---

## LESSON 12: DỰ ÁN PHÂN LOẠI TIN TUYỂN DỤNG (JOB CLASSIFICATION & FEATURE SELECTION)

Dự án thực hành trên tập dữ liệu tuyển dụng nghề nghiệp thực tế (`final_project.ods`):

### 1. Thách thức lớn của bài toán
- Không gian đặc trưng văn bản sau khi tạo N-grams (1, 2) bùng nổ lên tới **hơn 800,000 chiều**, gây tràn bộ nhớ và mô hình chạy cực kỳ chậm.
- Dữ liệu bị mất cân bằng trầm trọng giữa các chức danh nghề nghiệp (`specialist`, `bereichsleiter` rất ít mẫu so với `senior_specialist`).

### 2. Các kỹ thuật tối ưu hóa đột phá
* **Kiểm soát kích thước từ vựng với `min_df` và `max_df`:**
  ```python
  TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.99, stop_words="english")
  ```
  - `min_df=0.01`: Bỏ qua các từ xuất hiện dưới 1% tổng số văn bản (loại bỏ từ rác, lỗi chính tả).
  - `max_df=0.99`: Bỏ qua các từ xuất hiện trên 99% tổng số văn bản (loại bỏ từ thừa chung chung).
  - Kết quả: Giảm không gian chiều từ 848,501 đặc trưng xuống còn **7,954 đặc trưng**!
* **Chọn lọc đặc trưng bằng kiểm định Chi-Square ($\chi^2$):**
  - Dùng `SelectPercentile(chi2, percentile=8)` để chỉ giữ lại 8% số lượng đặc trưng có tương quan thống kê cao nhất với nhãn công việc cần dự đoán.
* **Cân bằng nhãn với SMOTEN:**
  ```python
  from imblearn.over_sampling import SMOTEN
  sampler = SMOTEN(sampling_strategy={"specialist": 500, "bereichsleiter": 1000}, k_neighbors=2, random_state=0)
  X_train_resampled, y_train_resampled = sampler.fit_resample(X_train, y_train)
  ```

---

## LESSON 13: BẢN CHẤT DỰ BÁO CHUỖI THỜI GIAN (TIME SERIES FORECASTING FUNDAMENTALS)

### 1. Time Series khác gì với Bài toán Hồi quy (Regression)?
* Giảng viên giải thích rõ sự nhầm lẫn phổ biến: **Time Series là bài toán**, còn **Linear Regression là thuật toán**.
* Dữ liệu dạng bảng thông thường có giả định $i.i.d$ (các mẫu độc lập và cùng phân phối). Dữ liệu chuỗi thời gian **vi phạm hoàn toàn** giả định này: giá trị hôm nay ($y_t$) phụ thuộc mật thiết vào giá trị ngày hôm qua ($y_{t-1}$) và các ngày trước đó (Temporal Dependency).
* Không bao giờ được phép dùng `train_test_split(shuffle=True)` vì sẽ gây rò rỉ dữ liệu tương lai về quá khứ (Look-ahead bias). Luôn cắt train/test theo trục thời gian tuyến tính.

### 2. Kỹ thuật Dịch chuyển cửa sổ (Sliding Window / Lag Features)
Để đưa dữ liệu chuỗi thời gian vào các mô hình học máy bảng (như Random Forest, Linear Regression, XGBoost), ta tạo các đặc trưng trễ (Lags):
$$x_{t-1} = y_{t-1}, \quad x_{t-2} = y_{t-2}, \dots, \quad x_{t-k} = y_{t-k}$$
Target cần dự báo: $y_t$.

---

## LESSON 14: THỰC HÀNH DỰ BÁO ĐA BƯỚC (RECURSIVE & DIRECT MULTI-STEP FORECASTING)

Thực hành trên bộ dữ liệu nồng độ khí CO2 (`co2.csv`):

### 1. Tiền xử lý dữ liệu chuỗi thời gian
- Chuyển đổi cột mốc thời gian sang kiểu `pd.to_datetime()`.
- Xử lý các điểm thiếu (missing values) theo thời gian bằng phương pháp nội suy tuyến tính: `data["co2"].interpolate()`.

### 2. Hai chiến lược Dự báo Đa bước (Multi-step Forecasting)
Khi cần dự báo không chỉ ngày mai ($t+1$) mà là 5 bước tiếp theo ($t+1, t+2, \dots, t+5$):

* **Chiến lược 1: Dự báo Đệ quy (Recursive Forecasting):**
  - Chỉ huấn luyện 1 mô hình duy nhất dự đoán $y_{t+1}$ từ $[y_t, y_{t-1}, \dots]$.
  - Lấy giá trị dự đoán $\hat{y}_{t+1}$ làm đầu vào mới để dự đoán tiếp $\hat{y}_{t+2}$, cứ lặp lại như vậy.
  - *Ưu điểm:* Tiết kiệm tài nguyên huấn luyện (chỉ cần 1 mô hình duy nhất).
  - *Nhược điểm:* **Sai số tích lũy (Error Accumulation)**. Nếu dự đoán bước 1 sai, bước 2 sẽ sai nhiều hơn và các bước sau sẽ phân kỳ nghiêm trọng.
* **Chiến lược 2: Dự báo Trực tiếp (Direct Forecasting):**
  - Huấn luyện riêng biệt $K$ mô hình độc lập:
    - Model 1 dự báo $y_{t+1}$ từ $[y_t, y_{t-1}, \dots]$
    - Model 2 dự báo $y_{t+2}$ từ $[y_t, y_{t-1}, \dots]$
    - Model $k$ dự báo $y_{t+k}$ từ $[y_t, y_{t-1}, \dots]$
  - *Ưu điểm:* Không bị tích lũy sai số giữa các bước dự báo.
  - *Nhược điểm:* Tốn tài nguyên vì phải huấn luyện và duy trì $K$ mô hình riêng biệt.

---

## LESSON 15: GIẢM CHIỀU DỮ LIỆU (CURSE OF DIMENSIONALITY, PCA & FEATURE SELECTION)

### 1. Lời nguyền số chiều (Curse of Dimensionality)
Khi số lượng đặc trưng $D$ tăng lên, thể tích không gian đặc trưng tăng theo cấp số nhân khiến các điểm dữ liệu trở nên cực kỳ thưa thớt (sparse). Khoảng cách giữa các điểm gần nhất và xa nhất tiệm cận bằng nhau, làm suy giảm nghiêm trọng độ chính xác của mô hình và khiến mô hình dễ bị Overfitting.

### 2. Chọn lọc đặc trưng (Feature Selection)
- **Variance Threshold:** Loại bỏ các đặc trưng có phương sai gần bằng 0 (hầu như không đổi giá trị trên tất cả các mẫu).
- **Correlation Filtering:** Loại bỏ các đặc trưng có tương quan quá thấp với nhãn Target hoặc tương quan quá cao với các đặc trưng khác.
- **Regularization L1 (Lasso):** Sử dụng hàm phạt chuẩn $L_1$ để ép trọng số của các đặc trưng không quan trọng về đúng bằng 0.
- **Tree-based Feature Importances:** Dùng `feature_importances_` từ Random Forest.

### 3. Trích xuất đặc trưng với Phân tích thành phần chính (PCA)
* **Ý tưởng toán học:** Tìm các hướng chiếu trực giao mới (Principal Components) sao cho phương sai của dữ liệu được bảo toàn lớn nhất.
* **Quy trình tính toán PCA:**
  1. *Bước 1:* Chuẩn hóa dữ liệu về trung bình 0 và độ lệch chuẩn 1.
  2. *Bước 2:* Tính Ma trận Hiệp phương sai (Covariance Matrix $\mathbf{\Sigma}$).
  3. *Bước 3:* Phân tích Eigenvalues ($\lambda$) và Eigenvectors ($\mathbf{v}$) từ $\mathbf{\Sigma}$.
  4. *Bước 4:* Sắp xếp Eigenvalues theo thứ tự giảm dần và chọn ra $k$ eigenvectors tương ứng với $k$ eigenvalues lớn nhất.
  5. *Bước 5:* Nhân ma trận dữ liệu gốc với ma trận chuyển đổi để thu được tập đặc trưng mới có số chiều $k$ nhỏ hơn rất nhiều.

---

## LESSON 16: XÂY DỰNG HỆ THỐNG GỢI Ý PHIM (CONTENT-BASED RECOMMENDATION SYSTEM)

Mã nguồn triển khai hoàn chỉnh trong bài giảng (`Learning_AI_VietNguyen/recommendation_system.py`):

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Đọc dữ liệu phim (movies.csv)
data = pd.read_csv("movie_data/movies.csv", encoding="latin-1", sep="\t", usecols=["title", "genres"])

# 2. Tiền xử lý chuỗi thể loại phim (thay | thành khoảng trắng)
data["genres"] = data["genres"].apply(lambda s: s.replace("|", " ").replace("-", ""))

# 3. Vector hóa chuỗi thể loại bằng TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data["genres"])

# 4. Tính toán Ma trận Tương quan Cosine giữa tất cả các cặp phim
# Cosine Similarity = (A . B) / (||A|| * ||B||)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=data["title"], columns=data["title"])

# 5. Hàm gợi ý Top-K bộ phim tương đồng nhất
def recommend_movies(movie_title, top_k=10):
    if movie_title not in cosine_sim_df:
        return f"Không tìm thấy phim: {movie_title}"
    similar_movies = cosine_sim_df[movie_title].sort_values(ascending=False)
    # Bỏ qua chính bộ phim đó (ở vị trí đầu tiên similarity = 1.0)
    return similar_movies.iloc[1:top_k+1]

print("Top 5 phim tương tự 'Heat (1995)':")
print(recommend_movies("Heat (1995)", top_k=5))
```

---

## LESSON 17: TRIỂN KHAI ỨNG DỤNG THỰC TẾ (DEPLOYMENT VỚI FASTAPI, STREAMLIT & DOCKER)

### 1. Kiến trúc Client - Server trong hệ thống Trí tuệ Nhân tạo
Tách biệt hoàn toàn tầng tính toán Machine Learning (Backend) và tầng giao diện người dùng (Frontend) thông qua giao thức HTTP REST API và định dạng dữ liệu JSON.

```
+--------------------------+                     +---------------------------+
|    Client (Streamlit)    |  --- POST /predict --> |    Backend (FastAPI)      |
|  - Giao diện nhập form   |                     |  - Load model.pkl, scaler |
|  - Hiển thị kết quả đẹp  |  <-- JSON Response --- |  - Tiền xử lý & Dự đoán   |
+--------------------------+                     +---------------------------+
```

### 2. Backend REST API với FastAPI (`Scripts/server.py`)
```python
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

with open("model.pkl", "rb") as f:
    model, scaler = pickle.load(f)

app = FastAPI(title="Diabetes Prediction API")

class DiabetesInput(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    input_list = [[
        data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness,
        data.Insulin, data.BMI, data.DiabetesPedigreeFunction, data.Age
    ]]
    scaled_data = scaler.transform(input_list)
    pred = int(model.predict(scaled_data)[0])
    return {
        "prediction": pred,
        "status": "Có nguy cơ tiểu đường" if pred == 1 else "Không có nguy cơ tiểu đường"
    }
```

### 3. Frontend Web App với Streamlit (`Scripts/client.py`)
```python
import streamlit as st
import requests

st.title("🩺 Ứng dụng Dự đoán Nguy cơ Tiểu đường")
glucose = st.number_input("Chỉ số Glucose", min_value=0.0, value=120.0)
bmi = st.number_input("Chỉ số Khối cơ thể (BMI)", min_value=0.0, value=25.5)
age = st.number_input("Tuổi", min_value=1.0, value=30.0)
# (các trường còn lại...)

if st.button("Dự đoán"):
    payload = {"Pregnancies": 2.0, "Glucose": glucose, "BloodPressure": 70.0, "SkinThickness": 20.0,
               "Insulin": 100.0, "BMI": bmi, "DiabetesPedigreeFunction": 0.5, "Age": age}
    res = requests.post("http://127.0.0.1:8000/predict", json=payload)
    if res.status_code == 200:
        result = res.json()
        if result["prediction"] == 1:
            st.error(f"Cảnh báo: {result['status']}")
        else:
            st.success(f"An toàn: {result['status']}")
```

### 4. Container hóa với Docker
- **Mục đích:** Giải quyết triệt để vấn đề "chạy được trên máy tôi nhưng không chạy được trên máy khách hàng/server".
- **Dockerfile:** Định nghĩa hệ điều hành cơ sở (Base OS Linux), cài đặt Python runtime, copy mã nguồn và cài thư viện `requirements.txt`.
- Đóng gói toàn bộ Backend và Frontend thành các Container độc lập, dễ dàng scale và deploy lên AWS/GCP/Heroku.

---

## LESSON 18: TỔNG KẾT KHÓA HỌC, TRADE-OFF BIAS/VARIANCE & LỘ TRÌNH NÂNG CAO

### 1. Đánh đổi Độ lệch và Phương sai (Bias - Variance Tradeoff)
* **Sai số tổng quát:** $\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$
* **Độ lệch cao (High Bias $\rightarrow$ Underfitting):** Mô hình quá đơn giản (ví dụ dùng đường thẳng Linear Regression cho dữ liệu phi tuyến cong), không học được cấu trúc của dữ liệu cả trên tập train và test.
* **Phương sai cao (High Variance $\rightarrow$ Overfitting):** Mô hình quá phức tạp (ví dụ Decision Tree không giới hạn độ sâu), học vẹt luôn cả nhiễu của tập train, dẫn đến kết quả train rất cao nhưng test rất kém.
* **Giải pháp kiểm soát Overfitting:**
  - Thu thập thêm dữ liệu hoặc tăng cường dữ liệu (Data Augmentation).
  - Giảm bớt số lượng đặc trưng (Feature Selection, PCA).
  - Áp dụng Regularization ($L_1$ Lasso, $L_2$ Ridge).
  - Sử dụng mô hình Ensemble (Random Forest).

### 2. Tiêu chí lựa chọn mô hình trong dự án thực tế
1. **Dựa vào khối lượng dữ liệu:**
   - Dữ liệu nhỏ ($< 10,000$ dòng): Linear/Logistic Regression, Naive Bayes, SVM.
   - Dữ liệu trung bình ($10,000 - 1,000,000$ dòng): Random Forest, LightGBM, XGBoost, CatBoost.
   - Dữ liệu rất lớn ($> 1,000,000$ dòng) hoặc dữ liệu phi cấu trúc (Ảnh, Âm thanh, Văn bản dài): Mạng nơ-ron tích chập (CNN), Transformer, Deep Learning.
2. **Dựa vào yêu cầu giải thích (Interpretability):**
   - Tài chính/Ngân hàng/Y tế bắt buộc giải thích: Logistic Regression, Decision Tree, Linear Regression.
   - Thương mại điện tử/Gợi ý cần độ chính xác tối đa: Ensemble Trees, Deep Learning.

### 3. Lộ trình phát triển tiếp theo (Next Steps)
* **Mở rộng sang Deep Learning:** Mạng truyền thẳng (MLP), Mạng nơ-ron tích chập (CNN) cho Thị giác máy tính (Computer Vision), Mạng nơ-ron hồi quy (LSTM/GRU) và Kiến trúc Transformer cho NLP.
* **Học kỹ thuật MLOps:** Quản lý vòng đời mô hình (MLflow, DVC), tự động hóa huấn luyện (CI/CD pipelines), giám sát hiện tượng suy thoái dữ liệu (Data Drift / Concept Drift) trong môi trường sản xuất.
