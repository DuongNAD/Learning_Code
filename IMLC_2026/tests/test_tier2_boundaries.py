"""
IMLC 2026 E2E Test Suite - Tier 2: Boundary & Corner Cases
Tests mathematical boundary conditions, extreme limits, singular matrices,
and edge cases across Ridge regularization, RLHF drift, decision trees, and statistical metrics.

Requirements: Standard Library and numpy only.
"""

import math
import numpy as np
import pytest


# ==============================================================================
# Ridge Regularization Mathematical Boundary Conditions
# ==============================================================================
class TestTier2RidgeBoundaries:
    """Mathematical boundary conditions for Ridge / Tikhonov regularization."""

    def setup_method(self):
        # Problem C dataset: 4 points (0, 1), (1, 3.2), (2, 4.8), (3, 7.0)
        self.xs = np.array([0.0, 1.0, 2.0, 3.0])
        self.ys = np.array([1.0, 3.2, 4.8, 7.0])
        self.n = len(self.xs)

        # Vandermonde matrix for cubic model M1 (excluding intercept for penalty)
        self.X1 = np.column_stack([self.xs**3, self.xs**2, self.xs, np.ones(self.n)])
        # Design matrix for linear model M2
        self.X2 = np.column_stack([self.xs, np.ones(self.n)])

    def test_tier2_ridge_lambda_approaching_zero(self):
        """As lambda -> 0+, Ridge objective J(M) converges to pure OLS RSS."""
        # For M1: degree-3 polynomial interpolates 4 distinct points perfectly
        # Analytical M1 coefficients: [0.2, -0.9, 2.9, 1.0]
        y_hat_m1 = 0.2 * self.xs**3 - 0.9 * self.xs**2 + 2.9 * self.xs + 1.0
        rss_m1 = np.sum((self.ys - y_hat_m1) ** 2)
        pen_m1 = 0.2**2 + (-0.9)**2 + 2.9**2  # 9.26

        # For M2: linear model [2.0, 1.0]
        y_hat_m2 = 2.0 * self.xs + 1.0
        rss_m2 = np.sum((self.ys - y_hat_m2) ** 2)  # 0.08
        pen_m2 = 2.0**2  # 4.0

        # Critical crossover is lambda* = 0.08 / 5.26 ~ 0.01521.
        # Below lambda*, interpolating model M1 beats M2.
        for lam in [1e-3, 1e-6, 1e-9]:
            j_m1 = rss_m1 + lam * pen_m1
            j_m2 = rss_m2 + lam * pen_m2
            # As lambda -> 0, j_m1 -> 0.0 and j_m2 -> 0.08
            assert j_m1 < j_m2  # At lambda < lambda*, M1 beats M2
            assert math.isclose(j_m1, 0.0, abs_tol=lam * 10)
            assert math.isclose(j_m2, 0.08, abs_tol=lam * 10)

    def test_tier2_ridge_lambda_approaching_infinity(self):
        """As lambda -> infty, non-intercept weights shrink to 0, predictions collapse to mean."""
        y_mean = np.mean(self.ys)  # (1 + 3.2 + 4.8 + 7) / 4 = 4.0
        # Total Sum of Squares TSS
        tss = np.sum((self.ys - y_mean) ** 2)  # 9 + 0.64 + 0.64 + 9 = 19.28

        # Solve Ridge with intercept unpenalized
        # Center X and y to unpenalize intercept
        x_centered = (self.xs - np.mean(self.xs)).reshape(-1, 1)
        y_centered = self.ys - y_mean

        for lam in [1e2, 1e4, 1e8]:
            # w = (X_c^T X_c + lam I)^(-1) X_c^T y_c
            xtx = np.dot(x_centered.T, x_centered)
            w = float(np.dot(np.linalg.inv(xtx + lam * np.eye(1)), np.dot(x_centered.T, y_centered))[0])
            # Verify shrinkage towards 0
            assert abs(w) <= 10.0 / lam
            preds = w * x_centered.flatten() + y_mean
            rss = np.sum((self.ys - preds) ** 2)
            # RSS is bounded by TSS and converges to TSS = 19.28
            assert rss <= tss + 1e-6
            if lam >= 1e4:
                assert math.isclose(rss, tss, abs_tol=0.1)

    def test_tier2_ridge_singular_ill_conditioned_matrix(self):
        """Ridge regularizer (X^T X + lambda*I) remains invertible even when X is collinear/rank-deficient."""
        # Create collinear matrix: column 2 is exactly 2 * column 1
        x_col1 = np.array([1.0, 2.0, 3.0, 4.0])
        x_col2 = 2.0 * x_col1
        X_sing = np.column_stack([x_col1, x_col2])

        xtx = np.dot(X_sing.T, X_sing)
        # OLS matrix is singular (determinant ~ 0, cond -> inf)
        det_ols = np.linalg.det(xtx)
        assert math.isclose(det_ols, 0.0, abs_tol=1e-10)

        # Ridge regularized matrix for any lambda > 0 is invertible
        for lam in [1e-4, 1e-2, 1.0, 10.0]:
            reg_mat = xtx + lam * np.eye(2)
            cond = np.linalg.cond(reg_mat)
            assert not np.isinf(cond)
            assert not np.isnan(cond)
            inv_mat = np.linalg.inv(reg_mat)
            # Verify identity reconstruction
            identity_reconstructed = np.dot(reg_mat, inv_mat)
            assert np.allclose(identity_reconstructed, np.eye(2), atol=1e-6)

    def test_tier2_ridge_zero_variance_features(self):
        """Feature vector with zero variance (all identical values) has bounded regularized weight."""
        X_flat = np.array([[5.0], [5.0], [5.0], [5.0]])  # zero variance
        y = np.array([2.0, 4.0, 6.0, 8.0])
        lam = 1.0
        xtx = np.dot(X_flat.T, X_flat)  # 4 * 25 = 100
        xty = np.dot(X_flat.T, y)        # 5 * 20 = 100
        w = float(np.dot(np.linalg.inv(xtx + lam * np.eye(1)), xty)[0])
        # w = 100 / (100 + 1) = 100 / 101 ~ 0.9901
        assert math.isclose(w, 100.0 / 101.0, rel_tol=1e-6)
        assert np.isfinite(w)


# ==============================================================================
# RLHF Drift Loss Mathematical Boundary Conditions
# ==============================================================================
class TestTier2RLHFBoundaries:
    """Mathematical boundary conditions for RLHF policy drift loss L(t) = -r*t + beta*t^2."""

    def test_tier2_rlhf_beta_approaching_zero(self):
        """As beta -> 0+, optimal policy drift t* -> +infty (unbounded reward hacking)."""
        r = 2.0
        betas = [1e-1, 1e-2, 1e-4, 1e-6]
        t_stars = [r / (2.0 * b) for b in betas]

        # Verify strict monotonic divergence to infinity
        for i in range(len(t_stars) - 1):
            assert t_stars[i] < t_stars[i + 1]
        assert t_stars[-1] == 1e6  # 2 / (2 * 1e-6) = 1,000,000

        # Minimal loss L(t*) = -r^2 / (4*beta) diverges to -infty
        losses = [-r * t + b * t**2 for b, t in zip(betas, t_stars)]
        assert losses[-1] == -1e6

    def test_tier2_rlhf_beta_approaching_infinity(self):
        """As beta -> infty, optimal policy drift t* -> 0+ (frozen reference policy anchor)."""
        r = 5.0
        betas = [1e2, 1e4, 1e6, 1e8]
        t_stars = [r / (2.0 * b) for b in betas]

        # Verify strict monotonic convergence to 0
        for i in range(len(t_stars) - 1):
            assert t_stars[i] > t_stars[i + 1]
        assert math.isclose(t_stars[-1], 0.0, abs_tol=1e-7)

    def test_tier2_rlhf_reward_zero_boundary(self):
        """When reward r = 0, optimal policy drift is exactly 0."""
        r = 0.0
        for beta in [0.1, 1.0, 10.0, 100.0]:
            t_star = r / (2.0 * beta)
            assert t_star == 0.0
            loss = -r * t_star + beta * t_star**2
            assert loss == 0.0

    def test_tier2_rlhf_exact_safety_boundary(self):
        """Exact safety boundary condition: beta = r_max / (2*T) ensures t*(r) <= T."""
        r_max = 8.0
        T = 2.0
        beta_safe = r_max / (2.0 * T)  # 8 / 4 = 2.0

        # At beta = beta_safe, for all r in (0, r_max], t*(r) <= T
        r_grid = np.linspace(1e-4, r_max, 500)
        t_values = r_grid / (2.0 * beta_safe)
        assert np.all(t_values <= T)
        # Exact equality at r = r_max
        assert math.isclose(t_values[-1], T, rel_tol=1e-9)

        # For any beta < beta_safe, safety threshold T is strictly violated at r = r_max
        for delta in [1e-6, 1e-4, 1e-2]:
            beta_unsafe = beta_safe - delta
            t_max_unsafe = r_max / (2.0 * beta_unsafe)
            assert t_max_unsafe > T

    def test_tier2_rlhf_negative_reward_behavior(self):
        """When reward r < 0 (harmful action), optimal shift t* <= 0 (negative drift)."""
        r_neg = -3.0
        beta = 1.5
        t_star = r_neg / (2.0 * beta)  # -3 / 3 = -1.0
        assert t_star < 0.0
        # If policy drift is constrained to t >= 0 (e.g. Euclidean distance norm),
        # the boundary solution is t* = 0 with L(0) = 0.
        loss_at_zero = 0.0
        loss_at_positive = -r_neg * 1.0 + beta * (1.0**2)  # 3 + 1.5 = 4.5 > 0
        assert loss_at_zero < loss_at_positive


# ==============================================================================
# Decision Tree Boundary Conditions & Invariants
# ==============================================================================
class TestTier2DecisionTreeBoundaries:
    """Boundary conditions and information invariants for Decision Tree induction."""

    @staticmethod
    def tree_predict(t: float, h: float, c: float) -> str:
        """Augmented decision tree logic for greenhouse roof control."""
        if t > 28.0:
            return "OPEN"
        if h > 70.0:
            return "OPEN"
        if c > 1250.0:
            return "OPEN"
        return "KEEP CLOSED"

    def test_tier2_decision_tree_exact_threshold_boundary(self):
        """Test exact split boundaries: strict > vs <=."""
        # 1. Temperature boundary at 28.0 C
        # At T=28.0 exactly, condition t > 28 is False (does not trigger OPEN)
        assert self.tree_predict(t=28.0, h=60.0, c=800.0) == "KEEP CLOSED"
        # At T=28.0001, condition t > 28 is True (triggers OPEN)
        assert self.tree_predict(t=28.0001, h=60.0, c=800.0) == "OPEN"

        # 2. Humidity boundary at 70.0%
        assert self.tree_predict(t=25.0, h=70.0, c=800.0) == "KEEP CLOSED"
        assert self.tree_predict(t=25.0, h=70.0001, c=800.0) == "OPEN"

        # 3. CO2 boundary at 1250.0 ppm
        assert self.tree_predict(t=25.0, h=60.0, c=1250.0) == "KEEP CLOSED"
        assert self.tree_predict(t=25.0, h=60.0, c=1250.0001) == "OPEN"

    def test_tier2_decision_tree_extreme_sensor_values(self):
        """Test physical extremes of greenhouse sensors."""
        # Sub-zero arctic freeze (-40 C, 10% H, 350 ppm CO2)
        assert self.tree_predict(t=-40.0, h=10.0, c=350.0) == "KEEP CLOSED"

        # Extreme greenhouse heatwave (75 C, 20% H, 400 ppm CO2)
        assert self.tree_predict(t=75.0, h=20.0, c=400.0) == "OPEN"

        # Saturated steam humidity (22 C, 100% H, 500 ppm CO2)
        assert self.tree_predict(t=22.0, h=100.0, c=500.0) == "OPEN"

        # Toxic carbon dioxide accumulation (18 C, 40% H, 5000 ppm CO2)
        assert self.tree_predict(t=18.0, h=40.0, c=5000.0) == "OPEN"

        # Absolute dry vacuum boundary (0 C, 0% H, 0 ppm CO2)
        assert self.tree_predict(t=0.0, h=0.0, c=0.0) == "KEEP CLOSED"

    def test_tier2_decision_tree_pure_partition_entropy_gini_zero(self):
        """A pure node (homogeneous labels) has identically 0 entropy and 0 Gini impurity."""
        def entropy(p_list):
            return -sum(p * math.log2(p) for p in p_list if p > 0)

        def gini(p_list):
            return 1.0 - sum(p**2 for p in p_list)

        # 100% OPEN
        p_pure = [1.0, 0.0]
        assert entropy(p_pure) == 0.0
        assert gini(p_pure) == 0.0

        # 100% CLOSED
        p_closed = [0.0, 1.0]
        assert entropy(p_closed) == 0.0
        assert gini(p_closed) == 0.0

    def test_tier2_decision_tree_maximum_entropy_multiclass(self):
        """Uniform distribution achieves theoretical maximum entropy of log2(K) bits."""
        def entropy(k):
            p = 1.0 / k
            return -sum(p * math.log2(p) for _ in range(k))

        # Binary uniform (p=0.5, 0.5) -> H = 1.0 bit
        assert math.isclose(entropy(2), 1.0)

        # Ternary uniform (Problem A classes: speech, music, alarm) -> H = log2(3) ~ 1.58496 bits
        assert math.isclose(entropy(3), math.log2(3))

        # K=10 classes -> H = log2(10) ~ 3.3219 bits
        assert math.isclose(entropy(10), math.log2(10))


# ==============================================================================
# Statistical Metrics & Fairness Invariant Boundaries
# ==============================================================================
class TestTier2StatisticalBoundaries:
    """Boundary conditions for distribution shift metrics (PSI, KS) and algorithmic fairness."""

    def test_tier2_psi_identical_distributions_zero(self):
        """When actual distribution Q equals expected distribution P, PSI is identically 0.0."""
        p_dist = np.array([0.1, 0.2, 0.4, 0.2, 0.1])
        q_dist = np.array([0.1, 0.2, 0.4, 0.2, 0.1])

        # PSI = sum (Q_k - P_k) * ln(Q_k / P_k)
        psi = np.sum((q_dist - p_dist) * np.log(q_dist / p_dist))
        assert math.isclose(psi, 0.0, abs_tol=1e-12)

    def test_tier2_ks_test_identical_distributions_stat_zero(self):
        """Two-sample Kolmogorov-Smirnov test on identical empirical samples yields D = 0.0."""
        x1 = np.array([1.0, 2.5, 3.8, 4.2, 5.0, 6.7, 8.1])
        x2 = np.copy(x1)

        # Empirical CDF supremum distance D = sup |F1(x) - F2(x)|
        combined = np.sort(np.unique(np.concatenate([x1, x2])))
        cdf1 = np.searchsorted(np.sort(x1), combined, side="right") / len(x1)
        cdf2 = np.searchsorted(np.sort(x2), combined, side="right") / len(x2)
        d_stat = np.max(np.abs(cdf1 - cdf2))
        assert d_stat == 0.0

        # Completely disjoint samples yield D = 1.0
        x3 = x1 + 100.0  # min(x3) >> max(x1)
        combined_disjoint = np.sort(np.unique(np.concatenate([x1, x3])))
        cdf1_d = np.searchsorted(np.sort(x1), combined_disjoint, side="right") / len(x1)
        cdf3_d = np.searchsorted(np.sort(x3), combined_disjoint, side="right") / len(x3)
        d_stat_max = np.max(np.abs(cdf1_d - cdf3_d))
        assert math.isclose(d_stat_max, 1.0)

    def test_tier2_fairness_base_rate_disparity_invariants(self):
        """Kleinberg Impossibility: Demographic Parity and Predictive Parity cannot both hold if base rates differ."""
        # Group 0: 100 individuals, base rate p0 = 0.2 (20 positive)
        # Group 1: 100 individuals, base rate p1 = 0.8 (80 positive)
        # Suppose a classifier predicts positive with probability 0.5 for BOTH groups (Demographic Parity)
        # P(Y_hat = 1 | A=0) = 0.5, P(Y_hat = 1 | A=1) = 0.5
        # If perfectly calibrated (Predictive Parity: P(Y=1 | Y_hat=1) must equal precision)
        # For Group 0, at most 20 positives exist in total, so among 50 predicted positives,
        # Precision <= 20 / 50 = 0.40.
        # For Group 1, among 50 predicted positives, Precision can be up to 50 / 50 = 1.0 (or at least 30/50 = 0.60 if random).
        # Precision(Group 0) <= 0.40 < 0.60 <= Precision(Group 1).
        # Hence Predictive Parity is strictly impossible when base rates differ.
        base_rate_0 = 0.2
        base_rate_1 = 0.8
        max_precision_0 = base_rate_0 / 0.5  # 0.4
        min_precision_1 = (base_rate_1 - 0.5) / 0.5  # at least 0.6
        assert max_precision_0 < min_precision_1  # Mathematically proves impossibility
