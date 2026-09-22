"""
Automated E2E Verification Test Suite for GCI World 202609 Course Study Notes.
Authoritative Specifications: ORIGINAL_REQUEST.md & PROJECT.md (orchestrator_1)

Test Organization:
- Tier 1: Existence and Non-Emptiness of all 7 study notes in `study_notes/`.
- Tier 2: Structural and Formatting Constraints per R1-R4:
          Section headers, Mermaid diagrams (>= 1),
          Active Recall Flashcards (>= 5 Q&A),
          Python code blocks with '#' inline comments,
          Minimum length (>= 2000 chars).
- Tier 3: Syntax Correctness:
          Mermaid diagram headers and non-emptiness;
          Python code snippet AST validity.
- Tier 4: Academic Concept & Feature Coverage (F01 - F32 from PROJECT.md).

Execution:
    pytest -v tests/test_study_notes.py
or:
    python tests/test_study_notes.py
or:
    python tests/run_tests.py
"""

import ast
import re
import textwrap
import unittest
from pathlib import Path
from typing import Dict, List, Tuple

# Workspace paths
TESTS_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = TESTS_DIR.parent
STUDY_NOTES_DIR = WORKSPACE_ROOT / "study_notes"

EXPECTED_FILES = [
    "00_Index_and_Roadmap.md",
    "01_Python_Foundations.md",
    "02_Statistics_and_EDA.md",
    "03_NumPy_Computing.md",
    "04_Supervised_Regression.md",
    "05_Supervised_Classification.md",
    "06_ML_Landscape_and_Strategy.md",
]

TOPIC_NOTE_FILES = [
    "01_Python_Foundations.md",
    "02_Statistics_and_EDA.md",
    "03_NumPy_Computing.md",
    "04_Supervised_Regression.md",
    "05_Supervised_Classification.md",
    "06_ML_Landscape_and_Strategy.md",
]

VALID_MERMAID_TYPES = {
    "flowchart",
    "graph",
    "sequencediagram",
    "classdiagram",
    "classdiagram-v2",
    "statediagram",
    "statediagram-v2",
    "erdiagram",
    "journey",
    "gantt",
    "pie",
    "quadrantchart",
    "requirementdiagram",
    "gitgraph",
    "mindmap",
    "timeline",
    "zenuml",
    "sankey-beta",
    "block-beta",
    "packet-beta",
    "xychart-beta",
    "c4context",
    "architecture-beta",
}

# Concept coverage specifications per PROJECT.md Feature Inventory (F01-F32)
CONCEPT_SPECS: Dict[str, List[Tuple[str, List[str]]]] = {
    "00_Index_and_Roadmap.md": [
        ("Course Philosophy / Matsuo Lab", [
            r"matsuo", r"đại học tokyo", r"tokyo university", r"đông kinh"
        ]),
        ("14-Week Curriculum Arc", [
            r"14\s*(?:tuần|weeks?)", r"14-week"
        ]),
        ("4-Stage Data Science Cycle", [
            r"4\s*giai\s*đoạn", r"4-stage",
            r"chu\s*kỳ\s*khoa\s*học\s*dữ\s*liệu", r"data\s*science\s*cycle"
        ]),
        ("Link to 01_Python_Foundations", [r"01_Python_Foundations\.md"]),
        ("Link to 02_Statistics_and_EDA", [r"02_Statistics_and_EDA\.md"]),
        ("Link to 03_NumPy_Computing", [r"03_NumPy_Computing\.md"]),
        ("Link to 04_Supervised_Regression", [
            r"04_Supervised_Regression\.md"
        ]),
        ("Link to 05_Supervised_Classification", [
            r"05_Supervised_Classification\.md"
        ]),
        ("Link to 06_ML_Landscape_and_Strategy", [
            r"06_ML_Landscape_and_Strategy\.md"
        ]),
    ],
    "01_Python_Foundations.md": [
        ("F02: Python Computational Model / Mutability", [
            r"mutab", r"immutab", r"tham\s*chiếu", r"reference", r"bộ\s*nhớ"
        ]),
        ("F03: Control Flow & Collatz Algorithm", [
            r"collatz", r"3n\s*\+\s*1"
        ]),
        ("F04: Functions, Lambdas & Comprehensions", [
            r"comprehension", r"lambda", r"def\s+\w+"
        ]),
        ("F05: OOP Architecture", [
            r"class\s+\w+", r"__init__", r"self\."
        ]),
    ],
    "02_Statistics_and_EDA.md": [
        ("F06: Descriptive Statistics", [
            r"mean|trung\s*bình", r"median|trung\s*vị",
            r"variance|phương\s*sai",
            r"standard\s*deviation|độ\s*lệch\s*chuẩn"
        ]),
        ("F07: Standardization & Z-Score", [
            r"z-score", r"chuẩn\s*hóa", r"standardiz"
        ]),
        ("F08: Tukey 5-Number Summary & IQR Outliers", [
            r"box\s*plot|biểu\s*đồ\s*hộp", r"iqr|tứ\s*phân\s*vị",
            r"whisker|1\.5\s*\*?\s*iqr", r"outlier|ngoại\s*lai"
        ]),
        ("F09: Pearson Correlation Coefficient", [
            r"pearson", r"tương\s*quan", r"correlation"
        ]),
        ("F10: Statistical Traps & Dark Data", [
            r"dark\s*data|dữ\s*liệu\s*tối", r"causation|nhân\s*quả",
            r"selection\s*bias|thiên\s*vị\s*chọn\s*mẫu"
        ]),
    ],
    "03_NumPy_Computing.md": [
        ("F11: ndarray & C-Contiguous Memory Architecture", [
            r"ndarray", r"c-contiguous|contiguous|bộ\s*nhớ\s*liên\s*tục",
            r"simd|vectoriz"
        ]),
        ("F12: Broadcasting Alignment Rules", [
            r"broadcasting"
        ]),
        ("F13: 2D Slicing & Axis Semantics", [
            r"axis\s*=\s*0", r"axis\s*=\s*1", r"trục\s*0|trục\s*1"
        ]),
        ("F14: Boolean Masking & Copy vs View", [
            r"boolean\s*mask|mặt\s*nạ", r"copy.*view|view.*copy"
        ]),
        ("F15: Linear Algebra & Matrix Dot", [
            r"linalg|dot|@", r"inv", r"det", r"norm"
        ]),
        ("F16: HW1 Odd Multiple of 5 Array Filter", [
            r"bội\s*số\s*lẻ\s*của\s*5|odd\s*multiple.*5",
            r"5\s*và.*lẻ|hw1|session2"
        ]),
    ],
    "04_Supervised_Regression.md": [
        ("F17: Linear Regression & OLS Normal Equation", [
            r"linear\s*regression|hồi\s*quy\s*tuyến\s*tính",
            r"ols|ordinary\s*least\s*squares",
            r"phương\s*trình\s*chuẩn|normal\s*equation"
        ]),
        ("F18: Evaluation Metrics (MSE, RMSE, R-squared)", [
            r"mse", r"rmse", r"mae",
            r"r-squared|r\^2|r²|hệ\s*số\s*xác\s*định"
        ]),
        ("F19: Validation & K-Fold Cross-Validation", [
            r"train_test_split|holdout",
            r"k-fold|cross-validation|kiểm\s*định\s*chéo"
        ]),
        ("F20: Outlier Processing Strategies", [
            r"outlier|ngoại\s*lai", r"iqr|scatter"
        ]),
        ("F21: Feature Scaling & Data Leakage Prevention", [
            r"standardscaler|chuẩn\s*hóa|scale",
            r"leakage|rò\s*rỉ\s*dữ\s*liệu"
        ]),
    ],
    "05_Supervised_Classification.md": [
        ("F22: Decision Tree Architecture", [
            r"decision\s*tree|cây\s*quyết\s*định", r"root|internal|leaf|gốc|lá"
        ]),
        ("F23: Impurity Criteria (Gini, Entropy, Info Gain)", [
            r"gini", r"entropy",
            r"information\s*gain|độ\s*lợi\s*thông\s*tin"
        ]),
        ("F24: Pruning & Overfitting Mitigation", [
            r"max_depth", r"min_samples_split",
            r"pruning|tỉa\s*cành", r"overfitting|quá\s*khớp"
        ]),
        ("F25: Categorical Encoding & Dummy Variable Trap", [
            r"one-hot|onehot|get_dummies|onehotencoder",
            r"drop_first|dummy\s*variable\s*trap|đa\s*cộng\s*tuyến"
        ]),
        ("F26: Data Imputation Strategies", [
            r"imput|điền\s*khuyết", r"mode|yếu\s*vị", r"groupby"
        ]),
        ("F27: Relational Data Integration (pd.merge)", [
            r"pd\.merge|merge", r"isin|foreign\s*key"
        ]),
        ("F28: Classification Evaluation (Confusion Matrix, F1)", [
            r"confusion\s*matrix|ma\s*trận\s*nhầm\s*lẫn",
            r"accuracy|precision|recall|f1"
        ]),
    ],
    "06_ML_Landscape_and_Strategy.md": [
        ("F29: Unsupervised Clustering & K-Means", [
            r"k-means|kmeans", r"inertia", r"elbow|khuỷu\s*tay"
        ]),
        ("F30: Dimensionality Reduction & PCA", [
            r"pca|principal\s*component", r"covariance|hiệp\s*phương\s*sai",
            r"eigen|riêng",
            r"variance\s*ratio|phương\s*sai\s*giải\s*thích"
        ]),
        ("F31: Time Series & Foundation Models", [
            r"time\s*series|chuỗi\s*thời\s*gian",
            r"autocorrelation|tự\s*tương\s*quan",
            r"next\s*token|llm|transformer|self-supervised"
        ]),
        ("F32: Enterprise AI Strategy & Data Flywheel", [
            r"data\s*flywheel|bánh\s*đà\s*dữ\s*liệu",
            r"moat|hào\s*kinh\s*tế|lợi\s*thế\s*cạnh\s*tranh",
            r"workflow\s*integration|quy\s*trình\s*tác\s*nghiệp",
            r"seven-eleven|7-eleven"
        ]),
    ],
}


# =====================================================================
# Parsing & Extraction Helpers
# =====================================================================

def read_note_content(filename: str) -> str:
    """Reads the full UTF-8 text content of a note file."""
    filepath = STUDY_NOTES_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Study note file not found: {filepath}")
    return filepath.read_text(encoding="utf-8")


def extract_mermaid_blocks(content: str) -> List[Tuple[int, str]]:
    """
    Extracts all Mermaid blocks as (start_line_number, block_code)
    using robust line-by-line CommonMark fence recognition.
    """
    blocks = []
    lines = content.splitlines()
    in_block = False
    current: List[str] = []
    start_line = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not in_block:
            if stripped.startswith("```"):
                tag = stripped[3:].strip().lower()
                if tag == "mermaid" or tag.startswith("mermaid"):
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


def extract_python_code_blocks(content: str) -> List[Tuple[int, str]]:
    """
    Extracts all Python code blocks as (start_line_number, code)
    using robust line-by-line CommonMark fence recognition.
    """
    blocks = []
    lines = content.splitlines()
    in_block = False
    current: List[str] = []
    start_line = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not in_block:
            if stripped.startswith("```"):
                tag = stripped[3:].strip().lower()
                is_py = (
                    tag in ("python", "py")
                    or tag.startswith("python")
                    or tag.startswith("py")
                )
                if is_py:
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


def count_flashcards(content: str) -> int:
    """
    Counts Active Recall flashcards in the note.
    Supports standard card headings (### Thẻ X, ### Flashcard X, ### Card X),
    explicit question-answer pairs (**Hỏi:** ... **Đáp:**, **Q:** ... **A:**),
    or <details><summary> tags.
    """
    # 1. Check card headings like ### Thẻ 1:, ### Flashcard 1:, ### Card 1:
    heading_cards = re.findall(
        r"^###\s*(?:Thẻ|Flashcard|Card|Câu hỏi)\s*\d+.*$",
        content,
        re.MULTILINE | re.IGNORECASE,
    )
    if len(heading_cards) >= 5:
        return len(heading_cards)

    # 2. Check explicit Question indicators in Q&A pairs
    # Matches patterns like "- **Hỏi:**", "**Câu hỏi 1:**", "1. **Hỏi:**"
    q_pattern = (
        r"(?:^\s*[-*]?\s*\*\*(?:Hỏi|Câu hỏi|Question|Q\d*)\s*[:.]|"
        r"\b(?:Câu hỏi|Question|Thẻ)\s+\d+[:.]|"
        r"^\s*\d+\.\s*\*\*(?:Hỏi|Q|Câu hỏi))"
    )
    question_items = re.findall(
        q_pattern,
        content,
        re.MULTILINE | re.IGNORECASE,
    )
    if len(question_items) >= 5:
        return len(question_items)

    # 3. Check HTML <details> blocks
    detail_blocks = re.findall(
        r"<details>.*?<summary>.*?</summary>",
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if len(detail_blocks) >= 5:
        return len(detail_blocks)

    return max(len(heading_cards), len(question_items), len(detail_blocks))


def clean_code_for_ast(code: str) -> str:
    """
    Sanitizes code snippet before ast.parse:
    - Dedents common leading whitespace (from nested markdown lists)
    - Removes interactive REPL prompts (>>> , ... )
    - Comments out IPython magic commands (%matplotlib, !pip, etc.)
    """
    dedented_code = textwrap.dedent(code)
    cleaned_lines = []
    for line in dedented_code.splitlines():
        stripped = line.strip()
        # Handle REPL prompt
        if stripped.startswith(">>> "):
            line = stripped[4:]
        elif stripped.startswith("... "):
            line = stripped[4:]

        # Handle IPython magics and shell escapes
        if line.strip().startswith("%") or line.strip().startswith("!"):
            cleaned_lines.append("# [IPython Magic]: " + line)
        else:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def get_mermaid_diagram_type(block: str) -> str:
    """
    Finds the first non-comment line of a Mermaid block and extracts the type.
    """
    lines = block.splitlines()
    in_frontmatter = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == "---":
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter or stripped.startswith("%%"):
            continue
        # First operative line
        first_token = stripped.split()[0].lower()
        return first_token
    return ""


# =====================================================================
# Test Tier 1: Existence and Non-Emptiness
# =====================================================================

class TestTier1ExistenceAndPopulated(unittest.TestCase):
    """
    Verifies that the study_notes directory and all 7 required files
    exist, are valid UTF-8, and meet the minimum content threshold.
    """

    def test_study_notes_directory_exists(self):
        """Verify that the target output directory exists."""
        self.assertTrue(
            STUDY_NOTES_DIR.exists() and STUDY_NOTES_DIR.is_dir(),
            f"Required directory '{STUDY_NOTES_DIR}' does not exist.",
        )

    def test_all_seven_notes_exist(self):
        """Verify that all 7 required study notes exist in study_notes/."""
        missing = [
            f for f in EXPECTED_FILES if not (STUDY_NOTES_DIR / f).exists()
        ]
        self.assertEqual(
            missing, [],
            f"The following files are missing from {STUDY_NOTES_DIR}:\n"
            + "\n".join(f"- {m}" for m in missing),
        )

    def test_all_notes_non_empty(self):
        """Verify that every study note has > 0 bytes."""
        empty_files = []
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                empty_files.append(f"{filename} (FILE MISSING)")
            elif filepath.stat().st_size == 0:
                empty_files.append(f"{filename} (0 BYTES)")
        self.assertEqual(
            empty_files, [],
            "The following study note files are empty or missing:\n"
            + "\n".join(f"- {e}" for e in empty_files),
        )

    def test_all_notes_minimum_length(self):
        """Verify that every study note contains at least 2,000 characters."""
        too_short = []
        min_chars = 2000
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                too_short.append(f"{filename} (MISSING)")
                continue
            content = read_note_content(filename)
            char_count = len(content)
            if char_count < min_chars:
                too_short.append(
                    f"{filename} ({char_count} chars < {min_chars} required)"
                )
        self.assertEqual(
            too_short, [],
            "The following notes do not meet the minimum length:\n"
            + "\n".join(f"- {s}" for s in too_short),
        )

    def test_all_notes_valid_utf8(self):
        """Verify that all files are cleanly decodable as UTF-8."""
        decode_errors = []
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if filepath.exists():
                try:
                    filepath.read_text(encoding="utf-8")
                except UnicodeDecodeError as e:
                    decode_errors.append(f"{filename}: {e}")
        self.assertEqual(
            decode_errors, [],
            "UTF-8 decoding errors encountered:\n" + "\n".join(decode_errors),
        )


# =====================================================================
# Test Tier 2: Structural and Formatting Constraints (R1-R4)
# =====================================================================

class TestTier2StructuralAndFormatting(unittest.TestCase):
    """
    Verifies adherence to R1-R4:
    - Standard section headers (Theory, Python code, Mermaid, Flashcards,
      Edge cases)
    - >= 1 Mermaid diagram block per note
    - >= 5 Active Recall Flashcards per note
    - Python code blocks with '#' inline comments
    """

    def test_standard_section_headings(self):
        """Verify that each note conforms to the standard 5-part structure."""
        failures = []
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                continue
            content = read_note_content(filename)

            # Check Level 1 title
            if not re.search(r"^#\s+\d+[\.\s]", content, re.MULTILINE):
                failures.append(
                    f"{filename}: Missing level 1 title '# <Number>. <Title>'"
                )

            # Check R1: Theory section
            r1_pat = r"^##\s*1[\.\s].*(?:Lý Thuyết|Khung Lý Thuyết|Nền Tảng)"
            if not re.search(r1_pat, content, re.MULTILINE | re.IGNORECASE):
                failures.append(
                    f"{filename}: Missing Section 1 ('## 1. Khung Lý Thuyết')"
                )

            # Check R4: Mermaid / Visual section
            r4_pat = r"^##\s*3[\.\s].*(?:Sơ Đồ|Mermaid|Trực Quan)"
            if not re.search(r4_pat, content, re.MULTILINE | re.IGNORECASE):
                failures.append(
                    f"{filename}: Missing Section 3 ('## 3. Sơ Đồ Tư Duy...')"
                )

            # Check R3: Flashcards section
            r3_pat = r"^##\s*4[\.\s].*(?:Thẻ Ghi Nhớ|Flashcard|Active Recall)"
            if not re.search(r3_pat, content, re.MULTILINE | re.IGNORECASE):
                failures.append(
                    f"{filename}: Missing Section 4 ('## 4. Hệ Thống Thẻ...')"
                )

            # Check Edge cases section
            edge_pat = (
                r"^##\s*5[\.\s].*(?:Bẫy Tri Thức|Trường Hợp Biên|Edge Cases)"
            )
            if not re.search(edge_pat, content, re.MULTILINE | re.IGNORECASE):
                failures.append(
                    f"{filename}: Missing Section 5 ('## 5. Bẫy Tri Thức...')"
                )

            # Check R2: Python code section (for topic notes 01-06)
            if filename in TOPIC_NOTE_FILES:
                r2_pat = r"^##\s*2[\.\s].*(?:Mã Nguồn|Python|Code)"
                if not re.search(
                    r2_pat, content, re.MULTILINE | re.IGNORECASE
                ):
                    failures.append(
                        f"{filename}: Missing Section 2 ('## 2. Mã Nguồn...')"
                    )

        self.assertEqual(
            failures, [],
            "Structural section heading violations found:\n"
            + "\n".join(f"- {f}" for f in failures),
        )

    def test_mermaid_diagram_presence(self):
        """Verify each note has at least 1 ```mermaid block (R4)."""
        insufficient_mermaid = []
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                continue
            content = read_note_content(filename)
            mermaid_blocks = extract_mermaid_blocks(content)
            if len(mermaid_blocks) < 1:
                insufficient_mermaid.append(
                    f"{filename} (Found {len(mermaid_blocks)}, expected >= 1)"
                )

        self.assertEqual(
            insufficient_mermaid, [],
            "Notes lacking required Mermaid diagrams (R4):\n"
            + "\n".join(f"- {item}" for item in insufficient_mermaid),
        )

    def test_flashcard_count(self):
        """Verify every study note contains >= 5 Flashcard items (R3)."""
        insufficient_flashcards = []
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                continue
            content = read_note_content(filename)
            count = count_flashcards(content)
            if count < 5:
                insufficient_flashcards.append(
                    f"{filename} (Found {count}, expected >= 5)"
                )

        self.assertEqual(
            insufficient_flashcards, [],
            "Notes lacking required Active Recall Flashcards (R3):\n"
            + "\n".join(f"- {item}" for item in insufficient_flashcards),
        )

    def test_python_code_blocks_and_comments(self):
        """
        Verify that topic notes (01-06) contain Python code blocks and
        explanatory comments '#' are consistently present (R2).
        """
        missing_code = []
        insufficient_comments = []

        for filename in TOPIC_NOTE_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                continue
            content = read_note_content(filename)
            code_blocks = extract_python_code_blocks(content)

            if len(code_blocks) == 0:
                missing_code.append(filename)
                continue

            # Count total comment lines across all Python blocks
            total_comment_lines = sum(
                sum(1 for line in code.splitlines() if "#" in line)
                for _, code in code_blocks
            )
            # Require at least 5 comment lines in the topic note
            if total_comment_lines < 5:
                insufficient_comments.append(
                    f"{filename}: Only {total_comment_lines} comment lines "
                    f"across {len(code_blocks)} code blocks (expected >= 5)"
                )

        error_msgs = []
        if missing_code:
            error_msgs.append(
                "Notes missing Python code blocks:\n"
                + "\n".join(f"- {m}" for m in missing_code)
            )
        if insufficient_comments:
            error_msgs.append(
                "Notes lacking sufficient Python explanatory '#' comments:\n"
                + "\n".join(f"- {m}" for m in insufficient_comments)
            )

        self.assertEqual(error_msgs, [], "\n\n".join(error_msgs))


# =====================================================================
# Test Tier 3: Syntax Correctness (Mermaid & Python AST)
# =====================================================================

class TestTier3SyntaxCorrectness(unittest.TestCase):
    """
    Verifies that:
    1. Mermaid diagram blocks start with valid declarations and are non-empty.
    2. Python code snippets parse cleanly with ast.parse (zero syntax errors).
    """

    def test_mermaid_syntax_headers(self):
        """Verify Mermaid code blocks have recognized opening declarations."""
        invalid_blocks = []
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                continue
            content = read_note_content(filename)
            blocks = extract_mermaid_blocks(content)

            for idx, (line_num, block) in enumerate(blocks, start=1):
                if not block.strip():
                    invalid_blocks.append(
                        f"{filename} [Block #{idx} around line {line_num}]: "
                        f"Empty Mermaid block"
                    )
                    continue

                diagram_type = get_mermaid_diagram_type(block)
                if diagram_type not in VALID_MERMAID_TYPES:
                    sample_types = sorted(list(VALID_MERMAID_TYPES))[:5]
                    invalid_blocks.append(
                        f"{filename} [Block #{idx} around line {line_num}]: "
                        f"Unrecognized Mermaid diagram type '{diagram_type}'. "
                        f"Expected one of: {sample_types}..."
                    )

        self.assertEqual(
            invalid_blocks, [],
            "Invalid Mermaid diagram syntax found:\n"
            + "\n".join(f"- {b}" for b in invalid_blocks),
        )

    def test_python_code_blocks_ast_valid(self):
        """Verify all Python code blocks parse cleanly with ast.parse."""
        syntax_errors = []
        for filename in EXPECTED_FILES:
            filepath = STUDY_NOTES_DIR / filename
            if not filepath.exists():
                continue
            content = read_note_content(filename)
            code_blocks = extract_python_code_blocks(content)

            for idx, (line_num, code) in enumerate(code_blocks, start=1):
                cleaned_code = clean_code_for_ast(code)
                try:
                    ast.parse(cleaned_code)
                except SyntaxError as e:
                    syntax_errors.append(
                        f"{filename} [Block #{idx} starting line {line_num}, "
                        f"snippet line {e.lineno}]: "
                        f"SyntaxError: {e.msg}\n"
                        f"    Offending line: {e.text and e.text.strip()}"
                    )

        self.assertEqual(
            syntax_errors, [],
            "Python SyntaxError detected in code blocks:\n"
            + "\n".join(f"- {err}" for err in syntax_errors),
        )


# =====================================================================
# Test Tier 4: Academic Concept & Feature Coverage (F01-F32)
# =====================================================================

class TestTier4ConceptCoverage(unittest.TestCase):
    """
    Verifies that the core academic concepts and techniques specified in
    PROJECT.md § Feature Inventory (F01-F32) are present in the corresponding
    notes.
    """

    def _verify_concepts_for_file(self, filename: str):
        filepath = STUDY_NOTES_DIR / filename
        self.assertTrue(
            filepath.exists(),
            f"Cannot test concept coverage: {filename} does not exist.",
        )
        content = read_note_content(filename)

        missing_concepts = []
        specs = CONCEPT_SPECS.get(filename, [])
        for concept_name, pattern_list in specs:
            matched = False
            for pat in pattern_list:
                if re.search(pat, content, re.IGNORECASE):
                    matched = True
                    break
            if not matched:
                missing_concepts.append(
                    f"{concept_name} (patterns checked: {pattern_list})"
                )

        self.assertEqual(
            missing_concepts, [],
            f"Missing core academic concepts in {filename}:\n"
            + "\n".join(f"- {c}" for c in missing_concepts),
        )

    def test_m0_f01_master_index_concepts(self):
        """Verify 00_Index_and_Roadmap.md covers F01."""
        self._verify_concepts_for_file("00_Index_and_Roadmap.md")

    def test_m1_f02_f05_python_foundations_concepts(self):
        """Verify 01_Python_Foundations.md covers F02-F05."""
        self._verify_concepts_for_file("01_Python_Foundations.md")

    def test_m2_f06_f10_statistics_and_eda_concepts(self):
        """Verify 02_Statistics_and_EDA.md covers F06-F10."""
        self._verify_concepts_for_file("02_Statistics_and_EDA.md")

    def test_m3_f11_f16_numpy_computing_concepts(self):
        """Verify 03_NumPy_Computing.md covers F11-F16."""
        self._verify_concepts_for_file("03_NumPy_Computing.md")

    def test_m4_f17_f21_supervised_regression_concepts(self):
        """Verify 04_Supervised_Regression.md covers F17-F21."""
        self._verify_concepts_for_file("04_Supervised_Regression.md")

    def test_m5_f22_f28_supervised_classification_concepts(self):
        """Verify 05_Supervised_Classification.md covers F22-F28."""
        self._verify_concepts_for_file("05_Supervised_Classification.md")

    def test_m6_f29_f32_ml_landscape_and_strategy_concepts(self):
        """Verify 06_ML_Landscape_and_Strategy.md covers F29-F32."""
        self._verify_concepts_for_file("06_ML_Landscape_and_Strategy.md")


if __name__ == "__main__":
    unittest.main(verbosity=2)
