# Project: IMLC 2026 Qualification Round Theoretical Study Guide

## Architecture
- **Document Output Layers**:
  - Educational Markdown Comprehensive Dossier: `docs/IMLC_2026_Study_Guide.md`
  - Publication-grade LaTeX Monograph: `latex/imlc_study_guide.tex` -> `latex/imlc_study_guide.pdf`
- **Core Pedagogical Framework**:
  - DeepTutor 5-Tier Socratic Scaffolding (Observation -> Probing -> Minimal Counterexample -> Abstract Pattern -> Autonomous Mastery)
  - Mathematical Rigor & Visual Intuition: Explicit loss functions, matrix gradients, closed-form solutions, variational proofs, and ASCII/Mermaid conceptual schematics
  - Strict Educational Firewall (R3): Zero numerical answers, zero contest test cases, pure first-principles knowledge
- **Verification & Testing Infrastructure**:
  - Automated test assertions in `tests/test_study_guide.py` verifying R1, R2, R3 compliance, formula existence, and keyword presence
  - Compilation verification of LaTeX/PDF build

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F1 | IMLC Structure & Funnel | 3-stage competition funnel (Qualification, Pre-Final, Final), rules, timelines | M1 | Survey (Explorer 2) |
| F2 | ML Competition Matrix | Multi-dimensional comparison: IMLC vs Kaggle vs IOI/ICPC vs IOAI vs NeurIPS | M1 | Survey (Explorer 2) |
| F3 | Evaluation Rubric & Strategy | 4-tier senior rubric, 3-pass paper mining, time management, 5 common pitfalls | M1 | Survey (Explorer 2) |
| F4 | Topic 1: ML Lifecycle & Drift | Mitchell's formulation, parameter vs inference, covariate/concept drift, KS-test, PSI | M2 | Survey (Explorer 3) |
| F5 | Topic 2: Decision Trees | Geometry of axis-aligned splits, entropy, Gini, CART cost-complexity pruning | M2 | Survey (Explorer 3) |
| F6 | Topic 3: Regularization | L2 Ridge gradient & closed-form, L1 Lasso soft-thresholding, bias-variance proof | M2 | Survey (Explorer 3) |
| F7 | Topic 4: RLHF & KL Drift | Bradley-Terry, PPO KL penalty, optimal Gibbs policy derivation, Fisher metric | M3 | Survey (Explorer 3) |
| F8 | Topic 5: AI Ethics & Deployment | Fairness criteria, Kleinberg theorem proof, conformal prediction, RAG governance | M3 | Survey (Explorer 3) |
| F9 | Variational Synthesis | Formal equivalence between L2 Tikhonov regularization and Gaussian Relative Entropy | M3 | Survey (Explorer 3) |
| F10 | Self-Study Taxonomies | Organized self-study keyword suites and Socratic diagnostic prompts for all 5 topics | M4 | Survey (Explorer 3) |
| F11 | R3 Non-Solution Firewall | Independent verification confirming zero direct contest solutions or numerical leaks | M4 | Survey (All) |
| F12 | Publication Monograph | Unified Markdown dossier in docs/ and compiled PDF in latex/ with clean toolchain | M4 | Survey (Explorer 1) |

## Milestones
| # | Name | Scope | Dependencies | Status | Key Outputs |
|---|------|-------|-------------|--------|-------------|
| M1 | IMLC Landscape & Framework | Features F1, F2, F3: Competition overview, comparison matrix, strategic handbook | none | DONE | IMLC Dossier & Strategy (`docs/modules/module1_imlc_landscape.md`, `docs/01_competition_dossier.md`, `docs/04_strategic_roadmap.md`) |
| M2 | Theoretical Core Part 1 | Features F4, F5, F6: ML Lifecycle & Drift, Decision Trees, Regularization & Math Proofs | M1 | DONE | Theoretical Core Modules 2-4 (`docs/modules/module2_ml_lifecycle.md`, `docs/modules/module3_decision_trees.md`, `docs/modules/module4_regularization.md`) |
| M3 | Theoretical Core Part 2 | Features F7, F8, F9: RLHF & KL Drift, AI Ethics/Fairness, Variational Synthesis | M2 | DONE | Theoretical Core Modules 5-7 (`docs/modules/module5_rlhf_divergence.md`, `docs/modules/module6_ethics_deployment.md`, `docs/modules/module7_cross_pillar_synthesis.md`) |
| M4 | Synthesis, Publication & Verification | Features F10, F11, F12: Unified Markdown, LaTeX/PDF compilation, test suite & audit | M3 | DONE | Unified Study Guide & LaTeX PDF (`docs/IMLC_2026_Study_Guide.md`, `latex/imlc_study_guide.tex`, `latex/imlc_study_guide.pdf`), Gate 3 PASS (240/240 tests pass, 0 leaks) |

## Interface Contracts
### M1 ↔ M2, M3
- M1 provides the pedagogical taxonomy, rubric expectations, and uniform chapter template (Pedagogical Overview -> Conceptual Intuition -> Mathematical Derivations -> DeepTutor Socratic Scaffolding -> Keywords).
- M2 and M3 implement the core theoretical content conforming strictly to this chapter template.

### M2, M3 ↔ M4
- M2 and M3 output markdown chapter deliverables into `docs/modules/`.
- M4 aggregates all chapters into `docs/IMLC_2026_Study_Guide.md` and `latex/imlc_study_guide.tex`.
- M4 runs the E2E verification suite (`pytest tests/test_study_guide.py`) and compiles `imlc_study_guide.pdf`.

## Code Layout
- `docs/IMLC_2026_Study_Guide.md` : Complete unified study guide dossier
- `docs/modules/` : Modular chapter drafts (Module 1 to Module 6)
- `latex/imlc_study_guide.tex` : Complete publication-grade LaTeX document
- `latex/imlc_study_guide.pdf` : Compiled PDF artifact
- `tests/test_study_guide.py` : Comprehensive automated audit test suite
