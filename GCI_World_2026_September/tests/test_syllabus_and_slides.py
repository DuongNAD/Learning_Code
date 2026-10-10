"""
Comprehensive Automated Verification Suite for GCI World 202609 Syllabus and Slide Systems.
Authoritative Specifications: PROJECT.md (Milestones 1, 2 & 3, Features F19–F35, F56–F75).

Covers:
- Tier 1: Deliverable Existence, Encoding & Non-emptiness (Modern Reveal.js files and purge of legacy files).
- Tier 2: HTML Presentation Engine Integrity (Reveal.js 5.1.0 CDN, KaTeX, Highlight.js, 2D grid structure).
- Tier 3: Markdown Presentation Structure & Purge Verification (legacy MD slides purged, syllabi intact).
- Tier 4: Cornell Handwritten Notebook Syllabus (3-column layout, 4-9 core parts, 2-min summary boxes across Buoi 0, 1, 2).
- Tier 5: Python AST Correctness (all executable Python snippets in syllabi and HTML slides parse cleanly).
- Tier 6: Feature Coverage F01–F18 (Buoi 0) and F19–F32 (Buoi 1).
- Tier 7: Interactive Dynamic Visualizer Modules & Widget Contracts.
- Tier 8: Global Zero-Emoji Compliance (emoji_policy: none).
"""

import ast
import re
import unittest
from pathlib import Path

# Paths
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = WORKSPACE_ROOT / "slides"
SYLLABUS_DIR = WORKSPACE_ROOT / "syllabus"
ROADMAP_DIR = WORKSPACE_ROOT / "roadmap"

CSS_THEME_FILE = SLIDES_DIR / "css" / "reveal-gci-theme.css"
CSS_WIDGETS_FILE = SLIDES_DIR / "css" / "slide-widgets.css"
JS_INIT_FILE = SLIDES_DIR / "js" / "reveal-init.js"
JS_WIDGETS_FILE = SLIDES_DIR / "js" / "widgets-bundle.js"

MASTER_HUB = SLIDES_DIR / "index.html"
BUOI0_HTML = SLIDES_DIR / "00_preparatory" / "index.html"
BUOI0_SYLLABUS = SYLLABUS_DIR / "buoi0_handwritten_notebook_syllabus.md"

BUOI1_HTML = SLIDES_DIR / "01_orientation" / "index.html"
BUOI1_SYLLABUS = SYLLABUS_DIR / "buoi1_handwritten_notebook_syllabus.md"

BUOI2_HTML = SLIDES_DIR / "02_numpy" / "index.html"
BUOI2_SYLLABUS = SYLLABUS_DIR / "buoi2_handwritten_notebook_syllabus.md"


class TestTier1DeliverableExistence(unittest.TestCase):
    """Verify presence of modern deliverables and complete purge of obsolete files."""

    DEPRECATED_FILES = [
        SLIDES_DIR / "buoi0_preparatory_slides.html",
        SLIDES_DIR / "buoi0_preparatory_slides.md",
        SLIDES_DIR / "buoi1_orientation_slides.html",
        SLIDES_DIR / "buoi1_orientation_slides.md",
        SLIDES_DIR / "buoi1_interactive_dynamic_slides.html",
        SLIDES_DIR / "css" / "minimalist-deck.css",
        SLIDES_DIR / "js" / "minimalist-deck.js",
        WORKSPACE_ROOT / "study_notes" / "numpy_slides.html",
        WORKSPACE_ROOT / "study_notes" / "numpy_optimization_slides.md",
        WORKSPACE_ROOT / "study_notes" / "restructure.py",
    ]

    def test_legacy_slides_completely_purged(self):
        """Assert that all 10 deprecated files are permanently removed."""
        for path in self.DEPRECATED_FILES:
            self.assertFalse(path.exists(), f"Old file still exists: {path}")

    def test_shared_deck_assets_exist(self):
        """Verify presence and size of modern Reveal.js shared assets."""
        for path in [CSS_THEME_FILE, CSS_WIDGETS_FILE, JS_INIT_FILE, JS_WIDGETS_FILE]:
            self.assertTrue(path.is_file(), f"Missing {path}")
            self.assertGreater(path.stat().st_size, 2000)

    def test_master_slide_hub_exists(self):
        self.assertTrue(MASTER_HUB.is_file(), f"Missing {MASTER_HUB}")
        self.assertGreater(MASTER_HUB.stat().st_size, 3000)

    def test_buoi0_deliverables_exist(self):
        for path in [BUOI0_HTML, BUOI0_SYLLABUS]:
            self.assertTrue(path.is_file(), f"Missing {path}")
            self.assertGreater(path.stat().st_size, 10000)

    def test_buoi1_deliverables_exist(self):
        for path in [BUOI1_HTML, BUOI1_SYLLABUS]:
            self.assertTrue(path.is_file(), f"Missing {path}")
            self.assertGreater(path.stat().st_size, 10000)

    def test_buoi2_deliverables_exist(self):
        for path in [BUOI2_HTML, BUOI2_SYLLABUS]:
            self.assertTrue(path.is_file(), f"Missing {path}")
            self.assertGreater(path.stat().st_size, 10000)

    def test_files_valid_utf8(self):
        targets = [
            MASTER_HUB, BUOI0_HTML, BUOI0_SYLLABUS,
            BUOI1_HTML, BUOI1_SYLLABUS, BUOI2_HTML, BUOI2_SYLLABUS,
            CSS_THEME_FILE, CSS_WIDGETS_FILE, JS_INIT_FILE, JS_WIDGETS_FILE
        ]
        for path in targets:
            content = path.read_text(encoding="utf-8")
            self.assertGreater(len(content), 0)


class TestTier2Buoi0HTMLPresentationEngine(unittest.TestCase):
    """Verify Buoi 0 Reveal.js HTML presentation engine, 2D sections, HUD controls, and CDN."""

    @classmethod
    def setUpClass(cls):
        cls.html = BUOI0_HTML.read_text(encoding="utf-8")

    def test_buoi0_reveal_structure(self):
        self.assertIn('<div class="reveal">', self.html)
        self.assertIn('<div class="slides">', self.html)
        sections = re.findall(r'<section', self.html)
        self.assertGreaterEqual(len(sections), 15, f"Expected >= 15 sections in Buoi 0, found {len(sections)}")

    def test_buoi0_css_and_js_linkages(self):
        self.assertIn('reveal-gci-theme.css', self.html)
        self.assertIn('slide-widgets.css', self.html)
        self.assertIn('reveal-init.js', self.html)
        self.assertIn('katex', self.html.lower())
        self.assertIn('highlight.js', self.html.lower())

    def test_buoi0_hud_header_present(self):
        self.assertIn('class="deck-hud-header"', self.html)
        self.assertIn('id="hud-trigger-btn"', self.html)

    def test_buoi0_core_chapters_present(self):
        self.assertIn("Preparatory Knowledge &amp; Data Science Fundamentals", self.html)
        self.assertIn("4-Step Data Science Life Cycle", self.html)
        self.assertIn("Data Taxonomy", self.html)
        self.assertIn("Machine Learning Landscape", self.html)
        self.assertIn("Applied Statistics", self.html)
        self.assertIn("Python OOP", self.html)


class TestTier2HTMLPresentationEngine(unittest.TestCase):
    """Verify Buoi 1 Reveal.js presentation engine, CDN linkages, 2D sections, and HUD."""

    @classmethod
    def setUpClass(cls):
        cls.html = BUOI1_HTML.read_text(encoding="utf-8")

    def test_slide_structure_and_count(self):
        self.assertIn('<div class="reveal">', self.html)
        self.assertIn('<div class="slides">', self.html)
        sections = re.findall(r'<section', self.html)
        self.assertGreaterEqual(len(sections), 15, f"Expected >= 15 sections, found {len(sections)}")

    def test_css_and_js_linkages(self):
        self.assertIn('reveal-gci-theme.css', self.html)
        self.assertIn('slide-widgets.css', self.html)
        self.assertIn('reveal-init.js', self.html)
        self.assertIn('katex', self.html.lower())
        self.assertIn('highlight.js', self.html.lower())

    def test_hud_header_present(self):
        self.assertIn('class="deck-hud-header"', self.html)
        self.assertIn('id="hud-trigger-btn"', self.html)

    def test_core_micro_sessions_covered(self):
        self.assertIn("Zettabyte Data Growth", self.html)
        self.assertTrue("Dark Data" in self.html)
        self.assertIn("Tanpin Kanri", self.html)
        self.assertIn("14-Week Curriculum", self.html)


class TestTier2Buoi2HTMLPresentationEngine(unittest.TestCase):
    """Verify Buoi 2 Reveal.js presentation engine and 3 interactive widget containers."""

    @classmethod
    def setUpClass(cls):
        cls.html = BUOI2_HTML.read_text(encoding="utf-8")

    def test_buoi2_reveal_structure(self):
        self.assertIn('<div class="reveal">', self.html)
        self.assertIn('<div class="slides">', self.html)
        sections = re.findall(r'<section', self.html)
        self.assertGreaterEqual(len(sections), 15)

    def test_buoi2_widgets_bundle_linkage(self):
        self.assertIn('widgets-bundle.js', self.html)
        self.assertIn('reveal-init.js', self.html)

    def test_buoi2_interactive_widgets_present(self):
        self.assertIn('id="widget-broadcasting-container"', self.html)
        self.assertIn('id="widget-strides-container"', self.html)
        self.assertIn('id="widget-vectorization-container"', self.html)


class TestTier3MarkdownPresentation(unittest.TestCase):
    """Verify obsolete MD slides are purged and Cornell syllabus markdown is intact."""

    def test_legacy_md_slides_purged(self):
        self.assertFalse((SLIDES_DIR / "buoi0_preparatory_slides.md").exists())
        self.assertFalse((SLIDES_DIR / "buoi1_orientation_slides.md").exists())

    def test_syllabi_markdown_integrity(self):
        for syl_file in [BUOI0_SYLLABUS, BUOI1_SYLLABUS, BUOI2_SYLLABUS]:
            text = syl_file.read_text(encoding="utf-8")
            self.assertGreater(len(text), 10000)
            self.assertTrue(re.search(r"COT 1|Cột 1|CỘT 1", text))
            self.assertTrue(re.search(r"COT 2|Cột 2|CỘT 2", text))
            self.assertTrue(re.search(r"COT 3|Cột 3|CỘT 3", text))

    def test_core_lecture_milestones_covered_in_syllabi(self):
        b0_text = BUOI0_SYLLABUS.read_text(encoding="utf-8")
        self.assertIn("Car Price", b0_text)
        self.assertIn("Mushroom", b0_text)

        b1_text = BUOI1_SYLLABUS.read_text(encoding="utf-8")
        self.assertTrue(re.search(r"Tư Duy Định Hướng Dữ Liệu|Evidence-Based|Data Science", b1_text))
        self.assertTrue("7-Eleven" in b1_text or "Seven-Eleven" in b1_text)
        self.assertIn("Omnicampus", b1_text)

        b2_text = BUOI2_SYLLABUS.read_text(encoding="utf-8")
        self.assertIn("C-Contiguous", b2_text)
        self.assertIn("SIMD", b2_text)
        self.assertIn("Broadcasting", b2_text)


class TestTier4Buoi0CornellHandwrittenSyllabus(unittest.TestCase):
    """Verify Cornell 3-column layout, 9 core parts, 2-min summary box, and workshops."""

    @classmethod
    def setUpClass(cls):
        cls.syllabus = BUOI0_SYLLABUS.read_text(encoding="utf-8")

    def test_buoi0_three_column_format(self):
        self.assertIn("Cột 1: Từ khóa & Gợi nhớ", self.syllabus)
        self.assertIn("Cột 2: Sơ đồ tư duy & Cơ chế vận hành", self.syllabus)
        self.assertIn("Cột 3: Hành động & Code minh họa", self.syllabus)

    def test_buoi0_nine_parts_present(self):
        for i in range(1, 10):
            self.assertIn(f"PHẦN {i}:", self.syllabus)

    def test_buoi0_summary_boxes_and_active_recall(self):
        self.assertIn("KHUNG TÓM TẮT & PHẢN XẠ 2 PHÚT CUỐI TRANG", self.syllabus)
        self.assertIn("3 CHÂN LÝ CỐT LÕI", self.syllabus)
        self.assertIn("3 CÂU HỎI TRUY HỒI TỰ KIỂM TRA PHẢN XẠ", self.syllabus)

    def test_buoi0_workshops_summary(self):
        self.assertIn("WORKSHOP 1: HỒI QUY GIÁ XE (Car Price)", self.syllabus)
        self.assertIn("WORKSHOP 2: PHÂN LOẠI NẤM ĐỘC (Mushroom)", self.syllabus)


class TestTier4CornellHandwrittenSyllabus(unittest.TestCase):
    """Verify Cornell 3-column format, 4 parts, 2-min summary boxes, and action checklist."""

    @classmethod
    def setUpClass(cls):
        cls.syllabus = BUOI1_SYLLABUS.read_text(encoding="utf-8")

    def test_three_column_format_and_cues(self):
        self.assertIn("CỘT 1: TỪ KHÓA & GỢI NHỚ", self.syllabus)
        self.assertIn("CỘT 2: SƠ ĐỒ TƯ DUY & CÔNG THỨC TOÁN", self.syllabus)
        self.assertIn("CỘT 3: HÀNH ĐỘNG & CODE", self.syllabus)

    def test_four_core_parts_present(self):
        self.assertIn("## PHẦN 1: TƯ DUY ĐỊNH HƯỚNG DỮ LIỆU", self.syllabus)
        self.assertIn("## PHẦN 2: HÀO LŨY AI, BÁNH ĐÀ DỮ LIỆU", self.syllabus)
        self.assertIn("## PHẦN 3: LỘ TRÌNH 14 TUẦN", self.syllabus)
        self.assertIn("## PHẦN 4: HỆ SINH THÁI CÔNG CỤ", self.syllabus)

    def test_summary_boxes_in_all_parts(self):
        matches = re.findall(r'KHUNG TÓM TẮT & TỰ PHẢN BIỆN PHẦN \d', self.syllabus)
        self.assertEqual(len(matches), 4, f"Expected 4 summary boxes, found {len(matches)}")
        self.assertIn("3 Điểm Chốt Hạ", self.syllabus)
        self.assertIn("Active Recall Check", self.syllabus)

    def test_action_checklist_present(self):
        self.assertIn("BẢNG CHECKLIST HÀNH ĐỘNG TUẦN 1", self.syllabus)
        self.assertIn("08/10/2026", self.syllabus)
        self.assertIn("Duongne2000", self.syllabus)


class TestTier4Buoi2CornellHandwrittenSyllabus(unittest.TestCase):
    """Verify Buoi 2 Cornell 3-column format, 5 parts, summary boxes, and action checklist."""

    @classmethod
    def setUpClass(cls):
        cls.syllabus = BUOI2_SYLLABUS.read_text(encoding="utf-8")

    def test_buoi2_three_column_format(self):
        self.assertTrue(re.search(r"(?:COT|C[ỘO]T)\s*1.*(?:TU\s*KHOA|T[ỪU]\s*KH[ÓO]A)", self.syllabus, re.IGNORECASE))
        self.assertTrue(re.search(r"(?:COT|C[ỘO]T)\s*2.*(?:SO\s*DO\s*TU\s*DUY|S[ƠO]\s*Đ[ỒO]\s*T[ƯU]\s*DUY)", self.syllabus, re.IGNORECASE))
        self.assertTrue(re.search(r"(?:COT|C[ỘO]T)\s*3.*(?:HANH\s*DONG|H[ÀA]NH\s*Đ[ỘO]NG)", self.syllabus, re.IGNORECASE))

    def test_buoi2_five_parts_present(self):
        for i in range(1, 6):
            self.assertTrue(re.search(rf"(?:PHAN|PH[ẦA]N)\s*{i}:", self.syllabus, re.IGNORECASE))

    def test_buoi2_summary_boxes_and_active_recall(self):
        self.assertTrue(re.search(r"KHUNG\s*T[ÓO]M\s*T[ẮA]T|KHUNG TOM TAT", self.syllabus, re.IGNORECASE))
        self.assertTrue(re.search(r"3\s*Điểm\s*Chốt\s*Hạ|3\s*Diem\s*Chot\s*Ha", self.syllabus, re.IGNORECASE))
        self.assertIn("Active Recall Check", self.syllabus)

    def test_buoi2_action_checklist_present(self):
        self.assertTrue(re.search(r"B[ẢA]NG\s*CHECKLIST\s*H[ÀA]NH\s*Đ[ỘO]NG|BANG CHECKLIST HANH DONG", self.syllabus, re.IGNORECASE))
        self.assertIn("08/10/2026", self.syllabus)
        self.assertIn("homework(a)", self.syllabus)


class TestTier5PythonASTCorrectness(unittest.TestCase):
    """Extract and parse all Python code snippets across syllabi and HTML slides."""

    def test_ast_python_in_buoi0_syllabus_tables(self):
        content = BUOI0_SYLLABUS.read_text(encoding="utf-8")
        blocks = re.findall(r'```python<br>(.*?)<br>```', content, re.DOTALL)
        self.assertGreaterEqual(len(blocks), 4, "Expected at least 4 python blocks in Buoi 0 syllabus")
        for i, block in enumerate(blocks):
            clean_code = block.replace("<br>", "\n")
            try:
                ast.parse(clean_code)
            except SyntaxError as e:
                self.fail(f"SyntaxError in buoi0 syllabus table block {i+1}: {e}\nCode:\n{clean_code}")

    def test_ast_python_in_buoi1_syllabus_tables(self):
        content = BUOI1_SYLLABUS.read_text(encoding="utf-8")
        blocks = re.findall(r'```python<br>(.*?)<br>```', content, re.DOTALL)
        self.assertGreaterEqual(len(blocks), 4, "Expected at least 4 python blocks in Buoi 1 syllabus")
        for i, block in enumerate(blocks):
            clean_code = block.replace("<br>", "\n")
            try:
                ast.parse(clean_code)
            except SyntaxError as e:
                self.fail(f"SyntaxError in buoi1 syllabus table block {i+1}: {e}\nCode:\n{clean_code}")

    def test_ast_python_in_buoi2_syllabus_tables(self):
        content = BUOI2_SYLLABUS.read_text(encoding="utf-8")
        blocks = re.findall(r'```python<br>(.*?)<br>```', content, re.DOTALL)
        self.assertGreaterEqual(len(blocks), 10, "Expected at least 10 python blocks in Buoi 2 syllabus")
        for i, block in enumerate(blocks):
            clean_code = block.replace("<br>", "\n")
            try:
                ast.parse(clean_code)
            except SyntaxError as e:
                self.fail(f"SyntaxError in buoi2 syllabus table block {i+1}: {e}\nCode:\n{clean_code}")

    def test_ast_python_in_html_slides(self):
        for html_path in [BUOI0_HTML, BUOI2_HTML]:
            content = html_path.read_text(encoding="utf-8")
            blocks = re.findall(r'<code class=[\"\']language-python[\"\']>([\s\S]*?)</code>', content)
            self.assertGreaterEqual(len(blocks), 2, f"Expected python blocks in {html_path.name}")
            for i, raw_code in enumerate(blocks):
                clean_code = raw_code.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
                try:
                    ast.parse(clean_code)
                except SyntaxError as e:
                    self.fail(f"SyntaxError in {html_path.name} block {i+1}: {e}\nCode:\n{clean_code}")


class TestTier6FeatureCoverageF01toF18(unittest.TestCase):
    """Verify 100% academic coverage of cataloged features F01–F18 in Buổi 0."""

    @classmethod
    def setUpClass(cls):
        cls.html = BUOI0_HTML.read_text(encoding="utf-8")
        cls.syllabus = BUOI0_SYLLABUS.read_text(encoding="utf-8")
        cls.combined = cls.html + "\n" + cls.syllabus

    def test_f01_matsuo_lab_philosophy(self):
        self.assertTrue(re.search(r"matsuo|yutaka|đại học tokyo", self.combined, re.IGNORECASE))

    def test_f02_three_pillars(self):
        self.assertIn("Domain Knowledge", self.combined)
        self.assertTrue(re.search(r"60[–-]70%", self.combined))

    def test_f03_four_step_workflow(self):
        for step in ["Understanding", "Preprocessing", "Modeling", "Evaluation"]:
            self.assertIn(step, self.combined)

    def test_f04_data_taxonomy(self):
        self.assertIn("Structured", self.combined)
        self.assertIn("Unstructured", self.combined)

    def test_f05_scales_of_measurement(self):
        self.assertTrue("Quantitative" in self.combined or "Định Lượng" in self.combined)
        self.assertTrue("Qualitative" in self.combined or "Định Tính" in self.combined)
        self.assertIn("Continuous", self.combined)
        self.assertIn("Nominal", self.combined)

    def test_f06_missing_data_imputation(self):
        self.assertIn("dropna", self.combined)
        self.assertIn("fillna", self.combined)
        self.assertIn("mode", self.combined.lower())

    def test_f07_dummy_variable_trap(self):
        self.assertIn("drop_first", self.combined)
        self.assertTrue(re.search(r"K\s*-\s*1", self.combined))

    def test_f08_zscore_standardization(self):
        self.assertIn("StandardScaler", self.combined)
        self.assertIn("Data Leakage", self.combined)

    def test_f09_train_test_split(self):
        self.assertIn("train_test_split", self.combined)
        self.assertTrue(re.search(r"80/20|80%|20%", self.combined))

    def test_f10_overfitting_mitigation(self):
        self.assertIn("Overfitting", self.combined)
        self.assertIn("max_depth", self.combined)

    def test_f11_central_tendency(self):
        self.assertIn("mean", self.combined.lower())
        self.assertIn("median", self.combined.lower())

    def test_f12_dispersion_and_gaussian(self):
        self.assertTrue(re.search(r"68(?:\.3)?", self.combined) and "Gaussian" in self.combined)

    def test_f13_tukey_iqr_boxplot(self):
        self.assertIn("IQR", self.combined)
        self.assertTrue(re.search(r"1\.5\s*\*?\s*IQR", self.combined))

    def test_f14_pearson_correlation(self):
        self.assertIn("Pearson", self.combined)
        self.assertIn("Causation", self.combined)

    def test_f15_python_oop(self):
        self.assertIn("class Pokemon", self.combined)
        self.assertIn("__init__", self.combined)

    def test_f16_relational_merge(self):
        self.assertIn("pd.merge", self.combined)
        self.assertTrue("how='left'" in self.combined or 'how="left"' in self.combined)

    def test_f17_ml_taxonomy(self):
        self.assertIn("Supervised", self.combined)
        self.assertIn("Unsupervised", self.combined)
        self.assertTrue("Reinforcement" in self.combined or "RL" in self.combined or "Tăng Cường" in self.combined)

    def test_f18_supervised_algorithms(self):
        self.assertIn("LinearRegression", self.combined)
        self.assertIn("DecisionTreeClassifier", self.combined)


class TestTier6FeatureCoverageF19toF32(unittest.TestCase):
    """Verify 100% academic coverage of cataloged features F19–F32."""

    @classmethod
    def setUpClass(cls):
        cls.html = BUOI1_HTML.read_text(encoding="utf-8")
        cls.syllabus = BUOI1_SYLLABUS.read_text(encoding="utf-8")
        cls.combined = cls.html + "\n" + cls.syllabus

    def test_f19_zettabyte_growth(self):
        self.assertTrue(re.search(r"527\s*ZB", self.combined), "F19: Missing 527 ZB growth projection")
        self.assertTrue(re.search(r"10\^?\{?21\}?", self.combined), "F19: Missing 10^21 byte conversion")

    def test_f20_crisp_dm_lifecycle(self):
        for phase in ["Business Understanding", "Data Understanding", "Data Preparation", "Modeling", "Evaluation", "Deployment"]:
            self.assertIn(phase, self.combined, f"F20: Missing CRISP-DM phase: {phase}")

    def test_f21_dark_data_and_selection_bias(self):
        self.assertIn("David J. Hand", self.combined)
        self.assertIn("Isao Hosoya", self.combined)
        self.assertIn("Food Truck", self.combined)
        self.assertIn("Selection Bias", self.combined)

    def test_f22_problem_to_data_translation(self):
        self.assertTrue(re.search(r"KGI|KPI", self.combined), "F22: Missing KGI/KPI reference")
        self.assertIn("Target", self.combined)

    def test_f23_ds_competency_triad(self):
        self.assertTrue(re.search(r"60[–-]70%", self.combined), "F23: Missing 60-70% domain knowledge ratio")
        self.assertIn("Domain", self.combined)

    def test_f24_seven_eleven_empirical_loop(self):
        self.assertIn("Tanpin Kanri", self.combined)
        self.assertTrue("7-Eleven" in self.combined or "Seven-Eleven" in self.combined)
        self.assertTrue(re.search(r"Observe.*Hypothesize.*(?:Experiment|Order).*(?:Action|Check|Revise)", self.combined, re.IGNORECASE | re.DOTALL))

    def test_f25_defensible_ai_moats(self):
        self.assertIn("Workflow Integration", self.combined)
        self.assertIn("SaaS", self.combined)

    def test_f26_compound_data_flywheel(self):
        self.assertIn("Data Flywheel", self.combined)
        self.assertIn("Vertical AI", self.combined)

    def test_f27_14_week_curriculum_roadmap(self):
        self.assertIn("14", self.combined)
        self.assertIn("NumPy", self.combined)
        self.assertIn("Pandas", self.combined)
        self.assertIn("Optuna", self.combined)

    def test_f28_ecosystem_and_platform_stack(self):
        self.assertIn("Omnicampus", self.combined)
        self.assertIn("Quri", self.combined)
        self.assertTrue("Google Colab" in self.combined or "Colab" in self.combined)
        self.assertIn("Slack", self.combined)

    def test_f29_three_tier_completion_model(self):
        self.assertIn("Honors", self.combined)
        self.assertIn("Tokyo", self.combined)
        self.assertTrue(re.search(r"10%", self.combined))
        self.assertTrue(re.search(r"20%", self.combined))

    def test_f30_course_policy_and_integrity(self):
        self.assertIn("08/10/2026", self.combined)
        self.assertIn("7/14", self.combined)
        self.assertIn("14/24", self.combined)
        self.assertIn("Late", self.combined)

    def test_f31_ml_operational_ladder(self):
        self.assertIn("5", self.combined)
        self.assertIn("Baseline", self.combined)
        self.assertIn("Optuna", self.combined)
        self.assertIn("Recall", self.combined)
        self.assertIn("Precision", self.combined)

    def test_f32_human_ai_co_evolution(self):
        self.assertIn("Falsification", self.combined)
        self.assertIn("Demis Hassabis", self.combined)


class TestTier7InteractiveDynamicModules(unittest.TestCase):
    """Verify presence, integrity, and contracts of interactive visualizer modules across decks and explorable."""

    @classmethod
    def setUpClass(cls):
        cls.b2_html = BUOI2_HTML.read_text(encoding="utf-8")
        cls.js = JS_WIDGETS_FILE.read_text(encoding="utf-8")
        cls.css = CSS_WIDGETS_FILE.read_text(encoding="utf-8")

    def test_broadcasting_widget_structure(self):
        """Module 1: Broadcasting Simulator elements and contracts."""
        self.assertIn('id="widget-broadcasting-container"', self.b2_html)
        self.assertIn('id="broadcast-alignment-card"', self.b2_html)
        self.assertIn('id="broadcast-grid-a"', self.b2_html)
        self.assertIn('id="broadcast-grid-b"', self.b2_html)
        self.assertIn('id="broadcast-grid-c"', self.b2_html)

    def test_strides_slicing_widget_structure(self):
        """Module 2: Strides & Slicing Memory Visualizer elements and contracts."""
        self.assertIn('id="widget-strides-container"', self.b2_html)
        self.assertIn('id="strides-slice-code"', self.b2_html)
        self.assertIn('id="strides-grid-container"', self.b2_html)
        self.assertIn('id="strides-ram-strip"', self.b2_html)

    def test_vectorization_benchmark_structure(self):
        """Module 3: SIMD Vectorization vs Python Loop Benchmark elements and contracts."""
        self.assertIn('id="widget-vectorization-container"', self.b2_html)
        self.assertIn('id="vec-speedup-svg"', self.b2_html)
        self.assertIn('id="race-bar-numpy"', self.b2_html)
        self.assertIn('id="race-bar-python"', self.b2_html)

    def test_js_widgets_bundle_exports(self):
        """Verify JS presentation engine exports all 3 interactive visualizers."""
        self.assertIn('mountBroadcastingWidget', self.js)
        self.assertIn('mountStridesWidget', self.js)
        self.assertIn('mountVectorizationWidget', self.js)
        self.assertIn('handleSlideChange', self.js)

    def test_css_interactive_classes(self):
        """Verify CSS contains dedicated styling for all interactive visualizers."""
        self.assertIn('#widget-broadcasting-container', self.css)
        self.assertIn('#widget-strides-container', self.css)
        self.assertIn('#widget-vectorization-container', self.css)
        self.assertIn('.matrix-cell', self.css)
        self.assertIn('.ram-cell', self.css)
        self.assertIn('.vec-visual-race', self.css)
        self.assertIn('.race-bar', self.css)

    def test_explorable_threeui_integration(self):
        """Verify pre-existing explorable engines for Buoi 1 and Buoi 2 remain intact."""
        self.assertTrue((WORKSPACE_ROOT / "explorable" / "buoi1" / "index.html").is_file())
        self.assertTrue((WORKSPACE_ROOT / "explorable" / "buoi2" / "index.html").is_file())
        self.assertTrue((WORKSPACE_ROOT / "explorable" / "buoi1" / "models_buoi1.js").is_file())
        self.assertTrue((WORKSPACE_ROOT / "explorable" / "buoi2" / "models_buoi2.js").is_file())


class TestGlobalZeroEmojiCompliance(unittest.TestCase):
    """
    Verify strict zero-emoji compliance (emoji_policy: none) across
    all project files in slides/, syllabus/, and roadmap/.
    """

    EMOJI_PATTERN = re.compile(
        r'[\U00010000-\U0010ffff]|'  # SMP: Emoji, pictographs, symbols
        r'[\u2600-\u27bf]|'          # Misc symbols, dingbats, warnings, stars
        r'[\u2300-\u23ff]|'          # Misc technical (stopwatch, keyboard, etc.)
        r'[\u2b50-\u2b55]|'          # Heavy stars & geometric circles
        r'[\u203c\u2049\u2139\u2194-\u2199\u21a9-\u21aa]'
    )

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
