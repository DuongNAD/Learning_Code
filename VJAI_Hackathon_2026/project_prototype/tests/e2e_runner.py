#!/usr/bin/env python3
"""
AgriCarbon Agent — Central E2E Test Runner CLI
Authoritative reference: ORIGINAL_REQUEST.md, PROJECT.md, TEST_INFRA.md

Usage:
    python tests/e2e_runner.py --all
    python tests/e2e_runner.py --tier 1
    python tests/e2e_runner.py --tier 2
    python tests/e2e_runner.py --tier 3
    python tests/e2e_runner.py --tier 4
    python tests/e2e_runner.py --all --verbose
    python tests/e2e_runner.py --summary
"""

import sys
import os
import argparse
import time
from pathlib import Path
from typing import Dict, List, Any

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

TIER_CONFIG = {
    1: {
        "name": "Tier 1: Feature Coverage",
        "dir": "tests/tier1_feature",
        "description": "Domain models, Tools, Supervisor routing, SSE stream, Fast Demo, Pitch Deck"
    },
    2: {
        "name": "Tier 2: Boundary & Corner Cases",
        "dir": "tests/tier2_boundary",
        "description": "Catastrophic weather, Out-of-bounds inputs, Network errors, Critic self-correction"
    },
    3: {
        "name": "Tier 3: Pairwise Integration",
        "dir": "tests/tier3_pairwise",
        "description": "Sensing -> Dispatch -> Carbon -> Ledger pipeline and Reflexion loops"
    },
    4: {
        "name": "Tier 4: TiB Demo Scenarios",
        "dir": "tests/tier4_scenarios",
        "description": "An Giang AWD Rice Polder & Lam Dong Arabica Coffee Farm stage demos"
    }
}


class E2ETestResultCollector:
    """Pytest plugin to collect per-test results and timing for summary reporting."""

    def __init__(self):
        self.results: List[Dict[str, Any]] = []
        self.start_time = time.time()
        self.end_time = 0.0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            file_path = report.nodeid.split("::")[0]
            test_name = report.nodeid.split("::")[-1]
            self.results.append({
                "nodeid": report.nodeid,
                "file": Path(file_path).name,
                "path": file_path,
                "test_name": test_name,
                "outcome": report.outcome,  # 'passed', 'failed', 'skipped'
                "duration": report.duration,
                "longrepr": str(report.longrepr) if report.failed else None
            })
        elif report.when == "setup" and report.outcome == "failed":
            file_path = report.nodeid.split("::")[0]
            self.results.append({
                "nodeid": report.nodeid,
                "file": Path(file_path).name,
                "path": file_path,
                "test_name": "setup",
                "outcome": "failed",
                "duration": report.duration,
                "longrepr": str(report.longrepr)
            })

    def pytest_sessionfinish(self, session, exitstatus):
        self.end_time = time.time()


def render_summary_table(results: List[Dict[str, Any]], active_tiers: List[int], total_elapsed: float) -> int:
    """Renders a clean tabular summary of test execution across tiers and files."""
    header_line = "=" * 115
    sub_line = "-" * 115

    print("\n" + header_line)
    print("                      AgriCarbon Agent -- E2E Test Suite Execution Report")
    print("                      Vietnam Japan AI Hackathon 2026 (Track 3: Green Growth)")
    print(header_line)
    print(f"{'Tier / Suite':<34} {'Target Test File':<42} {'Tests':>6} {'Pass':>6} {'Fail':>6} {'Time(s)':>8} {'Status':>8}")
    print(sub_line)

    total_tests = 0
    total_passed = 0
    total_failed = 0
    total_skipped = 0

    for tier_num in active_tiers:
        t_conf = TIER_CONFIG[tier_num]
        tier_dir_name = Path(t_conf["dir"]).name
        tier_results = [r for r in results if tier_dir_name in r["path"].replace("\\", "/")]

        # Group by file
        files_in_tier = {}
        for r in tier_results:
            f_name = r["file"]
            if f_name not in files_in_tier:
                files_in_tier[f_name] = []
            files_in_tier[f_name].append(r)

        first_row = True
        for f_name, f_tests in sorted(files_in_tier.items()):
            f_pass = sum(1 for t in f_tests if t["outcome"] == "passed")
            f_fail = sum(1 for t in f_tests if t["outcome"] == "failed")
            f_dur = sum(t["duration"] for t in f_tests)
            f_status = "PASS" if f_fail == 0 else "FAIL"

            total_tests += len(f_tests)
            total_passed += f_pass
            total_failed += f_fail

            tier_label = t_conf["name"] if first_row else ""
            print(f"{tier_label:<34} {f_name:<42} {len(f_tests):>6} {f_pass:>6} {f_fail:>6} {f_dur:>8.2f}s {f_status:>8}")
            first_row = False

        if not files_in_tier:
            print(f"{t_conf['name']:<34} {'[No test files found]':<42} {0:>6} {0:>6} {0:>6} {0.0:>8.2f}s {'SKIP':>8}")

    print(header_line)
    status_str = "100% PASSED (READY FOR TIB TOKYO DEMO)" if total_failed == 0 and total_tests > 0 else "TEST SUITE FAILED"
    print(f"TOTAL: {total_tests} Tests | {total_passed} Passed | {total_failed} Failed | Wall Clock: {total_elapsed:.2f}s | Status: {status_str}")
    print(header_line + "\n")

    # Print failure details if any
    failed_tests = [r for r in results if r["outcome"] == "failed"]
    if failed_tests:
        print("\n" + "!" * 105)
        print("                                     FAILURES & STACK TRACES")
        print("!" * 105)
        for f in failed_tests:
            print(f"\n[FAIL] {f['nodeid']}")
            if f["longrepr"]:
                print(f["longrepr"])
        print("!" * 105 + "\n")

    return 0 if (total_failed == 0 and total_tests > 0) else 1


def run_e2e_tests(selected_tiers: List[int], verbose: bool = False, fail_fast: bool = False) -> int:
    """Executes pytest targeting the selected tiers and renders results."""
    import pytest

    test_dirs = [str(PROJECT_ROOT / TIER_CONFIG[t]["dir"]) for t in selected_tiers]

    pytest_args = []
    if verbose:
        pytest_args.append("-v")
    else:
        pytest_args.append("-q")

    if fail_fast:
        pytest_args.append("-x")

    pytest_args.extend(test_dirs)

    collector = E2ETestResultCollector()
    start_time = time.time()

    # Run pytest with custom result collector plugin
    exit_code = pytest.main(pytest_args, plugins=[collector])
    total_elapsed = time.time() - start_time

    table_exit_code = render_summary_table(collector.results, selected_tiers, total_elapsed)
    return table_exit_code if table_exit_code != 0 else (0 if exit_code == 0 else 1)


def parse_args():
    parser = argparse.ArgumentParser(
        description="AgriCarbon Agent E2E Test Runner CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python tests/e2e_runner.py --all
    python tests/e2e_runner.py --tier 1
    python tests/e2e_runner.py --tier 2
    python tests/e2e_runner.py --tier 3
    python tests/e2e_runner.py --tier 4
    python tests/e2e_runner.py --all --verbose
    python tests/e2e_runner.py --summary
        """
    )
    parser.add_argument("--all", action="store_true", help="Run all 4 tiers (Tiers 1-4)")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4], help="Run specific test tier (1, 2, 3, or 4)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose test output")
    parser.add_argument("--summary", "-s", action="store_true", help="Display summary overview")
    parser.add_argument("--fail-fast", "-x", action="store_true", help="Stop execution upon first test failure")
    return parser.parse_args()


def main():
    args = parse_args()

    # Determine tiers to run
    if args.tier:
        active_tiers = [args.tier]
    else:
        # Default to all tiers if --all or --summary or no argument provided
        active_tiers = [1, 2, 3, 4]

    print(f"\n=========================================================================================")
    print(f" AgriCarbon Agent E2E Runner -- Running Tiers: {active_tiers}")
    for t in active_tiers:
        print(f"   * {TIER_CONFIG[t]['name']} ({TIER_CONFIG[t]['dir']})")
    print(f"=========================================================================================")

    exit_code = run_e2e_tests(
        selected_tiers=active_tiers,
        verbose=args.verbose,
        fail_fast=args.fail_fast
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
