# Task Assignment for E2E Test Writer

## Objective
Build the automated test infrastructure and test runner suite to verify that all study notes in `d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes\` strictly meet all user requirements (R1, R2, R3, R4) and quality criteria.

## Required Reading
- `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\ORIGINAL_REQUEST.md`
- `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\orchestrator_1\PROJECT.md`

## Required Deliverables
1. Python test script (e.g., `tests/test_study_notes.py`) executable via `python tests/test_study_notes.py` or `pytest`.
   - Tier 1: Feature Coverage (all 7 study note files exist and are populated).
   - Tier 2: Boundary & Formatting (each note has >= 1 mermaid block, >= 5 flashcards, python code with `#` comments, minimum word/byte thresholds).
   - Tier 3: Cross-Feature Syntax Verification (Mermaid block syntax validation, Python code blocks extractable and validated with `ast.parse` for zero syntax errors).
   - Tier 4: Real-world Academic Topic Verification (domain keyword checks for core concepts from `PROJECT.md § Feature Inventory`: Collatz, Z-score, IQR, ndarray, OLS, Gini, PCA, Dark Data).
2. Create `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\orchestrator_1\TEST_INFRA.md` documenting test architecture and test runner command.
3. Once tests are built and verified, create `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\orchestrator_1\TEST_READY.md`.
4. Write your `handoff.md` and report back via `send_message`.

## 2026-09-20T15:08:47Z
You are the E2E Test Writer for the GCI World 202609 course study notes project.
Your working directory: d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\test_writer_1
Workspace root: d:\02_Learning_Knowledge\GCI_World_2026_September
Task assignment: d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\test_writer_1\DISPATCH.md
Authoritative request: d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\ORIGINAL_REQUEST.md
Project plan & feature inventory: d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\orchestrator_1\PROJECT.md

MANDATORY FIRST STEP: Read ORIGINAL_REQUEST.md and PROJECT.md.
Then:
1. Create automated test scripts in `tests/test_study_notes.py` (and any required runner helpers) that verify:
   - Tier 1: Existence and non-emptiness of all 7 study notes in `study_notes/` (00_Index_and_Roadmap.md, 01_Python_Foundations.md, 02_Statistics_and_EDA.md, 03_NumPy_Computing.md, 04_Supervised_Regression.md, 05_Supervised_Classification.md, 06_ML_Landscape_and_Strategy.md).
   - Tier 2: Structural and formatting constraints per R1-R4 (each note has >= 1 ```mermaid block, >= 5 flashcard Q&A items, python code blocks with `#` comments, minimum 2000 characters).
   - Tier 3: Syntax correctness (validate Mermaid block opening headers, and parse all Python code snippets with `ast.parse` to ensure zero syntax errors).
   - Tier 4: Content and concept coverage checks (verifying that core course topics from PROJECT.md Feature Inventory are present in the corresponding notes).
2. Create `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\orchestrator_1\TEST_INFRA.md` describing the test architecture and commands.
3. Once tests are in place, publish `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\orchestrator_1\TEST_READY.md`.
4. Write handoff.md in your working directory and report back via send_message.
