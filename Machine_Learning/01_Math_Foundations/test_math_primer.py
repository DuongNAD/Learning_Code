"""
Unit tests for Machine Learning Math Primer (linear algebra, calculus, activations, losses).
"""

import numpy as np
import pytest
from math_primer import (
    dot_product,
    l2_norm,
    l1_norm,
    cosine_similarity,
    gradient_descent_step,
    stable_softmax,
    sigmoid,
    mse_loss,
    binary_cross_entropy
)


class TestMathPrimer:
    def test_dot_product(self):
        v1 = np.array([3.0, 4.0])
        v2 = np.array([1.0, 2.0])
        assert dot_product(v1, v2) == pytest.approx(11.0)

    def test_norms(self):
        v = np.array([3.0, 4.0])
        assert l2_norm(v) == pytest.approx(5.0)
        assert l1_norm(v) == pytest.approx(7.0)

    def test_cosine_similarity(self):
        v1 = np.array([1.0, 0.0])
        v2 = np.array([0.0, 1.0])
        # Orthogonal vectors -> cos = 0
        assert cosine_similarity(v1, v2) == pytest.approx(0.0)

        # Identical vectors -> cos = 1
        assert cosine_similarity(v1, v1) == pytest.approx(1.0)

        # Opposite vectors -> cos = -1
        assert cosine_similarity(v1, -v1) == pytest.approx(-1.0)

    def test_gradient_descent_convergence(self):
        w = 10.0
        lr = 0.1
        for _ in range(50):
            w, grad, loss = gradient_descent_step(w, lr)
        # Should converge to w* = 2.0
        assert w == pytest.approx(2.0, abs=1e-3)
        assert loss == pytest.approx(1.0, abs=1e-3)

    def test_stable_softmax_overflow_prevention(self):
        # Huge logits that would normally overflow exp()
        logits = np.array([1000.0, 1001.0, 1002.0])
        probs = stable_softmax(logits)
        assert not np.any(np.isnan(probs))
        assert not np.any(np.isinf(probs))
        assert np.sum(probs) == pytest.approx(1.0)
        assert probs[2] > probs[1] > probs[0]

    def test_sigmoid_bounds(self):
        assert sigmoid(0.0) == pytest.approx(0.5)
        assert sigmoid(100.0) == pytest.approx(1.0)
        assert sigmoid(-100.0) == pytest.approx(0.0)

    def test_mse_loss(self):
        y_true = np.array([1.0, 2.0, 3.0])
        y_pred = np.array([1.0, 2.0, 3.0])
        assert mse_loss(y_true, y_pred) == pytest.approx(0.0)

        y_pred2 = np.array([2.0, 3.0, 4.0])
        assert mse_loss(y_true, y_pred2) == pytest.approx(1.0)

    def test_binary_cross_entropy(self):
        y_true = np.array([1, 0])
        y_pred_perfect = np.array([0.9999, 0.0001])
        y_pred_bad = np.array([0.0001, 0.9999])
        loss_good = binary_cross_entropy(y_true, y_pred_perfect)
        loss_bad = binary_cross_entropy(y_true, y_pred_bad)
        assert loss_good < 0.01
        assert loss_bad > 5.0
