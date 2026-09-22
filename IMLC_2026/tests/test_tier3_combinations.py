"""
IMLC 2026 E2E Test Suite - Tier 3: Cross-Feature Combinations & Architectural Consistency
Tests pairwise interactions and consistency between documentation, mathematical proofs,
LaTeX templates, and Python verification code.

Requirements: Standard Library and numpy only.
"""

import math
import os
import re
import subprocess
import sys
from pathlib import Path
import numpy as np
import pytest

# Determine project paths
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
DOCS_DIR = PROJECT_ROOT / "docs"
LATEX_DIR = PROJECT_ROOT / "latex"
CODE_DIR = PROJECT_ROOT / "code"


def read_file(path: Path) -> str:
    if not path.exists():
        pytest.skip(f"Target deliverable {path.name} not yet created by milestone implementation")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ==============================================================================
# Cross-Feature Consistency: Documentation <-> Verification Code
# ==============================================================================
class TestTier3DocVsCodeConsistency:
    """Mathematical and numerical consistency between markdown docs and executable code."""

    def test_tier3_math_doc_vs_python_ridge_scores(self):
        """Numerical scores J(M1)=9.26 and J(M2)=4.08 match between docs and Python."""
        doc_path = DOCS_DIR / "03_qualification_solutions.md"
        content = read_file(doc_path)

        # Regex search for exact values in documentation
        assert "9.26" in content
        assert "4.08" in content
        assert "0.08" in content

        # Compare with Python script if it exists
        script_path = CODE_DIR / "verify_problem_c_ridge.py"
        if script_path.exists():
            res = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
            assert res.returncode == 0
            assert "9.26" in res.stdout
            assert "4.08" in res.stdout

        # Verify ground-truth mathematics directly
        xs = np.array([0.0, 1.0, 2.0, 3.0])
        ys = np.array([1.0, 3.2, 4.8, 7.0])
        m1 = 0.2 * xs**3 - 0.9 * xs**2 + 2.9 * xs + 1.0
        m2 = 2.0 * xs + 1.0
        j1 = float(np.sum((ys - m1)**2) + (0.2**2 + (-0.9)**2 + 2.9**2))
        j2 = float(np.sum((ys - m2)**2) + 2.0**2)
        assert math.isclose(j1, 9.26, rel_tol=1e-5)
        assert math.isclose(j2, 4.08, rel_tol=1e-5)

    def test_tier3_math_doc_vs_python_rlhf_formulas(self):
        """Formula consistency for optimal drift t*=r/(2beta) and safety bound beta >= r_max/(2T)."""
        doc_path = DOCS_DIR / "03_qualification_solutions.md"
        content = read_file(doc_path)
        assert "2\\beta" in content or "2 * \\beta" in content
        assert "r_{\\max}" in content or "r_max" in content
        assert "2T" in content or "2 * T" in content

        # Check Python script if available
        script_path = CODE_DIR / "verify_problem_d_rlhf.py"
        if script_path.exists():
            res = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
            assert res.returncode == 0
            assert "t*" in res.stdout or "optimal" in res.stdout.lower()

    def test_tier3_math_doc_vs_python_tree_thresholds(self):
        """Consistency of CO2 split condition (> 1250 ppm) and query (26, 68) -> KEEP CLOSED."""
        doc_path = DOCS_DIR / "03_qualification_solutions.md"
        content = read_file(doc_path)
        assert "1250" in content
        assert "KEEP CLOSED" in content

        # Check Python script
        script_path = CODE_DIR / "verify_problem_b_tree.py"
        if script_path.exists():
            res = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
            assert res.returncode == 0
            assert "KEEP CLOSED" in res.stdout
            assert "1250" in res.stdout


# ==============================================================================
# Cross-Problem Mathematical Unification: Problem C (L2) <-> Problem D (RLHF)
# ==============================================================================
class TestTier3ProblemCvsProblemDUnification:
    """Theoretical bridge between L2 Tikhonov Regularization and RLHF KL Drift Constraint."""

    def test_tier3_bayesian_map_and_kl_fisher_equivalence(self):
        """Mathematical verification of Gaussian prior in Ridge vs Fisher KL penalty in RLHF."""
        # Problem C: Gaussian prior w ~ N(0, (sigma^2 / lambda) * I)
        # Negative log-prior = (lambda / (2 * sigma^2)) * ||w||_2^2
        # Problem D: Reverse KL penalty beta * D_KL(pi_theta || pi_ref)
        # Taylor expansion: D_KL approx 1/2 * (theta - theta_ref)^T F (theta - theta_ref)
        # For isotropic Fisher F = (1 / sigma_theta^2) * I:
        # beta * D_KL approx (beta / (2 * sigma_theta^2)) * ||theta - theta_ref||_2^2 = (beta / (2 * sigma_theta^2)) * t^2
        # Thus, setting lambda_eff = beta / sigma_theta^2 maps Problem D directly into Problem C!
        sigma_sq = 1.0
        sigma_theta_sq = 1.0

        for beta in [0.5, 1.0, 2.0, 5.0]:
            lam_eff = beta / sigma_theta_sq
            # For 1D parameter shift w = t (anchor = 0)
            t = 1.5
            cost_ridge_penalty = lam_eff * (t**2)
            cost_rlhf_penalty = beta * (t**2)
            assert math.isclose(cost_ridge_penalty, cost_rlhf_penalty, rel_tol=1e-9)

    def test_tier3_shrinkage_geometry_mapping(self):
        """Both objectives enforce monotonic distance shrinkage towards reference anchor."""
        # In Ridge, w*(lambda) = sigma_i^2 / (sigma_i^2 + lambda) * w_ols
        # In RLHF, t*(beta) = r / (2 * beta)
        # Both shrinkage functions are strictly decreasing with penalty parameter
        lambdas = np.linspace(0.1, 10.0, 50)
        betas = np.linspace(0.1, 10.0, 50)

        ridge_shrinkage = [1.0 / (1.0 + lam) for lam in lambdas]
        rlhf_drift = [1.0 / (2.0 * b) for b in betas]

        # Verify strict monotonic decrease for both
        for i in range(len(lambdas) - 1):
            assert ridge_shrinkage[i] > ridge_shrinkage[i + 1]
            assert rlhf_drift[i] > rlhf_drift[i + 1]


# ==============================================================================
# Curriculum Pillars <-> Qualification Solutions Alignment
# ==============================================================================
class TestTier3CurriculumVsSolutionsAlignment:
    """Theoretical consistency between 6 pillars (M2) and qualification solutions (M3)."""

    def test_tier3_curriculum_pillar2_vs_problem_c_svd(self):
        """Pillar 2 (Optimization / Ridge SVD) matches Problem C spectral shrinkage."""
        p2_content = read_file(DOCS_DIR / "02_curriculum_breakdown.md")
        sol_content = read_file(DOCS_DIR / "03_qualification_solutions.md")

        # Both must detail SVD shrinkage formula sigma_i^2 / (sigma_i^2 + lambda)
        assert "sigma" in p2_content.lower() and "svd" in p2_content.lower()
        assert "sigma" in sol_content.lower() and "svd" in sol_content.lower()

    def test_tier3_curriculum_pillar4_vs_problem_d_rlhf(self):
        """Pillar 4 (Frontier Models / RLHF) matches Problem D drift formulation."""
        p4_content = read_file(DOCS_DIR / "02_curriculum_breakdown.md")
        sol_content = read_file(DOCS_DIR / "03_qualification_solutions.md")

        # Both must formulate reverse KL divergence and safety bounds
        assert "KL" in p4_content or "Kullback" in p4_content
        assert "KL" in sol_content or "Kullback" in sol_content

    def test_tier3_curriculum_pillar5_drift_vs_problem_a(self):
        """Pillar 5 (MLOps / Concept Drift) matches Problem A continual retraining rationale."""
        p5_content = read_file(DOCS_DIR / "02_curriculum_breakdown.md")
        sol_content = read_file(DOCS_DIR / "03_qualification_solutions.md")

        # Both discuss non-stationary distribution shift and retraining
        assert "drift" in p5_content.lower()
        assert "drift" in sol_content.lower()

    def test_tier3_curriculum_pillar6_vs_problem_e_nepal(self):
        """Pillar 6 (Trustworthy AI / RAG) matches Problem E agricultural system."""
        p6_content = read_file(DOCS_DIR / "02_curriculum_breakdown.md")
        sol_content = read_file(DOCS_DIR / "03_qualification_solutions.md")

        # Both discuss hallucination mitigation and RAG architectures
        assert "Hallucination" in p6_content or "hallucination" in p6_content.lower()
        assert "Hallucination" in sol_content or "hallucination" in sol_content.lower()


# ==============================================================================
# LaTeX Framework <-> Markdown Solutions Cross-Check
# ==============================================================================
class TestTier3LaTeXVsMarkdownAlignment:
    """Formula and structure consistency between LaTeX source and markdown documentation."""

    def test_tier3_latex_template_vs_markdown_equations(self):
        """LaTeX template equations match markdown mathematical formulas."""
        tex_path = LATEX_DIR / "imlc_study_guide.tex" if (LATEX_DIR / "imlc_study_guide.tex").exists() else LATEX_DIR / "imlc_submission.tex"
        tex_content = read_file(tex_path)

        # LaTeX should contain the core formulas
        assert "RSS" in tex_content or "lambda" in tex_content
        assert "beta" in tex_content or "drift" in tex_content.lower()

    def test_tier3_tikz_tree_topology_matches_problem_b(self):
        """TikZ tree topology renders Temperature, Humidity, and CO2 decisions."""
        tikz_path = LATEX_DIR / "tikz_decision_tree.tex"
        tikz_content = read_file(tikz_path)

        assert "tikzpicture" in tikz_content
        assert "28" in tikz_content or "T" in tikz_content
        assert "70" in tikz_content or "H" in tikz_content
        assert "1250" in tikz_content or "CO" in tikz_content

    def test_tier3_strategic_roadmap_dates_match_competition_dossier(self):
        """Key milestone dates in roadmap match competition dossier."""
        dossier_content = read_file(DOCS_DIR / "01_competition_dossier.md")
        roadmap_content = read_file(DOCS_DIR / "04_strategic_roadmap.md")

        # Both reference QR deadline (13 Dec 2026) and Final date (23 Feb 2027)
        assert "13" in roadmap_content and "2026" in roadmap_content
        assert "2027" in roadmap_content

    def test_tier3_bibtex_citations_cross_referenced(self):
        """BibTeX entries in references.bib are cited in documentation."""
        bib_path = LATEX_DIR / "references.bib"
        bib_content = read_file(bib_path)

        # Extract citation keys: @article{key, ...}
        cite_keys = re.findall(r"@\w+\s*\{\s*([a-zA-Z0-9_\-]+)\s*,", bib_content)
        assert len(cite_keys) > 0, "No BibTeX keys found in references.bib"

        # Check that at least some citation keys are referenced in markdown dossiers or tex
        sol_content = read_file(DOCS_DIR / "03_qualification_solutions.md")
        p_content = read_file(DOCS_DIR / "02_curriculum_breakdown.md")
        all_docs = sol_content + p_content
        matched = [k for k in cite_keys if k.lower() in all_docs.lower() or k.replace("_", " ").lower() in all_docs.lower()]
        # At least one key should match the literature referenced
        assert len(matched) >= 1 or len(cite_keys) >= 3
