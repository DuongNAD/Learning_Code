"""
Test suite for Time & Deadline Sentinel Protocol and pick_today.py enhancements.
Validates countdown computation, deadline parsing, automatic priority override,
deduplication, and screenshot ground truth verification.
Zero emoji policy strictly enforced.
"""

import sys
import re
from pathlib import Path
from datetime import datetime, timedelta
import pytest

WORKSPACE_ROOT = Path("D:/02_Learning_Knowledge")
sys.path.insert(0, str(WORKSPACE_ROOT))

import pick_today

def test_parse_deadline_datetime_formats():
    """Verify datetime parsing across supported formats."""
    # Standard YYYY-MM-DD HH:mm
    dt1 = pick_today.parse_deadline_datetime("2026-09-24 19:00")
    assert dt1 == datetime(2026, 9, 24, 19, 0)

    # Date only YYYY-MM-DD (defaults to end of day 23:59:59)
    dt2 = pick_today.parse_deadline_datetime("2026-09-24")
    assert dt2 == datetime(2026, 9, 24, 23, 59, 59)

    # ISO format YYYY-MM-DDTHH:mm
    dt3 = pick_today.parse_deadline_datetime("2026-10-08T18:00")
    assert dt3 == datetime(2026, 10, 8, 18, 0)

    # Empty / None
    assert pick_today.parse_deadline_datetime("") is None
    assert pick_today.parse_deadline_datetime(None) is None
    assert pick_today.parse_deadline_datetime("invalid-date") is None

def test_compute_countdown_categories():
    """Verify countdown calculation and categorization."""
    base_now = datetime(2026, 9, 23, 1, 0, 0)

    # 1. Completed task
    cd, rh, cat = pick_today.compute_countdown(base_now + timedelta(hours=10), is_completed=True, now=base_now)
    assert cd == "[COMPLETED]"
    assert cat == "completed"
    assert rh is None

    # 2. Overdue task (past deadline)
    overdue_dt = base_now - timedelta(hours=3, minutes=15)
    cd, rh, cat = pick_today.compute_countdown(overdue_dt, is_completed=False, now=base_now)
    assert "[OVERDUE:" in cd
    assert cat == "overdue"
    assert rh < 0

    # 3. Critical task (< 24 hours)
    crit_dt = base_now + timedelta(hours=14, minutes=30)
    cd, rh, cat = pick_today.compute_countdown(crit_dt, is_completed=False, now=base_now)
    assert "[D-0:" in cd
    assert "14h" in cd
    assert cat == "critical"

    # 4. Approaching task (24h to 48h) e.g. D-1 18h remaining
    app_dt = base_now + timedelta(days=1, hours=18)
    cd, rh, cat = pick_today.compute_countdown(app_dt, is_completed=False, now=base_now)
    assert cd == "[D-1: 18h remaining]"
    assert cat == "approaching"

    # 5. Heads-up task (48h to 72h)
    heads_dt = base_now + timedelta(hours=60)
    cd, rh, cat = pick_today.compute_countdown(heads_dt, is_completed=False, now=base_now)
    assert "[D-2:" in cd
    assert cat == "heads_up"

    # 6. Upcoming task (> 72h)
    up_dt = base_now + timedelta(days=15, hours=8)
    cd, rh, cat = pick_today.compute_countdown(up_dt, is_completed=False, now=base_now)
    assert cd == "[D-15: 8h remaining]"
    assert cat == "upcoming"

def test_parse_task_line():
    """Verify task string parsing into structured dictionary."""
    line1 = "- [ ] [Deadline: 2026-09-24 19:00] [Priority: P0] Chuẩn bị nội dung Buổi 2"
    t1 = pick_today.parse_task_line(line1, "Test")
    assert t1 is not None
    assert t1["is_completed"] is False
    assert t1["deadline_str"] == "2026-09-24 19:00"
    assert t1["priority"] == "P0"
    assert t1["description"] == "Chuẩn bị nội dung Buổi 2"

    # Completed task
    line2 = "- [x] [Deadline: 2026-10-08 18:00] [Priority: P0] Làm Khảo sát điểm danh Buổi 1 (Status: OK)"
    t2 = pick_today.parse_task_line(line2, "GCI")
    assert t2 is not None
    assert t2["is_completed"] is True
    assert t2["countdown_str"] == "[COMPLETED]"

    # Untagged priority defaults to P2
    line3 = "- [ ] Task without tags"
    t3 = pick_today.parse_task_line(line3, "Test")
    assert t3 is not None
    assert t3["priority"] == "P2"
    assert t3["deadline_str"] is None
    assert t3["countdown_str"] == "[NO DEADLINE]"

def test_gci_screenshot_ground_truth():
    """Verify Ground Truth from GCI Portal screenshot in GCI TASKS.md."""
    gci_tasks_file = WORKSPACE_ROOT / "GCI_World_2026_September" / "TASKS.md"
    assert gci_tasks_file.exists()
    content = gci_tasks_file.read_text(encoding="utf-8")

    # 1. Attendance Survey Session 1 marked completed with 2026-10-08 18:00
    assert re.search(r"-\s*\[x\]\s*\[Deadline:\s*2026-10-08 18:00\].*?Khảo sát điểm danh Buổi 1.*?Status:\s*OK", content, re.IGNORECASE)

    # 2. Homework HW1 for Session 2 marked completed with 3/3 pts and 2026-10-08 18:00
    assert re.search(r"-\s*\[x\]\s*\[Deadline:\s*2026-10-08 18:00\].*?HW1 for Session2.*?3/3", content, re.IGNORECASE)

    # 3. Session 2 date 2026-09-24 noted
    assert re.search(r"2026-09-24", content)

def test_sentinel_override_activation():
    """Verify approaching tasks (< 48 hours) trigger priority override for GCI World 2026."""
    goal_data, projects = pick_today.parse_active_learning(WORKSPACE_ROOT / "ACTIVE_LEARNING.md")
    # Current time on system is 2026-09-23 early morning; Session 2 deadline is 2026-09-24 19:00 (< 48 hours)
    now = datetime.now()
    tasks = pick_today.collect_all_tasks(WORKSPACE_ROOT / "ACTIVE_LEARNING.md", projects, now)

    urgent_tasks = [
        t for t in tasks
        if not t["is_completed"] and t["remaining_hours"] is not None and t["remaining_hours"] < 48.0
    ]
    assert len(urgent_tasks) > 0, "Expected urgent tasks due within 48h to be detected"

    first_urgent = urgent_tasks[0]
    matched = pick_today.match_task_to_project(first_urgent, projects)
    assert matched is not None
    assert "GCI World" in matched["title"]

def test_sentinel_protocol_documented_in_directives():
    """Verify Time & Deadline Sentinel Protocol is documented in GEMINI.md, AGENTS.md, and D:/GEMINI.md."""
    for filename in ["GEMINI.md", "AGENTS.md"]:
        fpath = WORKSPACE_ROOT / filename
        content = fpath.read_text(encoding="utf-8")
        assert "Time & Deadline Sentinel Protocol" in content
        assert "System Clock Awareness" in content
        assert "Overdue" in content
        assert "Due within 24 Hours" in content
        assert "Due within 3 Days" in content
        assert "Automated Priority Override" in content

    root_gemini = Path("D:/GEMINI.md")
    assert root_gemini.exists()
    root_content = root_gemini.read_text(encoding="utf-8")
    assert "Time & Deadline Sentinel Protocol" in root_content

def test_parse_deadline_datetime_slash_and_edge_formats():
    """Verify datetime parsing across slash formats (portal screenshot) and edge cases."""
    # Slash format with time: 2026/10/08 18:00 (exact portal screenshot format)
    dt1 = pick_today.parse_deadline_datetime("2026/10/08 18:00")
    assert dt1 == datetime(2026, 10, 8, 18, 0)

    # Slash date-only: 2026/10/08
    dt2 = pick_today.parse_deadline_datetime("2026/10/08")
    assert dt2 == datetime(2026, 10, 8, 23, 59, 59)

    # With seconds
    dt3 = pick_today.parse_deadline_datetime("2026-10-08 18:00:00")
    assert dt3 == datetime(2026, 10, 8, 18, 0, 0)

def test_clean_task_text_preserves_identifiers():
    """Verify markdown cleaner removes links, bold, backticks but preserves identifiers and filenames."""
    raw = "Khởi chạy [launch_hub.py](file:///D:/02_Learning_Knowledge/Python_Master/launch_hub.py) và `01_Regression`"
    cleaned = pick_today.clean_task_text(raw)
    assert cleaned == "Khởi chạy launch_hub.py và 01_Regression"
    assert "file:///" not in cleaned

def test_task_urgency_sort_key_priority_precedence():
    """Verify task urgency sort key enforces P0 > P1 > P2 within urgency tiers."""
    now = datetime(2026, 9, 23, 1, 0, 0)

    # Overdue P0 vs Overdue P2
    overdue_p0 = {
        "category": "overdue",
        "priority": "P0",
        "remaining_hours": -1.0,
    }
    overdue_p2 = {
        "category": "overdue",
        "priority": "P2",
        "remaining_hours": -48.0,
    }
    assert pick_today.task_urgency_sort_key(overdue_p0) < pick_today.task_urgency_sort_key(overdue_p2)

    # Critical P0 due in 15h vs Critical P1 due in 10h
    crit_p0 = {
        "category": "critical",
        "priority": "P0",
        "remaining_hours": 15.0,
    }
    crit_p1 = {
        "category": "critical",
        "priority": "P1",
        "remaining_hours": 10.0,
    }
    # P0 must take precedence over P1 within the critical tier
    assert pick_today.task_urgency_sort_key(crit_p0) < pick_today.task_urgency_sort_key(crit_p1)

    # Approaching P0 (due in 40h) vs Approaching P1 (due in 30h)
    app_p0 = {
        "category": "approaching",
        "priority": "P0",
        "remaining_hours": 40.0,
    }
    app_p1 = {
        "category": "approaching",
        "priority": "P1",
        "remaining_hours": 30.0,
    }
    assert pick_today.task_urgency_sort_key(app_p0) < pick_today.task_urgency_sort_key(app_p1)

def test_multi_task_override_scanning():
    """Verify that unassociated urgent tasks do not block override of active project tasks."""
    projects = [
        {"title": "1. GCI World 2026", "directory": "GCI_World_2026_September", "milestone": "M", "checkpoint": "C", "next_action": "N"}
    ]
    urgent_tasks = [
        {
            "description": "System maintenance infrastructure task",
            "source": "System Task Board",
            "priority": "P0",
            "remaining_hours": 5.0,
            "category": "critical",
            "countdown_str": "[D-0: 5h remaining]",
            "deadline_str": "2026-09-23 06:00",
        },
        {
            "description": "GCI World: Session 2 preparation with NumPy",
            "source": "1. GCI World 2026",
            "priority": "P0",
            "remaining_hours": 17.0,
            "category": "critical",
            "countdown_str": "[D-0: 17h remaining]",
            "deadline_str": "2026-09-24 19:00",
        }
    ]

    # Verify first task does not match
    assert pick_today.match_task_to_project(urgent_tasks[0], projects) is None

    # Verify override scanning successfully finds second task
    override_project = None
    override_task = None
    for ut in urgent_tasks:
        matched = pick_today.match_task_to_project(ut, projects)
        if matched:
            override_project = matched
            override_task = ut
            break

    assert override_project is not None
    assert override_project["title"] == "1. GCI World 2026"
    assert override_task["description"] == "GCI World: Session 2 preparation with NumPy"

def test_deduplication_between_macro_and_micro_boards():
    """Verify that tasks defined on both ACTIVE_LEARNING.md and local TASKS.md deduplicate cleanly."""
    goal_data, projects = pick_today.parse_active_learning(WORKSPACE_ROOT / "ACTIVE_LEARNING.md")
    now = datetime(2026, 9, 23, 1, 0, 0)
    tasks = pick_today.collect_all_tasks(WORKSPACE_ROOT / "ACTIVE_LEARNING.md", projects, now)

    # Count occurrences of the Ridge/Lasso task
    ridge_tasks = [t for t in tasks if "ridge" in t["description"].lower() and "lasso" in t["description"].lower()]
    assert len(ridge_tasks) == 1, f"Expected exactly 1 deduplicated Ridge task, found {len(ridge_tasks)}"

    # Count occurrences of the active uncompleted launch_hub milestone (due 2026-09-27)
    active_launch_tasks = [t for t in tasks if "launch_hub" in t["description"].lower() and not t["is_completed"]]
    assert len(active_launch_tasks) == 1, f"Expected exactly 1 deduplicated active launch_hub task, found {len(active_launch_tasks)}"

    # Count occurrences of Session 2 NumPy prep task (due 2026-09-24)
    gci_prep_tasks = [t for t in tasks if "buổi 2" in t["description"].lower() and not t["is_completed"]]
    assert len(gci_prep_tasks) == 1, f"Expected exactly 1 deduplicated GCI Session 2 prep task, found {len(gci_prep_tasks)}"
