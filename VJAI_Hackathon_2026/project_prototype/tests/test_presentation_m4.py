"""
Milestone 4 Unit Tests — TiB Tokyo Pitch Deck & Presentation Assets
Authoritative reference: ORIGINAL_REQUEST.md § R3 & R4, PROJECT.md § Milestone 4
Validates:
1. Physical existence of all 4 presentation files.
2. 10-slide completeness and structure in pitch_deck.md.
3. Rigorous quantitative metrics assertions (-38% water, -28.1% CO2e, -30.5% fertilizer, $0.028/run).
4. HTML renderability, self-contained assets, and interactive controls in pitch_deck.html.
5. 60-second backup demo 3-tier strategy and bilingual second-by-second script.
6. Judge Q&A defense coverage of 4 classic TiB judge questions with 30s punchlines.
"""

import os
import re
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PRESENTATION_DIR = PROJECT_ROOT / "presentation"


class TestPresentationMilestone4:
    """Comprehensive test suite for Milestone 4 presentation deliverables."""

    def test_presentation_files_exist_and_non_empty(self):
        """Verify all 4 required presentation assets exist and have substantive content."""
        expected_files = [
            PRESENTATION_DIR / "pitch_deck.md",
            PRESENTATION_DIR / "pitch_deck.html",
            PRESENTATION_DIR / "backup_demo_60s.md",
            PRESENTATION_DIR / "judge_qa_defense.md",
        ]
        for fpath in expected_files:
            assert fpath.exists(), f"Missing required presentation file: {fpath.name}"
            assert fpath.is_file(), f"Expected a file, got directory: {fpath.name}"
            content = fpath.read_text(encoding="utf-8")
            assert len(content.strip()) > 500, f"File {fpath.name} is unexpectedly short ({len(content)} chars)"

    def test_pitch_deck_md_10_slides_completeness(self):
        """Verify pitch_deck.md contains exactly 10 distinct, structured slides covering all rubrics."""
        deck_path = PRESENTATION_DIR / "pitch_deck.md"
        content = deck_path.read_text(encoding="utf-8")

        # Verify all 10 slide headers are explicitly declared
        slide_headers = re.findall(r"^##\s+Slide\s+(\d+):", content, flags=re.MULTILINE)
        slide_indices = [int(num) for num in slide_headers]
        assert len(slide_indices) == 10, f"Expected exactly 10 slide headers, found {len(slide_indices)}"
        assert slide_indices == list(range(1, 11)), f"Slide numbering must be contiguous 1..10, got {slide_indices}"

        # Verify all mandatory rubrics are covered
        required_topics = [
            ("Slide 1", ["cover", "title", "hook"]),
            ("Slide 2", ["real problem", "crisis", "salinity"]),
            ("Slide 3", ["existing flaws", "legacy", "greenwashing"]),
            ("Slide 4", ["agentic solution", "react", "closed-loop"]),
            ("Slide 5", ["system architecture", "supervisor", "memory"]),
            ("Slide 6", ["live demo", "flow", "preset"]),
            ("Slide 7", ["measurable impact", "water", "co2e"]),
            ("Slide 8", ["business model", "unit economics"]),
            ("Slide 9", ["roadmap", "phases"]),
            ("Slide 10", ["team", "call to action"]),
        ]

        content_lower = content.lower()
        for slide_label, keywords in required_topics:
            matched = any(kw in content_lower for kw in keywords)
            assert matched, f"Pitch deck does not sufficiently cover rubric '{keywords}' for {slide_label}"

    def test_pitch_deck_md_quantitative_metrics(self):
        """Verify strict adherence to hackathon quantitative impact metrics and unit economics."""
        deck_path = PRESENTATION_DIR / "pitch_deck.md"
        content = deck_path.read_text(encoding="utf-8")

        # 1. Water savings metric (-38% or -38.0%)
        assert re.search(r"-38(\.0)?%", content), "Pitch deck missing -38% water savings metric"

        # 2. CO2e emissions reduction metric (-28.1%)
        assert "-28.1%" in content, "Pitch deck missing -28.1% CO2e reduction metric"

        # 3. Chemical fertilizer reduction metric (-30.5%)
        assert "-30.5%" in content, "Pitch deck missing -30.5% fertilizer reduction metric"

        # 4. Unit economics ($0.028 / run)
        assert "$0.028" in content, "Pitch deck missing $0.028/run unit cost"

        # 5. Audit speed comparison (3 minutes vs 21 days)
        assert "3 minute" in content.lower() or "3 min" in content.lower(), "Missing 3 min audit claim"
        assert "21 day" in content.lower() or "21-day" in content.lower(), "Missing 21 days baseline audit claim"

        # 6. Four-phase roadmap
        assert "Phase 1" in content
        assert "Phase 2" in content
        assert "Phase 3" in content
        assert "Phase 4" in content

    def test_pitch_deck_html_renderability_and_interactivity(self):
        """Verify pitch_deck.html is self-contained, interactive, and contains all 10 slide views."""
        html_path = PRESENTATION_DIR / "pitch_deck.html"
        html_content = html_path.read_text(encoding="utf-8")

        # HTML5 validity & structural anchors
        assert "<!DOCTYPE html>" in html_content
        assert "<html" in html_content
        assert "<head>" in html_content
        assert "<body>" in html_content
        assert "<style>" in html_content
        assert "<script>" in html_content

        # Verify all 10 slide containers exist in the DOM
        for i in range(1, 11):
            assert f'id="slide-{i}"' in html_content, f"Missing HTML container id='slide-{i}'"

        # Verify interactive UI controls
        assert 'id="prev-btn"' in html_content, "Missing previous slide button"
        assert 'id="next-btn"' in html_content, "Missing next slide button"
        assert 'id="speaker-notes-drawer"' in html_content, "Missing speaker notes container"
        assert 'id="progress-bar"' in html_content, "Missing progress bar"

        # Verify keyboard event listener support
        assert "ArrowRight" in html_content
        assert "ArrowLeft" in html_content

        # Verify self-contained requirement (no unpinned external CDN scripts)
        assert '<script src="http' not in html_content, "HTML presentation must be self-contained for offline stage use"

        # Verify key impact metrics rendered in HTML
        assert "-38.0%" in html_content or "-38%" in html_content
        assert "-28.1%" in html_content
        assert "-30.5%" in html_content
        assert "$0.028" in html_content

    def test_backup_demo_60s_three_tier_and_timeline(self):
        """Verify backup_demo_60s.md contains 3-tier strategy and exact second-by-second bilingual script."""
        demo_path = PRESENTATION_DIR / "backup_demo_60s.md"
        content = demo_path.read_text(encoding="utf-8")

        # 3-tier strategy modes
        assert "LIVE_STREAMLIT_APP" in content
        assert "LOCAL_OFFLINE_CACHE" in content
        assert "BACKUP_MP4_VIDEO" in content

        # Second-by-second timeline checkpoints
        timeline_checkpoints = ["00:00", "00:10", "00:25", "00:40", "00:50", "01:00"]
        for ts in timeline_checkpoints:
            assert ts in content, f"Backup demo script missing timeline anchor '{ts}'"

        # Bilingual English and Japanese script components
        assert "Mekong" in content
        assert "GX-League" in content
        assert "メコンデルタ" in content or "農業" in content or "審査員" in content
        assert "2.8" in content or "0.028" in content

    def test_judge_qa_defense_four_questions_and_standards(self):
        """Verify judge_qa_defense.md provides 30s punchlines and technical proofs for all 4 classic questions."""
        qa_path = PRESENTATION_DIR / "judge_qa_defense.md"
        content = qa_path.read_text(encoding="utf-8")

        # 4 required topics
        assert "Hallucination" in content or "Crop Safety" in content
        assert "Token Cost" in content or "Economic Feasibility" in content
        assert "Data Privacy" in content or "Sovereign" in content
        assert "Legal Accountability" in content or "Greenwashing" in content

        # 30-second punchlines structure
        assert "30-Second Stage Punchline" in content
        assert content.count("30-Second Stage Punchline") >= 4

        # Japanese key talking points
        assert "日本語の要点" in content or "Japanese Key Talking Point" in content
        assert content.count("日本語の要点") >= 4

        # Technical verification standards
        assert "FAO-56" in content or "FAO" in content
        assert "IPCC" in content
        assert "SHA-256" in content
        assert "$0.028" in content
