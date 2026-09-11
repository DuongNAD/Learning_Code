"""
Model Evaluation Metrics Library
================================
Comprehensive suite for assessing machine learning models:
- Classification metrics: Accuracy, Balanced Accuracy, Precision, Recall, F1 (Macro/Weighted), ROC-AUC, PR-AUC, Confusion Matrix
- Regression metrics: MAE, MSE, RMSE, R², Adjusted R², MAPE, Max Error
- Decision threshold optimization: F1-maximization & Youden's J-statistic
- Cross-validation stability and variance analysis
"""

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    confusion_matrix,
    mean_squared_error,
    mean_absolute_error,
    r2_score,
)
from sklearn.model_selection import cross_val_score


def evaluate_classification(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: np.ndarray | None = None
) -> dict[str, float | list[list[int]]]:
    """
    Computes a comprehensive suite of classification metrics.

    Args:
        y_true: Ground truth binary or multiclass labels.
        y_pred: Predicted class labels.
        y_prob: Optional predicted probabilities for positive class (or per-class matrix).

    Returns:
        Dictionary of computed metric names and values.
    """
    y_t = np.asarray(y_true)
    y_p = np.asarray(y_pred)

    results = {
        "accuracy": float(accuracy_score(y_t, y_p)),
        "balanced_accuracy": float(balanced_accuracy_score(y_t, y_p)),
        "precision_macro": float(precision_score(y_t, y_p, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(y_t, y_p, average="macro", zero_division=0)),
        "f1_macro": float(f1_score(y_t, y_p, average="macro", zero_division=0)),
        "f1_weighted": float(f1_score(y_t, y_p, average="weighted", zero_division=0)),
        "confusion_matrix": confusion_matrix(y_t, y_p).tolist(),
    }

    # Binary-specific metrics if exactly 2 classes
    unique_classes = np.unique(y_t)
    if len(unique_classes) == 2:
        results["precision_binary"] = float(precision_score(y_t, y_p, zero_division=0))
        results["recall_binary"] = float(recall_score(y_t, y_p, zero_division=0))
        results["f1_binary"] = float(f1_score(y_t, y_p, zero_division=0))

    if y_prob is not None:
        try:
            results["roc_auc"] = float(roc_auc_score(y_t, y_prob))
            results["pr_auc"] = float(average_precision_score(y_t, y_prob))
        except ValueError:
            # Multi-class or single-class batch
            pass

    return results


def find_optimal_threshold(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    metric: str = "f1",
    thresholds: np.ndarray | None = None
) -> tuple[float, float]:
    """
    Finds optimal decision probability threshold for binary classification.

    Args:
        y_true: Ground truth binary labels (0 or 1).
        y_prob: Predicted probabilities for class 1.
        metric: Metric to maximize ('f1' or 'youden').
        thresholds: Array of candidate thresholds (default: 0.05 to 0.95 with step 0.01).

    Returns:
        Tuple of (optimal_threshold, best_metric_value).
    """
    y_t = np.asarray(y_true)
    probs = np.asarray(y_prob)

    if thresholds is None:
        thresholds = np.linspace(0.05, 0.95, 91)

    best_thresh = 0.5
    best_score = -1.0

    for t in thresholds:
        preds = (probs >= t).astype(int)
        if metric == "f1":
            score = f1_score(y_t, preds, zero_division=0)
        elif metric == "youden":
            # Youden's J = Sensitivity + Specificity - 1 = Recall - FPR
            cm = confusion_matrix(y_t, preds)
            tn, fp, fn, tp = cm.ravel()
            sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
            score = sensitivity + specificity - 1.0
        else:
            raise ValueError(f"Unsupported metric: {metric}")

        if score > best_score:
            best_score = score
            best_thresh = float(round(t, 4))

    return best_thresh, float(best_score)


def evaluate_regression(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    num_features: int | None = None
) -> dict[str, float]:
    """
    Computes regression evaluation metrics.

    Args:
        y_true: True continuous target values.
        y_pred: Predicted values.
        num_features: Number of features used in the model (for Adjusted R²).

    Returns:
        Dictionary of MAE, MSE, RMSE, R², Adjusted R², MAPE, Max Error.
    """
    y_t = np.asarray(y_true, dtype=float)
    y_p = np.asarray(y_pred, dtype=float)

    n = len(y_t)
    mae = mean_absolute_error(y_t, y_p)
    mse = mean_squared_error(y_t, y_p)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_t, y_p)
    max_err = float(np.max(np.abs(y_t - y_p)))

    # Mean Absolute Percentage Error (ignoring zeros to prevent div by zero)
    mask = y_t != 0
    mape = float(np.mean(np.abs((y_t[mask] - y_p[mask]) / y_t[mask])) * 100) if np.any(mask) else 0.0

    results = {
        "mae": float(mae),
        "mse": float(mse),
        "rmse": float(rmse),
        "r2": float(r2),
        "max_error": max_err,
        "mape_percent": mape
    }

    if num_features is not None:
        if n > (num_features + 1):
            adj_r2 = 1.0 - (1.0 - r2) * (n - 1) / (n - num_features - 1)
        else:
            adj_r2 = float(r2) if r2 == 1.0 else np.nan
        results["adjusted_r2"] = float(adj_r2)

    return results


def evaluate_cv_stability(
    estimator,
    X: np.ndarray,
    y: np.ndarray,
    cv: int = 5,
    scoring: str = "accuracy"
) -> dict[str, float | list[float]]:
    """
    Evaluates cross-validation performance and stability (mean and variance across folds).
    """
    scores = cross_val_score(estimator, X, y, cv=cv, scoring=scoring)
    return {
        "metric": scoring,
        "folds": cv,
        "fold_scores": [float(round(s, 4)) for s in scores],
        "mean_score": float(np.mean(scores)),
        "std_score": float(np.std(scores)),
        "min_score": float(np.min(scores)),
        "max_score": float(np.max(scores)),
    }


if __name__ == "__main__":
    # Quick Demonstration
    y_true_demo = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
    y_prob_demo = np.array([0.9, 0.2, 0.45, 0.8, 0.1, 0.6, 0.35, 0.15, 0.75, 0.4])
    y_pred_demo = (y_prob_demo >= 0.5).astype(int)

    print("=== DEMO: EVALUATION CLASSIFICATION ===")
    clf_res = evaluate_classification(y_true_demo, y_pred_demo, y_prob_demo)
    for k, v in clf_res.items():
        print(f" - {k:<20}: {v}")

    best_t, best_f1 = find_optimal_threshold(y_true_demo, y_prob_demo, metric="f1")
    print(f"\nOptimal threshold for F1: {best_t:.2f} (F1 = {best_f1:.4f})")
