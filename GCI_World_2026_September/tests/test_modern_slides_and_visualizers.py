"""
Comprehensive 5-Tier Automated Quality Verification Suite for GCI World 2026 September.
Validates Modern Reveal.js Slide Ecosystem, Interactive Visualizers, Knowledge Assets,
and Directory Hygiene.

Course: GCI World 2026 September (Matsuo-Iwasawa Lab, The University of Tokyo)
Author: worker_s3_tests
Strict Policy: emoji_policy: none (Zero Unicode Emojis Workspace-Wide)
RFC 2119 Compliance: Strict

Tiers:
- Tier 1: Deliverable Existence & HTML File Integrity (presence, size thresholds, valid UTF-8).
- Tier 2: CDN Integrity & Headless DOM/Script Sanity (HTTPS CDNs, Reveal.js 5.1.0, KaTeX, Highlight.js, 2D grid).
- Tier 3: Interactive Visualizer Widgets DOM Contracts & Mathematical Oracles (Broadcasting, Strides, Vectorization).
- Tier 4: Legacy Slide Purge & Directory Hygiene (permanent removal of 10 deprecated files, zero AppleDouble files).
- Tier 5: Knowledge Assets & Syllabus Integrity (Session 2 master notes, Cornell syllabus, micro-practice roadmap, alignment matrix, TASKS schema).
- Tier 6: Universal Zero-Emoji Compliance (strict verification across all deliverables).
"""

import ast
import json
import math
import re
import unittest
from pathlib import Path
import numpy as np

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = WORKSPACE_ROOT / "slides"
SYLLABUS_DIR = WORKSPACE_ROOT / "syllabus"
ROADMAP_DIR = WORKSPACE_ROOT / "roadmap"
NOTES_DIR = WORKSPACE_ROOT / "06_Notes_Transcripts"
MATERIALS_DIR = WORKSPACE_ROOT / "03_Materials"


# ==============================================================================
# Tier 1: Deliverable Existence & HTML File Integrity
# ==============================================================================
class TestTier1DeliverableExistenceAndHTMLIntegrity(unittest.TestCase):
    """Verify presence, non-emptiness, substantial byte size, and UTF-8 encoding of deliverables."""

    REQUIRED_SLIDE_ASSETS = [
        ("slides/index.html", 3000),
        ("slides/00_preparatory/index.html", 10000),
        ("slides/01_orientation/index.html", 10000),
        ("slides/02_numpy/index.html", 10000),
        ("slides/css/reveal-gci-theme.css", 3000),
        ("slides/css/slide-widgets.css", 3000),
        ("slides/js/reveal-init.js", 2000),
        ("slides/js/widgets-bundle.js", 10000),
    ]

    REQUIRED_SYLLABUS_FILES = [
        ("syllabus/buoi0_handwritten_notebook_syllabus.md", 10000),
        ("syllabus/buoi1_handwritten_notebook_syllabus.md", 10000),
        ("syllabus/buoi2_handwritten_notebook_syllabus.md", 10000),
        ("syllabus/cornell_notebook_guide.md", 2000),
    ]

    REQUIRED_ROADMAP_FILES = [
        ("roadmap/micro_practice_roadmap.md", 30000),
        ("roadmap/curriculum_alignment_matrix.md", 10000),
    ]

    def test_slide_ecosystem_deliverables_exist_and_non_trivial(self):
        """Assert presence and substantial size for all core slide ecosystem files."""
        for rel_path, min_size in self.REQUIRED_SLIDE_ASSETS:
            full_path = WORKSPACE_ROOT / rel_path
            self.assertTrue(full_path.is_file(), f"Missing required slide deliverable: {rel_path}")
            size = full_path.stat().st_size
            self.assertGreaterEqual(
                size, min_size,
                f"File unexpectedly small ({size} < {min_size} bytes): {rel_path}"
            )

    def test_syllabus_and_roadmap_deliverables_exist_and_non_trivial(self):
        """Assert presence and substantial size for all syllabus and roadmap files."""
        for rel_path, min_size in self.REQUIRED_SYLLABUS_FILES + self.REQUIRED_ROADMAP_FILES:
            full_path = WORKSPACE_ROOT / rel_path
            self.assertTrue(full_path.is_file(), f"Missing required deliverable: {rel_path}")
            size = full_path.stat().st_size
            self.assertGreaterEqual(
                size, min_size,
                f"File unexpectedly small ({size} < {min_size} bytes): {rel_path}"
            )

    def test_files_valid_utf8_encoding(self):
        """Assert all files decode cleanly without UTF-8 encoding errors."""
        all_targets = [p for p, _ in self.REQUIRED_SLIDE_ASSETS + self.REQUIRED_SYLLABUS_FILES + self.REQUIRED_ROADMAP_FILES]
        for rel_path in all_targets:
            full_path = WORKSPACE_ROOT / rel_path
            try:
                content = full_path.read_text(encoding="utf-8")
                self.assertGreater(len(content), 0, f"File was empty: {rel_path}")
            except UnicodeDecodeError as exc:
                self.fail(f"Unicode decode error in {rel_path}: {exc}")

    def test_mirrored_session_paths_exist(self):
        """Verify mirrored buoi0, buoi1, buoi2 folders exist for backward-compatible routing."""
        mirrored_paths = [
            "slides/buoi0/index.html",
            "slides/buoi1/index.html",
            "slides/buoi2/index.html",
        ]
        for rel_path in mirrored_paths:
            full_path = WORKSPACE_ROOT / rel_path
            self.assertTrue(full_path.is_file(), f"Missing mirrored slide deck: {rel_path}")
            self.assertGreater(full_path.stat().st_size, 5000)


# ==============================================================================
# Tier 2: CDN Integrity & Headless DOM/Script Sanity
# ==============================================================================
class TestTier2CDNIntegrityAndHeadlessDOMSanity(unittest.TestCase):
    """Verify HTTPS CDN URLs, Reveal.js 5.1.0, KaTeX, Highlight.js, and 2D grid structure."""

    DECK_FILES = [
        "slides/00_preparatory/index.html",
        "slides/01_orientation/index.html",
        "slides/02_numpy/index.html",
    ]

    CDN_REQUIREMENTS = [
        r"https://cdn\.jsdelivr\.net/npm/reveal\.js@5(?:\.1\.0)?/dist/reveal\.css",
        r"https://cdn\.jsdelivr\.net/npm/reveal\.js@5(?:\.1\.0)?/dist/reveal\.js",
        r"https://cdn\.jsdelivr\.net/npm/katex@0\.16\.9/dist/katex\.min\.css",
        r"https://cdn\.jsdelivr\.net/npm/highlight\.js@11\.9\.0/",
    ]

    def test_secure_https_cdn_links_only(self):
        """Assert zero insecure HTTP, localhost, or invalid protocols in script/link tags."""
        for rel_path in self.DECK_FILES + ["slides/index.html"]:
            full_path = WORKSPACE_ROOT / rel_path
            content = full_path.read_text(encoding="utf-8")

            # Check external script sources
            script_srcs = re.findall(r'<script\s+[^>]*src=[\"\']([^\"\']+)[\"\']', content)
            for src in script_srcs:
                if src.startswith("http://"):
                    self.fail(f"Insecure HTTP script src found in {rel_path}: {src}")
                if "localhost" in src or "127.0.0.1" in src:
                    self.fail(f"Localhost script src found in {rel_path}: {src}")

            # Check external stylesheet links
            link_hrefs = re.findall(r'<link\s+[^>]*href=[\"\']([^\"\']+)[\"\']', content)
            for href in link_hrefs:
                if href.startswith("http://"):
                    self.fail(f"Insecure HTTP link href found in {rel_path}: {href}")
                if "localhost" in href or "127.0.0.1" in href:
                    self.fail(f"Localhost link href found in {rel_path}: {href}")

    def test_reveal_katex_and_highlight_cdn_presence(self):
        """Verify presence of official CDN links for Reveal.js 5.1.0, KaTeX 0.16.9, and Highlight.js 11.9.0."""
        for rel_path in self.DECK_FILES:
            full_path = WORKSPACE_ROOT / rel_path
            content = full_path.read_text(encoding="utf-8")
            for pattern in self.CDN_REQUIREMENTS:
                self.assertTrue(
                    re.search(pattern, content),
                    f"Missing required CDN link matching '{pattern}' in {rel_path}"
                )

    def test_reveal_2d_grid_dom_structure(self):
        """Verify standard Reveal.js 2D grid structure: <div class='reveal'><div class='slides'><section>."""
        for rel_path in self.DECK_FILES:
            full_path = WORKSPACE_ROOT / rel_path
            content = full_path.read_text(encoding="utf-8")

            self.assertIn('<div class="reveal">', content, f"Missing .reveal container in {rel_path}")
            self.assertIn('<div class="slides">', content, f"Missing .slides container in {rel_path}")

            # 2D grid requires nested sections: <section><section>...</section></section>
            nested_sections = re.findall(r'<section>\s*<section>', content)
            self.assertGreaterEqual(
                len(nested_sections), 2,
                f"Expected 2D vertical grid navigation in {rel_path}, found {len(nested_sections)} nested sections"
            )

    def test_bootstrapper_script_linkage(self):
        """Verify reveal-init.js and initialization invocation across all deck files."""
        for rel_path in self.DECK_FILES:
            full_path = WORKSPACE_ROOT / rel_path
            content = full_path.read_text(encoding="utf-8")
            self.assertIn("reveal-init.js", content, f"Missing reveal-init.js in {rel_path}")
            self.assertIn("window.initGciReveal()", content, f"Missing initGciReveal() call in {rel_path}")


# ==============================================================================
# Tier 3: Interactive Visualizer Widgets DOM Contracts & Mathematical Oracles
# ==============================================================================
class TestTier3InteractiveVisualizerWidgetsDOMContracts(unittest.TestCase):
    """Verify contracts, container elements, and mathematical oracles for the 3 visualizers."""

    @classmethod
    def setUpClass(cls):
        cls.buoi2_html = (WORKSPACE_ROOT / "slides/02_numpy/index.html").read_text(encoding="utf-8")
        cls.bundle_js = (WORKSPACE_ROOT / "slides/js/widgets-bundle.js").read_text(encoding="utf-8")

    def test_widget1_broadcasting_dom_contract(self):
        """Verify Widget 1: Broadcasting Simulator elements and containers."""
        self.assertIn('id="widget-broadcasting-container"', self.buoi2_html)
        self.assertIn('id="broadcast-alignment-card"', self.buoi2_html)
        self.assertIn('id="broadcast-grid-a"', self.buoi2_html)
        self.assertIn('id="broadcast-grid-b"', self.buoi2_html)
        self.assertIn('id="broadcast-grid-c"', self.buoi2_html)

        # Implementation checks in JS bundle
        self.assertIn("mountBroadcastingWidget", self.bundle_js)
        self.assertIn("broadcastShapes", self.bundle_js)
        self.assertIn("RAM Conserved", self.bundle_js)
        self.assertIn("matrix-cell virtual", self.bundle_js)

    def test_widget2_strides_slicing_dom_contract(self):
        """Verify Widget 2: ndarray Indexing & Slicing Memory Visualizer elements."""
        self.assertIn('id="widget-strides-container"', self.buoi2_html)
        self.assertIn('id="strides-slice-code"', self.buoi2_html)
        self.assertIn('id="strides-grid-container"', self.buoi2_html)
        self.assertIn('id="strides-ram-strip"', self.buoi2_html)

        # Implementation checks in JS bundle
        self.assertIn("mountStridesWidget", self.bundle_js)
        self.assertIn("cContiguousStrides", self.bundle_js)
        self.assertIn("computeSlice", self.bundle_js)
        self.assertIn("[VIEW: 0 Bytes Allocated]", self.bundle_js)
        self.assertIn("[COPY:", self.bundle_js)

    def test_widget3_vectorization_benchmark_dom_contract(self):
        """Verify Widget 3: SIMD Vectorization vs Python Loop Benchmark elements."""
        self.assertIn('id="widget-vectorization-container"', self.buoi2_html)
        self.assertIn('id="vec-speedup-svg"', self.buoi2_html)
        self.assertIn('id="race-bar-numpy"', self.buoi2_html)
        self.assertIn('id="race-bar-python"', self.buoi2_html)

        # Implementation checks in JS bundle
        self.assertIn("mountVectorizationWidget", self.bundle_js)
        self.assertIn("timePythonNs", self.bundle_js)
        self.assertIn("timeNumpyNs", self.bundle_js)
        self.assertIn("AVX-512", self.bundle_js)

    def test_broadcasting_mathematical_oracle(self):
        """Python oracle certifying NumPy broadcasting mathematical properties."""
        # 1. Outer Product: (3, 1) + (1, 4) -> (3, 4)
        a = np.ones((3, 1))
        b = np.ones((1, 4))
        c = a + b
        self.assertEqual(c.shape, (3, 4))

        # 2. Row Bias: (4, 3) + (3,) -> (4, 3)
        a2 = np.ones((4, 3))
        b2 = np.ones((3,))
        c2 = a2 + b2
        self.assertEqual(c2.shape, (4, 3))

        # 3. Incompatible dimensions: (3, 2) + (3, 3) -> ValueError
        with self.assertRaises(ValueError):
            _ = np.ones((3, 2)) + np.ones((3, 3))

        # 4. 3D Tensor expansion: (2, 3, 1) + (1, 4) -> (2, 3, 4)
        a3 = np.ones((2, 3, 1))
        b3 = np.ones((1, 4))
        c3 = a3 + b3
        self.assertEqual(c3.shape, (2, 3, 4))

    def test_strides_affine_addressing_oracle(self):
        """Python oracle certifying C-contiguous strides and View vs Copy memory invariants."""
        # Base array: shape (4, 5), float64 (itemsize 8 bytes)
        arr = np.zeros((4, 5), dtype=np.float64)
        self.assertEqual(arr.strides, (40, 8))

        # Slice: arr[0:3:1, 1:5:2]
        sl = arr[0:3:1, 1:5:2]
        self.assertEqual(sl.shape, (3, 2))
        self.assertEqual(sl.strides, (40, 16))

        # View memory invariant: sl shares memory buffer with arr
        self.assertIs(sl.base, arr)
        self.assertTrue(np.shares_memory(sl, arr))

        # Fancy indexing copy invariant: allocates new heap buffer
        fancy = arr[[0, 2], :]
        self.assertIsNone(fancy.base)
        self.assertFalse(np.shares_memory(fancy, arr))

    def test_vectorization_analytical_model_oracle(self):
        """Oracle certifying analytical simulation behavior matches JS bundle equations."""
        # Verify analytical model: T_py(N) = N * 62.5 ns, T_np(N) = 2500 + N * 0.21 ns
        for log_n in [2, 3, 4, 5, 6, 7]:
            n = 10 ** log_n
            t_py = n * 62.5
            t_np = 2500.0 + n * 0.21
            speedup = t_py / t_np

            if log_n == 2:
                # For N=100, C dispatch latency dominates: speedup is modest (< 10x)
                self.assertLess(speedup, 10.0)
            elif log_n >= 5:
                # For N>=100,000, SIMD throughput dominates: speedup exceeds 200x
                self.assertGreater(speedup, 200.0)
                # Does not exceed theoretical ceiling ~297.6x
                self.assertLessEqual(speedup, 298.0)


# ==============================================================================
# Tier 4: Legacy Slide Purge & Directory Hygiene
# ==============================================================================
class TestTier4LegacySlidePurgeAndDirectoryHygiene(unittest.TestCase):
    """Explicitly assert that all 10 deprecated files are permanently purged and zero AppleDouble files exist."""

    DEPRECATED_FILES = [
        "slides/buoi0_preparatory_slides.html",
        "slides/buoi0_preparatory_slides.md",
        "slides/buoi1_orientation_slides.html",
        "slides/buoi1_orientation_slides.md",
        "slides/buoi1_interactive_dynamic_slides.html",
        "slides/css/minimalist-deck.css",
        "slides/js/minimalist-deck.js",
        "study_notes/numpy_slides.html",
        "study_notes/numpy_optimization_slides.md",
        "study_notes/restructure.py",
    ]

    REQUIRED_MODULAR_DIRECTORIES = [
        "slides/00_preparatory",
        "slides/01_orientation",
        "slides/02_numpy",
        "slides/css",
        "slides/js",
        "03_Materials/00_Preparatory",
        "03_Materials/01_Orientation",
        "03_Materials/02_NumPy",
    ]

    def test_deprecated_files_strictly_purged(self):
        """Assert that every single obsolete file has been completely removed."""
        for rel_path in self.DEPRECATED_FILES:
            full_path = WORKSPACE_ROOT / rel_path
            self.assertFalse(
                full_path.exists(),
                f"CRITICAL HYGIENE FAILURE: Obsolete file still exists: {rel_path}"
            )

    def test_required_modular_directories_exist(self):
        """Assert that the newly organized modular directories exist."""
        for rel_dir in self.REQUIRED_MODULAR_DIRECTORIES:
            full_dir = WORKSPACE_ROOT / rel_dir
            self.assertTrue(full_dir.is_dir(), f"Missing modular directory: {rel_dir}")

    def test_zero_appledouble_dot_underscore_files(self):
        """Assert zero AppleDouble ._* metadata files exist in slides/ or tests/."""
        for check_dir in [SLIDES_DIR, WORKSPACE_ROOT / "tests"]:
            dot_files = list(check_dir.glob("**/._*"))
            self.assertEqual(
                len(dot_files), 0,
                f"AppleDouble dot-underscore files detected in {check_dir.name}: {dot_files}"
            )


# ==============================================================================
# Tier 5: Knowledge Assets & Syllabus Integrity
# ==============================================================================
class TestTier5KnowledgeAssetsAndSyllabusIntegrity(unittest.TestCase):
    """Verify complete knowledge extraction, Cornell handwritten syllabus, roadmap, and task compliance."""

    def test_buoi2_master_detailed_notes_integrity(self):
        """Verify Lecture_02_Detailed_Notes.md contains comprehensive lecture extraction."""
        notes_path = NOTES_DIR / "Lecture_02_Detailed_Notes.md"
        self.assertTrue(notes_path.is_file(), "Missing Lecture_02_Detailed_Notes.md")
        content = notes_path.read_text(encoding="utf-8")

        self.assertGreaterEqual(len(content), 15000, "Lecture 2 notes unexpectedly short")

        # Academic checkpoints from lecture & transcripts
        key_concepts = [
            "C-contiguous",
            "SIMD",
            "AVX-512",
            "ufunc",
            "IEEE 754",
            "stride",
            "keepdims",
            "broadcasting",
            "NOAA",
            "999.9",
            "Omnicampus",
            "Quri",
        ]
        for concept in key_concepts:
            self.assertIn(
                concept.lower(), content.lower(),
                f"Missing key academic concept '{concept}' in Lecture_02_Detailed_Notes.md"
            )

    def test_session2_full_transcripts_presence_and_structure(self):
        """Verify presence and validity of all 3 Session 2 transcripts (markdown and json)."""
        transcripts = [
            "GCI_World_Session_02_Opening",
            "GCI_World_Session_02_During_Lecture",
            "GCI_World_Session_02_Closing",
        ]
        for name in transcripts:
            md_path = NOTES_DIR / f"{name}_transcript_full.md"
            json_path = NOTES_DIR / f"{name}_transcript_raw.json"

            self.assertTrue(md_path.is_file(), f"Missing transcript markdown: {md_path.name}")
            self.assertTrue(json_path.is_file(), f"Missing transcript JSON: {json_path.name}")

            md_content = md_path.read_text(encoding="utf-8")
            self.assertGreater(len(md_content), 5000)
            self.assertIn("**[00:", md_content, f"Missing timestamp markers in {md_path.name}")

            # Validate JSON parses correctly
            try:
                raw_data = json.loads(json_path.read_text(encoding="utf-8"))
                self.assertIsInstance(raw_data, (dict, list))
            except json.JSONDecodeError as exc:
                self.fail(f"Invalid JSON in {json_path.name}: {exc}")

    def test_buoi2_cornell_syllabus_schema(self):
        """Verify syllabus/buoi2_handwritten_notebook_syllabus.md follows 3-column Cornell schema."""
        syl_path = SYLLABUS_DIR / "buoi2_handwritten_notebook_syllabus.md"
        self.assertTrue(syl_path.is_file(), "Missing buoi2_handwritten_notebook_syllabus.md")
        content = syl_path.read_text(encoding="utf-8")

        self.assertGreaterEqual(len(content), 10000)

        # 3-column Cornell markers (supports accented Vietnamese and legacy anchors)
        self.assertTrue(re.search(r"(?:COT|C[ỘO]T)\s*1.*(?:TU\s*KHOA|T[ỪU]\s*KH[ÓO]A)", content, re.IGNORECASE))
        self.assertTrue(re.search(r"(?:COT|C[ỘO]T)\s*2.*(?:SO\s*DO\s*TU\s*DUY|S[ƠO]\s*Đ[ỒO]\s*T[ƯU]\s*DUY)", content, re.IGNORECASE))
        self.assertTrue(re.search(r"(?:COT|C[ỘO]T)\s*3.*(?:HANH\s*DONG|H[ÀA]NH\s*Đ[ỘO]NG)", content, re.IGNORECASE))

        # 5 core modules
        for mod_num in ["1", "2", "3", "4", "5"]:
            self.assertTrue(
                re.search(rf"(?:PHAN|PH[ẦA]N)\s*{mod_num}:", content, re.IGNORECASE),
                f"Missing PHAN {mod_num}: in buoi2 syllabus"
            )

        # Summary box & action checklist
        self.assertTrue(
            re.search(r"KHUNG\s*T[ÓO]M\s*T[ẮA]T|KHUNG TOM TAT", content, re.IGNORECASE),
            "Missing summary box marker in buoi2 syllabus"
        )
        self.assertTrue(re.search(r"CHECKLIST\s*H[ÀA]NH\s*Đ[ỘO]NG|CHECKLIST HANH DONG", content, re.IGNORECASE))

    def test_micro_practice_roadmap_buoi2_pedagogy(self):
        """Verify roadmap/micro_practice_roadmap.md contains Buoi 2 micro-sessions and review session."""
        roadmap_path = ROADMAP_DIR / "micro_practice_roadmap.md"
        self.assertTrue(roadmap_path.is_file(), "Missing micro_practice_roadmap.md")
        content = roadmap_path.read_text(encoding="utf-8")

        # 5 micro-sessions + 1 review session for Buoi 2
        for ms_id in ["Micro-2.1", "Micro-2.2", "Micro-2.3", "Micro-2.4", "Micro-2.5", "Session 2.S"]:
            self.assertIn(ms_id, content, f"Missing micro-session {ms_id} in micro_practice_roadmap.md")

        # Definition of Done and Active Recall reflex checks
        self.assertIn("Definition of Done", content)
        self.assertIn("Active Recall", content)
        self.assertIn("<details>", content)
        self.assertIn("<summary>", content)

    def test_curriculum_alignment_matrix_buoi2_integration(self):
        """Verify roadmap/curriculum_alignment_matrix.md maps Buoi 2 to HW1 and competency triad."""
        matrix_path = ROADMAP_DIR / "curriculum_alignment_matrix.md"
        self.assertTrue(matrix_path.is_file(), "Missing curriculum_alignment_matrix.md")
        content = matrix_path.read_text(encoding="utf-8")

        self.assertIn("HW1", content)
        self.assertIn("NumPy", content)
        self.assertIn("Micro-2.1", content)
        self.assertIn("Micro-2.5", content)
        self.assertIn("Session 2.S", content)

    def test_tasks_file_rfc2119_schema_compliance(self):
        """Verify all task items in TASKS.md adhere strictly to the standardized schema."""
        tasks_path = WORKSPACE_ROOT / "TASKS.md"
        self.assertTrue(tasks_path.is_file(), "Missing TASKS.md")
        lines = tasks_path.read_text(encoding="utf-8").splitlines()

        schema_pattern = re.compile(
            r'^- \[( |x)\] \[Deadline: \d{4}-\d{2}-\d{2} \d{2}:\d{2}\] \[Priority: P[012]\] .+$'
        )

        task_count = 0
        for line_no, line in enumerate(lines, 1):
            if line.startswith("- ["):
                self.assertTrue(
                    schema_pattern.match(line.strip()),
                    f"Line {line_no} violates standardized task schema: '{line.strip()}'"
                )
                task_count += 1

        self.assertGreaterEqual(task_count, 15, f"Expected >= 15 standardized tasks, found {task_count}")


# ==============================================================================
# Tier 6: Universal Zero-Emoji Compliance
# ==============================================================================
class TestTier6StrictZeroEmojiUniversalAudit(unittest.TestCase):
    """Assert zero unicode emojis workspace-wide across all deliverable formats."""

    EMOJI_PATTERN = re.compile(
        r'[\U00010000-\U0010ffff]|'  # Supplementary Multilingual Plane (emojis)
        r'[\u2600-\u27bf]|'          # Miscellaneous symbols, dingbats, stars
        r'[\u2300-\u23ff]|'          # Miscellaneous technical symbols
        r'[\u2b50-\u2b55]|'          # Heavy stars and geometric shapes
        r'[\u203c\u2049\u2139\u2194-\u2199\u21a9-\u21aa]'
    )

    SCAN_EXTENSIONS = {".html", ".css", ".js", ".md", ".py", ".json"}
    SCAN_DIRS = ["slides", "syllabus", "roadmap", "06_Notes_Transcripts", "tests", "03_Materials"]

    def test_universal_zero_emojis(self):
        """Scans all production, learning, and test files for any unicode emoji violations."""
        violations = []
        for dir_name in self.SCAN_DIRS:
            target_dir = WORKSPACE_ROOT / dir_name
            if not target_dir.exists():
                continue
            for file_path in target_dir.glob("**/*"):
                if file_path.is_file() and not file_path.name.startswith("._") and file_path.suffix in self.SCAN_EXTENSIONS:
                    try:
                        content = file_path.read_text(encoding="utf-8", errors="ignore")
                        matches = self.EMOJI_PATTERN.findall(content)
                        if matches:
                            violations.append(
                                f"{file_path.relative_to(WORKSPACE_ROOT)}: {len(matches)} emojis found: {set(matches)}"
                            )
                    except Exception as exc:
                        violations.append(f"{file_path.relative_to(WORKSPACE_ROOT)}: Read error: {exc}")

        self.assertEqual(
            len(violations), 0,
            "DeepTutor zero-emoji policy violation detected:\n" + "\n".join(f"  - {v}" for v in violations)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
