## 5. Theoretical Framework: Regularized Policy Drift & Bounded Divergence Dynamics

In policy alignment pipelines, balancing instruction adherence against linguistic preservation is formalized through regularized optimization. Rather than solving a stylized, ad-hoc toy problem, production alignment treats policy drift as a principled variational trade-off between expected proxy reward and information-theoretic divergence.

### 5.1 The Lagrangian Trade-Off & Pareto Frontier
Let $\mathcal{R}(\pi) = \mathbb{E}_{x \sim \mathcal{D}, y \sim \pi}[r(x, y)]$ represent the expected reward under the target policy $\pi$, and let $\mathcal{D}(\pi \,\|\, \pi_{\text{ref}})$ represent a statistical divergence anchor (such as the relative entropy $\mathbb{E}_x [D_{\text{KL}}(\pi(\cdot \mid x) \,\|\, \pi_{\text{ref}}(\cdot \mid x))]$).

An ideal alignment objective maximizes preference reward subject to an information-theoretic safety budget $\epsilon_{\text{safe}}$:

$$\max_{\pi} \mathcal{R}(\pi) \quad \text{subject to} \quad \mathcal{D}(\pi \,\|\, \pi_{\text{ref}}) \le \epsilon_{\text{safe}}$$

Applying Karush-Kuhn-Tucker (KKT) duality, this constrained optimization translates directly into minimizing the regularized drift loss:

$$\min_{\pi} \mathcal{L}_{\text{drift}}(\pi; \beta) = -\mathcal{R}(\pi) + \beta \cdot \mathcal{D}(\pi \,\|\, \pi_{\text{ref}})$$

where the regularization coefficient $\beta \ge 0$ serves as the Lagrange dual multiplier (or inverse temperature). Varying $\beta$ across $(0, \infty)$ traces the complete **Pareto Frontier** between reward exploitation and distribution drift:
- At any point on this frontier, the marginal gain in expected reward equals the marginal information cost weighted by $\beta$:
  $$\frac{\delta \mathcal{R}(\pi)}{\delta \pi} = \beta \frac{\delta \mathcal{D}(\pi \,\|\, \pi_{\text{ref}})}{\delta \pi}$$

### 5.2 Qualitative Dynamics of the Alignment Parameter $\beta$
Understanding the limiting behavior of the regularization hyperparameter is fundamental to diagnosing training instabilities in production:

1. **Under-Regularized Regime ($\beta \to 0^+$: Unconstrained Exploitation)**:
   $$\lim_{\beta \to 0^+} \pi^*(y \mid x) = \arg\max_y r(x, y)$$
   When the divergence penalty vanishes, the anchor to $\pi_{\text{ref}}$ is severed. The policy degenerates into pathological **reward hacking** (Goodhart's Law): exploiting out-of-distribution artifacts, repeating high-reward n-grams, or generating artificially inflated sequences that maximize the proxy score while destroying grammatical fluency and factuality.
2. **Over-Regularized Regime ($\beta \to \infty$: Frozen Policy)**:
   $$\lim_{\beta \to \infty} \pi^*(y \mid x) = \pi_{\text{ref}}(y \mid x)$$
   When the divergence penalty dominates, the policy is rigidly clamped to the reference anchor. Policy drift is completely suppressed, but the model fails to learn human preferences, remaining unaligned.
3. **Operational Alignment Regime ($\beta \in (0, \infty)$)**:
   A calibrated $\beta$ achieves optimal alignment: sufficient policy drift to satisfy user instructions while bounding the distributional shift within the trust region where the reward model remains reliable.

### 5.3 Safety Governance: Worst-Case Divergence Boundaries
In mission-critical deployments, AI safety standards mandate that an aligned model must never drift beyond a validated trust-region threshold $T_{\text{drift}}$:

$$\mathcal{D}(\pi^* \,\|\, \pi_{\text{ref}}) \le T_{\text{drift}}$$

Because empirical reward estimates are subject to stochastic noise and varying prompt difficulties, the effective reward sensitivity can fluctuate across an operational uncertainty interval $r \in (0, r_{\max}]$. 

To guarantee safety, governance frameworks perform **worst-case boundary analysis**:

$$\sup_{r \in (0, r_{\max}]} \text{Drift}(r, \beta) \le T_{\text{drift}}$$

Engineers determine the critical regularization lower bound $\beta_{\text{crit}}$ such that even under the maximum possible reward perturbation $r_{\max}$, the policy shift remains safely within the trust boundary $T_{\text{drift}}$.

### 5.4 Cross-Pillar Synthesis: Quadratic Penalties across Paradigms
A deep unifying principle across modern machine learning is the equivalence of quadratic penalties as local stabilizers across diverse problem spaces:

| Feature / Dimension | Supervised Regression (Topic 3) | RLHF Policy Alignment (Topic 4) |
| :--- | :--- | :--- |
| **Optimization Target** | Parameter vector $w \in \mathbb{R}^{p+1}$ | Generative policy distribution $\pi_\theta$ |
| **Fidelity Objective** | Empirical Residual Sum of Squares $\frac{1}{2n}\|y - \Phi w\|_2^2$ | Expected Human Preference Reward $\mathbb{E}[r_\psi(x, y)]$ |
| **Regularization Anchor** | Origin $\mathbf{0}$ (isotropic shrinkage) | Frozen base language model $\pi_{\text{ref}}$ |
| **Penalty Metric** | Euclidean squared norm $\|w\|_2^2 = \sum_j w_j^2$ | Relative entropy $D_{\text{KL}}(\pi \,\|\, \pi_{\text{ref}})$ |
| **Local Geometric Form** | Isotropic quadratic form $\frac{\lambda}{2} w^T I^* w$ | Riemannian quadratic form $\frac{1}{2}\beta \Delta\theta^T \mathcal{F}(\theta_{\text{ref}}) \Delta\theta$ |
| **Vanishing Penalty ($\to 0$)** | Runge's phenomenon / extreme variance | Reward hacking / catastrophic mode collapse |
| **Infinite Penalty ($\to \infty$)** | Flat baseline model ($w \to \mathbf{0}$) | Completely frozen pretraining anchor ($\pi \to \pi_{\text{ref}}$) |
