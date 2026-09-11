"""
Model Benchmark Comparison Suite
================================
Trains and evaluates multiple candidate algorithms on a common dataset,
measuring accuracy, F1, training latency, and inference speed.
"""

import time
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score


def benchmark_classifiers(
    models: dict[str, any],
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray
) -> pd.DataFrame:
    """
    Benchmarks multiple classifiers side-by-side.

    Returns:
        DataFrame sorted by F1-Score descending.
    """
    records = []
    for name, model in models.items():
        # Measure training latency
        t0 = time.perf_counter()
        model.fit(X_train, y_train)
        fit_time_ms = (time.perf_counter() - t0) * 1000

        # Measure inference latency (single sample average)
        t1 = time.perf_counter()
        y_pred = model.predict(X_test)
        infer_latency_us = ((time.perf_counter() - t1) / len(X_test)) * 1_000_000

        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

        # ROC-AUC if predict_proba is supported
        roc = np.nan
        if hasattr(model, "predict_proba"):
            try:
                y_prob = model.predict_proba(X_test)[:, 1]
                roc = roc_auc_score(y_test, y_prob)
            except Exception:
                pass

        records.append({
            "Model": name,
            "Accuracy": round(acc, 4),
            "F1_Score": round(f1, 4),
            "ROC_AUC": round(roc, 4) if not np.isnan(roc) else "N/A",
            "Fit_Time_ms": round(fit_time_ms, 2),
            "Inference_Latency_us": round(infer_latency_us, 2)
        })

    df_res = pd.DataFrame(records).sort_values(by="F1_Score", ascending=False).reset_index(drop=True)
    return df_res


if __name__ == "__main__":
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split

    X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

    benchmark_models = {
        "Logistic Regression": LogisticRegression(random_state=42),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=50, random_state=42),
        "SVM (RBF)": SVC(probability=True, random_state=42),
        "KNN (k=5)": KNeighborsClassifier(n_neighbors=5)
    }

    df_benchmark = benchmark_classifiers(benchmark_models, X_tr, y_tr, X_te, y_te)
    print("=== MODEL BENCHMARK COMPARISON MATRIX ===")
    print(df_benchmark.to_string(index=False))
