#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Study Decision Roulette & Time Sentinel - True Random Generator & Deadline Watcher
Master Knowledge Map: file:///D:/02_Learning_Knowledge/INDEX.md
Dynamically parses ACTIVE_LEARNING.md and project TASKS.md to select today's active study mission.
Enforces the Time & Deadline Sentinel Protocol: checks system clock against task deadlines,
computes countdowns, and automatically flags or overrides priority when deadlines approach (< 48h).
Uses cryptographically secure hardware entropy (os.urandom / secrets).
Emoji Policy: strictly 0 emojis.
"""

import os
import re
import sys
import time
import secrets
from pathlib import Path
from datetime import datetime

# Force UTF-8 stdout encoding on Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).parent.resolve()
INDEX_FILE = SCRIPT_DIR / "INDEX.md"
ACTIVE_FILE = SCRIPT_DIR / "ACTIVE_LEARNING.md"
CENTRAL_TASKS_FILE = SCRIPT_DIR / "TASKS.md"

def parse_deadline_datetime(deadline_str: str | None) -> datetime | None:
    """Parse deadline string in YYYY-MM-DD HH:mm, YYYY/MM/DD HH:mm, ISO, or date-only formats."""
    if not deadline_str:
        return None
    s = deadline_str.strip().replace("T", " ").replace("/", "-")
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(s, fmt)
            if fmt == "%Y-%m-%d":
                dt = dt.replace(hour=23, minute=59, second=59)
            return dt
        except ValueError:
            continue
    return None

def clean_task_text(desc: str) -> str:
    """Clean markdown links, formatting, and file:/// URLs from task description."""
    s = desc.strip()
    # Replace markdown links [text](url) with just text
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    # Remove raw URLs
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"file:///\S+", "", s)
    # Remove markdown bold/italics (**text** or *text*)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    # Remove markdown inline code backticks `code`
    s = re.sub(r"`([^`]+)`", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()

def compute_countdown(deadline_dt: datetime | None, is_completed: bool, now: datetime | None = None) -> tuple[str, float | None, str]:
    """
    Compute countdown string, remaining hours, and urgency category.
    Categories: 'completed', 'overdue', 'critical' (<24h), 'approaching' (<48h), 'heads_up' (<72h), 'upcoming', 'none'
    Format examples: '[COMPLETED]', '[D-1: 18h remaining]', '[D-0: 4h 12m remaining]', '[OVERDUE: 2h ago]'
    """
    if is_completed:
        return ("[COMPLETED]", None, "completed")
    if deadline_dt is None:
        return ("[NO DEADLINE]", None, "none")

    if now is None:
        now = datetime.now()

    delta = deadline_dt - now
    total_seconds = delta.total_seconds()
    remaining_hours = total_seconds / 3600.0

    if total_seconds < 0:
        past = now - deadline_dt
        p_days = past.days
        p_hours = int(past.seconds // 3600)
        p_mins = int((past.seconds % 3600) // 60)
        if p_days > 0:
            countdown_str = f"[OVERDUE: {p_days}d {p_hours}h ago]"
        elif p_hours > 0:
            countdown_str = f"[OVERDUE: {p_hours}h {p_mins}m ago]"
        else:
            countdown_str = f"[OVERDUE: {p_mins}m ago]"
        return (countdown_str, remaining_hours, "overdue")

    days = delta.days
    hours = int(delta.seconds // 3600)
    mins = int((delta.seconds % 3600) // 60)

    if days > 0:
        countdown_str = f"[D-{days}: {hours}h remaining]"
    elif hours > 0:
        countdown_str = f"[D-0: {hours}h {mins}m remaining]"
    else:
        countdown_str = f"[D-0: {mins}m remaining]"

    if remaining_hours < 24.0:
        category = "critical"
    elif remaining_hours < 48.0:
        category = "approaching"
    elif remaining_hours < 72.0:
        category = "heads_up"
    else:
        category = "upcoming"

    return (countdown_str, remaining_hours, category)

def parse_task_line(line: str, source_label: str = "", now: datetime | None = None) -> dict | None:
    """Parse a single markdown checkbox task line into structured dictionary."""
    m = re.match(r"^\s*-\s*\[([ xX])\]\s*(.*)$", line)
    if not m:
        return None

    is_completed = m.group(1).lower() == "x"
    rest = m.group(2).strip()

    deadline_match = re.search(r"\[Deadline:\s*([^\]]+)\]", rest, re.IGNORECASE)
    priority_match = re.search(r"\[Priority:\s*(P[0-2])\]", rest, re.IGNORECASE)

    deadline_str = deadline_match.group(1).strip() if deadline_match else None
    priority = priority_match.group(1).upper() if priority_match else "P2"

    # Clean description
    desc = rest
    if deadline_match:
        desc = desc.replace(deadline_match.group(0), "")
    if priority_match:
        desc = desc.replace(priority_match.group(0), "")
    desc = clean_task_text(desc)

    deadline_dt = parse_deadline_datetime(deadline_str)
    countdown_str, remaining_hours, category = compute_countdown(deadline_dt, is_completed, now)

    return {
        "description": desc,
        "is_completed": is_completed,
        "deadline_str": deadline_str,
        "deadline_dt": deadline_dt,
        "priority": priority,
        "countdown_str": countdown_str,
        "remaining_hours": remaining_hours,
        "category": category,
        "source": source_label,
        "raw": line.strip(),
    }

def parse_active_learning(file_path: Path):
    """
    Parse ACTIVE_LEARNING.md for Today's Dynamic Goal and Active Projects.
    Preserves exact contract expected by test suites.
    """
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")

    # 1. Parse Today's Dynamic Goal
    goal_data = {}
    goal_match = re.search(
        r"(?m)^##\s+Today's Dynamic Goal.*?\n(.*?)(?=\n#{1,2}\s+|\Z)",
        content,
        re.DOTALL | re.IGNORECASE
    )
    if goal_match:
        for line in goal_match.group(1).strip().split("\n"):
            line = line.strip()
            if re.match(r"^[-*]?\s*Date\s*:", line, re.IGNORECASE):
                goal_data["date"] = re.sub(r"^[-*]?\s*Date\s*:\s*", "", line, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Subject\s*:", line, re.IGNORECASE):
                goal_data["subject"] = re.sub(r"^[-*]?\s*Subject\s*:\s*", "", line, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Target\s*:", line, re.IGNORECASE):
                goal_data["target"] = re.sub(r"^[-*]?\s*Target\s*:\s*", "", line, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*(?:Definition of Done\s*(?:\(DoD\))?|DoD)\s*:", line, re.IGNORECASE):
                goal_data["dod"] = re.sub(r"^[-*]?\s*(?:Definition of Done\s*(?:\(DoD\))?|DoD)\s*:\s*", "", line, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Status\s*:", line, re.IGNORECASE):
                goal_data["status"] = re.sub(r"^[-*]?\s*Status\s*:\s*", "", line, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Deadline\s*:", line, re.IGNORECASE):
                goal_data["deadline"] = re.sub(r"^[-*]?\s*Deadline\s*:\s*", "", line, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Priority\s*:", line, re.IGNORECASE):
                goal_data["priority"] = re.sub(r"^[-*]?\s*Priority\s*:\s*", "", line, flags=re.IGNORECASE).strip()

    # 2. Parse Active Projects
    section_match = re.search(
        r"(?m)^##\s+Active Projects.*?\n(.*?)(?=\n#{1,2}\s+|\Z)",
        content,
        re.DOTALL | re.IGNORECASE
    )
    if not section_match:
        print("Error: Could not locate '## Active Projects' section in ACTIVE_LEARNING.md")
        sys.exit(1)

    raw_section = section_match.group(1)
    raw_items = re.findall(r"(?m)^###\s+(.*?)(?=(?:\n###\s+|\Z))", raw_section, re.DOTALL)
    projects = []

    for item in raw_items:
        item = item.strip()
        if not item:
            continue
        lines = [l for l in item.split("\n") if l.strip()]
        if not lines:
            continue
        title = lines[0].strip()

        directory = ""
        task_board = ""
        milestone = ""
        checkpoint = ""
        next_action = ""
        deadline = ""
        priority = "P2"

        for line in lines[1:]:
            line_str = line.strip()
            if re.match(r"^[-*]?\s*Directory:", line_str, re.IGNORECASE):
                directory = re.sub(r"^[-*]?\s*Directory:\s*", "", line_str, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*(?:Tasks|Task Board):", line_str, re.IGNORECASE):
                task_board = re.sub(r"^[-*]?\s*(?:Tasks|Task Board):\s*", "", line_str, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Milestone:", line_str, re.IGNORECASE):
                milestone = re.sub(r"^[-*]?\s*Milestone:\s*", "", line_str, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Checkpoint:", line_str, re.IGNORECASE):
                checkpoint = re.sub(r"^[-*]?\s*Checkpoint:\s*", "", line_str, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Next Action:", line_str, re.IGNORECASE):
                next_action = re.sub(r"^[-*]?\s*Next Action:\s*", "", line_str, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Deadline:", line_str, re.IGNORECASE):
                deadline = re.sub(r"^[-*]?\s*Deadline:\s*", "", line_str, flags=re.IGNORECASE).strip()
            elif re.match(r"^[-*]?\s*Priority:", line_str, re.IGNORECASE):
                priority = re.sub(r"^[-*]?\s*Priority:\s*", "", line_str, flags=re.IGNORECASE).strip()

        projects.append({
            "title": title,
            "directory": directory,
            "task_board": task_board,
            "milestone": milestone,
            "checkpoint": checkpoint,
            "next_action": next_action,
            "deadline": deadline,
            "priority": priority,
        })

    return goal_data, projects

def resolve_project_dir(directory_str: str, base_dir: Path) -> Path | None:
    """Extract and resolve directory path from markdown links or plain paths."""
    if not directory_str:
        return None
    m_url = re.search(r"file:///(?:[a-zA-Z]:/)?([^\s\)\"\'\`>\]]+)", directory_str)
    if m_url:
        cand = Path(m_url.group(0).replace("file:///", ""))
        if cand.exists():
            return cand
    m_md = re.search(r"\[(.*?)\]\((.*?)\)", directory_str)
    if m_md:
        link = m_md.group(2)
        if link.startswith("file:///"):
            cand = Path(link[8:])
            if cand.exists():
                return cand
        cand = base_dir / m_md.group(1)
        if cand.exists():
            return cand
    clean = re.sub(r"[\[\]]", "", directory_str).strip()
    cand = base_dir / clean
    if cand.exists():
        return cand
    cand_abs = Path(clean)
    if cand_abs.exists():
        return cand_abs
    return None

def normalize_task_desc(desc: str, known_prefixes: list[str] | None = None) -> str:
    """Normalize task description to aid deduplication across boards."""
    s = clean_task_text(desc).lower().strip()
    if known_prefixes:
        for pfx in known_prefixes:
            clean_pfx = re.escape(pfx.lower().strip())
            s = re.sub(rf"^{clean_pfx}\s*:\s*", "", s)
    s = re.sub(r"^(?:gci world|machine learning|python master|quantum computing|amd ai academy|cos pro)\s*:\s*", "", s)
    s = re.sub(r"^[a-z0-9_\s-]{3,30}\s*:\s*", "", s)
    s = re.sub(r"[^\w\s]", "", s)
    return re.sub(r"\s+", " ", s).strip()

def collect_all_tasks(active_file: Path, projects: list, now: datetime | None = None) -> list[dict]:
    """
    Collect and deduplicate tasks from ACTIVE_LEARNING.md, central TASKS.md,
    and active subproject TASKS.md boards. Avoids duplicate reads of the same file.
    Prefers authoritative project boards for source and details.
    """
    tasks = []
    task_map = {}  # key -> index in tasks
    parsed_files = set()

    known_prefixes = [p["title"] for p in projects] + [re.sub(r"^\d+\.\s*", "", p["title"]) for p in projects]

    def add_task(t: dict | None, is_project_board: bool = False):
        if not t:
            return
        norm = normalize_task_desc(t["description"], known_prefixes)
        key = (norm, t["deadline_str"])
        if key not in task_map:
            task_map[key] = len(tasks)
            tasks.append(t)
        else:
            existing_idx = task_map[key]
            existing = tasks[existing_idx]
            # Prioritize project board metadata over macro or central board
            if is_project_board or (existing["source"] in ["Active Learning Board", "System Task Board"] and t["source"] not in ["Active Learning Board", "System Task Board"]):
                tasks[existing_idx] = t

    # 1. Parse active file (e.g. ACTIVE_LEARNING.md)
    if active_file.exists():
        parsed_files.add(active_file.resolve())
        content = active_file.read_text(encoding="utf-8")
        for line in content.splitlines():
            if re.match(r"^\s*-\s*\[[ xX]\]", line):
                src_label = "Active Learning Board"
                for p in projects:
                    p_name = re.sub(r"^\d+\.\s*", "", p["title"]).strip().lower()
                    clean_line = clean_task_text(line).lower()
                    if f"{p_name}:" in clean_line or f"{p['title'].lower()}:" in clean_line:
                        src_label = p["title"]
                        break
                add_task(parse_task_line(line, src_label, now), is_project_board=False)

    # 2. Parse central TASKS.md
    if CENTRAL_TASKS_FILE.exists():
        parsed_files.add(CENTRAL_TASKS_FILE.resolve())
        content = CENTRAL_TASKS_FILE.read_text(encoding="utf-8")
        for line in content.splitlines():
            if re.match(r"^\s*-\s*\[[ xX]\]", line):
                add_task(parse_task_line(line, "System Task Board", now), is_project_board=False)

    # 3. Parse active project TASKS.md files
    for p in projects:
        p_tasks_file = None
        if p.get("task_board"):
            m_tb = re.search(r"file:///(?:[a-zA-Z]:/)?([^\s\)\"\'\`>\]]+)", p["task_board"])
            if m_tb:
                cand = Path(m_tb.group(0).replace("file:///", ""))
                if cand.exists():
                    p_tasks_file = cand
        if not p_tasks_file:
            p_dir = resolve_project_dir(p["directory"], SCRIPT_DIR)
            if p_dir and p_dir.is_dir():
                p_tasks_file = (p_dir / "TASKS.md").resolve()

        if p_tasks_file and p_tasks_file.exists() and p_tasks_file not in parsed_files:
            parsed_files.add(p_tasks_file)
            content = p_tasks_file.read_text(encoding="utf-8")
            for line in content.splitlines():
                if re.match(r"^\s*-\s*\[[ xX]\]", line):
                    add_task(parse_task_line(line, p["title"], now), is_project_board=True)

    # 4. Check subdirectories under SCRIPT_DIR with TASKS.md not yet parsed
    for sub in SCRIPT_DIR.iterdir():
        if sub.is_dir():
            sub_file = (sub / "TASKS.md").resolve()
            if sub_file.exists() and sub_file not in parsed_files:
                parsed_files.add(sub_file)
                content = sub_file.read_text(encoding="utf-8")
                for line in content.splitlines():
                    if re.match(r"^\s*-\s*\[[ xX]\]", line):
                        add_task(parse_task_line(line, sub.name, now), is_project_board=True)

    return tasks

PRIORITY_RANK = {"P0": 0, "P1": 1, "P2": 2}

def task_urgency_sort_key(t: dict) -> tuple:
    """
    Sort key respecting urgency tier, priority tag, and remaining time:
    - Tier 0: Overdue (< 0h) - Immediate blockers
    - Tier 1: Critical (< 24h) - Urgent alerts
    - Tier 2: Approaching (< 48h) - High priority override
    - Tier 3: Other
    Within each tier: P0 before P1 before P2.
    Within same tier and priority: tasks due earlier first.
    """
    if t["category"] == "overdue":
        tier = 0
    elif t["remaining_hours"] is not None and t["remaining_hours"] < 24.0:
        tier = 1
    elif t["remaining_hours"] is not None and t["remaining_hours"] < 48.0:
        tier = 2
    else:
        tier = 3
    p_rank = PRIORITY_RANK.get(t.get("priority", "P2").upper(), 2)
    rem = t.get("remaining_hours") if t.get("remaining_hours") is not None else float("inf")
    return (tier, p_rank, rem)

def match_task_to_project(task: dict, projects: list) -> dict | None:
    """Associate a task with an active project dynamically without fragile hardcoded keywords."""
    src = task.get("source", "").lower()
    desc = clean_task_text(task.get("description", "")).lower()

    for p in projects:
        p_title = p["title"].lower()
        p_name = re.sub(r"^\d+\.\s*", "", p_title).strip()
        p_dir_str = p.get("directory", "").lower()
        m_folder = re.search(r"/(?:[a-zA-Z]:/)?(?:02_Learning_Knowledge/)?([^/\]\)\"\'`]+)", p_dir_str)
        p_folder = m_folder.group(1).lower() if m_folder else ""
        p_folder_spaced = p_folder.replace("_", " ")

        # 1. Match against source label
        if p_title in src or p_name in src:
            return p
        if p_folder and (p_folder in src or p_folder_spaced in src):
            return p

        # 2. Match against description prefix
        if desc.startswith(f"{p_name}:") or desc.startswith(f"{p_title}:"):
            return p
        if p_folder and (desc.startswith(f"{p_folder}:") or desc.startswith(f"{p_folder_spaced}:")):
            return p

        # 3. Check project title / clean name / folder presence in description
        if p_name in desc:
            return p
        if p_folder and (p_folder in desc or p_folder_spaced in desc):
            return p

        # 4. Check distinctive acronyms / keywords
        if "gci" in p_name and ("gci" in desc or "omnicampus" in desc):
            return p
        if "machine learning" in p_name and ("machine learning" in desc or "regression" in desc or "supervised" in desc):
            return p
        if "python master" in p_name and ("python" in desc or "cos pro" in desc or "launch_hub" in desc):
            return p
        if "quantum" in p_name and ("quantum" in desc or "katas" in desc or "qsim" in desc):
            return p
        if "amd" in p_name and ("amd" in desc or "ai agents" in desc):
            return p

    return None

def display_spinner(projects: list):
    """Visual hardware entropy spinner."""
    print("\n[Study Decision Roulette] - Hardware Entropy Randomizer")
    print("=" * 67)
    print(f"Loaded {len(projects)} active subjects from ACTIVE_LEARNING.md")
    print("Shuffling via secrets.choice (OS cryptographic entropy)...")
    print("-" * 67)

    spin_names = [p["title"] for p in projects]
    if sys.stdout.isatty():
        total_spins = 15
        for i in range(total_spins):
            cur = spin_names[i % len(spin_names)]
            sys.stdout.write(f"\r  Rolling: [ {cur:<45} ]")
            sys.stdout.flush()
            time.sleep(0.04 + (i * 0.015))
        print("\r" + " " * 67 + "\r", end="")

def print_sentinel_report(tasks: list, now: datetime):
    """Detailed Sentinel audit report of all task deadlines."""
    print("\n" + "=" * 30 + " TIME SENTINEL AUDIT " + "=" * 30)
    print(f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 81)

    overdue = [t for t in tasks if t["category"] == "overdue"]
    critical = [t for t in tasks if t["category"] == "critical"]
    approaching = [t for t in tasks if t["category"] == "approaching"]
    heads_up = [t for t in tasks if t["category"] == "heads_up"]
    upcoming = [t for t in tasks if t["category"] == "upcoming"]
    unscheduled = [t for t in tasks if t["category"] == "none" and not t["is_completed"]]
    completed = [t for t in tasks if t["is_completed"]]

    def print_group(label: str, group: list):
        if not group:
            return
        print(f"\n[{label}] ({len(group)} items):")
        for t in group:
            p_tag = f"[{t['priority']}]"
            cd_tag = t["countdown_str"]
            dl_tag = f"(Deadline: {t['deadline_str']})" if t["deadline_str"] else ""
            print(f"  * {p_tag:<5} {cd_tag:<24} {dl_tag:<28} [{t['source']}]")
            print(f"    Task: {t['description']}")

    print_group("OVERDUE - BLOCKERS", overdue)
    print_group("CRITICAL (< 24H) - IMMEDIATE ACTION", critical)
    print_group("APPROACHING (< 48H) - HIGH PRIORITY", approaching)
    print_group("HEADS-UP (< 72H) - PROACTIVE REMINDER", heads_up)
    print_group("UPCOMING (> 72H) - ON TRACK", upcoming)
    print_group("UNSCHEDULED (NO DEADLINE SET)", unscheduled)
    print(f"\n[COMPLETED MILESTONES] ({len(completed)} items verified)")
    print("=" * 81 + "\n")

def main():
    now = datetime.now()

    # CLI argument parsing
    force_roll = "--roll" in sys.argv
    sentinel_mode = "--sentinel" in sys.argv or "--check" in sys.argv

    custom_files = [Path(a) for a in sys.argv[1:] if not a.startswith("-")]
    target_file = custom_files[0] if custom_files else ACTIVE_FILE

    goal_data, projects = parse_active_learning(target_file)
    if not projects:
        print("Error: No active projects parsed from ACTIVE_LEARNING.md.")
        sys.exit(1)

    # Collect tasks across workspace and project boards
    tasks = collect_all_tasks(target_file, projects, now)

    if sentinel_mode:
        print_sentinel_report(tasks, now)
        return

    # Check for approaching (< 48 hours) or overdue tasks
    urgent_tasks = [
        t for t in tasks
        if not t["is_completed"] and t["remaining_hours"] is not None and t["remaining_hours"] < 48.0
    ]
    urgent_tasks.sort(key=task_urgency_sort_key)

    override_project = None
    override_task = None
    if urgent_tasks:
        print("\n" + "=" * 71)
        print(f"[URGENT DEADLINE SENTINEL: {len(urgent_tasks)} TASK(S) DUE WITHIN 48 HOURS]")
        print("=" * 71)
        for ut in urgent_tasks:
            src = ut["source"]
            print(f"  ! [{ut['priority']}] {ut['countdown_str']} (Deadline: {ut['deadline_str']})")
            print(f"    Source: {src}")
            print(f"    Task  : {ut['description']}")
        print("-" * 71)

        # Scan for the highest-ranking urgent task mapped to an active project
        for ut in urgent_tasks:
            matched = match_task_to_project(ut, projects)
            if matched:
                override_project = matched
                override_task = ut
                break

        if not force_roll and override_project and override_task:
            print("AUTOMATIC PRIORITY OVERRIDE ENGAGED")
            print(f"Study focus locked to: {override_project['title']}")
            print(f"Reason: Impending deadline {override_task['countdown_str']} (< 48h sentinel threshold).")
            print(f"        [{override_task['priority']}] {override_task['description']}")
            print("Notice: Pass '--roll' to bypass override and run hardware roulette.")
            print("=" * 71)
        elif force_roll:
            print("FLAGGED PRIORITY WARNING: Impending deadlines detected above.")
            print("Notice: Bypassing automatic override due to '--roll' CLI flag.")
            print("=" * 71)
        else:
            print("NOTICE: Urgent cross-cutting or unassigned tasks detected.")
            print("=" * 71)

    # Select mission
    if override_project and not force_roll:
        chosen = override_project
    else:
        display_spinner(projects)
        chosen = secrets.choice(projects)

    # Display Today's Mission
    print("\n" + "=" * 27 + " TODAY'S MISSION " + "=" * 27 + "\n")
    print(f"  Topic       : {chosen['title']}")
    if chosen["directory"]:
        print(f"  Directory   : {chosen['directory']}")
    if chosen.get("task_board"):
        print(f"  Task Board  : {chosen['task_board']}")
    if chosen["milestone"]:
        print(f"  Milestone   : {chosen['milestone']}")
    if chosen["checkpoint"]:
        print(f"  Last Stop   : {chosen['checkpoint']}")
    if chosen["next_action"]:
        print(f"  Next Action : {chosen['next_action']}")
    if chosen.get("deadline"):
        dl_dt = parse_deadline_datetime(chosen["deadline"])
        cd, _, _ = compute_countdown(dl_dt, False, now)
        print(f"  Deadline    : {chosen['deadline']} {cd}")

    # Display Current Active Goal if present
    if goal_data and goal_data.get("subject"):
        print("\n" + "-" * 71)
        print("  Current Active Goal:")
        print(f"  [{goal_data.get('date', 'N/A')}] {goal_data.get('subject')}: {goal_data.get('target')}")
        print(f"  DoD         : {goal_data.get('dod', 'N/A')}")
        print(f"  Status      : {goal_data.get('status', 'Pending')}")
        if goal_data.get("deadline"):
            g_dl_dt = parse_deadline_datetime(goal_data["deadline"])
            g_cd, _, _ = compute_countdown(g_dl_dt, goal_data.get("status", "").lower() == "completed", now)
            print(f"  Deadline    : {goal_data['deadline']} {g_cd}")

    # Display Upcoming Active Deadlines summary
    pending_dated_tasks = [
        t for t in tasks
        if not t["is_completed"] and t["deadline_dt"] is not None and t["remaining_hours"] is not None
    ]
    pending_dated_tasks.sort(key=lambda t: t["remaining_hours"])
    if pending_dated_tasks:
        print("\n" + "-" * 71)
        print("  Upcoming Active Deadlines:")
        for t in pending_dated_tasks[:4]:
            print(f"  * {t['countdown_str']:<22} [{t['priority']}] {t['description'][:48]} ({t['source']})")

    index_url = f"file:///{INDEX_FILE.as_posix()}" if INDEX_FILE.exists() else "file:///D:/02_Learning_Knowledge/INDEX.md"
    print("\n" + "=" * 71)
    print(f"  Master Knowledge Map: {index_url}")
    print(f"  Target Action       : Tell AI: 'Set mục tiêu hôm nay cho {chosen['title']}'")
    print("=" * 71 + "\n")

if __name__ == "__main__":
    main()
