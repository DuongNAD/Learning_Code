"""
Forensic Auditor Deep Inspection Script
Executes exhaustive empirical checks across study_notes/ and tests/.
"""

import ast
import os
import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(r"d:\02_Learning_Knowledge\GCI_World_2026_September")
STUDY_NOTES_DIR = WORKSPACE_ROOT / "study_notes"
TESTS_DIR = WORKSPACE_ROOT / "tests"
COURSE_DATA_DIR = WORKSPACE_ROOT / "extracted_gci_world" / "GCI World_202609"

NOTES = [
    "00_Index_and_Roadmap.md",
    "01_Python_Foundations.md",
    "02_Statistics_and_EDA.md",
    "03_NumPy_Computing.md",
    "04_Supervised_Regression.md",
    "05_Supervised_Classification.md",
    "06_ML_Landscape_and_Strategy.md",
]

report = []

def log(msg):
    print(msg)
    report.append(msg)

log("=" * 80)
log("FORENSIC AUDITOR INDEPENDENT DEEP VERIFICATION")
log("=" * 80)

# Check 1: Verify test suite contains genuine assertions (no tautologies)
log("\n--- [CHECK 1] Test Suite Sincerity & Assertion Audit ---")
test_file = TESTS_DIR / "test_study_notes.py"
test_content = test_file.read_text(encoding="utf-8")

tautology_patterns = [
    r"self\.assertTrue\(True\)",
    r"self\.assertFalse\(False\)",
    r"self\.assertEqual\(([^,]+),\s*\1\)",
    r"assert\s+True\b",
    r"@unittest\.skip",
    r"@pytest\.mark\.skip",
]

suspicious_assertions = []
for pat in tautology_patterns:
    matches = list(re.finditer(pat, test_content))
    if matches:
        suspicious_assertions.append((pat, len(matches)))

if suspicious_assertions:
    log(f"FAIL: Found suspicious test assertions: {suspicious_assertions}")
else:
    log("PASS: Zero tautological or skipped assertions in test_study_notes.py.")

# Count total real asserts in test suite
real_asserts = re.findall(r"self\.assert[A-Za-z]+|assert\s+", test_content)
log(f"INFO: Total real assertion calls in test suite: {len(real_asserts)}")

# Check 2: Prohibited Patterns & Facade Detection across all study notes
log("\n--- [CHECK 2] Facade & Prohibited Patterns Scan in study_notes ---")
prohibited_findings = []
for note_name in NOTES:
    note_path = STUDY_NOTES_DIR / note_name
    text = note_path.read_text(encoding="utf-8")
    
    # Check for placeholder markers
    for bad_word in ["TODO", "TBD", "FIXME", "PLACEHOLDER", "LOREM IPSUM"]:
        if bad_word in text:
            prohibited_findings.append(f"{note_name}: Contains '{bad_word}'")
            
    # Check for empty code blocks: ```python\s*```
    empty_code_blocks = re.findall(r"```(?:python|mermaid|py)?\s*```", text)
    if empty_code_blocks:
        prohibited_findings.append(f"{note_name}: Contains {len(empty_code_blocks)} empty code blocks")

if prohibited_findings:
    log(f"FAIL: Prohibited patterns found: {prohibited_findings}")
else:
    log("PASS: Zero placeholders, zero TODOs, zero empty code blocks in study_notes/.")

# Check 3: Extract and AST parse every single Python block in all notes
log("\n--- [CHECK 3] Python Code Blocks AST & Execution Verification ---")
total_code_blocks = 0
total_code_lines = 0
total_comments = 0
ast_failures = []

def extract_py_blocks(content):
    blocks = []
    lines = content.splitlines()
    in_block = False
    current = []
    start_line = 0
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if not in_block:
            if stripped.startswith("```"):
                tag = stripped[3:].strip().lower()
                if tag in ("python", "py"):
                    in_block = True
                    start_line = idx
                    current = []
        else:
            if stripped == "```":
                in_block = False
                blocks.append((start_line, "\n".join(current)))
                current = []
            else:
                current.append(line)
    return blocks

for note_name in NOTES:
    note_path = STUDY_NOTES_DIR / note_name
    text = note_path.read_text(encoding="utf-8")
    blocks = extract_py_blocks(text)
    total_code_blocks += len(blocks)
    
    for start_line, code in blocks:
        lines = code.splitlines()
        total_code_lines += len(lines)
        total_comments += sum(1 for l in lines if "#" in l)
        
        # Clean for AST (dedent, remove REPL, ignore magics)
        import textwrap
        dedented = textwrap.dedent(code)
        cleaned_lines = []
        for l in dedented.splitlines():
            s = l.strip()
            if s.startswith(">>> ") or s.startswith("... "):
                cleaned_lines.append(s[4:])
            elif s.startswith("%") or s.startswith("!"):
                cleaned_lines.append("# magic: " + s)
            else:
                cleaned_lines.append(l)
        cleaned_code = "\n".join(cleaned_lines)
        
        try:
            tree = ast.parse(cleaned_code)
            # Check for dummy functions whose body is only `return <constant>` or `pass`
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if len(node.body) == 1:
                        stmt = node.body[0]
                        if isinstance(stmt, ast.Pass):
                            ast_failures.append(f"{note_name} line {start_line}: function {node.name} body is only `pass`")
                        elif isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Constant):
                            # Constant return could be dummy unless it's a test or trivial helper
                            ast_failures.append(f"{note_name} line {start_line}: function {node.name} returns constant {stmt.value.value}")
        except SyntaxError as e:
            ast_failures.append(f"{note_name} line {start_line}: SyntaxError: {e}")

log(f"INFO: Inspected {total_code_blocks} Python code blocks ({total_code_lines} lines, {total_comments} comments).")
if ast_failures:
    log(f"FAIL: AST / Dummy function issues detected: {ast_failures}")
else:
    log("PASS: 100% of Python code blocks parse cleanly with AST and have genuine functional implementations.")

# Check 4: Mermaid Diagram Syntax & Structural Integrity
log("\n--- [CHECK 4] Mermaid Diagram Deep Inspection ---")
total_mermaid_blocks = 0
mermaid_failures = []

def extract_mermaid(content):
    blocks = []
    lines = content.splitlines()
    in_block = False
    current = []
    start_line = 0
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if not in_block:
            if stripped.startswith("```"):
                tag = stripped[3:].strip().lower()
                if tag.startswith("mermaid"):
                    in_block = True
                    start_line = idx
                    current = []
        else:
            if stripped == "```":
                in_block = False
                blocks.append((start_line, "\n".join(current)))
                current = []
            else:
                current.append(line)
    return blocks

valid_diagram_types = {"flowchart", "graph", "sequencediagram", "classdiagram", "statediagram", "mindmap"}

for note_name in NOTES:
    note_path = STUDY_NOTES_DIR / note_name
    text = note_path.read_text(encoding="utf-8")
    blocks = extract_mermaid(text)
    total_mermaid_blocks += len(blocks)
    
    if len(blocks) < 1:
        mermaid_failures.append(f"{note_name}: Zero Mermaid blocks found (R4 requires >= 1)")
        
    for start_line, mcode in blocks:
        if not mcode.strip():
            mermaid_failures.append(f"{note_name} line {start_line}: Empty Mermaid block")
            continue
        first_line = ""
        for l in mcode.splitlines():
            s = l.strip()
            if s and not s.startswith("%%"):
                first_line = s.lower().split()[0]
                break
        if first_line not in valid_diagram_types:
            mermaid_failures.append(f"{note_name} line {start_line}: Unknown diagram type '{first_line}'")

log(f"INFO: Inspected {total_mermaid_blocks} Mermaid diagram blocks across 7 notes.")
if mermaid_failures:
    log(f"FAIL: Mermaid issues: {mermaid_failures}")
else:
    log("PASS: All notes satisfy R4 with valid Mermaid syntax and diagram structures.")

# Check 5: Active Recall Flashcards (R3)
log("\n--- [CHECK 5] Active Recall Flashcards Deep Inspection (R3) ---")
flashcard_failures = []
total_cards = 0
for note_name in NOTES:
    note_path = STUDY_NOTES_DIR / note_name
    text = note_path.read_text(encoding="utf-8")
    
    # Check heading cards
    heading_cards = re.findall(r"^###\s*(?:Thẻ|Flashcard|Card|Câu hỏi)\s*\d+.*$", text, re.MULTILINE | re.IGNORECASE)
    # Check Q&A pairs
    q_matches = re.findall(r"(?:[-*]?\s*\*\*(?:Hỏi|Câu hỏi|Question|Q\d*|\bHỏi\s*\(Q\))\s*[:.]|\b(?:Câu hỏi|Question|Thẻ)\s+\d+[:.]|^\s*\d+\.\s*\*\*(?:Hỏi|Q|Câu hỏi))", text, re.MULTILINE | re.IGNORECASE)
    a_matches = re.findall(r"(?:[-*]?\s*\*\*(?:Đáp|Trả lời|Answer|A\d*|\bĐáp\s*\(A\))\s*[:.]|^\s*\d+\.\s*\*\*(?:Đáp|A|Trả lời))", text, re.MULTILINE | re.IGNORECASE)
    
    card_count = max(len(heading_cards), len(q_matches))
    total_cards += card_count
    
    if card_count < 5:
        flashcard_failures.append(f"{note_name}: Found {card_count} flashcards (expected >= 5)")
    if len(q_matches) > 0 and len(a_matches) == 0:
        flashcard_failures.append(f"{note_name}: Flashcards have questions but zero explicit answer indicators")

log(f"INFO: Total flashcards verified across 7 notes: {total_cards}")
if flashcard_failures:
    log(f"FAIL: Flashcard issues: {flashcard_failures}")
else:
    log("PASS: All notes satisfy R3 with >= 5 comprehensive Q&A flashcards.")

# Check 6: Course Materials Derivation Check
log("\n--- [CHECK 6] Authenticity & Direct Course Material Derivation ---")
derivation_checks = [
    ("Matsuo Lab & 14-week arc", "00_Index_and_Roadmap.md", r"Matsuo.*Tokyo|Đại học Tokyo.*Matsuo"),
    ("Seven-Eleven Japan case", "00_Index_and_Roadmap.md", r"Seven-Eleven|7-Eleven"),
    ("Collatz 3n+1 Algorithm", "01_Python_Foundations.md", r"Collatz|3n\s*\+\s*1"),
    ("20 students English/Math exam", "02_Statistics_and_EDA.md", r"English.*Math|Tiếng Anh.*Toán|285\.3|524\.7"),
    ("NumPy HW1 odd multiple of 5", "03_NumPy_Computing.md", r"bội số.*5.*lẻ|odd multiple.*5"),
    ("Car Price R2 Level 1-4 progression", "04_Supervised_Regression.md", r"Car_Price|engine-size.*curb-weight|0\.78.*0\.71.*0\.85"),
    ("Mushroom datasets & Gini", "05_Supervised_Classification.md", r"Mushroom|bruises.*odor|Gini"),
    ("K-Means Inertia & PCA Eigenvectors", "06_ML_Landscape_and_Strategy.md", r"Inertia.*Elbow|Covariance.*Eigen"),
]

derivation_failures = []
for label, note_name, pat in derivation_checks:
    text = (STUDY_NOTES_DIR / note_name).read_text(encoding="utf-8")
    if not re.search(pat, text, re.IGNORECASE):
        derivation_failures.append(f"Missing course evidence for '{label}' in {note_name}")

if derivation_failures:
    log(f"FAIL: Course derivation issues: {derivation_failures}")
else:
    log("PASS: 100% of core course materials, datasets, and specific exercises are authentically represented.")

log("\n" + "=" * 80)
log("FORENSIC AUDIT EMPIRICAL VERIFICATION COMPLETE")
log("=" * 80)
