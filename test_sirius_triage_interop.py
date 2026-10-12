"""
Interop tests: pick_today.py honours task-triage decisions recorded by Sirius in .sirius/triage.json.

Covers the derived-file contract (superseded / parked / snoozed until a date), tolerance of a missing or malformed
file, the --no-triage switch, dedupe across boards, and the roulette / sentinel output. Every test builds its own
tiny workspace under tmp_path and passes an explicit `now`; nothing touches the real workspace or the network.
Zero emoji policy strictly enforced.
"""

import inspect
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import pytest

WORKSPACE_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(WORKSPACE_ROOT))

import pick_today

NOW = datetime(2026, 10, 12, 9, 0, 0)

# The Alpha title is longer than 30 characters on purpose: the generic "short prefix:" stripper in
# normalize_task_desc cannot remove it, so matching the watchlist copy needs the project titles (known_prefixes).
ALPHA_NAME = "Alpha Course for Applied Statistics"
ALPHA = f"1. {ALPHA_NAME}"
BETA = "2. Beta Lab"
PREFIXES = [ALPHA, BETA, ALPHA_NAME, "Beta Lab"]

V1_DEADLINE = "2026-09-26 23:59"        # overdue at NOW: belongs to the plan that was replaced
V2_DEADLINE = "2026-11-15 21:00"        # the re-planned copy of the same task
URGENT_DEADLINE = "2026-10-12 21:00"    # 12 hours after NOW

V1_LINE = f"- [ ] [Deadline: {V1_DEADLINE}] [Priority: P1] Implement ridge regression from scratch"
V1_DONE = V1_LINE.replace("[ ]", "[x]", 1)
V2_LINE = f"- [ ] [Deadline: {V2_DEADLINE}] [Priority: P1] Implement ridge regression from scratch"
URGENT_LINE = f"- [ ] [Deadline: {URGENT_DEADLINE}] [Priority: P1] Submit the week 1 report"
UNSCHEDULED_LINE = "- [ ] Tidy the reference notes"
WATCHLIST_LINE = (
    f"- [ ] [Deadline: {V1_DEADLINE}] [Priority: P1] {ALPHA_NAME}: Implement ridge regression from scratch."
)
VIETNAMESE_LINE = (
    "- [ ] [Deadline: 2026-09-27 23:59] [Priority: P1] "
    "Cài đặt Decision Tree Classifier và phân tích Gini Impurity"
)

ACTIVE_LEARNING_MD = """\
# Active Learning Hub

## Today's Dynamic Goal
- Date: 2026-10-12
- Subject: Alpha Course
- Target: Re-plan the regression track
- Definition of Done (DoD): v2 tasks listed
- Status: In Progress
- Deadline: 2026-10-17 23:59
- Priority: P2

## Active Priority Watchlist & Deadlines
{watchlist}

## Active Projects

### {alpha}
- Directory: Alpha_Course
- Tasks: Alpha_Course/TASKS.md
- Milestone: Finish the regression track.
- Checkpoint: Plan v2 replaced the v1 schedule.
- Next Action: Start week 1.
- Deadline: 2026-10-30 21:00
- Priority: P1

### {beta}
- Directory: Beta_Lab
- Tasks: Beta_Lab/TASKS.md
- Milestone: Ship the lab.
- Checkpoint: Draft written.
- Next Action: Polish the draft.
- Deadline: 2026-10-12 21:00
- Priority: P1
"""


class FrozenDatetime(datetime):
    """datetime whose now() is pinned to NOW, so main() is deterministic."""

    @classmethod
    def now(cls, tz=None):
        return cls(NOW.year, NOW.month, NOW.day, NOW.hour, NOW.minute, NOW.second)


def notice(count: int) -> str:
    """The one-line summary pick_today prints when Sirius triage hides tasks."""
    return f"Triaged by Sirius (excluded from deadline alerts): {count} task(s) - see .sirius/triage.json"


def make_workspace(tmp_path, alpha_lines=(V1_LINE, V2_LINE), beta_lines=(URGENT_LINE,), watchlist=(WATCHLIST_LINE,)):
    """Tiny workspace: ACTIVE_LEARNING.md plus one TASKS.md board per project. Returns the workspace root."""
    ws = tmp_path / "workspace"
    ws.mkdir()
    (ws / "ACTIVE_LEARNING.md").write_text(
        ACTIVE_LEARNING_MD.format(watchlist="\n".join(watchlist), alpha=ALPHA, beta=BETA), encoding="utf-8"
    )
    for folder, lines in (("Alpha_Course", alpha_lines), ("Beta_Lab", beta_lines)):
        (ws / folder).mkdir()
        (ws / folder / "TASKS.md").write_text(f"# {folder} tasks\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return ws


def triage_entry(raw, decision="superseded", **extra):
    """One entry in the shape Sirius writes (see the .sirius/triage.json contract)."""
    entry = {
        "taskId": "0123456789",
        "file": "Alpha_Course/TASKS.md",
        "line": 3,
        "raw": raw,
        "deadlineRaw": V1_DEADLINE,
        "text": "Implement ridge regression from scratch",
        "decision": decision,
        "at": "2026-10-11T20:00:00",
    }
    entry.update(extra)
    return entry


def write_json(path, entries, **top_level):
    document = {"v": 1, "updated": "2026-10-11T20:00:00", "entries": entries}
    document.update(top_level)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, ensure_ascii=False), encoding="utf-8")
    return path


def write_triage(ws, entries, **top_level):
    """Write <ws>/.sirius/triage.json."""
    return write_json(ws / ".sirius" / "triage.json", entries, **top_level)


def load(ws, **kwargs):
    """(projects, tasks) for a workspace, with an explicit clock."""
    active = ws / "ACTIVE_LEARNING.md"
    _, projects = pick_today.parse_active_learning(active)
    return projects, pick_today.collect_all_tasks(active, projects, NOW, base_dir=ws, **kwargs)


def by_deadline(tasks, deadline):
    found = [t for t in tasks if t["deadline_str"] == deadline]
    assert len(found) == 1, f"expected exactly one task due {deadline}, found {len(found)}"
    return found[0]


def run_cli(monkeypatch, capsys, ws, *flags):
    """Run pick_today.main() against a workspace with a frozen clock, a fixed roulette pick, and no spinner."""
    monkeypatch.setattr(pick_today, "SCRIPT_DIR", ws)
    monkeypatch.setattr(pick_today, "INDEX_FILE", ws / "INDEX.md")
    monkeypatch.setattr(pick_today, "ACTIVE_FILE", ws / "ACTIVE_LEARNING.md")
    monkeypatch.setattr(pick_today, "CENTRAL_TASKS_FILE", ws / "TASKS.md")
    monkeypatch.setattr(pick_today, "TRIAGE_FILE", ws / ".sirius" / "triage.json")
    monkeypatch.setattr(pick_today, "datetime", FrozenDatetime)
    monkeypatch.setattr(pick_today, "display_spinner", lambda projects: None)
    monkeypatch.setattr(pick_today.secrets, "choice", lambda seq: seq[0])
    monkeypatch.setattr(sys, "argv", ["pick_today.py", *flags])
    capsys.readouterr()
    pick_today.main()
    return capsys.readouterr().out


# --------------------------------------------------------------------------- (a) no triage file: unchanged behaviour

def test_without_triage_file_overdue_task_stays_urgent_and_locks_selection(tmp_path):
    ws = make_workspace(tmp_path)
    projects, tasks = load(ws)

    v1 = by_deadline(tasks, V1_DEADLINE)
    assert v1["category"] == "overdue"
    assert "triaged" not in v1
    assert not pick_today.is_triaged(v1)

    urgent = pick_today.select_urgent_tasks(tasks)
    assert [t["deadline_str"] for t in urgent] == [V1_DEADLINE, URGENT_DEADLINE]
    assert pick_today.match_task_to_project(urgent[0], projects)["title"] == ALPHA
    assert not (ws / ".sirius").exists(), "reading must never create the .sirius folder"


# --------------------------------------------------------------------------- (b) superseded / parked

@pytest.mark.parametrize("decision", ["superseded", "parked"])
def test_triaged_task_leaves_alerts_and_selection(tmp_path, capsys, decision):
    ws = make_workspace(tmp_path)
    write_triage(ws, [triage_entry(V1_LINE, decision, replacedBy="a1b2c3d4e5", note="plan v2 of 2026-10-10")])
    projects, tasks = load(ws)

    v1 = by_deadline(tasks, V1_DEADLINE)
    assert v1["triaged"] == decision
    assert pick_today.is_triaged(v1)
    # Only a flag is added: classification and every other field are kept.
    assert v1["category"] == "overdue" and v1["remaining_hours"] < 0 and v1["priority"] == "P1"
    # The re-planned copy (same description, new deadline) and the urgent task are different tasks.
    assert "triaged" not in by_deadline(tasks, V2_DEADLINE)
    assert "triaged" not in by_deadline(tasks, URGENT_DEADLINE)

    urgent = pick_today.select_urgent_tasks(tasks)
    assert [t["deadline_str"] for t in urgent] == [URGENT_DEADLINE]
    assert pick_today.match_task_to_project(urgent[0], projects)["title"] == BETA

    pick_today.print_sentinel_report(tasks, NOW)
    out = capsys.readouterr().out
    assert V1_DEADLINE not in out and "OVERDUE" not in out
    assert "[CRITICAL (< 24H) - IMMEDIATE ACTION] (1 items):" in out
    assert notice(1) in out


def test_triage_also_hides_upcoming_and_unscheduled_tasks(tmp_path, capsys):
    ws = make_workspace(tmp_path, alpha_lines=(V1_LINE, V2_LINE, UNSCHEDULED_LINE))
    write_triage(ws, [triage_entry(V2_LINE, "parked"), triage_entry(UNSCHEDULED_LINE, "parked")])
    _, tasks = load(ws)

    pick_today.print_sentinel_report(tasks, NOW)
    out = capsys.readouterr().out

    assert "UPCOMING" not in out and "UNSCHEDULED" not in out
    assert "[OVERDUE - BLOCKERS] (1 items):" in out      # the v1 task is not triaged in this scenario
    assert notice(2) in out


# --------------------------------------------------------------------------- (c) snoozed

@pytest.mark.parametrize(
    "until, now, excluded",
    [
        ("2026-10-11", datetime(2026, 10, 12, 9, 0, 0), False),     # snooze ended yesterday
        ("2026-10-12", datetime(2026, 10, 12, 9, 0, 0), True),      # last snoozed day is today
        ("2026-10-12", datetime(2026, 10, 12, 23, 59, 59), True),   # still today at the last second
        ("2026-10-12", datetime(2026, 10, 13, 0, 0, 0), False),     # flips at local midnight
        ("2026-12-31", datetime(2026, 10, 12, 9, 0, 0), True),      # snoozed for weeks
    ],
)
def test_snooze_lasts_through_the_until_date(tmp_path, until, now, excluded):
    path = write_json(tmp_path / "triage.json", [triage_entry(V1_LINE, "snoozed", until=until)])
    assert bool(pick_today.load_triage_exclusions(path, PREFIXES, now)) is excluded


def test_expired_snooze_keeps_task_urgent_while_active_snooze_hides_it(tmp_path):
    ws = make_workspace(tmp_path)

    write_triage(ws, [triage_entry(V1_LINE, "snoozed", until="2026-10-11")])
    _, tasks = load(ws)
    assert "triaged" not in by_deadline(tasks, V1_DEADLINE)
    assert pick_today.select_urgent_tasks(tasks)[0]["deadline_str"] == V1_DEADLINE

    write_triage(ws, [triage_entry(V1_LINE, "snoozed", until="2026-10-12")])
    _, tasks = load(ws)
    assert by_deadline(tasks, V1_DEADLINE)["triaged"] == "snoozed"
    assert [t["deadline_str"] for t in pick_today.select_urgent_tasks(tasks)] == [URGENT_DEADLINE]


# --------------------------------------------------------------------------- (d) malformed input never crashes

@pytest.mark.parametrize(
    "payload",
    [
        b"",
        b"{not json",
        b"[]",
        b"null",
        b"42",
        b'"text"',
        b'{"v": 1}',
        b'{"v": 1, "entries": null}',
        b'{"v": 1, "entries": {"a": 1}}',
        b"\xff\xfe\x00 not utf-8",
    ],
)
def test_unusable_file_yields_no_exclusions(tmp_path, payload):
    path = tmp_path / "triage.json"
    path.write_bytes(payload)
    assert pick_today.load_triage_exclusions(path, PREFIXES, NOW) == {}


def test_missing_file_or_directory_yields_no_exclusions(tmp_path):
    assert pick_today.load_triage_exclusions(tmp_path / "absent.json", PREFIXES, NOW) == {}
    (tmp_path / "folder.json").mkdir()
    assert pick_today.load_triage_exclusions(tmp_path / "folder.json", PREFIXES, NOW) == {}


ABSENT = object()


@pytest.mark.parametrize(
    "version",
    [0, 2, "1", True, None, [1], pytest.param(ABSENT, id="absent")],
)
def test_wrong_schema_version_is_ignored(tmp_path, version):
    document = {"entries": [triage_entry(V1_LINE)]}
    if version is not ABSENT:
        document["v"] = version
    path = tmp_path / "triage.json"
    path.write_text(json.dumps(document), encoding="utf-8")
    assert pick_today.load_triage_exclusions(path, PREFIXES, NOW) == {}


def test_malformed_entries_are_skipped_and_valid_ones_kept(tmp_path):
    entries = [
        None,
        "text",
        42,
        ["raw"],
        {"decision": "superseded"},                                    # no raw line
        {"raw": 5, "decision": "parked"},                              # raw is not a string
        {"raw": "## not a task line", "decision": "parked"},           # raw does not parse as a task
        {"raw": V1_LINE},                                              # no decision
        {"raw": V1_LINE, "decision": "done"},                          # unknown decision
        {"raw": V1_LINE, "decision": ["parked"]},                      # decision of the wrong type
        {"raw": V1_LINE, "decision": "snoozed"},                       # snooze without until
        {"raw": V1_LINE, "decision": "snoozed", "until": "soon"},      # until that is not a date
        {"raw": V1_LINE, "decision": "snoozed", "until": 20261231},    # until of the wrong type
        triage_entry(V2_LINE, "parked"),                               # the only usable entry
    ]
    path = write_json(tmp_path / "triage.json", entries)

    result = pick_today.load_triage_exclusions(path, PREFIXES, NOW)

    assert len(result) == 1
    (key, entry), = result.items()
    assert key[1] == V2_DEADLINE
    assert entry["decision"] == "parked"


def test_unexpected_error_on_one_entry_skips_only_that_entry(tmp_path, monkeypatch):
    path = write_json(tmp_path / "triage.json", [triage_entry(V1_LINE), triage_entry(V2_LINE, "parked")])
    real_parse = pick_today.parse_task_line

    def flaky_parse(line, *args, **kwargs):
        if V1_DEADLINE in line:
            raise RuntimeError("simulated parser failure")
        return real_parse(line, *args, **kwargs)

    monkeypatch.setattr(pick_today, "parse_task_line", flaky_parse)

    result = pick_today.load_triage_exclusions(path, PREFIXES, NOW)

    assert [key[1] for key in result] == [V2_DEADLINE]


@pytest.mark.parametrize(
    "content",
    ["{not json", '{"v": 1, "entries": [null, 3, {"raw": 1}, {"raw": "x", "decision": "parked"}]}'],
    ids=["invalid-json", "junk-entries"],
)
def test_garbage_triage_file_leaves_collection_unchanged(tmp_path, content):
    ws = make_workspace(tmp_path)
    (ws / ".sirius").mkdir()
    (ws / ".sirius" / "triage.json").write_text(content, encoding="utf-8")

    _, with_file = load(ws)
    _, without_file = load(ws, use_triage=False)

    assert with_file == without_file
    assert all("triaged" not in t for t in with_file)


def test_utf8_bom_is_tolerated(tmp_path):
    path = tmp_path / "triage.json"
    body = json.dumps({"v": 1, "entries": [triage_entry(V1_LINE)]})
    path.write_bytes(b"\xef\xbb\xbf" + body.encode("utf-8"))
    assert len(pick_today.load_triage_exclusions(path, PREFIXES, NOW)) == 1


@pytest.mark.parametrize("ensure_ascii", [True, False], ids=["escaped-unicode", "raw-utf8"])
def test_vietnamese_task_line_matches_through_json(tmp_path, ensure_ascii):
    ws = make_workspace(tmp_path, alpha_lines=(V1_LINE, V2_LINE, VIETNAMESE_LINE))
    path = ws / ".sirius" / "triage.json"
    path.parent.mkdir()
    document = {"v": 1, "updated": "2026-10-11T20:00:00", "entries": [triage_entry(VIETNAMESE_LINE)]}
    path.write_text(json.dumps(document, ensure_ascii=ensure_ascii), encoding="utf-8")

    _, tasks = load(ws)

    assert by_deadline(tasks, "2026-09-27 23:59")["triaged"] == "superseded"
    assert sum(1 for t in tasks if "triaged" in t) == 1


# --------------------------------------------------------------------------- (e) --no-triage / use_triage=False

def test_use_triage_false_ignores_a_valid_file(tmp_path):
    ws = make_workspace(tmp_path)
    write_triage(ws, [triage_entry(V1_LINE)])

    _, tasks = load(ws, use_triage=False)

    assert all("triaged" not in t for t in tasks)
    assert [t["deadline_str"] for t in pick_today.select_urgent_tasks(tasks)] == [V1_DEADLINE, URGENT_DEADLINE]


# --------------------------------------------------------------------------- (f) dedupe still works

@pytest.mark.parametrize("raw", [V1_LINE, WATCHLIST_LINE], ids=["board-line", "watchlist-line"])
def test_one_entry_excludes_every_deduplicated_copy(tmp_path, raw):
    ws = make_workspace(tmp_path)
    assert WATCHLIST_LINE in (ws / "ACTIVE_LEARNING.md").read_text(encoding="utf-8")   # copy 1: watchlist
    assert V1_LINE in (ws / "Alpha_Course" / "TASKS.md").read_text(encoding="utf-8")   # copy 2: project board
    write_triage(ws, [triage_entry(raw)])

    _, tasks = load(ws)
    _, untriaged = load(ws, use_triage=False)

    copies = [t for t in tasks if t["deadline_str"] == V1_DEADLINE]
    assert len(copies) == 1, "dedupe must still merge the watchlist and board copies"
    assert copies[0]["source"] == ALPHA
    assert copies[0]["triaged"] == "superseded"
    assert len(tasks) == len(untriaged), "triage flags tasks, it never drops or adds any"
    assert [t["triaged"] for t in tasks if "triaged" in t] == ["superseded"]


def test_watchlist_only_task_is_excluded(tmp_path):
    ws = make_workspace(tmp_path, alpha_lines=(V2_LINE,))
    write_triage(ws, [triage_entry(V1_LINE)])

    _, tasks = load(ws)

    watchlist_copy = by_deadline(tasks, V1_DEADLINE)
    assert watchlist_copy["source"] == ALPHA
    assert watchlist_copy["triaged"] == "superseded"


def test_exclusion_key_is_the_live_dedupe_key(tmp_path):
    ws = make_workspace(tmp_path)
    _, projects = pick_today.parse_active_learning(ws / "ACTIVE_LEARNING.md")
    prefixes = [p["title"] for p in projects] + [re.sub(r"^\d+\.\s*", "", p["title"]) for p in projects]
    path = write_triage(ws, [triage_entry(WATCHLIST_LINE)])

    (key,) = pick_today.load_triage_exclusions(path, prefixes, NOW)

    live = pick_today.parse_task_line(V1_LINE, ALPHA, NOW)
    assert key == pick_today.task_key(live, prefixes)
    assert key[1] == V1_DEADLINE


def test_duplicate_entries_for_one_task_collapse_to_the_first(tmp_path):
    entries = [triage_entry(V1_LINE, "superseded"), triage_entry(WATCHLIST_LINE, "parked")]
    path = write_json(tmp_path / "triage.json", entries)

    result = pick_today.load_triage_exclusions(path, PREFIXES, NOW)

    assert len(result) == 1
    assert next(iter(result.values()))["decision"] == "superseded"


def test_completed_task_is_never_treated_as_triaged(tmp_path, capsys):
    ws = make_workspace(tmp_path, alpha_lines=(V1_DONE, V2_LINE), watchlist=())
    write_triage(ws, [triage_entry(V1_LINE)])   # the key ignores the checkbox state

    _, tasks = load(ws)

    done = by_deadline(tasks, V1_DEADLINE)
    assert done["is_completed"] and not pick_today.is_triaged(done)
    pick_today.print_sentinel_report(tasks, NOW)
    out = capsys.readouterr().out
    assert "Triaged by Sirius" not in out
    assert "[COMPLETED MILESTONES] (1 items verified)" in out


# --------------------------------------------------------------------------- command line: roulette and sentinel

def test_cli_without_triage_file_locks_subject_to_the_overdue_task(monkeypatch, capsys, tmp_path):
    ws = make_workspace(tmp_path)

    out = run_cli(monkeypatch, capsys, ws)

    assert "[URGENT DEADLINE SENTINEL: 2 TASK(S) DUE WITHIN 48 HOURS]" in out
    assert f"Study focus locked to: {ALPHA}" in out
    assert V1_DEADLINE in out
    assert "Triaged by Sirius" not in out


def test_cli_skips_triaged_task_and_locks_the_next_urgent_one(monkeypatch, capsys, tmp_path):
    ws = make_workspace(tmp_path)
    write_triage(ws, [triage_entry(V1_LINE)])

    out = run_cli(monkeypatch, capsys, ws)

    assert "[URGENT DEADLINE SENTINEL: 1 TASK(S) DUE WITHIN 48 HOURS]" in out
    assert f"Study focus locked to: {BETA}" in out
    assert "Submit the week 1 report" in out
    assert V1_DEADLINE not in out and "OVERDUE" not in out
    assert out.count(notice(1)) == 1


def test_cli_with_every_urgent_task_triaged_falls_back_to_the_roulette(monkeypatch, capsys, tmp_path):
    ws = make_workspace(tmp_path)
    write_triage(ws, [triage_entry(V1_LINE), triage_entry(URGENT_LINE, "parked")])

    out = run_cli(monkeypatch, capsys, ws)

    assert "URGENT DEADLINE SENTINEL" not in out and "AUTOMATIC PRIORITY OVERRIDE" not in out
    assert "Submit the week 1 report" not in out and "OVERDUE" not in out
    assert f"Topic       : {ALPHA}" in out    # secrets.choice is pinned to the first project
    assert out.count(notice(2)) == 1


@pytest.mark.parametrize("flag", ["--sentinel", "--check"])
def test_cli_sentinel_mode_hides_triaged_tasks_and_prints_the_count(monkeypatch, capsys, tmp_path, flag):
    ws = make_workspace(tmp_path)
    before = run_cli(monkeypatch, capsys, ws, flag)
    assert "[OVERDUE - BLOCKERS] (1 items):" in before and "Triaged by Sirius" not in before

    write_triage(ws, [triage_entry(V1_LINE)])
    after = run_cli(monkeypatch, capsys, ws, flag)

    assert "OVERDUE" not in after and V1_DEADLINE not in after
    assert "[CRITICAL (< 24H) - IMMEDIATE ACTION] (1 items):" in after
    assert "[UPCOMING (> 72H) - ON TRACK] (1 items):" in after    # the re-planned copy stays visible
    assert after.count(notice(1)) == 1


@pytest.mark.parametrize("flags", [(), ("--sentinel",)], ids=["roulette", "sentinel"])
def test_cli_no_triage_flag_restores_the_previous_output(monkeypatch, capsys, tmp_path, flags):
    ws = make_workspace(tmp_path)
    reference = run_cli(monkeypatch, capsys, ws, *flags)          # no triage file yet
    write_triage(ws, [triage_entry(V1_LINE)])

    honoured = run_cli(monkeypatch, capsys, ws, *flags)
    disabled = run_cli(monkeypatch, capsys, ws, *flags, "--no-triage")

    assert honoured != reference
    assert disabled == reference


def test_new_parameters_are_optional_and_default_to_the_previous_behaviour():
    params = inspect.signature(pick_today.collect_all_tasks).parameters
    assert list(params)[:3] == ["active_file", "projects", "now"]
    assert params["base_dir"].default is None and params["use_triage"].default is True
    assert list(inspect.signature(pick_today.load_triage_exclusions).parameters)[:3] == [
        "path", "known_prefixes", "now",
    ]
    assert pick_today.TRIAGE_FILE == pick_today.SCRIPT_DIR / ".sirius" / "triage.json"
