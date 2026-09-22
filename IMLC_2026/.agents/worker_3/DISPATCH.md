## 2026-09-18T13:34:14Z
You are Worker 3 (Remediation Specialist).
Your working directory is: d:\02_Learning_Knowledge\IMLC_2026\.agents\worker_3

CRITICAL REQUIREMENT: You MUST read the authoritative user request at:
d:\02_Learning_Knowledge\IMLC_2026\.agents\ORIGINAL_REQUEST.md
before starting your work!

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Background & Context:
Gate 2 failed due to an INTEGRITY VIOLATION found by Forensic Auditor 2 and REQUEST_CHANGES by Challenger 3.
The primary study guide (`docs/IMLC_2026_Study_Guide.md`, `docs/modules/*.md`, `latex/imlc_study_guide.pdf`) is 100% clean, verified, and sound.
However, 3 secondary files retain Problem D contest solutions/formulas:
1. `docs/02_curriculum_breakdown.md`: Lines 757–778 contain "4.4.3 Derivation of Problem D: The Price of Drift & Safe Policy Boundary" with exact formulas $L(t) = -rt + \beta t^2$, $t^* = \frac{r}{2\beta}$, $L(t^*) = -\frac{r^2}{4\beta}$, and $\beta \ge \frac{r+\delta}{2t_{safe}}$. Also line 27 ("Problem D Safe Drift Envelope Proof"), line 45 ("Safe Boundary Proof (Prob D)"), line 797 ("(Qualification Problem A Mapping)"), line 967 ("(Qualification Problem E Mapping)").
2. `docs/01_competition_dossier.md`: Lines 425–427 contain limits $\lim_{\beta \to 0^+} t^* = +\infty$, $\lim_{\beta \to \infty} t^* = 0$, and $\beta \ge \frac{r_{\max}}{2T}$.
3. `code/generate_latex_study_guide.py`: Lines 482–488 contain unpurged Problem D LaTeX source that overwrites `latex/imlc_study_guide.tex`.
4. `tests/test_study_guide.py`: Blind spot in test harness only scans `docs/IMLC_2026_Study_Guide.md`, missing secondary files in `docs/`.
5. `tests/test_challenger3_adversarial_leakage.py` currently fails on `docs/02_curriculum_breakdown.md`.

Refer to the full audit and challenger evidence reports:
- `d:\02_Learning_Knowledge\IMLC_2026\.agents\auditor_2\handoff.md`
- `d:\02_Learning_Knowledge\IMLC_2026\.agents\challenger_3\handoff.md`

Your Assignment:
1. You exclusively own and must modify:
   - `docs/02_curriculum_breakdown.md`: Replace Section 4.4.3 with generalized variational policy drift regularization $\min_\pi \mathcal{L}_{\text{drift}}(\pi; \beta) = -\mathcal{R}(\pi) + \beta \mathcal{D}(\pi \,\|\, \pi_{\text{ref}})$ and Fisher Information geometry / Socratic prompts (conforming to the theoretical style in `docs/modules/module5_rlhf_divergence.md`). Sanitize lines 27, 45, 797, 967 to remove contest problem headers.
   - `docs/01_competition_dossier.md`: Sanitize lines 425–427 to replace specific Problem D limits and formulas with generalized rubric language.
   - `code/generate_latex_study_guide.py`: Synchronize lines 482–488 with the sanitized theoretical content from `latex/imlc_study_guide.tex`.
   - `tests/test_study_guide.py`: Extend leakage testing to assert that all markdown files in `docs/` (`docs/**/*.md`) are free of direct contest answers and Problem D formulas.
2. Execute and verify commands:
   - Run `pytest tests/test_challenger3_adversarial_leakage.py -v` (must pass 10/10).
   - Run `pytest tests/test_study_guide.py -v` (must pass 100%).
   - Run `pytest tests/` (must pass 100% with 0 failures across the entire suite).
   - Run `python code/generate_latex_study_guide.py` (if applicable) and verify `latex/imlc_study_guide.pdf` compiles or remains intact and clean.
3. Write your `progress.md` and complete `handoff.md` in `d:\02_Learning_Knowledge\IMLC_2026\.agents\worker_3` with all command outputs and verification evidence. Report back when finished.
