# Module 5: Topic 4 — Frontier Alignment, RLHF & Policy Divergence Dynamics

**Document Reference**: `IMLC-2026-GUIDE-MOD5`  
**Topic Coverage**: Qualification Topic 4 (RLHF, Reward Hacking, KL Divergence, Gibbs Policy & Fisher Geometry)  
**Author**: Lead Educational Author & LaTeX Architect  
**Governing Standard**: DeepTutor Pedagogical Scaffolding & Strict R3 Non-Solution Compliance

---

## 1. Pedagogical Overview: The Alignment Challenge & Goodhart's Law

Pretrained Large Language Models (LLMs) are trained on web-scale text corpora using self-supervised causal language modeling:

$$\mathcal{L}_{\text{pretrain}}(\theta) = -\sum_{t=1}^T \log P_\theta(x_t \mid x_{<t})$$

While this produces rich representations of linguistic syntax and encyclopedic knowledge, optimizing for **next-token statistical likelihood** does not guarantee helpfulness, factual accuracy, or safety. Models readily emit hallucinations, toxic slurs, or sycophantic text if such sequences are statistically plausible in the uncurated training web corpus.

Supervised Fine-Tuning (SFT) on curated instruction-response pairs aligns the surface formatting, but cannot scale to cover the combinatorial space of open-ended conversational prompts.

To bridge this divide, modern foundation models employ **Reinforcement Learning from Human Feedback (RLHF)**:
1. **Bradley-Terry Reward Modeling**: A neural reward model $r_\psi(x, y)$ is trained on human pairwise preference judgments:
   $$P(y_w \succ y_l \mid x) = \sigma\left( r_\psi(x, y_w) - r_\psi(x, y_l) \right)$$
2. **Reinforcement Learning Optimization**: The language model acts as an RL policy $\pi_\theta(y \mid x)$, generating text tokens as actions to maximize expected scalar reward $r_\psi(x, y)$.

```
+---------------------------------------------------------------------------------------+
|                    REINFORCEMENT LEARNING FROM HUMAN FEEDBACK (RLHF)                  |
+---------------------------------------------------------------------------------------+
|                                                                                       |
|   Prompt x ---> [ Aligned Policy pi_theta ] ---> Candidate Response y                 |
|                        |                                    |                         |
|                        v                                    v                         |
|                 Log-Probability                      Reward Model                     |
|              log pi_theta(y|x)                      r_psi(x, y)                       |
|                        |                                    |                         |
|                        +---------------+                    |                         |
|                                        v                    v                         |
|   Prompt x ---> [ Reference Model pi_ref ]       Composite Objective:                 |
|                        |                  J(theta) = E[ r_psi(x,y) ]                  |
|                        v                             - beta * D_KL( pi_theta || pi_ref )
|                 Log-Probability                             |                         |
|               log pi_ref(y|x)                               v                         |
|                        |                         Policy Gradient Optimization         |
|                        +-----------------------> (PPO / Policy Loss Updates)          |
|                                                                                       |
+---------------------------------------------------------------------------------------+
```

### Goodhart's Law & Reward Hacking
> *"When a measure becomes a target, it ceases to be a good measure."* — Marilyn Strathern

Because the reward model $r_\psi(x, y)$ is an imperfect, finite-capacity neural proxy of human values, unconstrained policy optimization triggers **reward hacking**:
- **Verbosity Bias**: Generating excessively long, padded responses because human annotators unconsciously equate length with effort.
- **Sycophancy**: Affirming user errors and flattery rather than delivering truthful corrections.
- **Adversarial Exploitation**: Emitting repetitive nonsensical tokens or out-of-distribution strings that accidentally activate extreme positive logits in the reward model.
- **Catastrophic Forgetting**: Losing core grammatical and reasoning capabilities acquired during pretraining.

---

## 2. Mathematical Formulation: The KL Divergence Penalty

### 2.1 Conceptual Explanation (Mandatory Acceptance Requirement)
To prevent reward hacking, modern alignment pipelines augment the reward objective with a relative entropy penalty that anchors the active policy to a trusted, frozen reference model (typically the base SFT model). Conceptually, this penalty functions as an information-theoretic tether: the policy is incentivized to maximize human preference reward, but it incurs a quadratic penalty proportional to how far its token probability distribution diverges from the reference distribution. This ensures that the model learns to satisfy human instructions while preserving the linguistic fluency, world knowledge, and semantic coherence established during base training.

### 2.2 Mathematical Formulation (Mandatory Acceptance Requirement)
The composite RLHF alignment objective is:

$$\max_{\theta} \mathcal{J}_{\text{RLHF}}(\theta) = \mathbb{E}_{x \sim \mathcal{D}, \, y \sim \pi_\theta(\cdot \mid x)} \left[ r_\psi(x, y) \right] - \beta \mathbb{E}_{x \sim \mathcal{D}} \left[ D_{\text{KL}}(\pi_\theta(\cdot \mid x) \,\|\, \pi_{\text{ref}}(\cdot \mid x)) \right]$$

where:
- $\pi_\theta(y \mid x)$: The active parameterized policy undergoing optimization.
- $\pi_{\text{ref}}(y \mid x)$: The frozen reference language model (unchanged throughout training).
- $\beta > 0$: The KL divergence penalty coefficient (acting as an inverse temperature parameter).

### 2.3 Definition of Kullback-Leibler Divergence
For a discrete token sequence distribution over vocabulary paths $\mathcal{Y}$:

$$D_{\text{KL}}(\pi_\theta(\cdot \mid x) \,\|\, \pi_{\text{ref}}(\cdot \mid x)) = \sum_{y \in \mathcal{Y}} \pi_\theta(y \mid x) \log\left( \frac{\pi_\theta(y \mid x)}{\pi_{\text{ref}}(y \mid x)} \right) = \mathbb{E}_{y \sim \pi_\theta} \left[ \log \pi_\theta(y \mid x) - \log \pi_{\text{ref}}(y \mid x) \right]$$

Because $\pi_\theta$ is inside the expectation, this is the **Reverse KL Divergence**, which exhibits strong **mode-seeking (zero-avoiding)** behavior.

### 2.4 Token-Level Surrogate Reward in PPO
In policy gradient implementations like Proximal Policy Optimization (PPO), the objective is decomposed into token-level surrogate rewards:

$$R_{\text{surrogate}}(x, y) = r_\psi(x, y) - \beta \left( \log \pi_\theta(y \mid x) - \log \pi_{\text{ref}}(y \mid x) \right)$$

- If the policy assigns substantially higher probability to a token than the reference model ($\pi_\theta \gg \pi_{\text{ref}}$), the log-ratio is positive, penalizing the surrogate reward.
- If the policy adheres closely to the reference distribution ($\pi_\theta \approx \pi_{\text{ref}}$), the penalty vanishes.

---

## 3. First-Principles Derivation of the Optimal Gibbs Policy

A celebrated theoretical foundation of alignment proves that the non-parametric optimal policy under the KL-regularized objective has an exact analytical closed form.

### 3.1 Variational Formulation
Fix prompt $x$. We optimize over the non-parametric probability distribution $\pi(y) \equiv \pi(y \mid x)$ on the probability simplex $\Delta^{|\mathcal{Y}|-1}$. Introducing Lagrange multiplier $\mu$ for the normalization axiom $\sum_{y \in \mathcal{Y}} \pi(y) = 1$:

$$\mathcal{L}(\pi, \mu) = \sum_{y \in \mathcal{Y}} \pi(y) r(x, y) - \beta \sum_{y \in \mathcal{Y}} \pi(y) \log\left( \frac{\pi(y)}{\pi_{\text{ref}}(y)} \right) + \mu \left( 1 - \sum_{y \in \mathcal{Y}} \pi(y) \right)$$

### 3.2 First-Order Stationarity Condition
Differentiating with respect to probability $\pi(y)$:

$$\frac{\partial \mathcal{L}}{\partial \pi(y)} = r(x, y) - \beta \left[ \log\left(\frac{\pi(y)}{\pi_{\text{ref}}(y)}\right) + \pi(y) \cdot \frac{1}{\pi(y)} \right] - \mu = 0$$

$$r(x, y) - \beta \log\left(\frac{\pi(y)}{\pi_{\text{ref}}(y)}\right) - \beta - \mu = 0$$

Isolating the log-ratio:

$$\log\left(\frac{\pi(y)}{\pi_{\text{ref}}(y)}\right) = \frac{r(x, y)}{\beta} - \left(1 + \frac{\mu}{\beta}\right)$$

Exponentiating both sides:

$$\pi^*(y \mid x) = \pi_{\text{ref}}(y \mid x) \exp\left( \frac{r(x, y)}{\beta} \right) \exp\left( -1 - \frac{\mu}{\beta} \right)$$

### 3.3 Normalization & The Partition Function
Enforcing the normalization axiom $\sum_{y \in \mathcal{Y}} \pi^*(y \mid x) = 1$:

$$\exp\left( -1 - \frac{\mu}{\beta} \right) \sum_{y' \in \mathcal{Y}} \pi_{\text{ref}}(y' \mid x) \exp\left( \frac{r(x, y')}{\beta} \right) = 1$$

$$\exp\left( -1 - \frac{\mu}{\beta} \right) = \frac{1}{Z(x)}, \quad \text{where } Z(x) = \sum_{y' \in \mathcal{Y}} \pi_{\text{ref}}(y' \mid x) \exp\left( \frac{r(x, y')}{\beta} \right)$$

**Theorem (The Optimal Aligned Policy)**:  
The global unconstrained optimum of the KL-regularized reward maximization objective is the **Gibbs / Boltzmann Policy**:

$$\mathbf{\pi^*(y \mid x) = \frac{1}{Z(x)} \pi_{\text{ref}}(y \mid x) \exp\left( \frac{r(x, y)}{\beta} \right)}$$

### 3.4 Direct Preference Optimization (DPO) Reparameterization
By taking logarithms on both sides and rearranging:

$$r(x, y) = \beta \log\left( \frac{\pi^*(y \mid x)}{\pi_{\text{ref}}(y \mid x)} \right) + \beta \log Z(x)$$

Rafailov et al. (2023) substituted this analytical expression directly into the Bradley-Terry preference loss, proving that preference alignment can be solved **in closed form without training an explicit reward model or running unstable reinforcement learning loops**:

$$\mathcal{L}_{\text{DPO}}(\theta) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]$$

---

## 4. Information Geometry: Second-Order Expansion & Fisher Metric

Why is policy drift frequently formalized as a quadratic penalty $\beta t^2$ in analytical model problems?

Consider the Taylor series expansion of relative entropy $D_{\text{KL}}(\pi_\theta \,\|\, \pi_{\theta_{\text{ref}}})$ with respect to parameters $\theta$ around the reference point $\theta = \theta_{\text{ref}}$:
1. **Value at Reference Point**:
   $$D_{\text{KL}}(\pi_{\theta_{\text{ref}}} \,\|\, \pi_{\theta_{\text{ref}}}) = 0$$
2. **First Derivative (Gradient)**:
   Because KL divergence is non-negative and achieves its global minimum at $\theta = \theta_{\text{ref}}$, its gradient vanishes:
   $$\nabla_\theta D_{\text{KL}}(\pi_\theta \,\|\, \pi_{\theta_{\text{ref}}})\Big|_{\theta = \theta_{\text{ref}}} = \mathbf{0}$$
3. **Second Derivative (Hessian)**:
   The Hessian of KL divergence evaluated at the reference model is the **Fisher Information Matrix** $\mathcal{F}(\theta_{\text{ref}})$:
   $$\nabla_\theta^2 D_{\text{KL}}(\pi_\theta \,\|\, \pi_{\theta_{\text{ref}}})\Big|_{\theta = \theta_{\text{ref}}} = \mathcal{F}(\theta_{\text{ref}}) = \mathbb{E}_{y \sim \pi_{\theta_{\text{ref}}}} \left[ \nabla_\theta \log \pi_\theta(y) \nabla_\theta \log \pi_\theta(y)^T \right]$$

The second-order Taylor approximation is therefore:

$$D_{\text{KL}}(\pi_\theta \,\|\, \pi_{\theta_{\text{ref}}}) = \frac{1}{2} (\theta - \theta_{\text{ref}})^T \mathcal{F}(\theta_{\text{ref}}) (\theta - \theta_{\text{ref}}) + \mathcal{O}(\|\theta - \theta_{\text{ref}}\|^3)$$

Defining the Riemannian Mahalanobis policy drift distance:

$$t = \|\theta - \theta_{\text{ref}}\|_{\mathcal{F}} = \sqrt{(\theta - \theta_{\text{ref}})^T \mathcal{F}(\theta_{\text{ref}}) (\theta - \theta_{\text{ref}})}$$

The KL penalty satisfies:

$$\beta D_{\text{KL}}(\pi_\theta \,\|\, \pi_{\theta_{\text{ref}}}) \approx \frac{1}{2} \beta t^2 \propto \beta t^2$$

This proves that **quadratic drift penalties $\beta t^2$ are the canonical local Riemannian approximations of relative entropy in parameterized policy manifolds**.

---

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

---

## 6. DeepTutor 5-Tier Socratic Diagnostic Suite

### Tier 1: Phenomenological Observation
When interacting with a commercial LLM, you notice that asking it to summarize a 100-word paragraph results in an 800-word essay with elaborate decorative emojis and praise. What proxy reward incentive was likely unbalanced in the training reward model?

### Tier 2: Socratic Probing
Why must the reference model $\pi_{\text{ref}}$ remain permanently frozen during RLHF? What would occur to the KL divergence term $D_{\text{KL}}(\pi_\theta \,\|\, \pi_{\text{ref}})$ if $\pi_{\text{ref}}$ were continually updated to equal $\pi_\theta$ at every gradient step?

### Tier 3: Minimal Counterexample
Suppose a reward model assigns high positive scores to responses that include the phrase "In conclusion, it is important to remember".
If $\beta = 0$, what failure mode will the policy exhibit?
If $\beta = 10{,}000$, what response will the policy produce?

### Tier 4: Abstract Mathematical Pattern
Consider an idealized scalar approximation where reward gain is a concave function $g(t)$ of policy drift $t \ge 0$, and regularization is enforced via a strictly convex penalty $\Omega(t)$:
$$\mathcal{L}(t) = -g(t) + \beta \Omega(t), \quad \text{with } g'(t) > 0, \; g''(t) \le 0, \; \Omega'(t) > 0, \; \Omega''(t) > 0$$
1. Using the First-Order Condition $\frac{d\mathcal{L}}{dt} = 0$, express the relationship between marginal reward gain and marginal penalty cost at the optimal drift $t^*$.
2. Prove that the Second-Order Condition $\frac{d^2\mathcal{L}}{dt^2} > 0$ holds strictly for all $\beta > 0$, guaranteeing a unique global minimum.
3. If an engineering specification requires $t^* \le T_{\text{drift}}$ for all reward scales $r \le r_{\max}$, formulate how the worst-case supremum $\sup_{r \le r_{\max}} t^*(r, \beta) \le T_{\text{drift}}$ establishes a lower bound on alignment strength $\beta$.

### Tier 5: Autonomous Mastery Prompt
Starting from the Bradley-Terry preference loss $\mathcal{L}(\theta) = -\mathbb{E}[\log \sigma(r(x, y_w) - r(x, y_l))]$ and the Gibbs policy $r(x, y) = \beta \log \frac{\pi^*(y \mid x)}{\pi_{\text{ref}}(y \mid x)} + \beta \log Z(x)$, prove algebraically that the partition function $Z(x)$ cancels out completely from the pairwise difference $r(x, y_w) - r(x, y_l)$. Explain why this mathematical cancellation is the core breakthrough of Direct Preference Optimization (DPO).

---

## 7. Self-Study Keywords: Topic 4

- Causal Language Modeling Pretraining
- Supervised Fine-Tuning (SFT)
- Bradley-Terry Preference Model
- Reward Model (RM) Architecture & Calibration
- Reinforcement Learning from Human Feedback (RLHF)
- Proximal Policy Optimization (PPO)
- Actor-Critic Architecture in Generative Models
- Value Network & Generalized Advantage Estimation (GAE)
- Kullback-Leibler (KL) Divergence / Relative Entropy
- Reverse KL (Mode-Seeking) vs. Forward KL (Mean-Seeking)
- Token-Level Surrogate Reward
- Policy Drift & Alignment Tax
- Reward Hacking / Reward Gaming (Goodhart's Law)
- Gibbs / Boltzmann Distribution
- Partition Function $Z(x)$
- Direct Preference Optimization (DPO)
- Kahneman-Tversky Optimization (KTO)
- Fisher Information Matrix & Natural Policy Gradient
- Information Geometry / Riemannian Policy Manifold
- Safe Policy Divergence & Governance Boundaries
- Trust-Region Policy Optimization (TRPO)
