"""
Verification test suite for AI-Native Markdown Architecture and Knowledge Map.
Tests link validity, emoji absence, pick_today.py parsing, and RFC 2119 keywords.
"""

import os
import re
import sys
import unicodedata
from pathlib import Path
import pytest

WORKSPACE_ROOT = Path("D:/02_Learning_Knowledge")
ROOT_GEMINI = Path("D:/GEMINI.md")

TARGET_FILES = [
    WORKSPACE_ROOT / "INDEX.md",
    WORKSPACE_ROOT / "ACTIVE_LEARNING.md",
    WORKSPACE_ROOT / "GEMINI.md",
    WORKSPACE_ROOT / "AGENTS.md",
    WORKSPACE_ROOT / "TASKS.md",
    WORKSPACE_ROOT / "README.md",
    WORKSPACE_ROOT / "pick_today.py",
    WORKSPACE_ROOT / "roll_study.bat",
    WORKSPACE_ROOT / "roll_study.command",
    ROOT_GEMINI,
    WORKSPACE_ROOT / "GCI_World_2026_September" / "TASKS.md",
    WORKSPACE_ROOT / "Machine_Learning" / "TASKS.md",
    WORKSPACE_ROOT / "Python_Master" / "TASKS.md",
    WORKSPACE_ROOT / "Quantum_Computing" / "TASKS.md",
    WORKSPACE_ROOT / "AMD_AI_Academy_AI_Agents_101" / "TASKS.md",
    WORKSPACE_ROOT / "test_deadline_sentinel.py",
]

def is_emoji_or_icon(char: str) -> bool:
    """Check if character is an emoji or symbol icon."""
    cat = unicodedata.category(char)
    code = ord(char)
    # Common emoji ranges
    if 0x1F300 <= code <= 0x1FAD6:
        return True
    if 0x1F600 <= code <= 0x1F64F:
        return True
    if 0x2600 <= code <= 0x27BF:
        return True
    if 0xFE00 <= code <= 0xFE0F:  # Variation selector
        return True
    if 0x1F900 <= code <= 0x1F9FF:
        return True
    return False

def test_target_files_exist():
    for f in TARGET_FILES:
        assert f.exists(), f"File does not exist: {f}"

def test_zero_emojis_in_target_files():
    for f in TARGET_FILES:
        content = f.read_text(encoding="utf-8")
        emojis_found = []
        for line_no, line in enumerate(content.splitlines(), start=1):
            for char in line:
                if is_emoji_or_icon(char):
                    emojis_found.append((line_no, char, hex(ord(char))))
        assert len(emojis_found) == 0, f"Found emojis in {f.name}: {emojis_found}"

def test_file_links_validity():
    """Verify all file:/// absolute links resolve to real paths."""
    link_regex = re.compile(r"file:///(D:[^\s\)\"\'\`>\]]+)")
    for f in TARGET_FILES:
        if f.suffix in [".py", ".bat", ".command"]:
            continue
        content = f.read_text(encoding="utf-8")
        matches = link_regex.findall(content)
        assert len(matches) > 0, f"No file:/// links found in {f.name}"
        for path_str in matches:
            # Strip markdown anchor fragments (#...)
            clean_path = path_str.split("#")[0]
            # Replace %23 if any
            clean_path = clean_path.replace("%23", "#")
            p = Path(clean_path)
            assert p.exists(), f"Broken link in {f.name}: {clean_path}"

def test_rfc2119_keywords_present():
    """Verify key documents strictly contain RFC 2119 constraint keywords MUST, NEVER, and ONLY IF."""
    docs = [
        WORKSPACE_ROOT / "INDEX.md",
        WORKSPACE_ROOT / "ACTIVE_LEARNING.md",
        WORKSPACE_ROOT / "GEMINI.md",
        WORKSPACE_ROOT / "AGENTS.md",
        WORKSPACE_ROOT / "TASKS.md",
        WORKSPACE_ROOT / "README.md",
    ]
    required_keywords = ["MUST", "NEVER", "ONLY IF"]
    for doc in docs:
        content = doc.read_text(encoding="utf-8")
        for kw in required_keywords:
            assert re.search(r"\b" + kw + r"\b", content), (
                f"Document {doc.name} missing mandatory RFC 2119 keyword '{kw}'"
            )

def test_metadata_headers_present():
    """Verify key documents start with YAML frontmatter."""
    docs = [
        WORKSPACE_ROOT / "INDEX.md",
        WORKSPACE_ROOT / "ACTIVE_LEARNING.md",
        WORKSPACE_ROOT / "GEMINI.md",
        WORKSPACE_ROOT / "AGENTS.md",
        WORKSPACE_ROOT / "TASKS.md",
        WORKSPACE_ROOT / "README.md",
    ]
    for doc in docs:
        content = doc.read_text(encoding="utf-8")
        assert content.startswith("---\n"), f"Document {doc.name} missing YAML frontmatter header"
        assert "\nmaster_index: " in content or "document_type: master_knowledge_map" in content, (
            f"Document {doc.name} does not reference master_index"
        )

def test_condition_action_matrices_present():
    """Verify condition-action matrices exist in key documentation."""
    docs = [
        WORKSPACE_ROOT / "INDEX.md",
        WORKSPACE_ROOT / "ACTIVE_LEARNING.md",
        WORKSPACE_ROOT / "GEMINI.md",
        WORKSPACE_ROOT / "AGENTS.md",
    ]
    for doc in docs:
        content = doc.read_text(encoding="utf-8")
        assert "| " in content and " |" in content, f"No Markdown matrix found in {doc.name}"
        assert re.search(r"\|\s*(?:Agent Trigger|Event|Learner Input)", content), (
            f"Expected condition-action column not found in {doc.name}"
        )

def test_pick_today_parses_cleanly():
    """Verify pick_today.py functions properly on actual active file."""
    sys.path.insert(0, str(WORKSPACE_ROOT))
    import pick_today
    goal_data, projects = pick_today.parse_active_learning(WORKSPACE_ROOT / "ACTIVE_LEARNING.md")

    assert len(projects) == 5, f"Expected exactly 5 active projects, got {len(projects)}"
    expected_titles = [
        "1. GCI World 2026",
        "2. Machine Learning",
        "3. Python Master",
        "4. Quantum Computing",
        "5. AMD AI Academy - AI Agents 101",
    ]
    actual_titles = [p["title"] for p in projects]
    assert actual_titles == expected_titles

    for p in projects:
        assert p["directory"], f"Missing directory for {p['title']}"
        assert p["milestone"], f"Missing milestone for {p['title']}"
        assert p["checkpoint"], f"Missing checkpoint for {p['title']}"
        assert p["next_action"], f"Missing next action for {p['title']}"

    assert goal_data.get("subject") == "GCI World 2026"
    assert goal_data.get("status") == "Pending"
    assert goal_data.get("dod")

def test_pick_today_edge_cases(tmp_path):
    """Verify pick_today handles corner cases gracefully."""
    import pick_today

    # 1. Active file without goal section
    test_file_no_goal = tmp_path / "NO_GOAL.md"
    test_file_no_goal.write_text(
        "## Active Projects\n\n### 1. Test Project\n- Directory: D:/test\n- Milestone: Test\n- Checkpoint: Done\n- Next Action: Continue\n",
        encoding="utf-8"
    )
    goal_data, projects = pick_today.parse_active_learning(test_file_no_goal)
    assert goal_data == {}
    assert len(projects) == 1
    assert projects[0]["title"] == "1. Test Project"

    # 2. Missing Active Projects section exits with error
    test_file_missing_projects = tmp_path / "MISSING_PROJECTS.md"
    test_file_missing_projects.write_text("## Some Other Heading\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        pick_today.parse_active_learning(test_file_missing_projects)

    # 3. Active Projects with introductory prose text does NOT produce a phantom project
    test_file_with_intro = tmp_path / "WITH_INTRO.md"
    test_file_with_intro.write_text(
        "## Active Projects\n\n"
        "Here is the project overview and WIP bound directives.\n"
        "Do not parse this intro paragraph as a project.\n\n"
        "### 1. Project Alpha\n"
        "- Directory: D:/alpha\n"
        "- Milestone: Alpha Done\n"
        "- Checkpoint: Checked\n"
        "- Next Action: Advance\n\n"
        "### 2. Project Beta\n"
        "- Directory: D:/beta\n"
        "- Milestone: Beta Done\n"
        "- Checkpoint: Checked\n"
        "- Next Action: Advance\n",
        encoding="utf-8"
    )
    goal_data, projects = pick_today.parse_active_learning(test_file_with_intro)
    assert len(projects) == 2
    assert projects[0]["title"] == "1. Project Alpha"
    assert projects[1]["title"] == "2. Project Beta"

    # 4. Today's Dynamic Goal with asterisk bullets, DoD variant, extra whitespace, and embedded target tokens
    test_file_goal_variants = tmp_path / "GOAL_VARIANTS.md"
    test_file_goal_variants.write_text(
        "## Today's Dynamic Goal\n"
        "* Date : 2026-09-23\n"
        "* Subject: Quantum Computing\n"
        "* Target: Fix issue with - Target: string correctly\n"
        "* DoD: Zero runtime errors and clean tests\n"
        "* Status: In Progress\n\n"
        "## Active Projects\n\n"
        "### 1. Quantum Computing\n"
        "- Directory: D:/quantum\n"
        "- Milestone: Gate simulation\n"
        "- Checkpoint: State prep\n"
        "- Next Action: Bell states\n",
        encoding="utf-8"
    )
    goal_data, projects = pick_today.parse_active_learning(test_file_goal_variants)
    assert goal_data["date"] == "2026-09-23"
    assert goal_data["subject"] == "Quantum Computing"
    assert goal_data["target"] == "Fix issue with - Target: string correctly"
    assert goal_data["dod"] == "Zero runtime errors and clean tests"
    assert goal_data["status"] == "In Progress"
    assert len(projects) == 1

def test_2_tier_task_architecture_integrity():
    """Verify that all 5 active focus projects have dedicated TASKS.md with standardized schema and valid frontmatter."""
    project_task_files = [
        WORKSPACE_ROOT / "GCI_World_2026_September" / "TASKS.md",
        WORKSPACE_ROOT / "Machine_Learning" / "TASKS.md",
        WORKSPACE_ROOT / "Python_Master" / "TASKS.md",
        WORKSPACE_ROOT / "Quantum_Computing" / "TASKS.md",
        WORKSPACE_ROOT / "AMD_AI_Academy_AI_Agents_101" / "TASKS.md",
    ]
    task_pattern = re.compile(r"^\s*-\s*\[[ xX]\]\s*\[Deadline:\s*\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}\]\s*\[Priority:\s*P[0-2]\]\s+.+$")

    for ptf in project_task_files:
        assert ptf.exists(), f"Project task board missing: {ptf}"
        content = ptf.read_text(encoding="utf-8")
        assert content.startswith("---\n"), f"Missing YAML header in {ptf.name}"
        assert "document_type: project_task_board" in content
        assert "master_index: " in content
        assert "focus_board: " in content
        assert "- [ ]" in content or "- [x]" in content, f"No checklists found in {ptf}"
        for kw in ["MUST", "NEVER", "ONLY IF"]:
            assert re.search(r"\b" + kw + r"\b", content), f"Missing RFC 2119 keyword '{kw}' in {ptf}"

        # Verify all task checkboxes adhere to standardized tag schema
        task_lines = [l for l in content.splitlines() if re.match(r"^\s*-\s*\[[ xX]\]", l)]
        assert len(task_lines) > 0, f"No task lines found in {ptf.name}"
        for tl in task_lines:
            assert task_pattern.match(tl), f"Non-conforming task in {ptf.name}: {tl}"

def test_agent_directives_specify_2_tier_workflow():
    """Verify GEMINI.md and AGENTS.md explicitly mandate the 2-tier task management workflow."""
    directive_files = [
        WORKSPACE_ROOT / "GEMINI.md",
        WORKSPACE_ROOT / "AGENTS.md",
    ]
    for df in directive_files:
        content = df.read_text(encoding="utf-8")
        assert "2-Tier Task Management" in content
        assert "Macro-Tier" in content
        assert "Micro-Tier" in content
        assert "Workspace System Tier" in content
        assert "ACTIVE_LEARNING.md" in content
        assert "local `TASKS.md`" in content

def test_active_learning_router_links():
    """Verify ACTIVE_LEARNING.md includes direct links to all 5 local TASKS.md files."""
    content = (WORKSPACE_ROOT / "ACTIVE_LEARNING.md").read_text(encoding="utf-8")
    expected_links = [
        "file:///D:/02_Learning_Knowledge/GCI_World_2026_September/TASKS.md",
        "file:///D:/02_Learning_Knowledge/Machine_Learning/TASKS.md",
        "file:///D:/02_Learning_Knowledge/Python_Master/TASKS.md",
        "file:///D:/02_Learning_Knowledge/Quantum_Computing/TASKS.md",
        "file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/TASKS.md",
    ]
    for el in expected_links:
        assert el in content, f"ACTIVE_LEARNING.md missing direct link to: {el}"
