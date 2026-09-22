#!/usr/bin/env python3
"""
Automated Verification Suite for AMD AI Academy Code Labs
Validates:
1. Python syntax compilation (python3 -m py_compile) on all lab scripts.
2. End-to-end execution of Labs 1, 2, 3, and 4 in deterministic standalone test mode.
3. Assertions of required architectural tokens and zero runtime defects.
"""

import os
import sys
import time
import py_compile
import subprocess
from pathlib import Path

# Directories
CURRENT_DIR = Path(__file__).resolve().parent
LAB_FILES = [
    "01_pure_react_agent.py",
    "02_tool_calling_agent.py",
    "03_memory_state_agent.py",
    "04_framework_agent_langgraph.py"
]

def print_header(title: str):
    print("\n" + "=" * 75)
    print(f"🧪 {title}")
    print("=" * 75)

def run_syntax_checks() -> bool:
    print_header("Step 1: Python Syntax Compilation (py_compile)")
    all_passed = True

    for filename in LAB_FILES:
        filepath = CURRENT_DIR / filename
        if not filepath.exists():
            print(f"❌ FAIL: File not found: {filename}")
            all_passed = False
            continue

        try:
            py_compile.compile(str(filepath), doraise=True)
            print(f"✅ PASS: {filename:<36} Syntax valid.")
        except py_compile.PyCompileError as e:
            print(f"❌ FAIL: {filename:<36} Syntax Error:\n{e}")
            all_passed = False

    return all_passed

def run_lab_execution_tests() -> bool:
    print_header("Step 2: End-to-End Test Mode Executions")
    all_passed = True
    results = []

    test_assertions = {
        "01_pure_react_agent.py": [
            "Thought:", "Action:", "Observation:", "Final Answer:", "400"
        ],
        "02_tool_calling_agent.py": [
            "Calling Tool:", "Tool Error Caught", "Self-Correction", "Final Response:", "200"
        ],
        "03_memory_state_agent.py": [
            "LAYER 1: STRUCTURED ENTITY STORE", "LAYER 2: ROLLING SUMMARY",
            "Alex", "Ryzen AI 9 HX 370", "Recalled Response:"
        ],
        "04_framework_agent_langgraph.py": [
            "supervisor", "hardware_specialist", "benchmark_analyst",
            "synthesizer", "APPROVED", "CDNA 3", "XDNA 2"
        ]
    }

    for filename in LAB_FILES:
        filepath = CURRENT_DIR / filename
        if not filepath.exists():
            continue

        start_time = time.perf_counter()
        cmd = [sys.executable, str(filepath), "--test-mode"]

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            duration = time.perf_counter() - start_time

            if res.returncode != 0:
                print(f"❌ FAIL: {filename} exited with code {res.returncode}")
                print(f"Stderr:\n{res.stderr.strip()}")
                all_passed = False
                results.append((filename, False, duration, "Exit code non-zero"))
                continue

            # Verify semantic assertions
            stdout_text = res.stdout
            missing_tokens = [tok for tok in test_assertions[filename] if tok not in stdout_text]

            if missing_tokens:
                print(f"❌ FAIL: {filename} missing required semantic tokens: {missing_tokens}")
                all_passed = False
                results.append((filename, False, duration, f"Missing tokens: {missing_tokens}"))
            else:
                print(f"✅ PASS: {filename:<36} Completed in {duration:6.2f}s")
                results.append((filename, True, duration, "All assertions verified"))

        except subprocess.TimeoutExpired:
            duration = time.perf_counter() - start_time
            print(f"❌ FAIL: {filename} timed out after 15 seconds")
            all_passed = False
            results.append((filename, False, duration, "Timeout"))
        except Exception as e:
            duration = time.perf_counter() - start_time
            print(f"❌ FAIL: {filename} unexpected error: {e}")
            all_passed = False
            results.append((filename, False, duration, str(e)))

    # Summary Dashboard
    print("\n" + "+" + "-" * 73 + "+")
    print(f"| {'Lab Test Suite Summary':<45} | {'Status':<12} | {'Time':<8} |")
    print("+" + "-" * 73 + "+")
    for name, status, duration, note in results:
        status_str = "✅ PASS" if status else "❌ FAIL"
        print(f"| {name:<45} | {status_str:<12} | {duration:6.2f}s |")
    print("+" + "-" * 73 + "+")

    return all_passed

def main():
    print("=" * 75)
    print("🚀 Starting AMD AI Academy Labs Verification Suite")
    print(f"Python Interpreter: {sys.executable} ({sys.version.split()[0]})")
    print("=" * 75)

    syntax_ok = run_syntax_checks()
    if not syntax_ok:
        print("\n❌ Verification Aborted: Syntax errors detected.")
        sys.exit(1)

    exec_ok = run_lab_execution_tests()
    if not exec_ok:
        print("\n❌ Verification Failed: Runtime defects detected.")
        sys.exit(1)

    print("\n🎉 ALL TESTS PASSED: Zero defects detected across all 4 Code Labs!")
    sys.exit(0)

if __name__ == "__main__":
    main()
