"""
IMLC 2026 Qualification Round (Senior Division) - Problem C Verification
Module: verify_problem_c_ridge.py

Focus:
    - Empirical data: (0, 1.0), (1, 3.2), (2, 4.8), (3, 7.0).
    - Exact evaluation of candidate models:
        * M1(x) = 0.2*x^3 - 0.9*x^2 + 2.9*x + 1.0 (RSS=0.0000, penalty=9.2600, J=9.2600)
        * M2(x) = 2.0*x + 1.0 (RSS=0.0800, penalty=4.0000, J=4.0800)
    - Closed-form Ridge regression w* = (X^T X + lambda I)^{-1} X^T y across lambda in [10^-4, 10^3].
    - Singular Value Decomposition (SVD) and spectral shrinkage factors f_i = sigma_i^2 / (sigma_i^2 + lambda).
    - Theoretical & empirical Bias-Variance tradeoff curve derivation.
    - Exact computation of critical phase transition threshold lambda* = 0.08 / 5.26 approx 0.015209.
"""

from __future__ import annotations
import math
from typing import Any, Dict, List, Tuple
import numpy as np


# =====================================================================
# 1. Canonical Dataset & Candidate Models
# =====================================================================

X_DATA = np.array([0.0, 1.0, 2.0, 3.0], dtype=np.float64)
Y_DATA = np.array([1.0, 3.2, 4.8, 7.0], dtype=np.float64)

# Model 1: Cubic Polynomial: y = 0.2*x^3 - 0.9*x^2 + 2.9*x + 1.0
# Coefficients [a0 (intercept), a1, a2, a3]
M1_COEFFS = np.array([1.0, 2.9, -0.9, 0.2], dtype=np.float64)

# Model 2: Linear Model: y = 2.0*x + 1.0
# Coefficients [a0 (intercept), a1, a2, a3]
M2_COEFFS = np.array([1.0, 2.0, 0.0, 0.0], dtype=np.float64)


# =====================================================================
# 2. Evaluation Functions: RSS, Complexity Penalty, and Score J
# =====================================================================

def evaluate_polynomial(x: np.ndarray, coeffs: np.ndarray) -> np.ndarray:
    """
    Evaluates polynomial y = sum_{k=0}^d coeffs[k] * x^k.
    """
    y_pred = np.zeros_like(x, dtype=np.float64)
    for k, a_k in enumerate(coeffs):
        y_pred += a_k * (x ** k)
    return y_pred


def compute_rss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Computes Residual Sum of Squares (RSS) = sum((y_i - y_hat_i)^2)."""
    residuals = y_true - y_pred
    return float(np.sum(residuals ** 2))


def compute_l2_penalty(coeffs: np.ndarray) -> float:
    """
    Computes Tikhonov L2 penalty over non-intercept coefficients:
        sum_{i >= 1} a_i^2
    """
    non_intercept = coeffs[1:]
    return float(np.sum(non_intercept ** 2))


def compute_score_j(y_true: np.ndarray, y_pred: np.ndarray, coeffs: np.ndarray, lambda_reg: float) -> float:
    """
    Computes regularized objective score J = RSS + lambda * sum_{i >= 1} a_i^2.
    """
    rss = compute_rss(y_true, y_pred)
    penalty = compute_l2_penalty(coeffs)
    return rss + lambda_reg * penalty


# =====================================================================
# 3. Closed-Form Ridge Regression Engine
# =====================================================================

def build_polynomial_design_matrix(x: np.ndarray, degree: int = 3, include_intercept: bool = True) -> np.ndarray:
    """Constructs Vandermonde design matrix for polynomial regression."""
    start = 0 if include_intercept else 1
    cols = [x ** k for k in range(start, degree + 1)]
    return np.column_stack(cols)


def solve_ridge_regression(X_full: np.ndarray, y: np.ndarray, lambda_reg: float) -> np.ndarray:
    """
    Solves closed-form Ridge regression with unpenalized intercept:
        w* = (X^T X + Lambda)^{-1} X^T y
    where Lambda = diag(0, lambda, lambda, ...).
    """
    n, p = X_full.shape
    penalty_diag = np.full(p, lambda_reg, dtype=np.float64)
    penalty_diag[0] = 0.0  # Do NOT regularize the intercept term
    Lambda_matrix = np.diag(penalty_diag)
    
    XtX = X_full.T @ X_full
    A = XtX + Lambda_matrix
    b = X_full.T @ y
    w_star = np.linalg.solve(A, b)
    return w_star


def compute_svd_spectral_shrinkage(X_centered: np.ndarray, lambdas: np.ndarray) -> Dict[str, Any]:
    """
    Computes SVD of centered feature matrix X_centered = U Sigma V^T,
    and derives the theoretical singular value shrinkage factors:
        f_i(lambda) = sigma_i^2 / (sigma_i^2 + lambda).
    """
    U, s, Vt = np.linalg.svd(X_centered, full_matrices=False)
    # s contains singular values sigma_1 >= sigma_2 >= ...
    shrinkage_factors = []
    for lam in lambdas:
        factors = (s ** 2) / ((s ** 2) + lam)
        shrinkage_factors.append(factors)
        
    return {
        "singular_values": s,
        "lambdas": lambdas,
        "shrinkage_factors": np.array(shrinkage_factors),
        "V": Vt.T,
        "U": U
    }


def compute_bias_variance_decomposition(X_centered: np.ndarray,
                                        w_true: np.ndarray,
                                        noise_variance: float,
                                        lambdas: np.ndarray) -> Dict[str, np.ndarray]:
    """
    Computes exact theoretical Bias^2 and Variance across regularization spectrum lambda:
        Bias(w*) = -lambda * (X^T X + lambda I)^{-1} w_true
        Var(w*)  = sigma^2 * Tr( (X^T X + lambda I)^{-1} X^T X (X^T X + lambda I)^{-1} )
    """
    p = X_centered.shape[1]
    XtX = X_centered.T @ X_centered
    I_p = np.eye(p)
    
    biases_sq = []
    variances = []
    total_mses = []
    
    for lam in lambdas:
        inv_A = np.linalg.inv(XtX + lam * I_p)
        # Bias vector
        bias_vec = -lam * (inv_A @ w_true)
        bias_sq = float(np.sum(bias_vec ** 2))
        
        # Covariance trace
        cov_matrix = noise_variance * (inv_A @ XtX @ inv_A)
        variance = float(np.trace(cov_matrix))
        
        biases_sq.append(bias_sq)
        variances.append(variance)
        total_mses.append(bias_sq + variance)
        
    return {
        "lambdas": lambdas,
        "bias_sq": np.array(biases_sq),
        "variance": np.array(variances),
        "expected_mse": np.array(total_mses)
    }


# =====================================================================
# 4. Critical Phase Transition Threshold Derivation
# =====================================================================

def compute_critical_threshold(rss1: float, pen1: float, rss2: float, pen2: float) -> float:
    """
    Solves J(M1, lambda*) = J(M2, lambda*):
        rss1 + lambda* * pen1 = rss2 + lambda* * pen2
        => lambda* = (rss2 - rss1) / (pen1 - pen2)
    """
    delta_rss = rss2 - rss1
    delta_pen = pen1 - pen2
    if delta_pen <= 0:
        raise ValueError("pen1 must be strictly greater than pen2 for a valid transition threshold.")
    return delta_rss / delta_pen


# =====================================================================
# 5. Master Verification Pipeline for Problem C
# =====================================================================

def verify_problem_c() -> Dict[str, Any]:
    """
    Executes the full formal verification pipeline for Problem C:
        1. Evaluates M1 predictions: asserts RSS=0.0000, penalty=9.2600, J=9.2600 at lambda=1.
        2. Evaluates M2 predictions: asserts RSS=0.0800, penalty=4.0000, J=4.0800 at lambda=1.
        3. Asserts J(M2) < J(M1) (4.0800 < 9.2600) -> M2 is chosen.
        4. Verifies critical threshold lambda* = 0.08 / 5.26 approx 0.015209.
        5. Computes closed-form Ridge spectrum over lambda in [10^-4, 10^3].
           - Asserts w*(lambda -> 0) converges to OLS polynomial solution M1.
           - Asserts w*(lambda -> infty) shrinks non-intercept coefficients to 0.
        6. Verifies SVD shrinkage factors f_i in (0, 1] and monotonic decrease with lambda.
        7. Verifies Bias-Variance monotonicity: Bias^2 strictly increases with lambda,
           Variance strictly decreases with lambda.
    """
    results: Dict[str, Any] = {}
    
    # -------------------------------------------------------------
    # Step 1: Evaluation of Model 1 (Cubic Polynomial)
    # -------------------------------------------------------------
    y_pred_m1 = evaluate_polynomial(X_DATA, M1_COEFFS)
    rss_m1 = compute_rss(Y_DATA, y_pred_m1)
    pen_m1 = compute_l2_penalty(M1_COEFFS)
    j_m1 = compute_score_j(Y_DATA, y_pred_m1, M1_COEFFS, lambda_reg=1.0)
    
    # Assertions for M1
    np.testing.assert_allclose(y_pred_m1, Y_DATA, atol=1e-12,
                               err_msg="M1 predictions must match target data exactly (interpolation)")
    assert math.isclose(rss_m1, 0.0000, abs_tol=1e-12), f"RSS(M1) must be 0.0, got {rss_m1}"
    assert math.isclose(pen_m1, 9.2600, abs_tol=1e-12), f"Penalty(M1) must be 9.26, got {pen_m1}"
    assert math.isclose(j_m1, 9.2600, abs_tol=1e-12), f"J(M1) must be 9.26, got {j_m1}"
    
    results["M1"] = {
        "predictions": y_pred_m1.tolist(),
        "residuals": (Y_DATA - y_pred_m1).tolist(),
        "rss": rss_m1,
        "penalty": pen_m1,
        "score_j": j_m1
    }
    
    # -------------------------------------------------------------
    # Step 2: Evaluation of Model 2 (Linear Model)
    # -------------------------------------------------------------
    y_pred_m2 = evaluate_polynomial(X_DATA, M2_COEFFS)
    residuals_m2 = Y_DATA - y_pred_m2
    expected_residuals_m2 = np.array([0.0, 0.2, -0.2, 0.0])
    np.testing.assert_allclose(residuals_m2, expected_residuals_m2, atol=1e-12,
                               err_msg="M2 residuals must be exactly [0.0, 0.2, -0.2, 0.0]")
    
    rss_m2 = compute_rss(Y_DATA, y_pred_m2)
    pen_m2 = compute_l2_penalty(M2_COEFFS)
    j_m2 = compute_score_j(Y_DATA, y_pred_m2, M2_COEFFS, lambda_reg=1.0)
    
    # Assertions for M2
    assert math.isclose(rss_m2, 0.0800, abs_tol=1e-12), f"RSS(M2) must be 0.08, got {rss_m2}"
    assert math.isclose(pen_m2, 4.0000, abs_tol=1e-12), f"Penalty(M2) must be 4.00, got {pen_m2}"
    assert math.isclose(j_m2, 4.0800, abs_tol=1e-12), f"J(M2) must be 4.08, got {j_m2}"
    
    results["M2"] = {
        "predictions": y_pred_m2.tolist(),
        "residuals": residuals_m2.tolist(),
        "rss": rss_m2,
        "penalty": pen_m2,
        "score_j": j_m2
    }
    
    # -------------------------------------------------------------
    # Step 3: Model Selection Decision at lambda = 1
    # -------------------------------------------------------------
    assert j_m2 < j_m1, f"Scoring rule must select M2 (got J(M2)={j_m2} >= J(M1)={j_m1})"
    results["selected_model_lambda_1"] = "Model 2 (Linear)"
    results["loss_gap"] = j_m1 - j_m2  # 9.26 - 4.08 = 5.18
    assert math.isclose(results["loss_gap"], 5.1800, abs_tol=1e-12)
    
    # -------------------------------------------------------------
    # Step 4: Critical Phase Transition Threshold
    # -------------------------------------------------------------
    lambda_star = compute_critical_threshold(rss_m1, pen_m1, rss_m2, pen_m2)
    expected_lambda_star = 0.08 / 5.26  # ~ 0.01520912547528517
    assert math.isclose(lambda_star, expected_lambda_star, rel_tol=1e-9), (
        f"Critical threshold must be {expected_lambda_star}, got {lambda_star}"
    )
    
    # Verify behavior on both sides of threshold
    eps = 1e-4
    j1_below = compute_score_j(Y_DATA, y_pred_m1, M1_COEFFS, lambda_reg=lambda_star - eps)
    j2_below = compute_score_j(Y_DATA, y_pred_m2, M2_COEFFS, lambda_reg=lambda_star - eps)
    assert j1_below < j2_below, "Below lambda*, M1 (cubic) must achieve lower score J"
    
    j1_above = compute_score_j(Y_DATA, y_pred_m1, M1_COEFFS, lambda_reg=lambda_star + eps)
    j2_above = compute_score_j(Y_DATA, y_pred_m2, M2_COEFFS, lambda_reg=lambda_star + eps)
    assert j2_above < j1_above, "Above lambda*, M2 (linear) must achieve lower score J"
    
    results["critical_threshold_lambda_star"] = lambda_star
    
    # -------------------------------------------------------------
    # Step 5: Closed-Form Ridge Regression across Spectrum
    # -------------------------------------------------------------
    X_poly = build_polynomial_design_matrix(X_DATA, degree=3, include_intercept=True)
    lambda_spectrum = np.logspace(-4, 3, 50)
    
    ridge_weights = []
    for lam in lambda_spectrum:
        w_lam = solve_ridge_regression(X_poly, Y_DATA, lam)
        ridge_weights.append(w_lam)
    ridge_weights = np.array(ridge_weights)
    
    # Check limit as lambda -> 0: converges to M1 (Lagrange interpolator)
    w_min = solve_ridge_regression(X_poly, Y_DATA, 1e-8)
    np.testing.assert_allclose(w_min, M1_COEFFS, atol=1e-5,
                               err_msg="Ridge solution at lambda -> 0 must converge to M1 OLS coefficients")
    
    # Check limit as lambda -> infinity: non-intercept weights vanish
    w_inf = solve_ridge_regression(X_poly, Y_DATA, 1e8)
    assert math.isclose(w_inf[0], np.mean(Y_DATA), abs_tol=1e-5), (
        f"At lambda -> infty, intercept must converge to y_mean={np.mean(Y_DATA)}, got {w_inf[0]}"
    )
    np.testing.assert_allclose(w_inf[1:], np.zeros(3), atol=1e-5,
                               err_msg="At lambda -> infty, non-intercept weights must converge to 0")
    
    results["ridge_spectrum"] = {
        "lambdas": lambda_spectrum.tolist(),
        "w_min_lambda": w_min.tolist(),
        "w_inf_lambda": w_inf.tolist()
    }
    
    # -------------------------------------------------------------
    # Step 6: SVD & Singular Value Spectral Shrinkage
    # -------------------------------------------------------------
    # Use centered design matrix for the 3 polynomial features
    X_features = build_polynomial_design_matrix(X_DATA, degree=3, include_intercept=False)
    X_centered = X_features - np.mean(X_features, axis=0)
    
    svd_res = compute_svd_spectral_shrinkage(X_centered, lambda_spectrum)
    singular_values = svd_res["singular_values"]
    shrinkage_factors = svd_res["shrinkage_factors"]  # Shape: (num_lambdas, num_features)
    
    # Verification: Each shrinkage factor f_i(lambda) in (0, 1]
    assert np.all(shrinkage_factors > 0.0) and np.all(shrinkage_factors <= 1.0)
    # Verification: Each f_i(lambda) strictly decreases as lambda increases
    diffs = np.diff(shrinkage_factors, axis=0)
    assert np.all(diffs < 0.0), "SVD shrinkage factors f_i must strictly decrease as lambda increases"
    
    results["svd"] = {
        "singular_values": singular_values.tolist(),
        "sample_shrinkage_at_lambda_1": shrinkage_factors[np.argmin(np.abs(lambda_spectrum - 1.0))].tolist()
    }
    
    # -------------------------------------------------------------
    # Step 7: Bias-Variance Decomposition Invariants
    # -------------------------------------------------------------
    w_true = M1_COEFFS[1:]  # True generative coefficients [2.9, -0.9, 0.2]
    noise_var = 0.05
    bv_res = compute_bias_variance_decomposition(X_centered, w_true, noise_var, lambda_spectrum)
    
    bias_sq = bv_res["bias_sq"]
    variance = bv_res["variance"]
    
    # Assert Bias^2 is monotonically increasing in lambda
    bias_diffs = np.diff(bias_sq)
    assert np.all(bias_diffs >= -1e-12), "Squared bias must be monotonically increasing in lambda"
    
    # Assert Variance is monotonically decreasing in lambda
    var_diffs = np.diff(variance)
    assert np.all(var_diffs <= 1e-12), "Variance must be monotonically decreasing in lambda"
    
    results["bias_variance"] = {
        "min_bias_sq": float(bias_sq[0]),
        "max_bias_sq": float(bias_sq[-1]),
        "max_variance": float(variance[0]),
        "min_variance": float(variance[-1]),
        "optimal_lambda_mse": float(lambda_spectrum[np.argmin(bv_res["expected_mse"])])
    }
    results["all_assertions_passed"] = True
    
    return results


# =====================================================================
# 6. Standalone CLI Output Formatter
# =====================================================================

def main() -> None:
    print("=" * 80)
    print(" IMLC 2026 QUALIFICATION ROUND - PROBLEM C VERIFICATION")
    print(" To Fit or Not to Fit: Ridge Regularization (L2) & Spectral Shrinkage")
    print("=" * 80)
    
    res = verify_problem_c()
    
    print("\n[1] Model 1 (Cubic Polynomial: y = 0.2x^3 - 0.9x^2 + 2.9x + 1.0):")
    m1 = res["M1"]
    print(f"    Predictions:  {m1['predictions']}")
    print(f"    Residuals:    {m1['residuals']}")
    print(f"    RSS(M1):      {m1['rss']:.4f} (Exact Interpolation)")
    print(f"    Penalty(M1):  {m1['penalty']:.4f}")
    print(f"    Score J(M1):  {m1['score_j']:.4f} (at lambda = 1)")
    
    print("\n[2] Model 2 (Linear Model: y = 2.0x + 1.0):")
    m2 = res["M2"]
    print(f"    Predictions:  {m2['predictions']}")
    print(f"    Residuals:    {m2['residuals']}")
    print(f"    RSS(M2):      {m2['rss']:.4f}")
    print(f"    Penalty(M2):  {m2['penalty']:.4f}")
    print(f"    Score J(M2):  {m2['score_j']:.4f} (at lambda = 1)")
    
    print("\n[3] Model Selection Decision (at lambda = 1.0):")
    print(f"    Selection:    {res['selected_model_lambda_1']}")
    print(f"    Delta Score:  J(M1) - J(M2) = {res['loss_gap']:.4f} > 0 => M2 is preferred")
    print("    Rationale:    Complexity penalty savings (5.26) heavily exceed residual error (0.08)")
    
    print("\n[4] Critical Phase Transition Threshold (lambda*):")
    lam_star = res["critical_threshold_lambda_star"]
    print(f"    lambda* = delta_RSS / delta_Penalty = 0.0800 / 5.2600 = {lam_star:.6f}")
    print(f"    - For lambda < {lam_star:.6f}: Model 1 (Cubic) is selected (fit dominates)")
    print(f"    - For lambda > {lam_star:.6f}: Model 2 (Linear) is selected (penalty dominates)")
    
    print("\n[5] SVD & Spectral Shrinkage Analysis:")
    svd = res["svd"]
    print(f"    Singular Values of Centered X: {svd['singular_values']}")
    print(f"    Spectral Shrinkage Factors at lambda=1.0: {svd['sample_shrinkage_at_lambda_1']}")
    
    print("\n[6] Bias-Variance Tradeoff Bounds:")
    bv = res["bias_variance"]
    print(f"    Squared Bias: [{bv['min_bias_sq']:.6f} -> {bv['max_bias_sq']:.6f}] (Monotonically Increasing)")
    print(f"    Variance:     [{bv['max_variance']:.6f} -> {bv['min_variance']:.6f}] (Monotonically Decreasing)")
    print(f"    Optimal Regularization lambda (MSE Minimizer): {bv['optimal_lambda_mse']:.6f}")
    
    print("\n" + "=" * 80)
    print(" [OK] Problem C Verification Suite: ALL ASSERTIONS PASSED (100%)")
    print("=" * 80)


def test_verify_problem_c() -> None:
    """Entry point for automated pytest discovery."""
    res = verify_problem_c()
    assert res["all_assertions_passed"] is True


if __name__ == "__main__":
    main()

