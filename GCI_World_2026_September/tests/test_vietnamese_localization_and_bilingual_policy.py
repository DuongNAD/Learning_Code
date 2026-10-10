"""
Comprehensive 5-Tier Automated Quality Verification Suite for Vietnamese Localization
and Bilingual Policy Compliance.

Course: Global Consumer Intelligence (GCI World 2026 September)
Lab: Matsuo-Iwasawa Lab, The University of Tokyo
Agent: worker_s4_tests (Teamwork Test Writer)
Policy: emoji_policy: none (Strict Zero Unicode Emojis Workspace-Wide)
RFC 2119 Compliance: Strict

Tiers:
- Tier 1: Slide Decks & Master Hub Vietnamese Localization Completeness
  * html lang="vi"
  * Vietnamese prose character density (>= 80%)
  * Absence of untranslated English narrative paragraphs
  * Mirrored folder binary parity (00_preparatory vs buoi0, 01_orientation vs buoi1, 02_numpy vs buoi2)
- Tier 2: Bilingual Technical Terminology Schema Validation
  * Format: Thuật ngữ Tiếng Anh (Dịch nghĩa tiếng Việt: Bản chất kỹ thuật & Ví dụ minh họa)
  * Terms: Broadcasting, ndarray, View, Copy, CRISP-DM, Dark Data, Tanpin Kanri, LLMs, Z-Score,
           Vectorization, ufunc, Overfitting, Data Leakage, Dummy Variable Trap, etc.
- Tier 3: Interactive Widgets UI Vietnamese Localization
  * Binary equivalence between widgets-bundle.js and visualizer-widgets.js
  * Invariant string and formula preservation
  * Vietnamese UI labels, button names, telemetry readouts, error alerts across all 3 visualizers
- Tier 4: Cornell Handwritten Syllabus Vietnamese & Accents Integrity
  * buoi2_handwritten_notebook_syllabus.md full Vietnamese diacritics integrity
  * Unified active recall cues: *Gợi nhớ (Active Recall Cue):* across buoi0, buoi1, buoi2
  * Executable Python code blocks inside syllabus tables pass ast.parse()
- Tier 5: UTF-8 Encoding & Strict Zero-Emoji Policy
  * Clean UTF-8 decoding without BOM or mojibake corruption
  * Strict emoji_policy: none across all deliverables and test infrastructure
"""

import ast
import filecmp
import json
import re
import unittest
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = WORKSPACE_ROOT / "slides"
SYLLABUS_DIR = WORKSPACE_ROOT / "syllabus"
ROADMAP_DIR = WORKSPACE_ROOT / "roadmap"
NOTES_DIR = WORKSPACE_ROOT / "06_Notes_Transcripts"
MATERIALS_DIR = WORKSPACE_ROOT / "03_Materials"
TESTS_DIR = WORKSPACE_ROOT / "tests"

VIETNAMESE_DIACRITICS_REGEX = re.compile(
    r"[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ"
    r"ÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ]"
)

# Comprehensive Unicode Emoji Regex including SMP, Dingbats, Symbols, and enclosed ideographs
UNICODE_EMOJI_REGEX = re.compile(
    r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u203c\u2049\u2139\u2194-\u2199\u21a9-\u21aa]"
)

# Common mojibake byte-corruption signatures when UTF-8 is misdecoded as Latin-1/CP1252
MOJIBAKE_REGEX = re.compile(r"Ã¡|Ã©|Ã²|Ãº|Ä‘|Æ°|Ã¢|â€|â€“|â€”|\ufffd")


# ==============================================================================
# Tier 1: Slide Decks & Master Hub Vietnamese Localization Completeness
# ==============================================================================
class TestTier1SlideAndMasterHubVietnameseLocalization(unittest.TestCase):
    """Verify that all slides and the master hub are fully localized to Vietnamese."""

    PRIMARY_SLIDE_FILES = [
        SLIDES_DIR / "index.html",
        SLIDES_DIR / "00_preparatory" / "index.html",
        SLIDES_DIR / "01_orientation" / "index.html",
        SLIDES_DIR / "02_numpy" / "index.html",
    ]

    MIRRORED_SLIDE_FILES = [
        SLIDES_DIR / "buoi0" / "index.html",
        SLIDES_DIR / "buoi1" / "index.html",
        SLIDES_DIR / "buoi2" / "index.html",
    ]

    ALL_SLIDE_FILES = PRIMARY_SLIDE_FILES + MIRRORED_SLIDE_FILES

    def test_all_slide_files_exist(self):
        """All primary and mirrored slide HTML files must exist."""
        for path in self.ALL_SLIDE_FILES:
            self.assertTrue(path.is_file(), f"Missing required slide file: {path}")

    def test_html_lang_attribute_is_vi(self):
        """Every slide HTML file must specify <html lang="vi">."""
        lang_pattern = re.compile(r'<html\s+[^>]*lang=["\']vi["\']', re.IGNORECASE)
        for path in self.ALL_SLIDE_FILES:
            content = path.read_text(encoding="utf-8")
            self.assertIsNotNone(
                lang_pattern.search(content),
                f"File {path.relative_to(WORKSPACE_ROOT)} does not declare lang='vi'",
            )

    def test_vietnamese_prose_character_density_exceeds_threshold(self):
        """At least 80% of prose blocks (p, li, h1-4, td, th) must contain Vietnamese diacritics."""
        tag_pattern = re.compile(r"<(p|li|h1|h2|h3|h4|td|th)[^>]*>(.*?)</\1>", re.DOTALL)
        strip_code_pattern = re.compile(
            r"<(script|style|pre|code)[^>]*>.*?</\1>", re.DOTALL
        )
        tag_strip_pattern = re.compile(r"<[^>]+>")

        for path in self.ALL_SLIDE_FILES:
            raw = path.read_text(encoding="utf-8")
            cleaned = strip_code_pattern.sub(" ", raw)
            tags = tag_pattern.findall(cleaned)

            self.assertGreater(
                len(tags),
                0,
                f"No prose elements found in {path.relative_to(WORKSPACE_ROOT)}",
            )

            vn_count = 0
            total_count = 0
            for tag_name, inner in tags:
                plain = tag_strip_pattern.sub(" ", inner).strip()
                # Skip trivial icon/number text (under 3 characters)
                if len(plain) < 3:
                    continue
                total_count += 1
                if VIETNAMESE_DIACRITICS_REGEX.search(plain):
                    vn_count += 1

            self.assertGreater(
                total_count,
                0,
                f"No substantive prose text in {path.relative_to(WORKSPACE_ROOT)}",
            )
            ratio = vn_count / total_count
            self.assertGreaterEqual(
                ratio,
                0.80,
                f"Vietnamese prose density in {path.relative_to(WORKSPACE_ROOT)} is {ratio:.2%}, expected >= 80%",
            )

    def test_zero_untranslated_english_narrative_paragraphs(self):
        """No prose paragraph may contain untranslated narrative English paragraphs."""
        strip_code_pattern = re.compile(
            r"<(script|style|pre|code)[^>]*>.*?</\1>", re.DOTALL
        )
        p_pattern = re.compile(r"<(p|li)[^>]*>(.*?)</\1>", re.DOTALL)
        tag_strip_pattern = re.compile(r"<[^>]+>")

        for path in self.ALL_SLIDE_FILES:
            raw = path.read_text(encoding="utf-8")
            cleaned = strip_code_pattern.sub(" ", raw)
            paragraphs = p_pattern.findall(cleaned)

            violations = []
            for tag_name, inner in paragraphs:
                plain = tag_strip_pattern.sub(" ", inner).strip()
                words = plain.split()
                # If a paragraph has 8 or more words and ZERO Vietnamese diacritics, it is an untranslated block
                if len(words) >= 8 and not VIETNAMESE_DIACRITICS_REGEX.search(plain):
                    # Exclude math formulas or code-heavy blocks
                    if not (plain.startswith("$") or "Addr(" in plain or "0x" in plain):
                        violations.append(plain)

            self.assertEqual(
                len(violations),
                0,
                f"Found untranslated English narrative paragraphs in {path.relative_to(WORKSPACE_ROOT)}:\n"
                + "\n".join(f"  - {v[:100]}..." for v in violations[:5]),
            )

    def test_absence_of_deprecated_untranslated_phrases(self):
        """Explicitly verify that legacy untranslated English phrases have been replaced."""
        deprecated_phrases = [
            "Data science is not merely writing model algorithms",
            "A NumPy ndarray consists of two distinct components",
            "There is no moat in having databases",
            "Transitioning from passive software consumer to active data scientist",
        ]
        for path in self.ALL_SLIDE_FILES:
            content = path.read_text(encoding="utf-8")
            for phrase in deprecated_phrases:
                self.assertNotIn(
                    phrase,
                    content,
                    f"Found deprecated untranslated phrase '{phrase}' in {path.relative_to(WORKSPACE_ROOT)}",
                )

    def test_mirrored_folders_binary_parity(self):
        """Mirrored folders slides/buoi0, buoi1, buoi2 must match their counterparts byte-for-byte."""
        pairs = [
            (
                SLIDES_DIR / "00_preparatory" / "index.html",
                SLIDES_DIR / "buoi0" / "index.html",
            ),
            (
                SLIDES_DIR / "01_orientation" / "index.html",
                SLIDES_DIR / "buoi1" / "index.html",
            ),
            (
                SLIDES_DIR / "02_numpy" / "index.html",
                SLIDES_DIR / "buoi2" / "index.html",
            ),
        ]
        for primary, mirror in pairs:
            self.assertTrue(primary.is_file(), f"Primary missing: {primary}")
            self.assertTrue(mirror.is_file(), f"Mirror missing: {mirror}")
            is_identical = filecmp.cmp(primary, mirror, shallow=False)
            self.assertTrue(
                is_identical,
                f"Binary mismatch between {primary.name} and mirror {mirror.relative_to(WORKSPACE_ROOT)}",
            )


# ==============================================================================
# Tier 2: Bilingual Technical Terminology Schema Validation
# ==============================================================================
class TestTier2BilingualTechnicalTermSchema(unittest.TestCase):
    """Verify presence of the bilingual format Thuật ngữ (Dịch nghĩa: Bản chất & Ví dụ)."""

    SYLLABUS_FILES = [
        SYLLABUS_DIR / "buoi0_handwritten_notebook_syllabus.md",
        SYLLABUS_DIR / "buoi1_handwritten_notebook_syllabus.md",
        SYLLABUS_DIR / "buoi2_handwritten_notebook_syllabus.md",
    ]

    CORE_TECHNICAL_TERMS = [
        ("Broadcasting", ["Lan truyền", "Mở rộng chiều"]),
        ("ndarray", ["Mảng đa chiều"]),
        ("Strides", ["Bước nhảy"]),
        ("View", ["Khung nhìn", "Bản chiếu"]),
        ("Copy", ["Bản sao"]),
        ("CRISP-DM", ["Chu trình", "Khai phá dữ liệu", "Quy trình"]),
        ("Dark Data", ["Dữ liệu tối", "Dữ liệu tiềm ẩn"]),
        ("Tanpin Kanri", ["Quản lý từng món hàng", "Quản lý chi tiết"]),
        ("LLMs", ["Mô hình ngôn ngữ", "Trí tuệ nhân tạo"]),
        ("Z-Score", ["Chuẩn hóa"]),
        ("Vectorization", ["Vector Hóa", "Véc-tơ hóa"]),
        ("ufunc", ["Hàm vạn năng", "Hàm tính toán"]),
        ("Overfitting", ["Quá khớp", "Học vẹt"]),
        ("Data Leakage", ["Rò rỉ dữ liệu", "Rò rỉ"]),
        ("Dummy Variable Trap", ["Bẫy biến giả"]),
    ]

    def test_cornell_syllabus_table_bilingual_schema(self):
        """All Column 1 entries in Cornell syllabus tables must adhere to the bilingual pattern."""
        cell_pattern = re.compile(
            r"\|\s*\*\*([^\*]+)\*\*\s*<br>\s*\*?\(([^\)]+)\)\*?", re.DOTALL
        )

        min_counts = {
            "buoi0_handwritten_notebook_syllabus.md": 20,
            "buoi1_handwritten_notebook_syllabus.md": 20,
            "buoi2_handwritten_notebook_syllabus.md": 15,
        }

        for path in self.SYLLABUS_FILES:
            content = path.read_text(encoding="utf-8")
            matches = cell_pattern.findall(content)

            self.assertGreaterEqual(
                len(matches),
                min_counts[path.name],
                f"Too few bilingual table entries in {path.name}: {len(matches)} found",
            )

            for term, explanation in matches:
                # Must contain Vietnamese diacritics
                self.assertIsNotNone(
                    VIETNAMESE_DIACRITICS_REGEX.search(explanation),
                    f"Explanation for '{term}' in {path.name} lacks Vietnamese diacritics: ({explanation})",
                )
                # Must contain ':' separating Vietnamese definition and technical essence
                self.assertIn(
                    ":",
                    explanation,
                    f"Explanation for '{term}' in {path.name} lacks colon separator: ({explanation})",
                )

    def test_core_technical_terms_bilingual_coverage(self):
        """Every core technical term must be paired with its Vietnamese translation across deliverables."""
        combined_corpus = ""
        for p in self.SYLLABUS_FILES:
            combined_corpus += p.read_text(encoding="utf-8") + "\n"
        for p in TestTier1SlideAndMasterHubVietnameseLocalization.PRIMARY_SLIDE_FILES:
            combined_corpus += p.read_text(encoding="utf-8") + "\n"

        for term, expected_translations in self.CORE_TECHNICAL_TERMS:
            # Term must be in corpus
            self.assertIn(
                term.lower(),
                combined_corpus.lower(),
                f"Core technical term '{term}' not found in syllabus/slide corpus",
            )
            # At least one expected Vietnamese translation must appear near the term or in the corpus
            found_translation = any(
                vn_trans.lower() in combined_corpus.lower()
                for vn_trans in expected_translations
            )
            self.assertTrue(
                found_translation,
                f"Missing expected Vietnamese translation for '{term}' (expected one of: {expected_translations})",
            )

    def test_bilingual_academic_quotes_in_buoi1(self):
        """Buổi 1 must preserve authentic English lecture quotes paired with Vietnamese translations."""
        content = (
            SYLLABUS_DIR / "buoi1_handwritten_notebook_syllabus.md"
        ).read_text(encoding="utf-8")
        # Shuda quote
        self.assertIn("There is no moat in having databases", content)
        self.assertIn("Dịch nghĩa song ngữ", content)
        self.assertIn(
            "Chẳng có con hào bảo vệ nào trong việc chỉ sở hữu các cơ sở dữ liệu",
            content,
        )
        # Demis Hassabis quote
        self.assertIn(
            "Asking the right question is the hardest part of science", content
        )
        self.assertIn(
            "Đặt ra đúng câu hỏi chính là phần khó khăn nhất của khoa học",
            content,
        )


# ==============================================================================
# Tier 3: Interactive Widgets UI Vietnamese Localization
# ==============================================================================
class TestTier3InteractiveWidgetsUILocalization(unittest.TestCase):
    """Verify widgets-bundle.js and visualizer-widgets.js Vietnamese UI and invariants."""

    BUNDLE_PATH = SLIDES_DIR / "js" / "widgets-bundle.js"
    VISUALIZER_PATH = SLIDES_DIR / "js" / "visualizer-widgets.js"
    REVEAL_INIT_PATH = SLIDES_DIR / "js" / "reveal-init.js"

    @classmethod
    def setUpClass(cls):
        cls.bundle_code = cls.BUNDLE_PATH.read_text(encoding="utf-8")
        cls.visualizer_code = cls.VISUALIZER_PATH.read_text(encoding="utf-8")

    def test_widget_bundles_binary_parity(self):
        """widgets-bundle.js and visualizer-widgets.js must be byte-for-byte identical."""
        self.assertTrue(self.BUNDLE_PATH.is_file(), "widgets-bundle.js missing")
        self.assertTrue(self.VISUALIZER_PATH.is_file(), "visualizer-widgets.js missing")
        is_identical = filecmp.cmp(
            self.BUNDLE_PATH, self.VISUALIZER_PATH, shallow=False
        )
        self.assertTrue(
            is_identical,
            "Binary divergence between widgets-bundle.js and visualizer-widgets.js",
        )

    def test_critical_test_invariants_preserved(self):
        """Critical telemetry, formula, and contract invariants must be preserved verbatim."""
        required_invariants = [
            "RAM Conserved",
            "[VIEW: 0 Bytes Allocated]",
            "[COPY:",
            "Formula: Addr(i, j) = 0x1000 + i *",
            "Base: 0x1000 (+ ",
            "AVX-512",
            "stride=0",
            "matrix-cell virtual",
            "Right-to-Left Trailing Alignment",
            "Speedup Factor",
        ]
        for inv in required_invariants:
            self.assertIn(
                inv,
                self.bundle_code,
                f"Critical test invariant '{inv}' was removed or modified in widgets-bundle.js",
            )

    def test_widget1_broadcasting_vietnamese_ui(self):
        """Broadcasting simulator must contain Vietnamese presets, labels, badges, and telemetry."""
        expected_strings = [
            "Mẫu 1: Tích ngoài (Outer Product)",
            "Mẫu 2: Cộng chệch hàng (Row Bias Add)",
            "Mẫu 3: Không tương thích (Incompatible)",
            "Căn lề từ phải sang trái (Right-to-Left Trailing Alignment)",
            "Xác thực căn chỉnh chiều (Dimension Alignment Verification):",
            "[TƯƠNG THÍCH (COMPATIBLE): Shape đầu ra",
            "[LỖI BROADCASTING: Lệch trục (Axis Mismatch)]",
            "Mảng A (Array A)",
            "Mảng B (Array B)",
            "Ma trận kết quả (Result Matrix)",
            "Lưu thực tế trong RAM (Stored In RAM):",
            "Sao chép thô ngây thơ (Naive Duplication):",
            "Tiết kiệm RAM (RAM Conserved):",
        ]
        for s in expected_strings:
            self.assertIn(
                s,
                self.bundle_code,
                f"Missing Widget 1 Vietnamese string: '{s}'",
            )

    def test_widget2_strides_slicing_vietnamese_ui(self):
        """Strides & Memory Slicing visualizer must contain Vietnamese controls and indicators."""
        expected_strings = [
            "Biểu thức cắt lát (Slice Expression):",
            "Cắt lát cơ bản (Basic Slicing - View)",
            "Chỉ mục nâng cao (Fancy Indexing - Copy)",
            "Hàng bắt đầu (Row Start):",
            "Hàng dừng (Row Stop):",
            "Bước nhảy hàng (Row Step):",
            "Cột bắt đầu (Col Start):",
            "Cột dừng (Col Stop):",
            "Bước nhảy cột (Col Step):",
            "Ma trận logic 2D (2D Logical Matrix)",
            "Dải lưu trữ RAM vật lý 1D",
            "Công thức định vị byte (Formula: Addr(i, j) = 0x1000 + i *",
            "[VIEW: 0 Bytes Allocated] (Không tốn RAM)",
            "[COPY:",
            "Cấp phát mới",
        ]
        for s in expected_strings:
            self.assertIn(
                s,
                self.bundle_code,
                f"Missing Widget 2 Vietnamese string: '{s}'",
            )

    def test_widget3_vectorization_benchmark_vietnamese_ui(self):
        """Vectorization benchmark visualizer must contain Vietnamese controls and labels."""
        expected_strings = [
            "Kích thước mảng N (Array Size N):",
            "Cộng từng phần tử: Element Add (a + b)",
            "Tổng tích lũy (Cumsum)",
            "Lọc theo ngưỡng (Threshold Filter)",
            "Vòng lặp Python thuần (Python Loop Execution)",
            "Véc-tơ hóa NumPy C / SIMD (Vectorized)",
            "Hệ số tăng tốc (Speedup Factor)",
            "Nhanh hơn",
            "(Faster)",
            "Véc-tơ hóa NumPy (NumPy Vectorized - AVX-512 SIMD)",
            "Vòng lặp tuần tự Python (Python Iterative for-loop)",
        ]
        for s in expected_strings:
            self.assertIn(
                s,
                self.bundle_code,
                f"Missing Widget 3 Vietnamese string: '{s}'",
            )

    def test_reveal_init_hud_vietnamese_localization(self):
        """The keyboard HUD navigation modal in reveal-init.js must be in Vietnamese."""
        content = self.REVEAL_INIT_PATH.read_text(encoding="utf-8")
        self.assertIn(
            "Bảng điều khiển & Phím tắt (Navigation & Controls HUD)", content
        )
        self.assertIn(
            "Slide tiếp theo / Hiệu ứng con (Next Slide / Fragment)", content
        )
        self.assertIn(
            "Tiến trình dọc (Chủ đề chuyên sâu - Vertical Progression)", content
        )
        self.assertIn(
            "Bật/Tắt lưới tổng quan 2D (Slide Overview Grid)", content
        )
        self.assertIn(
            "Mở cửa sổ ghi chú diễn giả (Speaker Notes Console)", content
        )


# ==============================================================================
# Tier 4: Cornell Handwritten Syllabus Vietnamese & Accents Integrity
# ==============================================================================
class TestTier4CornellSyllabusAccentsAndRecallIntegrity(unittest.TestCase):
    """Verify buoi2 diacritics integrity, active recall cues, and Python AST parsing."""

    BUOI2_PATH = SYLLABUS_DIR / "buoi2_handwritten_notebook_syllabus.md"
    ALL_SYLLABI = [
        SYLLABUS_DIR / "buoi0_handwritten_notebook_syllabus.md",
        SYLLABUS_DIR / "buoi1_handwritten_notebook_syllabus.md",
        SYLLABUS_DIR / "buoi2_handwritten_notebook_syllabus.md",
    ]

    def test_buoi2_syllabus_full_vietnamese_diacritics(self):
        """buoi2_handwritten_notebook_syllabus.md must use standard Vietnamese diacritics."""
        content = self.BUOI2_PATH.read_text(encoding="utf-8")
        body_content = content.split("<!-- Test Compatibility Anchors")[0]

        # Verify absence of legacy unaccented uppercase titles
        self.assertNotIn("DE CUONG VO GHI CHEP TAY", body_content)
        self.assertNotIn("Xu Ly Du Lieu Hieu Nang Cao", body_content)
        self.assertNotIn("COT 1: TU KHOA & GOI NHO", body_content)

        # Verify presence of standard accented titles
        self.assertIn("ĐỀ CƯƠNG VỞ GHI CHÉP TAY", content)
        self.assertIn("Xử Lý Dữ Liệu Hiệu Năng Cao Với NumPy", content)
        self.assertIn("CỘT 1: TỪ KHÓA & GỢI NHỚ", content)
        self.assertIn("CỘT 2: SƠ ĐỒ TƯ DUY & CÔNG THỨC TOÁN", content)
        self.assertIn("CỘT 3: HÀNH ĐỘNG & CODE", content)
        self.assertIn("KHUNG TÓM TẮT & TỰ PHẢN BIỆN", content)
        self.assertIn("BẢNG CHECKLIST HÀNH ĐỘNG TUẦN 2", content)

    def test_active_recall_cues_harmonization(self):
        """All 3 syllabi must use the unified cue format *Gợi nhớ (Active Recall Cue):*."""
        min_cues = {
            "buoi0_handwritten_notebook_syllabus.md": 20,
            "buoi1_handwritten_notebook_syllabus.md": 20,
            "buoi2_handwritten_notebook_syllabus.md": 15,
        }

        total_cues = 0
        for path in self.ALL_SYLLABI:
            content = path.read_text(encoding="utf-8")
            cue_count = content.count("*Gợi nhớ (Active Recall Cue):*")
            total_cues += cue_count

            self.assertGreaterEqual(
                cue_count,
                min_cues[path.name],
                f"Too few active recall cues in {path.name}: {cue_count}",
            )

            # Assert complete absence of legacy cues
            self.assertNotIn(
                "*Hỏi:*",
                content,
                f"Found legacy cue '*Hỏi:*' in {path.name}",
            )
            # Assert no unharmonized *Gợi nhớ:* standing alone
            standalone = re.findall(
                r"\*Gợi nhớ:\*(?!\s*\(Active Recall Cue\))", content
            )
            self.assertEqual(
                len(standalone),
                0,
                f"Found unharmonized standalone '*Gợi nhớ:*' in {path.name}: {standalone}",
            )

        self.assertGreaterEqual(
            total_cues, 60, f"Total active recall cues across syllabi: {total_cues} < 60"
        )

    def test_python_ast_syntax_in_markdown_tables(self):
        """All Python code snippets embedded in syllabus markdown tables must parse cleanly."""
        total_parsed = 0
        for path in self.ALL_SYLLABI:
            content = path.read_text(encoding="utf-8")
            blocks1 = re.findall(r"```python<br>(.*?)<br>```", content, re.DOTALL)
            blocks2 = re.findall(r"```python\n(.*?)\n```", content, re.DOTALL)
            blocks = blocks1 + blocks2

            self.assertGreater(
                len(blocks),
                0,
                f"No python blocks found in {path.name}",
            )

            for i, block in enumerate(blocks):
                clean_code = block.replace("<br>", "\n").strip()
                if not clean_code:
                    continue
                try:
                    ast.parse(clean_code)
                    total_parsed += 1
                except SyntaxError as exc:
                    self.fail(
                        f"SyntaxError in {path.name} code snippet #{i+1}:\n{clean_code}\nError: {exc}"
                    )

        self.assertGreaterEqual(
            total_parsed,
            30,
            f"Expected at least 30 executable Python blocks, parsed {total_parsed}",
        )


# ==============================================================================
# Tier 5: UTF-8 Encoding & Strict Zero-Emoji Policy
# ==============================================================================
class TestTier5Utf8EncodingAndZeroEmojiPolicy(unittest.TestCase):
    """Verify clean UTF-8 encoding without mojibake/BOM and strict zero-emoji policy across deliverables."""

    DELIVERABLE_EXTENSIONS = {".md", ".html", ".js", ".py", ".css", ".json"}
    SCAN_DIRS = [
        "slides",
        "syllabus",
        "roadmap",
        "06_Notes_Transcripts",
        "tests",
        "03_Materials",
    ]

    def _collect_deliverables(self):
        deliverables = []
        for dir_name in self.SCAN_DIRS:
            target_dir = WORKSPACE_ROOT / dir_name
            if not target_dir.exists():
                continue
            for file_path in target_dir.rglob("*"):
                if (
                    file_path.is_file()
                    and not file_path.name.startswith("._")
                    and file_path.suffix in self.DELIVERABLE_EXTENSIONS
                ):
                    deliverables.append(file_path)
        return deliverables

    def test_clean_utf8_decoding_and_no_bom(self):
        """All workspace deliverables must decode strictly as UTF-8 without byte order mark (BOM)."""
        deliverables = self._collect_deliverables()
        self.assertGreater(len(deliverables), 30, "Too few files collected")

        bom_files = []
        decode_errors = []

        for p in deliverables:
            raw_bytes = p.read_bytes()
            if raw_bytes.startswith(b"\xef\xbb\xbf"):
                bom_files.append(str(p.relative_to(WORKSPACE_ROOT)))
            try:
                raw_bytes.decode("utf-8")
            except UnicodeDecodeError as exc:
                decode_errors.append((str(p.relative_to(WORKSPACE_ROOT)), str(exc)))

        self.assertEqual(
            len(bom_files),
            0,
            f"Found UTF-8 BOM in files: {bom_files}",
        )
        self.assertEqual(
            len(decode_errors),
            0,
            f"Found UTF-8 decode errors: {decode_errors}",
        )

    def test_no_mojibake_artifacts(self):
        """No deliverable file may contain mojibake corruption artifacts."""
        deliverables = self._collect_deliverables()
        mojibake_found = []

        for p in deliverables:
            # Skip test files that explicitly test mojibake patterns
            if "test" in p.name:
                continue
            content = p.read_text(encoding="utf-8")
            matches = MOJIBAKE_REGEX.findall(content)
            if matches:
                mojibake_found.append(
                    (str(p.relative_to(WORKSPACE_ROOT)), matches[:5])
                )

        self.assertEqual(
            len(mojibake_found),
            0,
            f"Found mojibake corruption artifacts in: {mojibake_found}",
        )

    def test_strict_global_zero_emoji_compliance(self):
        """Scan all project deliverable files and assert zero unicode emoji violations (emoji_policy: none)."""
        deliverables = self._collect_deliverables()
        violations = []

        for p in deliverables:
            content = p.read_text(encoding="utf-8")
            # If the file is a test file, ignore lines defining emoji regex patterns
            if "test" in p.name:
                lines = [
                    line
                    for line in content.splitlines()
                    if not (
                        "UNICODE_EMOJI_REGEX" in line
                        or "EMOJI_PATTERN" in line
                        or "EMOJI_REGEX" in line
                        or "emoji_pattern" in line
                        or ("re.compile" in line and "00010000" in line)
                    )
                ]
                content = "\n".join(lines)

            emojis = UNICODE_EMOJI_REGEX.findall(content)
            if emojis:
                violations.append(
                    (str(p.relative_to(WORKSPACE_ROOT)), emojis[:10])
                )

        self.assertEqual(
            len(violations),
            0,
            f"Strict emoji_policy: none violated! Emojis found in: {violations}",
        )


if __name__ == "__main__":
    unittest.main()
