"""
Unsupervised Learning: K-Means Clustering & PCA Dimensionality Reduction

Mục tiêu học tập:
1. Thuật toán K-Means: Tìm trọng tâm cụm (centroids) và gán nhãn không cần giám sát.
2. Phương pháp khuỷu tay (Elbow Method) và Hệ số bóng đổ (Silhouette Score) chọn số cụm K tối ưu.
3. Phân tích thành phần chính (PCA): Chiếu dữ liệu đa chiều xuống 2 chiều giữ lại phương sai lớn nhất.
"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def run_unsupervised_demo():
    # 1. Sinh dữ liệu giả lập 4 cụm trong không gian 6 chiều
    X, y_true = make_blobs(n_samples=500, n_features=6, centers=4, cluster_std=1.2, random_state=42)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("=== 1. Đánh Giá K Tối Ưu Với Elbow & Silhouette Score ===")
    inertias = []
    sil_scores = []
    k_range = range(2, 8)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        inertias.append(kmeans.inertia_)
        sil = silhouette_score(X_scaled, labels)
        sil_scores.append(sil)
        print(f"K = {k} | Inertia (WCSS): {kmeans.inertia_:8.2f} | Silhouette Score: {sil:.4f}")

    best_k = list(k_range)[np.argmax(sil_scores)]
    print(f"\n-> Số cụm K tối ưu theo Silhouette Score: {best_k}")

    # 2. Huấn luyện mô hình K-Means với K tối ưu
    best_kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    cluster_labels = best_kmeans.fit_predict(X_scaled)

    # 3. Giảm chiều dữ liệu bằng PCA (6D -> 2D)
    print("\n=== 2. Giảm Chiều Dữ Liệu Bằng PCA (6D -> 2D) ===")
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    explained_var = pca.explained_variance_ratio_
    total_var = np.sum(explained_var)
    print(f"Tỷ lệ phương sai thành phần 1 (PC1): {explained_var[0] * 100:.2f}%")
    print(f"Tỷ lệ phương sai thành phần 2 (PC2): {explained_var[1] * 100:.2f}%")
    print(f"Tổng phương sai được giữ lại trong 2D: {total_var * 100:.2f}%")
    print(f"Tọa độ trọng tâm (Centroids) sau khi chiếu PCA:\n{pca.transform(best_kmeans.cluster_centers_)}")

if __name__ == "__main__":
    run_unsupervised_demo()
