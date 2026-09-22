#!/usr/bin/env python3
"""
IMLC 2026 Research Dossier - Master E2E Test Suite Runner
Executes all 4 tiers of automated opaque-box tests sequentially,
prints a structured test matrix with pass/fail counts,
and exits with code 0 on success.

Dependencies: Standard Library and numpy only.
"""

import argparse
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# Paths
TESTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TESTS_DIR.parent

TIER_FILES = {
    1: ("Feature Coverage (FI-01 to FI-27)", TESTS_DIR / "test_tier1_features.py"),
    2: ("Boundary & Corner Cases", TESTS_DIR / "test_tier2_boundaries.py"),
    3: ("Cross-Feature Combinations", TESTS_DIR / "test_tier3_combinations.py"),
    4: ("Real-World Application Scenarios", TESTS_DIR / "test_tier4_applications.py"),
}


def parse_pytest_output(output: str):
    """Parses pytest terminal output for test counts and execution summary."""
    passed = 0
    skipped = 0
    failed = 0
    errors = 0

    # Look for summary line: "== 132 passed, 3 skipped in 1.94s =="
    summary_match = re.search(
        r"=+\s*(?:(?P<passed>\d+)\s+passed)?(?:[,\s]+(?P<skipped>\d+)\s+skipped)?(?:[,\s]+(?P<failed>\d+)\s+failed)?(?:[,\s]+(?P<errors>\d+)\s+errors)?.*in\s+([0-9\.]+)s",
        output,
    )
    if summary_match:
        if summary_match.group("passed"):
            passed = int(summary_match.group("passed"))
        if summary_match.group("skipped"):
            skipped = int(summary_match.group("skipped"))
        if summary_match.group("failed"):
            failed = int(summary_match.group("failed"))
        if summary_match.group("errors"):
            errors = int(summary_match.group("errors"))
    else:
        # Fallback counting from individual test lines: "PASSED", "FAILED", "SKIPPED"
        passed = len(re.findall(r"\s+PASSED\s+", output))
        skipped = len(re.findall(r"\s+SKIPPED\s+", output))
        failed = len(re.findall(r"\s+FAILED\s+", output))
        errors = len(re.findall(r"\s+ERROR\s+", output))

    total = passed + skipped + failed + errors
    return {
        "passed": passed,
        "skipped": skipped,
        "failed": failed + errors,
        "total": total,
    }


def run_tier(tier_num: int, tier_name: str, tier_path: Path, verbose: bool = False):
    """Executes a single test tier via pytest and captures statistics."""
    if not tier_path.exists():
        return {
            "tier": tier_num,
            "name": tier_name,
            "total": 0,
            "passed": 0,
            "skipped": 0,
            "failed": 1,
            "duration": 0.0,
            "success": False,
            "output": f"Test file {tier_path.name} does not exist",
        }

    start_time = time.time()
    cmd = [sys.executable, "-m", "pytest", str(tier_path), "-v", "--tb=short"]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))
    duration = time.time() - start_time

    combined_output = proc.stdout + "\n" + proc.stderr
    stats = parse_pytest_output(combined_output)
    success = (proc.returncode == 0) and (stats["failed"] == 0)

    return {
        "tier": tier_num,
        "name": tier_name,
        "total": stats["total"],
        "passed": stats["passed"],
        "skipped": stats["skipped"],
        "failed": stats["failed"],
        "duration": duration,
        "success": success,
        "output": combined_output,
    }


def print_matrix(results, total_duration):
    """Prints a publication-grade ASCII test matrix."""
    header = "=" * 98
    print(header)
    print("                    IMLC 2026 RESEARCH DOSSIER - E2E TEST EXECUTION MATRIX")
    print(header)
    print(f" {'Tier':<6} | {'Scope & Objective':<38} | {'Total':>6} | {'Passed':>6} | {'Skip':>5} | {'Fail':>5} | {'Status':>8}")
    print("-" * 98)

    total_tests = sum(r["total"] for r in results)
    total_passed = sum(r["passed"] for r in results)
    total_skipped = sum(r["skipped"] for r in results)
    total_failed = sum(r["failed"] for r in results)
    all_success = all(r["success"] for r in results)

    for r in results:
        status_str = "PASS" if r["success"] else "FAIL"
        tier_label = f"T{r['tier']}"
        print(
            f" {tier_label:<6} | {r['name']:<38} | {r['total']:>6} | {r['passed']:>6} | {r['skipped']:>5} | {r['failed']:>5} | {status_str:>8}"
        )

    print("-" * 98)
    overall_status = "PASS" if all_success else "FAIL"
    print(
        f" {'TOTAL':<6} | {'Comprehensive E2E Suite':<38} | {total_tests:>6} | {total_passed:>6} | {total_skipped:>5} | {total_failed:>5} | {overall_status:>8}"
    )
    print(header)
    print(f" Execution Time: {total_duration:.2f}s | Environment: Python {sys.version.split()[0]} on {sys.platform}")
    if all_success:
        print(" Verdict: ALL EXECUTED TESTS PASSED (Return Code 0)")
    else:
        print(" Verdict: TEST SUITE FAILED (Return Code 1)")
    print(header)


def main():
    parser = argparse.ArgumentParser(description="IMLC 2026 Master E2E Test Suite Runner")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4], help="Execute specific test tier only (1-4)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print full output from pytest")
    args = parser.parse_args()

    selected_tiers = [args.tier] if args.tier else [1, 2, 3, 4]

    print("\n" + "=" * 98)
    print(" >>> Starting IMLC 2026 E2E Automated Test Suite Execution...")
    print("=" * 98)

    suite_start = time.time()
    results = []

    for t_num in selected_tiers:
        t_name, t_path = TIER_FILES[t_num]
        print(f" [*] Executing Tier {t_num}: {t_name}...")
        res = run_tier(t_num, t_name, t_path, verbose=args.verbose)
        results.append(res)
        if args.verbose or not res["success"]:
            print(res["output"])

    total_duration = time.time() - suite_start
    print_matrix(results, total_duration)

    all_pass = all(r["success"] for r in results)
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
