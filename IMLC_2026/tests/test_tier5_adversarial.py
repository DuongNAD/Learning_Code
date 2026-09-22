"""
IMLC 2026 E2E Test Suite - Tier 5: Adversarial Coverage Hardening
Stress-tests mathematical solutions and Python implementations against extreme numerical,
physical, and theoretical boundaries.

Target Modules:
    - imlc_2026_research/code/verify_problem_b_tree.py
    - imlc_2026_research/code/verify_problem_c_ridge.py
    - imlc_2026_research/code/verify_problem_d_rlhf.py

Test Scope:
    1. High-condition number, perfect collinearity, and near-singular matrices in Ridge regression.
    2. Floating-point perturbations and crossover stability around critical threshold lambda* = 0.08 / 5.26.
    3. Non-convexity, negative rewards, ultra-small beta, and massive reward scaling in RLHF drift.
    4. Exact decision boundaries (CO2 = 1250 ppm), physical sensor outliers, zero-variance subsets,
       and invariance under strictly monotonic feature transformations in Decision Trees.
    5. Gibbs distribution numerical stability (log-sum-exp trick under large positive/negative logits).

Dependencies: Standard Library, numpy, and pytest only.
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple
import numpy as np
import pytest

# Ensure code directory is in sys.path for direct imports
TESTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TESTS_DIR.parent
CODE_DIR = PROJECT_ROOT / "code"
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import verify_problem_b_tree as prob_b
import verify_problem_c_ridge as prob_c
import verify_problem_d_rlhf as prob_d


# ==============================================================================
# 1. Ridge Regression: Conditioning & Near-Singular Inversion
# ==============================================================================
class TestTier5RidgeAdversarialConditioning:
    """Stress-tests Ridge regression under pathological matrix conditions."""

    def test_tier5_ridge_perfect_collinearity_and_rank_deficiency(self):
        """
        Adversarial Scenario: Design matrix contains identical and collinear feature columns.
        Unregularized OLS is singular (det ~ 0, cond -> inf).
        Ridge regularization (lambda > 0) guarantees strict positive-definiteness and stable inversion.
        """
        # 4 samples, 4 columns: intercept, x, 2*x (perfect collinearity), and zero-variance dummy
        x_base = np.array([0.0, 1.0, 2.0, 3.0], dtype=np.float64)
        y = np.array([1.0, 3.2, 4.8, 7.0], dtype=np.float64)

        X_collinear = np.column_stack([
            np.ones(4),         # Intercept
            x_base,             # Feature 1
            2.0 * x_base,       # Feature 2 (Collinear: 2 * Feature 1)
            x_base ** 2         # Feature 3
        ])

        XtX = X_collinear.T @ X_collinear
        det_ols = float(np.linalg.det(XtX))
        cond_ols = float(np.linalg.cond(XtX))

        # Assert unregularized OLS is degenerate
        assert abs(det_ols) < 1e-10 or cond_ols > 1e12

        # Verify Ridge regularization for lambda in [1e-6, 1.0, 1e6]
        for lam in [1e-6, 1.0, 1e6]:
            w_ridge = prob_c.solve_ridge_regression(X_collinear, y, lambda_reg=lam)
            assert not np.any(np.isnan(w_ridge)), f"Ridge produced NaN weights at lambda={lam}"
            assert not np.any(np.isinf(w_ridge)), f"Ridge produced Inf weights at lambda={lam}"

            # Verify normal equation reconstruction: (X^T X + Lambda) w = X^T y
            lambda_diag = np.diag([0.0, lam, lam, lam])
            A = XtX + lambda_diag
            b = X_collinear.T @ y
            lhs = A @ w_ridge
            np.testing.assert_allclose(lhs, b, rtol=1e-5, atol=1e-5,
                                       err_msg=f"Normal equations failed at lambda={lam}")

    def test_tier5_ridge_ultra_low_regularization_lambda_1e12(self):
        """
        Adversarial Scenario: lambda -> 1e-12 on Vandermonde cubic matrix.
        Validates that solve_ridge_regression does not suffer from catastrophic cancellation
        and converges smoothly to the interpolating polynomial M1.
        """
        X_poly = prob_c.build_polynomial_design_matrix(prob_c.X_DATA, degree=3, include_intercept=True)
        w_ultra_low = prob_c.solve_ridge_regression(X_poly, prob_c.Y_DATA, lambda_reg=1e-12)

        # Must match M1 polynomial coefficients within floating-point tolerance
        np.testing.assert_allclose(w_ultra_low, prob_c.M1_COEFFS, atol=1e-4,
                                   err_msg="At lambda=1e-12, weights must converge to M1 OLS coefficients")

        # Predictions must perfectly interpolate empirical data
        y_pred = X_poly @ w_ultra_low
        np.testing.assert_allclose(y_pred, prob_c.Y_DATA, atol=1e-4)

    def test_tier5_ridge_ultra_high_regularization_lambda_1e12(self):
        """
        Adversarial Scenario: lambda -> 1e12 (infinite regularization limit).
        All non-intercept coefficients must shrink to zero (< 1e-10),
        and the unpenalized intercept must equal sample mean y_bar = 4.0.
        """
        X_poly = prob_c.build_polynomial_design_matrix(prob_c.X_DATA, degree=3, include_intercept=True)
        w_ultra_high = prob_c.solve_ridge_regression(X_poly, prob_c.Y_DATA, lambda_reg=1e12)

        y_mean = float(np.mean(prob_c.Y_DATA))  # 4.0
        assert math.isclose(w_ultra_high[0], y_mean, abs_tol=1e-8), (
            f"Intercept must converge to mean {y_mean}, got {w_ultra_high[0]}"
        )
        np.testing.assert_allclose(w_ultra_high[1:], np.zeros(3), atol=1e-9,
                                   err_msg="Non-intercept weights must be strictly zero at lambda=1e12")

    def test_tier5_ridge_spectral_condition_number_decay(self):
        """
        Verifies condition number kappa(X^T X + lambda I) is strictly monotonically decreasing
        as lambda ranges from 1e-4 to 1e6, asymptotically reaching 1.0 (perfectly conditioned).
        """
        X_features = prob_c.build_polynomial_design_matrix(prob_c.X_DATA, degree=3, include_intercept=False)
        X_centered = X_features - np.mean(X_features, axis=0)
        XtX = X_centered.T @ X_centered

        lambdas = np.logspace(-4, 6, 20)
        conds = [float(np.linalg.cond(XtX + lam * np.eye(3))) for lam in lambdas]

        diffs = np.diff(conds)
        assert np.all(diffs < 0.0), "Ridge regularized matrix condition number must strictly decrease with lambda"
        assert conds[0] > 1000.0, f"Initial condition number should be large, got {conds[0]}"
        assert conds[-1] < 1.01, f"Final condition number must asymptote to 1.0, got {conds[-1]}"

    def test_tier5_ridge_svd_shrinkage_monotonicity_under_extreme_spectrum(self):
        """
        Verifies singular value shrinkage factors f_i(lambda) = sigma_i^2 / (sigma_i^2 + lambda)
        across extreme range lambda in [1e-10, 1e15].
        Asserts bounds in (0, 1] and strictly decreasing behavior.
        """
        X_features = prob_c.build_polynomial_design_matrix(prob_c.X_DATA, degree=3, include_intercept=False)
        X_centered = X_features - np.mean(X_features, axis=0)

        lambdas = np.logspace(-10, 15, 26)
        res = prob_c.compute_svd_spectral_shrinkage(X_centered, lambdas)
        factors = res["shrinkage_factors"]

        assert np.all(factors > 0.0) and np.all(factors <= 1.0)
        diffs = np.diff(factors, axis=0)
        assert np.all(diffs < 0.0), "SVD shrinkage factors must strictly decrease over resolvable range"
        # At lambda = 1e-10, factors are extremely close to 1.0
        assert np.all(factors[0] > 0.999999)
        # At lambda = 1e15, factors vanish below 1e-12
        assert np.all(factors[-1] < 1e-12)


# ==============================================================================
# 2. Ridge Regression: Phase Transition Floating-Point Perturbations
# ==============================================================================
class TestTier5RidgePhaseTransitionPerturbations:
    """Stress-tests the critical phase transition threshold lambda* = 0.08 / 5.26."""

    def setup_method(self):
        self.y_pred_m1 = prob_c.evaluate_polynomial(prob_c.X_DATA, prob_c.M1_COEFFS)
        self.y_pred_m2 = prob_c.evaluate_polynomial(prob_c.X_DATA, prob_c.M2_COEFFS)
        self.lambda_star = 0.08 / 5.26  # ~ 0.01520912547528517

    def test_tier5_ridge_exact_crossover_equality(self):
        """
        At lambda* = 0.08 / 5.26, theoretical scores J(M1) and J(M2) are exactly identical.
        Asserts absolute difference is bounded by floating-point machine precision (<= 1e-15).
        """
        j1 = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m1, prob_c.M1_COEFFS, self.lambda_star)
        j2 = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m2, prob_c.M2_COEFFS, self.lambda_star)

        # Theoretical common score: 9.26 * (0.08 / 5.26) = 0.7408 / 5.26 ~ 0.1408365019...
        expected_score = 0.08 * (9.26 / 5.26)
        assert math.isclose(j1, expected_score, rel_tol=1e-12)
        assert math.isclose(j2, expected_score, rel_tol=1e-12)
        assert abs(j1 - j2) <= 1e-15, f"At exact threshold, |J1 - J2| must be <= 1e-15, got {abs(j1 - j2)}"

    def test_tier5_ridge_micro_perturbations_around_threshold(self):
        """
        Tests micro-perturbations delta = 1e-8 around lambda*.
        Verifies score difference strictly follows delta * (pen1 - pen2) = 5.26 * 1e-8.
        """
        delta = 1e-8
        j1_sub = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m1, prob_c.M1_COEFFS, self.lambda_star - delta)
        j2_sub = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m2, prob_c.M2_COEFFS, self.lambda_star - delta)
        assert j1_sub < j2_sub
        assert math.isclose(j2_sub - j1_sub, delta * 5.26, rel_tol=1e-6)

        j1_sup = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m1, prob_c.M1_COEFFS, self.lambda_star + delta)
        j2_sup = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m2, prob_c.M2_COEFFS, self.lambda_star + delta)
        assert j2_sup < j1_sup
        assert math.isclose(j1_sup - j2_sup, delta * 5.26, rel_tol=1e-6)

    def test_tier5_ridge_sub_nano_perturbations_approaching_precision_limit(self):
        """
        Tests extreme perturbation delta = 1e-12 (near IEEE 754 float64 limit).
        Verifies that model selection inequality still strictly holds.
        """
        delta = 1e-12
        j1_below = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m1, prob_c.M1_COEFFS, self.lambda_star - delta)
        j2_below = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m2, prob_c.M2_COEFFS, self.lambda_star - delta)
        assert j1_below < j2_below, "Below lambda*, M1 must win even at 1e-12 delta"

        j1_above = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m1, prob_c.M1_COEFFS, self.lambda_star + delta)
        j2_above = prob_c.compute_score_j(prob_c.Y_DATA, self.y_pred_m2, prob_c.M2_COEFFS, self.lambda_star + delta)
        assert j2_above < j1_above, "Above lambda*, M2 must win even at 1e-12 delta"

    def test_tier5_ridge_invalid_penalty_difference_exception(self):
        """
        Verifies compute_critical_threshold raises ValueError when pen1 <= pen2
        (violating the fundamental condition that M1 must be more complex than M2).
        """
        # Equal penalty
        with pytest.raises(ValueError, match="pen1 must be strictly greater than pen2"):
            prob_c.compute_critical_threshold(rss1=0.0, pen1=4.0, rss2=0.08, pen2=4.0)

        # Inverted penalty
        with pytest.raises(ValueError, match="pen1 must be strictly greater than pen2"):
            prob_c.compute_critical_threshold(rss1=0.0, pen1=2.0, rss2=0.08, pen2=9.0)

    def test_tier5_ridge_bias_variance_invariants_under_extreme_noise(self):
        """
        Verifies that in Bias-Variance decomposition:
        1. Squared Bias is strictly invariant to noise variance sigma^2.
        2. Variance scales strictly linearly with noise variance sigma^2.
        """
        X_features = prob_c.build_polynomial_design_matrix(prob_c.X_DATA, degree=3, include_intercept=False)
        X_centered = X_features - np.mean(X_features, axis=0)
        w_true = prob_c.M1_COEFFS[1:]
        lambdas = np.array([0.01, 1.0, 100.0])

        res_noise1 = prob_c.compute_bias_variance_decomposition(X_centered, w_true, noise_variance=1.0, lambdas=lambdas)
        res_noise100 = prob_c.compute_bias_variance_decomposition(X_centered, w_true, noise_variance=100.0, lambdas=lambdas)

        # Bias^2 must be independent of noise
        np.testing.assert_allclose(res_noise1["bias_sq"], res_noise100["bias_sq"], rtol=1e-12)
        # Variance must scale exactly by 100x
        np.testing.assert_allclose(res_noise1["variance"] * 100.0, res_noise100["variance"], rtol=1e-12)


# ==============================================================================
# 3. RLHF Policy Drift: Extreme Values & Strict Convexity
# ==============================================================================
class TestTier5RLHFAdversarialRegimes:
    """Stress-tests RLHF drift loss under extreme and adversarial parameters."""

    def test_tier5_rlhf_negative_reward_penalty_drift(self):
        """
        Adversarial Scenario: Negative reward r < 0 (toxic / penalized outputs).
        Optimal drift is negative: t* = r / (2*beta) < 0 (policy shifts away from penalized behavior).
        Loss L(t*) = -r^2 / (4*beta) remains negative.
        Strict convexity holds because d^2L/dt^2 = 2*beta > 0.
        """
        r_neg = -12.0
        beta = 3.0
        t_star = prob_d.analytical_optimal_drift(r_neg, beta)
        l_star = prob_d.analytical_minimal_loss(r_neg, beta)

        assert t_star == -2.0, f"Expected t*=-2.0, got {t_star}"
        assert l_star == -12.0, f"Expected L(t*)=-12.0, got {l_star}"

        # Numerical optimizer verification with negative search bounds
        t_num, l_num = prob_d.numerical_optimize_drift(r_neg, beta, t_bounds=(-10.0, 0.0))
        assert math.isclose(t_num, t_star, abs_tol=1e-5)
        assert math.isclose(l_num, l_star, abs_tol=1e-5)

        # Strict convexity verification
        assert 2.0 * beta > 0.0

    def test_tier5_rlhf_ultra_small_beta_reward_hacking(self):
        """
        Adversarial Scenario: beta -> 1e-9 (unconstrained policy drift / catastrophic reward hacking).
        Optimal drift t* grows to astronomical values (> 1e9).
        """
        r = 4.0
        beta_tiny = 1e-9
        t_star = prob_d.analytical_optimal_drift(r, beta_tiny)
        l_star = prob_d.analytical_minimal_loss(r, beta_tiny)

        assert math.isclose(t_star, 2e9, rel_tol=1e-9)
        assert math.isclose(l_star, -4e9, rel_tol=1e-9)
        # Loss must be lower than any moderate shift
        assert l_star < prob_d.rlhf_drift_loss(100.0, r, beta_tiny)

    def test_tier5_rlhf_extreme_massive_reward_scaling(self):
        """
        Adversarial Scenario: Massive reward scale r_max = 1e7 with tight safety bound T = 0.02.
        Critical boundary beta_crit = 1e7 / (2 * 0.02) = 2.5e8.
        Verifies safety theorem holds at scale:
            - Sub-critical beta violates T.
            - Critical beta attains exactly T.
            - Super-critical beta guarantees 0 violations.
        """
        r_max = 1e7
        T_limit = 0.02
        expected_beta_crit = 2.5e8

        res = prob_d.verify_safety_bound(r_max=r_max, T=T_limit, num_samples=5000)
        assert math.isclose(res["beta_critical"], expected_beta_crit, rel_tol=1e-12)
        assert res["sub_critical"]["violates"] is True
        assert res["sub_critical"]["violations_count"] > 0
        assert res["critical"]["exact_bound_achieved"] is True
        assert res["super_critical"]["safe"] is True
        assert res["super_critical"]["violations_count"] == 0

    def test_tier5_rlhf_invalid_beta_exception_handling(self):
        """
        Verifies analytical_optimal_drift and analytical_minimal_loss strictly reject
        non-positive beta <= 0 (where loss becomes unbounded below / concave).
        """
        for bad_beta in [0.0, -0.01, -100.0]:
            with pytest.raises(ValueError, match="beta must be strictly positive"):
                prob_d.analytical_optimal_drift(r=1.0, beta=bad_beta)

            with pytest.raises(ValueError, match="beta must be strictly positive"):
                prob_d.analytical_minimal_loss(r=1.0, beta=bad_beta)

    def test_tier5_rlhf_golden_section_robustness_across_scales(self):
        """
        Tests numerical_optimize_drift against analytical formula across 6 orders
        of magnitude in (r, beta) using adaptive search bounds.
        """
        test_pairs = [
            (1e-3, 1e-1),   # Small r, moderate beta -> t* = 0.005
            (1e2, 1e-1),    # Large r, small beta -> t* = 500
            (1e-2, 1e1),    # Small r, large beta -> t* = 0.0005
            (50.0, 2.5),    # Typical RLHF range -> t* = 10.0
        ]

        for r, beta in test_pairs:
            t_ana = prob_d.analytical_optimal_drift(r, beta)
            # Use search interval bracket [0, 3 * t_ana]
            t_num, l_num = prob_d.numerical_optimize_drift(r, beta, t_bounds=(0.0, 3.0 * t_ana), num_steps=120)
            assert math.isclose(t_num, t_ana, rel_tol=1e-4), f"Failed for r={r}, beta={beta}"


# ==============================================================================
# 4. Decision Tree: Pathological Sensor Values & Monotonic Invariance
# ==============================================================================
class TestTier5DecisionTreeAdversarial:
    """Stress-tests Decision Tree logic under boundary, outlier, and transformed sensor data."""

    def setup_method(self):
        self.tree = prob_b.build_refined_tree(co2_threshold=1250.0)

    def test_tier5_tree_exact_threshold_boundary_co2_1250(self):
        """
        Adversarial Scenario: CO2 sensor reports exactly 1250.0 ppm.
        Because split condition is strictly '>' (CO2 > 1250.0), CO2=1250.0 must evaluate
        to False -> KEEP CLOSED.
        A microscopic increase to 1250.000001 must flip decision to OPEN.
        """
        # Exactly 1250.0 ppm at T=24 C, H=55% (Rows 5-6 conditions)
        sample_exact = {"temperature": 24.0, "humidity": 55.0, "co2": 1250.0}
        assert self.tree.predict(sample_exact) == "KEEP CLOSED"

        # Epsilon above threshold
        sample_above = {"temperature": 24.0, "humidity": 55.0, "co2": 1250.000001}
        assert self.tree.predict(sample_above) == "OPEN"

        # Epsilon below threshold
        sample_below = {"temperature": 24.0, "humidity": 55.0, "co2": 1249.999999}
        assert self.tree.predict(sample_below) == "KEEP CLOSED"

    def test_tier5_tree_extreme_sensor_outliers(self):
        """
        Adversarial Scenario: Physically anomalous / malfunctioning sensor readings.
        Tree must evaluate deterministically without crash or infinite recursion.
        """
        # Outlier 1: Wildfire / extreme temperature (500 C)
        outlier_fire = {"temperature": 500.0, "humidity": -20.0, "co2": -500.0}
        assert self.tree.predict(outlier_fire) == "OPEN"

        # Outlier 2: Deep freeze (-273.15 C), negative humidity, near zero CO2
        outlier_freeze = {"temperature": -273.15, "humidity": -100.0, "co2": 1.0}
        assert self.tree.predict(outlier_freeze) == "KEEP CLOSED"

        # Outlier 3: Industrial CO2 leak (10,000,000 ppm) with freezing temp
        outlier_leak = {"temperature": -50.0, "humidity": 10.0, "co2": 1e7}
        assert self.tree.predict(outlier_leak) == "OPEN"

    def test_tier5_tree_zero_variance_feature_subset(self):
        """
        Adversarial Scenario: Sub-dataset where all CO2 values are identical.
        evaluate_co2_splits must detect no distinct consecutive values and return empty candidate list.
        """
        zero_var_subset = [
            {"row": 1, "co2": 1200.0, "action": "OPEN"},
            {"row": 2, "co2": 1200.0, "action": "KEEP CLOSED"},
            {"row": 3, "co2": 1200.0, "action": "OPEN"},
        ]
        candidates = prob_b.evaluate_co2_splits(zero_var_subset)
        assert len(candidates) == 0, f"Expected 0 candidate splits for identical feature values, got {len(candidates)}"

    def test_tier5_tree_zero_variance_labels_pure_entropy(self):
        """
        Verifies shannon_entropy and gini_impurity handle degenerate distributions:
        - Empty list -> 0.0
        - Homogeneous single-class list -> 0.0
        - Single element -> 0.0
        """
        assert prob_b.shannon_entropy([]) == 0.0
        assert prob_b.gini_impurity([]) == 0.0

        pure_labels = ["OPEN"] * 50
        assert prob_b.shannon_entropy(pure_labels) == 0.0
        assert prob_b.gini_impurity(pure_labels) == 0.0

        single = ["KEEP CLOSED"]
        assert prob_b.shannon_entropy(single) == 0.0
        assert prob_b.gini_impurity(single) == 0.0

    def test_tier5_tree_missing_feature_key_error(self):
        """
        Verifies predict raises KeyError when an evaluated node encounters a missing feature key.
        """
        sample_missing_co2 = {"temperature": 24.0, "humidity": 55.0}  # Reaches CO2 node
        with pytest.raises(KeyError, match="Sample missing required feature: 'co2'"):
            self.tree.predict(sample_missing_co2)

        sample_missing_temp = {"humidity": 55.0, "co2": 800.0}  # Fails at root
        with pytest.raises(KeyError, match="Sample missing required feature: 'temperature'"):
            self.tree.predict(sample_missing_temp)

    def test_tier5_tree_invariance_under_monotonic_transformations(self):
        """
        Theorem: Decision tree split optimization (Information Gain & Gini Gain)
        is strictly invariant under order-preserving (monotonic increasing) feature transformations.
        Tests 3 transformations on CO2:
            1. Logarithmic: g(x) = ln(x)
            2. Affine: g(x) = 17.5 * x - 250.0
            3. Polynomial: g(x) = (x / 1000.0)^3
        Asserts that in all cases, the optimal split achieves IG = 1.0 bit, Gini Gain = 0.5,
        and isolates the exact same partition of observations.
        """
        sub_dataset = [s for s in prob_b.CANONICAL_LOGGED_OBSERVATIONS if s["row"] in (3, 4, 5, 6)]

        transformations = [
            ("Logarithmic", lambda x: math.log(x)),
            ("Affine", lambda x: 17.5 * x - 250.0),
            ("Cubic", lambda x: (x / 1000.0) ** 3),
        ]

        for name, trans in transformations:
            transformed_sub = [
                {"row": s["row"], "co2": trans(s["co2"]), "action": s["action"]}
                for s in sub_dataset
            ]
            candidates = prob_b.evaluate_co2_splits(transformed_sub)
            assert len(candidates) == 3, f"Expected 3 candidate splits under {name}, got {len(candidates)}"

            best_split = max(candidates, key=lambda c: c["information_gain"])
            assert math.isclose(best_split["information_gain"], 1.0, abs_tol=1e-9), (
                f"Information gain under {name} must be 1.0, got {best_split['information_gain']}"
            )
            assert math.isclose(best_split["gini_gain"], 0.5, abs_tol=1e-9), (
                f"Gini gain under {name} must be 0.5, got {best_split['gini_gain']}"
            )
            assert best_split["is_pure"] is True, f"Split under {name} must be 100% pure"


# ==============================================================================
# 5. Gibbs Distribution & Softmax Numerical Stability
# ==============================================================================
class TestTier5GibbsNumericalStability:
    """Stress-tests Gibbs policy and softmax numerical stability against logit overflow."""

    def test_tier5_gibbs_softmax_extreme_large_logits_logsumexp_trick(self):
        """
        Adversarial Scenario: Logits with massive base offset (1e12).
        Naive softmax (exp(x) / sum(exp(x))) overflows to inf / inf = NaN.
        The stable max-subtraction softmax implementation must remain numerically stable,
        sum to 1.0, and preserve exact relative odds.
        """
        large_logits = np.array([1e12, 1e12 + 1.0, 1e12 - 2.0, 1e12 + 3.0], dtype=np.float64)

        # Naive calculation fails with overflow
        with np.errstate(over="ignore", invalid="ignore"):
            naive_exp = np.exp(large_logits)
            naive_probs = naive_exp / np.sum(naive_exp)
            assert np.isnan(naive_probs).all(), "Naive softmax must overflow to NaN"

        # Stable softmax succeeds
        probs = prob_d.softmax(large_logits)
        assert not np.any(np.isnan(probs))
        assert not np.any(np.isinf(probs))
        assert math.isclose(float(np.sum(probs)), 1.0, abs_tol=1e-12)

        # Verify odds ratio: P(index 3) / P(index 0) = exp(3.0 - 0.0) = exp(3)
        expected_ratio = math.exp(3.0)
        actual_ratio = probs[3] / probs[0]
        assert math.isclose(actual_ratio, expected_ratio, rel_tol=1e-9)

    def test_tier5_gibbs_softmax_extreme_large_negative_logits(self):
        """
        Adversarial Scenario: Logits with large negative offset (-1e12).
        Verifies softmax handles underflow cleanly and assigns mass to the relative maximum.
        """
        neg_logits = np.array([-1e12, -1e12 - 5.0, -1e12 + 2.0], dtype=np.float64)
        probs = prob_d.softmax(neg_logits)

        assert not np.any(np.isnan(probs))
        assert math.isclose(float(np.sum(probs)), 1.0, abs_tol=1e-12)
        # Index 2 has highest relative logit (-1e12 + 2.0 vs -1e12 and -1e12 - 5.0)
        assert probs[2] > 0.88

    def test_tier5_gibbs_kl_divergence_clipped_boundary_safety(self):
        """
        Verifies compute_kl_divergence handles degenerate / one-hot distributions
        where components are 0.0 without triggering log(0) = -inf or NaN.
        """
        p_degenerate = np.array([1.0, 0.0, 0.0], dtype=np.float64)
        q_degenerate = np.array([0.0, 1.0, 0.0], dtype=np.float64)

        kl = prob_d.compute_kl_divergence(p_degenerate, q_degenerate)
        assert not np.isnan(kl)
        assert not np.isinf(kl)
        assert kl >= 0.0

        # Uniform vs uniform -> 0.0
        q_uniform = np.ones(3) / 3.0
        kl_identity = prob_d.compute_kl_divergence(q_uniform, q_uniform)
        assert math.isclose(kl_identity, 0.0, abs_tol=1e-12)

    def test_tier5_gibbs_policy_argmax_convergence_at_low_beta(self):
        """
        Verifies that as beta -> 1e-3 in Gibbs distribution pi*(y) proportional to pi_ref(y) * exp(r(y)/beta),
        the policy deterministically concentrates all probability mass (P -> 1.0) on the token
        with maximum reward (argmax policy).
        """
        vocab_size = 8
        rewards = np.array([1.0, 2.0, 3.5, 1.2, 0.8, 5.0, 2.1, 3.0])  # Index 5 has max reward = 5.0
        pi_ref = np.ones(vocab_size) / vocab_size

        beta_low = 1e-3
        unnorm_log = np.log(pi_ref + 1e-15) + (rewards / beta_low)
        pi_star = prob_d.softmax(unnorm_log)

        max_idx = int(np.argmax(rewards))
        assert max_idx == 5
        assert math.isclose(pi_star[max_idx], 1.0, abs_tol=1e-6), (
            f"Expected argmax token to receive probability 1.0, got {pi_star[max_idx]}"
        )
        assert np.sum(pi_star) == 1.0
