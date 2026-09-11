"""
Hyperparameter Tuning Suite
===========================
Comparison and diagnostic tools for optimization algorithms:
- GridSearchCV vs RandomizedSearchCV efficiency benchmark
- Overfitting / Underfitting diagnosis via Validation Curves
"""

import time
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, validation_curve


def compare_grid_vs_random_search(
    estimator,
    param_grid: dict,
    param_distributions: dict,
    X: np.ndarray,
    y: np.ndarray,
    n_iter: int = 10,
    cv: int = 3,
    scoring: str = "accuracy"
) -> dict:
    """
    Benchmarks GridSearchCV vs RandomizedSearchCV on the same model and parameter space.

    Returns:
        Dictionary comparing runtime, best parameters, and best cross-validation scores.
    """
    # 1. GridSearchCV
    t0 = time.time()
    grid = GridSearchCV(estimator, param_grid=param_grid, cv=cv, scoring=scoring, n_jobs=-1)
    grid.fit(X, y)
    grid_time = time.time() - t0

    # 2. RandomizedSearchCV
    t1 = time.time()
    rand = RandomizedSearchCV(
        estimator,
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=cv,
        scoring=scoring,
        random_state=42,
        n_jobs=-1
    )
    rand.fit(X, y)
    rand_time = time.time() - t1

    return {
        "grid_search": {
            "time_seconds": round(grid_time, 4),
            "best_score": round(float(grid.best_score_), 4),
            "best_params": grid.best_params_,
            "total_fits": len(grid.cv_results_["params"]) * cv
        },
        "random_search": {
            "time_seconds": round(rand_time, 4),
            "best_score": round(float(rand.best_score_), 4),
            "best_params": rand.best_params_,
            "total_fits": n_iter * cv
        },
        "speedup_factor": round(grid_time / max(rand_time, 1e-6), 2)
    }


def diagnose_validation_curve(
    estimator,
    X: np.ndarray,
    y: np.ndarray,
    param_name: str,
    param_range: list | np.ndarray,
    cv: int = 5,
    scoring: str = "accuracy"
) -> dict:
    """
    Calculates training and validation scores across a parameter range to diagnose overfitting.

    Returns:
        Dictionary containing param_range, train_mean, train_std, val_mean, val_std.
    """
    train_scores, test_scores = validation_curve(
        estimator,
        X,
        y,
        param_name=param_name,
        param_range=param_range,
        cv=cv,
        scoring=scoring,
        n_jobs=-1
    )

    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    return {
        "param_name": param_name,
        "param_range": [float(p) if isinstance(p, (int, float, np.number)) else str(p) for p in param_range],
        "train_mean": [float(round(m, 4)) for m in train_mean],
        "train_std": [float(round(s, 4)) for s in train_std],
        "validation_mean": [float(round(m, 4)) for m in test_mean],
        "validation_std": [float(round(s, 4)) for s in test_std],
    }
