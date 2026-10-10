"""
Comprehensive Automated Verification Suite for Milestone 3 Deliverables:
- roadmap/micro_practice_roadmap.md
- roadmap/curriculum_alignment_matrix.md
- syllabus/cornell_notebook_guide.md

Verifies:
1. Deliverable presence, non-emptiness, and UTF-8 encoding.
2. Python AST syntax correctness across all markdown code blocks.
3. Micro-session partitioning (Buoi 0: 4 micro-sessions + 1 review; Buoi 1: 5 micro-sessions + 1 review).
4. Pedagogical structure: 2-step rhythm (Step 1 Pen-First, Step 2 Practice), DoD, and Active Recall checks with <details>.
5. Curriculum alignment completeness: 14 weeks, HW1-HW8, Omnicampus autograder (14/24), Competition (Top 20%), Final Assignment (Top 10%), Tokyo tour.
6. Cornell notebook guide structural completeness (3 columns 20/50/30, summary box, neuroscience, stationery, habit protocol, spaced repetition).
7. Strict zero-emoji compliance (emoji_policy: none).
"""

import ast
import re
import unittest
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
ROADMAP_DIR = WORKSPACE_ROOT / "roadmap"
SYLLABUS_DIR = WORKSPACE_ROOT / "syllabus"

MICRO_PRACTICE_FILE = ROADMAP_DIR / "micro_practice_roadmap.md"
ALIGNMENT_MATRIX_FILE = ROADMAP_DIR / "curriculum_alignment_matrix.md"
CORNELL_GUIDE_FILE = SYLLABUS_DIR / "cornell_notebook_guide.md"


class TestMilestone3DeliverablePresence(unittest.TestCase):
    """Verify presence, non-emptiness, and UTF-8 encoding of Milestone 3 deliverables."""

    def test_m3_files_exist(self):
        for path in [MICRO_PRACTICE_FILE, ALIGNMENT_MATRIX_FILE, CORNELL_GUIDE_FILE]:
            self.assertTrue(path.is_file(), f"Missing required deliverable: {path}")
            self.assertGreater(path.stat().st_size, 5000, f"File unexpectedly small (<5KB): {path}")

    def test_utf8_decodable(self):
        for path in [MICRO_PRACTICE_FILE, ALIGNMENT_MATRIX_FILE, CORNELL_GUIDE_FILE]:
            content = path.read_text(encoding="utf-8")
            self.assertGreater(len(content), 0)


class TestMilestone3PythonAST(unittest.TestCase):
    """Verify all Python code snippets in M3 markdown files parse cleanly with ast.parse()."""

    def _verify_python_blocks_in_file(self, file_path: Path):
        content = file_path.read_text(encoding="utf-8")
        blocks = re.findall(r"```python\s*(.*?)\s*```", content, re.DOTALL)
        for i, code in enumerate(blocks):
            try:
                ast.parse(code)
            except SyntaxError as e:
                self.fail(f"SyntaxError in {file_path.name} block {i+1}:\n{e}\nCode snippet:\n{code}")

    def test_python_ast_in_micro_practice_roadmap(self):
        self._verify_python_blocks_in_file(MICRO_PRACTICE_FILE)

    def test_python_ast_in_alignment_matrix(self):
        self._verify_python_blocks_in_file(ALIGNMENT_MATRIX_FILE)

    def test_python_ast_in_cornell_guide(self):
        self._verify_python_blocks_in_file(CORNELL_GUIDE_FILE)


class TestMilestone3MicroPracticeRoadmap(unittest.TestCase):
    """Verify structural and pedagogical compliance of micro_practice_roadmap.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = MICRO_PRACTICE_FILE.read_text(encoding="utf-8")

    def test_buoi0_micro_sessions_and_synthesis(self):
        # Buoi 0 must have exactly 4 micro-sessions + 1 synthesis session
        self.assertIn("MICRO-0.1", self.content)
        self.assertIn("MICRO-0.2", self.content)
        self.assertIn("MICRO-0.3", self.content)
        self.assertIn("MICRO-0.4", self.content)
        self.assertIn("SYNTHESIS-0.S", self.content)
        self.assertIn("MISSION-0.1", self.content)
        self.assertIn("MISSION-0.2", self.content)
        self.assertIn("MISSION-0.3", self.content)
        self.assertIn("MISSION-0.4", self.content)

    def test_buoi1_micro_sessions_and_synthesis(self):
        # Buoi 1 must have exactly 5 micro-sessions + 1 synthesis session
        self.assertIn("MICRO-1.1", self.content)
        self.assertIn("MICRO-1.2", self.content)
        self.assertIn("MICRO-1.3", self.content)
        self.assertIn("MICRO-1.4", self.content)
        self.assertIn("MICRO-1.5", self.content)
        self.assertIn("SYNTHESIS-1.S", self.content)
        self.assertIn("MISSION-1.1", self.content)
        self.assertIn("MISSION-1.2", self.content)
        self.assertIn("MISSION-1.3", self.content)
        self.assertIn("MISSION-1.4", self.content)
        self.assertIn("MISSION-1.5", self.content)

    def test_two_step_pedagogical_rhythm_present(self):
        # Every micro-session must have Step 1 (Pen-first) and Step 2 (Practice & Reflection)
        step1_matches = re.findall(r"Bước 1:\s*Chép Tay Vào Vở Cornell", self.content)
        step2_matches = re.findall(r"Bước 2:\s*Thực Hành Vi Mô & Phản Xạ Phản Biện", self.content)
        # 4 in Buoi 0 + 5 in Buoi 1 = 9 micro-sessions total
        self.assertGreaterEqual(len(step1_matches), 9, f"Expected 9 Step 1 occurrences, found {len(step1_matches)}")
        self.assertGreaterEqual(len(step2_matches), 9, f"Expected 9 Step 2 occurrences, found {len(step2_matches)}")

    def test_definition_of_done_and_duration_in_all_sessions(self):
        dod_matches = re.findall(r"Tiêu Chí Hoàn Thành \(Definition of Done - DoD\)", self.content)
        self.assertGreaterEqual(len(dod_matches), 9, f"Expected 9 DoD sections, found {len(dod_matches)}")

        # Duration 30-45 minutes
        durations = re.findall(r"Thời lượng:\*{0,2}\s*(\d+)\s*Phút", self.content)
        self.assertGreaterEqual(len(durations), 11, f"Expected 11 duration specs (9 micro + 2 synthesis), found {len(durations)}")
        for d in durations:
            minutes = int(d)
            self.assertTrue(30 <= minutes <= 45, f"Duration {minutes} not within 30-45 min range")

    def test_active_recall_with_collapsible_details(self):
        # Diagnostic Active Recall Questions with hidden details
        details_matches = re.findall(r"<details>\s*<summary>.*?<\/summary>.*?<\/details>", self.content, re.DOTALL)
        self.assertGreaterEqual(len(details_matches), 12, f"Expected 12 collapsible Active Recall checks (9 micro + 3 synthesis), found {len(details_matches)}")

    def test_synthesis_readiness_audits(self):
        self.assertIn("Bảng Kiểm Toán Mức Độ Sẵn Sàng (Milestone 0 Readiness Audit)", self.content)
        self.assertIn("Khung Kiểm Toán Chuyển Giao Buổi 1 Sang Tuần 2 (Milestone 1 Readiness Audit)", self.content)


class TestMilestone3CurriculumAlignmentMatrix(unittest.TestCase):
    """Verify alignment matrix links micro-sessions to 14 weeks, HW1-8, competition, capstone."""

    @classmethod
    def setUpClass(cls):
        cls.content = ALIGNMENT_MATRIX_FILE.read_text(encoding="utf-8")

    def test_14_weeks_covered(self):
        for week in range(1, 15):
            self.assertTrue(re.search(rf"Tuần\s*{week}\b", self.content), f"Missing reference to Week {week}")

    def test_8_homeworks_specified(self):
        for hw in range(1, 9):
            self.assertIn(f"HW{hw}", self.content, f"Missing reference to HW{hw}")
        self.assertIn("14.0 / 24.0", self.content)
        self.assertIn("2.0 Điểm", self.content)
        self.assertIn("3.0 Điểm", self.content)

    def test_competition_and_capstone_alignment(self):
        self.assertIn("5-Step ML Ladder", self.content)
        self.assertIn("Top 20%", self.content)
        self.assertIn("Top 10%", self.content)
        self.assertIn("Tokyo Study Tour", self.content)
        self.assertIn("Final Business Capstone", self.content)

    def test_competency_triad(self):
        self.assertTrue(re.search(r"60[–-]70%", self.content))
        self.assertIn("Data Science", self.content)
        self.assertIn("Data Engineering", self.content)


class TestMilestone3CornellNotebookGuide(unittest.TestCase):
    """Verify master Cornell guide content, structure, and methodologies."""

    @classmethod
    def setUpClass(cls):
        cls.content = CORNELL_GUIDE_FILE.read_text(encoding="utf-8")

    def test_three_column_proportions(self):
        self.assertIn("20%", self.content)
        self.assertIn("50%", self.content)
        self.assertIn("30%", self.content)
        self.assertIn("Summary Box", self.content)

    def test_neuroscience_principles(self):
        self.assertIn("Illusion of Competence", self.content)
        self.assertIn("Mueller", self.content)
        self.assertIn("Oppenheimer", self.content)
        self.assertIn("Reticular Activating System", self.content)
        self.assertIn("Motor Cortex", self.content)

    def test_stationery_and_color_coding(self):
        self.assertTrue(re.search(r"B5|A4", self.content))
        self.assertIn("100", self.content)  # 100 gsm
        self.assertIn("Màu 1", self.content)
        self.assertIn("Màu 2", self.content)
        self.assertIn("Màu 3", self.content)

    def test_habit_protocol_and_spaced_repetition(self):
        self.assertIn("Pre-Lecture", self.content)
        self.assertIn("Pen-First", self.content)
        self.assertIn("Post-Session", self.content)
        self.assertIn("T+0", self.content)
        self.assertIn("T+1", self.content)
        self.assertIn("T+3", self.content)
        self.assertIn("T+7", self.content)
        self.assertIn("Cover-and-Recite", self.content)


class TestZeroEmojiCompliance(unittest.TestCase):
    """Verify strict adherence to DeepTutor emoji_policy: none across all deliverables."""

    # Unicode ranges for common emojis
    EMOJI_PATTERN = re.compile(
        r'[\U00010000-\U0010ffff]|'  # SMP (Supplementary Multilingual Plane - includes emojis)
        r'[\u2600-\u27bf]|'          # Misc symbols & dingbats
        r'[\u2300-\u23ff]|'          # Misc technical
        r'[\u2b50-\u2b55]'           # Stars & circles
    )

    def _check_zero_emojis(self, file_path: Path):
        content = file_path.read_text(encoding="utf-8")
        matches = self.EMOJI_PATTERN.findall(content)
        self.assertEqual(len(matches), 0, f"Found emojis in {file_path.name}: {set(matches)}")

    def test_zero_emojis_in_m3_files(self):
        for path in [MICRO_PRACTICE_FILE, ALIGNMENT_MATRIX_FILE, CORNELL_GUIDE_FILE]:
            self._check_zero_emojis(path)

    def test_zero_emojis_globally_across_all_deliverables(self):
        violations = []
        directories = [
            WORKSPACE_ROOT / "slides",
            WORKSPACE_ROOT / "syllabus",
            WORKSPACE_ROOT / "roadmap",
        ]
        target_extensions = {".html", ".md", ".css", ".js"}

        for d in directories:
            self.assertTrue(d.is_dir(), f"Directory not found: {d}")
            for p in sorted(d.rglob("*")):
                if p.is_file() and not p.name.startswith("._") and p.suffix in target_extensions:
                    content = p.read_text(encoding="utf-8")
                    matches = self.EMOJI_PATTERN.findall(content)
                    if matches:
                        violations.append(
                            f"{p.relative_to(WORKSPACE_ROOT)}: Found {len(matches)} emojis -> {set(matches)}"
                        )

        self.assertEqual(
            violations, [],
            "DeepTutor zero-emoji policy violation detected:\n" + "\n".join(f"  - {v}" for v in violations)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
