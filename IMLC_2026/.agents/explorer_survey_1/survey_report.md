# Comprehensive Survey Report: Workspace Assets, Codebase & Pedagogical Gap Analysis
**International Machine Learning Competition (IMLC 2026) — Qualification Round Study Dossier**

- **Author**: Explorer 1 (Survey — Codebase & Assets)
- **Agent Identity**: `teamwork_preview_explorer` (Conv ID: `1392f217-c961-4fa9-a9d4-9c881b48c078`)
- **Parent Orchestrator**: `orchestrator_1` (Conv ID: `d108cbbb-577a-49c6-bb18-c13c2cc3f05b`)
- **Working Directory**: `d:\02_Learning_Knowledge\IMLC_2026\.agents\explorer_survey_1`
- **Date & Timestamp**: 2026-09-18T12:23:00Z
- **Reference Request**: `d:\02_Learning_Knowledge\IMLC_2026\.agents\ORIGINAL_REQUEST.md`

---

## 1. Executive Summary

A comprehensive, multi-angle technical survey was executed across the `d:\02_Learning_Knowledge\IMLC_2026` workspace. The repository houses a fully developed, publication-grade academic repository comprising over **280 KB of structured markdown documentation**, a complete **15-page LaTeX publication template (`imlc_submission.tex` / `imlc_submission.pdf`)**, **4 modular Python verification scripts**, and an exhaustive **5-tier test harness with 194 automated pytest test cases (100% pass rate)**.

### Core Survey Findings & Critical Strategic Insight:
1. **Asset Wealth & Theoretical Depth**:
   - The workspace contains authoritative information on the IMLC competition structure (`docs/01_competition_dossier.md`), an exhaustive 6-pillar mathematical syllabus (`docs/02_curriculum_breakdown.md`), formal solution derivations (`docs/03_qualification_solutions.md`), and a 16-week preparation roadmap with scientific paper reading protocols (`docs/04_strategic_roadmap.md`).
   - The toolchains are fully operational: Python 3.11 with `numpy` and `pytest`, as well as MiKTeX 64-bit with `pdflatex`, `xelatex`, and `latexmk`.

2. **The Crucial Alignment Gap (Direct Solutions vs. Pedagogical Study Guide)**:
   - **Current Asset State**: The existing `docs/03_qualification_solutions.md`, `latex/imlc_submission.tex`, and Python verification scripts (`code/`) were created as a **direct contest submission** (scoring 25/25 pts), solving the exact numbers and specific questions of Problems A, B, C, D, and E (e.g. calculating $J(M_1)=9.26$ vs $J(M_2)=4.08$, exact threshold $\text{CO}_2 \le 1250\text{ ppm}$, and verifying individual school audio pipeline steps).
   - **Authoritative User Request (`ORIGINAL_REQUEST.md`)**: The user has explicitly mandated a **pedagogical study guide / review dossier (Tài liệu ôn tập)** in **DeepTutor Mode**:
     - **R1**: Comprehensive overview of IMLC format, rules, and comparison to other ML competitions.
     - **R2**: Conceptual, visual, and moderate mathematical foundations for the 5 problem topics (ML Lifecycle, Decision Trees, Polynomial Ridge Regularization, RLHF & KL Divergence, AI Ethics / Deployment).
     - **R3**: **STRICTLY NO DIRECT SOLUTIONS OR ANSWERS** to specific contest questions (Problems A–E).
     - **Acceptance Criteria**: Dual conceptual + mathematical explanation for Regularization and RLHF Drift; strict cross-check ensuring NO answer leaks; keywords for student self-study.
   - **Strategic Implication**: The existing assets represent the "Ground Truth / Answer Key" and provide high-quality mathematical proofs and figures that can be leveraged. However, to fulfill `ORIGINAL_REQUEST.md`, the team must produce a dedicated **Study Guide / Review Dossier** that abstracts away the specific answers/numbers into generalized educational frameworks, guided questions (Socratic scaffolding), conceptual diagrams, and self-study keyword banks.

---

## 2. Complete Repository Inventory & Asset Catalog

The root directory `d:\02_Learning_Knowledge\IMLC_2026` contains five main operational folders plus the agent metadata directory:

```
d:\02_Learning_Knowledge\IMLC_2026\
├── .agents/
│   ├── ORIGINAL_REQUEST.md               # User prompt & acceptance rubric (2,191 bytes)
│   ├── orchestrator_1/                   # Orchestrator dispatch, briefing, progress
│   ├── explorer_survey_1/                # (This agent) Codebase & asset survey
│   ├── explorer_survey_2/                # IMLC competition structure survey
│   └── explorer_survey_3/                # Pedagogical scope survey
├── docs/
│   ├── 01_competition_dossier.md         # 736 lines | 65,289 bytes | Governance, rules, scoring, prizes
│   ├── 02_curriculum_breakdown.md        # 1,035 lines | 89,827 bytes | 6-pillar mathematical syllabus
│   ├── 03_qualification_solutions.md     # 902 lines | 67,705 bytes | Formal solutions to Problems A-E
│   └── 04_strategic_roadmap.md           # 633 lines | 57,276 bytes | 16-week plan, 3-pass paper reading
├── latex/
│   ├── imlc_submission.tex               # 683 lines | 42,902 bytes | Formal LaTeX submission paper
│   ├── imlc_submission.pdf               # 15 pages | 670,635 bytes | Precompiled submission PDF
│   ├── tikz_decision_tree.tex            # 96 lines | 2,806 bytes | TikZ vector graphics for Problem B
│   ├── references.bib                    # 31 entries | 9,365 bytes | Peer-reviewed academic bibliography
│   └── [auxiliary files]                 # .aux, .bbl, .blg, .log, .out, .toc
├── code/
│   ├── verify_problem_b_tree.py          # 581 lines | 22,967 bytes | Decision tree & information theory
│   ├── verify_problem_c_ridge.py         # 427 lines | 18,500 bytes | Ridge regression, SVD shrinkage, bias-variance
│   ├── verify_problem_d_rlhf.py          # 459 lines | 18,829 bytes | RLHF drift loss, safety limit, Gibbs policy
│   └── run_all_verifications.py          # 429 lines | 16,576 bytes | Master verification runner (18 tests)
├── tests/
│   ├── test_tier1_features.py            # 1,074 lines | 45,112 bytes | 104 tests (FI-01 to FI-27 coverage)
│   ├── test_tier2_boundaries.py          # 367 lines | 14,878 bytes | 16 tests (Boundary & corner cases)
│   ├── test_tier3_combinations.py        # 266 lines | 11,292 bytes | 13 tests (Cross-feature consistency)
│   ├── test_tier4_applications.py        # 424 lines | 18,708 bytes | 5 tests (Real-world scenarios)
│   ├── test_tier5_adversarial.py         # 650 lines | 27,282 bytes | 25 tests (Numerical & adversarial tests)
│   └── run_e2e_tests.py                  # 173 lines | 6,072 bytes | Master pytest execution harness
└── README.md                             # 63 lines | 4,059 bytes | Master project overview
```

### Table 1: Codebase & Asset Statistics
| Directory | File Count | Total Size | Primary Language / Format | Verification Status |
| :--- | :---: | :---: | :---: | :---: |
| `docs/` | 4 | 280,097 bytes (~280 KB) | Markdown with LaTeX math ($\LaTeX$) | Audited & cross-referenced |
| `latex/` | 10 (4 source + 6 aux) | 737,477 bytes (~737 KB) | LaTeX, TikZ, BibTeX, PDF | Compiles with `pdflatex` |
| `code/` | 4 | 76,872 bytes (~77 KB) | Python 3 (NumPy, stdlib) | 18/18 verifications pass |
| `tests/` | 6 | 123,344 bytes (~123 KB) | Pytest (Python 3) | 194/194 test cases pass |
| Root | 2 | 6,250 bytes (~6.2 KB) | Markdown | Verified |

---

## 3. Analysis of Existing Documentation (`docs/`)

### 3.1 `docs/01_competition_dossier.md` (Competition Architecture & Regulations)
- **Authority**: Edu.Harbour GbR (Hamburg, Germany), co-founded by Dr. Rami Aly (University of Cambridge) and Fabian Schneider.
- **Operating Model**: Yunus Social Enterprise (non-loss, non-dividend, 100% reinvestment of nominal €12 Pre-Final fee into cloud grading, proctoring, financial aid, and $1,500 prize pool).
- **Three-Stage Competition Funnel**:
  1. *Stage I: Qualification Round (Vòng Sơ loại)*: Open-book, take-home, 5 problems (A–E), 25 points maximum. Scoring $\ge 17$ points (Senior) or $\ge 12$ points (Junior) guarantees advancement to Pre-Final. Free entry.
  2. *Stage II: Pre-Final Round (Vòng Bán kết)*: Timed 60-minute written examination based on a designated scientific research paper released 48 hours in advance. Supervised via strict camera/screen proctoring and dynamic QR-code mobile uploads.
  3. *Stage III: Final Round (Vòng Chung kết)*: 40-minute live proctored examination (20 questions, 2 minutes/question, non-backtracking, negative marking).
- **Senior Division Criteria**: University students or candidates aged $\ge 19$ on the qualification submission deadline. Differential evaluation standards apply higher mathematical rigor and deeper proof requirements compared to Junior division.
- **Awards & Recognition**: $1,500 USD cash prize pool (Senior 1st: $400, 2nd: $250, 3rd: $150; Junior 1st: $300, 2nd: $150, 3rd: $100; National: $150). Gold, Silver, Bronze medals distributed in a 1:2:3 ratio among the top 20% of finalists. Dedicated **"Special Honour for Digital Submission"** awarded for publication-grade digital formatting (LaTeX).

### 3.2 `docs/02_curriculum_breakdown.md` (Six-Pillar Mathematical Syllabus)
An exhaustive theoretical compendium detailing:
- **Pillar 1: Core Machine Learning Methods**: Bayes optimal classifier, Bayes risk $R^*$, Empirical Risk Minimization (ERM), VC-dimension bounds, decision tree partitioning algorithms (ID3, C4.5, CART), Shannon entropy, Gini impurity, Ensemble methods (Bagging, Random Forests, AdaBoost, Gradient Boosting, XGBoost), RKHS and SVM Wolfe dual formulations.
- **Pillar 2: Optimization Theory & Dynamics**: Convex analysis, subgradients, SGD with momentum, Adam, AdamW decoupled weight decay proof, Lagrangian duality, KKT conditions, Regularization geometry ($L_1$ sparsity diamond vs. $L_2$ shrinkage sphere), and Bayesian MAP equivalence (Laplace vs. Gaussian priors).
- **Pillar 3: Deep Learning Formulations & Architectures**: Universal approximation theorems, matrix backpropagation calculus, CNN spatial geometry, Scaled Dot-Product Attention variance proof ($\text{Var}(q^T k) = d_k$), Rotary Position Embedding (RoPE) complex rotation geometry, and loss landscape geometry.
- **Pillar 4: Frontier Models & RLHF Alignment**: Autoregressive causal language modeling, Bradley-Terry preference probability model, PPO actor-critic objectives, Direct Preference Optimization (DPO) closed-form reparameterization, reverse KL divergence mode-seeking behavior, Fisher information metric proxy, and policy drift safety envelopes.
- **Pillar 5: Real-World Applications & MLOps**: Full production lifecycle (Data curation, Training, Generalization validation, Serialization/Deployment, Real-time serving, Continual retraining loop), Post-Training Quantization (PTQ) INT8 affine mapping, structured/unstructured pruning, distribution shifts (Covariate Shift vs. Concept Shift), two-sample Kolmogorov-Smirnov test, and Population Stability Index (PSI).
- **Pillar 6: Trustworthy AI, Safety & Governance**: Fairness metrics (Demographic Parity vs. Equalized Odds), proof of Kleinberg’s Impossibility Theorem, adversarial robustness via min-max optimization (FGSM, PGD), hallucination mitigation via grounded Retrieval-Augmented Generation (RAG) and conformal prediction, and regulatory compliance (EU AI Act risk tiers).

### 3.3 `docs/03_qualification_solutions.md` (Current Direct Problem Solutions)
This document is a complete, publication-grade formal solution manual for the 2026 Qualification Round:
- **Section 1 (Problem A)**: 6 lifecycle steps classified into Data Collection, Training, Evaluation, Deployment, Inference. Formal proof using Tom Mitchell's $(T, P, E)$ framework and Vapnik's ERM that learning occurs **only during Step 2 and Step 6** ($\Delta\theta \neq \mathbf{0}$). Analysis of acoustic covariate shift vs. concept shift in school deployment.
- **Section 2 (Problem B)**: Analysis of 6 greenhouse telemetry records $(T, H, \text{CO}_2)$. Part (a) query $(26^\circ\text{C}, 68\%)$ evaluates to **KEEP CLOSED**. Part (b) identifies failure on rows 5 and 6 (accuracy 66.7%). Calculates Shannon entropy ($H=1.0\text{ bit}$) and Gini impurity ($G=0.50$). Computes information gain across split candidates ($750, 950, 1250, 1475\text{ ppm}$) and identifies optimal split at $\text{CO}_2 \le 1250\text{ ppm}$ yielding $IG=1.0\text{ bit}$ and $100\%$ accuracy. Provides ASCII tree, Boolean propositional logic, JSON schema, and TikZ code.
- **Section 3 (Problem C)**: Dataset of 4 points: $\{(0, 1.0), (1, 3.2), (2, 4.8), (3, 7.0)\}$. Model $M_1(x) = 0.2x^3 - 0.9x^2 + 2.9x + 1$ has $\text{RSS}(M_1) = 0.00$, penalty $\sum a_i^2 = 9.26 \implies J(M_1) = 9.26$. Model $M_2(x) = 2x + 1$ has $\text{RSS}(M_2) = 0.08$, penalty $\sum a_i^2 = 4.00 \implies J(M_2) = 4.08$. Scoring rule selects $M_2$. Explains Runge's phenomenon, Occam's razor, critical threshold $\lambda^* \approx 0.5596$, SVD spectral shrinkage factors $f_j = \frac{s_j^2}{s_j^2 + \lambda}$, and analytical bias-variance curves.
- **Section 4 (Problem D)**: Objective $L(t) = -rt + \beta t^2$. First derivative $-r + 2\beta t = 0 \implies t^* = \frac{r}{2\beta}$, minimum loss $L(t^*) = -\frac{r^2}{4\beta}$. Second derivative $2\beta > 0$ proves strict convexity. Asymptotics: $\beta \to 0 \implies t^* \to \infty$ (unconstrained reward hacking / Goodhart's law); $\beta \to \infty \implies t^* \to 0$ (frozen policy). Proves Safe Boundary Theorem: $\beta \ge \frac{r_{\max}}{2T} \iff \sup_{r \in (0, r_{\max}]} t^*(r) \le T$. Unifies with Problem C's $L_2$ regularization. Senior extension derives Gibbs policy via calculus of variations and second-order Taylor expansion proving equivalence to Fisher information geometry.
- **Section 5 (Quantitative Cross-Analysis)**: 11-dimension comparative matrix between Ridge ($L_2$) and RLHF quadratic drift penalty, Bayesian MAP equivalence with Gaussian priors.
- **Section 6 (Problem E)**: Deployment of agronomic LLM in rural Nepal. Evaluates 3 transformative opportunities (multimodal vernacular NLP, holistic multi-source in-context agronomic synthesis, near-zero marginal cost scaling) and 3 systemic failure modes (toxic agrochemical hallucination, OOD Himalayan microclimate/landrace mismatch, automation bias & liability void). Proposes trustworthy AI architecture combining grounded RAG, conformal prediction sets, and human extension officer escalation.

### 3.4 `docs/04_strategic_roadmap.md` (Preparation Roadmap & Tactics)
- **16-Week Chronological Preparation Roadmap**: Divided into 5 distinct phases (Phase 1: Core Foundations; Phase 2: Optimization & Deep Learning; Phase 3: Frontier Models & Qualification Sprint; Phase 4: Scientific Paper Mining; Phase 5: High-Speed Live Sprint).
- **The 3-Pass Scientific Literature Mining Protocol**: Structured methodology for dissecting research papers in 48 hours for Stage II (Pre-Final):
  - Pass 1 (5–10 min): Title, abstract, figures, conclusion, problem statement.
  - Pass 2 (20–25 min): Core methodology, equations, experimental setups, key results.
  - Pass 3 (20 min): Edge cases, mathematical proofs, failure modes, virtual re-implementation.
  - 15-point critical evaluation checklist.
- **Round-by-Round Examination Tactics**: Pacing strategies for 60-min Pre-Final and 40-min Final (non-backtracking live exam), mental math estimation shortcuts (logarithms, sigmoid, softmax, entropy).
- **LaTeX Best Practices**: Modular typesetting, TikZ styling, BibTeX management to win the "Special Honour for Digital Submission".

---

## 4. LaTeX Framework & Typesetting Infrastructure (`latex/`)

The workspace features an established LaTeX publishing pipeline designed to meet the criteria for the **"Special Honour for Digital Submission"**:

### 4.1 Document Class & Styling Configurations
- **Document Class**: `\documentclass[11pt,a4paper]{article}`
- **Geometry**: `\usepackage[margin=1in]{geometry}` with microtypography optimizations (`microtype`, `lmodern`).
- **Running Headers & Footers**: Configured via `fancyhdr`:
  - Header Left: `\textsc{IMLC 2026} --- Senior Division`
  - Header Center: `\textbf{Qualification Round Formal Solutions}`
  - Header Right: `Candidate ID: \texttt{[SENIOR-2026-VN-0428]}`
  - Footer Left: `\textit{Special Honour for Digital Submission}`
  - Footer Right: `Page \thepage\ of \pageref{LastPage}`
- **Mathematical Environments**: Powered by `amsmath`, `amssymb`, `amsfonts`, `amsthm`, `mathtools`, and `bm`. Defined theorem styles for `definition`, `problem`, `example`, `theorem`, `lemma`, `proposition`, `corollary`, `remark`, and `solution`.
- **Custom Mathematical Operators**: `\argmax`, `\argmin`, `\E`, `\Var`, `\Cov`, `\Tr`, `\norm`, `\KL`.
- **Cross-Referencing**: Configured with `hyperref` (custom color links: blue links, green citations) and `cleveref` (`\cref`).

### 4.2 Vector Graphics & Algorithm Typesetting
- **TikZ Diagram (`latex/tikz_decision_tree.tex`)**: Professional vector visualization of the Problem B decision tree with color-coded decision nodes (blue), positive action leaves (green: "OPEN ROOF"), and negative action leaves (red: "KEEP CLOSED"). Includes explicit branch probability and condition annotations.
- **PGFPlots**: Integrated with `\pgfplotsset{compat=1.18}` for high-precision plotting.
- **Algorithms**: Typeset using `algorithm2e` with boxed formatting and line numbers.

### 4.3 Academic Bibliography (`latex/references.bib`)
Contains **31 peer-reviewed citations** properly formatted in BibTeX, spanning:
- Classical Foundations: Mitchell (1997), Vapnik (1998), Quinlan (1986 ID3), Breiman (1984 CART, 2001 Random Forests), Chen & Guestrin (2016 XGBoost), Cortes & Vapnik (1995 SVM).
- Modern Architectures: Vaswani et al. (2017 Transformers), Su et al. (2024 RoFormer / RoPE), Kingma & Ba (2014 Adam), Loshchilov & Hutter (2019 AdamW).
- Alignment & RLHF: Christiano et al. (2017 Deep RL from Human Preferences), Ouyang et al. (2022 InstructGPT), Rafailov et al. (2023 DPO), Schulman et al. (2017 PPO).
- Trustworthy AI: Kleinberg et al. (2016 Algorithmic Fairness), Hardt et al. (2016 Equal Opportunity), Madry et al. (2018 Adversarial Robustness), Angelopoulos & Bates (2021 Conformal Prediction).

### 4.4 Compilation Toolchain Verification
Local system check confirmed:
- `C:\Users\Admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe` is installed and functioning.
- `latexmk` and `xelatex` are available.
- `latex/imlc_submission.pdf` is already pre-compiled (15 pages, 670 KB), displaying complete formatting.

---

## 5. Computational Codebase & Verification Scripts (`code/`)

All computational scripts are written in standard Python 3.11 with `numpy` as the sole numerical dependency (no black-box ML frameworks like PyTorch or Scikit-Learn), adhering to first-principles computation.

### Table 2: Python Verification Modules Overview
| Script Path | Purpose | Key Functions & Classes | Key Algorithms Implemented |
| :--- | :--- | :--- | :--- |
| `code/verify_problem_b_tree.py` | Decision Tree & Information Theory Verification | `shannon_entropy()`, `gini_impurity()`, `information_gain()`, `gini_gain()`, `DecisionTreeNode`, `GreenhouseDecisionTree`, `evaluate_co2_splits()` | Shannon entropy calculation, Gini impurity, continuous feature candidate midpoint splitting, recursive tree traversal and accuracy benchmarking. |
| `code/verify_problem_c_ridge.py` | Polynomial Ridge Regularization & SVD Shrinkage | `evaluate_polynomial()`, `compute_rss()`, `compute_l2_penalty()`, `compute_score_j()`, `solve_ridge_regression()`, `compute_svd_spectral_shrinkage()`, `compute_bias_variance_decomposition()`, `compute_critical_threshold()` | Polynomial Horner evaluation, Normal Equations $(X^TX + \lambda I)^{-1}X^Ty$, SVD decomposition $X = U \Sigma V^T$, spectral filter factors $f_j = \frac{s_j^2}{s_j^2 + \lambda}$, bias-variance integral curves. |
| `code/verify_problem_d_rlhf.py` | RLHF Drift Penalty Optimizer & Safety Bounds | `rlhf_drift_loss()`, `analytical_optimal_drift()`, `analytical_minimal_loss()`, `numerical_optimize_drift()`, `verify_safety_bound()`, `simulate_token_space_rlhf()`, `verify_fisher_quadratic_proxy_equivalence()` | Closed-form calculus vs. Golden-section numerical optimization, Monte Carlo safety bound validation ($N=10{,}000$), Gibbs optimal policy softmax simulation, Fisher Information Metric Hessian matching. |
| `code/run_all_verifications.py` | Master Verification Harness | `VerificationReportGenerator`, `main()` | Automated execution of 18 test cases across Problems B, C, D; high-precision timer; structured ASCII table output with pass/fail tracking. |

### Execution Performance:
Executing `python code/run_all_verifications.py` synchronously executes all 18 test cases (TC-B01 to TC-D06) in **284.64 ms** with **100% pass rate** and zero failures.

---

## 6. Multi-Tier Automated Test Suite (`tests/`)

The repository implements an industrial-strength, multi-tier testing pyramid using `pytest`:

```
                       [ Tier 5: Adversarial & Numerical Hardening ]   (25 tests)
                    [ Tier 4: Real-World Applications & Workflows ]    (5 tests)
                 [ Tier 3: Cross-Paradigm Consistency & Alignment ]    (13 tests)
              [ Tier 2: Boundary Conditions & Extreme Parameters ]     (16 tests)
           [ Tier 1: Core Feature Coverage (FI-01 to FI-27) ]          (104 tests)
```

### Table 3: Test Suite Architecture & Results
| Tier | Test File | Test Count | Scope & Focus | Status |
| :---: | :--- | :---: | :--- | :---: |
| **Tier 1** | `test_tier1_features.py` | 104 | Complete functional verification of Features FI-01 through FI-27. Validates every requirement across competition rules, 6 syllabus pillars, problem statements, mathematical proofs, roadmap timeline, and code modules. | **104/104 PASS** |
| **Tier 2** | `test_tier2_boundaries.py` | 16 | Extreme limits and corner cases: $\lambda \to 0^+$, $\lambda \to \infty$, $\beta \to 0^+$, $\beta \to \infty$, singular/ill-conditioned matrices, zero-variance features, pure partitions ($H=0, G=0$), uniform distributions, and base rate disparities. | **16/16 PASS** |
| **Tier 3** | `test_tier3_combinations.py` | 13 | Multi-feature consistency: verifying Markdown equations match Python implementations, Problem C vs D Bayesian/Fisher equivalence, curriculum pillar alignments, TikZ diagram topology matching code, and BibTeX citations matching text references. | **13/13 PASS** |
| **Tier 4** | `test_tier4_applications.py` | 5 | End-to-end operational workflows: senior submission grading workflow simulation, continuous greenhouse sensor telemetry streaming, Ridge cross-validation search, RLHF policy drift governance monitoring, and Nepal agricultural advisory RAG pipeline. | **5/5 PASS** |
| **Tier 5** | `test_tier5_adversarial.py` | 25 | Adversarial stability: perfect multicollinearity, condition number decay, sub-nanometer perturbation around crossover threshold $\lambda^*$, negative reward hacking, LogSumExp tricks under extreme logits, and clipped KL safety boundaries. | **25/25 PASS** |
| **TOTAL** | `run_e2e_tests.py` | **194** | Master automated execution across all 5 tiers. Completed in 8.47s. | **194/194 PASS (100%)** |

---

## 7. Problem Outlines & Topic Breakdown (Problems A–E)

The 5 qualification problems test key concepts in modern machine learning:

### Table 4: Problem Outlines, Core ML Topics, and Underlying Mathematical Frameworks
| Problem | Official Title / Context | Core ML Pillar / Concept | Mathematical Formulations & Objects | Visual / Geometric Models |
| :---: | :--- | :--- | :--- | :--- |
| **A** | Acoustic Monitoring Lifecycle | **ML Production Lifecycle & Concept Drift** (Pillar 5) | • Mitchell’s $(T, P, E)$ framework<br>• Vapnik’s Empirical Risk $\hat{R}_n(\theta) = \frac{1}{n} \sum \ell(f_\theta(x_i), y_i)$<br>• Parameter state transitions $\Delta\theta \neq \mathbf{0}$ vs $\Delta\theta = \mathbf{0}$<br>• Covariate shift $P_{\text{tr}}(X) \neq P_{\text{dep}}(X)$ vs Concept shift $P_{\text{tr}}(Y \mid X) \neq P_{\text{dep}}(Y \mid X)$ | • Circular MLOps lifecycle pipeline<br>• Acoustic spectrogram distribution shifts<br>• Confusion matrix trajectory |
| **B** | Greenhouse Climate Control | **Decision Tree Induction & Information Theory** (Pillar 1) | • Shannon Entropy: $H(S) = -\sum p_k \log_2 p_k$<br>• Gini Impurity: $G(S) = 1 - \sum p_k^2$<br>• Information Gain: $IG(S, A) = H(S) - \sum \frac{\|S_v\|}{\|S\|} H(S_v)$<br>• Continuous feature midpoint splitting $\theta = \frac{x_{(i)} + x_{(i+1)}}{2}$ | • 2D / 3D axis-aligned feature space partitions ($T \times H \times \text{CO}_2$)<br>• Hierarchical binary decision tree graph (TikZ) |
| **C** | Polynomial Regression Selection | **Overfitting, $L_2$ Ridge Regularization & SVD Shrinkage** (Pillars 1 & 2) | • Regularized Loss: $J = \text{RSS} + \lambda \sum_{i=1}^p a_i^2$<br>• Ridge Normal Eq: $\hat{\beta}_{\text{ridge}} = (X^T X + \lambda I)^{-1} X^T y$<br>• SVD Spectral Shrinkage: $f_j = \frac{s_j^2}{s_j^2 + \lambda}$<br>• Bias-Variance Decomposition: $\text{MSE} = \text{Bias}^2 + \text{Var} + \sigma^2$ | • Polynomial curve oscillation (Runge’s phenomenon)<br>• $L_2$ spherical penalty geometry vs RSS contours<br>• Spectral singular value decay curve |
| **D** | RLHF Policy Drift Bounds | **Frontier Alignment, KL Divergence & Safety Bounds** (Pillar 4) | • Simplified Drift Loss: $L(t) = -rt + \beta t^2$<br>• First-order condition: $t^* = \frac{r}{2\beta}$, $L(t^*) = -\frac{r^2}{4\beta}$<br>• Safe Policy Boundary: $\beta \ge \frac{r_{\max}}{2T}$<br>• Full Policy Objective: $\max_{\pi} \E[r(x,y)] - \beta D_{\text{KL}}(\pi \parallel \pi_{\text{ref}})$<br>• Closed-form Gibbs Policy: $\pi^*(y \mid x) \propto \pi_{\text{ref}}(y \mid x) \exp(r(x,y)/\beta)$ | • Quadratic loss parabola and minimum shift<br>• Mode-seeking reverse KL geometry<br>• Safe boundary operational envelope ($t^* \le T$) |
| **E** | Agricultural Advisory in Nepal | **Trustworthy AI, LLM Deployment & Socio-Technical Governance** (Pillar 6) | • Autoregressive token generation probability: $P(w_t \mid w_{<t})$<br>• Conformal Prediction: $\hat{C}(x) = \{y : s(x,y) \le \hat{q}_{1-\alpha}\}$<br>• Grounded RAG similarity: $\text{sim}(q, d) = \frac{q \cdot d}{\|q\| \|d\|}$<br>• Fallback / Human escalation routing logic | • Grounded RAG multi-tier system architecture<br>• Risk mitigation matrix (Likelihood vs Severity)<br>• Human-in-the-loop escalation flowchart |

---

## 8. Gap & Compliance Analysis: Direct Solutions vs. Pedagogical Study Guide

The most critical contribution of this survey is identifying and resolving the structural difference between the existing codebase and the user's authoritative prompt in `ORIGINAL_REQUEST.md`.

### Table 5: Detailed Gap Matrix & Transformation Strategy
| Aspect | Existing Codebase State (`docs/03`, `latex/`, `code/`) | Required Study Guide State (`ORIGINAL_REQUEST.md`) | Required Action / Transformation |
| :--- | :--- | :--- | :--- |
| **Purpose** | Solution manual for contest submission (25/25 pts target). | Educational study guide & review dossier (Tài liệu ôn tập). | Shift perspective from "Here is the answer" to "Here is the theoretical framework and foundational intuition." |
| **Direct Answers** | Explicitly solves Part (a) and (b) for Problems A–E with exact answers ($J(M_1)=9.26$, $t^*=r/(2\beta)$, $\text{CO}_2 \le 1250$, etc.). | **STRICTLY FORBIDDEN (R3)**: "Tuyệt đối không giải trực tiếp hoặc cung cấp đáp án cho các câu hỏi cụ thể trong đề (A, B, C, D, E)." | Abstract all specific problem instances into generalized mathematical formulations. Replace exact numerical computations with parametric examples and conceptual walk-throughs. |
| **Contest Data** | Hardcodes specific problem numbers: 6 greenhouse log rows, 4 regression data points, specific polynomial coefficients. | Exam questions should not be duplicated or solved. Theory must be explained using independent or generalized illustrative examples. | Use independent illustrative examples (e.g., general 2-class tree splits, generic degree-2 vs degree-4 polynomials, general $(T, P, E)$ examples like email spam or self-driving perception). |
| **Mathematical Formulas** | Rigorous graduate-level proofs (KKT, SVD, Calculus of Variations, Fisher Information). | Accessible, moderate mathematics: visual intuition combined with fundamental formulas (loss functions, basic derivatives) as requested in R2. | Retain core formulas (Loss functions, first derivative / stationary points, entropy formulas) while providing intuitive geometric interpretations and clear step-by-step guidance. |
| **Regularization & RLHF Drift** | Rigorous mathematical derivations in separate sections. | **Acceptance Criteria**: Must contain at least one conceptual explanation paragraph AND one mathematical formula illustration for both topics. | Explicitly craft dual conceptual + mathematical sections for Regularization ($L_1$ vs $L_2$) and RLHF Policy Drift ($D_{\text{KL}}$ penalty). |
| **Keywords for Self-Study** | Embedded implicitly within the text. | **Acceptance Criteria**: Each topic must include a dedicated list of keywords for student self-study. | Add a curated, structured "Keywords for Self-Study" (Từ khóa tự học) section to each of the 5 topic modules. |
| **Verification Strategy** | Existing test suite tests for exact solution numbers (`J(M1)==9.26`). | Must verify that the educational study guide does NOT leak answers (Forensic audit / No-leak verification). | Retain existing test suite as the internal ground-truth benchmark, while developing/specifying verification checks to audit the educational study guide against accidental answer leakage. |

---

## 9. Established Repository Conventions & Layout Standards

To ensure total coherence across team outputs, all agents should align with the following standards already established in the codebase:

### 9.1 Layout & File Discipline
- `.agents/`: Strictly reserved for agent metadata (`BRIEFING.md`, `DISPATCH.md`, `progress.md`, `handoff.md`, `survey_report.md`). **No project deliverables, source code, or user documents may be placed here.**
- `docs/`: Markdown dossiers organized with clear numbered prefixes (`01_`, `02_`, `03_`, `04_`), featuring bilingual or English academic titles, structured tables, and LaTeX math formatting (`$...$` and `$$...$$`).
- `latex/`: Modular LaTeX code centered around `imlc_submission.tex`, adhering to standard typography, `fancyhdr` running headers, and TikZ vector graphics.
- `code/`: Python 3 scripts with clean functional architectures, PEP 8 compliance, explicit type hinting (`typing`), and self-contained execution via `if __name__ == "__main__":`.
- `tests/`: Pytest test files partitioned by tier (`test_tier1_*.py` through `test_tier5_*.py`), with zero heavy external dependencies.

### 9.2 DeepTutor Pedagogical Conventions (RULE Compliance)
As mandated by `AGENTS.md` and `GEMINI.md`:
1. **Never spoil code/answers directly**: Do not provide ready-made answers to contest tasks.
2. **5-Tier Socratic Scaffolding**:
   - Tier 1: Symptom observation (point out anomalies).
   - Tier 2: Open-ended guiding questions (boundary conditions, invariants).
   - Tier 3: Minimal counter-examples.
   - Tier 4: Abstract syntax patterns / pseudo-code.
   - Tier 5: Detailed examples only when explicitly requested or on non-contest mock problems.
3. **Cognitive Gap Assessment**: Identify whether learner confusion is Structural, Deviation, Application, or Metacognitive.
4. **Visual Diagrams & Active Recall**: Include ASCII or Mermaid diagrams and diagnostic self-check questions at the end of each topic module.

---

## 10. Actionable Recommendations for Orchestrator & Subsequent Phases

1. **Architecture & Decomposition (Phase 1)**:
   - Create a dedicated educational deliverable: a comprehensive **IMLC 2026 Study & Preparation Dossier (Tài liệu Ôn tập IMLC 2026)**.
   - The deliverable can be structured as Markdown dossiers in `docs/` (e.g. `docs/imlc_study_guide.md` or modular topic chapters) and/or a clean, publication-grade LaTeX PDF study guide in `latex/` that complies with R1, R2, R3.
   - Keep the existing `docs/03_qualification_solutions.md` and `code/` untouched as the internal reference solution bank, but ensure the new study guide strictly omits all direct answers.

2. **Content Module Structure (Phase 2)**:
   - **Module 0 (Overview of IMLC)**: Institutional background (Edu.Harbour, Dr. Rami Aly), 3-round architecture (Qualification $\to$ Pre-Final $\to$ Final), scoring rubrics, comparisons with Kaggle, IOI/ICPC, and academic olympiads (R1).
   - **Module 1 (Topic A - ML Production Lifecycle & Distribution Shift)**: Mitchell $(T, P, E)$ framework, ERM parameter updates ($\Delta\theta \neq \mathbf{0}$ vs static inference $\Delta\theta = \mathbf{0}$), Covariate Shift vs Concept Shift with real-world examples, self-study keywords (R2, R3).
   - **Module 2 (Topic B - Decision Trees & Impurity Metrics)**: Mathematical formulations of Shannon Entropy and Gini Impurity, Information Gain calculation, continuous feature splitting algorithms, visual axis-aligned partitioning intuition, self-study keywords (R2, R3).
   - **Module 3 (Topic C - Polynomial Regression, Overfitting & Regularization)**: Underfitting vs Overfitting, Runge's phenomenon, $L_2$ Ridge penalty geometry ($\lambda \sum a_i^2$), bias-variance tradeoff, dual conceptual paragraph + mathematical formula illustration, self-study keywords (R2, R3, Rubric).
   - **Module 4 (Topic D - RLHF Policy Drift & Safety Bounds)**: Language model alignment foundations, reward hacking / Goodhart's Law, drift penalty formulation (quadratic proxy $\beta t^2$ and reverse KL divergence), first-order derivative for optimal shift, safe policy boundary derivation, dual conceptual paragraph + mathematical formula illustration, self-study keywords (R2, R3, Rubric).
   - **Module 5 (Topic E - Trustworthy AI & Deployment in Developing Contexts)**: Foundation model opportunities in agriculture/vernacular NLP, systemic risks (hallucination, toxic dosages, OOD microclimates, automation bias), mitigation architectures (grounded RAG, conformal prediction, human escalation), self-study keywords (R2, R3).

3. **Auditing & Forensic Verification (Phase 3)**:
   - Assign a dedicated Reviewer/Auditor to perform a strict line-by-line cross-check against `ORIGINAL_REQUEST.md` Rubric:
     - Check 1: Detailed IMLC format introduction present?
     - Check 2: Dual conceptual + mathematical explanation present for Regularization and RLHF Drift?
     - Check 3: ZERO direct solutions/answers or contest numbers for Problems A–E leaked?
     - Check 4: Dedicated keywords section present in all 5 topics?

---
*Report compiled and delivered by Explorer 1 (Survey — Codebase & Assets).*
