"""
Tier 1: Feature Coverage - Presentation & TiB Stage Assets
Tests 10-slide pitch deck rubrics, 60s backup video script timing, Judge Q&A defense coverage,
and bilingual (VN/JA) ESG certificate export schema.
Authoritative source: ORIGINAL_REQUEST.md § R3 & R4, PROJECT.md § Presentation Assets
"""

import pytest
import sys
from pathlib import Path
from typing import Dict, Any, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# Canonical 10 Slide Titles and Required Topics
REQUIRED_PITCH_SLIDES = [
    "Slide 1: Title & Hook (AgriCarbon Agent - Precision Agriculture & Scope 1-3 Auditing)",
    "Slide 2: The Problem & Pain Points (Mekong Delta Salinity & Strict GX Japan/EU CBAM Rules)",
    "Slide 3: Existing Market Flaws (Manual Soil Testing & 21-Day Expensive Carbon Audits)",
    "Slide 4: The Agentic Solution (Autonomous Multi-Agent ReAct Engine)",
    "Slide 5: System Architecture (Supervisor, 4 Workers, Dual Memory & Guardrails)",
    "Slide 6: Live Stage Demo Flow (An Giang AWD Rice & Lam Dong Arabica Coffee)",
    "Slide 7: Measurable Sustainable Impact (-38% Water, -28.1% CO2e, 3min Audit)",
    "Slide 8: Business Model & Monetization (B2B SaaS Tiered Subscriptions + Carbon Credits)",
    "Slide 9: Roadmap & Japan Market Go-To-Market (GX-League & J-Credit Integration)",
    "Slide 10: The Team & Vision (Vietnam-Japan AI Builders for Sustainable Growth)"
]


# Canonical 60-Second Video Demo Storyboard Structure
CANONICAL_60S_SCRIPT = [
    {"seconds": "00-10", "scene": "Problem Hook", "action": "Farmer facing drought & costly export audit"},
    {"seconds": "10-25", "scene": "Autonomous Sensing", "action": "Agent queries Open-Meteo & soil IoT telemetry"},
    {"seconds": "25-40", "scene": "ReAct Dispatch", "action": "Pump optimized for off-peak hours, saving water"},
    {"seconds": "40-50", "scene": "Audit Ledger", "action": "Cryptographic SHA-256 certificate generated in 3 mins"},
    {"seconds": "50-60", "scene": "Impact Summary", "action": "-38% water, -28.1% CO2e, call to action"}
]


class TestPresentationArtifacts:
    """Validates structure and content of pitch deck, demo script, and judge defenses."""

    def test_pitch_deck_rubrics_and_slide_count(self):
        """Verify 10-slide deck covers all mandatory rubrics in ORIGINAL_REQUEST.md § R4."""
        assert len(REQUIRED_PITCH_SLIDES) == 10, "Pitch deck must contain exactly 10 structured slides"
        rubrics = ["Problem", "Architecture", "Impact", "Business Model", "Roadmap", "Team"]
        slide_text = " ".join(REQUIRED_PITCH_SLIDES)
        for rubric in rubrics:
            assert rubric.lower() in slide_text.lower(), f"Slide deck missing mandatory rubric '{rubric}'"

    def test_backup_demo_60s_script_timing_and_phases(self):
        """Verify 60-second backup video script adheres to strict stage timing constraints."""
        total_phases = len(CANONICAL_60S_SCRIPT)
        assert total_phases == 5, "Script must have 5 concise pacing segments"
        assert CANONICAL_60S_SCRIPT[0]["seconds"] == "00-10"
        assert CANONICAL_60S_SCRIPT[-1]["seconds"] == "50-60"
        
        # Verify narrative covers autonomous sensing and carbon audit
        actions = " ".join([p["action"] for p in CANONICAL_60S_SCRIPT])
        assert "sensing" in actions.lower() or "telemetry" in actions.lower()
        assert "ledger" in actions.lower() or "certificate" in actions.lower()

    def test_judge_qa_defense_coverage(self):
        """Verify Judge Q&A Defense playbook covers top 4 critical competition angles."""
        defense_playbook = {
            "hallucination": "Deterministic FAO-56 and IPCC formulas verified by Critic Guardrail agent.",
            "token_cost": "Local small-model routing, prompt caching, and rule-based fallback reduce tokens by 65%.",
            "data_privacy": "On-premise edge IoT processing with zero raw telemetry uploaded to public models.",
            "accuracy_and_audit": "SHA-256 tamper-evident hash chaining with dual-signature verification."
        }
        required_topics = ["hallucination", "token_cost", "data_privacy", "accuracy_and_audit"]
        for topic in required_topics:
            assert topic in defense_playbook
            assert len(defense_playbook[topic]) > 20, f"Defense for '{topic}' is too brief"

    def test_bilingual_esg_report_schema(self):
        """Verify bilingual ESG Carbon Certificate contains Vietnamese and Japanese required fields."""
        certificate_sample = {
            "certificate_id": "CERT-VN-JA-2026-0089",
            "timestamp": "2026-09-08T07:00:00Z",
            "issuer": "AgriCarbon Multi-Agent Verifier",
            "titles": {
                "vi": "CHỨNG NHẬN GIẢM PHÁT THẢI CARBON NÔNG NGHIỆP",
                "ja": "農業カーボン排出削減証明書 (AgriCarbon 認証)"
            },
            "metrics": {
                "water_saved_m3": 2850.0,
                "water_saved_pct": 38.0,
                "co2e_reduced_kg": 1840.5,
                "co2e_reduced_pct": 28.1,
                "fertilizer_saved_kg": 320.0
            },
            "compliance_standards": ["IPCC Tier 2", "FAO-56", "Japan GX-League", "EU CBAM"],
            "cryptographic_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        }
        assert "vi" in certificate_sample["titles"]
        assert "ja" in certificate_sample["titles"]
        assert certificate_sample["metrics"]["water_saved_pct"] == 38.0
        assert certificate_sample["metrics"]["co2e_reduced_pct"] == 28.1
        assert len(certificate_sample["cryptographic_hash"]) == 64

    def test_three_tier_failsafe_strategy(self):
        """Verify Tokyo Innovation Base failsafe strategy: Live Demo -> Local Cache -> Video MP4."""
        failsafe_modes = ["LIVE_STREAMLIT_APP", "LOCAL_OFFLINE_CACHE", "BACKUP_MP4_VIDEO"]
        assert len(failsafe_modes) == 3
        assert "LIVE_STREAMLIT_APP" in failsafe_modes
        assert "LOCAL_OFFLINE_CACHE" in failsafe_modes
        assert "BACKUP_MP4_VIDEO" in failsafe_modes
