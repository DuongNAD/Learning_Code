"""
Unit tests for 05_Deep_Learning_Basics algorithms (Perceptron, TwoLayerMLP Backprop).
"""

import numpy as np
import pytest
from perceptron_from_scratch import Perceptron
from mlp_backprop_numpy import TwoLayerMLP


class TestDeepLearningBasics:
    def test_perceptron_and_gate(self):
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y = np.array([0, 0, 0, 1])

        p = Perceptron(learning_rate=0.1, max_epochs=20)
        converged = p.fit(X, y)
        assert converged is True
        preds = p.predict(X)
        np.testing.assert_array_equal(preds, y)

    def test_perceptron_or_gate(self):
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y = np.array([0, 1, 1, 1])

        p = Perceptron(learning_rate=0.1, max_epochs=20)
        converged = p.fit(X, y)
        assert converged is True
        preds = p.predict(X)
        np.testing.assert_array_equal(preds, y)

    def test_perceptron_xor_linear_inseparability(self):
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y = np.array([0, 1, 1, 0])

        p = Perceptron(learning_rate=0.1, max_epochs=50)
        converged = p.fit(X, y)
        # Perceptron single layer CANNOT separate XOR
        assert converged is False
        preds = p.predict(X)
        assert not np.array_equal(preds, y)

    def test_two_layer_mlp_xor_convergence(self):
        X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y_xor = np.array([[0], [1], [1], [0]])

        mlp = TwoLayerMLP(input_dim=2, hidden_dim=4, output_dim=1, lr=3.0)
        mlp.fit(X_xor, y_xor, epochs=3000)

        preds = mlp.predict(X_xor)
        np.testing.assert_array_equal(preds, y_xor)
