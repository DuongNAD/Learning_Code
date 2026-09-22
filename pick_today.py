#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Study Decision Roulette - True Random Generator & Dynamic Goal Tracker
Dynamically parses ACTIVE_LEARNING.md to pick today's active study mission.
Uses cryptographically secure hardware entropy (os.urandom / secrets).
"""

import os
import re
import sys
import time
import secrets
from pathlib import Path
from datetime import datetime

# Force UTF-8 stdout encoding on Windows
if sys.platform == "win32":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).parent.resolve()
ACTIVE_FILE = SCRIPT_DIR / "ACTIVE_LEARNING.md"

def parse_active_learning(file_path: Path):
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")
    
    # 1. Parse Today's Dynamic Goal if present
    goal_data = {}
    goal_match = re.search(
        r"##\s+Today's Dynamic Goal.*?\n(.*?)(?=\n## |\Z)",
        content,
        re.DOTALL | re.IGNORECASE
    )
    if goal_match:
        for line in goal_match.group(1).strip().split("\n"):
            line = line.strip()
            if line.startswith("- Date:"):
                goal_data["date"] = line.replace("- Date:", "").strip()
            elif line.startswith("- Subject:"):
                goal_data["subject"] = line.replace("- Subject:", "").strip()
            elif line.startswith("- Target:"):
                goal_data["target"] = line.replace("- Target:", "").strip()
            elif line.startswith("- Definition of Done (DoD):"):
                goal_data["dod"] = line.replace("- Definition of Done (DoD):", "").strip()
            elif line.startswith("- Status:"):
                goal_data["status"] = line.replace("- Status:", "").strip()

    # 2. Parse Active Projects
    section_match = re.search(
        r"##\s+Active Projects.*?\n(.*?)(?=\n## |\Z)",
        content,
        re.DOTALL | re.IGNORECASE
    )
    if not section_match:
        print("Error: Could not locate '## Active Projects' section in ACTIVE_LEARNING.md")
        sys.exit(1)

    raw_section = section_match.group(1)
    raw_items = re.split(r"(?m)^###\s+", raw_section)
    projects = []

    for item in raw_items:
        item = item.strip()
        if not item:
            continue
        lines = item.split("\n")
        title = lines[0].strip()

        directory = ""
        milestone = ""
        checkpoint = ""
        next_action = ""

        for line in lines[1:]:
            line_str = line.strip()
            if re.match(r"^[-*]?\s*Directory:", line_str, re.IGNORECASE):
                directory = re.sub(r"^[-*]?\s*Directory:\s*", "", line_str, flags=re.IGNORECASE)
            elif re.match(r"^[-*]?\s*Milestone:", line_str, re.IGNORECASE):
                milestone = re.sub(r"^[-*]?\s*Milestone:\s*", "", line_str, flags=re.IGNORECASE)
            elif re.match(r"^[-*]?\s*Checkpoint:", line_str, re.IGNORECASE):
                checkpoint = re.sub(r"^[-*]?\s*Checkpoint:\s*", "", line_str, flags=re.IGNORECASE)
            elif re.match(r"^[-*]?\s*Next Action:", line_str, re.IGNORECASE):
                next_action = re.sub(r"^[-*]?\s*Next Action:\s*", "", line_str, flags=re.IGNORECASE)

        projects.append({
            "title": title,
            "directory": directory,
            "milestone": milestone,
            "checkpoint": checkpoint,
            "next_action": next_action,
        })

    return goal_data, projects

def display_spinner(projects):
    print("\n[Study Decision Roulette] - Hardware Entropy Randomizer")
    print("=" * 65)
    print(f"Loaded {len(projects)} active subjects from ACTIVE_LEARNING.md")
    print("Shuffling via secrets.choice (OS cryptographic entropy)...")
    print("-" * 65)

    spin_names = [p["title"] for p in projects]
    total_spins = 15
    for i in range(total_spins):
        cur = spin_names[i % len(spin_names)]
        sys.stdout.write(f"\r  Rolling: [ {cur:<45} ]")
        sys.stdout.flush()
        time.sleep(0.04 + (i * 0.015))

    print("\r" + " " * 65 + "\r", end="")

def main():
    goal_data, projects = parse_active_learning(ACTIVE_FILE)
    if not projects:
        print("Error: No active projects parsed from ACTIVE_LEARNING.md.")
        sys.exit(1)

    display_spinner(projects)

    # True cryptographic random selection
    chosen = secrets.choice(projects)

    print("\n" + "=" * 25 + " TODAY'S MISSION " + "=" * 25 + "\n")
    print(f"  Topic       : {chosen['title']}")
    if chosen['directory']:
        print(f"  Directory   : {chosen['directory']}")
    if chosen['milestone']:
        print(f"  Milestone   : {chosen['milestone']}")
    if chosen['checkpoint']:
        print(f"  Last Stop   : {chosen['checkpoint']}")
    if chosen['next_action']:
        print(f"  Next Action : {chosen['next_action']}")

    # Check if there is an existing goal
    if goal_data and goal_data.get("subject"):
        print("\n" + "-" * 67)
        print("  Current Active Goal:")
        print(f"  [{goal_data.get('date', 'N/A')}] {goal_data.get('subject')}: {goal_data.get('target')}")
        print(f"  DoD   : {goal_data.get('dod', 'N/A')}")
        print(f"  Status: {goal_data.get('status', 'Pending')}")

    print("\n" + "=" * 67)
    print(f"💬 To set/update dynamic goal, tell AI: 'Set mục tiêu hôm nay cho {chosen['title']}'")
    print("=" * 67 + "\n")

if __name__ == "__main__":
    main()
