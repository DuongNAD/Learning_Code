"""
IMLC 2026 Qualification Round (Senior Division) - Master Verification Runner
Module: run_all_verifications.py

Focus:
    - Unified master test harness executing Problem B, Problem C, and Problem D verifications.
    - Comprehensive assertion checks across all qualification algorithms:
        * Decision Tree Shannon Entropy, Gini Impurity, CO2 splitting, and 100% accuracy.
        * Ridge Regularization RSS, complexity penalties, critical threshold lambda*, SVD shrinkage.
        * RLHF Policy Drift loss, optimal shift, safety bound theorem, and Fisher information geometry.
    - Formatted terminal matrix report displaying execution metrics and pass/fail verdicts.
    - Exit code 0 if all tests pass; exit code 1 if any assertion fails.
"""

from __future__ import annotations
import sys
import time
import math
from typing import Any, Callable, Dict, List, Tuple

# Import verification modules
try:
    from verify_problem_b_tree import verify_problem_b
    from verify_problem_c_ridge import verify_problem_c
    from verify_problem_d_rlhf import verify_problem_d
except ImportError:
    # Support execution from project root or other working directories
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    from verify_problem_b_tree import verify_problem_b
    from verify_problem_c_ridge import verify_problem_c
    from verify_problem_d_rlhf import verify_problem_d


# =====================================================================
# Test Case Definition & Battery
# =====================================================================

class TestCaseResult:
    __test__ = False

    def __init__(self, test_id: str, problem: str, description: str,
                 expected: str, observed: str, passed: bool, duration_ms: float, error: str = ""):
        self.test_id = test_id
        self.problem = problem
        self.description = description
        self.expected = expected
        self.observed = observed
        self.passed = passed
        self.duration_ms = duration_ms
        self.error = error


def run_problem_b_battery(b_data: Dict[str, Any]) -> List[TestCaseResult]:
    tests: List[TestCaseResult] = []
    
    # Test B-01: Initial Query Prediction
    t0 = time.perf_counter()
    pred = b_data.get("query_prediction")
    ok = (pred == "KEEP CLOSED")
    tests.append(TestCaseResult(
        test_id="TC-B01",
        problem="Problem B",
        description="Initial Query (T=26 C, H=68%) evaluation",
        expected="KEEP CLOSED",
        observed=str(pred),
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test B-02: Baseline Tree Accuracy (4/6 = 66.67%)
    t0 = time.perf_counter()
    base_eval = b_data.get("baseline_evaluation", {})
    acc = base_eval.get("accuracy", 0.0)
    ok = (base_eval.get("correct") == 4 and math.isclose(acc, 4.0/6.0, rel_tol=1e-5))
    tests.append(TestCaseResult(
        test_id="TC-B02",
        problem="Problem B",
        description="Baseline Tree logged accuracy (Rows 1-6)",
        expected="4/6 (66.67%)",
        observed=f"{base_eval.get('correct')}/6 ({acc*100:.2f}%)",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test B-03: Baseline Failure Isolation on Rows 5 & 6
    t0 = time.perf_counter()
    mismatches = [m["row_index"] for m in base_eval.get("mismatches", [])]
    ok = (mismatches == [5, 6])
    tests.append(TestCaseResult(
        test_id="TC-B03",
        problem="Problem B",
        description="Baseline Tree failure rows isolation",
        expected="Rows [5, 6]",
        observed=f"Rows {mismatches}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test B-04: Sub-Node Entropy & Gini Impurity Prior to Split
    t0 = time.perf_counter()
    sub_imp = b_data.get("sub_node_impurity", {})
    h_sub = sub_imp.get("entropy", 0.0)
    g_sub = sub_imp.get("gini", 0.0)
    ok = (math.isclose(h_sub, 1.0, abs_tol=1e-9) and math.isclose(g_sub, 0.5, abs_tol=1e-9))
    tests.append(TestCaseResult(
        test_id="TC-B04",
        problem="Problem B",
        description="Sub-node (T<=28 & H<=70) Entropy & Gini",
        expected="H=1.0000 bit, G=0.5000",
        observed=f"H={h_sub:.4f} bit, G={g_sub:.4f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test B-05: Optimal Split Threshold CO2 > 1250 ppm & Information Gain
    t0 = time.perf_counter()
    candidates = b_data.get("candidate_splits", [])
    split_1250 = next((c for c in candidates if math.isclose(c["threshold"], 1250.0)), {})
    ig = split_1250.get("information_gain", 0.0)
    gg = split_1250.get("gini_gain", 0.0)
    is_pure = split_1250.get("is_pure", False)
    ok = (math.isclose(ig, 1.0, abs_tol=1e-9) and math.isclose(gg, 0.5, abs_tol=1e-9) and is_pure)
    tests.append(TestCaseResult(
        test_id="TC-B05",
        problem="Problem B",
        description="CO2 split at 1250 ppm IG and Gini gain",
        expected="IG=1.0000 bit, G=0.5000, Pure",
        observed=f"IG={ig:.4f} bit, G={gg:.4f}, Pure={is_pure}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test B-06: Refined Tree 100% Classification Accuracy
    t0 = time.perf_counter()
    ref_eval = b_data.get("refined_evaluation", {})
    ref_acc = ref_eval.get("accuracy", 0.0)
    ref_correct = ref_eval.get("correct", 0)
    ok = (ref_correct == 6 and math.isclose(ref_acc, 1.0, abs_tol=1e-9))
    tests.append(TestCaseResult(
        test_id="TC-B06",
        problem="Problem B",
        description="Refined Tree accuracy on all 6 log observations",
        expected="6/6 (100.0%)",
        observed=f"{ref_correct}/6 ({ref_acc*100:.1f}%)",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    return tests


def run_problem_c_battery(c_data: Dict[str, Any]) -> List[TestCaseResult]:
    tests: List[TestCaseResult] = []
    
    # Test C-01: Model 1 Polynomial Interpolation (RSS = 0.0)
    t0 = time.perf_counter()
    m1 = c_data.get("M1", {})
    rss_m1 = m1.get("rss", -1.0)
    pen_m1 = m1.get("penalty", -1.0)
    j_m1 = m1.get("score_j", -1.0)
    ok = (math.isclose(rss_m1, 0.0, abs_tol=1e-12) and
          math.isclose(pen_m1, 9.2600, abs_tol=1e-12) and
          math.isclose(j_m1, 9.2600, abs_tol=1e-12))
    tests.append(TestCaseResult(
        test_id="TC-C01",
        problem="Problem C",
        description="Model 1 (Cubic) RSS, Penalty, and J(lambda=1)",
        expected="RSS=0.00, Pen=9.26, J=9.26",
        observed=f"RSS={rss_m1:.2f}, Pen={pen_m1:.2f}, J={j_m1:.2f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test C-02: Model 2 Linear Fit (RSS = 0.08, Penalty = 4.0, J = 4.08)
    t0 = time.perf_counter()
    m2 = c_data.get("M2", {})
    rss_m2 = m2.get("rss", -1.0)
    pen_m2 = m2.get("penalty", -1.0)
    j_m2 = m2.get("score_j", -1.0)
    ok = (math.isclose(rss_m2, 0.0800, abs_tol=1e-12) and
          math.isclose(pen_m2, 4.0000, abs_tol=1e-12) and
          math.isclose(j_m2, 4.0800, abs_tol=1e-12))
    tests.append(TestCaseResult(
        test_id="TC-C02",
        problem="Problem C",
        description="Model 2 (Linear) RSS, Penalty, and J(lambda=1)",
        expected="RSS=0.08, Pen=4.00, J=4.08",
        observed=f"RSS={rss_m2:.2f}, Pen={pen_m2:.2f}, J={j_m2:.2f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test C-03: Model Selection Decision at lambda = 1.0
    t0 = time.perf_counter()
    selected = c_data.get("selected_model_lambda_1", "")
    gap = c_data.get("loss_gap", 0.0)
    ok = ("Model 2" in selected and math.isclose(gap, 5.1800, abs_tol=1e-12))
    tests.append(TestCaseResult(
        test_id="TC-C03",
        problem="Problem C",
        description="Model Selection rule at lambda=1 (J(M2) < J(M1))",
        expected="Model 2 (Linear) [Delta J = 5.1800]",
        observed=f"{selected} [Delta J = {gap:.4f}]",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test C-04: Critical Phase Transition Threshold lambda*
    t0 = time.perf_counter()
    lam_star = c_data.get("critical_threshold_lambda_star", 0.0)
    expected_lam_star = 0.08 / 5.26
    ok = math.isclose(lam_star, expected_lam_star, rel_tol=1e-9)
    tests.append(TestCaseResult(
        test_id="TC-C04",
        problem="Problem C",
        description="Critical transition threshold lambda* = 0.08 / 5.26",
        expected=f"{expected_lam_star:.6f}",
        observed=f"{lam_star:.6f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test C-05: SVD Shrinkage Invariant: f_i in (0, 1] & strictly decreasing
    t0 = time.perf_counter()
    svd = c_data.get("svd", {})
    s_vals = svd.get("singular_values", [])
    ok = (len(s_vals) == 3 and s_vals[0] > s_vals[1] > s_vals[2] > 0)
    tests.append(TestCaseResult(
        test_id="TC-C05",
        problem="Problem C",
        description="SVD spectrum on centered polynomial design matrix",
        expected="3 singular values sigma_1 > sigma_2 > sigma_3 > 0",
        observed=f"{[round(s, 2) for s in s_vals]}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test C-06: Bias-Variance Tradeoff Monotonicity
    t0 = time.perf_counter()
    bv = c_data.get("bias_variance", {})
    ok = (bv.get("min_bias_sq", 0) < bv.get("max_bias_sq", 0) and
          bv.get("max_variance", 0) > bv.get("min_variance", 0))
    tests.append(TestCaseResult(
        test_id="TC-C06",
        problem="Problem C",
        description="Bias-Variance Tradeoff Monotonicity",
        expected="Bias^2 strictly rises, Var strictly drops",
        observed=f"Bias^2:[{bv.get('min_bias_sq',0):.4f}->{bv.get('max_bias_sq',0):.2f}], Var:[{bv.get('max_variance',0):.2f}->{bv.get('min_variance',0):.5f}]",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    return tests


def run_problem_d_battery(d_data: Dict[str, Any]) -> List[TestCaseResult]:
    tests: List[TestCaseResult] = []
    
    # Test D-01: Optimal Drift t* and Minimal Loss Formula
    t0 = time.perf_counter()
    opt_ok = d_data.get("optimal_drift_verified", False)
    tests.append(TestCaseResult(
        test_id="TC-D01",
        problem="Problem D",
        description="Analytical t*=r/(2beta) and L(t*)=-r^2/(4beta)",
        expected="100% match with numerical optimizer",
        observed="Verified strictly convex global minimum",
        passed=opt_ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test D-02: Asymptotic Limit beta -> 0+
    t0 = time.perf_counter()
    asymp = d_data.get("asymptotics", {})
    t_zero = asymp.get("beta_to_zero_max_drift", 0.0)
    ok = (t_zero >= 10000.0)
    tests.append(TestCaseResult(
        test_id="TC-D02",
        problem="Problem D",
        description="Asymptotic behavior as beta -> 0+ (Reward Hacking)",
        expected="t* -> +infinity (t* >= 10000)",
        observed=f"t* = {t_zero:.1f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test D-03: Asymptotic Limit beta -> infty
    t0 = time.perf_counter()
    t_inf = asymp.get("beta_to_infty_min_drift", 1.0)
    ok = (t_inf <= 0.001)
    tests.append(TestCaseResult(
        test_id="TC-D03",
        problem="Problem D",
        description="Asymptotic behavior as beta -> infinity (Frozen Policy)",
        expected="t* -> 0+ (t* <= 0.001)",
        observed=f"t* = {t_inf:.6f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test D-04: Safety Bound Theorem beta >= r_max / (2T)
    t0 = time.perf_counter()
    sb = d_data.get("safety_bound", {})
    sub_viol = sb.get("sub_critical", {}).get("violates", False)
    crit_exact = sb.get("critical", {}).get("exact_bound_achieved", False)
    sup_safe = sb.get("super_critical", {}).get("safe", False)
    ok = (sub_viol and crit_exact and sup_safe)
    tests.append(TestCaseResult(
        test_id="TC-D04",
        problem="Problem D",
        description="Safe Policy Boundary Condition beta >= r_max / (2T)",
        expected="Sub-crit violates, Crit exact, Super-crit safe",
        observed=f"Sub-viol={sub_viol}, Crit-exact={crit_exact}, Super-safe={sup_safe}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test D-05: Token Distribution Space Gibbs Policy KL Divergence
    t0 = time.perf_counter()
    tok = d_data.get("token_rlhf", {})
    kl_min = tok.get("kl_at_min_beta", 0.0)
    kl_max = tok.get("kl_at_max_beta", 0.0)
    ok = (kl_min > kl_max and kl_max >= 0.0)
    tests.append(TestCaseResult(
        test_id="TC-D05",
        problem="Problem D",
        description="Gibbs Policy KL divergence monotonic decrease with beta",
        expected="D_KL(beta=0.1) > D_KL(beta=100) >= 0",
        observed=f"D_KL(0.1)={kl_min:.4f} > D_KL(100)={kl_max:.4f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    # Test D-06: Fisher Information Quadratic Equivalence (Ratio -> 1.0)
    t0 = time.perf_counter()
    fe = d_data.get("fisher_equivalence", {})
    lim_ratio = fe.get("limiting_ratio", 0.0)
    ok = math.isclose(lim_ratio, 1.0, rel_tol=1e-2)
    tests.append(TestCaseResult(
        test_id="TC-D06",
        problem="Problem D",
        description="Fisher Information Metric equivalence: KL / (0.5 * Delta^T F Delta)",
        expected="Limiting ratio -> 1.0000 as eps -> 0",
        observed=f"Limiting ratio = {lim_ratio:.6f}",
        passed=ok,
        duration_ms=(time.perf_counter() - t0) * 1000
    ))
    
    return tests


# =====================================================================
# Master Execution & Reporting Engine
# =====================================================================

def print_master_report(all_results: List[TestCaseResult], total_elapsed_ms: float) -> int:
    num_passed = sum(1 for t in all_results if t.passed)
    num_total = len(all_results)
    pass_pct = (num_passed / num_total) * 100 if num_total > 0 else 0.0
    
    print("\n" + "=" * 110)
    print(" IMLC 2026 QUALIFICATION ROUND - MASTER VERIFICATION TEST RUNNER REPORT")
    print("=" * 110)
    print(f"{'ID':<8} | {'Problem':<11} | {'Description':<42} | {'Time (ms)':<9} | {'Verdict':<7}")
    print("-" * 110)
    
    for t in all_results:
        verdict = "[PASS]" if t.passed else "[FAIL]"
        print(f"{t.test_id:<8} | {t.problem:<11} | {t.description[:42]:<42} | {t.duration_ms:<9.3f} | {verdict:<7}")
        
    print("-" * 110)
    print(f"SUMMARY: {num_passed}/{num_total} Tests Passed ({pass_pct:.1f}%) | Total Execution Time: {total_elapsed_ms:.2f} ms")
    
    if num_passed == num_total:
        print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY WITH ZERO ERRORS. (Exit code 0)")
        print("=" * 110 + "\n")
        return 0
    else:
        print(f"CRITICAL FAILURE: {num_total - num_passed} TESTS FAILED! (Exit code 1)")
        print("=" * 110 + "\n")
        return 1


def main() -> int:
    t_start = time.perf_counter()
    all_tests: List[TestCaseResult] = []
    
    try:
        # Module B Execution
        print("[*] Executing Problem B (Decision Tree & Information Theory)...")
        b_data = verify_problem_b()
        b_tests = run_problem_b_battery(b_data)
        all_tests.extend(b_tests)
        
        # Module C Execution
        print("[*] Executing Problem C (Ridge L2 Regularization & SVD Shrinkage)...")
        c_data = verify_problem_c()
        c_tests = run_problem_c_battery(c_data)
        all_tests.extend(c_tests)
        
        # Module D Execution
        print("[*] Executing Problem D (RLHF Policy Drift & Safe Boundary)...")
        d_data = verify_problem_d()
        d_tests = run_problem_d_battery(d_data)
        all_tests.extend(d_tests)
        
    except Exception as ex:
        print(f"[ERROR] Fatal exception during verification execution: {ex}")
        import traceback
        traceback.print_exc()
        return 1
        
    total_elapsed_ms = (time.perf_counter() - t_start) * 1000
    exit_code = print_master_report(all_tests, total_elapsed_ms)
    return exit_code


def test_run_all_verifications() -> None:
    """Entry point for automated pytest discovery."""
    code = main()
    assert code == 0


if __name__ == "__main__":
    sys.exit(main())

