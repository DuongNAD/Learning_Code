"""
Unit tests for 04_Model_Evaluation_Tuning modules.
"""

import numpy as np
import pytest
from sklearn.datasets import make_classification, make_regression
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier

from model_evaluation_metrics import (
    evaluate_classification,
    evaluate_regression,
    find_optimal_threshold,
    evaluate_cv_stability
)
from hyperparameter_tuning_suite import (
    compare_grid_vs_random_search,
    diagnose_validation_curve
)
from model_benchmark_comparison import benchmark_classifiers


class TestModelEvaluationMetrics:
    def test_evaluate_classification_binary(self):
        y_true = np.array([1, 0, 1, 1, 0, 0])
        y_pred = np.array([1, 0, 1, 0, 0, 0])
        y_prob = np.array([0.9, 0.1, 0.8, 0.4, 0.2, 0.3])

        metrics = evaluate_classification(y_true, y_pred, y_prob)
        assert "accuracy" in metrics
        assert "f1_binary" in metrics
        assert "roc_auc" in metrics
        assert 0.0 <= metrics["accuracy"] <= 1.0
        assert 0.0 <= metrics["roc_auc"] <= 1.0

    def test_find_optimal_threshold_f1(self):
        y_true = np.array([1, 1, 1, 0, 0, 0])
        y_prob = np.array([0.8, 0.7, 0.6, 0.4, 0.3, 0.2])

        best_t, best_score = find_optimal_threshold(y_true, y_prob, metric="f1")
        assert 0.05 <= best_t <= 0.95
        assert best_score == pytest.approx(1.0)

    def test_find_optimal_threshold_youden(self):
        y_true = np.array([1, 1, 0, 0])
        y_prob = np.array([0.9, 0.8, 0.2, 0.1])

        best_t, best_score = find_optimal_threshold(y_true, y_prob, metric="youden")
        assert best_score == pytest.approx(1.0)

    def test_evaluate_regression_perfect(self):
        y_true = np.array([10.0, 20.0, 30.0])
        y_pred = np.array([10.0, 20.0, 30.0])

        res = evaluate_regression(y_true, y_pred, num_features=2)
        assert res["mae"] == pytest.approx(0.0)
        assert res["mse"] == pytest.approx(0.0)
        assert res["rmse"] == pytest.approx(0.0)
        assert res["r2"] == pytest.approx(1.0)
        assert res["adjusted_r2"] == pytest.approx(1.0)

    def test_evaluate_cv_stability(self):
        X, y = make_classification(n_samples=100, n_features=4, random_state=42)
        model = LogisticRegression()
        cv_res = evaluate_cv_stability(model, X, y, cv=3)
        assert cv_res["folds"] == 3
        assert len(cv_res["fold_scores"]) == 3
        assert 0.0 <= cv_res["mean_score"] <= 1.0

    def test_compare_grid_vs_random_search(self):
        X, y = make_classification(n_samples=100, n_features=5, random_state=42)
        model = RandomForestClassifier(random_state=42)
        param_grid = {"n_estimators": [10, 20]}
        param_dist = {"n_estimators": [10, 20]}

        comp = compare_grid_vs_random_search(model, param_grid, param_dist, X, y, n_iter=2, cv=2)
        assert "grid_search" in comp
        assert "random_search" in comp
        assert comp["grid_search"]["best_score"] > 0

    def test_benchmark_classifiers(self):
        X, y = make_classification(n_samples=100, n_features=5, random_state=42)
        models = {
            "LogReg": LogisticRegression(),
            "RF": RandomForestClassifier(n_estimators=10, random_state=42)
        }
        df_bench = benchmark_classifiers(models, X[:80], y[:80], X[80:], y[80:])
        assert len(df_bench) == 2
        assert "Accuracy" in df_bench.columns
        assert "F1_Score" in df_bench.columns
        assert "Inference_Latency_us" in df_bench.columns
