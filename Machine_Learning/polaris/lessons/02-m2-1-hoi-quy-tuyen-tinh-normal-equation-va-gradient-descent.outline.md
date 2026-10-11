# Đề cương bài học: M2.1 - Hồi quy tuyến tính: Normal Equation và Gradient Descent

- **Module:** M2.1 - M2.1 - Hồi quy tuyến tính: Normal Equation và Gradient Descent
- **Thời gian (when):** Theo lịch học
- **Thời lượng:** 20 phút
- **Theme:** ocean
- **Icon:** `trend-up`

## 1. Mục tiêu (Đầu ra)
- [O3] Tự cài đặt Linear Regression từ đầu bằng NumPy sử dụng Normal Equation và Gradient Descent trên tập dữ liệu StudentScore, đối chiếu hệ số khớp scikit-learn LinearRegression dưới 1e-3.
- Giải thích hình học của Ordinary Least Squares (hình chiếu trực giao lên không gian cột của X) và các điều kiện ma trận suy biến dẫn đến đa cộng tuyến.

## 2. Dữ kiện có nguồn (Dùng cho slide `source`)
- [F1] "Dự đoán tuyến tính dạng ma trận được biểu diễn là y_hat = X @ w + b với X thuộc R^(n x d), w thuộc R^(d,), bias b thuộc R, hoặc dạng mở rộng cột bias là y_hat = X_bar @ theta với X_bar thuộc R^(n x (d+1))." — Nguồn: S1 @ lines 18-35 [Khóa học]
- [F2] "Hàm mất mát sai số toàn phương trung bình (MSE) có dạng J(w) = (1/n) * ||X @ w - y||^2 và gradient giải tích tương ứng là nabla J = (2/n) * X.T @ (X @ w - y)." — Nguồn: S1 @ lines 52-68 [Khóa học]
- [F4] "Điều kiện dừng tối ưu đặt gradient nabla J = 0 dẫn đến phương trình pháp tuyến (Normal Equation) X.T @ X @ w = X.T @ y, có nghiệm duy nhất khi ma trận hiệp phương sai X.T @ X khả nghịch (full column rank)." — Nguồn: S7 @ [p. 11], Sec. 1.2 [Khóa học]
- [F7] "Phương thức scikit-learn LinearRegression giải bài toán bình phương tối thiểu thông qua scipy.linalg.lstsq dựa trên phân tích SVD hoặc QR, không dùng nghịch đảo trực tiếp np.linalg.inv để đảm bảo độ ổn định số học khi ma trận suy biến." — Nguồn: S4 @ #ordinary-least-squares [Khóa học]
- [F8] "Nếu dữ liệu có các đặc trưng mang thang đo chênh lệch lớn, mặt mức (contour) của hàm mất mát trở thành hình elip dẹt, khiến Gradient Descent di chuyển ngoằn ngoèo (zigzag) và buộc phải giảm learning rate rất nhỏ để tránh phân kỳ." — Nguồn: S5 @ Sec. 1.5.4 Tips on Practical Use [Khóa học]
- [F9] "Chuẩn hóa đặc trưng (StandardScaler: z = (x - mu) / sigma) đưa các đường đồng mức về hình tròn đồng tâm, giúp gradient trỏ gần như trực diện về điểm cực tiểu toàn cục và tăng tốc độ hội tụ của thuật toán tối ưu bậc một." — Nguồn: S5 @ Sec. 1.5.4 Tips on Practical Use [Khóa học]
- [F10] "Trong bài toán hồi quy đơn biến y = w*x + b, nghiệm giải tích đóng là w = sum((x_i - bar(x))*(y_i - bar(y))) / sum((x_i - bar(x))^2) và b = bar(y) - w*bar(x), bảo đảm tổng các phần dư sum(e_i) = 0 khi có bias." — Nguồn: S6 @ Sec. 3.1.1 Estimating the Coefficients [Khóa học]
- [F11] "Hình học của OLS: vector dự đoán y_hat = X @ w_hat là hình chiếu trực giao (orthogonal projection) của vector mục tiêu y lên không gian cột của ma trận thiết kế X, do đó vector phần dư e = y - y_hat vuông góc với mọi cột của X." — Nguồn: S6 @ Sec. 3.2.1 Multiple Linear Regression [Mở rộng]
- [F12] "Tập dữ liệu StudentScore chứa thông tin điểm thi học sinh gồm các biến đầu vào điểm đọc, điểm viết và biến mục tiêu math score; tệp mang định dạng thực chất là CSV phân tách bởi dấu phẩy dù có phần mở rộng .xls." — Nguồn: S3 @ lines 1-20 [Khóa học]
- [F14] "Hệ số xác định R^2 đo lường tỷ lệ phương sai của biến mục tiêu được giải thích bởi mô hình; trên tập kiểm tra (test set), R^2 có thể nhận giá trị âm nếu mô hình dự đoán tệ hơn việc lấy trung bình đơn giản của tập huấn luyện." — Nguồn: S4 @ Sec. Regression metrics [Mở rộng]
- [F15] "Khi tồn tại hiện tượng đa cộng tuyến hoàn hảo (multicollinearity) giữa các cột của X, chỉ số điều kiện cond(X.T @ X) tiến tới vô cùng, khiến phương trình pháp tuyến có vô số nghiệm và độ dao động của hệ số cực lớn." — Nguồn: S6 @ Sec. 3.3.3 Collinearity [Mở rộng]

## 3. Hiểu lầm -> Phương án nhiễu cho Quiz
### Hiểu lầm 1: "Hệ số xác định R^2 luôn nằm trong đoạn [0, 1] trên mọi tập dữ liệu kiểm tra."
- **Nguyên nhân hiểu sai:** Nhiều người nhầm lẫn R^2 là bình phương hệ số tương quan Pearson r^2 nên nghĩ rằng nó luôn không âm.
- **Bản chất đúng:** R^2 chỉ bị chặn dưới bởi 0 trên tập huấn luyện của OLS có hệ số chặn; trên tập kiểm tra (test set), nếu mô hình dự đoán tệ hơn cả giá trị trung bình thì R^2 hoàn toàn có thể nhận giá trị âm.
- **Gợi ý phương án nhiễu (distractor):** Đưa quan niệm sai "Hệ số xác định R^2 luôn nằm trong đoạn [0, 1] trên mọi tập dữ liệu kiểm tra." vào làm đáp án bẫy trong câu hỏi quiz trắc nghiệm.

### Hiểu lầm 2: "Cách tốt nhất để giải Normal Equation trong thực tế là dùng np.linalg.inv(X.T @ X)."
- **Nguyên nhân hiểu sai:** Công thức toán học viết w = (X.T @ X)^(-1) @ X.T @ y khiến người học áp dụng hàm nghịch đảo ma trận thô trong code.
- **Bản chất đúng:** Nghịch đảo trực tiếp X.T @ X rất dễ gặp lỗi số học khi ma trận gần suy biến (ill-conditioned); các thư viện chuẩn như scikit-learn dùng phân tích SVD hoặc QR để giải bình phương tối thiểu ổn định hơn.
- **Gợi ý phương án nhiễu (distractor):** Đưa quan niệm sai "Cách tốt nhất để giải Normal Equation trong thực tế là dùng np.linalg.inv(X.T @ X)." vào làm đáp án bẫy trong câu hỏi quiz trắc nghiệm.

## 4. Thực hành & Dự đoán (Predict-then-Run)
- **Khởi động (15'):** Tính nghiệm giải tích w, b bằng công thức giải tích đóng cho 3 điểm dữ liệu đơn giản (1, 1), (2, 2), (3, 2), sau đó kiểm tra lại bằng np.polyfit(x, y, 1).
  - *DoD:* Kết quả tính tay khớp np.polyfit đến 3 chữ số thập phân; giải thích lý do toán học vì sao tổng phần dư triệt tiêu về 0 khi mô hình có hệ số chệch b.
- **Cốt lõi (45'):** Tạo notebook 02_Supervised_Learning/01_Regression/m2_linreg_scratch.ipynb: đọc dữ liệu StudentScore.xls bằng pd.read_csv, thiết lập bài toán dự đoán math score từ reading score và writing score; chia tập 80/20, chuẩn hóa đặc trưng bằng thống kê của train; tự lập trình hai phương pháp tìm nghiệm: Normal Equation và Gradient Descent từ đầu bằng NumPy.
  - *DoD:* Không xảy ra rò rỉ dữ liệu (chỉ dùng mean và std của train để transform test); hệ số w và bias b giữa Normal Equation, Gradient Descent và scikit-learn LinearRegression sai khác dưới 1e-3.
- **Thử thách (30'):** Thực hiện thí nghiệm loại bỏ bước chuẩn hóa đặc trưng trước khi chạy Gradient Descent trên StudentScore, đo số vòng lặp và mức độ dao động của hàm mất mát.
  - *DoD:* Biểu đồ đường cong hàm mất mát MSE qua 200 vòng lặp so sánh giữa có và không chuẩn hóa; giải thích tại sao không chuẩn hóa buộc learning rate phải giảm ít nhất 10 lần.
*(Lưu ý: Không viết code giải bài tập ở đây; chỉ đưa ra ý tưởng slide bài tập và tiêu chuẩn hoàn thành DoD)*

## 5. Neo trí nhớ gợi ý (Memory Anchors)
- **Memory Palace (Lâu đài ký ức):** Đặt các bước thực thi tuần tự tại các vị trí quen thuộc trong nhà (Cửa chính -> Phòng khách -> Bàn làm việc -> Giá sách).
- **Picture Anchors (Hình ảnh trực quan):** Biểu tượng cụ thể cho các khái niệm trừu tượng (ví dụ: cái phích cắm cho MCP, cái cân cho token budget).
- **Analogy (Ẩn dụ):** So sánh cơ chế với đời sống thực tế và chỉ rõ ranh giới mà phép ẩn dụ không còn đúng.
- **Mnemonic:** Câu khẩu hiệu hoặc từ khóa tóm lược nguyên tắc bất biến.

## 6. Trang vở gợi ý (Notebook: 4-8 dòng chép tay)
```text
1. M2.1 - Hồi quy tuyến tính: Normal Equation và Gradient Descent: Hồi quy tuyến tính là nền móng của học có giám sát; việc tự cài đặt từ đầu bằng cả nghiệm đóng và tối ưu hóa lặp giúp làm chủ cách siêu tham số điều khiển mô hình trước khi bước sang các thuật toán phức tạp hơn.
2. Trong hồi quy đơn biến, nghiệm giải tích đóng là w = sum((x_i - bar(x))*(y_i - bar(y))) / sum((x_i - bar(x))^2) và b = bar(y) - w*bar(x); tổng sai số phần dư sum(e_i) luôn bằng 0 khi mô hình có hệ số chặn b.
3. Trong hồi quy đa biến, điều kiện triệt tiêu gradient nabla J = 0 dẫn đến phương trình pháp tuyến (Normal Equation) X.T @ X @ w = X.T @ y, có nghiệm duy nhất khi ma trận thiết kế X có đầy đủ hạng cột.
4. Quy tắc: R^2 chỉ bị chặn dưới bởi 0 trên tập huấn luyện của OLS có hệ số chặn; trên tập kiểm tra (test set), nếu mô hình dự đoán tệ hơn cả giá trị trung bình thì R^2 hoàn toàn có thể nhận giá trị âm.
5. Checkpoint: Notebook m2_linreg_scratch.ipynb đạt Definition of Done
```

## 7. Tự kiểm tra (Quiz / Flashcards)
1. (explain) Vì sao trong bài toán hồi quy tuyến tính đơn biến có hệ số chặn (bias b), tổng của tất cả các phần dư sum(y_i - y_hat_i) luôn bằng 0?
   - *Đáp án:* Hệ số chặn b được xác định bằng cách đặt đạo hàm riêng của tổng bình phương phần dư theo b bằng 0: d(sum (y_i - w*x_i - b)^2) / db = -2 * sum(y_i - y_hat_i) = 0. Do đó tổng các phần dư triệt tiêu hoàn toàn về 0.
2. (explain) Giải thích ý nghĩa hình học của vector dự đoán y_hat trong không gian Euclid n chiều đối với phương pháp bình phương tối thiểu OLS.
   - *Đáp án:* Trong không gian n chiều của các quan sát mẫu, vector dự đoán y_hat = X @ w là hình chiếu trực giao của vector nhãn thực tế y lên không gian con tạo bởi các cột của ma trận thiết kế X. Khoảng cách Euclid ||y - y_hat|| ngắn nhất khi vector sai số e = y - y_hat vuông góc trực giao với mọi vector cột của X.
3. (predict) Dự đoán giá trị của hệ số xác định R^2 trên tập kiểm tra (test set) khi mô hình đưa ra dự đoán kém hơn mức trung bình của tập huấn luyện.
   - *Đáp án:* Hệ số R^2 = 1 - (SS_res / SS_tot). Khi tổng bình phương sai số dự đoán SS_res lớn hơn tổng bình phương độ lệch so với trung bình SS_tot, phân số lớn hơn 1 dẫn đến R^2 nhận giá trị âm.
4. (remember) Tại sao scikit-learn sử dụng scipy.linalg.lstsq thay vì nghịch đảo trực tiếp np.linalg.inv(X.T @ X) để giải bài toán Ordinary Least Squares?
   - *Đáp án:* Nghịch đảo trực tiếp X.T @ X tốn chi phí tính toán O(d^3), làm bình phương chỉ số điều kiện cond(X)^2 khiến sai số số học tăng vọt và báo lỗi nếu ma trận suy biến. scipy.linalg.lstsq sử dụng phân tích SVD hoặc QR để tìm nghiệm bình phương tối thiểu ổn định số học và xử lý được trường hợp ma trận không khả nghịch.

## 8. Code liên quan (Materials)
- **Giáo trình Khóa học - Lesson 05: Linear Regression** (15 phút) path: `00_Curriculum_and_Materials/GIAO_TRINH_CHI_TIET_TOAN_BO_KHOA_HOC.md` 
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `00_Curriculum_and_Materials/GIAO_TRINH_CHI_TIET_TOAN_BO_KHOA_HOC.md` và trích dẫn dòng cốt lõi.
- **regression.py - Student Score Prediction Pipeline** (15 phút) path: `02_Supervised_Learning/01_Regression/regression.py` 
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `02_Supervised_Learning/01_Regression/regression.py` và trích dẫn dòng cốt lõi.
- **scikit-learn User Guide - 1.1.1 Ordinary Least Squares** (25 phút)  url: https://scikit-learn.org/stable/modules/linear_model.html
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `scikit-learn User Guide - 1.1.1 Ordinary Least Squares` và trích dẫn dòng cốt lõi.
- **An Introduction to Statistical Learning (ISLP) - Chương 3: Linear Regression** (25 phút)  url: https://www.statlearning.com/
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `An Introduction to Statistical Learning (ISLP) - Chương 3: Linear Regression` và trích dẫn dòng cốt lõi.

## 9. Dàn ý Slide đề xuất (Slide Plan Skeleton)
1. `title`: Tiêu đề bài học và cam kết đầu ra rõ ràng
2. `big-fact` / `split`: Trực giác nền tảng và lý thuyết cốt lõi kèm citation `source`
3. `steps` / `cards`: Neo trí nhớ (Memory anchors, hình ảnh hóa hoặc memory palace)
4. `quote` / `markdown`: Trang vở ghi chép (Notebook 4-8 dòng chép tay)
5. `code-run` / `split`: Dự đoán kết quả rồi mới chạy (Predict-then-run, dễ -> khó)
6. `quiz`: Câu hỏi trắc nghiệm kiểm tra nhanh với phương án nhiễu từ hiểu lầm
7. `bullets` / `steps`: Đi bộ hồi tưởng (Recall walk qua các chặng)
8. `summary`: Tổng kết kiến thức và bài tập tiếp theo
