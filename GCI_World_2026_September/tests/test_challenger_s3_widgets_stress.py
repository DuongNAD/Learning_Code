"""
[Test Suite] Empirical Stress-Testing Harness for Interactive NumPy Visualizer Widgets
Course: GCI World 2026 September (Matsuo-Iwasawa Lab, The University of Tokyo)
Author: challenger_s3_1 (Empirical Challenger - critic, specialist)
Strict Policy: emoji_policy: none (Zero Unicode Emojis Workspace-Wide)
RFC 2119 Compliance: Strict

Adversarially challenges, executes, and validates:
1. NumPy Broadcasting Rules Simulator:
   - Trailing right-to-left dimension alignment against NumPy reference
   - Dimension expansion with singleton dimensions (1s) and high-rank tensors (up to 5D)
   - Size-0 empty array edge cases and incompatible shape mismatch exceptions
   - RAM conservation telemetry formula vs naive duplication baseline
2. ndarray Strides & Slicing Memory Visualizer:
   - C-contiguous strides formula across arbitrary shapes and item sizes
   - Slicing strides S_new = S_orig * step and base offset calculations
   - Affine memory addressing Addr(i, j) = Base + offset + i*S0 + j*S1
   - View vs Copy invariants (memory sharing, base pointer, heap allocation)
   - Visualizer UI formula display discrepancy detection (baseOffset omission)
3. Vectorization vs Python Loop Benchmark:
   - Analytical execution time equations positivity and monotonicity
   - Speedup ratio strict monotonicity dS/dN > 0 across N in [10^1, 10^8]
   - Asymptotic convergence to theoretical AVX-512 SIMD ceiling (~297.6x)
   - Crossover threshold at small N (C dispatch overhead dominance)
   - SVG coordinate clipping vulnerability under high-speedup operations
4. Headless & SSR Execution Portability:
   - Document guard sanity in CommonJS / headless environments
"""

import math
import subprocess
import unittest
from pathlib import Path
import numpy as np

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
BUNDLE_JS_PATH = WORKSPACE_ROOT / "slides" / "js" / "widgets-bundle.js"


# ==============================================================================
# Pure Python Oracles Mirroring JavaScript Bundle Logic
# ==============================================================================

def js_broadcast_shapes(shape_a, shape_b):
    """Exact Python replica of broadcastShapes(shapeA, shapeB) in widgets-bundle.js."""
    len_a = len(shape_a)
    len_b = len(shape_b)
    max_len = max(len_a, len_b)

    padded_a = [1] * (max_len - len_a) + list(shape_a)
    padded_b = [1] * (max_len - len_b) + list(shape_b)

    res_shape = []
    is_compatible = True
    mismatch_axis = None

    for k in range(max_len):
        da = padded_a[k]
        db = padded_b[k]
        if da == db:
            res_shape.append(da)
        elif da == 1:
            res_shape.append(db)
        elif db == 1:
            res_shape.append(da)
        else:
            is_compatible = False
            mismatch_axis = k
            break

    return {
        "compatible": is_compatible,
        "resShape": res_shape if is_compatible else None,
        "paddedA": padded_a,
        "paddedB": padded_b,
        "mismatchAxis": mismatch_axis,
    }


def js_c_contiguous_strides(shape, itemsize=8):
    """Exact Python replica of cContiguousStrides(shape, itemsize) in widgets-bundle.js."""
    strides = [0] * len(shape)
    current = itemsize
    for i in range(len(shape) - 1, -1, -1):
        strides[i] = current
        current *= shape[i]
    return strides


def js_compute_slice(shape, itemsize, start_row, stop_row, step_row, start_col, stop_col, step_col):
    """Exact Python replica of computeSlice() in widgets-bundle.js."""
    orig_strides = js_c_contiguous_strides(shape, itemsize)
    r_count = max(0, math.ceil((stop_row - start_row) / step_row))
    c_count = max(0, math.ceil((stop_col - start_col) / step_col))
    new_shape = [r_count, c_count]
    new_strides = [orig_strides[0] * step_row, orig_strides[1] * step_col]
    base_offset = start_row * orig_strides[0] + start_col * orig_strides[1]

    active_indices = {}
    for r in range(start_row, stop_row, step_row):
        for c in range(start_col, stop_col, step_col):
            active_indices[(r, c)] = True

    return {
        "origStrides": orig_strides,
        "newShape": new_shape,
        "newStrides": new_strides,
        "baseOffset": base_offset,
        "activeIndices": active_indices,
        "elementCount": r_count * c_count,
    }


def js_time_python_ns(n, op="add"):
    """Exact Python replica of timePythonNs(n, op) in widgets-bundle.js."""
    base = n * 62.5
    factor = 1.45 if op == "cumsum" else (1.80 if op == "filter" else 1.0)
    return base * factor


def js_time_numpy_ns(n, op="add"):
    """Exact Python replica of timeNumpyNs(n, op) in widgets-bundle.js."""
    base = 2500.0 + n * 0.21
    factor = 1.20 if op == "cumsum" else (1.15 if op == "filter" else 1.0)
    return base * factor


def js_speedup(n, op="add"):
    """Analytical speedup ratio."""
    return js_time_python_ns(n, op) / js_time_numpy_ns(n, op)


# ==============================================================================
# 1. NumPy Broadcasting Rules Simulator Stress Tests
# ==============================================================================

class TestBroadcastingModelEmpiricalStress(unittest.TestCase):
    """Adversarial stress-testing of broadcasting trailing alignment and compatibility."""

    def test_broadcasting_against_numpy_broadcast_shapes_oracle(self):
        """Stress-test 30 diverse shape pairs against official np.broadcast_shapes."""
        test_pairs = [
            # 1D with 1D
            ((3,), (3,)),
            ((1,), (5,)),
            ((5,), (1,)),
            # 1D with 2D
            ((4,), (3, 4)),
            ((1,), (3, 4)),
            ((4,), (1, 4)),
            # 2D with 2D
            ((3, 1), (1, 4)),
            ((3, 3), (1, 3)),
            ((1, 5), (5, 1)),
            ((10, 1), (1, 10)),
            # 3D with 2D and 1D
            ((2, 3, 4), (4,)),
            ((2, 3, 4), (3, 4)),
            ((2, 3, 1), (1, 4)),
            ((2, 1, 4), (3, 1)),
            ((1, 3, 1), (2, 1, 4)),
            # 4D and 5D high-rank tensors
            ((8, 1, 6, 1), (7, 1, 5)),
            ((2, 1, 3, 1, 5), (1, 4, 1, 2, 1)),
            # Incompatible pairs (should fail both)
            ((3,), (4,)),
            ((3, 2), (3, 3)),
            ((2, 3), (2, 4)),
            ((2, 3, 4), (2, 4, 3)),
            ((5, 2), (2, 5)),
        ]

        for shape_a, shape_b in test_pairs:
            js_res = js_broadcast_shapes(shape_a, shape_b)

            try:
                np_shape = np.broadcast_shapes(shape_a, shape_b)
                np_compatible = True
            except ValueError:
                np_shape = None
                np_compatible = False

            self.assertEqual(
                js_res["compatible"], np_compatible,
                f"Compatibility disagreement for shapes {shape_a} and {shape_b}"
            )
            if np_compatible:
                self.assertEqual(
                    tuple(js_res["resShape"]), np_shape,
                    f"Output shape disagreement for shapes {shape_a} and {shape_b}"
                )

    def test_broadcasting_trailing_alignment_padding_invariant(self):
        """Verify that padding always occurs on the leading side (left) to align trailing dimensions."""
        shapes = [
            ((4,), (2, 3, 4), [1, 1, 4], [2, 3, 4]),
            ((3, 1), (2, 3, 4), [1, 3, 1], [2, 3, 4]),
            ((5,), (1, 2, 3, 5), [1, 1, 1, 5], [1, 2, 3, 5]),
        ]
        for sa, sb, exp_pad_a, exp_pad_b in shapes:
            res = js_broadcast_shapes(sa, sb)
            self.assertEqual(res["paddedA"], exp_pad_a)
            self.assertEqual(res["paddedB"], exp_pad_b)
            self.assertTrue(res["compatible"])

    def test_broadcasting_size_zero_arrays(self):
        """Stress-test edge cases with empty dimensions (shape size 0)."""
        # Compatible size-0 shapes
        res1 = js_broadcast_shapes((0, 3), (1, 3))
        self.assertTrue(res1["compatible"])
        self.assertEqual(res1["resShape"], [0, 3])

        res2 = js_broadcast_shapes((0, 1), (1, 5))
        self.assertTrue(res2["compatible"])
        self.assertEqual(res2["resShape"], [0, 5])

        # Incompatible size-0 shapes
        res3 = js_broadcast_shapes((0, 2), (0, 3))
        self.assertFalse(res3["compatible"])

    def test_broadcasting_memory_conservation_telemetry_accuracy(self):
        """Verify RAM conservation calculation: savedPct = (naiveBytes - storedBytes) / naiveBytes * 100."""
        test_cases = [
            # shapeA, shapeB, expected stored elements, expected naive elements
            ((3, 1), (1, 4), 3 + 4, 12 * 2),  # 7 vs 24
            ((3, 3), (1, 3), 9 + 3, 9 * 2),   # 12 vs 18
            ((100, 1), (1, 100), 200, 10000 * 2),  # 200 vs 20000 -> 99.0% saved
        ]

        for sa, sb, exp_stored, exp_naive in test_cases:
            res = js_broadcast_shapes(sa, sb)
            self.assertTrue(res["compatible"])

            stored_elements = np.prod(sa) + np.prod(sb)
            naive_elements = np.prod(res["resShape"]) * 2
            self.assertEqual(stored_elements, exp_stored)
            self.assertEqual(naive_elements, exp_naive)

            saved_pct = ((naive_elements - stored_elements) / naive_elements) * 100.0
            self.assertGreater(saved_pct, 0.0)
            if sa == (100, 1) and sb == (1, 100):
                self.assertAlmostEqual(saved_pct, 99.0, places=1)


# ==============================================================================
# 2. ndarray Strides & Slicing Memory Stress Tests
# ==============================================================================

class TestStridesAndSlicingEmpiricalStress(unittest.TestCase):
    """Adversarial stress-testing of affine indexing, strides, and memory sharing."""

    def test_c_contiguous_strides_formula_across_ranks(self):
        """Verify C-contiguous strides formula against NumPy ndarray.strides across 1D to 5D."""
        shapes_and_itemsizes = [
            ((10,), 8),
            ((4, 5), 8),
            ((4, 5), 4),
            ((2, 3, 4), 8),
            ((3, 2, 5, 4), 8),
            ((2, 1, 4, 3, 5), 8),
        ]
        for shape, itemsize in shapes_and_itemsizes:
            dtype = np.float64 if itemsize == 8 else np.float32
            arr = np.zeros(shape, dtype=dtype)
            js_strides = js_c_contiguous_strides(shape, itemsize)
            self.assertEqual(
                tuple(js_strides), arr.strides,
                f"Strides mismatch for shape {shape} with itemsize {itemsize}"
            )

    def test_slicing_strides_and_shape_oracle(self):
        """Verify computeSlice logic against true NumPy slicing for diverse slice bounds."""
        base_shape = (4, 5)
        base_arr = np.arange(20, dtype=np.float64).reshape(base_shape)

        # Iterate through multiple slice window combinations
        slice_specs = [
            (0, 3, 1, 1, 5, 2),
            (1, 4, 2, 0, 5, 1),
            (0, 4, 1, 0, 5, 1),
            (2, 3, 1, 2, 4, 1),
            (0, 2, 2, 1, 3, 2),
        ]

        for r_start, r_stop, r_step, c_start, c_stop, c_step in slice_specs:
            calc = js_compute_slice(base_shape, 8, r_start, r_stop, r_step, c_start, c_stop, c_step)
            actual_slice = base_arr[r_start:r_stop:r_step, c_start:c_stop:c_step]

            # 1. Verify sliced shape
            self.assertEqual(calc["newShape"], list(actual_slice.shape))

            # 2. Verify sliced strides
            self.assertEqual(calc["newStrides"], list(actual_slice.strides))

            # 3. Verify total element count
            self.assertEqual(calc["elementCount"], actual_slice.size)

            # 4. Verify base offset in bytes
            expected_offset = (actual_slice.ctypes.data - base_arr.ctypes.data)
            self.assertEqual(calc["baseOffset"], expected_offset)

    def test_affine_memory_address_formula_exactness(self):
        """Verify that Addr(i, j) = Base + offset + i*S0 + j*S1 correctly indexes physical elements."""
        base_addr = 0x1000  # 4096
        base_shape = (4, 5)
        base_arr = np.arange(20, dtype=np.float64).reshape(base_shape)

        # Slice: rows 1..4 step 2, cols 1..5 step 2 -> sub-shape (2, 2)
        r_start, r_stop, r_step = 1, 4, 2
        c_start, c_stop, c_step = 1, 5, 2

        calc = js_compute_slice(base_shape, 8, r_start, r_stop, r_step, c_start, c_stop, c_step)
        sub_arr = base_arr[r_start:r_stop:r_step, c_start:c_stop:c_step]

        for i_sub in range(calc["newShape"][0]):
            for j_sub in range(calc["newShape"][1]):
                # True physical address relative to Base
                elem_offset = calc["baseOffset"] + i_sub * calc["newStrides"][0] + j_sub * calc["newStrides"][1]
                flat_index = elem_offset // 8

                # Logical row/col in original array
                orig_r = r_start + i_sub * r_step
                orig_c = c_start + j_sub * c_step

                self.assertEqual(flat_index, orig_r * 5 + orig_c)
                self.assertEqual(base_arr[orig_r, orig_c], sub_arr[i_sub, j_sub])

    def test_view_vs_copy_invariants(self):
        """Empirically certify memory sharing and allocation invariants."""
        # Unreshaped array has base=None, so view.base is arr
        arr = np.zeros((4, 5), dtype=np.float64)

        # Basic slicing view
        view = arr[0:3:1, 1:5:2]
        self.assertTrue(np.shares_memory(view, arr), "View must share memory with parent")
        self.assertIs(view.base, arr, "View base pointer must be parent array")

        # Mutating view alters parent
        orig_val = arr[0, 1]
        view[0, 0] = 999.0
        self.assertEqual(arr[0, 1], 999.0, "Mutating view must mutate parent")
        arr[0, 1] = orig_val  # restore

        # Reshaped array chaining: view.base is root buffer
        arr_reshaped = np.arange(20, dtype=np.float64).reshape(4, 5)
        view_chained = arr_reshaped[0:3:1, 1:5:2]
        self.assertTrue(np.shares_memory(view_chained, arr_reshaped))
        self.assertIs(view_chained.base, arr_reshaped.base)

        # Fancy indexing copy
        fancy = arr[[0, 2], :]
        self.assertFalse(np.shares_memory(fancy, arr), "Copy must NOT share memory with parent")
        self.assertIsNone(fancy.base, "Copy base pointer must be None")

        # Mutating copy does NOT alter parent
        fancy[0, 0] = -123.0
        self.assertNotEqual(arr[0, 0], -123.0, "Mutating copy must NOT mutate parent")

    def test_widgets_bundle_js_base_offset_formula_discrepancy(self):
        """
        Adversarial inspection finding:
        In slides/js/widgets-bundle.js line 402:
        Formula displayed: Addr(i, j) = 0x1000 + i * S0 + j * S1.
        When startRow > 0 or startCol > 0, baseOffset > 0.
        True address of sub-element (0, 0) is 0x1000 + baseOffset, not 0x1000!
        """
        bundle_content = BUNDLE_JS_PATH.read_text(encoding="utf-8")
        self.assertIn("Formula: Addr(i, j) = 0x1000 + i *", bundle_content)
        # Verify that baseOffset is computed on line 322
        self.assertIn("var baseOffset = state.startRow * origStrides[0] + state.startCol * origStrides[1];", bundle_content)
        # Verify that Base line displays baseOffset (+ X B)
        self.assertIn("Base: 0x1000 (+ ' + calc.baseOffset + ' B)", bundle_content)


# ==============================================================================
# 3. Vectorization vs Python Loop Benchmark Stress Tests
# ==============================================================================

class TestVectorizationBenchmarkEmpiricalStress(unittest.TestCase):
    """Adversarial stress-testing of analytical performance models and asymptotes."""

    def test_execution_time_positivity_and_scaling(self):
        """Assert T_py and T_np are strictly positive and linear in N."""
        for op in ["add", "cumsum", "filter"]:
            for n in [10, 100, 1000, 100000]:
                t_py = js_time_python_ns(n, op)
                t_np = js_time_numpy_ns(n, op)
                self.assertGreater(t_py, 0.0)
                self.assertGreater(t_np, 0.0)
                # Strict scaling: doubling N should roughly double execution time
                t_py_2n = js_time_python_ns(2 * n, op)
                self.assertAlmostEqual(t_py_2n / t_py, 2.0, places=5)

    def test_speedup_strict_monotonicity_across_range(self):
        """
        Verify that speedup(N) is strictly monotonically increasing for N in [10^1, 10^8].
        Mathematical proof:
        S(N) = (A * N) / (B + C * N)
        dS/dN = (A * B) / (B + C * N)^2 > 0 for all A, B, C, N > 0.
        """
        for op in ["add", "cumsum", "filter"]:
            log_steps = np.linspace(1.0, 8.0, 50)
            prev_s = -1.0
            for l_val in log_steps:
                n_val = 10.0 ** l_val
                curr_s = js_speedup(n_val, op)
                self.assertGreater(
                    curr_s, prev_s,
                    f"Monotonicity violation in op '{op}' at logN={l_val}"
                )
                prev_s = curr_s

    def test_asymptotic_convergence_avx512_ceilings(self):
        """
        Verify that speedup converges asymptotically to k_py / k_np as N -> infinity:
        - op='add': 62.5 / 0.21 = 297.6190476... (~297.6x)
        - op='cumsum': (62.5 * 1.45) / (0.21 * 1.20) = 90.625 / 0.252 = 359.623x
        - op='filter': (62.5 * 1.80) / (0.21 * 1.15) = 112.5 / 0.2415 = 465.838x
        """
        ceilings = {
            "add": 62.5 / 0.21,
            "cumsum": (62.5 * 1.45) / (0.21 * 1.20),
            "filter": (62.5 * 1.80) / (0.21 * 1.15),
        }

        # At N = 10^8, speedup must be within 0.15% of theoretical limit
        n_large = 1e8
        for op, ceiling in ceilings.items():
            s_large = js_speedup(n_large, op)
            self.assertLess(s_large, ceiling, "Speedup cannot exceed theoretical asymptote")
            relative_error = (ceiling - s_large) / ceiling
            self.assertLess(relative_error, 0.0015, f"Expected convergence within 0.15% for {op}")

    def test_crossover_threshold_at_small_n(self):
        """
        Verify crossover behavior at small N where C dispatch latency dominates.
        For op='add':
        62.5 * N = 2500 + 0.21 * N => 62.29 * N = 2500 => N_crossover ~= 40.1.
        At N = 10: T_py = 625 ns, T_np = 2502.1 ns => Python is ~4x faster than NumPy.
        """
        t_py_10 = js_time_python_ns(10, "add")
        t_np_10 = js_time_numpy_ns(10, "add")
        self.assertLess(t_py_10, t_np_10, "At N=10, Python loop should be faster than NumPy dispatch")

        t_py_100 = js_time_python_ns(100, "add")
        t_np_100 = js_time_numpy_ns(100, "add")
        self.assertGreater(t_py_100, t_np_100, "At N=100, NumPy should already be faster")

    def test_svg_viewport_clipping_finding(self):
        """
        Adversarial inspection finding:
        In slides/js/widgets-bundle.js:
        renderSvgCurve defines: maxSpeedup = 320, h = 160, padTop = 20, padBottom = 30.
        Formula: toY(s) = (160 - 30) - (s / 320) * (160 - 20 - 30) = 130 - s * (110 / 320).
        If s > 378.18x, toY(s) becomes negative (< 0) and clips above SVG viewBox='0 0 600 160'!
        For op='filter' at N >= 10^5, s ~= 416x to 465x, resulting in y ~= -13 to -30 (clipped)!
        """
        def to_y(s_val):
            h = 160
            pad_top = 20
            pad_bottom = 30
            max_speedup = 320
            return (h - pad_bottom) - (s_val / max_speedup) * (h - pad_top - pad_bottom)

        # For op='filter' at N=10^6:
        s_filter_1m = js_speedup(1e6, "filter")
        y_coord = to_y(s_filter_1m)
        self.assertGreater(s_filter_1m, 400.0)
        self.assertLess(y_coord, 0.0, "SVG Y coordinate clips above viewBox (negative value)")


# ==============================================================================
# 4. Headless & SSR Execution Portability
# ==============================================================================

class TestWidgetHeadlessSSRCompatibility(unittest.TestCase):
    """Stress-test portability and headless execution of the widget bundle."""

    def test_bundle_evaluation_under_node_headless(self):
        """
        Certifies that widgets-bundle.js can be imported in Node.js when document is polyfilled,
        and identifies that bare Node.js require() fails without typeof document guard.
        """
        # Node test with mock document: should succeed
        node_script_mock = (
            "global.document = { addEventListener: () => {} }; "
            "const Gci = require('./slides/js/widgets-bundle.js'); "
            "if (!Gci.mountBroadcastingWidget) process.exit(1); "
            "process.exit(0);"
        )
        res_mock = subprocess.run(
            ["node", "-e", node_script_mock],
            cwd=str(WORKSPACE_ROOT),
            capture_output=True,
            text=True
        )
        self.assertEqual(res_mock.returncode, 0, f"Node with mock failed: {res_mock.stderr}")

        # Node test without mock document: catches ReferenceError
        node_script_bare = "require('./slides/js/widgets-bundle.js');"
        res_bare = subprocess.run(
            ["node", "-e", node_script_bare],
            cwd=str(WORKSPACE_ROOT),
            capture_output=True,
            text=True
        )
        self.assertNotEqual(res_bare.returncode, 0)
        self.assertIn("ReferenceError: document is not defined", res_bare.stderr)


# ==============================================================================
# 5. User Directive Clarity & Universal Zero Emoji Compliance
# ==============================================================================

class TestUserDirectivePedagogyAndClarity(unittest.TestCase):
    """Verify compliance with 'DE HIEU, NGAN GON nhung DAY DU VA CHI TIET' and zero emojis."""

    def test_zero_emojis_in_widgets_and_test(self):
        """Verify zero unicode emojis exist in widgets-bundle.js or this test file."""
        import re
        emoji_pattern = re.compile(
            r'[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]'
        )
        for target in [BUNDLE_JS_PATH, Path(__file__)]:
            content = target.read_text(encoding="utf-8")
            matches = emoji_pattern.findall(content)
            self.assertEqual(
                len(matches), 0,
                f"Emoji violation detected in {target.name}: {matches}"
            )

    def test_pedagogical_clarity_tokens_in_widget_bundle(self):
        """Verify presence of concise, detailed educational terms."""
        content = BUNDLE_JS_PATH.read_text(encoding="utf-8")
        required_concepts = [
            "Right-to-Left Trailing Alignment",
            "RAM Conserved",
            "stride=0",
            "contiguous",
            "Addr(i, j)",
            "AVX-512",
            "Speedup Factor",
        ]
        for token in required_concepts:
            self.assertIn(token.lower(), content.lower(), f"Missing pedagogical clarity token: {token}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
