"""
IMLC 2026 Challenger 3 - Adversarial Leakage & Invariance Verification Suite
=============================================================================
Author: Challenger 3 (Adversarial Leakage & Invariance Challenger)
Target: Comprehensive adversarial audit of docs/, latex/, README.md, quarantine,
        and mathematical invariance of the revised generalized drift framework.
"""

import re
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
MODULES_DIR = DOCS_DIR / "modules"
LATEX_DIR = PROJECT_ROOT / "latex"
ARCHIVE_DIR = PROJECT_ROOT / ".archive" / "qualification_solutions"
STUDY_GUIDE_MD = DOCS_DIR / "IMLC_2026_Study_Guide.md"
STUDY_GUIDE_TEX = LATEX_DIR / "imlc_study_guide.tex"
README_FILE = PROJECT_ROOT / "README.md"

# Comprehensive catalog of forbidden contest leakage patterns across Problems A through E
FORBIDDEN_LEAK_PATTERNS = [
    # Problem A: Acoustic Lifecycle in School
    (r"Step 2 and Step 6", "Problem A: Active learning steps direct answer"),
    (r"10[,.]?000 recordings", "Problem A: Specific contest dataset size"),
    (r"labelled\s+speech,\s+music,\s+or\s+alarm", "Problem A: Exact label triad prompt"),
    (r"Collect 10[,.]?000 recordings labelled \*speech\*", "Problem A: Step 1 description"),
    (r"Install the model in a school", "Problem A: Step 4 description"),
    (r"installed model receives a new sound and predicts \*alarm\*", "Problem A: Step 5 description"),

    # Problem B: Greenhouse Decision Tree & CO2 Log
    (r"KEEP CLOSED", "Problem B: Action KEEP CLOSED"),
    (r"OPEN ROOF|OPEN the roof", "Problem B: Action OPEN ROOF"),
    (r"1250\s*ppm", "Problem B: Exact contest threshold 1250 ppm"),
    (r"Is\s+Temperature\s*>\s*28", "Problem B: Baseline tree root query"),
    (r"Is\s+Humidity\s*>\s*70", "Problem B: Baseline tree humidity query"),
    (r"T\s*=\s*26.*H\s*=\s*68", "Problem B: Question (a) query tuple"),
    (r"T\s*=\s*31.*H\s*=\s*60.*CO_?2\s*=\s*700", "Problem B: Log row 1"),
    (r"T\s*=\s*26.*H\s*=\s*75.*CO_?2\s*=\s*650", "Problem B: Log row 2"),
    (r"T\s*=\s*25.*H\s*=\s*60.*CO_?2\s*=\s*800", "Problem B: Log row 3"),
    (r"T\s*=\s*27.*H\s*=\s*68.*CO_?2\s*=\s*1100", "Problem B: Log row 4"),
    (r"T\s*=\s*24.*H\s*=\s*55.*CO_?2\s*=\s*1400", "Problem B: Log row 5"),
    (r"T\s*=\s*22.*H\s*=\s*50.*CO_?2\s*=\s*1550", "Problem B: Log row 6"),

    # Problem C: Polynomial Regression & Ridge Regularization
    (r"\b9\.26\b|9\.2600", "Problem C: Exact regularized score J(M1)"),
    (r"\b4\.08\b|4\.0800", "Problem C: Exact regularized score J(M2)"),
    (r"0\.015209|0\.01521\b", "Problem C: Exact lambda* threshold"),
    (r"0\.2x\^3\s*-\s*0\.9x\^2\s*\+\s*2\.9x\s*\+\s*1", "Problem C: Model 1 formula"),
    (r"\{\(0,\s*1\.0\),\s*\(1,\s*3\.2\),\s*\(2,\s*4\.8\),\s*\(3,\s*7\.0\)\}", "Problem C: Dataset"),
    (r"a_1\s*=\s*2\.9,\s*a_2\s*=\s*-0\.9,\s*a_3\s*=\s*0\.2", "Problem C: Polynomial coefficients"),

    # Problem D: Scalar RLHF Drift & Exact Safety Bound
    (r"-rt\s*\+\s*(\\beta|beta)\s*t\^2", "Problem D: Scalar loss model L(t) = -rt + beta t^2"),
    (r"L\(t\)\s*=\s*-?\s*rt", "Problem D: Loss formulation L(t) = -rt"),
    (r"t\^\*\s*=\s*\\frac\{r\}\{2\\beta\}|t\^\*\s*=\s*r\s*/\s*\(?2\\beta\)?", "Problem D: Question (a) optimal t*"),
    (r"-\\frac\{r\^2\}\{4\\beta\}|-r\^2\s*/\s*\(?4\\beta\)?", "Problem D: Question (a) minimum loss L(t*)"),
    (r"(\\beta|beta)\s*\\ge\s*\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2T\}", "Problem D: Question (c) safety bound"),
    (r"\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2(\\beta|beta)\}\s*\\le\s*T", "Problem D: Question (c) drift bound"),
    (r"The reward achieved is rt", "Problem D: Prompt description"),
    (r"quantify the drift from the reference model", "Problem D: Prompt description"),
    (r"SENIOR-2026-VN-0428", "Problem D: Candidate ID"),

    # Problem E: Nepal Agronomic Advisory System
    (r"rural\s+Nepal|farmers?\s+across\s+rural\s+Nepal|rice\s+farmer\s+in\s+Nepal", "Problem E: Nepal context"),
    (r"Irrigate.*Apply treatment.*Wait.*Contact an expert", "Problem E: 4 action keys"),

    # Generic Contest Solution Headers
    (r"Official Problem Statement", "Prohibited contest heading"),
    (r"Mathematical Solutions and Theoretical Analysis", "Prohibited solution document title"),
]


class TestAdversarialLeakageFirewallDocs:
    """Scans every markdown document in docs/ and docs/modules/."""

    def test_all_docs_files_free_of_contest_leaks(self):
        doc_files = list(DOCS_DIR.glob("*.md")) + list(MODULES_DIR.glob("*.md"))
        assert len(doc_files) >= 5, f"Expected multiple doc files, found {len(doc_files)}"

        leak_occurrences = []
        for doc_path in doc_files:
            content = doc_path.read_text(encoding="utf-8", errors="ignore")
            for pattern, desc in FORBIDDEN_LEAK_PATTERNS:
                matches = list(re.finditer(pattern, content, re.IGNORECASE))
                if matches:
                    for m in matches:
                        line_no = content[: m.start()].count("\n") + 1
                        leak_occurrences.append(
                            f"{doc_path.name}:{line_no} [{desc}] -> '{m.group(0)}'"
                        )

        assert not leak_occurrences, (
            f"Adversarial Leakage Detected in docs/ ({len(leak_occurrences)} hits):\n"
            + "\n".join(leak_occurrences)
        )


class TestAdversarialLeakageFirewallLatex:
    """Scans all active LaTeX and bibliography files in latex/."""

    def test_latex_sources_free_of_contest_leaks(self):
        assert STUDY_GUIDE_TEX.exists(), "latex/imlc_study_guide.tex must exist"
        latex_files = [STUDY_GUIDE_TEX]
        bib_file = LATEX_DIR / "references.bib"
        if bib_file.exists():
            latex_files.append(bib_file)

        leak_occurrences = []
        for lpath in latex_files:
            content = lpath.read_text(encoding="utf-8", errors="ignore")
            for pattern, desc in FORBIDDEN_LEAK_PATTERNS:
                matches = list(re.finditer(pattern, content, re.IGNORECASE))
                if matches:
                    for m in matches:
                        line_no = content[: m.start()].count("\n") + 1
                        leak_occurrences.append(
                            f"{lpath.name}:{line_no} [{desc}] -> '{m.group(0)}'"
                        )

        assert not leak_occurrences, (
            f"Adversarial Leakage Detected in latex/ ({len(leak_occurrences)} hits):\n"
            + "\n".join(leak_occurrences)
        )


class TestAdversarialLeakageFirewallReadme:
    """Scans repository README.md."""

    def test_readme_free_of_contest_leaks(self):
        assert README_FILE.exists(), "README.md must exist"
        content = README_FILE.read_text(encoding="utf-8", errors="ignore")
        leak_occurrences = []
        for pattern, desc in FORBIDDEN_LEAK_PATTERNS:
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if matches:
                for m in matches:
                    line_no = content[: m.start()].count("\n") + 1
                    leak_occurrences.append(
                        f"README.md:{line_no} [{desc}] -> '{m.group(0)}'"
                    )

        assert not leak_occurrences, (
            f"Adversarial Leakage Detected in README.md ({len(leak_occurrences)} hits):\n"
            + "\n".join(leak_occurrences)
        )


class TestQuarantineIntegrity:
    """Verifies that solution files are quarantined and removed from public paths."""

    def test_quarantined_files_not_in_docs_or_latex(self):
        forbidden_public_paths = [
            DOCS_DIR / "03_qualification_solutions.md",
            LATEX_DIR / "imlc_submission.tex",
            LATEX_DIR / "imlc_submission.pdf",
            LATEX_DIR / "imlc_submission.aux",
            LATEX_DIR / "imlc_submission.log",
            LATEX_DIR / "tikz_decision_tree.tex",
        ]
        present = [str(p) for p in forbidden_public_paths if p.exists()]
        assert not present, f"Quarantined files still present in public deliverable paths: {present}"

    def test_quarantined_files_exist_in_archive(self):
        assert ARCHIVE_DIR.exists(), f"Quarantine directory {ARCHIVE_DIR} does not exist"
        archived_solutions = ARCHIVE_DIR / "03_qualification_solutions.md"
        archived_latex = ARCHIVE_DIR / "imlc_submission.tex"
        archived_readme = ARCHIVE_DIR / "README.md"

        assert archived_solutions.exists(), "03_qualification_solutions.md missing from archive"
        assert archived_latex.exists(), "imlc_submission.tex missing from archive"
        assert archived_readme.exists(), "README.md missing from archive"

        readme_text = archived_readme.read_text(encoding="utf-8")
        assert "Quarantined" in readme_text or "R3" in readme_text, (
            "Quarantine README must document R3 status"
        )


class TestMathematicalInvarianceAndGeneralization:
    """Verifies that the generalized drift framework is mathematically rigorous and invariant."""

    def test_generalized_drift_objective_presence(self):
        for path in [STUDY_GUIDE_MD, STUDY_GUIDE_TEX]:
            text = path.read_text(encoding="utf-8", errors="ignore")
            # Must formulate generalized objective with reward and divergence
            has_gen_obj = bool(
                re.search(r"\\mathcal\{L\}_\{?\\(?:mathrm|text)\{drift\}?\}?|\\min_\{?\\pi\}?.*\\mathcal\{L\}", text)
                or re.search(r"-\\mathcal\{R\}\\(\s*\\pi\s*\\)\s*\\+\s*\\beta.*\\mathcal\{D\}", text)
                or re.search(r"\\mathbb\{E\}.*r\(x,\s*y\).*\\beta.*\\mathcal\{D\}", text)
                or re.search(r"\\mathbb\{E\}.*r\(x,\s*y\).*\\beta.*D_\{?\\text\{KL\}?\}?", text)
            )
            assert has_gen_obj, f"Missing generalized drift objective in {path.name}"

    def test_optimal_gibbs_policy_mathematical_derivation(self):
        for path in [STUDY_GUIDE_MD, STUDY_GUIDE_TEX]:
            text = path.read_text(encoding="utf-8", errors="ignore")
            has_gibbs = bool(
                re.search(r"\\pi\^\*\s*\(y\s*\\mid\s*x\)\s*=\s*\\frac\{1\}\{Z\(x\)\}", text)
                or re.search(r"\\frac\{1\}\{Z\}\s*\\pi_\{?\\text\{ref\}?\}?.*\\exp", text)
                or re.search(r"\\exp\s*\(\s*\\frac\{r\(.*\)\}\{\\beta\}\s*\)", text)
            )
            assert has_gibbs, f"Missing Gibbs optimal policy derivation in {path.name}"

    def test_fisher_information_geometry_invariant(self):
        for path in [STUDY_GUIDE_MD, STUDY_GUIDE_TEX]:
            text = path.read_text(encoding="utf-8", errors="ignore")
            has_fisher = bool(
                re.search(r"Fisher|\\mathcal\{F\}|information\s+metric", text, re.IGNORECASE)
                and re.search(r"Taylor|Hessian|second-order", text, re.IGNORECASE)
            )
            assert has_fisher, f"Missing Fisher Information geometric invariance in {path.name}"

    def test_abstract_safety_boundary_framework(self):
        for path in [STUDY_GUIDE_MD, STUDY_GUIDE_TEX]:
            text = path.read_text(encoding="utf-8", errors="ignore")
            # Should discuss divergence bounds, trust regions, or drift limits without hardcoded contest solution
            has_boundary = bool(
                re.search(r"sup.*r_\{?\\text\{max\}?\}?.*T_\{?\\text\{drift\}?\}?", text)
                or re.search(r"safety\s+bound|divergence\s+bound|trust\s+region", text, re.IGNORECASE)
            )
            assert has_boundary, f"Missing abstract safety boundary framework in {path.name}"

    def test_zero_leak_of_scalar_model_in_generalized_drift(self):
        for path in [STUDY_GUIDE_MD, STUDY_GUIDE_TEX]:
            text = path.read_text(encoding="utf-8", errors="ignore")
            assert not re.search(r"-rt\s*\+\s*\\beta\s*t\^2", text), f"Found scalar leak in {path.name}"
            assert not re.search(r"t\^\*\s*=\s*\\frac\{r\}\{2\\beta\}", text), f"Found t* leak in {path.name}"
            assert not re.search(r"-\\frac\{r\^2\}\{4\\beta\}", text), f"Found min loss leak in {path.name}"
            assert not re.search(r"\\beta\s*\\ge\s*\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2T\}", text), f"Found bound leak in {path.name}"
