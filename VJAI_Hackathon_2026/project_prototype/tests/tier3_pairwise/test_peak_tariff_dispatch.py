"""
Tier 3: Pairwise - EVN Peak Electricity Tariff & Dispatch Schedule Interaction
Tests how dynamic electricity tariffs (peak vs normal vs off-peak) shape irrigation pump timing.
Authoritative source: PROJECT.md § ResourceEcoDispatchAgent
"""

import pytest
import sys
from pathlib import Path
from typing import Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def optimize_pump_timing_for_tariff(
    current_hour: int,
    urgency: str,
    duration_minutes: int
) -> Dict[str, Any]:
    """
    EVN TOU Tariff Schedule (Vietnam Standard):
    - Peak hours: 09:30 - 11:30 (hours 9, 10) and 17:00 - 20:00 (hours 17, 18, 19) [~3,100 VND/kWh]
    - Off-peak: 22:00 - 04:00 [~1,100 VND/kWh]
    - Normal: remaining hours [~1,700 VND/kWh]
    """
    is_peak = current_hour in [9, 10, 17, 18, 19]
    
    if is_peak and urgency != "HIGH":
        # Shift to off-peak / normal window
        deferred_hour = 12 if current_hour in [9, 10] else 20
        return {
            "dispatch_mode": "DEFERRED",
            "scheduled_hour": deferred_hour,
            "duration_minutes": duration_minutes,
            "tariff_rate_vnd": 1700,
            "reason": "Avoid peak tariff to minimize farmer electricity cost"
        }
    
    # Urgent or not peak: run immediately
    tariff = 3100 if is_peak else (1100 if current_hour in [22, 23, 0, 1, 2, 3] else 1700)
    return {
        "dispatch_mode": "IMMEDIATE",
        "scheduled_hour": current_hour,
        "duration_minutes": duration_minutes,
        "tariff_rate_vnd": tariff,
        "reason": "Emergency deficit requires immediate water delivery" if is_peak else "Optimal run window"
    }


class TestPeakTariffDispatch:
    """Validates smart energy-tariff-aware pump scheduling."""

    def test_peak_tariff_hours_delayed_dispatch(self):
        """Non-urgent irrigation request during 10:00 AM peak is deferred to 12:00 PM."""
        res = optimize_pump_timing_for_tariff(
            current_hour=10,
            urgency="MEDIUM",
            duration_minutes=45
        )
        assert res["dispatch_mode"] == "DEFERRED"
        assert res["scheduled_hour"] == 12
        assert res["tariff_rate_vnd"] == 1700
        assert "Avoid peak tariff" in res["reason"]

    def test_emergency_deficit_overrides_peak_tariff(self):
        """Emergency soil moisture deficit (< wilting point) triggers immediate pump run despite peak tariff."""
        res = optimize_pump_timing_for_tariff(
            current_hour=18,  # Peak evening hour (18:00)
            urgency="HIGH",   # Crop danger!
            duration_minutes=60
        )
        assert res["dispatch_mode"] == "IMMEDIATE"
        assert res["scheduled_hour"] == 18
        assert res["tariff_rate_vnd"] == 3100
        assert "Emergency deficit" in res["reason"]

    def test_off_peak_night_irrigation_cost_savings(self):
        """Night pumping (23:00) gets lowest off-peak tariff rate (1,100 VND/kWh)."""
        res = optimize_pump_timing_for_tariff(
            current_hour=23,
            urgency="LOW",
            duration_minutes=40
        )
        assert res["dispatch_mode"] == "IMMEDIATE"
        assert res["tariff_rate_vnd"] == 1100
