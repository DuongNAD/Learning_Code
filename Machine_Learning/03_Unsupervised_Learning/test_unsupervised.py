"""
Unit tests for 03_Unsupervised_Learning algorithms (K-Means, PCA, Recommender).
"""

import sys
import os
import numpy as np
import pytest
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs

# Add Recommender_Systems directory to sys.path
REC_DIR = os.path.join(os.path.dirname(__file__), "Recommender_Systems")
if REC_DIR not in sys.path:
    sys.path.insert(0, REC_DIR)

from recommendation_system import ContentBasedRecommender


class TestUnsupervisedLearning:
    def test_kmeans_clustering_stability(self):
        # Generate 4 distinct isotropic Gaussian clusters
        X, y_true = make_blobs(n_samples=200, centers=4, cluster_std=0.6, random_state=42)
        kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)

        assert len(np.unique(labels)) == 4
        sil = silhouette_score(X, labels)
        # Silhouette for well-separated blobs should be > 0.65
        assert sil > 0.65

    def test_pca_dimensionality_reduction(self):
        X, _ = make_blobs(n_samples=100, n_features=10, random_state=42)
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X)

        assert X_pca.shape == (100, 2)
        explained_var = np.sum(pca.explained_variance_ratio_)
        assert 0.0 < explained_var <= 1.0

    def test_content_based_recommender(self):
        recommender = ContentBasedRecommender()
        recs = recommender.recommend("Heat (1995)", top_k=5)

        assert len(recs) == 5
        assert "Tên phim gợi ý" in recs.columns
        assert "Độ tương đồng Cosine" in recs.columns
        # Top match should have very high similarity
        top_score = recs.iloc[0]["Độ tương đồng Cosine"]
        assert top_score >= 0.8
