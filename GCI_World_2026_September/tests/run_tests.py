"""
Test Runner Helper for GCI World 202609 Study Notes Test Suite.

Usage:
    python tests/run_tests.py
"""

import sys
import unittest
from pathlib import Path

# Add workspace root to sys.path
TESTS_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = TESTS_DIR.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from tests.test_study_notes import (  # noqa: E402
    TestTier1ExistenceAndPopulated,
    TestTier2StructuralAndFormatting,
    TestTier3SyntaxCorrectness,
    TestTier4ConceptCoverage,
)


def run():
    print("=" * 70)
    print(" GCI World 202609 Study Notes - 4-Tier Automated Verification")
    print("=" * 70)

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(
        loader.loadTestsFromTestCase(TestTier1ExistenceAndPopulated)
    )
    suite.addTests(loader.loadTestsFromTestCase(
        TestTier2StructuralAndFormatting
    ))
    suite.addTests(loader.loadTestsFromTestCase(TestTier3SyntaxCorrectness))
    suite.addTests(loader.loadTestsFromTestCase(TestTier4ConceptCoverage))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    print(" SUMMARY")
    print("=" * 70)
    print(f"Total Tests Run: {result.testsRun}")
    passed = result.testsRun - len(result.failures) - len(result.errors)
    print(f"Passed: {passed}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    if result.wasSuccessful():
        print("\n>>> ALL TESTS PASSED SUCCESSFULLY! <<<")
        return 0
    else:
        print("\n>>> SOME TESTS FAILED. See details above. <<<")
        return 1


if __name__ == "__main__":
    sys.exit(run())
