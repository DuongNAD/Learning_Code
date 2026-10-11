# Đề cương bài học: M1 - Toán nền tảng cho Machine Learning

- **Module:** M1 - M1 - Toán nền tảng cho Machine Learning
- **Thời gian (when):** Theo lịch học
- **Thời lượng:** 20 phút
- **Theme:** midnight
- **Icon:** `function`

## 1. Mục tiêu (Đầu ra)
- [O1] Viết phương trình ma trận y_hat = X @ w + b chuẩn shape, tính giải tích gradient của MSE và kiểm chứng bằng gradient số với sai số tương đối < 1e-6.
- [O2] Dự đoán chính xác hành vi của Gradient Descent (hội tụ, dao động đổi dấu, phân kỳ) theo các giá trị learning rate eta và giải thích vai trò của chuẩn hóa đặc trưng.

## 2. Dữ kiện có nguồn (Dùng cho slide `source`)
- [F1] "Dự đoán tuyến tính dạng ma trận được biểu diễn là y_hat = X @ w + b với X thuộc R^(n x d), w thuộc R^(d,), bias b thuộc R, hoặc dạng mở rộng cột bias là y_hat = X_bar @ theta với X_bar thuộc R^(n x (d+1))." — Nguồn: S1 @ lines 18-35 [Khóa học]
- [F2] "Hàm mất mát sai số toàn phương trung bình (MSE) có dạng J(w) = (1/n) * ||X @ w - y||^2 và gradient giải tích tương ứng là nabla J = (2/n) * X.T @ (X @ w - y)." — Nguồn: S1 @ lines 52-68 [Khóa học]
- [F3] "Đạo hàm giải tích của hàm mất mát được kiểm tra tính chính xác qua gradient số đối xứng với công thức dJ/dw_j approx (J(w + epsilon * e_j) - J(w - epsilon * e_j)) / (2 * epsilon) với epsilon xấp xỉ 1e-5." — Nguồn: S1 @ lines 80-105 [Khóa học]
- [F4] "Điều kiện dừng tối ưu đặt gradient nabla J = 0 dẫn đến phương trình pháp tuyến (Normal Equation) X.T @ X @ w = X.T @ y, có nghiệm duy nhất khi ma trận hiệp phương sai X.T @ X khả nghịch (full column rank)." — Nguồn: S7 @ [p. 11], Sec. 1.2 [Khóa học]
- [F5] "Cập nhật tham số trong Gradient Descent theo quy tắc w_(t+1) = w_t - eta * nabla J. Với hàm mục tiêu bậc hai f(w) = w^2, hệ số cập nhật là w_(t+1) = (1 - 2*eta)*w_t, hội tụ khi 0 < eta < 1, dao động đổi dấu khi 0.5 < eta < 1, và phân kỳ khi eta > 1." — Nguồn: S10 @ Sec. Convergence and step size [Khóa học]
- [F6] "Khi hàm mất mát viết dưới dạng J = (1/(2n)) * ||X @ w - y||^2 (chuẩn quy ước Stanford CS229), gradient thu được là (1/n) * X.T @ (X @ w - y), làm miền hội tụ của learning rate tăng gấp đôi (eta < 2 thay vì eta < 1)." — Nguồn: S7 @ [p. 10], Sec. 1.1 [Khóa học]
- [F8] "Nếu dữ liệu có các đặc trưng mang thang đo chênh lệch lớn, mặt mức (contour) của hàm mất mát trở thành hình elip dẹt, khiến Gradient Descent di chuyển ngoằn ngoèo (zigzag) và buộc phải giảm learning rate rất nhỏ để tránh phân kỳ." — Nguồn: S5 @ Sec. 1.5.4 Tips on Practical Use [Khóa học]
- [F9] "Chuẩn hóa đặc trưng (StandardScaler: z = (x - mu) / sigma) đưa các đường đồng mức về hình tròn đồng tâm, giúp gradient trỏ gần như trực diện về điểm cực tiểu toàn cục và tăng tốc độ hội tụ của thuật toán tối ưu bậc một." — Nguồn: S5 @ Sec. 1.5.4 Tips on Practical Use [Khóa học]
- [F13] "Lỗi phát thanh (broadcasting) trong NumPy xảy ra khi trừ vector 1D (n,) với vector cột 2D (n, 1), tạo ra ma trận vuông (n, n) thay vì mảng sai số 1D, dẫn đến tính toán gradient sai lệch nghiêm trọng mà không báo lỗi runtime." — Nguồn: S1 @ lines 110-125 [Khóa học]
- [F15] "Khi tồn tại hiện tượng đa cộng tuyến hoàn hảo (multicollinearity) giữa các cột của X, chỉ số điều kiện cond(X.T @ X) tiến tới vô cùng, khiến phương trình pháp tuyến có vô số nghiệm và độ dao động của hệ số cực lớn." — Nguồn: S6 @ Sec. 3.3.3 Collinearity [Mở rộng]

## 3. Hiểu lầm -> Phương án nhiễu cho Quiz
### Hiểu lầm 1: "Gradient là vector chỉ hướng xuống dốc dốc nhất của hàm mất mát."
- **Nguyên nhân hiểu sai:** Nhiều người học lầm tưởng vector gradient trỏ về đáy vực cực tiểu.
- **Bản chất đúng:** Gradient luôn chỉ hướng hàm số tăng nhanh nhất; thuật toán Gradient Descent phải đi ngược hướng gradient (trừ đi gradient) để hạ thấp hàm mất mát.
- **Gợi ý phương án nhiễu (distractor):** Đưa quan niệm sai "Gradient là vector chỉ hướng xuống dốc dốc nhất của hàm mất mát." vào làm đáp án bẫy trong câu hỏi quiz trắc nghiệm.

### Hiểu lầm 2: "Trừ vector (n,) cho vector (n, 1) trong NumPy vẫn cho ra vector sai số kích thước (n,)."
- **Nguyên nhân hiểu sai:** Trộn vector hàng (n,) với vector cột (n, 1) kích hoạt broadcasting ngầm định của NumPy mà không báo lỗi.
- **Bản chất đúng:** In .shape của phần dư y - X @ w trước khi tính norm hoặc dot product để đảm bảo mảng giữ đúng kích thước 1D (n,).
- **Gợi ý phương án nhiễu (distractor):** Đưa quan niệm sai "Trừ vector (n,) cho vector (n, 1) trong NumPy vẫn cho ra vector sai số kích thước (n,)." vào làm đáp án bẫy trong câu hỏi quiz trắc nghiệm.

## 4. Thực hành & Dự đoán (Predict-then-Run)
- **Khởi động (15'):** Ghi dự đoán kích thước (shape) của các biểu thức NumPy: X @ w, X - X.mean(axis=0), y - X @ w, và y - (X @ w).reshape(-1, 1) với X shape (100, 3), w shape (3,), y shape (100,) trước khi thực thi mã nguồn.
  - *DoD:* Bảng dự đoán shape ghi trước khi chạy; phát hiện và giải thích được lỗi broadcasting tạo ma trận (100, 100) trong Sổ lỗi nếu có.
- **Cốt lõi (45'):** Tạo notebook 01_Math_Foundations/m1_gradient_lab.ipynb: sinh 200 điểm thực nghiệm y = 3x + 2 + nhiễu; tự tính gradient giải tích của MSE và so khớp với gradient số đối xứng (epsilon = 1e-5); chạy vòng lặp Gradient Descent 100 bước với 3 learning rate eta in {0.001, 0.1, 1.1} sau khi ghi dự đoán trước.
  - *DoD:* Sai số tương đối giữa gradient giải tích và gradient số < 1e-6; hoàn thành bảng đối chiếu (eta, dự đoán, kết quả thực tế); nghiệm w, b của eta tối ưu khớp np.linalg.lstsq với sai số < 1e-3.
- **Thử thách (30'):** Tạo ma trận dữ liệu có 2 cột tương quan tuyến tính hoàn hảo, đo chỉ số điều kiện np.linalg.cond(X.T @ X) và quan sát hiện tượng số học khi giải Normal Equation.
  - *DoD:* Báo cáo 1 trang phân tích hình học chứng minh ma trận mất hạng cột dẫn đến không gian nghiệm vô hạn và chỉ số điều kiện cond tiến tới vô cùng.
*(Lưu ý: Không viết code giải bài tập ở đây; chỉ đưa ra ý tưởng slide bài tập và tiêu chuẩn hoàn thành DoD)*

## 5. Neo trí nhớ gợi ý (Memory Anchors)
- **Memory Palace (Lâu đài ký ức):** Đặt các bước thực thi tuần tự tại các vị trí quen thuộc trong nhà (Cửa chính -> Phòng khách -> Bàn làm việc -> Giá sách).
- **Picture Anchors (Hình ảnh trực quan):** Biểu tượng cụ thể cho các khái niệm trừu tượng (ví dụ: cái phích cắm cho MCP, cái cân cho token budget).
- **Analogy (Ẩn dụ):** So sánh cơ chế với đời sống thực tế và chỉ rõ ranh giới mà phép ẩn dụ không còn đúng.
- **Mnemonic:** Câu khẩu hiệu hoặc từ khóa tóm lược nguyên tắc bất biến.

## 6. Trang vở gợi ý (Notebook: 4-8 dòng chép tay)
```text
1. M1 - Toán nền tảng cho Machine Learning: Mọi thuật toán học có giám sát đều lặp lại mô thức: biểu diễn dữ liệu bằng ma trận, định nghĩa hàm mất mát toàn cục và tối ưu hóa tham số theo hướng ngược vector gradient.
2. Dữ liệu được tổ chức thành ma trận X kích thước (n x d), dự đoán tuyến tính là tích vô hướng X @ w + b; lưu ý lỗi broadcasting khi trừ mảng (n,) với cột (n, 1) tạo ma trận vuông (n, n).
3. Hàm mất mát Mean Squared Error (MSE) có đạo hàm giải tích nabla J = (2/n) * X.T @ (X @ w - y), thể hiện hướng tăng dốc mạnh nhất của sai số.
4. Quy tắc: Gradient luôn chỉ hướng hàm số tăng nhanh nhất; thuật toán Gradient Descent phải đi ngược hướng gradient (trừ đi gradient) để hạ thấp hàm mất mát.
5. Checkpoint: Notebook m1_gradient_lab.ipynb đạt Definition of Done
```

## 7. Tự kiểm tra (Quiz / Flashcards)
1. (apply) Viết công thức gradient giải tích nabla J của hàm mất mát sai số toàn phương trung bình J(w) = (1/n) * ||X @ w - y||^2 theo vector w.
   - *Đáp án:* nabla J = (2/n) * X.T @ (X @ w - y). Nếu dùng quy ước J = (1/(2n)) * ||X @ w - y||^2 thì nabla J = (1/n) * X.T @ (X @ w - y).
2. (explain) Giải thích trực giác hình học vì sao việc chuẩn hóa đặc trưng (feature scaling) giúp thuật toán Gradient Descent hội tụ nhanh hơn và ổn định hơn?
   - *Đáp án:* Khi các đặc trưng có thang đo chênh lệch lớn, các đường đồng mức của hàm mất mát bị kéo dài thành hình elip rất dẹt. Vector gradient luôn vuông góc với đường đồng mức nên không trỏ về tâm cực tiểu mà dao động ngoằn ngoèo. Chuẩn hóa đặc trưng giúp các đường đồng mức trở nên tròn đều, vector gradient trỏ thẳng về cực tiểu giúp bước nhảy đi thẳng và nhanh chóng hội tụ.
3. (predict) Cho hàm mục tiêu bậc hai f(w) = w^2, điểm khởi tạo w_0 = 1, và tốc độ học eta = 0.75. Dự đoán giá trị của w_1, w_2 và nhận định thuật toán sẽ hội tụ, dao động hay phân kỳ?
   - *Đáp án:* Đạo hàm f'(w) = 2w. Công thức cập nhật: w_(t+1) = w_t - 0.75*(2w_t) = (1 - 1.5)*w_t = -0.5 * w_t. Do đó w_1 = -0.5, w_2 = 0.25. Giá trị w đổi dấu qua mỗi bước (dao động) nhưng biên độ giảm dần về 0 (| -0.5 | < 1), do đó thuật toán dao động và hội tụ về 0.
4. (predict) Trong NumPy, cho mảng a có shape (3,) và mảng b có shape (3, 1). Dự đoán kết quả shape của phép trừ (a - b) và giải thích hiện tượng này.
   - *Đáp án:* Kết quả có shape (3, 3). Do quy tắc broadcasting, mảng a được mở rộng thành hàng (1, 3) rồi sao chép thành 3 hàng, mảng b được sao chép thành 3 cột, dẫn đến ma trận kích thước (3, 3) thay vì mảng 1D (3,). Đây là lỗi broadcasting phổ biến khi tính sai số hồi quy.

## 8. Code liên quan (Materials)
- **math_primer.py - Đạo hàm ma trận và Gradient Check** (15 phút) path: `01_Math_Foundations/math_primer.py` 
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `01_Math_Foundations/math_primer.py` và trích dẫn dòng cốt lõi.
- **ML_Cheatsheet_Formulas.md - Mục 1: Math Foundations** (15 phút) path: `Notes/ML_Cheatsheet_Formulas.md` 
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `Notes/ML_Cheatsheet_Formulas.md` và trích dẫn dòng cốt lõi.
- **Stanford CS229 Lecture Notes - Supervised Learning & Gradient Descent** (20 phút)  url: https://cs229.stanford.edu/main_notes.pdf
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `Stanford CS229 Lecture Notes - Supervised Learning & Gradient Descent` và trích dẫn dòng cốt lõi.
- **Wikipedia: Gradient descent** (20 phút)  url: https://en.wikipedia.org/wiki/Gradient_descent
  - Gợi ý slide: dùng slide `split` hoặc `code-run` với file `Wikipedia: Gradient descent` và trích dẫn dòng cốt lõi.

## 9. Dàn ý Slide đề xuất (Slide Plan Skeleton)
1. `title`: Tiêu đề bài học và cam kết đầu ra rõ ràng
2. `big-fact` / `split`: Trực giác nền tảng và lý thuyết cốt lõi kèm citation `source`
3. `steps` / `cards`: Neo trí nhớ (Memory anchors, hình ảnh hóa hoặc memory palace)
4. `quote` / `markdown`: Trang vở ghi chép (Notebook 4-8 dòng chép tay)
5. `code-run` / `split`: Dự đoán kết quả rồi mới chạy (Predict-then-run, dễ -> khó)
6. `quiz`: Câu hỏi trắc nghiệm kiểm tra nhanh với phương án nhiễu từ hiểu lầm
7. `bullets` / `steps`: Đi bộ hồi tưởng (Recall walk qua các chặng)
8. `summary`: Tổng kết kiến thức và bài tập tiếp theo
