# 🔍 Học Không Giám Sát & Hệ Thống Gợi Ý (Unsupervised Learning & Recommenders)

Khám phá cấu trúc tiềm ẩn, phân nhóm dữ liệu tự động, nén chiều dữ liệu và xây dựng động cơ gợi ý sản phẩm.

---

## 📂 Các Tiểu Thư Mục Thực Hành

### 1. `Clustering_and_Dimensionality_Reduction/`
- **Tập tin chính**: `kmeans_pca_demo.py`
- **Nội dung thực hành**:
  - Thuật toán phân cụm **K-Means**: Tìm trọng tâm cụm (Centroids).
  - Phương pháp khuỷu tay (**Elbow Method** / WCSS Inertia) & Hệ số bóng đổ (**Silhouette Score**) để chọn số lượng cụm $K$ tối ưu.
  - Phân tích thành phần chính (**PCA**): Giảm chiều dữ liệu từ không gian 6D xuống 2D, giải thích tỷ lệ phương sai tích lũy và trực quan hóa trọng tâm cụm.
- **Chạy thử**: `python3 kmeans_pca_demo.py`

### 2. `Recommender_Systems/`
- **Tập tin chính**:
  - `recommendation_system.py`: Động cơ gợi ý phim dựa trên nội dung (Content-Based Filtering) dùng `TfidfVectorizer` và `cosine_similarity`.
  - `movie_data/`: Tập dữ liệu chuẩn MovieLens với `movies.csv`, `ratings.csv`, `users.csv`.
- **Chạy thử**: `python3 recommendation_system.py`
