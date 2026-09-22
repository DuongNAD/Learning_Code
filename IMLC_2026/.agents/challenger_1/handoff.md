# Handoff Report: Adversarial Solution Leakage Audit (Requirement R3 Firewall)

**Agent**: Challenger 1 (Adversarial Solution Leakage Challenger)  
**Role**: critic, specialist  
**Working Directory**: `d:\02_Learning_Knowledge\IMLC_2026\.agents\challenger_1`  
**Milestone**: M4 Verification & Adversarial Audit  
**Date**: 2026-09-18T12:45:00Z  
**Verdict**: **`REQUEST_CHANGES`** (Critical solution leak detected for Problem D)

---

## 1. Observation

Direct empirical investigation comparing `docs/03_qualification_solutions.md` against target deliverables (`docs/IMLC_2026_Study_Guide.md`, `latex/imlc_study_guide.tex`, and `docs/modules/*.md`) revealed the following exact observations:

### Observation 1.1: Official Contest Problem D Statement
From `docs/03_qualification_solutions.md` lines 526–535:
```markdown
Let $t \ge 0$ quantify the drift from the reference model. The reward achieved is $rt$, and the drift penalty is $\beta t^2$, with scalars $r > 0$ and $\beta > 0$. The resulting training loss is:
$$L(t) = -rt + \beta t^2$$
Training minimizes $L(t)$ over $t \ge 0$.

**Questions**:
- **(a)** Find the shift $t^*$ that minimizes the loss, and the loss value it reaches.
- **(b)** What happens to $t^*$ as $\beta \to 0$, and as $\beta \to \infty$? Explain what each case means for the language model.
- **(c)** The reward estimate $r$ is noisy: engineers only know that $0 < r \le r_{\max}$. They require the shift to stay below safety limit $T$ for any $r \in (0, r_{\max}]$. Show that this is guaranteed exactly when $\beta \ge \frac{r_{\max}}{2T}$.
- **(d)** What does the term $\lambda \sum_i a_i^2$ from Problem C have in common with the penalty term $\beta t^2$ here?
```

### Observation 1.2: Leaked Solution in `docs/IMLC_2026_Study_Guide.md` (lines 1248–1284)
Verbatim excerpt from `docs/IMLC_2026_Study_Guide.md`:
```markdown
## 5. Analytical Drift Optimization & Safe Boundary Analysis

In mathematical competitions and theoretical analyses, the trade-off between reward seeking and drift penalties is often analyzed via the canonical scalar loss model:

$$L(t) = -rt + \beta t^2$$

where $t \ge 0$ represents policy drift, $r > 0$ represents reward sensitivity, and $\beta > 0$ represents regularization strength.

### 5.1 First-Order & Second-Order Optimality Conditions
1. **First-Order Condition (FOC)**:
   $$\frac{dL}{dt} = -r + 2\beta t = 0 \implies \mathbf{t^* = \frac{r}{2\beta}}$$
2. **Minimal Attainable Loss**:
   $$L(t^*) = -r\left(\frac{r}{2\beta}\right) + \beta\left(\frac{r}{2\beta}\right)^2 = -\frac{r^2}{2\beta} + \frac{r^2}{4\beta} = \mathbf{-\frac{r^2}{4\beta}}$$
3. **Second-Order Condition (SOC)**:
   $$\frac{d^2L}{dt^2} = 2\beta > 0 \quad (\forall \beta > 0)$$
   Because the second derivative is strictly positive, the loss function $L(t)$ is **strictly convex**, guaranteeing that $t^*$ is a unique, global minimum.

### 5.2 Asymptotic Behavior of Alignment Strength $\beta$
- **Vanishing Penalty Limit ($\beta \to 0^+$)**:
  $$\lim_{\beta \to 0^+} t^* = \lim_{\beta \to 0^+} \frac{r}{2\beta} = +\infty$$
  $$\lim_{\beta \to 0^+} \pi^*(y \mid x) = \arg\max_y r(x, y)$$
  When regularization vanishes, the policy experiences **catastrophic drift**, degenerating into deterministic exploitation of proxy reward artifacts (complete reward hacking).
- **Infinite Penalty Limit ($\beta \to \infty$)**:
  $$\lim_{\beta \to \infty} t^* = \lim_{\beta \to \infty} \frac{r}{2\beta} = 0$$
  $$\lim_{\beta \to \infty} \pi^*(y \mid x) = \pi_{\text{ref}}(y \mid x)$$
  When penalty dominates, the policy is **frozen** at the reference anchor, suppressing adaptation entirely.

### 5.3 Safe Boundary Theorem
In safety-critical governance, engineers enforce a hard operational boundary $t^* \le T$, where $T$ is the maximum tolerable divergence from the reference anchor.

Suppose reward sensitivity is bounded: $r \in (0, r_{\max}]$.

$$\sup_{r \in (0, r_{\max}]} t^*(r) \le T \iff \frac{r_{\max}}{2\beta} \le T \iff \mathbf{\beta \ge \frac{r_{\max}}{2T}}$$

This defines the **Safe Regularization Boundary**: to guarantee that an aligned system never exceeds drift threshold $T$ under worst-case reward sensitivity $r_{\max}$, the regularization coefficient must satisfy $\beta \ge \frac{r_{\max}}{2T}$.
```
Also reproduced verbatim in `docs/modules/module5_rlhf_divergence.md` lines 169–205.

### Observation 1.3: Leaked Solution in `latex/imlc_study_guide.tex` (lines 480–486)
Verbatim excerpt from `latex/imlc_study_guide.tex`:
```latex
\subsection{Scalar Drift Dynamics \& Safe Boundary Theorem}
Consider scalar loss $L(t) = -rt + \beta t^2$ with $t \ge 0, r > 0, \beta > 0$:
\begin{itemize}[noitemsep]
    \item First-Order Condition: $\frac{dL}{dt} = -r + 2\beta t = 0 \implies \mathbf{t^* = \frac{r}{2\beta}}$, with $L(t^*) = -\frac{r^2}{4\beta}$.
    \item Second-Order Condition: $\frac{d^2L}{dt^2} = 2\beta > 0$ proves strict convexity.
    \item Safe Regularization Boundary: For drift limit $T$, $\sup_{r \in (0, r_{\max}]} t^*(r) \le T \iff \mathbf{\beta \ge \frac{r_{\max}}{2T}}$.
\end{itemize}
```

### Observation 1.4: Contaminated Requirement in `tests/test_study_guide.py` (lines 356–371)
```python
    def test_tier2_rlhf_scalar_drift_and_safety_bound(self):
        """Topic RLHF Drift must include scalar drift loss L(t) = -rt + beta t^2 and safety bound."""
        content = get_study_guide_markdown()
        has_scalar_drift = bool(
            re.search(r"-rt\s*\+\s*\\beta\s*t\^2|-rt\s*\+\s*beta\s*t\^2", content)
            and re.search(r"t\^\*\s*=\s*\\frac\{r\}\{2\\beta\}|r\s*/\s*\(2\\beta\)", content)
        )
        has_safety_bound = bool(
            re.search(r"\\beta\s*\\ge\s*\\frac\{r_\{?\\(?:text\{)?max\}?\}?\}\{2T\}|r_\{?\\max\}?\s*/\s*\(?2T\)?|\\beta\s*\\ge\s*.*r.*2T", content)
        )
        assert has_scalar_drift, (
            "Missing scalar drift formulation: L(t) = -rt + beta t^2, t* = r / (2 beta)."
        )
        assert has_safety_bound, (
            "Missing safe policy boundary condition proof: beta >= r_max / (2T)."
        )
```
Moreover, `TestTier3NonSolutionFirewall` in `tests/test_study_guide.py` (lines 399–497) explicitly tests and asserts the absence of solutions for Problems A, B, and C, but contains ZERO assertions preventing the leakage of Problem D.

### Observation 1.5: Cleanliness of Problems A, B, C, and E
Across all 28 automated checks:
- **Problem A**: 0 leaks. The acoustic 10,000 recordings dataset, 6-step discrete classification table, and direct learning answer ("Step 2 and Step 6") are completely absent. Pedagogical discussions focus on Tom Mitchell's formulation and generic sensor drift.
- **Problem B**: 0 leaks. The greenhouse table (temperature 28°C, humidity 70%, CO2 1250 ppm, rows 1–6 log dataset, query (26°C, 68%) -> "KEEP CLOSED") is completely absent. Module 3 teaches general recursive partitioning, Shannon entropy, and CART pruning on abstract/XOR datasets.
- **Problem C**: 0 leaks. The 4-point dataset `{(0, 1.0), (1, 3.2), (2, 4.8), (3, 7.0)}`, candidate polynomials $M_1(x)$ and $M_2(x)$, numerical scores $J(M_1)=9.26$, $J(M_2)=4.08$, $\text{RSS}(M_2)=0.08$, and critical threshold $\lambda^*=0.0152$ are completely absent. Module 4 teaches general OLS, Ridge, Lasso, SVD spectral shrinkage, and bias-variance proofs on arbitrary degree $p$.
- **Problem E**: 0 leaks. The Nepal rural agronomic setting, specific four discrete actions (Irrigate, Apply treatment, Wait, Contact an expert), and pre-formulated 3 opportunities / 3 risks are completely absent. Module 6 provides general mathematical proofs of Kleinberg's theorem, algorithmic fairness, and conformal prediction bounds.

---

## 2. Logic Chain

1. **Premise 1 (R3 Strict Firewall Requirement)**: `ORIGINAL_REQUEST.md` (lines 24–25 and 32) and `PROJECT.md` (lines 10, 28) strictly prohibit providing direct solutions or answers to any of the five contest problems:
   > *"Tuyệt đối không giải trực tiếp hoặc cung cấp đáp án cho các câu hỏi cụ thể trong đề (A, B, C, D, E). Chỉ đóng vai trò hướng dẫn lý thuyết. Kiểm tra chéo toàn bộ tài liệu để đảm bảo KHÔNG có đáp án trực tiếp cho các số liệu/câu hỏi trong đề thi."*
2. **Premise 2 (Direct Answer Delivery)**: Contest Problem D specifically asks students to:
   - Calculate the optimal shift $t^*$ minimizing $L(t) = -rt + \beta t^2$ and the minimal loss value $L(t^*)$ [Question (a)];
   - Analyze the limits as $\beta \to 0$ and $\beta \to \infty$ and explain their meaning for LLMs [Question (b)];
   - Prove that $t^*(r) \le T$ for all $r \in (0, r_{\max}]$ iff $\beta \ge \frac{r_{\max}}{2T}$ [Question (c)].
3. **Inference from Observations 1.1, 1.2, 1.3**:
   - `docs/IMLC_2026_Study_Guide.md` Section 5, `docs/modules/module5_rlhf_divergence.md` Section 5, and `latex/imlc_study_guide.tex` Subsection 5.4 provide verbatim the exact solutions, calculus derivations, asymptotic limits, and mathematical proofs for Questions (a), (b), and (c) of Problem D.
   - Any student reading the study guide has a 100% complete, copy-paste answer key for Problem D.
4. **Inference from Observation 1.4**:
   - The test suite `tests/test_study_guide.py` suffered from a specification error: `test_tier2_rlhf_scalar_drift_and_safety_bound` inadvertently enforced the inclusion of Problem D's solution, while `TestTier3NonSolutionFirewall` lacked an assertion to catch it.
5. **Conclusion**:
   - Requirement R3 is violated in the current draft.
   - The study guide cannot be approved until Section 5 of Topic 4 is scrubbed of the specific contest problem and test assertions are corrected.

---

## 3. Caveats

- **No Caveats regarding Problem D Leakage**: The overlap between Problem D and Chapter 5 Section 5 is exact, verbatim, and irrefutable.
- **Pedagogical Quality**: The theoretical material in Sections 1–4 of Module 5 (Bradley-Terry preference model, PPO with KL penalty, calculus of variations derivation of Gibbs policy, DPO, and Fisher Information Riemannian metric) is of exceptional academic quality and does not need to be removed. Only the scalar contest toy problem in Section 5 violates R3.
- **Other Modules**: Modules 1, 2, 3, 4, 6, and 7 are clean, rigorously scaffolded, and fully conform to R3.

---

## 4. Conclusion

**Verdict**: **`REQUEST_CHANGES`**

### Required Action Items for Worker/Implementation Agents:
1. **Scrub Problem D Contest Solution from Markdown**:
   - In `docs/modules/module5_rlhf_divergence.md` and `docs/IMLC_2026_Study_Guide.md`:
     - Delete Section 5 ("Analytical Drift Optimization & Safe Boundary Analysis", lines 1248–1284).
     - In Section 6 (DeepTutor Socratic Suite), rewrite Tier 4 (lines 1300–1304) to formulate an abstract Socratic exploration of quadratic divergence penalties without mentioning $L(t) = -rt + \beta t^2$.
     - In Section 7 (Keywords), replace `- Safe Regularization Boundary (\beta \ge \frac{r_{\max}}{2T})` with `- Safe Divergence Boundaries in Policy Optimization`.
2. **Scrub Problem D Contest Solution from LaTeX**:
   - In `latex/imlc_study_guide.tex`:
     - Delete or replace Subsection 5.4 ("Scalar Drift Dynamics & Safe Boundary Theorem", lines 480–486).
     - In Remark 5.1 (Keywords, line 489), replace `Safe Boundary Theorem` with `Policy Divergence Bounds`.
3. **Fix Test Suite in `tests/test_study_guide.py`**:
   - In `tests/test_study_guide.py`:
     - Delete or refactor `test_tier2_rlhf_scalar_drift_and_safety_bound` (lines 356–371). Topic 4 math verification should check for KL divergence, Bradley-Terry sigmoid, and Gibbs optimal policy formulas, NOT the leaked contest scalar toy loss.
     - Add `test_tier3_no_problem_d_solution_leakage` to `TestTier3NonSolutionFirewall`, asserting that `-rt + \beta t^2`, `t^* = \frac{r}{2\beta}`, and `\beta \ge \frac{r_{\max}}{2T}` are strictly absent from both Markdown and LaTeX files.
4. **Recompile and Re-run Full Verification**:
   - Re-run `pytest tests/test_study_guide.py`.
   - Re-compile `latex/imlc_study_guide.tex` to update `imlc_study_guide.pdf`.

---

## 5. Verification Method

To independently verify the findings in this report:

1. **Verify Leaked Occurrences via Terminal**:
   ```powershell
   Select-String -Path docs\IMLC_2026_Study_Guide.md, latex\imlc_study_guide.tex, docs\modules\module5_rlhf_divergence.md -Pattern "L\(t\) = -rt \+ \\beta t\^2"
   Select-String -Path docs\IMLC_2026_Study_Guide.md, latex\imlc_study_guide.tex, docs\modules\module5_rlhf_divergence.md -Pattern "\\beta \\ge \\frac\{r_\{?max\}?\}\{2T\}"
   ```
   *Expected Current Output*: Matches found on lines 1252, 1280 of `docs/IMLC_2026_Study_Guide.md`, lines 173, 201 of `docs/modules/module5_rlhf_divergence.md`, and lines 481, 485 of `latex/imlc_study_guide.tex`.

2. **Verify Contest Problem Statement in Source of Truth**:
   Inspect `docs/03_qualification_solutions.md` at lines 526–535. Notice that it matches the study guide equations character-for-character.

3. **Condition for Invalidation**:
   This audit finding is invalidated if and only if the exact contest expressions ($L(t) = -rt + \beta t^2$, $t^* = \frac{r}{2\beta}$, $L(t^*) = -\frac{r^2}{4\beta}$, and $\beta \ge \frac{r_{\max}}{2T}$) are completely removed from all study guide deliverables, replaced by generic theoretical discussions, and the test suite passes with an adversarial negative assertion against Problem D leakage.
