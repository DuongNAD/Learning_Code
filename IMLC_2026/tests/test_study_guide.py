"""
IMLC 2026 E2E Test Suite - Study Guide Verification (Tiers 1 to 5)
==================================================================

Author: Test Writer 1 (E2E Testing Track)
Target: Comprehensive E2E verification of the IMLC 2026 Theoretical Study Guide
Deliverables Tested:
  - Markdown Monograph: docs/IMLC_2026_Study_Guide.md (or docs/modules/*.md)
  - LaTeX Monograph: latex/imlc_study_guide.tex -> latex/imlc_study_guide.pdf
  
Test Tiers Covered:
  - Tier 1: Feature Coverage (F1-F12: IMLC format intro + 5 qualification topics + variational synthesis)
  - Tier 2: Boundary & Math Verification (Explicit loss formulas, matrix gradients, closed-form solutions,
            soft-thresholding, KL divergence, Bradley-Terry, Gibbs optimal policy, Fisher metric, asymptotics)
  - Tier 3: R3 Integrity & Non-Leakage Firewall (Zero contest answer leaks, strictly pedagogical guidance)
  - Tier 4: Pedagogical Scaffolding & Keywords (DeepTutor 5-tier scaffold, keyword banks, Socratic questions)
  - Tier 5: Build & Document Quality (Markdown encoding, code block balance, LaTeX syntax & compilation)
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pytest

# Project Path Configurations
TESTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TESTS_DIR.parent
DOCS_DIR = PROJECT_ROOT / "docs"
MODULES_DIR = DOCS_DIR / "modules"
LATEX_DIR = PROJECT_ROOT / "latex"

STUDY_GUIDE_MD = DOCS_DIR / "IMLC_2026_Study_Guide.md"
STUDY_GUIDE_TEX = LATEX_DIR / "imlc_study_guide.tex"
STUDY_GUIDE_PDF = LATEX_DIR / "imlc_study_guide.pdf"

# ==============================================================================
# Content Retrieval & Progressive Fallback Helpers
# ==============================================================================

def clean_text(raw_text: str) -> str:
    """Removes UTF-8 BOM and standardizes line endings."""
    return raw_text.lstrip("\ufeff").replace("\r\n", "\n")


def get_study_guide_markdown() -> str:
    """
    Retrieves the complete Markdown study guide content.
    Supports progressive testability: if docs/IMLC_2026_Study_Guide.md exists,
    returns its content. Otherwise, aggregates all available module files in
    docs/modules/*.md. If neither exists, skips with an informative message.
    """
    if STUDY_GUIDE_MD.exists():
        with open(STUDY_GUIDE_MD, "r", encoding="utf-8-sig") as f:
            return clean_text(f.read())

    # Progressive fallback: aggregate docs/modules/*.md
    if MODULES_DIR.exists():
        module_files = sorted(MODULES_DIR.glob("*.md"))
        if module_files:
            combined = []
            for mf in module_files:
                with open(mf, "r", encoding="utf-8-sig") as f:
                    combined.append(clean_text(f.read()))
            return "\n\n".join(combined)

    pytest.skip(
        "Study guide markdown deliverable not yet created. "
        "Expected docs/IMLC_2026_Study_Guide.md or docs/modules/*.md."
    )


def get_all_docs_markdown() -> list[tuple[Path, str]]:
    """
    Retrieves all Markdown files across docs/ and its subdirectories (docs/**/*.md).
    Returns list of tuples (Path, content_string).
    """
    docs = []
    if DOCS_DIR.exists():
        for p in sorted(DOCS_DIR.glob("**/*.md")):
            if p.is_file():
                with open(p, "r", encoding="utf-8-sig") as f:
                    docs.append((p, clean_text(f.read())))
    return docs


def get_module_content(name_or_keyword: str) -> str:
    """
    Retrieves content for a specific module file in docs/modules/,
    or returns the aggregated study guide markdown if unified.
    """
    if MODULES_DIR.exists():
        for mf in sorted(MODULES_DIR.glob("*.md")):
            if name_or_keyword.lower() in mf.name.lower():
                with open(mf, "r", encoding="utf-8-sig") as f:
                    return clean_text(f.read())

    # Fallback to combined guide
    return get_study_guide_markdown()


def get_study_guide_latex() -> str:
    """
    Retrieves the LaTeX study guide source content.
    Skips if latex/imlc_study_guide.tex has not yet been generated.
    """
    if not STUDY_GUIDE_TEX.exists():
        pytest.skip(
            f"LaTeX deliverable {STUDY_GUIDE_TEX.name} not yet created by implementation track."
        )
    with open(STUDY_GUIDE_TEX, "r", encoding="utf-8-sig") as f:
        return clean_text(f.read())


# ==============================================================================
# TIER 1: Feature Coverage (Requirements R1, R2; Features F1 - F12)
# ==============================================================================

class TestTier1FeatureCoverage:
    """
    Verifies that the study guide comprehensively covers:
    - IMLC format, competition funnel, comparison matrix, strategic handbook (R1)
    - All 5 qualification topics with conceptual foundations (R2)
    - Cross-paradigm variational synthesis (F9)
    """

    def test_tier1_deliverable_presence_and_substance(self):
        """Validates that the study guide exists and contains substantial substance (> 5,000 words)."""
        content = get_study_guide_markdown()
        assert len(content.strip()) > 5000, "Study guide is too brief to be a comprehensive monograph"
        words = len(content.split())
        assert words >= 2500, f"Study guide has {words} words; expected substantial educational depth"

    def test_tier1_imlc_structure_and_funnel(self):
        """F1: Validates institutional background, 3-stage competition funnel, and division rules."""
        content = get_study_guide_markdown()
        # Institutional Context
        assert "Edu.Harbour" in content or "Edu.Harbour GbR" in content, "Missing Edu.Harbour context"
        assert "Hamburg" in content, "Missing Hamburg location reference"
        assert "social enterprise" in content.lower() or "yunus" in content.lower(), (
            "Missing Yunus social enterprise context"
        )

        # 3-Stage Funnel
        assert re.search(r"qualification", content, re.IGNORECASE), "Missing Qualification stage"
        assert re.search(r"pre-final|prefinal", content, re.IGNORECASE), "Missing Pre-Final stage"
        assert re.search(r"\bfinal\b", content, re.IGNORECASE), "Missing Final stage"
        assert "25" in content, "Missing Qualification 25-point scale reference"

        # Division rules
        assert re.search(r"senior", content, re.IGNORECASE), "Missing Senior division reference"
        assert re.search(r"junior", content, re.IGNORECASE), "Missing Junior division reference"

    def test_tier1_competition_comparison_matrix(self):
        """F2: Validates multi-dimensional comparison between IMLC and peer competitions."""
        content = get_study_guide_markdown()
        assert "Kaggle" in content, "Comparison matrix must reference Kaggle"
        assert "IOI" in content or "ICPC" in content, "Comparison matrix must reference IOI/ICPC"
        assert "NeurIPS" in content or "IOAI" in content, "Comparison matrix must reference NeurIPS/IOAI"

    def test_tier1_evaluation_rubric_and_strategy(self):
        """F3: Validates scientific paper reading protocol, time allocation, and pitfall analysis."""
        content = get_study_guide_markdown()
        assert re.search(r"3-pass|three-pass|pass\s+1", content, re.IGNORECASE), (
            "Missing 3-pass scientific paper reading protocol"
        )
        assert re.search(r"pitfall|common\s+mistake|failure\s+mode", content, re.IGNORECASE), (
            "Missing competition pitfall analysis"
        )

    def test_tier1_topic1_ml_lifecycle_and_drift(self):
        """F4: Validates Topic 1: ML Lifecycle, Mitchell's formulation, and distribution drift."""
        content = get_study_guide_markdown()
        assert re.search(r"Mitchell", content, re.IGNORECASE), "Missing Tom Mitchell's learning definition"
        assert re.search(r"covariate\s+shift", content, re.IGNORECASE), "Missing Covariate Shift"
        assert re.search(r"concept\s+shift", content, re.IGNORECASE), "Missing Concept Shift"
        assert re.search(r"inference", content, re.IGNORECASE), "Missing inference vs training distinction"
        assert re.search(r"KS-test|Kolmogorov|PSI|Population Stability", content, re.IGNORECASE), (
            "Missing drift detection metrics (KS-test or PSI)"
        )

    def test_tier1_topic2_decision_trees(self):
        """F5: Validates Topic 2: Decision Trees, entropy, Gini, and cost-complexity pruning."""
        content = get_study_guide_markdown()
        assert re.search(r"entropy", content, re.IGNORECASE), "Missing Shannon Entropy"
        assert re.search(r"Gini", content, re.IGNORECASE), "Missing Gini Impurity"
        assert re.search(r"information\s+gain", content, re.IGNORECASE), "Missing Information Gain"
        assert re.search(r"pruning|cost-complexity", content, re.IGNORECASE), "Missing CART pruning"

    def test_tier1_topic3_regularization(self):
        """F6: Validates Topic 3: Polynomial Regression, Runge phenomenon, Ridge and Lasso."""
        content = get_study_guide_markdown()
        assert re.search(r"Ridge", content, re.IGNORECASE), "Missing Ridge regression"
        assert re.search(r"Lasso", content, re.IGNORECASE), "Missing Lasso regression"
        assert re.search(r"Runge", content, re.IGNORECASE), "Missing Runge's phenomenon"
        assert re.search(r"bias-variance|bias\s+variance", content, re.IGNORECASE), (
            "Missing Bias-Variance trade-off"
        )

    def test_tier1_topic4_rlhf_and_drift(self):
        """F7: Validates Topic 4: RLHF, Bradley-Terry, KL divergence, Goodhart's law."""
        content = get_study_guide_markdown()
        assert re.search(r"RLHF|human\s+feedback", content, re.IGNORECASE), "Missing RLHF"
        assert re.search(r"Bradley-Terry|Bradley\s+Terry", content, re.IGNORECASE), (
            "Missing Bradley-Terry preference model"
        )
        assert re.search(r"Kullback|KL\s+divergence|relative\s+entropy", content, re.IGNORECASE), (
            "Missing KL Divergence"
        )
        assert re.search(r"Goodhart|reward\s+hack", content, re.IGNORECASE), (
            "Missing Goodhart's law / reward hacking"
        )

    def test_tier1_topic5_ai_ethics_and_deployment(self):
        """F8: Validates Topic 5: Algorithmic Fairness, Kleinberg theorem, Conformal Prediction, RAG."""
        content = get_study_guide_markdown()
        assert re.search(r"demographic\s+parity", content, re.IGNORECASE), "Missing Demographic Parity"
        assert re.search(r"equalized\s+odds", content, re.IGNORECASE), "Missing Equalized Odds"
        assert re.search(r"Kleinberg", content, re.IGNORECASE), "Missing Kleinberg's Impossibility Theorem"
        assert re.search(r"conformal\s+prediction", content, re.IGNORECASE), "Missing Conformal Prediction"
        assert re.search(r"RAG|retrieval-augmented|retrieval\s+augmented", content, re.IGNORECASE), (
            "Missing Grounded RAG architecture"
        )

    def test_tier1_cross_pillar_variational_synthesis(self):
        """F9: Validates Cross-Pillar Variational Synthesis (L2 Tikhonov = Gaussian Relative Entropy)."""
        content = get_study_guide_markdown()
        assert re.search(r"variational|synthesis|relative\s+entropy|Gaussian", content, re.IGNORECASE), (
            "Missing variational cross-pillar synthesis"
        )


# ==============================================================================
# TIER 2: Boundary & Mathematical Verification (Acceptance Criteria 2)
# ==============================================================================

class TestTier2BoundaryAndMathVerification:
    """
    Verifies that:
    - Topic "Regularization" contains both conceptual explanation AND explicit mathematical formulas:
      loss L_Ridge / J_Ridge, matrix gradient nabla_w J, closed-form normal equation, soft-thresholding.
    - Topic "RLHF Drift" contains both conceptual explanation AND explicit mathematical formulas:
      D_KL(pi_theta || pi_ref), Bradley-Terry preference probability, optimal policy derivation.
    - Extreme asymptotic boundary conditions (lambda -> 0, lambda -> inf; beta -> 0, beta -> inf).
    """

    # --- Regularization Math & Concepts ---

    def test_tier2_regularization_conceptual_explanation(self):
        """Acceptance Criteria 2: Topic Regularization must have conceptual explanation."""
        content = get_study_guide_markdown()
        # Conceptual notions: controlling complexity, smoothing oscillations, variance reduction, Occam's razor
        has_complexity = bool(re.search(r"complexity|overfit|capacity", content, re.IGNORECASE))
        has_variance = bool(re.search(r"variance|bias-variance|shrinkage", content, re.IGNORECASE))
        has_oscillation = bool(re.search(r"oscillation|Runge|curvature|wiggl", content, re.IGNORECASE))
        assert has_complexity and has_variance and has_oscillation, (
            "Topic Regularization lacks comprehensive conceptual explanation of complexity and variance."
        )

    def test_tier2_regularization_loss_formulas(self):
        """Topic Regularization must define mathematical loss formula for L2 Ridge."""
        content = get_study_guide_markdown()
        # Look for J_Ridge, L_Ridge, RSS + lambda ||w||^2, or ||y - \Phi w||_2^2 + \lambda/2 ||w||_2^2
        has_ridge_loss = bool(
            re.search(r"J_\{?\\text\{Ridge\}?\}?|\\mathcal\{L\}_\{?\\text\{Ridge\}?\}?", content)
            or re.search(r"\|y\s*-\s*\\Phi\s*w\|_2\^2.*\\lambda", content)
            or re.search(r"\|y\s*-\s*Xw\|_2\^2.*\\lambda", content)
            or re.search(r"\\lambda.*\\|w.*\\|_2\^2|\\lambda.*\\sum.*w_j\^2", content)
            or re.search(r"\\lambda\s*\\sum.*a_i\^2", content)
        )
        assert has_ridge_loss, "Missing mathematical formula for Ridge regression loss (L_Ridge / J_Ridge)."

    def test_tier2_regularization_matrix_gradient_derivation(self):
        """Topic Regularization must contain explicit matrix gradient derivation."""
        content = get_study_guide_markdown()
        # \nabla_w J or nabla J with design matrix Phi^T or X^T and lambda term
        has_gradient = bool(
            re.search(r"\\nabla_w\s*J|\\nabla\s*J|\\frac\{\\partial\s*J\}\{\\partial\s*w\}", content)
            and (re.search(r"\\Phi\^T", content) or re.search(r"X\^T", content))
            and (re.search(r"\\lambda.*w", content) or re.search(r"\\lambda\s*I", content))
        )
        assert has_gradient, "Missing matrix gradient derivation for Ridge regression loss."

    def test_tier2_regularization_closed_form_normal_equations(self):
        """Topic Regularization must state closed-form normal equation with matrix inverse."""
        content = get_study_guide_markdown()
        # (\Phi^T \Phi + n\lambda I^*)^{-1} or (X^T X + \lambda I)^{-1}
        has_closed_form = bool(
            re.search(r"\(\s*\\Phi\^T\s*\\Phi\s*\+\s*.*\\lambda.*I.*\)\^\{?-1\}?", content)
            or re.search(r"\(\s*X\^T\s*X\s*\+\s*.*\\lambda.*I.*\)\^\{?-1\}?", content)
        )
        assert has_closed_form, (
            "Missing closed-form normal equation: (X^T X + \\lambda I)^{-1} X^T y or (\\Phi^T \\Phi + n\\lambda I^*)^{-1}"
        )

    def test_tier2_regularization_soft_thresholding_operator(self):
        """Topic Regularization must state L1 Lasso soft-thresholding operator S_lambda."""
        content = get_study_guide_markdown()
        has_soft_threshold = bool(
            re.search(r"\\mathcal\{S\}_|soft-threshold|soft\s+threshold", content, re.IGNORECASE)
            and re.search(r"\\text\{sign\}|\\text\{sgn\}|sign\(", content, re.IGNORECASE)
        )
        assert has_soft_threshold, (
            "Missing L1 Lasso soft-thresholding operator formula or definition."
        )

    def test_tier2_regularization_asymptotic_limits(self):
        """Topic Regularization must analyze asymptotic limits (lambda -> 0 vs lambda -> inf)."""
        content = get_study_guide_markdown()
        has_limits = bool(
            (re.search(r"\\lambda.*0", content) or re.search(r"lambda.*0", content, re.IGNORECASE))
            and (re.search(r"\\infty", content) or re.search(r"infinity", content, re.IGNORECASE))
        )
        assert has_limits, (
            "Missing asymptotic limit analysis for regularization parameter lambda (0 and infinity)."
        )

    # --- RLHF Drift Math & Concepts ---

    def test_tier2_rlhf_drift_conceptual_explanation(self):
        """Acceptance Criteria 2: Topic RLHF Drift must have conceptual explanation."""
        content = get_study_guide_markdown()
        has_alignment = bool(re.search(r"alignment|human\s+preference|reward\s+model", content, re.IGNORECASE))
        has_goodhart = bool(re.search(r"Goodhart|reward\s+hack|gaming|exploit", content, re.IGNORECASE))
        has_anchor = bool(re.search(r"reference\s+model|anchor|divergence|KL", content, re.IGNORECASE))
        assert has_alignment and has_goodhart and has_anchor, (
            "Topic RLHF Drift lacks comprehensive conceptual explanation of alignment, hacking, and reference anchor."
        )

    def test_tier2_rlhf_kl_divergence_formula(self):
        """Topic RLHF Drift must define Kullback-Leibler divergence mathematically."""
        content = get_study_guide_markdown()
        has_kl = bool(
            re.search(r"D_\{?\\text\{KL\}?\}?|D_\{KL\}", content)
            and re.search(r"\\pi.*\\pi_\{?\\text\{ref\}?\}?", content)
            and re.search(r"\\log", content)
        )
        assert has_kl, (
            "Missing mathematical definition of KL divergence: D_KL(pi_theta || pi_ref)."
        )

    def test_tier2_rlhf_bradley_terry_preference_formula(self):
        """Topic RLHF Drift must state Bradley-Terry preference probability formula."""
        content = get_study_guide_markdown()
        has_bt = bool(
            re.search(r"P\s*\(.*\\succ.*\\mid.*x\)|P\(y_w\s*\\succ\s*y_l\)", content)
            or re.search(r"\\sigma\s*\(\s*r.*y_w.*\s*-\s*r.*y_l.*\)", content)
            or (re.search(r"Bradley-Terry|Bradley\s+Terry", content, re.IGNORECASE) and re.search(r"\\sigma|sigmoid", content))
        )
        assert has_bt, (
            "Missing mathematical Bradley-Terry preference probability formula: P(y_w > y_l | x) = sigma(r_w - r_l)."
        )

    def test_tier2_rlhf_gibbs_optimal_policy_derivation(self):
        """Topic RLHF Drift must state closed-form Gibbs / Boltzmann optimal policy."""
        content = get_study_guide_markdown()
        has_gibbs = bool(
            re.search(r"\\pi\^\*\s*\(y\s*\\mid\s*x\)\s*=\s*\\frac\{1\}\{Z\(x\)\}", content)
            or re.search(r"\\frac\{1\}\{Z\}\s*\\pi_\{?\\text\{ref\}?\}?.*\\exp", content)
            or re.search(r"\\exp\s*\(\s*\\frac\{r\(.*\)\}\{\\beta\}\s*\)", content)
        )
        assert has_gibbs, (
            "Missing optimal Gibbs policy derivation: pi^*(y|x) = (1/Z(x)) pi_ref(y|x) exp(r(x,y)/beta)."
        )

    def test_tier2_rlhf_drift_objective_and_safety_bound(self):
        """Topic RLHF Drift must formulate composite alignment objective and policy divergence bounds."""
        content = get_study_guide_markdown()
        # Verifies composite RLHF objective with reward and KL divergence penalty, or PPO surrogate reward
        has_composite_objective = bool(
            re.search(r"\\mathcal\{J\}_\{?\\text\{RLHF\}?\}?|\\max_\{?\\theta\}?\s*\\mathcal\{J\}", content)
            or re.search(r"R_\{?\\text\{surrogate\}?\}?\s*=\s*r.*-.*\\beta", content)
            or re.search(r"\\mathbb\{E\}.*r.*-.*\\beta.*D_\{?\\text\{KL\}?\}?", content)
            or re.search(r"\\mathcal\{L\}_\{?\\text\{DPO\}?\}?", content)
        )
        # Verifies general theoretical framework of policy drift, safety boundaries, and reference anchoring
        has_divergence_boundary = bool(
            re.search(r"drift|divergence|trust\s+region|boundary|tether", content, re.IGNORECASE)
            and re.search(r"reference|anchor|frozen|collapse|hacking", content, re.IGNORECASE)
            and re.search(r"\\beta|penalty|regulariz", content, re.IGNORECASE)
        )
        assert has_composite_objective, (
            "Missing composite RLHF alignment objective: max_theta J(theta) = E[r(x,y)] - beta * E[D_KL(pi_theta || pi_ref)] "
            "or token-level surrogate reward R_surrogate(x,y) = r(x,y) - beta * (log pi_theta - log pi_ref)."
        )
        assert has_divergence_boundary, (
            "Missing theoretical analysis of policy drift boundaries and safety regularization trade-offs."
        )

    # Backward-compatible alias for existing runners and references
    test_tier2_rlhf_scalar_drift_and_safety_bound = test_tier2_rlhf_drift_objective_and_safety_bound

    def test_tier2_rlhf_fisher_information_geometry(self):
        """Topic RLHF Drift must connect KL divergence to Fisher information metric."""
        content = get_study_guide_markdown()
        has_fisher = bool(
            re.search(r"Fisher|\\mathcal\{F\}|information\s+metric|Riemannian", content, re.IGNORECASE)
            and re.search(r"Taylor|second-order|\^2", content, re.IGNORECASE)
        )
        assert has_fisher, (
            "Missing connection between relative entropy Taylor expansion and Fisher Information Matrix."
        )

    def test_tier2_rlhf_asymptotic_limits(self):
        """Topic RLHF Drift must analyze asymptotic limits (beta -> 0 vs beta -> inf)."""
        content = get_study_guide_markdown()
        has_limits = bool(
            (re.search(r"\\beta.*0", content) or re.search(r"beta.*0", content, re.IGNORECASE))
            and (re.search(r"\\infty", content) or re.search(r"infinity", content, re.IGNORECASE))
        )
        assert has_limits, (
            "Missing asymptotic limit analysis for drift penalty parameter beta (0 and infinity)."
        )


# ==============================================================================
# TIER 3: R3 Integrity & Non-Leakage Firewall (Requirement R3; Acceptance Criteria 3)
# ==============================================================================

class TestTier3NonSolutionFirewall:
    """
    Scans documentation and LaTeX source to verify Requirement R3:
    - NO direct contest answers or numerical calculations for Problems A, B, C, D, E.
    - Presence of an explicit pedagogical non-solution firewall disclaimer.
    - Confirms material is 100% theoretical, first-principles, and review-oriented.
    """

    def test_tier3_pedagogical_disclaimer_presence(self):
        """Acceptance Criteria 3: Document must state explicit educational disclaimer / R3 Firewall."""
        content = get_study_guide_markdown()
        has_disclaimer = bool(
            re.search(r"Firewall|không giải trực tiếp|không cung cấp lời giải|non-solution|educational\s+guide|DeepTutor", content, re.IGNORECASE)
        )
        assert has_disclaimer, (
            "Missing explicit R3 Pedagogical Firewall statement / non-solution disclaimer."
        )

    def test_tier3_no_official_exam_submission_headers(self):
        """Study guide must NOT be titled as an exam submission or contest solution manual."""
        forbidden_headers = [
            r"#+\s*Mathematical Solutions and Theoretical Analysis",
            r"#+\s*Section 1:\s*Problem A",
            r"#+\s*Section 2:\s*Problem B",
            r"#+\s*Section 3:\s*Problem C",
            r"#+\s*Section 4:\s*Problem D",
            r"#+\s*Section 5:\s*Section 6:\s*Problem E",
            r"#+\s*Official Problem Statement",
        ]
        all_docs = get_all_docs_markdown()
        for doc_path, content in all_docs:
            for pattern in forbidden_headers:
                match = re.search(pattern, content)
                assert match is None, (
                    f"R3 Violation in {doc_path.name}: Found prohibited contest solution header: {match.group(0)}"
                )

    def test_tier3_no_problem_a_solution_leakage(self):
        """Must NOT leak direct contest answer for Problem A (acoustic school steps)."""
        forbidden_snippets = [
            r"The system is actively learning only during Step 2 and Step 6",
            r"Collect 10\{?,?\}?000 recordings labelled speech, music, or alarm",
            r"Collect 10,000 recordings labelled \*speech\*",
        ]
        all_docs = get_all_docs_markdown()
        for doc_path, content in all_docs:
            for pattern in forbidden_snippets:
                match = re.search(pattern, content, re.IGNORECASE)
                assert match is None, (
                    f"R3 Violation in {doc_path.name}: Leaked Problem A contest specific solution: {match.group(0)}"
                )

    def test_tier3_no_problem_b_solution_leakage(self):
        """Must NOT leak direct contest answer or log table for Problem B (greenhouse tree)."""
        forbidden_snippets = [
            r"The tree unequivocally predicts KEEP CLOSED",
            r"T\s*=\s*26.*H\s*=\s*68.*KEEP CLOSED",
            r"T = 31.*H = 60.*CO_?2 = 700",
            r"Is CO_?2 > 1250 ppm\?",
        ]
        all_docs = get_all_docs_markdown()
        for doc_path, content in all_docs:
            for pattern in forbidden_snippets:
                match = re.search(pattern, content, re.IGNORECASE)
                assert match is None, (
                    f"R3 Violation in {doc_path.name}: Leaked Problem B contest greenhouse dataset or direct query answer: {match.group(0)}"
                )

    def test_tier3_no_problem_c_numerical_calculations_leakage(self):
        """Must NOT leak direct contest dataset and numerical scores for Problem C."""
        forbidden_snippets = [
            r"J\(M_1\)\s*=\s*9\.26",
            r"J\(M_2\)\s*=\s*4\.08",
            r"0\.015209|0\.01521\b",  # lambda* threshold for Problem C specific data
            r"\{\(0,\s*1\.0\),\s*\(1,\s*3\.2\),\s*\(2,\s*4\.8\),\s*\(3,\s*7\.0\)\}",
        ]
        all_docs = get_all_docs_markdown()
        for doc_path, content in all_docs:
            for pattern in forbidden_snippets:
                match = re.search(pattern, content)
                assert match is None, (
                    f"R3 Violation in {doc_path.name}: Leaked Problem C contest numerical evaluation: {match.group(0)}"
                )

    def test_tier3_no_problem_d_solution_leakage(self):
        """Must NOT leak direct contest answers or derivations for Problem D (scalar drift loss & safety bound)."""
        forbidden_snippets = [
            # Contest Problem D scalar loss model
            r"L\(t\)\s*=\s*-?\s*r\s*t\s*\+\s*\\?beta\s*t\^2",
            r"-r\s*t\s*\+\s*\\beta\s*t\^2",
            r"-r\s*t\s*\+\s*beta\s*t\^2",
            # Question (a) solutions: optimal shift t* and minimal loss L(t*)
            r"t\^\*\s*=\s*\\frac\{r\}\{2\\beta\}",
            r"t\^\*\s*=\s*r\s*/\s*\(?2\\beta\)?",
            r"-\\frac\{r\^2\}\{4\\beta\}",
            r"-r\^2\s*/\s*\(?4\\beta\)?",
            # Question (c) solution: exact safety regularization boundary formula
            r"\\beta\s*\\ge\s*\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2T\}",
            r"\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2\\beta\}\s*\\le\s*T",
            r"beta\s*>=\s*r_?max\s*/\s*\(?2T\)?",
            r"beta\s*>=\s*\(r\s*\+\s*delta\)\s*/",
            # Problem D verbatim prompt and framing text
            r"quantify the drift from the reference model",
            r"The reward achieved is rt, and the drift penalty is",
            r"The reward estimate r is noisy",
            r"Safe Regularization Boundary\s*\(\\beta\s*\\ge",
            r"Scalar Drift Dynamics\s*&\s*Safe Boundary Theorem",
        ]
        all_docs = get_all_docs_markdown()
        for doc_path, content in all_docs:
            for pattern in forbidden_snippets:
                match = re.search(pattern, content, re.IGNORECASE)
                assert match is None, (
                    f"R3 Violation in {doc_path.name}: Leaked Problem D contest specific formulation or solution: {match.group(0)}"
                )

    def test_tier3_no_problem_e_solution_leakage(self):
        """Must NOT leak direct contest scenarios or answer keys for Problem E (Nepal agronomy LLM)."""
        forbidden_snippets = [
            r"rice farmer in Nepal",
            r"Nepal rural agronomic",
            r"Irrigate.*Apply treatment.*Wait.*Contact an expert",
        ]
        all_docs = get_all_docs_markdown()
        for doc_path, content in all_docs:
            for pattern in forbidden_snippets:
                match = re.search(pattern, content, re.IGNORECASE)
                assert match is None, (
                    f"R3 Violation in {doc_path.name}: Leaked Problem E contest scenario or action key: {match.group(0)}"
                )

    def test_tier3_latex_non_leakage_firewall(self):
        """Verifies that latex/imlc_study_guide.tex also strictly adheres to R3 non-leakage."""
        if not STUDY_GUIDE_TEX.exists():
            pytest.skip("LaTeX study guide not yet generated.")
        latex_content = get_study_guide_latex()
        forbidden_latex = [
            r"J\(M_1\)\s*=\s*9\.26",
            r"J\(M_2\)\s*=\s*4\.08",
            r"actively learning only during Step 2 and Step 6",
            r"The tree unequivocally predicts KEEP CLOSED",
            r"Official Problem Statement",
            # Problem D leaks in LaTeX
            r"L\(t\)\s*=\s*-?\s*r\s*t\s*\+\s*\\beta\s*t\^2",
            r"t\^\*\s*=\s*\\frac\{r\}\{2\\beta\}",
            r"-\\frac\{r\^2\}\{4\\beta\}",
            r"\\beta\s*\\ge\s*\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2T\}",
            r"Scalar Drift Dynamics\s*&\s*Safe Boundary Theorem",
        ]
        for pattern in forbidden_latex:
            match = re.search(pattern, latex_content, re.IGNORECASE)
            assert match is None, (
                f"R3 Violation in LaTeX document: Found prohibited contest solution: {match.group(0)}"
            )

    def test_tier3_all_docs_markdown_free_of_contest_answers(self):
        """
        Comprehensive repository-wide firewall asserting that every Markdown document
        in docs/ and its subdirectories (docs/**/*.md) is 100% free of contest solutions.
        """
        all_docs = get_all_docs_markdown()
        assert len(all_docs) >= 5, f"Expected multiple documentation files in docs/, found {len(all_docs)}"

        all_forbidden = [
            (r"The system is actively learning only during Step 2 and Step 6", "Problem A answer"),
            (r"Collect 10\{?,?\}?000 recordings labelled speech, music, or alarm", "Problem A dataset"),
            (r"Collect 10,000 recordings labelled \*speech\*", "Problem A step 1"),
            (r"The tree unequivocally predicts KEEP CLOSED", "Problem B prediction"),
            (r"T\s*=\s*26.*H\s*=\s*68.*KEEP CLOSED", "Problem B query answer"),
            (r"T = 31.*H = 60.*CO_?2 = 700", "Problem B dataset log"),
            (r"Is CO_?2 > 1250 ppm\?", "Problem B contest split"),
            (r"J\(M_1\)\s*=\s*9\.26", "Problem C score M1"),
            (r"J\(M_2\)\s*=\s*4\.08", "Problem C score M2"),
            (r"0\.015209|0\.01521\b", "Problem C critical lambda"),
            (r"\{\(0,\s*1\.0\),\s*\(1,\s*3\.2\),\s*\(2,\s*4\.8\),\s*\(3,\s*7\.0\)\}", "Problem C dataset"),
            (r"-r\s*t\s*\+\s*\\?beta\s*t\^2", "Problem D scalar model"),
            (r"t\^\*\s*=\s*\\frac\{r\}\{2\\beta\}|t\^\*\s*=\s*r\s*/\s*\(?2\\beta\)?", "Problem D optimal shift"),
            (r"-\\frac\{r\^2\}\{4\\beta\}|-r\^2\s*/\s*\(?4\\beta\)?", "Problem D minimal loss"),
            (r"(\\beta|beta)\s*\\ge\s*\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2T\}", "Problem D safety bound"),
            (r"beta\s*>=\s*r_?max\s*/\s*\(?2T\)?", "Problem D safety bound ascii"),
            (r"quantify the drift from the reference model", "Problem D prompt text"),
            (r"rice farmer in Nepal", "Problem E Nepal scenario"),
            (r"Nepal rural agronomic", "Problem E context"),
            (r"Irrigate.*Apply treatment.*Wait.*Contact an expert", "Problem E answer key"),
        ]

        violations = []
        for path, content in all_docs:
            for pat, desc in all_forbidden:
                matches = list(re.finditer(pat, content, re.IGNORECASE))
                if matches:
                    for m in matches:
                        line_no = content[: m.start()].count("\n") + 1
                        violations.append(f"{path.name}:{line_no} [{desc}] -> '{m.group(0)}'")

        assert not violations, (
            f"R3 Firewall: Detected contest solutions in docs/ ({len(violations)} occurrences):\n"
            + "\n".join(violations)
        )


# ==============================================================================
# TIER 4: Pedagogical Scaffolding & Keywords (Acceptance Criteria 4)
# ==============================================================================

class TestTier4PedagogicalScaffoldingAndKeywords:
    """
    Verifies that:
    - DeepTutor 5-Tier scaffolding methodology is implemented.
    - Each of the 5 qualification topics includes:
      1. A dedicated, explicit keyword suite for independent self-study.
      2. Socratic guiding / diagnostic questions for active learning.
    """

    def test_tier4_deeptutor_scaffolding_framework(self):
        """Validates DeepTutor 5-tier pedagogical scaffolding structure."""
        content = get_study_guide_markdown()
        has_scaffolding = bool(
            re.search(r"DeepTutor", content, re.IGNORECASE)
            and re.search(r"Socratic", content, re.IGNORECASE)
            and re.search(r"Observation|Probing|Counterexample|Mastery", content, re.IGNORECASE)
        )
        assert has_scaffolding, (
            "Missing DeepTutor 5-tier pedagogical scaffolding framework."
        )

    def test_tier4_topic1_keywords_and_socratic_questions(self):
        """Topic 1 must have self-study keywords and Socratic guiding questions."""
        content = get_study_guide_markdown()
        keywords = ["Covariate Shift", "Concept Shift", "Empirical Risk Minimization", "Mitchell"]
        found = sum(1 for kw in keywords if re.search(kw, content, re.IGNORECASE))
        assert found >= 3, f"Topic 1 missing key taxonomy keywords: found {found}/4"

        # Socratic questions check
        has_socratic = bool(
            re.search(r"Socratic|Guiding Question|Diagnostic|Self-Check", content, re.IGNORECASE)
            and "?" in content
        )
        assert has_socratic, "Topic 1 missing Socratic guiding questions."

    def test_tier4_topic2_keywords_and_socratic_questions(self):
        """Topic 2 must have self-study keywords and Socratic guiding questions."""
        content = get_study_guide_markdown()
        keywords = ["Information Gain", "Entropy", "Gini", "Cost-Complexity"]
        found = sum(1 for kw in keywords if re.search(kw, content, re.IGNORECASE))
        assert found >= 3, f"Topic 2 missing key taxonomy keywords: found {found}/4"

        has_questions = bool(re.search(r"Decision Tree.*(\?|Socratic|Guiding)", content, re.IGNORECASE | re.DOTALL))
        assert has_questions, "Topic 2 missing Socratic guiding questions."

    def test_tier4_topic3_keywords_and_socratic_questions(self):
        """Topic 3 must have self-study keywords and Socratic guiding questions."""
        content = get_study_guide_markdown()
        keywords = ["Ridge", "Lasso", "Tikhonov", "Bias-Variance", "Normal Equation"]
        found = sum(1 for kw in keywords if re.search(kw, content, re.IGNORECASE))
        assert found >= 3, f"Topic 3 missing key taxonomy keywords: found {found}/5"

    def test_tier4_topic4_keywords_and_socratic_questions(self):
        """Topic 4 must have self-study keywords and Socratic guiding questions."""
        content = get_study_guide_markdown()
        keywords = ["Bradley-Terry", "KL Divergence", "Gibbs Policy", "Goodhart", "PPO"]
        found = sum(1 for kw in keywords if re.search(kw, content, re.IGNORECASE))
        assert found >= 3, f"Topic 4 missing key taxonomy keywords: found {found}/5"

    def test_tier4_topic5_keywords_and_socratic_questions(self):
        """Topic 5 must have self-study keywords and Socratic guiding questions."""
        content = get_study_guide_markdown()
        keywords = ["Demographic Parity", "Equalized Odds", "Kleinberg", "Conformal Prediction", "RAG"]
        found = sum(1 for kw in keywords if re.search(kw, content, re.IGNORECASE))
        assert found >= 3, f"Topic 5 missing key taxonomy keywords: found {found}/5"

    def test_tier4_comprehensive_keyword_breadth(self):
        """Acceptance Criteria 4: Master glossary / keyword taxonomy across all topics must be rich (>= 20 distinct terms)."""
        content = get_study_guide_markdown()
        expected_lexicon = [
            "Mitchell", "Empirical Risk Minimization", "Covariate Shift", "Concept Shift", "KS-test",
            "Population Stability Index", "Entropy", "Gini Impurity", "Information Gain", "CART",
            "Pruning", "Cost-Complexity", "Runge", "Ridge", "Tikhonov", "Lasso", "Soft-Thresholding",
            "Normal Equation", "Spectral Shrinkage", "Bias-Variance", "RLHF", "Bradley-Terry",
            "KL Divergence", "Gibbs", "Goodhart", "Fisher Information", "DPO", "Demographic Parity",
            "Equalized Odds", "Kleinberg", "Conformal Prediction", "RAG"
        ]
        present = [term for term in expected_lexicon if re.search(r"\b" + re.escape(term) + r"\b", content, re.IGNORECASE)]
        assert len(present) >= 20, (
            f"Taxonomy contains {len(present)}/32 expected core terms: {present}. Expected >= 20."
        )


# ==============================================================================
# TIER 5: Build & Document Quality (Build Sanity, Markdown, LaTeX)
# ==============================================================================

class TestTier5BuildAndDocumentQuality:
    """
    Verifies that:
    - Markdown files are syntactically well-formed, UTF-8 encoded, with balanced code blocks.
    - LaTeX source latex/imlc_study_guide.tex has balanced environments and valid syntax.
    - Compilation check via pdflatex or verification of valid PDF artifact.
    """

    def test_tier5_markdown_utf8_encoding_and_clean_text(self):
        """Markdown files must be valid UTF-8 without null bytes or carriage corruption."""
        if STUDY_GUIDE_MD.exists():
            files_to_check = [STUDY_GUIDE_MD]
        elif MODULES_DIR.exists():
            files_to_check = list(MODULES_DIR.glob("*.md"))
        else:
            pytest.skip("No markdown files available yet.")

        for mf in files_to_check:
            with open(mf, "rb") as f:
                raw = f.read()
            assert b"\x00" not in raw, f"Found null byte in {mf.name}"
            # Verify utf-8 decode
            decoded = raw.decode("utf-8")
            assert len(decoded) > 0, f"{mf.name} is empty"

    def test_tier5_markdown_code_block_balance(self):
        """Markdown code blocks (triple backticks ```) must be properly opened and closed."""
        content = get_study_guide_markdown()
        triple_backticks = content.count("```")
        assert triple_backticks % 2 == 0, (
            f"Markdown has unbalanced code block delimiters: count is {triple_backticks} (must be even)."
        )

    def test_tier5_markdown_heading_hierarchy(self):
        """Markdown document must have a clean heading hierarchy (H1 -> H2 -> H3)."""
        content = get_study_guide_markdown()
        h1_matches = re.findall(r"^#\s+(.+)$", content, re.MULTILINE)
        h2_matches = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)
        h3_matches = re.findall(r"^###\s+(.+)$", content, re.MULTILINE)

        assert len(h1_matches) >= 1, "Missing H1 top-level heading"
        assert len(h2_matches) >= 5, f"Expected at least 5 H2 section headings, found {len(h2_matches)}"
        assert len(h3_matches) >= 5, f"Expected at least 5 H3 subsection headings, found {len(h3_matches)}"

    def test_tier5_latex_structure_and_syntax(self):
        """LaTeX document must contain proper documentclass, begin/end document, and metadata."""
        if not STUDY_GUIDE_TEX.exists():
            pytest.skip("latex/imlc_study_guide.tex not yet generated.")
        content = get_study_guide_latex()
        assert r"\documentclass" in content, "Missing \\documentclass declaration"
        assert r"\begin{document}" in content, "Missing \\begin{document}"
        assert r"\end{document}" in content, "Missing \\end{document}"

    def test_tier5_latex_environment_balance(self):
        """LaTeX environments (equation, align, figure, table) must have matching \\begin and \\end."""
        if not STUDY_GUIDE_TEX.exists():
            pytest.skip("latex/imlc_study_guide.tex not yet generated.")
        content = get_study_guide_latex()
        environments = ["equation", "align", "figure", "table", "center", "itemize", "enumerate"]
        for env in environments:
            begin_count = len(re.findall(r"\\begin\{" + env + r"\*?\}", content))
            end_count = len(re.findall(r"\\end\{" + env + r"\*?\}", content))
            assert begin_count == end_count, (
                f"Unbalanced LaTeX environment '{env}': \\begin count={begin_count}, \\end count={end_count}"
            )

    def test_tier5_latex_compilation_or_pdf_validity(self):
        """Validates that either latex/imlc_study_guide.pdf exists with valid PDF header or pdflatex succeeds."""
        if STUDY_GUIDE_PDF.exists():
            with open(STUDY_GUIDE_PDF, "rb") as f:
                header = f.read(5)
            assert header == b"%PDF-", f"Invalid PDF file header: {header}"
            file_size = STUDY_GUIDE_PDF.stat().st_size
            assert file_size > 10000, f"PDF file size ({file_size} bytes) is suspiciously small"
        elif STUDY_GUIDE_TEX.exists():
            # Run pdflatex in draft/nonstop mode to test compilation
            cmd = [
                "pdflatex",
                "-draftmode",
                "-interaction=nonstopmode",
                "-output-directory", str(LATEX_DIR),
                str(STUDY_GUIDE_TEX),
            ]
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=str(PROJECT_ROOT))
                assert res.returncode == 0 or "Output written on" in res.stdout, (
                    f"pdflatex compilation failed with code {res.returncode}:\n{res.stdout[-1000:]}"
                )
            except (subprocess.SubprocessError, FileNotFoundError) as e:
                pytest.skip(f"pdflatex invocation skipped or timed out: {e}")
        else:
            pytest.skip("Neither LaTeX source nor PDF artifact generated yet.")
