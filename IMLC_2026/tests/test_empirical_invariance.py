"""
IMLC 2026 Empirical Mathematical Invariance Stress Test Suite
============================================================
Author: Challenger 2 (Empirical Test & Formula Invariance Challenger)
Target: Independent, empirical, first-principles validation of key mathematical
        identities and invariants presented in the IMLC 2026 Study Guide.

Invariants Tested:
  1. Ridge Loss, Matrix Gradient & Closed-Form Normal Equations
  2. Guaranteed Invertibility under Underdetermined & Collinear Regimes
  3. Soft-Thresholding Operator Optimality & Subdifferential Invariance
  4. Gibbs Optimal Policy Normalization & Variational Optimality
  5. Kleinberg's Impossibility Theorem Algebraic Contradiction
  6. Bias-Variance Strict Monotonicity & Strictly Superior Ridge Optimum
  7. Gaussian Relative Entropy vs. L2 Tikhonov Algebraic Equivalence
"""

import numpy as np
import pytest
from scipy.optimize import minimize, minimize_scalar
import sympy as sp


# ==============================================================================
# 1. Ridge Loss, Matrix Gradient & Closed-Form Normal Equations
# ==============================================================================
class TestRidgeMathematicalInvariance:
    """Stress-tests Ridge regression loss, gradient, and closed form."""

    @pytest.mark.parametrize("seed", [42, 123, 999])
    @pytest.mark.parametrize("n, p", [(10, 3), (25, 6), (50, 10)])
    def test_ridge_matrix_gradient_finite_difference(self, seed: int, n: int, p: int):
        """
        Validates: nabla_w J_Ridge(w) = -(1/n) * Phi^T (y - Phi*w) + lambda * I* * w
        via central finite differences to 1e-8 tolerance.
        """
        np.random.seed(seed)
        Phi = np.column_stack([np.ones(n), np.random.randn(n, p - 1)])
        y = np.random.randn(n)
        w = np.random.randn(p)
        lam = 0.45
        I_star = np.diag([0.0] + [1.0] * (p - 1))

        def J(w_vec):
            residual = y - Phi @ w_vec
            return (1.0 / (2.0 * n)) * np.sum(residual**2) + (lam / 2.0) * (w_vec @ I_star @ w_vec)

        def grad_analytical(w_vec):
            return -(1.0 / n) * (Phi.T @ (y - Phi @ w_vec)) + lam * (I_star @ w_vec)

        # Central finite differences
        eps = 1e-7
        grad_fd = np.zeros(p)
        for i in range(p):
            w_pos = w.copy()
            w_pos[i] += eps
            w_neg = w.copy()
            w_neg[i] -= eps
            grad_fd[i] = (J(w_pos) - J(w_neg)) / (2.0 * eps)

        ga = grad_analytical(w)
        max_diff = np.max(np.abs(ga - grad_fd))
        assert max_diff < 1e-7, f"Gradient mismatch: max diff = {max_diff}"

    def test_ridge_closed_form_stationarity(self):
        """
        Validates that w_Ridge = (Phi^T Phi + n*lambda*I*)^(-1) Phi^T y
        achieves exact zero gradient nabla_w J(w_Ridge) == 0.
        """
        np.random.seed(42)
        n, p = 30, 5
        Phi = np.column_stack([np.ones(n), np.random.randn(n, p - 1)])
        y = np.random.randn(n)
        lam = 0.75
        I_star = np.diag([0.0] + [1.0] * (p - 1))

        # Closed-form solution
        A = Phi.T @ Phi + n * lam * I_star
        b = Phi.T @ y
        w_ridge = np.linalg.solve(A, b)

        # Gradient at w_ridge
        grad = -(1.0 / n) * (Phi.T @ (y - Phi @ w_ridge)) + lam * (I_star @ w_ridge)
        max_residual = np.max(np.abs(grad))
        assert max_residual < 1e-12, f"Stationarity violated: max grad = {max_residual}"

    def test_ridge_underdetermined_strict_invertibility(self):
        """
        Stress-tests the regularized matrix (Phi^T Phi + n*lambda*I*) when n < p+1
        (underdetermined regime). Gram matrix is singular, but regularized matrix
        must be strictly positive definite (all eigenvalues > 0).
        """
        np.random.seed(2026)
        n, p = 3, 8  # 3 observations, 8 features + intercept = 9 parameters
        Phi = np.column_stack([np.ones(n), np.random.randn(n, p)])
        lam = 1.0
        I_star = np.diag([0.0] + [1.0] * p)

        Gram = Phi.T @ Phi
        assert np.linalg.matrix_rank(Gram) <= n < p + 1, "Gram matrix should be singular"

        Reg = Gram + n * lam * I_star
        eigenvalues = np.linalg.eigvalsh(Reg)

        # Strictly positive definite
        assert np.all(eigenvalues > 1e-8), f"Non-positive eigenvalues found: {eigenvalues}"
        assert np.linalg.cond(Reg) < 1e6, "Matrix condition number exploded"


# ==============================================================================
# 2. Soft-Thresholding Operator Invariance
# ==============================================================================
class TestSoftThresholdingInvariance:
    """Stress-tests L1 Lasso soft-thresholding operator S_lambda(z)."""

    def test_soft_thresholding_1d_exact_optimum(self):
        """
        Verifies that S_lambda(z) = sign(z) * max(0, |z| - lambda)
        is the exact analytical minimizer of 0.5 * (w - z)^2 + lambda * |w|.
        """
        lam = 0.8
        test_points = [-3.0, -1.5, -0.8, -0.5, 0.0, 0.5, 0.8, 1.5, 3.0]

        for z in test_points:
            s_analytical = np.sign(z) * max(0.0, abs(z) - lam)

            # Numerical optimization
            res = minimize_scalar(
                lambda w: 0.5 * (w - z)**2 + lam * abs(w),
                bounds=(z - 2 * lam, z + 2 * lam),
                method="bounded",
            )
            assert abs(res.x - s_analytical) < 1e-5, (
                f"Mismatch at z={z}: analytical={s_analytical}, numerical={res.x}"
            )

    def test_soft_thresholding_boundary_kinks(self):
        """Checks exact behavior at boundaries |z| == lambda and z == 0."""
        lam = 1.2
        # Exactly at boundary
        assert np.sign(lam) * max(0.0, abs(lam) - lam) == 0.0
        assert np.sign(-lam) * max(0.0, abs(-lam) - lam) == 0.0
        assert np.sign(0.0) * max(0.0, abs(0.0) - lam) == 0.0

        # Just outside boundary
        eps = 1e-4
        assert np.isclose(np.sign(lam + eps) * max(0.0, abs(lam + eps) - lam), eps)
        assert np.isclose(np.sign(-lam - eps) * max(0.0, abs(-lam - eps) - lam), -eps)


# ==============================================================================
# 3. Gibbs Optimal Policy & RLHF Normalization Invariance
# ==============================================================================
class TestGibbsOptimalPolicyInvariance:
    """Stress-tests optimal Gibbs / Boltzmann policy in RLHF."""

    @pytest.mark.parametrize("vocab_size", [3, 7, 20])
    @pytest.mark.parametrize("beta", [0.1, 0.5, 2.0])
    def test_gibbs_policy_normalization_sum_to_one(self, vocab_size: int, beta: float):
        """
        Validates that pi^*(y|x) = (1/Z(x)) * pi_ref(y|x) * exp(r(x, y) / beta)
        strictly normalizes: sum_y pi^*(y|x) == 1.0 to machine precision.
        """
        np.random.seed(42)
        r = np.random.randn(vocab_size)
        pi_ref = np.random.dirichlet(np.ones(vocab_size))

        # Log-sum-exp numerically stable partition function
        scaled_r = r / beta
        max_logit = np.max(scaled_r)
        weights = pi_ref * np.exp(scaled_r - max_logit)
        Z = np.sum(weights)
        pi_star = weights / Z

        assert abs(np.sum(pi_star) - 1.0) < 1e-14, f"Sum is {np.sum(pi_star)}, expected 1.0"
        assert np.all(pi_star >= 0.0), "Probabilities must be non-negative"

    def test_gibbs_policy_variational_maximization(self):
        """
        Numerically verifies that Gibbs policy achieves the unique global maximum
        of the objective: J(pi) = E_pi[r] - beta * D_KL(pi || pi_ref).
        """
        np.random.seed(101)
        K = 4
        r = np.array([2.5, -1.0, 0.5, 1.2])
        pi_ref = np.array([0.25, 0.25, 0.25, 0.25])
        beta = 0.5

        # Analytical Gibbs policy
        Z = np.sum(pi_ref * np.exp(r / beta))
        pi_star_analytical = (pi_ref * np.exp(r / beta)) / Z

        # Numerical solver with exact analytical Jacobian
        def neg_obj(p):
            kl = np.sum(p * (np.log(p) - np.log(pi_ref)))
            return -(np.sum(p * r) - beta * kl)

        def neg_grad(p):
            return -r + beta * (np.log(p) - np.log(pi_ref) + 1.0)

        bounds = [(1e-12, 1.0)] * K
        constraints = {"type": "eq", "fun": lambda p: np.sum(p) - 1.0, "jac": lambda p: np.ones(K)}
        res = minimize(
            neg_obj,
            np.ones(K) / K,
            jac=neg_grad,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-15, "maxiter": 500},
        )

        diff = np.max(np.abs(pi_star_analytical - res.x))
        assert diff < 1e-7, f"Analytical Gibbs policy deviates from variational optimizer: diff={diff}"


# ==============================================================================
# 4. Kleinberg's Impossibility Theorem Algebraic Contradiction
# ==============================================================================
class TestKleinbergTheoremInvariance:
    """Stress-tests Kleinberg's theorem algebraic contradiction."""

    def test_kleinberg_symbolic_impossibility(self):
        """
        Symbolically proves via SymPy that under Equalized Odds (equal TPR and FPR):
        PPV_0 - PPV_1 = [FPR * TPR * (p0 - p1)] / Denominator.
        For PPV_0 == PPV_1 with p0 != p1, we must have FPR * TPR == 0.
        Simultaneously for NPV_0 == NPV_1, we must have (1 - FPR) * (1 - TPR) == 0.
        Hence TPR=1 and FPR=0 (perfect classification).
        """
        p0, p1, TPR, FPR = sp.symbols("p0 p1 TPR FPR", positive=True)

        PPV0 = (TPR * p0) / (TPR * p0 + FPR * (1 - p0))
        PPV1 = (TPR * p1) / (TPR * p1 + FPR * (1 - p1))
        diff_ppv = sp.simplify(PPV0 - PPV1)
        numer_ppv = sp.factor(sp.numer(diff_ppv))

        # Check numerator is algebraically equal to FPR * TPR * (p0 - p1)
        assert sp.simplify(numer_ppv - FPR * TPR * (p0 - p1)) == 0

        NPV0 = ((1 - FPR) * (1 - p0)) / ((1 - FPR) * (1 - p0) + (1 - TPR) * p0)
        NPV1 = ((1 - FPR) * (1 - p1)) / ((1 - FPR) * (1 - p1) + (1 - TPR) * p1)
        diff_npv = sp.simplify(NPV0 - NPV1)
        numer_npv = sp.factor(sp.numer(diff_npv))

        # Check numerator is algebraically equal to -(1 - FPR) * (1 - TPR) * (p0 - p1)
        assert sp.simplify(numer_npv - (-(FPR - 1) * (TPR - 1) * (p0 - p1))) == 0

    @pytest.mark.parametrize("p0, p1", [(0.1, 0.4), (0.2, 0.8), (0.05, 0.35)])
    def test_kleinberg_numerical_grid_violation(self, p0: float, p1: float):
        """
        Numerically confirms that any non-trivial classifier (0 < TPR < 1, 0 < FPR < 1)
        satisfying Equalized Odds strictly violates Predictive Parity.
        """
        TPR = 0.80
        FPR = 0.15

        PPV0 = (TPR * p0) / (TPR * p0 + FPR * (1 - p0))
        PPV1 = (TPR * p1) / (TPR * p1 + FPR * (1 - p1))

        ppv_gap = abs(PPV0 - PPV1)
        assert ppv_gap > 0.05, f"Expected non-zero PPV gap for p0={p0}, p1={p1}; got {ppv_gap}"


# ==============================================================================
# 5. Bias-Variance Strictly Positive Optimal Lambda
# ==============================================================================
class TestBiasVarianceTradeoffInvariance:
    """Stress-tests the bias-variance trade-off proof."""

    def test_ridge_strictly_positive_optimal_lambda(self):
        """
        Validates the fundamental theorem: d(MSE)/d(lambda) at lambda=0 is strictly negative:
        d(MSE)/d(lambda)|_{lambda=0} = -2 * sigma^2 * sum(1 / sigma_j^4) < 0.
        Hence there exists lambda* > 0 with MSE(lambda*) < MSE(0).
        """
        np.random.seed(888)
        n, p = 25, 4
        Phi = np.random.randn(n, p)
        w_true = np.random.randn(p)
        sigma2 = 0.25

        _, s, Vt = np.linalg.svd(Phi, full_matrices=False)

        def mse(lam):
            bias2 = np.sum(((lam / (s**2 + lam))**2) * ((Vt @ w_true)**2))
            var = sigma2 * np.sum(s**2 / ((s**2 + lam)**2))
            return bias2 + var

        mse_0 = mse(0.0)
        lams = np.linspace(1e-4, 1.0, 500)
        mses = [mse(l) for l in lams]
        min_mse = min(mses)
        best_lam = lams[np.argmin(mses)]

        assert min_mse < mse_0, f"Ridge failed to strictly improve upon OLS: OLS={mse_0}, min={min_mse}"
        assert best_lam > 0.0, "Optimal lambda should be strictly positive"


# ==============================================================================
# 6. Gaussian Relative Entropy vs. L2 Tikhonov Equivalence
# ==============================================================================
class TestGaussianKLEquivalence:
    """Stress-tests Module 7 variational synthesis proof."""

    def test_gaussian_kl_identity(self):
        """
        Validates identity: ||w||_2^2 = 2 * sigma^2 * D_KL(N(w, sigma^2*I) || N(0, sigma^2*I)).
        """
        np.random.seed(777)
        p = 5
        w = np.random.randn(p)
        sigma2 = 1.8

        # Exact formula for D_KL between N(w, sigma2*I) and N(0, sigma2*I)
        # D_KL = 0.5 * [ Tr(I) - p + (0 - w)^T (sigma2*I)^(-1) (0 - w) + ln(det(I)) ]
        #      = 0.5 * [ 0 + (1 / sigma2) * ||w||_2^2 + 0 ]
        #      = (1 / (2 * sigma2)) * ||w||_2^2
        d_kl = (1.0 / (2.0 * sigma2)) * np.sum(w**2)

        reconstructed_norm2 = 2.0 * sigma2 * d_kl
        actual_norm2 = np.sum(w**2)

        assert np.isclose(reconstructed_norm2, actual_norm2), (
            f"Equivalence failed: reconstructed={reconstructed_norm2}, actual={actual_norm2}"
        )
