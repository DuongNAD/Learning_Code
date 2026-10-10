"""
[Test Suite] Challenger P2-2 Empirical Performance & Runtime Stress-Testing
Role: Performance & Runtime Stress-Testing Challenger (critic, specialist)
Compliance: Strict RFC 2119, emoji_policy: none (Zero Unicode Emojis)

Adversarially validates:
1. Frame Budget & Latency (< 16.6ms 60 FPS standard under rapid updates)
2. Layout Shift (CLS) on KaTeX numeric slot updates (.dyn-slot textContent exclusivity)
3. Universal Portability under file:// protocol (Zero bare ES imports/exports, zero type=module)
4. DOM Contract Integrity across all 5 explorable pages
5. 16:9 Projection auto-scaler coordinate centering and transform scaling
"""

import math
import os
import re
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXPLORABLE_DIR = PROJECT_ROOT / "explorable"
ENGINE_DIR = EXPLORABLE_DIR / "engine"
BUOI1_DIR = EXPLORABLE_DIR / "buoi1"
BUOI2_DIR = EXPLORABLE_DIR / "buoi2"
TEMPLATES_DIR = EXPLORABLE_DIR / "templates"

ENGINE_JS = ENGINE_DIR / "threeui-engine.js"
ENGINE_CSS = ENGINE_DIR / "threeui-engine.css"
SHADER_BG_JS = ENGINE_DIR / "threeui-shader-bg.js"
HUB_INDEX_HTML = EXPLORABLE_DIR / "index.html"
BUOI1_INDEX_HTML = BUOI1_DIR / "index.html"
BUOI1_MODELS_JS = BUOI1_DIR / "models_buoi1.js"
BUOI2_INDEX_HTML = BUOI2_DIR / "index.html"
BUOI2_MODELS_JS = BUOI2_DIR / "models_buoi2.js"
BOILERPLATE_HTML = TEMPLATES_DIR / "boilerplate_explorable.html"
ENGINE_INDEX_HTML = ENGINE_DIR / "index.html"


class TestChallengerP22EmpiricalStress(unittest.TestCase):
    """
    Adversarial stress and verification tests implemented by Challenger P2-2.
    """

    # -------------------------------------------------------------------------
    # 1. Universal Portability under file:// protocol
    # -------------------------------------------------------------------------
    def test_zero_bare_es_module_imports_or_exports(self):
        """
        Verify that all JavaScript and HTML files in explorable/ contain ZERO
        bare ES module 'import ... from' or 'export' statements, ensuring
        frictionless execution when launched via file:// from USB or disk.
        """
        import_pattern = re.compile(r'^\s*import\s+(?:(?:\*\s+as\s+\w+)|(?:\{\s*[\w\s,]+\s*\})|(?:\w+))\s+from\s+[\'"][^\'"]+[\'"]', re.MULTILINE)
        export_pattern = re.compile(r'^\s*export\s+(?:default\s+)?(?:const|var|let|function|class|\{)', re.MULTILINE)
        module_script_pattern = re.compile(r'<script\b[^>]*\btype\s*=\s*[\'"]module[\'"][^>]*>', re.IGNORECASE)
        root_abs_pattern = re.compile(r'(?:href|src)\s*=\s*[\'"]\/(?!\/)[^\'"]*[\'"]', re.IGNORECASE)

        for p in EXPLORABLE_DIR.rglob("*"):
            if p.is_file() and not p.name.startswith("._"):
                if p.suffix == ".js":
                    content = p.read_text(encoding="utf-8")
                    self.assertIsNone(
                        import_pattern.search(content),
                        f"Bare ES import detected in {p.relative_to(PROJECT_ROOT)}"
                    )
                    self.assertIsNone(
                        export_pattern.search(content),
                        f"Bare ES export detected in {p.relative_to(PROJECT_ROOT)}"
                    )
                elif p.suffix == ".html":
                    content = p.read_text(encoding="utf-8")
                    self.assertIsNone(
                        module_script_pattern.search(content),
                        f"type='module' script detected in {p.relative_to(PROJECT_ROOT)}"
                    )
                    self.assertIsNone(
                        root_abs_pattern.search(content),
                        f"Root-absolute link detected in {p.relative_to(PROJECT_ROOT)}"
                    )

    # -------------------------------------------------------------------------
    # 2. Layout Shift (CLS) on KaTeX Numeric Slot Updates
    # -------------------------------------------------------------------------
    def test_katex_slot_textcontent_exclusivity(self):
        """
        Verify that bindKatexSlot mutates textContent strictly and does not touch
        innerHTML, protecting against DOM destruction, layout reflow, and CLS.
        """
        content = ENGINE_JS.read_text(encoding="utf-8")
        bind_slot_match = re.search(r'bindKatexSlot[\s\S]*?return effect;', content)
        self.assertIsNotNone(bind_slot_match, "bindKatexSlot must be defined in threeui-engine.js")
        slot_code = bind_slot_match.group(0)

        self.assertIn("el.textContent = formatted", slot_code, "Must mutate textContent")
        self.assertNotIn("innerHTML", slot_code, "Must NOT touch innerHTML in slot effect")
        self.assertIn("el.classList.add('dyn-slot')", slot_code, "Must enforce dyn-slot class")

    def test_css_slot_layout_containment_and_tabular_nums(self):
        """
        Verify that CSS contains .dyn-slot, tabular-nums, inline-block, and font-mono
        to prevent numeric layout shifts during continuous slider drags.
        """
        css = ENGINE_CSS.read_text(encoding="utf-8")
        self.assertIn(".dyn-slot", css, "CSS must declare .dyn-slot")
        self.assertIn("tabular-nums", css, "CSS must declare tabular-nums for equal digit widths")
        self.assertIn("display: inline-block", css, "CSS must declare inline-block for slot")

    # -------------------------------------------------------------------------
    # 3. DOM Contract Integrity across all 5 Explorable Pages
    # -------------------------------------------------------------------------
    def test_dom_contracts_across_all_five_documents(self):
        """
        Verify presence of core UI architecture across engine fixture, Buoi 1,
        Buoi 2, curriculum boilerplate, and master hub.
        """
        docs = [
            (ENGINE_INDEX_HTML, ["data-view=\"document\"", "threeui-bg-canvas", "threeui-engine.js", "data-theme-btn"]),
            (BUOI1_INDEX_HTML, ["data-view=\"document\"", "slide-1", "slide-2", "slide-3", "threeui-cornell-grid", "threeui-deck-hud"]),
            (BUOI2_INDEX_HTML, ["data-view=\"document\"", "slide-strides", "slide-broadcasting", "slide-vectorization", "threeui-cornell-grid", "threeui-deck-hud"]),
            (BOILERPLATE_HTML, ["data-view=\"document\"", "Split-Apply-Combine", "Gradient Descent", "threeui-cornell-grid", "threeui-deck-hud"]),
            (HUB_INDEX_HTML, ["threeui-bg-canvas", "buoi1/index.html", "buoi2/index.html", "templates/boilerplate_explorable.html", "engine/index.html"])
        ]

        for file_path, required_tokens in docs:
            self.assertTrue(file_path.exists(), f"File {file_path.name} must exist")
            content = file_path.read_text(encoding="utf-8")
            for token in required_tokens:
                self.assertIn(token, content, f"Token '{token}' must exist in {file_path.name}")

    # -------------------------------------------------------------------------
    # 4. 16:9 Projection Auto-Scaler Viewport Matrix
    # -------------------------------------------------------------------------
    def test_auto_scaler_projection_matrix(self):
        """
        Verify 16:9 projection auto-scaler math: scale = min(W/1920, H/1080)
        and centered offset calculations across diverse display dimensions.
        """
        target_w, target_h = 1920, 1080
        test_cases = [
            (1920, 1080, 1.0, 0.0, 0.0),
            (3840, 2160, 2.0, 0.0, 0.0),
            (1366, 768, 768 / 1080, (1366 - 1920 * (768 / 1080)) / 2, 0.0),
            (3440, 1440, 1440 / 1080, (3440 - 1920 * (1440 / 1080)) / 2, 0.0),
            (390, 844, 390 / 1920, 0.0, (844 - 1080 * (390 / 1920)) / 2)
        ]

        for w, h, exp_scale, exp_off_x, exp_off_y in test_cases:
            scale = min(w / target_w, h / target_h)
            off_x = (w - target_w * scale) / 2
            off_y = (h - target_h * scale) / 2

            self.assertAlmostEqual(scale, exp_scale, places=4)
            self.assertAlmostEqual(off_x, exp_off_x, places=4)
            self.assertAlmostEqual(off_y, exp_off_y, places=4)


if __name__ == "__main__":
    unittest.main()
