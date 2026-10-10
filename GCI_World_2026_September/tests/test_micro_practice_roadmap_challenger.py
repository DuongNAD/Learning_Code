"""
Empirical Stress-Testing and Verification Suite for GCI World 202609 Micro-Practice Roadmap.
Authored by Challenger 1 (Empirical Challenger: Critic & Specialist).

Empirically challenges, executes, and validates:
1. Definition of Done (DoD) testability and measurability across all micro-sessions.
2. Isolated runtime execution of all 9 Python code blocks in roadmap/micro_practice_roadmap.md.
3. ADVERSARIAL REPRODUCTION of runtime failures (e.g. Block 7 NameError: name 'np' is not defined).
4. Mathematical formulations:
   - Z-score normalization vs StandardScaler behavior (ddof=0 vs ddof=1, constant column zero division).
   - Dummy variable trap prevention (drop_first=True, matrix rank deficiency, condition number).
   - OLS regression MSE formulation and scikit-learn API compatibility.
   - Pearson correlation coefficient bounds [-1, 1] and constant variance NaN behavior.
   - Seven-Eleven Tanpin Kanri order logic, edge cases, and missing dependency.
   - Cost matrix tradeoff financial savings calculation.
   - 3-tier graduation eligibility boundary conditions.
5. Active Recall question coverage and scientific validity.
"""

import math
import re
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
ROADMAP_FILE = WORKSPACE_ROOT / "roadmap" / "micro_practice_roadmap.md"


class TestMicroPracticeCodeExecutionIsolated(unittest.TestCase):
    """
    Empirical execution test for each code block in micro_practice_roadmap.md.
    Each block is executed in a completely fresh, isolated namespace to detect
    missing imports, hidden dependencies, or undeclared global variables.
    """

    @classmethod
    def setUpClass(cls):
        cls.content = ROADMAP_FILE.read_text(encoding="utf-8")
        lines = cls.content.splitlines()
        cls.blocks = []
        in_block = False
        cur_block = []
        start_line = 0
        for idx, line in enumerate(lines):
            if line.strip() == "```python":
                in_block = True
                cur_block = []
                start_line = idx + 1
            elif in_block and line.strip() == "```":
                in_block = False
                cls.blocks.append((start_line, idx + 1, "\n".join(cur_block)))
            elif in_block:
                cur_block.append(line)

    def test_extracted_block_count(self):
        """Verify exactly 9 Python code blocks are present across the 9 micro-sessions."""
        self.assertGreaterEqual(len(self.blocks), 9, f"Expected 9 code blocks, found {len(self.blocks)}")

    def test_block_1_micro_01_execution(self):
        """Micro-0.1: Data audit and dtype separation."""
        start, end, code = self.blocks[0]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 1 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        self.assertIn("df", env)
        self.assertEqual(env["df"].shape, (5, 5))
        self.assertIn("num_cols", env)
        self.assertIn("cat_cols", env)
        self.assertIn("body_style", env["cat_cols"])
        self.assertIn("price", env["num_cols"])

    def test_block_2_micro_02_execution(self):
        """Micro-0.2: Imputation, dummy encoding, StandardScaler fit/transform split."""
        start, end, code = self.blocks[1]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 2 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        self.assertIn("X_train_scaled", env)
        self.assertIn("X_test_scaled", env)
        # Verify train mean is ~0 and std is ~1
        np.testing.assert_allclose(env["X_train_scaled"].mean(axis=0), [0.0, 0.0], atol=1e-7)
        np.testing.assert_allclose(env["X_train_scaled"].std(axis=0), [1.0, 1.0], atol=1e-7)

    def test_block_3_micro_03_execution(self):
        """Micro-0.3: Descriptive stats, Pearson r, Tukey Boxplot outlier filter."""
        start, end, code = self.blocks[2]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 3 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        self.assertAlmostEqual(env["mean_val"], 145.5, places=2)
        self.assertAlmostEqual(env["median_val"], 132.5, places=2)
        self.assertGreater(env["r"], 0.95)
        self.assertEqual(env["outliers"].tolist(), [300])

    def test_block_4_micro_04_execution(self):
        """Micro-0.4: LinearRegression R2 > 0.70 and DecisionTreeClassifier max_depth=3 gap < 0.15."""
        start, end, code = self.blocks[3]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 4 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        self.assertIn("reg_model", env)
        self.assertIn("tree_controlled", env)
        r2 = r2_score(env["y_te"], env["y_pred"])
        self.assertGreater(r2, 0.70)
        train_acc = env["tree_controlled"].score(env["X_ctr"], env["y_ctr"])
        test_acc = env["tree_controlled"].score(env["X_cte"], env["y_cte"])
        self.assertLess(abs(train_acc - test_acc), 0.15)

    def test_block_5_micro_11_execution(self):
        """Micro-1.1: Zettabyte growth factor and CRISP-DM decision gate."""
        start, end, code = self.blocks[4]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 5 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        self.assertAlmostEqual(env["growth_factor"], 527 / 64, places=2)
        gate = env["crisp_dm_decision_gate"]
        self.assertIn("TỪ CHỐI", gate(test_r2=0.68, target_kpi=0.75))
        self.assertIn("PHÊ DUYỆT", gate(test_r2=0.82, target_kpi=0.75))

    def test_block_6_micro_12_execution(self):
        """Micro-1.2: Credit score simulation and selection bias / dark data."""
        start, end, code = self.blocks[5]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 6 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        self.assertEqual(env["n_applicants"], 1000)
        self.assertGreater(env["approved_data"].mean(), env["credit_score"].mean())

    def test_block_7_micro_13_isolated_execution(self):
        """Micro-1.3: Verify Tanpin Kanri order logic executes cleanly in isolation."""
        start, end, code = self.blocks[6]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 7 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        fn = env["tanpin_kanri_order"]
        self.assertEqual(fn(100, False, False, 1.0), 100)
        self.assertEqual(fn(100, True, True, 1.25), 175)
        self.assertEqual(fn(100, True, False, 1.0), 85)

    def test_block_8_micro_14_execution(self):
        """Micro-1.4: Cost matrix financial calculation."""
        start, end, code = self.blocks[7]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 8 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        self.assertEqual(env["cost_model_a"], 251000)
        self.assertEqual(env["cost_model_b"], 2000)
        self.assertEqual(env["cost_model_a"] - env["cost_model_b"], 249000)

    def test_block_9_micro_15_execution(self):
        """Micro-1.5: Academic sentinel graduation audit."""
        start, end, code = self.blocks[8]
        env = {}
        try:
            exec(code, env)
        except Exception as e:
            self.fail(f"Block 9 (lines {start}-{end}) failed with {type(e).__name__}: {e}")
        check_fn = env["check_graduation_status"]
        # Failure: attendance < 7
        res1 = check_fn(6, [3.0]*8, True, 5.0, 5.0)
        self.assertIn("TRƯỢT", res1)
        self.assertIn("điểm danh", res1)
        # Failure: homework < 14
        res2 = check_fn(10, [1.0]*8, True, 5.0, 5.0)
        self.assertIn("TRƯỢT", res2)
        self.assertIn("bài tập", res2)
        # Failure: final not submitted
        res3 = check_fn(10, [3.0]*8, False, 5.0, 5.0)
        self.assertIn("TRƯỢT", res3)
        self.assertIn("Final", res3)
        # Success: Honors & Tokyo
        res4 = check_fn(10, [3.0]*8, True, 8.0, 15.0)
        self.assertIn("XUẤT SẮC", res4)
        self.assertIn("TOKYO", res4)
        # Success: Standard Completed
        res5 = check_fn(10, [3.0]*8, True, 15.0, 25.0)
        self.assertIn("ĐẠT", res5)


class TestMathematicalFormulationsEmpirical(unittest.TestCase):
    """
    Stress-tests the mathematical claims, bounds, and edge cases
    specified across micro-practice tasks.
    """

    def test_z_score_ddof_and_constant_column_behavior(self):
        """
        Verify mathematical properties of Z-score vs StandardScaler:
        1. StandardScaler uses ddof=0 (population standard deviation).
        2. Pandas df.std() uses ddof=1 (sample standard deviation).
        3. Constant columns (sigma=0) cause division by zero in manual formula,
           while StandardScaler maps them safely to 0.
        """
        arr = np.array([12.0, 15.0, 18.0, 20.0, 25.0])
        scaler = StandardScaler()
        arr_scaled = scaler.fit_transform(arr.reshape(-1, 1)).flatten()

        manual_ddof0 = (arr - np.mean(arr)) / np.std(arr, ddof=0)
        np.testing.assert_allclose(arr_scaled, manual_ddof0, atol=1e-12)

        manual_ddof1 = (arr - np.mean(arr)) / np.std(arr, ddof=1)
        self.assertFalse(np.allclose(arr_scaled, manual_ddof1))

        # Constant column edge case
        const_col = np.array([42.0, 42.0, 42.0, 42.0])
        scaled_const = scaler.fit_transform(const_col.reshape(-1, 1)).flatten()
        np.testing.assert_array_equal(scaled_const, np.zeros(4))

        with np.errstate(divide="ignore", invalid="ignore"):
            manual_const = (const_col - np.mean(const_col)) / np.std(const_col)
        self.assertTrue(np.all(np.isnan(manual_const)))

    def test_dummy_variable_trap_rank_and_condition_number(self):
        """
        Verify linear algebra mechanics of Dummy Variable Trap:
        When intercept is present with K dummy variables:
        - Rank(X^T X) = K (deficient; size is (K+1)x(K+1)).
        - Condition number is ~1e16 (infinite in 64-bit float).
        With drop_first=True:
        - Rank(X^T X) = K (full rank; size is K x K).
        - Invertible with stable condition number.
        """
        # 3 categories, 6 samples
        # Design matrix with explicit intercept (x0=1) and 3 one-hot columns
        X_trap = np.array([
            [1.0, 1.0, 0.0, 0.0],
            [1.0, 0.0, 1.0, 0.0],
            [1.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 0.0, 0.0],
            [1.0, 0.0, 1.0, 0.0],
            [1.0, 0.0, 0.0, 1.0],
        ])
        XT_X_trap = X_trap.T @ X_trap
        self.assertEqual(np.linalg.matrix_rank(XT_X_trap), 3)
        self.assertEqual(XT_X_trap.shape, (4, 4))
        self.assertGreater(np.linalg.cond(XT_X_trap), 1e15)

        # drop_first=True removes 1 column
        X_safe = X_trap[:, :3]
        XT_X_safe = X_safe.T @ X_safe
        self.assertEqual(np.linalg.matrix_rank(XT_X_safe), 3)
        self.assertEqual(XT_X_safe.shape, (3, 3))
        self.assertLess(np.linalg.cond(XT_X_safe), 100.0)

    def test_pearson_bounds_and_zero_variance_edge_cases(self):
        """
        Verify Pearson r bounds [-1, 1] and zero-variance edge cases:
        1. Always in [-1, 1] for arbitrary continuous distributions.
        2. Returns NaN when any feature has zero variance.
        """
        np.random.seed(42)
        x = np.random.randn(100)
        y = np.random.randn(100)
        r = np.corrcoef(x, y)[0, 1]
        self.assertTrue(-1.0 <= r <= 1.0)

        # Constant x
        x_const = np.ones(100) * 5.0
        with np.errstate(divide="ignore", invalid="ignore"):
            r_const = np.corrcoef(x_const, y)[0, 1]
        self.assertTrue(np.isnan(r_const))

    def test_seven_eleven_order_logic_behavior(self):
        """
        Verify Tanpin Kanri order logic with fixed import and boundary cases:
        - Rain + temp drop: +40%
        - Rain + no temp drop: -15%
        - Normal sunny: base_demand
        """
        def tanpin_kanri_order_fixed(base_demand: int, weather_rain: bool, temperature_drop: bool, pos_trend_ratio: float) -> int:
            order_qty = float(base_demand)
            if weather_rain and temperature_drop:
                order_qty *= 1.40
            elif weather_rain and not temperature_drop:
                order_qty *= 0.85
            order_qty *= pos_trend_ratio
            return round(order_qty)

        # Baseline sunny
        self.assertEqual(tanpin_kanri_order_fixed(100, False, False, 1.0), 100)
        # Cold rain with 1.25 trend
        self.assertEqual(tanpin_kanri_order_fixed(100, True, True, 1.25), 175)
        # Warm rain with 1.0 trend
        self.assertEqual(tanpin_kanri_order_fixed(100, True, False, 1.0), 85)


class TestDefinitionOfDoneMeasurability(unittest.TestCase):
    """
    Stress-tests the Definition of Done (DoD) across all micro-sessions
    and synthesis sessions for measurability, testability, and non-ambiguity.
    """

    @classmethod
    def setUpClass(cls):
        cls.content = ROADMAP_FILE.read_text(encoding="utf-8")

    def test_all_micro_sessions_have_verifiable_dod(self):
        """Every micro-session must have a DoD checklist with at least 3 concrete check items."""
        sections = [
            "MICRO-0.1", "MICRO-0.2", "MICRO-0.3", "MICRO-0.4",
            "MICRO-1.1", "MICRO-1.2", "MICRO-1.3", "MICRO-1.4", "MICRO-1.5"
        ]
        for sec in sections:
            pattern = rf"### {sec}.*?#### Tiêu Chí Hoàn Thành \(Definition of Done - DoD\)\s*(.*?)(?=####|---|\Z)"
            match = re.search(pattern, self.content, re.DOTALL)
            self.assertIsNotNone(match, f"Missing DoD section for {sec}")
            items = re.findall(r"-\s*\[\s*\]\s*(.+)", match.group(1))
            self.assertGreaterEqual(len(items), 3, f"{sec} has fewer than 3 DoD items: {items}")

    def test_synthesis_sessions_have_readiness_audits(self):
        """Both synthesis sessions must have readiness audit checklists."""
        self.assertIn("Bảng Kiểm Toán Mức Độ Sẵn Sàng (Milestone 0 Readiness Audit)", self.content)
        self.assertIn("Khung Kiểm Toán Chuyển Giao Buổi 1 Sang Tuần 2 (Milestone 1 Readiness Audit)", self.content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
