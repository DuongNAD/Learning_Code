"""
Comprehensive Empirical Stress-Testing Harness for GCI World 202609 Study Notes.
Authored by Challenger 1 (Code & Empirical Verifier).

Adversarially challenges, executes, and validates:
1. HW1: Odd multiples of 5 array filtering (boundary, negative, zero, large, float).
2. Note 01: Collatz conjecture algorithm, manual reverse, linear max, OnlineStatisticsEstimator (Welford).
3. Note 02: Descriptive stats (ddof=0 vs ddof=1), Z-score, Tukey IQR outlier filter, Pearson correlation.
4. Note 03: Log1p/expm1, broadcasting, axis reductions, slicing views vs indexing copies, linear algebra.
5. Note 04: Regression pipelines (Level 0-4), Normal equation, evaluation metrics (MSE, RMSE, MAE, R2).
6. Note 05: Classification pipelines (Level 0-3), Decision Trees, One-Hot encoding, Group Mode imputation,
            Confusion Matrix, Gini / Entropy / Precision / Recall / F1.
7. Note 06: K-Means clustering, PCA explained variance, Autocorrelation (ACF), Softmax with temperature.
8. Note 00: Seven-Eleven Japan RetailEmpiricalLoop simulation.
"""

import math
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
from numpy import linalg as LA

# Workspace roots
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
STUDY_NOTES_DIR = WORKSPACE_ROOT / "study_notes"
EXTRACTED_DIR = WORKSPACE_ROOT / "extracted_gci_world" / "GCI World_202609" / "02. Preparatory Materials"

CAR_PRICE_CSV = EXTRACTED_DIR / "6. Exercise_ Regression" / "data" / "Car_Price_Data.csv"
MUSHROOM_APP_CSV = EXTRACTED_DIR / "7. Exercise_ Classification" / "data" / "Mushroom_Appearence_Data.csv"
MUSHROOM_ODOR_CSV = EXTRACTED_DIR / "7. Exercise_ Classification" / "data" / "Mushroom_Odor_Data.csv"


# ==============================================================================
# 1. HW1 Array Filtering Stress-Testing Harness
# ==============================================================================
def hw1_homework(a):
    """Implementation from Note 03 (study_notes/03_NumPy_Computing.md line 286)."""
    condition_mask = (a % 5 == 0) & (a % 2 == 1)
    return a[condition_mask]


class TestHW1OddMultiplesOf5(unittest.TestCase):
    """Adversarial stress-testing of HW1 array filtering logic."""

    def test_hw1_standard_cases(self):
        """Test standard course cases."""
        test1 = np.array([1, 5, 10, 3, 4, 25, 30])
        res1 = hw1_homework(test1)
        np.testing.assert_array_equal(res1, np.array([5, 25]))

        test2 = np.array([11, 15, 20, 21, 35, 40, 45])
        res2 = hw1_homework(test2)
        np.testing.assert_array_equal(res2, np.array([15, 35, 45]))

    def test_hw1_empty_array(self):
        """Test on empty arrays with various dtypes."""
        empty_int = np.array([], dtype=int)
        res_empty = hw1_homework(empty_int)
        self.assertEqual(len(res_empty), 0)
        self.assertEqual(res_empty.dtype, np.int64 if np.dtype(int) == np.int64 else np.int32)

        empty_default = np.array([])
        res_empty_float = hw1_homework(empty_default)
        self.assertEqual(len(res_empty_float), 0)

    def test_hw1_no_matches(self):
        """Test on array containing no odd multiples of 5 (e.g. only even multiples, or non-multiples)."""
        test_even_mults = np.array([10, 20, 30, 40, 50, 100])
        self.assertEqual(len(hw1_homework(test_even_mults)), 0)

        test_odds_not_5 = np.array([1, 3, 7, 9, 11, 13, 17, 19, 21, 23])
        self.assertEqual(len(hw1_homework(test_odds_not_5)), 0)

    def test_hw1_negative_numbers(self):
        """
        Adversarial test: Negative odd multiples of 5.
        -25, -15, -5 are odd multiples of 5.
        -20, -10, 0 are even multiples of 5.
        Verify Python & NumPy % behavior on negatives:
        In Python and NumPy: -25 % 5 == 0, -25 % 2 == 1.
        """
        test_neg = np.array([-30, -25, -20, -15, -10, -5, 0, 5, 10, 15])
        res_neg = hw1_homework(test_neg)
        expected = np.array([-25, -15, -5, 5, 15])
        np.testing.assert_array_equal(res_neg, expected)

    def test_hw1_zero(self):
        """Zero is a multiple of 5 (0*5 = 0), but zero is EVEN (0%2 == 0). It must NOT be included."""
        test_zero = np.array([0])
        self.assertEqual(len(hw1_homework(test_zero)), 0)

    def test_hw1_large_array_performance(self):
        """Stress test with 1,000,000 integers to verify SIMD vectorization and memory safety."""
        np.random.seed(42)
        large_arr = np.random.randint(-10000, 10000, size=1_000_000)
        res_large = hw1_homework(large_arr)
        # Check all extracted elements satisfy criteria
        self.assertTrue(np.all(res_large % 5 == 0))
        self.assertTrue(np.all(res_large % 2 == 1))
        # Ground truth count via comprehension or oracle
        oracle_count = sum(1 for x in large_arr if x % 5 == 0 and x % 2 == 1)
        self.assertEqual(len(res_large), oracle_count)


# ==============================================================================
# 2. Note 01: Collatz, Manual Algorithms & Online Statistics OOP
# ==============================================================================
def collatz_steps(start_val: int) -> int:
    """Implementation from Note 01 (study_notes/01_Python_Foundations.md line 246)."""
    if start_val <= 0:
        raise ValueError("Số khởi đầu của chuỗi Collatz phải là số nguyên dương!")
    current = start_val
    steps = 0
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        steps += 1
    return steps


def manual_reverse(input_list: list) -> list:
    """Implementation from Note 01 line 276."""
    reversed_result = []
    total_elements = len(input_list)
    for i in range(total_elements):
        reversed_result.append(input_list[-i - 1])
    return reversed_result


def find_max_linear(input_list: list) -> float:
    """Implementation from Note 01 line 292."""
    if not input_list:
        raise ValueError("Danh sách đầu vào không được rỗng!")
    largest = input_list[0]
    for element in input_list[1:]:
        if element > largest:
            largest = element
    return largest


class OnlineStatisticsEstimator:
    """Implementation from Note 01 line 371."""

    def __init__(self, feature_name: str = "metric"):
        self.feature_name: str = feature_name
        self.count: int = 0
        self._mean: float = 0.0
        self._M2: float = 0.0

    def update(self, value: float) -> None:
        self.count += 1
        delta = value - self._mean
        self._mean += delta / self.count
        delta2 = value - self._mean
        self._M2 += delta * delta2

    def update_batch(self, values: list) -> None:
        for val in values:
            self.update(val)

    @property
    def mean(self) -> float:
        if self.count == 0:
            return 0.0
        return self._mean

    @property
    def variance(self) -> float:
        if self.count < 2:
            return 0.0
        return self._M2 / (self.count - 1)

    @property
    def std_dev(self) -> float:
        return math.sqrt(self.variance)

    def get_summary(self) -> dict:
        return {
            "feature": self.feature_name,
            "count": float(self.count),
            "mean": self.mean,
            "variance": self.variance,
            "std_dev": self.std_dev,
        }

    def reset(self) -> None:
        self.count = 0
        self._mean = 0.0
        self._M2 = 0.0


class TestNote01AlgorithmsAndOOP(unittest.TestCase):
    """Empirical verification of Note 01 Python code and algorithms."""

    def test_collatz_known_values(self):
        """Verify known Collatz sequences."""
        self.assertEqual(collatz_steps(1), 0)
        self.assertEqual(collatz_steps(2), 1)
        self.assertEqual(collatz_steps(3), 7)
        self.assertEqual(collatz_steps(4), 2)
        self.assertEqual(collatz_steps(7), 16)
        self.assertEqual(collatz_steps(27), 111)
        self.assertEqual(collatz_steps(31), 106)

    def test_collatz_invalid_inputs(self):
        """Verify boundary condition: non-positive inputs raise ValueError."""
        with self.assertRaises(ValueError):
            collatz_steps(0)
        with self.assertRaises(ValueError):
            collatz_steps(-1)
        with self.assertRaises(ValueError):
            collatz_steps(-100)

    def test_manual_reverse_and_max(self):
        """Verify manual reverse and max linear."""
        self.assertEqual(manual_reverse([]), [])
        self.assertEqual(manual_reverse([1]), [1])
        self.assertEqual(manual_reverse([3, 9, 7, 1, 0]), [0, 1, 7, 9, 3])
        self.assertEqual(manual_reverse(["a", "b", "c"]), ["c", "b", "a"])

        with self.assertRaises(ValueError):
            find_max_linear([])
        self.assertEqual(find_max_linear([42]), 42)
        self.assertEqual(find_max_linear([45, 82, 19, 98, 73, 91]), 98)
        self.assertEqual(find_max_linear([-10, -50, -3, -99]), -3)

    def test_online_statistics_estimator_accuracy(self):
        """Verify Welford's algorithm matches numpy ddof=1 precision."""
        estimator = OnlineStatisticsEstimator("sensor_test")
        # Empty state
        self.assertEqual(estimator.mean, 0.0)
        self.assertEqual(estimator.variance, 0.0)
        self.assertEqual(estimator.std_dev, 0.0)

        # Single element
        estimator.update(100.0)
        self.assertEqual(estimator.mean, 100.0)
        self.assertEqual(estimator.variance, 0.0)

        # Stream from note
        sensor_stream = [88.5, 91.0, 89.2, 95.4, 90.1, 87.8, 92.3, 94.0]
        estimator.reset()
        estimator.update_batch(sensor_stream)

        expected_mean = float(np.mean(sensor_stream))
        expected_var = float(np.var(sensor_stream, ddof=1))
        expected_std = float(np.std(sensor_stream, ddof=1))

        self.assertAlmostEqual(estimator.mean, expected_mean, places=6)
        self.assertAlmostEqual(estimator.variance, expected_var, places=6)
        self.assertAlmostEqual(estimator.std_dev, expected_std, places=6)

    def test_online_statistics_numerical_stability(self):
        """Test Welford numerical stability with massive offsets (catastrophic cancellation test)."""
        offset = 1e9
        data = [offset + 1.0, offset + 2.0, offset + 3.0, offset + 4.0, offset + 5.0]
        est = OnlineStatisticsEstimator("stability")
        est.update_batch(data)
        # Expected variance of [1, 2, 3, 4, 5] with ddof=1 is 2.5
        self.assertAlmostEqual(est.variance, 2.5, places=5)


# ==============================================================================
# 3. Note 02: Descriptive Statistics, Z-Score, Tukey IQR, Pearson Correlation
# ==============================================================================
class TestNote02StatisticsAndEDA(unittest.TestCase):
    """Empirical verification of Note 02 statistics and formulas."""

    def setUp(self):
        self.english_scores = np.array([
            65, 80, 35, 55, 65, 80, 55, 65, 50, 85,
            55, 55, 70, 50, 80, 70, 65, 80, 65, 15
        ])
        self.math_scores = np.array([
            85, 55, 40, 90, 35, 40, 50, 40, 95, 40,
            90, 45, 85, 45, 40, 85, 50, 55, 100, 75
        ])

    def test_mean_and_median_reproducibility(self):
        """Check values cited in note: Mean = 62.00, Median Eng = 65, Math = 52.5."""
        self.assertAlmostEqual(np.mean(self.english_scores), 62.0, places=2)
        self.assertAlmostEqual(np.mean(self.math_scores), 62.0, places=2)
        self.assertEqual(np.median(self.english_scores), 65.0)
        self.assertEqual(np.median(self.math_scores), 52.5)

    def test_variance_and_std_ddof(self):
        """Check ddof=0 vs ddof=1."""
        self.assertAlmostEqual(np.var(self.english_scores), 271.0, places=2)
        self.assertAlmostEqual(np.var(self.math_scores), 498.5, places=2)
        self.assertAlmostEqual(np.var(self.english_scores, ddof=1), 285.263, places=1)
        self.assertAlmostEqual(np.var(self.math_scores, ddof=1), 524.736, places=1)
        self.assertAlmostEqual(np.std(self.english_scores, ddof=1), 16.889, places=1)
        self.assertAlmostEqual(np.std(self.math_scores, ddof=1), 22.907, places=1)

    def test_z_score_math(self):
        """Check Z-score formula: mu=0, std=1."""
        mu = np.mean(self.english_scores)
        sigma = np.std(self.english_scores)
        z = (self.english_scores - mu) / sigma
        self.assertAlmostEqual(np.mean(z), 0.0, places=6)
        self.assertAlmostEqual(np.std(z), 1.0, places=6)

    def test_tukey_outlier_detection(self):
        """Check Tukey IQR calculation on English scores: outlier should be 15."""
        q1 = np.percentile(self.english_scores, 25)
        q3 = np.percentile(self.english_scores, 75)
        iqr = q3 - q1
        lower_whisker = q1 - 1.5 * iqr
        upper_whisker = q3 + 1.5 * iqr

        outlier_mask = (self.english_scores < lower_whisker) | (self.english_scores > upper_whisker)
        outliers = self.english_scores[outlier_mask]
        self.assertEqual(outliers.tolist(), [15])

    def test_pearson_correlation(self):
        """
        Verify Pearson correlation between English and Math scores.
        Note 02 comment states '# Kết quả: -0.2120'.
        Empirical calculation shows actual value is -0.214936...
        """
        corr = np.corrcoef(self.english_scores, self.math_scores)[0, 1]
        # True mathematical value
        self.assertAlmostEqual(corr, -0.2149, places=3)
        # Verify comment discrepancy: comment claims -0.2120, difference is ~0.0029
        self.assertNotEqual(round(float(corr), 4), -0.2120)


# ==============================================================================
# 4. Note 03: NumPy Slicing, Broadcasting & Linear Algebra
# ==============================================================================
class TestNote03NumPyComputing(unittest.TestCase):
    """Empirical verification of Note 03 NumPy operations."""

    def test_log1p_and_expm1(self):
        """Verify numerical stability of log1p with zero values."""
        prcp = np.array([0.0, 5.2, 0.0, 18.5])
        log_safe = np.log1p(prcp)
        self.assertFalse(np.any(np.isneginf(log_safe)))
        recovered = np.expm1(log_safe)
        np.testing.assert_allclose(recovered, prcp, rtol=1e-5)

    def test_broadcasting_axis_semantics(self):
        """Verify axis=0 (down column) and axis=1 (across row) reductions."""
        scores = np.array([
            [75, 80, 90],
            [60, 95, 85],
            [85, 70, 65]
        ])
        subject_means = np.mean(scores, axis=0)
        self.assertEqual(subject_means.shape, (3,))
        centered_col = scores - subject_means
        np.testing.assert_allclose(np.mean(centered_col, axis=0), [0.0, 0.0, 0.0], atol=1e-10)

        student_means_2d = np.mean(scores, axis=1, keepdims=True)
        self.assertEqual(student_means_2d.shape, (3, 1))
        centered_row = scores - student_means_2d
        np.testing.assert_allclose(np.mean(centered_row, axis=1), [0.0, 0.0, 0.0], atol=1e-10)

    def test_linear_algebra_operations(self):
        """Verify det, inv, norm, SVD on matrix A."""
        A = np.array([[3.0, 2.0], [1.0, 4.0]])
        det_A = LA.det(A)
        self.assertAlmostEqual(det_A, 10.0, places=5)

        inv_A = LA.inv(A)
        identity = A @ inv_A
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-10)

        v = np.array([3.0, -4.0])
        self.assertAlmostEqual(LA.norm(v, ord=1), 7.0)
        self.assertAlmostEqual(LA.norm(v, ord=2), 5.0)
        self.assertAlmostEqual(LA.norm(v, ord=np.inf), 4.0)


# ==============================================================================
# 5. Note 04: Supervised Regression Pipelines & Critical Bug Detection
# ==============================================================================
class TestNote04SupervisedRegression(unittest.TestCase):
    """Empirical verification of Note 04 regression code and scikit-learn API compatibility."""

    def test_level_0_toy_regression(self):
        """Verify Level 0 toy linear regression executes and computes R2."""
        from sklearn.linear_model import LinearRegression
        data = {
            'width': [64.1, 65.5, 65.5, 66.2],
            'engine-size': [130, 130, 152, 109],
            'price': [13495, 16500, 16500, 13950]
        }
        df_toy = pd.DataFrame(data)
        X = df_toy[['width', 'engine-size']]
        y = df_toy['price']
        model = LinearRegression().fit(X, y)
        r2 = model.score(X, y)
        self.assertTrue(0.0 <= r2 <= 1.0)
        self.assertEqual(len(model.coef_), 2)

    def test_regression_pipeline_car_price_dataset(self):
        """Test regression pipeline on real Car_Price_Data.csv if available."""
        if not CAR_PRICE_CSV.exists():
            self.skipTest(f"Car_Price_Data.csv not found at {CAR_PRICE_CSV}")

        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.preprocessing import StandardScaler

        df = pd.read_csv(CAR_PRICE_CSV).dropna()
        features = ['engine-size', 'curb-weight', 'city-mpg']
        X = df[features]
        y = df['price']

        # Baseline split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        lr = LinearRegression().fit(X_train, y_train)
        r2_base = lr.score(X_test, y_test)
        self.assertGreater(r2_base, 0.7)

        # Scaling without data leakage
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        lr_scaled = LinearRegression().fit(X_train_scaled, y_train)
        r2_scaled = lr_scaled.score(X_test_scaled, y_test)
        self.assertAlmostEqual(r2_base, r2_scaled, places=5)

    def test_regression_rmse_api_compatibility_adversarial(self):
        """
        ADVERSARIAL CHALLENGE:
        Note 04 line 223 calls:
            rmse = mean_squared_error(y_test, y_pred, squared=False)
        In scikit-learn 1.8.0, does `squared=False` work or fail?
        """
        from sklearn.metrics import mean_squared_error

        y_true = [10.0, 20.0, 30.0]
        y_pred = [11.0, 19.0, 32.0]

        # Check if squared keyword raises TypeError in the current environment
        with self.assertRaises(TypeError) as context:
            _ = mean_squared_error(y_true, y_pred, squared=False)
        self.assertIn("squared", str(context.exception))

        # Check correct modern alternatives
        # Alternative 1: np.sqrt(mean_squared_error(y_true, y_pred))
        rmse_np = np.sqrt(mean_squared_error(y_true, y_pred))
        self.assertAlmostEqual(rmse_np, math.sqrt((1 + 1 + 4) / 3), places=5)

        # Alternative 2: root_mean_squared_error
        try:
            from sklearn.metrics import root_mean_squared_error
            rmse_sklearn = root_mean_squared_error(y_true, y_pred)
            self.assertAlmostEqual(rmse_sklearn, rmse_np, places=5)
        except ImportError:
            pass


# ==============================================================================
# 6. Note 05: Supervised Classification Pipelines
# ==============================================================================
class TestNote05SupervisedClassification(unittest.TestCase):
    """Empirical verification of Note 05 classification code and data pipelines."""

    def test_level_0_toy_tree(self):
        """Verify Level 0 baseline Decision Tree on toy mushroom data."""
        from sklearn.tree import DecisionTreeClassifier
        toy_data = {
            'bruises': ['yes', 'no', 'no', 'yes'],
            'odor': ['almond', 'anise', 'none', 'pungent'],
            'poison': [0, 0, 0, 1]
        }
        df_toy = pd.DataFrame(toy_data)
        X_raw = df_toy[['bruises', 'odor']]
        y = df_toy['poison']
        X_encoded = pd.get_dummies(X_raw, drop_first=True, dtype=int)
        clf = DecisionTreeClassifier(random_state=42).fit(X_encoded, y)
        self.assertEqual(clf.score(X_encoded, y), 1.0)

    def test_mushroom_pipeline_and_group_mode(self):
        """Verify Group Mode Imputation logic on Mushroom dataset."""
        if not MUSHROOM_APP_CSV.exists() or not MUSHROOM_ODOR_CSV.exists():
            self.skipTest("Mushroom datasets not found.")

        df_app = pd.read_csv(MUSHROOM_APP_CSV)
        df_odor = pd.read_csv(MUSHROOM_ODOR_CSV)

        # Unmatched keys verification
        unmatched = ~df_app['ID'].isin(df_odor['ID'])
        self.assertEqual(unmatched.sum(), 4)  # 4 IDs in app do not exist in odor

        # Merge
        df_merged = pd.merge(df_app, df_odor, on='ID', how='inner')
        self.assertEqual(len(df_merged), len(df_app) - 4)

        # Test group mode imputation
        group_modes = df_app.groupby('cap_color')['bruises'].describe()['top']
        self.assertGreater(len(group_modes), 0)

    def test_classification_metrics_math(self):
        """Verify confusion matrix unpacking and metric formulas."""
        from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

        y_true = [0, 0, 0, 0, 1, 1, 1, 1]
        y_pred = [0, 0, 0, 1, 0, 1, 1, 1]  # TN=3, FP=1, FN=1, TP=3

        cm = confusion_matrix(y_true, y_pred)
        tn, fp, fn, tp = cm.ravel()
        self.assertEqual((tn, fp, fn, tp), (3, 1, 1, 3))

        self.assertEqual(accuracy_score(y_true, y_pred), 6 / 8)
        self.assertEqual(precision_score(y_true, y_pred), 3 / 4)
        self.assertEqual(recall_score(y_true, y_pred), 3 / 4)
        self.assertEqual(f1_score(y_true, y_pred), 3 / 4)

    def test_gini_and_entropy_equations(self):
        """Verify Gini impurity and Shannon entropy mathematical formulas cited in R1."""
        # Pure node: p = [1.0, 0.0] -> Gini = 0, Entropy = 0
        p_pure = np.array([1.0, 0.0])
        gini_pure = 1.0 - np.sum(p_pure ** 2)
        self.assertEqual(gini_pure, 0.0)

        # Maximum impurity binary node: p = [0.5, 0.5] -> Gini = 0.5, Entropy = 1.0
        p_split = np.array([0.5, 0.5])
        gini_split = 1.0 - np.sum(p_split ** 2)
        entropy_split = -np.sum(p_split * np.log2(p_split))
        self.assertEqual(gini_split, 0.5)
        self.assertEqual(entropy_split, 1.0)


# ==============================================================================
# 7. Note 06: ML Landscape, Strategy, PCA, ACF, Softmax
# ==============================================================================
class TestNote06MLLandscapeAndStrategy(unittest.TestCase):
    """Empirical verification of Note 06 unsupervised and foundation model algorithms."""

    def test_kmeans_and_inertia(self):
        """Verify KMeans cluster convergence and inertia calculation."""
        from sklearn.cluster import KMeans
        np.random.seed(42)
        X = np.random.randn(100, 2)
        kmeans = KMeans(n_clusters=3, n_init=10, random_state=42).fit(X)
        self.assertEqual(len(kmeans.cluster_centers_), 3)
        self.assertGreater(kmeans.inertia_, 0.0)

    def test_pca_variance_ratio_sum(self):
        """Verify PCA explained variance ratio sums to 1.0 for all components."""
        from sklearn.decomposition import PCA
        np.random.seed(42)
        X = np.random.randn(100, 5)
        pca = PCA(n_components=5).fit(X)
        evr = pca.explained_variance_ratio_
        self.assertAlmostEqual(float(np.sum(evr)), 1.0, places=5)
        # Verify monotonically decreasing variance explained
        for i in range(len(evr) - 1):
            self.assertGreaterEqual(evr[i], evr[i + 1])

    def test_autocorrelation_acf_math(self):
        """Verify Autocorrelation ACF implementation."""
        np.random.seed(42)
        t = np.arange(100)
        # Pure lag 7 seasonal cycle
        ts = pd.Series(np.sin(2 * np.pi * t / 7))
        y_mean = ts.mean()
        var_denom = np.sum((ts - y_mean) ** 2)

        # lag 7 covariance
        k = 7
        cov_num = np.sum((ts.iloc[k:].values - y_mean) * (ts.iloc[:-k].values - y_mean))
        r_7 = cov_num / var_denom
        # For a period-7 sine wave with N=100, (N-k)/N = 93/100, so r_7 should be ~0.93
        self.assertGreater(r_7, 0.90)
        self.assertAlmostEqual(float(r_7), 0.9294, places=3)

    def test_softmax_temperature_behavior(self):
        """Verify Softmax with temperature behavior."""
        logits = np.array([2.0, 4.0, 1.0])

        def softmax_temp(z, temp):
            scaled = z / temp
            exp_z = np.exp(scaled - np.max(scaled))
            return exp_z / np.sum(exp_z)

        p_std = softmax_temp(logits, 1.0)
        p_low = softmax_temp(logits, 0.1)   # sharp (focused)
        p_high = softmax_temp(logits, 10.0) # uniform (creative)

        # Probabilities sum to 1
        self.assertAlmostEqual(float(np.sum(p_std)), 1.0, places=6)
        self.assertAlmostEqual(float(np.sum(p_low)), 1.0, places=6)
        self.assertAlmostEqual(float(np.sum(p_high)), 1.0, places=6)

        # High temperature approaches uniform distribution (1/3 for each)
        np.testing.assert_allclose(p_high, [1/3, 1/3, 1/3], atol=0.1)

        # Low temperature concentrates probability mass on index 1 (max logit)
        self.assertGreater(p_low[1], 0.99)


# ==============================================================================
# 8. Note 00: Seven-Eleven Japan RetailEmpiricalLoop Simulation
# ==============================================================================
class TestNote00RetailEmpiricalLoop(unittest.TestCase):
    """Empirical verification of Note 00 Seven-Eleven loop simulation."""

    def test_seven_eleven_simulation(self):
        """Test observation, hypothesis, experiment, analysis loop."""
        base_demand = 100.0
        sensitivity = 5.0
        # Hypothesis: base + rain * sensitivity
        rainfall = 10.0
        multiplier = 1.2
        expected_demand = (base_demand + rainfall * sensitivity) * multiplier
        self.assertEqual(expected_demand, 180.0)

        # Stockout when actual > ordered
        ordered = 150.0
        actual = 180.0
        sold = min(ordered, actual)
        stockout = max(0.0, actual - ordered)
        self.assertEqual(sold, 150.0)
        self.assertEqual(stockout, 30.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
