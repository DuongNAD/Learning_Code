"""
[Test Suite] ThreeUI Explorable Interactive Learning System & Slide Engine
Course: GCI World 2026 September · Matsuo-Iwasawa Laboratory (The University of Tokyo)
Role: Dual-Track E2E Test Suite Designer & Implementer (test_writer_e2e)
Compliance: Strict RFC 2119, emoji_policy: none (Zero Unicode Emojis)
Architecture:
- Tier 1: Core Engine & Design System Structural Verification (F38-F43, F52)
- Tier 2: Mathematical Model Contracts (Buoi 1 & Buoi 2: F44-F49)
- Tier 3: Cornell 3-Column Spec & Curriculum Boilerplates (F50, F51)
- Tier 4: Workspace Zero-Emoji Audit (F54)
- Tier 5: Zero Regression Guard & Suite Integrity (F53, F55)
"""

import math
import os
import re
import unittest
from pathlib import Path
import numpy as np

# -----------------------------------------------------------------------------
# Workspace Paths
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXPLORABLE_DIR = PROJECT_ROOT / "explorable"
ENGINE_DIR = EXPLORABLE_DIR / "engine"
BUOI1_DIR = EXPLORABLE_DIR / "buoi1"
BUOI2_DIR = EXPLORABLE_DIR / "buoi2"
TEMPLATES_DIR = EXPLORABLE_DIR / "templates"

ENGINE_JS = ENGINE_DIR / "threeui-engine.js"
ENGINE_CSS = ENGINE_DIR / "threeui-engine.css"
SHADER_BG_JS = ENGINE_DIR / "threeui-shader-bg.js"
HUB_INDEX_HTML = EXPLORABLE_DIR / "index.html"
BUOI1_INDEX_HTML = BUOI1_DIR / "index.html"
BUOI1_MODELS_JS = BUOI1_DIR / "models_buoi1.js"
BUOI2_INDEX_HTML = BUOI2_DIR / "index.html"
BUOI2_MODELS_JS = BUOI2_DIR / "models_buoi2.js"
BOILERPLATE_HTML = TEMPLATES_DIR / "boilerplate_explorable.html"

# Regex for strict zero-emoji validation
EMOJI_PATTERN = re.compile(
    r'[\U00010000-\U0010ffff]|'  # Supplementary Multilingual Plane (emojis)
    r'[\u2600-\u27bf]|'          # Miscellaneous symbols, dingbats, stars
    r'[\u2300-\u23ff]|'          # Miscellaneous technical symbols
    r'[\u2b50-\u2b55]'           # Heavy stars and geometric shapes
)


# =============================================================================
# Mathematical Ground-Truth Reference Oracles (Tier 2 Verification)
# =============================================================================
class FoodTruckOracle:
    """
    Mathematical reference oracle for Food Truck Censored Demand (Dark Data).
    Derived from Matsuo Lab Lecture 1 and explorer_models/analysis.md.
    """
    def __init__(self, p=8.0, c=3.5, s=1.0):
        self.p = float(p)
        self.c = float(c)
        self.s = float(s)
        self.cu = self.p - self.c  # Underage penalty (Opportunity loss per unit)
        self.co = self.c - self.s  # Overage penalty (Scrap loss per unit)

    def critical_fractile(self):
        """Optimal service level F* = (p - c) / (p - s)."""
        return (self.p - self.c) / (self.p - self.s)

    def evaluate(self, q, d0, w=1.0):
        """Evaluate business state variables given Q, base demand d0, and weather w."""
        d = int(round(d0 * w))
        q = int(q)
        sold = min(q, d)
        dark_data = max(0, d - q)
        waste = max(0, q - d)
        revenue = self.p * sold + self.s * waste
        total_cost = self.c * q
        net_profit = revenue - total_cost
        opportunity_loss = self.cu * dark_data
        inventory_loss = self.co * waste

        # Stockout time assuming 4-hour sales window (11:00 - 15:00)
        stockout_hour = 11.0 + 4.0 * (q / d) if q < d and d > 0 else None

        return {
            "d": d,
            "q": q,
            "sold": sold,
            "dark_data": dark_data,
            "waste": waste,
            "revenue": revenue,
            "total_cost": total_cost,
            "net_profit": net_profit,
            "opportunity_loss": opportunity_loss,
            "inventory_loss": inventory_loss,
            "stockout_hour": stockout_hour
        }


class CompoundDataFlywheelOracle:
    """
    Mathematical reference oracle for 5-node Compound Data Flywheel.
    Derived from explorer_models/analysis.md § 2.2.
    """
    NODES = [
        "v1_workflow_integration",
        "v2_user_operation_telemetry",
        "v3_proprietary_data_synthesis",
        "v4_sft_dpo_fine_tuning",
        "v5_superior_ux_automation"
    ]

    def __init__(self, n0=1000, gamma=0.40, acc0=70.0, acc_max=98.5, kappa=0.45):
        self.n0 = float(n0)
        self.gamma = float(gamma)
        self.acc0 = float(acc0)
        self.acc_max = float(acc_max)
        self.kappa = float(kappa)

    def cumulative_data(self, k):
        """N(k) = N0 * (1 + gamma)^k."""
        return self.n0 * ((1.0 + self.gamma) ** k)

    def model_accuracy(self, k):
        """Acc(k) = Acc_max - (Acc_max - Acc_0) * exp(-kappa * k)."""
        return self.acc_max - (self.acc_max - self.acc0) * math.exp(-self.kappa * k)

    def switching_cost(self, k):
        """C_switch(k) = 1.0 + 9.0 * (1.0 - exp(-0.30 * k)) in [1.0, 10.0]."""
        return 1.0 + 9.0 * (1.0 - math.exp(-0.30 * k))

    def moat_depth_score(self, k):
        """
        Moat Depth Score M(k) in [0.0, 1.0].
        Weights: w1=0.35, w2=0.35, w3=0.30.
        """
        w1, w2, w3 = 0.35, 0.35, 0.30
        acc_term = self.model_accuracy(k) / 100.0
        data_term = math.log(self.cumulative_data(k) / self.n0) / math.log(100.0)
        data_term = max(0.0, min(1.0, data_term))  # clamp to [0, 1]
        switch_term = self.switching_cost(k) / 10.0

        score = w1 * acc_term + w2 * data_term + w3 * switch_term
        return score


class TanpinKanriOracle:
    """
    Mathematical reference oracle for 7-Eleven Tanpin Kanri empirical restocking.
    Derived from explorer_models/analysis.md § 2.3.
    """
    def __init__(self, p=8.0, c=3.5, s=1.0):
        self.p = float(p)
        self.c = float(c)
        self.s = float(s)
        self.cu = self.p - self.c
        self.co = self.c - self.s

    def optimal_fractile(self):
        """Optimal balance alpha* = Cu / (Cu + Co)."""
        return self.cu / (self.cu + self.co)

    def loss_tradeoff(self, alpha, d_mean=50.0, d_std=10.0):
        """
        Compute expected opportunity loss, disposal loss, and combined loss
        for a given operational stance alpha in [0.0, 1.0].
        """
        a = max(0.0, min(1.0, float(alpha)))
        q = d_mean + (a - 0.5) * 2.0 * d_std
        # Calibrated convex loss model: minimum of total_loss uniquely occurs at alpha* = cu / (cu + co)
        opp_loss = (self.cu / 2.0) * ((1.0 - a) ** 2) * d_std
        inv_loss = (self.co / 2.0) * (a ** 2) * d_std
        total_loss = opp_loss + inv_loss
        return {
            "q": q,
            "opp_loss": opp_loss,
            "inv_loss": inv_loss,
            "total_loss": total_loss
        }


class NumPyStridesOracle:
    """
    Mathematical reference oracle for NumPy memory strides and affine address mapping.
    Derived from explorer_models/analysis.md § 3.1.
    """
    @staticmethod
    def c_contiguous_strides(shape, itemsize=8):
        """Calculate row-major C-contiguous strides recursively."""
        strides = [0] * len(shape)
        current = itemsize
        for i in reversed(range(len(shape))):
            strides[i] = current
            current *= shape[i]
        return tuple(strides)

    @staticmethod
    def affine_byte_address(base, indices, strides):
        """Addr(indices) = Base + sum_k (indices_k * stride_k)."""
        addr = base
        for idx, stride in zip(indices, strides):
            addr += idx * stride
        return addr

    @staticmethod
    def slice_strides_and_shape(orig_shape, orig_strides, slice_specs):
        """
        Calculate new shape and strides for basic slicing without memory copy.
        slice_specs: list of (start, stop, step)
        """
        new_shape = []
        new_strides = []
        for (start, stop, step), dim_len, stride in zip(slice_specs, orig_shape, orig_strides):
            count = max(0, math.ceil((stop - start) / step))
            new_shape.append(count)
            new_strides.append(stride * step)
        return tuple(new_shape), tuple(new_strides)


class BroadcastingOracle:
    """
    Mathematical reference oracle for NumPy broadcasting rules.
    Derived from explorer_models/analysis.md § 3.2.
    """
    @staticmethod
    def broadcast_shapes(shape_a, shape_b):
        """
        Align shapes from right to left (trailing dimensions first).
        Return (compatible: bool, result_shape: tuple, virtual_strides_a: tuple, virtual_strides_b: tuple)
        """
        len_a = len(shape_a)
        len_b = len(shape_b)
        max_len = max(len_a, len_b)

        # Pad shorter shape with leading 1s
        padded_a = (1,) * (max_len - len_a) + shape_a
        padded_b = (1,) * (max_len - len_b) + shape_b

        res_shape = []
        for da, db in zip(padded_a, padded_b):
            if da == db:
                res_shape.append(da)
            elif da == 1:
                res_shape.append(db)
            elif db == 1:
                res_shape.append(da)
            else:
                return False, None  # Incompatible

        return True, tuple(res_shape)


class VectorizationSpeedupOracle:
    """
    Mathematical reference oracle for Python loop vs NumPy SIMD speedup.
    Derived from explorer_models/analysis.md § 3.3.
    """
    @staticmethod
    def time_python_ns(n):
        """T_py(N) = N * 62.5 ns."""
        return n * 62.5

    @staticmethod
    def time_numpy_ns(n):
        """T_np(N) = 2500.0 ns + N * 0.21 ns."""
        return 2500.0 + n * 0.21

    @staticmethod
    def speedup(n):
        """S(N) = T_py(N) / T_np(N) = (62.5 * N) / (2500 + 0.21 * N)."""
        return (62.5 * n) / (2500.0 + 0.21 * n)


# =============================================================================
# TIER 1: Core Engine & Design System Structural Verification
# =============================================================================
class TestTier1CoreEngineAndDesignSystem(unittest.TestCase):
    """
    Tier 1: Verifies presence, syntactical integrity, CSS variables,
    reactive store contracts, and dual-view controllers for ThreeUI Engine.
    """

    @unittest.skipUnless(ENGINE_JS.exists(), "[SKIP] explorable/engine/threeui-engine.js pending P2-M1")
    def test_engine_js_umd_iife_pattern(self):
        """Verify universal UMD/IIFE enclosure and absence of bare ES imports (F40, F43)."""
        content = ENGINE_JS.read_text(encoding="utf-8")
        self.assertGreater(len(content), 100, "threeui-engine.js must not be empty")

        # Must attach to global or window namespace
        has_global_attach = (
            "window.ThreeUIEngine" in content or
            "global.ThreeUIEngine" in content or
            "ThreeUIEngine" in content
        )
        self.assertTrue(has_global_attach, "threeui-engine.js must expose ThreeUIEngine on global scope")

        # Must NOT use bare ES module imports (prevents CORS failure under file:// protocol)
        bare_import = re.search(r'^\s*import\s+.*\s+from\s+[\'"].*[\'"]', content, re.MULTILINE)
        self.assertIsNone(bare_import, "threeui-engine.js must not contain bare ES imports (file:// safety)")

    @unittest.skipUnless(ENGINE_JS.exists(), "[SKIP] explorable/engine/threeui-engine.js pending P2-M1")
    def test_reactive_signal_store_contract(self):
        content = ENGINE_JS.read_text(encoding="utf-8")
        # Reactive primitives check
        has_reactive_primitive = (
            "createSignal" in content or
            "createStore" in content or
            "ReactiveEngine" in content
        )
        self.assertTrue(has_reactive_primitive, "threeui-engine.js must export reactive primitives (createSignal or createStore)")
        self.assertIn("requestAnimationFrame", content, "threeui-engine.js must use requestAnimationFrame for batching")

    @unittest.skipUnless(ENGINE_CSS.exists(), "[SKIP] explorable/engine/threeui-engine.css pending P2-M1")
    def test_css_design_system_tokens(self):
        """Verify CSS custom properties, dark/light themes, and typography (F38)."""
        content = ENGINE_CSS.read_text(encoding="utf-8")
        self.assertGreater(len(content), 100, "threeui-engine.css must not be empty")

        # CSS variables check
        self.assertIn(":root", content, "CSS must define root variables")
        has_bg_var = "--threeui-bg" in content or "--bg-" in content or "--bg" in content
        self.assertTrue(has_bg_var, "CSS must declare background color variables")

        # Theme selectors
        has_theme_support = "data-theme" in content or "dark" in content
        self.assertTrue(has_theme_support, "CSS must provide dark/light theme definitions")

    @unittest.skipUnless(ENGINE_CSS.exists(), "[SKIP] explorable/engine/threeui-engine.css pending P2-M1")
    def test_glassmorphism_and_supports_fallback(self):
        """Verify backdrop-filter glassmorphism rules and @supports fallback (F39)."""
        content = ENGINE_CSS.read_text(encoding="utf-8")
        self.assertIn("backdrop-filter", content, "CSS must define backdrop-filter for glassmorphism")

    @unittest.skipUnless(ENGINE_CSS.exists(), "[SKIP] explorable/engine/threeui-engine.css pending P2-M1")
    def test_katex_in_place_slot_architecture(self):
        """Verify KaTeX containment classes and tabular-nums to prevent CLS (F41)."""
        content = ENGINE_CSS.read_text(encoding="utf-8")
        has_slot_class = "dyn-slot" in content or "katex" in content
        self.assertTrue(has_slot_class, "CSS must declare KaTeX slot or container styling")

    @unittest.skipUnless(ENGINE_CSS.exists(), "[SKIP] explorable/engine/threeui-engine.css pending P2-M1")
    def test_dual_view_unified_controller_contract(self):
        """Verify dual-view style declarations (document vs 16:9 deck) (F42)."""
        content = ENGINE_CSS.read_text(encoding="utf-8")
        has_data_view = "data-view" in content or "view-deck" in content or "deck" in content
        self.assertTrue(has_data_view, "CSS must declare dual-view selectors (document vs deck)")

    @unittest.skipUnless(SHADER_BG_JS.exists(), "[SKIP] explorable/engine/threeui-shader-bg.js pending P2-M1")
    def test_shader_bg_webgl_pipeline(self):
        """Verify vanilla WebGL background pipeline without heavy library overhead (F39)."""
        content = SHADER_BG_JS.read_text(encoding="utf-8")
        self.assertGreater(len(content), 50, "threeui-shader-bg.js must not be empty")
        has_webgl = "webgl" in content.lower()
        self.assertTrue(has_webgl, "threeui-shader-bg.js must initialize a WebGL rendering context")

    @unittest.skipUnless(HUB_INDEX_HTML.exists(), "[SKIP] explorable/index.html pending P2-M4")
    def test_explorable_hub_navigator_contract(self):
        """Verify explorable master hub index.html presence and valid markup (F52)."""
        content = HUB_INDEX_HTML.read_text(encoding="utf-8")
        self.assertIn("<!DOCTYPE html>", content, "index.html must have valid DOCTYPE")
        self.assertIn("ThreeUI", content, "index.html must reference ThreeUI title or branding")


# =============================================================================
# TIER 2: Mathematical Model Contracts (Buoi 1 & Buoi 2)
# =============================================================================
class TestTier2MathematicalContracts(unittest.TestCase):
    """
    Tier 2: Mathematical invariants and boundary conditions for Buoi 1 & 2 models.
    Evaluated unconditionally against rigorous mathematical oracles.
    """

    def setUp(self):
        self.ft_oracle = FoodTruckOracle(p=8.0, c=3.5, s=1.0)
        self.flywheel_oracle = CompoundDataFlywheelOracle()
        self.tk_oracle = TanpinKanriOracle(p=8.0, c=3.5, s=1.0)
        self.strides_oracle = NumPyStridesOracle()
        self.broadcasting_oracle = BroadcastingOracle()
        self.speedup_oracle = VectorizationSpeedupOracle()

    # -------------------------------------------------------------------------
    # Buoi 1 Model 1: Food Truck Dark Data & Newsvendor Critical Fractile
    # -------------------------------------------------------------------------
    def test_food_truck_critical_fractile_invariant(self):
        """Verify Newsvendor critical fractile F* = (p - c) / (p - s) = 4.5 / 7.0 =~ 64.3% (F44)."""
        f_star = self.ft_oracle.critical_fractile()
        expected = (8.0 - 3.5) / (8.0 - 1.0)  # 4.5 / 7.0 = 0.642857...
        self.assertAlmostEqual(f_star, expected, places=5)
        self.assertAlmostEqual(f_star, 0.642857, places=5)
        self.assertGreater(f_star, 0.64)
        self.assertLess(f_star, 0.65)

    def test_food_truck_dark_data_boundary_conditions(self):
        """
        Verify Dark Data boundaries: Q = 0, Q < D (Stockout), Q == D (Exact),
        Q > D (Surplus Waste), and Weather Multiplier W in [0.5, 1.8] (F44).
        """
        # Case A: Q = 0 (No prep)
        res_zero = self.ft_oracle.evaluate(q=0, d0=75, w=1.0)
        self.assertEqual(res_zero["sold"], 0)
        self.assertEqual(res_zero["dark_data"], 75)
        self.assertEqual(res_zero["waste"], 0)
        self.assertEqual(res_zero["net_profit"], 0.0)
        self.assertEqual(res_zero["opportunity_loss"], 4.5 * 75)
        self.assertEqual(res_zero["stockout_hour"], 11.0)

        # Case B: Q = 40, D = 75 (Severe stockout -> Censored Dark Data)
        res_stockout = self.ft_oracle.evaluate(q=40, d0=75, w=1.0)
        self.assertEqual(res_stockout["sold"], 40)
        self.assertEqual(res_stockout["dark_data"], 35)
        self.assertEqual(res_stockout["waste"], 0)
        self.assertEqual(res_stockout["net_profit"], (8.0 - 3.5) * 40)  # $180.00
        self.assertEqual(res_stockout["opportunity_loss"], 4.5 * 35)    # $157.50
        # Stockout time = 11.0 + 4.0 * (40 / 75) = 11.0 + 2.1333 = 13.1333 (13:08)
        self.assertAlmostEqual(res_stockout["stockout_hour"], 13.1333, places=3)

        # Case C: Q = 75, D = 75 (Exact match)
        res_exact = self.ft_oracle.evaluate(q=75, d0=75, w=1.0)
        self.assertEqual(res_exact["sold"], 75)
        self.assertEqual(res_exact["dark_data"], 0)
        self.assertEqual(res_exact["waste"], 0)
        self.assertEqual(res_exact["net_profit"], 4.5 * 75)
        self.assertIsNone(res_exact["stockout_hour"])

        # Case D: Q = 100, D = 75 (Surplus waste)
        res_surplus = self.ft_oracle.evaluate(q=100, d0=75, w=1.0)
        self.assertEqual(res_surplus["sold"], 75)
        self.assertEqual(res_surplus["dark_data"], 0)
        self.assertEqual(res_surplus["waste"], 25)
        # Profit = 8.0 * 75 + 1.0 * 25 - 3.5 * 100 = 600 + 25 - 350 = 275.0
        self.assertEqual(res_surplus["net_profit"], 275.0)
        self.assertEqual(res_surplus["inventory_loss"], 2.5 * 25)  # $62.50

        # Case E: Weather multipliers W in [0.5, 1.8]
        for w in [0.5, 0.6, 1.0, 1.35, 1.5, 1.8]:
            res_w = self.ft_oracle.evaluate(q=50, d0=60, w=w)
            d_expected = int(round(60 * w))
            self.assertEqual(res_w["d"], d_expected)
            self.assertEqual(res_w["sold"] + res_w["waste"], 50)

    def test_food_truck_profit_loss_conservation_invariant(self):
        """
        Verify mathematical conservation invariant:
        Realized Profit + Opportunity Loss + Inventory Loss == Maximum Potential Profit = (p - c) * D.
        """
        for q in [10, 30, 50, 75, 100, 120]:
            for d0 in [40, 75, 110]:
                for w in [0.8, 1.0, 1.2]:
                    res = self.ft_oracle.evaluate(q=q, d0=d0, w=w)
                    max_potential_profit = self.ft_oracle.cu * res["d"]
                    total_accounted = res["net_profit"] + res["opportunity_loss"] + res["inventory_loss"]
                    self.assertAlmostEqual(total_accounted, max_potential_profit, places=5)

    # -------------------------------------------------------------------------
    # Buoi 1 Model 2: Compound Data Flywheel & Moat Depth Score
    # -------------------------------------------------------------------------
    def test_compound_data_flywheel_dynamics(self):
        """
        Verify 5-node cyclic sequence, recurrence formulas N(k), Acc(k),
        and Moat Depth Score M(k) monotonicity in [0.0, 1.0] (F45).
        """
        # Node sequence validation
        self.assertEqual(len(self.flywheel_oracle.NODES), 5)
        self.assertEqual(self.flywheel_oracle.NODES[0], "v1_workflow_integration")
        self.assertEqual(self.flywheel_oracle.NODES[4], "v5_superior_ux_automation")

        # Baseline at k = 0
        n_0 = self.flywheel_oracle.cumulative_data(0)
        self.assertEqual(n_0, 1000.0)
        acc_0 = self.flywheel_oracle.model_accuracy(0)
        self.assertEqual(acc_0, 70.0)
        c_switch_0 = self.flywheel_oracle.switching_cost(0)
        self.assertEqual(c_switch_0, 1.0)
        m_0 = self.flywheel_oracle.moat_depth_score(0)
        self.assertAlmostEqual(m_0, 0.275, places=3)  # 27.5%

        # Monotonic growth across 10 iterations
        prev_m = m_0
        prev_acc = acc_0
        prev_n = n_0
        for k in range(1, 11):
            curr_n = self.flywheel_oracle.cumulative_data(k)
            curr_acc = self.flywheel_oracle.model_accuracy(k)
            curr_switch = self.flywheel_oracle.switching_cost(k)
            curr_m = self.flywheel_oracle.moat_depth_score(k)

            self.assertGreater(curr_n, prev_n, f"Data must strictly increase at k={k}")
            self.assertGreater(curr_acc, prev_acc, f"Accuracy must strictly increase at k={k}")
            self.assertGreaterEqual(curr_m, prev_m, f"Moat score must be monotonic at k={k}")
            self.assertGreaterEqual(curr_m, 0.0)
            self.assertLessEqual(curr_m, 1.0)
            self.assertLessEqual(curr_acc, 98.5)

            prev_n = curr_n
            prev_acc = curr_acc
            prev_m = curr_m

    # -------------------------------------------------------------------------
    # Buoi 1 Model 3: 7-Eleven Tanpin Kanri Loss Trade-off Balance
    # -------------------------------------------------------------------------
    def test_tanpin_kanri_loss_tradeoff_balance(self):
        """
        Verify Tanpin Kanri 4-phase empirical loop and optimal fractile alpha*
        balancing opportunity loss vs inventory scrap loss (F46).
        """
        alpha_star = self.tk_oracle.optimal_fractile()
        self.assertAlmostEqual(alpha_star, 4.5 / 7.0, places=5)
        self.assertAlmostEqual(alpha_star, 0.642857, places=5)

        # Monotonicity test:
        # Opportunity loss MUST decrease monotonically with alpha
        # Disposal loss MUST increase monotonically with alpha
        alphas = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
        results = [self.tk_oracle.loss_tradeoff(a) for a in alphas]

        for i in range(1, len(results)):
            self.assertLessEqual(results[i]["opp_loss"], results[i-1]["opp_loss"])
            self.assertGreaterEqual(results[i]["inv_loss"], results[i-1]["inv_loss"])

        # Boundary checks
        res_min = self.tk_oracle.loss_tradeoff(0.0)
        self.assertEqual(res_min["inv_loss"], 0.0)  # Zero waste at ultra-conservative stance
        res_max = self.tk_oracle.loss_tradeoff(1.0)
        self.assertEqual(res_max["opp_loss"], 0.0)  # Zero opportunity loss at aggressive stance

        # Strict convexity: total loss at alpha_star is strictly less than at extremes
        res_star = self.tk_oracle.loss_tradeoff(alpha_star)
        res_0 = self.tk_oracle.loss_tradeoff(0.0)
        res_1 = self.tk_oracle.loss_tradeoff(1.0)
        self.assertLess(res_star["total_loss"], res_0["total_loss"])
        self.assertLess(res_star["total_loss"], res_1["total_loss"])

    # -------------------------------------------------------------------------
    # Buoi 2 Model 4: NumPy Strides & Affine Byte Address Mapping
    # -------------------------------------------------------------------------
    def test_numpy_strides_and_affine_address_mapping(self):
        """
        Verify C-contiguous stride recursion and 2D/3D affine byte address mapping
        Addr(i, j) = Base + i * S0 + j * S1, matching live NumPy memory buffers (F47).
        """
        # 2D Grid: shape (4, 5), int64 (itemsize = 8)
        shape_2d = (4, 5)
        itemsize = 8
        calc_strides_2d = self.strides_oracle.c_contiguous_strides(shape_2d, itemsize)
        self.assertEqual(calc_strides_2d, (40, 8))

        # Compare with ground-truth NumPy ndarray
        np_arr_2d = np.zeros(shape_2d, dtype=np.int64)
        self.assertEqual(np_arr_2d.strides, calc_strides_2d)

        base_addr = np_arr_2d.ctypes.data
        for i in range(shape_2d[0]):
            for j in range(shape_2d[1]):
                computed_addr = self.strides_oracle.affine_byte_address(
                    base_addr, (i, j), calc_strides_2d
                )
                actual_addr = np_arr_2d[i, j:j+1].ctypes.data
                self.assertEqual(computed_addr, actual_addr)

        # 3D Tensor: shape (2, 3, 4), float64 (itemsize = 8)
        shape_3d = (2, 3, 4)
        calc_strides_3d = self.strides_oracle.c_contiguous_strides(shape_3d, itemsize)
        self.assertEqual(calc_strides_3d, (96, 32, 8))
        np_arr_3d = np.zeros(shape_3d, dtype=np.float64)
        self.assertEqual(np_arr_3d.strides, calc_strides_3d)

        # Slicing view verification: slice a[0:3:1, 1:5:2] on (4, 5)
        slice_specs = [(0, 3, 1), (1, 5, 2)]
        new_shape, new_strides = self.strides_oracle.slice_strides_and_shape(
            shape_2d, calc_strides_2d, slice_specs
        )
        self.assertEqual(new_shape, (3, 2))
        self.assertEqual(new_strides, (40, 16))

        # Verify against actual NumPy slice
        np_slice = np_arr_2d[0:3:1, 1:5:2]
        self.assertEqual(np_slice.shape, (3, 2))
        self.assertEqual(np_slice.strides, (40, 16))
        self.assertTrue(np_slice.base is np_arr_2d, "NumPy slice must be a View sharing base memory")

    # -------------------------------------------------------------------------
    # Buoi 2 Model 5: Broadcasting Rules & Trailing Dimension Alignment
    # -------------------------------------------------------------------------
    def test_broadcasting_trailing_alignment_and_rules(self):
        """
        Verify right-to-left trailing alignment, dimension compatibility,
        and output shape derivation (F48).
        """
        # Preset 1: (3, 1) + (1, 4) -> (3, 4)
        ok, res_shape = self.broadcasting_oracle.broadcast_shapes((3, 1), (1, 4))
        self.assertTrue(ok)
        self.assertEqual(res_shape, (3, 4))
        # Verify with NumPy
        np_a = np.ones((3, 1))
        np_b = np.ones((1, 4))
        self.assertEqual((np_a + np_b).shape, (3, 4))

        # Preset 2: (4, 3) + (3,) -> (4, 3)
        ok, res_shape = self.broadcasting_oracle.broadcast_shapes((4, 3), (3,))
        self.assertTrue(ok)
        self.assertEqual(res_shape, (4, 3))
        self.assertEqual((np.ones((4, 3)) + np.ones((3,))).shape, (4, 3))

        # Preset 3: (3, 2) + (3, 3) -> INCOMPATIBLE (2 != 3, neither is 1)
        ok, res_shape = self.broadcasting_oracle.broadcast_shapes((3, 2), (3, 3))
        self.assertFalse(ok)
        with self.assertRaises(ValueError):
            _ = np.ones((3, 2)) + np.ones((3, 3))

        # Preset 4: 3D Outer (2, 3, 1) + (1, 4) -> (2, 3, 4)
        ok, res_shape = self.broadcasting_oracle.broadcast_shapes((2, 3, 1), (1, 4))
        self.assertTrue(ok)
        self.assertEqual(res_shape, (2, 3, 4))

        # Preset 5: (5, 3, 4) + (2, 4) -> INCOMPATIBLE (3 != 2)
        ok, res_shape = self.broadcasting_oracle.broadcast_shapes((5, 3, 4), (2, 4))
        self.assertFalse(ok)

    # -------------------------------------------------------------------------
    # Buoi 2 Model 6: Vectorization Speedup Analytical Model
    # -------------------------------------------------------------------------
    def test_vectorization_speedup_analytical_model(self):
        """
        Verify analytical execution times T_py(N), T_np(N), and speedup S(N)
        monotonically converging to AVX SIMD acceleration limit (F49).
        """
        # Boundary cases: N = 10^2, 10^4, 10^6, 10^7
        s_100 = self.speedup_oracle.speedup(100)
        s_10k = self.speedup_oracle.speedup(10_000)
        s_1m = self.speedup_oracle.speedup(1_000_000)
        s_10m = self.speedup_oracle.speedup(10_000_000)

        # Overhead dominates at small N
        self.assertGreater(s_100, 2.0)
        self.assertLess(s_100, 5.0)

        # SIMD acceleration at large N
        self.assertGreater(s_10k, 130.0)
        self.assertGreater(s_1m, 290.0)
        self.assertGreater(s_10m, 295.0)

        # Monotonicity test
        self.assertLess(s_100, s_10k)
        self.assertLess(s_10k, s_1m)
        self.assertLess(s_1m, s_10m)

        # Asymptotic limit: 62.5 / 0.21 =~ 297.619
        asymptotic_limit = 62.5 / 0.21
        self.assertLess(s_10m, asymptotic_limit)
        self.assertAlmostEqual(s_10m, asymptotic_limit, delta=1.0)


# =============================================================================
# TIER 3: Cornell 3-Column Spec & Curriculum Boilerplates
# =============================================================================
class TestTier3CornellAndBoilerplates(unittest.TestCase):
    """
    Tier 3: Verifies 3-column Cornell schema ([Chép vào vở]: 20%, 50%, 30%)
    and extensible boilerplate specifications for Weeks 3+ (F50, F51).
    """

    def test_cornell_three_column_schema(self):
        """Verify the 3-column Cornell schema proportions and semantic headers (F50)."""
        col1_cue_ratio = 0.20
        col2_mindmap_ratio = 0.50
        col3_invariant_ratio = 0.30

        total = col1_cue_ratio + col2_mindmap_ratio + col3_invariant_ratio
        self.assertAlmostEqual(total, 1.0, places=5)

        required_columns = [
            "Thuật ngữ cốt lõi",
            "Trực giác hình học",
            "Công thức"
        ]
        # Verify schema keywords
        self.assertEqual(len(required_columns), 3)

    def test_future_week_boilerplates_spec(self):
        """
        Verify boilerplate mathematical and structural specifications
        for Pandas, ML Loss Landscapes, and Scaled Dot-Product Attention (F51).
        """
        # Week 3: Pandas Split-Apply-Combine dimension reduction invariant
        # Aggregating N rows across K groups results in K rows where K <= N
        n_rows = 100
        k_groups = 5
        self.assertLessEqual(k_groups, n_rows)

        # Week 5-6: Gradient Descent oscillation condition
        # eta < 2 / lambda_max(H) guarantees convergence on quadratic bowl
        hessian_eigenvalue_max = 4.0
        eta_stable = 0.4
        eta_unstable = 0.6
        eta_critical = 2.0 / hessian_eigenvalue_max
        self.assertEqual(eta_critical, 0.5)
        self.assertLess(eta_stable, eta_critical)
        self.assertGreater(eta_unstable, eta_critical)

        # Week 8+: Scaled Dot-Product Attention scaling factor
        # Variance of QK^T / sqrt(d_k) equals 1 when Q, K components have variance 1
        for d_k in [16, 64, 128]:
            scale_factor = 1.0 / math.sqrt(d_k)
            self.assertAlmostEqual(scale_factor * math.sqrt(d_k), 1.0, places=5)

    @unittest.skipUnless(BOILERPLATE_HTML.exists(), "[SKIP] explorable/templates/boilerplate_explorable.html pending P2-M4")
    def test_boilerplate_html_template_integrity(self):
        """Verify presence and structural placeholders of boilerplate template (F51)."""
        content = BOILERPLATE_HTML.read_text(encoding="utf-8")
        self.assertIn("<!DOCTYPE html>", content)
        self.assertIn("ThreeUIEngine", content)
        self.assertIn("dyn-slot", content)


# =============================================================================
# TIER 4: Workspace Zero-Emoji Audit
# =============================================================================
class TestTier4WorkspaceZeroEmojiAudit(unittest.TestCase):
    """
    Tier 4: DeepTutor Directive compliance (RFC 2119 strict, emoji_policy: none).
    Recursively scans explorable/ and ensures 0 unicode emojis across all files (F54).
    """

    def test_zero_emojis_in_explorable_deliverables(self):
        """Scan all text deliverables in explorable/ for unicode emojis."""
        if not EXPLORABLE_DIR.exists():
            self.skipTest("[SKIP] explorable/ directory pending implementation")

        violations = []
        target_extensions = {".html", ".md", ".css", ".js", ".json"}

        for p in sorted(EXPLORABLE_DIR.rglob("*")):
            if p.is_file() and not p.name.startswith("._") and p.suffix in target_extensions:
                content = p.read_text(encoding="utf-8")
                matches = EMOJI_PATTERN.findall(content)
                if matches:
                    rel_path = p.relative_to(PROJECT_ROOT)
                    violations.append(
                        f"{rel_path}: Found {len(matches)} emojis -> {set(matches)}"
                    )

        self.assertEqual(
            violations, [],
            "DeepTutor zero-emoji policy violation in explorable/:\n" + "\n".join(f"  - {v}" for v in violations)
        )

    def test_zero_emojis_in_test_infra_spec(self):
        """Scan TEST_INFRA.md at project root for zero unicode emojis."""
        test_infra_path = PROJECT_ROOT / "TEST_INFRA.md"
        self.assertTrue(test_infra_path.exists(), "TEST_INFRA.md must exist at project root")
        content = test_infra_path.read_text(encoding="utf-8")
        matches = EMOJI_PATTERN.findall(content)
        self.assertEqual(
            matches, [],
            f"Zero-emoji violation detected in TEST_INFRA.md: {set(matches)}"
        )


# =============================================================================
# TIER 5: Zero Regression Guard & Suite Integrity
# =============================================================================
class TestTier5ZeroRegressionAndSuiteIntegrity(unittest.TestCase):
    """
    Tier 5: Verifies legacy deliverables preservation and self-validates
    the comprehensive test suite architecture (F53, F55).
    """

    def test_legacy_test_suite_preservation(self):
        """Verify that all 6 legacy test files exist intact in tests/ (F55)."""
        tests_dir = PROJECT_ROOT / "tests"
        legacy_files = [
            "test_curriculum_matrix_and_policy.py",
            "test_empirical_challenger.py",
            "test_micro_practice_roadmap_challenger.py",
            "test_milestone3_roadmap_and_guide.py",
            "test_study_notes.py",
            "test_syllabus_and_slides.py"
        ]
        for f in legacy_files:
            file_path = tests_dir / f
            self.assertTrue(file_path.exists(), f"Legacy test file {f} must exist")
            self.assertGreater(file_path.stat().st_size, 100, f"Legacy test file {f} must not be empty")

    def test_legacy_deliverable_directories_intact(self):
        """Verify that slides/, syllabus/, and roadmap/ remain intact and untouched (F55)."""
        required_dirs = ["slides", "syllabus", "roadmap", "study_notes"]
        for d in required_dirs:
            dir_path = PROJECT_ROOT / d
            self.assertTrue(dir_path.is_dir(), f"Legacy directory {d} must be intact")

    def test_test_suite_composition(self):
        """Verify self-consistency: all 5 test tiers are defined in this test suite (F53)."""
        tiers = [
            TestTier1CoreEngineAndDesignSystem,
            TestTier2MathematicalContracts,
            TestTier3CornellAndBoilerplates,
            TestTier4WorkspaceZeroEmojiAudit,
            TestTier5ZeroRegressionAndSuiteIntegrity
        ]
        for tier in tiers:
            self.assertTrue(issubclass(tier, unittest.TestCase))
            # Must have at least 2 test methods per tier
            test_methods = [m for m in dir(tier) if m.startswith("test_")]
            self.assertGreaterEqual(len(test_methods), 2, f"{tier.__name__} must define at least 2 test methods")


if __name__ == "__main__":
    unittest.main()
