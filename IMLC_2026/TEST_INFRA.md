# IMLC 2026 Theoretical Study Guide — Test Infrastructure & Quality Assurance Specification

**Document Version**: 1.0.0  
**Author**: Test Writer 1 (E2E Testing Track)  
**Governing Authority**: `d:\02_Learning_Knowledge\IMLC_2026\.agents\ORIGINAL_REQUEST.md` & `PROJECT.md`  
**Working Test Suite**: `tests/test_study_guide.py`

---

## 1. Architectural Overview

The verification test suite for the **International Machine Learning Competition (IMLC 2026) Theoretical Study Guide** is designed to provide automated, reproducible, multi-tiered end-to-end (E2E) quality assurance. The testing architecture guarantees both high mathematical rigor and pedagogical integrity while enforcing an impenetrable educational firewall against contest answer leakage (Requirement R3).

```
========================================================================================
             IMLC 2026 QUALITY ASSURANCE & VERIFICATION TEST ARCHITECTURE
========================================================================================

 [Tier 1: Feature Coverage] --------------> Validates F1-F12: IMLC Structure & Funnel,
                                            5 Qualification Topics, Variational Synthesis.
                                            (Requirements R1 & R2)
        |
 [Tier 2: Boundary & Math Verification] --> Validates explicit mathematical formulas:
                                            L_Ridge, matrix gradient nabla_w J, closed-form
                                            normal equations, soft-thresholding, KL divergence,
                                            Bradley-Terry model, Gibbs optimal policy,
                                            extreme asymptotic limits (lambda, beta -> 0, inf),
                                            composite RLHF objective, and general policy divergence bounds.
        |
 [Tier 3: R3 Non-Solution Firewall] ------> Automated regex scanner detecting and blocking
                                            direct contest solution leaks, specific numerical
                                            results, or exam submission headings.
                                            (Requirement R3 & Acceptance Criteria 3)
        |
 [Tier 4: Pedagogical Scaffolding] -------> Verifies DeepTutor 5-tier Socratic scaffold,
                                            per-topic self-study keywords (>= 5 terms),
                                            and active diagnostic questions.
                                            (Acceptance Criteria 4)
        |
 [Tier 5: Build & Document Quality] ------> Validates Markdown formatting, UTF-8 encoding,
                                            code block balance, heading hierarchy, LaTeX
                                            syntax balance, and PDF compilation.
========================================================================================
```

---

## 2. Requirement-to-Test Traceability Matrix

| Requirement / Feature | Description | Target Deliverable | Test Class & Method |
| :--- | :--- | :--- | :--- |
| **R1 (F1, F2, F3)** | IMLC Landscape, 3-Stage Funnel, Comparison Matrix, Prep Strategy | `docs/IMLC_2026_Study_Guide.md`, `latex/imlc_study_guide.tex` | `TestTier1FeatureCoverage::test_tier1_imlc_structure_and_funnel`<br>`TestTier1FeatureCoverage::test_tier1_competition_comparison_matrix`<br>`TestTier1FeatureCoverage::test_tier1_evaluation_rubric_and_strategy` |
| **R2 (F4)** | Topic 1: ML Production Lifecycle & Distributional Drift | Module 2 & Unified Dossier | `TestTier1FeatureCoverage::test_tier1_topic1_ml_lifecycle_and_drift`<br>`TestTier4PedagogicalScaffoldingAndKeywords::test_tier4_topic1_keywords_and_socratic_questions` |
| **R2 (F5)** | Topic 2: Decision Trees & Information-Theoretic Partitioning | Module 3 & Unified Dossier | `TestTier1FeatureCoverage::test_tier1_topic2_decision_trees`<br>`TestTier4PedagogicalScaffoldingAndKeywords::test_tier4_topic2_keywords_and_socratic_questions` |
| **R2 & AC2 (F6)** | Topic 3: Polynomial Regression & Regularization Mechanics | Module 4 & Unified Dossier | `TestTier1FeatureCoverage::test_tier1_topic3_regularization`<br>`TestTier2BoundaryAndMathVerification::test_tier2_regularization_conceptual_explanation`<br>`TestTier2BoundaryAndMathVerification::test_tier2_regularization_loss_formulas`<br>`TestTier2BoundaryAndMathVerification::test_tier2_regularization_matrix_gradient_derivation`<br>`TestTier2BoundaryAndMathVerification::test_tier2_regularization_closed_form_normal_equations`<br>`TestTier2BoundaryAndMathVerification::test_tier2_regularization_soft_thresholding_operator`<br>`TestTier2BoundaryAndMathVerification::test_tier2_regularization_asymptotic_limits` |
| **R2 & AC2 (F7)** | Topic 4: Frontier Alignment, RLHF & Policy Divergence Dynamics | Module 5 & Unified Dossier | `TestTier1FeatureCoverage::test_tier1_topic4_rlhf_and_drift`<br>`TestTier2BoundaryAndMathVerification::test_tier2_rlhf_drift_conceptual_explanation`<br>`TestTier2BoundaryAndMathVerification::test_tier2_rlhf_kl_divergence_formula`<br>`TestTier2BoundaryAndMathVerification::test_tier2_rlhf_bradley_terry_preference_formula`<br>`TestTier2BoundaryAndMathVerification::test_tier2_rlhf_gibbs_optimal_policy_derivation`<br>`TestTier2BoundaryAndMathVerification::test_tier2_rlhf_drift_objective_and_safety_bound`<br>`TestTier2BoundaryAndMathVerification::test_tier2_rlhf_fisher_information_geometry`<br>`TestTier2BoundaryAndMathVerification::test_tier2_rlhf_asymptotic_limits` |
| **R2 (F8)** | Topic 5: AI Ethics, Algorithmic Fairness & Trustworthy Deployment | Module 6 & Unified Dossier | `TestTier1FeatureCoverage::test_tier1_topic5_ai_ethics_and_deployment`<br>`TestTier4PedagogicalScaffoldingAndKeywords::test_tier4_topic5_keywords_and_socratic_questions` |
| **F9** | Cross-Pillar Variational Synthesis (Tikhonov = Gaussian Relative Entropy) | Module 7 & Unified Dossier | `TestTier1FeatureCoverage::test_tier1_cross_pillar_variational_synthesis` |
| **R3 & AC3 (F11)** | Strict Educational Firewall: Zero Contest Answer or Numerical Leaks | All Markdown & LaTeX docs | `TestTier3NonSolutionFirewall::test_tier3_pedagogical_disclaimer_presence`<br>`TestTier3NonSolutionFirewall::test_tier3_no_official_exam_submission_headers`<br>`TestTier3NonSolutionFirewall::test_tier3_no_problem_a_solution_leakage`<br>`TestTier3NonSolutionFirewall::test_tier3_no_problem_b_solution_leakage`<br>`TestTier3NonSolutionFirewall::test_tier3_no_problem_c_numerical_calculations_leakage`<br>`TestTier3NonSolutionFirewall::test_tier3_no_problem_d_solution_leakage`<br>`TestTier3NonSolutionFirewall::test_tier3_no_problem_e_solution_leakage`<br>`TestTier3NonSolutionFirewall::test_tier3_latex_non_leakage_firewall` |
| **AC4 (F10)** | DeepTutor Socratic Scaffolding & Self-Study Keyword Suites | All Modules & Unified Dossier | `TestTier4PedagogicalScaffoldingAndKeywords::test_tier4_deeptutor_scaffolding_framework`<br>`TestTier4PedagogicalScaffoldingAndKeywords::test_tier4_topic1_keywords_and_socratic_questions` through `topic5`<br>`TestTier4PedagogicalScaffoldingAndKeywords::test_tier4_comprehensive_keyword_breadth` |
| **Quality (F12)** | Syntactic Balance, Clean Formatting, Valid PDF Artifact | Markdown & LaTeX sources | `TestTier5BuildAndDocumentQuality::test_tier5_markdown_utf8_encoding_and_clean_text`<br>`TestTier5BuildAndDocumentQuality::test_tier5_markdown_code_block_balance`<br>`TestTier5BuildAndDocumentQuality::test_tier5_markdown_heading_hierarchy`<br>`TestTier5BuildAndDocumentQuality::test_tier5_latex_structure_and_syntax`<br>`TestTier5BuildAndDocumentQuality::test_tier5_latex_environment_balance`<br>`TestTier5BuildAndDocumentQuality::test_tier5_latex_compilation_or_pdf_validity` |

---

## 3. Progressive Testability Framework

To support concurrent multi-agent development where documentation modules are authored iteratively across Milestones M1 through M4:
1. **Unified Priority**: If the aggregated monograph `docs/IMLC_2026_Study_Guide.md` exists, the test suite verifies the complete compiled document.
2. **Progressive Modular Fallback**: If the unified monograph is being built, the test loader dynamically aggregates available module chapters in `docs/modules/*.md`.
3. **Graceful Skip Protocol**: If an artifact under active generation by another milestone track has not yet been written, tests for that artifact gracefully issue `pytest.skip(...)` with actionable diagnostic information, preventing spurious suite aborts.

---

## 4. Test Execution & Runner Commands

### 4.1 Prerequisites
- Python 3.10+ (tested on Python 3.11.9)
- `pytest` (>= 8.0.0, tested with `pytest 9.1.0`)
- Optional for LaTeX PDF generation: `pdflatex` (MiKTeX 4.26+)

### 4.2 Standard Execution Commands
```powershell
# Execute the full E2E Study Guide test suite
pytest tests/test_study_guide.py -v

# Execute specific test tiers
pytest tests/test_study_guide.py -k "TestTier1" -v  # Tier 1: Feature Coverage
pytest tests/test_study_guide.py -k "TestTier2" -v  # Tier 2: Boundary & Math Verification
pytest tests/test_study_guide.py -k "TestTier3" -v  # Tier 3: R3 Non-Solution Firewall
pytest tests/test_study_guide.py -k "TestTier4" -v  # Tier 4: Pedagogical Scaffolding
pytest tests/test_study_guide.py -k "TestTier5" -v  # Tier 5: Document & Build Sanity

# Fast summary mode with traceback truncation
pytest tests/test_study_guide.py -q --tb=short
```

---

## 5. Quality Thresholds & Pass Criteria

- **Feature Coverage (Tier 1)**: 100% of required topics and competition overview sections must be present. Word count must exceed 2,500 words minimum (comprehensive guide target: 15,000+ words).
- **Mathematical Formulations (Tier 2)**: 100% of explicit formulas ($\mathcal{L}_{Ridge}$, $\nabla_w J$, $(X^T X + \lambda I)^{-1} X^T y$, $\mathcal{S}_\lambda$, $D_{KL}$, Bradley-Terry, Gibbs policy $\pi^*$, Fisher metric expansion, composite RLHF objective $\mathcal{J}_{\text{RLHF}}$, surrogate reward, and safe policy divergence bounds) must be present with rigorous conceptual context.
- **R3 Educational Non-Solution Firewall (Tier 3)**: **Zero-tolerance (0 violations allowed)**. Any occurrence of direct numerical problem answers (e.g. $J(M_1)=9.26$, $J(M_2)=4.08$, greenhouse split $\text{CO}_2 > 1250\text{ ppm}$, acoustic step solution declarations, Problem D contest scalar loss $L(t)=-rt+\beta t^2$, $t^*=\frac{r}{2\beta}$, $\beta \ge \frac{r_{\max}}{2T}$, or Problem E Nepal agronomic scenario answers) will trigger immediate test failure.
- **Pedagogical Taxonomy (Tier 4)**: Every topic must feature at least 4 domain keywords and Socratic diagnostic questions. Master glossary must contain $\ge 20$ unique technical terms.
- **Build Quality (Tier 5)**: Markdown documents must have balanced code blocks and clean UTF-8 encoding. LaTeX documents must compile cleanly or produce a valid PDF artifact.
