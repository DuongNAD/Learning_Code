"""
Empirical Stress-Testing Harness for Curriculum Alignment Matrix & Course Policies.
Authored by Challenger 2 (Empirical Challenger).

Verifies and stress-tests:
1. Exact scoring and threshold math:
   - 8 homeworks * 3.0 pts = 24.0 pts max
   - Minimum passing threshold >= 14.0 pts (58.33%)
   - Late penalty formula: max 2.0 pts per late submission
   - Full combinatorial analysis of pass/fail scenarios (all on-time, all late, mixed, boundary)
2. Attendance survey policy:
   - 14 surveys, minimum >= 7 required (50.0%)
   - Strict zero late policy (late submissions receive 0 credit)
3. 3-tier completion model & eligibility oracle:
   - Completed: attendance >= 7, HW >= 14.0, Capstone pass
   - Honors: Completed + Capstone Top 10% + Competition Top 20%
   - Outstanding: Honors + Interview pass + First-time student (Returning students strictly excluded)
4. Timeline and micro-session workload feasibility:
   - 30-45 minute micro-sessions with 2-step rhythm (Step 1 Pen-First + Step 2 Practice)
   - Working professional schedule simulation (standard vs peak crunch weeks)
5. Cross-reference integrity:
   - Buoi 0/1 topics to HW1-HW8, ML Competition (5-step ladder), and Final Capstone (5 criteria summing to 100%)
   - Competency Triad weights (60-70% Domain, 15% DS, 15% DE)
   - Zero-emoji compliance
"""

import math
import re
import unittest
from pathlib import Path
from typing import Dict, List, Optional, Tuple

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
ROADMAP_DIR = WORKSPACE_ROOT / "roadmap"
ALIGNMENT_MATRIX_FILE = ROADMAP_DIR / "curriculum_alignment_matrix.md"
MICRO_PRACTICE_FILE = ROADMAP_DIR / "micro_practice_roadmap.md"
SLIDES_DIR = WORKSPACE_ROOT / "slides"
BUOI1_SLIDES_FILE = SLIDES_DIR / "01_orientation" / "index.html"


# ==============================================================================
# Domain Oracle: Course Policy & Completion Tier Evaluator
# ==============================================================================
def evaluate_completion_tier(
    attendance_count: int,
    hw_score: float,
    capstone_passed: bool,
    capstone_percentile: Optional[float] = None,      # e.g., 0.05 for Top 5%
    competition_percentile: Optional[float] = None,   # e.g., 0.15 for Top 15%
    is_first_time_student: bool = True,
    interview_passed: bool = False,
) -> str:
    """
    Evaluates student graduation tier based on official UTokyo GCI World policies.

    Tiers:
    - 'INCOMPLETE': Did not meet basic completion requirements
    - 'COMPLETED': Standard completion certificate
    - 'HONORS': Honors certificate (Top 10% Capstone AND Top 20% Competition)
    - 'OUTSTANDING': Tokyo Study Tour scholarship (Honors + Interview + First-time only)
    """
    # Base requirements
    if attendance_count < 7 or hw_score < 14.0 or not capstone_passed:
        return "INCOMPLETE"

    # Honors eligibility: Top 10% Capstone AND Top 20% Competition
    is_honors = (
        capstone_percentile is not None
        and capstone_percentile <= 0.10
        and competition_percentile is not None
        and competition_percentile <= 0.20
    )

    if not is_honors:
        return "COMPLETED"

    # Outstanding eligibility: Honors + First-time student + Interview pass
    if is_first_time_student and interview_passed:
        return "OUTSTANDING"

    return "HONORS"


# ==============================================================================
# 1. Scoring & Threshold Math Stress-Testing
# ==============================================================================
class TestScoringAndThresholdMath(unittest.TestCase):
    """Stress-test mathematical properties and edge cases of grading policies."""

    def test_maximum_points_math(self):
        """Verify maximum possible homework score is exactly 24.0 points."""
        total_hw = 8
        max_pts_per_hw = 3.0
        total_max = total_hw * max_pts_per_hw
        self.assertEqual(total_max, 24.0)

    def test_passing_threshold_math_and_percentage(self):
        """Verify passing threshold is 14.0 / 24.0 (58.333...%)."""
        threshold = 14.0
        max_score = 24.0
        ratio = threshold / max_score
        self.assertAlmostEqual(ratio, 7 / 12, places=7)
        self.assertAlmostEqual(ratio * 100, 58.3333333, places=4)
        self.assertEqual(f"{ratio * 100:.2f}%", "58.33%")

    def test_on_time_only_combinations(self):
        """Stress-test how many on-time homeworks are necessary and sufficient to pass."""
        # Minimum on-time submissions needed with full marks (3.0):
        # ceil(14.0 / 3.0) = 5 submissions (15.0 pts)
        min_on_time = math.ceil(14.0 / 3.0)
        self.assertEqual(min_on_time, 5)
        self.assertGreaterEqual(5 * 3.0, 14.0)

        # 4 full on-time submissions: 4 * 3.0 = 12.0 < 14.0 (FAILS)
        self.assertLess(4 * 3.0, 14.0)

        # 4 full on-time (12.0) + 1 late full (2.0) = 14.0 (EXACT PASS BOUNDARY)
        self.assertEqual(4 * 3.0 + 1 * 2.0, 14.0)

    def test_late_submissions_passability_scenario(self):
        """
        Adversarial test: Can a student who submits EVERY homework late still pass?
        Policy: Late submission gets max 2.0 pts.
        8 * 2.0 = 16.0 pts.
        Since 16.0 >= 14.0, YES, an all-late student CAN pass!
        """
        all_late_max = 8 * 2.0
        self.assertEqual(all_late_max, 16.0)
        self.assertGreaterEqual(all_late_max, 14.0)

        # Minimum late homeworks required to pass: ceil(14.0 / 2.0) = 7
        min_late = math.ceil(14.0 / 2.0)
        self.assertEqual(min_late, 7)
        self.assertEqual(7 * 2.0, 14.0)

        # 6 late submissions: 6 * 2.0 = 12.0 < 14.0 (FAILS)
        self.assertLess(6 * 2.0, 14.0)

    def test_combinatorial_grading_boundary_simulation(self):
        """Exhaustively verify all possible on-time / late integer submissions."""
        passing_configs = []
        failing_configs = []

        for on_time in range(9):
            for late in range(9 - on_time):
                missed = 8 - on_time - late
                score = on_time * 3.0 + late * 2.0
                if score >= 14.0:
                    passing_configs.append((on_time, late, missed, score))
                else:
                    failing_configs.append((on_time, late, missed, score))

        # There are (9 * 10) / 2 = 45 possible (on_time, late) pairs
        self.assertEqual(len(passing_configs) + len(failing_configs), 45)

        # Verify lowest passing score is exactly 14.0
        lowest_passing_score = min(score for _, _, _, score in passing_configs)
        self.assertEqual(lowest_passing_score, 14.0)

        # Verify highest failing score is strictly less than 14.0 (13.0 or 12.0)
        highest_failing_score = max(score for _, _, _, score in failing_configs)
        self.assertLess(highest_failing_score, 14.0)
        self.assertEqual(highest_failing_score, 13.0)  # e.g., 3 on-time (9) + 2 late (4) = 13.0


# ==============================================================================
# 2. Attendance Survey Policy & Zero Late Stress-Testing
# ==============================================================================
class TestAttendanceSurveyPolicy(unittest.TestCase):
    """Stress-test attendance survey rules, counting, and zero late policy."""

    def test_survey_counts_and_threshold(self):
        """Verify 14 surveys total, >= 7 required (50.0%)."""
        total_surveys = 14
        min_surveys = 7
        ratio = min_surveys / total_surveys
        self.assertEqual(ratio, 0.5)
        self.assertEqual(f"{ratio * 100:.1f}%", "50.0%")

    def test_strict_zero_late_survey_policy(self):
        """
        Adversarial scenario:
        A student fills out 14 surveys, but 8 of them were submitted 1 second after 11:00 AM UTC.
        Under zero late policy:
        Valid surveys = 6 (< 7).
        The student must FAIL the course despite attending all lectures.
        """
        total_submitted = 14
        on_time = 6
        late = 8  # strict 0 credit
        valid_attendance = on_time

        tier = evaluate_completion_tier(
            attendance_count=valid_attendance,
            hw_score=24.0,
            capstone_passed=True,
            capstone_percentile=0.01,
            competition_percentile=0.01,
        )
        self.assertEqual(tier, "INCOMPLETE")

    def test_attendance_exact_boundary(self):
        """Boundary test: 7 on-time surveys PASSES; 6 on-time surveys FAILS."""
        tier_7 = evaluate_completion_tier(7, 14.0, True)
        self.assertEqual(tier_7, "COMPLETED")

        tier_6 = evaluate_completion_tier(6, 14.0, True)
        self.assertEqual(tier_6, "INCOMPLETE")


# ==============================================================================
# 3. 3-Tier Completion Model & Returning Student Exclusion
# ==============================================================================
class TestThreeTierCompletionModel(unittest.TestCase):
    """Stress-test 3-tier completion model, percentiles, and returning student exclusion."""

    def test_tier1_completed_student_requirements(self):
        """Completed tier requires Attendance >= 7, HW >= 14.0, Capstone Pass."""
        # Minimal passing student
        res = evaluate_completion_tier(7, 14.0, True)
        self.assertEqual(res, "COMPLETED")

        # Competition is optional for Tier 1
        res_no_comp = evaluate_completion_tier(7, 14.0, True, competition_percentile=None)
        self.assertEqual(res_no_comp, "COMPLETED")

    def test_tier2_honors_student_requirements(self):
        """Honors tier requires Top 10% Capstone AND Top 20% Competition."""
        # Exactly Top 10% Capstone and Top 20% Competition -> HONORS
        res_boundary = evaluate_completion_tier(
            attendance_count=10,
            hw_score=20.0,
            capstone_passed=True,
            capstone_percentile=0.10,
            competition_percentile=0.20,
        )
        self.assertEqual(res_boundary, "HONORS")

        # Capstone Top 10.1% (fails Honors, falls back to Completed)
        res_cap_fail = evaluate_completion_tier(
            attendance_count=10,
            hw_score=20.0,
            capstone_passed=True,
            capstone_percentile=0.101,
            competition_percentile=0.05,
        )
        self.assertEqual(res_cap_fail, "COMPLETED")

        # Competition Top 20.1% (fails Honors, falls back to Completed)
        res_comp_fail = evaluate_completion_tier(
            attendance_count=10,
            hw_score=20.0,
            capstone_passed=True,
            capstone_percentile=0.05,
            competition_percentile=0.201,
        )
        self.assertEqual(res_comp_fail, "COMPLETED")

    def test_tier3_outstanding_student_and_returning_student_exclusion(self):
        """
        Adversarial test:
        Returning student gets Rank 1 (Top 0.1%) in Capstone and Rank 1 in Competition,
        and passes the interview.
        MUST NOT receive Outstanding Student (ineligible due to returning student rule).
        Must be capped at Honors Student.
        """
        res_returning = evaluate_completion_tier(
            attendance_count=14,
            hw_score=24.0,
            capstone_passed=True,
            capstone_percentile=0.001,
            competition_percentile=0.001,
            is_first_time_student=False,  # Returning student
            interview_passed=True,
        )
        self.assertEqual(res_returning, "HONORS")

        # First-time student with same metrics receives OUTSTANDING
        res_first_time = evaluate_completion_tier(
            attendance_count=14,
            hw_score=24.0,
            capstone_passed=True,
            capstone_percentile=0.001,
            competition_percentile=0.001,
            is_first_time_student=True,
            interview_passed=True,
        )
        self.assertEqual(res_first_time, "OUTSTANDING")


# ==============================================================================
# 4. Timeline Feasibility & Micro-Session Workload Modeling
# ==============================================================================
class TestTimelineFeasibilityAndWorkload(unittest.TestCase):
    """Stress-test time commitment and schedule feasibility for working students."""

    def test_micro_session_durations_in_roadmap(self):
        """Verify all micro-sessions stay strictly within the 30–45 minute envelope."""
        content = MICRO_PRACTICE_FILE.read_text(encoding="utf-8")
        durations = [int(m) for m in re.findall(r"Thời lượng:\*{0,2}\s*(\d+)\s*Phút", content)]

        self.assertGreater(len(durations), 0)
        for d in durations:
            self.assertTrue(
                30 <= d <= 45,
                f"Micro-session duration {d} mins violates 30–45 min specification!"
            )

    def test_weekly_workload_simulation_working_student(self):
        """
        Simulate weekly time budget for a working student.
        Assumptions:
        - Weekday study: 1 micro-session/day (35-40 min) * 4 days = 140-160 min (2.5h)
        - Weekend study: Synthesis session (45 min) + HW / Live lecture (1.5h - 2.5h) = ~3-4h
        - Base weekly workload = 5.5 - 7.0 hours/week.
        - Peak crunch weeks (Weeks 7–10: ML Competition + HW + Capstone):
          Base (6h) + Competition (2h) + Capstone (2h) = ~10.0 hours/week.
        Verify that peak workload is <= 12 hours/week, which is manageable for working professionals.
        """
        base_lecture_hours = 1.5
        micro_sessions_per_week = 4
        avg_micro_duration_hours = 40 / 60  # ~0.67h
        weekly_micro_hours = micro_sessions_per_week * avg_micro_duration_hours
        hw_hours = 1.5

        normal_weekly_load = base_lecture_hours + weekly_micro_hours + hw_hours
        self.assertAlmostEqual(normal_weekly_load, 5.67, places=1)
        self.assertLessEqual(normal_weekly_load, 7.0)

        # Peak crunch load during Weeks 7-10
        competition_weekly_hours = 2.0
        capstone_weekly_hours = 2.5
        peak_weekly_load = normal_weekly_load + competition_weekly_hours + capstone_weekly_hours
        self.assertLessEqual(peak_weekly_load, 11.0)


# ==============================================================================
# 5. Curriculum Alignment Matrix Text & Cross-Reference Integrity
# ==============================================================================
class TestCurriculumAlignmentMatrixIntegrity(unittest.TestCase):
    """Verify authoritative text, numbers, formulas, and references in alignment matrix."""

    @classmethod
    def setUpClass(cls):
        cls.matrix_text = ALIGNMENT_MATRIX_FILE.read_text(encoding="utf-8")
        cls.slides_text = BUOI1_SLIDES_FILE.read_text(encoding="utf-8")

    def test_exact_scoring_and_threshold_text(self):
        """Verify explicit occurrence of exact scoring numbers."""
        self.assertIn("8 Bài tập", self.matrix_text)
        self.assertIn("3.0 Điểm / Bài", self.matrix_text)
        self.assertIn("Tổng 24.0 Điểm", self.matrix_text)
        self.assertIn("14.0 / 24.0", self.matrix_text)
        self.assertIn("2.0 Điểm / Bài", self.matrix_text)

    def test_attendance_survey_policy_text(self):
        """Verify 14 surveys, >= 7 required, and zero late policy."""
        self.assertIn("14", self.matrix_text)
        self.assertIn(">= 7 / 14", self.matrix_text)
        self.assertTrue(
            "Tuyệt đối không trễ hạn" in self.matrix_text
            or "Hạn cuối tuyệt đối không thể mở lại" in self.matrix_text
        )

    def test_three_tier_completion_text(self):
        """Verify 3-tier completion model and returning student exclusion."""
        self.assertIn("COMPLETED STUDENT", self.matrix_text)
        self.assertIn("HONORS STUDENT", self.matrix_text)
        self.assertIn("OUTSTANDING STUDENT", self.matrix_text)
        self.assertIn("TOP 10%", self.matrix_text)
        self.assertIn("TOP 20%", self.matrix_text)
        self.assertIn("TOKYO STUDY TOUR", self.matrix_text)
        self.assertIn("First-time students only", self.matrix_text)

    def test_capstone_evaluation_weights_sum_to_100_percent(self):
        """Verify the 5 Capstone evaluation criteria sum to exactly 100%."""
        weights = [
            int(w)
            for w in re.findall(
                r"Trọng số\s*(\d+)%", self.matrix_text
            )
        ]
        self.assertEqual(len(weights), 5, f"Expected 5 Capstone weights, found {weights}")
        self.assertEqual(sum(weights), 100, f"Capstone weights sum to {sum(weights)}%, not 100%!")
        self.assertEqual(weights, [30, 20, 20, 20, 10])

    def test_competency_triad_weights(self):
        """Verify Competency Triad weights in alignment matrix."""
        self.assertTrue(re.search(r"DOMAIN.*?60[–-]70%", self.matrix_text, re.DOTALL))
        self.assertIn("DATA SCIENCE (15%)", self.matrix_text)
        self.assertIn("DATA ENGINEERING (15%)", self.matrix_text)

    def test_hw1_to_hw8_cross_references(self):
        """Verify all 8 homework assignments are mapped with technical topics."""
        expected_hw_topics = {
            "HW1": "NumPy",
            "HW2": "Pandas",
            "HW3": "EDA",
            "HW4": "OLS",
            "HW5": "Chi Phí Sai Lầm",
            "HW6": "Optuna",
            "HW7": "SQL",
            "HW8": "Chuỗi Thời Gian",
        }
        for hw_code, topic_keyword in expected_hw_topics.items():
            self.assertIn(hw_code, self.matrix_text)
            self.assertIn(topic_keyword, self.matrix_text)

    def test_five_step_ml_ladder_cross_references(self):
        """Verify 5-Step ML Operational Ladder for Omnicampus competition."""
        steps = [
            "Bước 1: Submit Baseline Code",
            "Bước 2: Domain-Driven Feature Engineering",
            "Bước 3: Thử Nghiệm Kiến Trúc Mô Hình Hiện Đại",
            "Bước 4: Tự Động Dò Tham Số Bằng Optuna",
            "Bước 5: Ensembling & Post-Processing",
        ]
        for step in steps:
            self.assertIn(step, self.matrix_text)

    def test_zero_emojis_in_matrix(self):
        """Verify RFC 2119 zero-emoji compliance."""
        emoji_pattern = re.compile(
            "[\U00010000-\U0010ffff]|"
            "[\u2600-\u27bf]|"
            "[\u2300-\u23ff]|"
            "[\u2b50-\u2b55]"
        )
        matches = emoji_pattern.findall(self.matrix_text)
        real_emojis = [m for m in matches if ord(m) > 0x2700 or ord(m) in (0x2600, 0x2601, 0x2615, 0x2728, 0x2b50)]
        self.assertEqual(len(real_emojis), 0, f"Found emojis in matrix: {real_emojis}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
