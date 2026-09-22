# Module 3: Topic 2 — Decision Trees & Information-Theoretic Partitioning

**Document Reference**: `IMLC-2026-GUIDE-MOD3`  
**Topic Coverage**: Qualification Topic 2 (Decision Trees, Information Theory & Space Partitioning)  
**Author**: Lead Educational Author & LaTeX Architect  
**Governing Standard**: DeepTutor Pedagogical Scaffolding & Strict R3 Non-Solution Compliance

---

## 1. Pedagogical Overview & Geometric Intuition

Decision trees are among the most intuitive yet mathematically rich paradigms in classical machine learning. At their core, decision trees perform **recursive orthogonal partitioning** of an input feature space $\mathcal{X} \subseteq \mathbb{R}^d$ into a finite set of mutually disjoint, axis-aligned hyper-rectangles $\{R_m\}_{m=1}^M$.

Within each terminal region $R_m$, the tree fits an elementary local model—typically a constant prediction $c_m$:

$$f(x) = \sum_{m=1}^M c_m \mathbb{I}(x \in R_m)$$

For classification tasks, $c_m$ is the majority class label or empirical class probability vector; for regression tasks, $c_m$ is the sample mean of targets within $R_m$.

```
+---------------------------------------------------------------------------------------+
|                    DECISION TREE ORTHOGONAL GEOMETRIC PARTITION                       |
+---------------------------------------------------------------------------------------+
|   Feature X2                                                                          |
|       ^                                                                               |
|       |                                                                               |
|   1.0 +-----------------------+-------------------------------+                       |
|       |                       |                               |                       |
|       |      Region R_1       |          Region R_3           |                       |
|       |      (Class: A)       |          (Class: B)           |                       |
|       |                       |                               |                       |
|  theta2+ - - - - - - - - - - - + - - - - - - - - - - - - - - - +                       |
|       |                       |                               |                       |
|       |      Region R_2       |          Region R_4           |                       |
|       |      (Class: B)       |          (Class: A)           |                       |
|       |                       |                               |                       |
|   0.0 +-----------------------+-------------------------------+---> Feature X1        |
|      0.0                    theta1                          1.0                       |
|                                                                                       |
|   Hierarchy:                                                                          |
|               [ Is X1 <= theta1? ]                                                    |
|                 /              \                                                      |
|             (Yes)              (No)                                                   |
|             /                      \                                                  |
|     [ Is X2 <= theta2? ]       [ Is X2 <= theta2? ]                                   |
|       /            \             /            \                                       |
|    (Yes)          (No)        (Yes)          (No)                                     |
|     |              |            |              |                                      |
|    R_2 (B)        R_1 (A)      R_4 (A)        R_3 (B)                                 |
+---------------------------------------------------------------------------------------+
```

### Key Geometric Properties:
- **Axis Alignment**: Every split decision is parallel to a coordinate axis (e.g., $x_j \le \tau$). A decision tree cannot easily represent diagonal decision boundaries (e.g., $x_1 + x_2 \le 1$) without constructing a fine-grained "staircase" approximation requiring many splits.
- **Hierarchical Composition**: Sub-trees partition subsets of data independently, allowing adaptive resolution in complex regions of feature space.

---

## 2. Mathematical Formulations of Impurity Metrics

Let node $S \subseteq \mathcal{D}$ contain $|S|$ samples belonging to $K$ distinct classes $\{1, 2, \dots, K\}$. The empirical probability of class $k$ in node $S$ is:

$$p_k = \frac{1}{|S|} \sum_{(x_i, y_i) \in S} \mathbb{I}(y_i = k), \quad \text{where } \sum_{k=1}^K p_k = 1, \quad p_k \ge 0$$

An impurity metric $I(S)$ quantifies the degree of label heterogeneity within node $S$. A valid impurity function satisfies:
1. $I(S) = 0$ if and only if the node is pure ($\exists k$ such that $p_k = 1$).
2. $I(S)$ attains its maximum when classes are uniformly distributed ($p_k = 1/K, \forall k$).
3. $I(S)$ is strictly concave with respect to the probability vector $p$.

### 2.1 Shannon Entropy & Information Gain (ID3 Paradigm)
Rooted in information theory, Shannon entropy measures the average information content (in bits) required to identify the class of an arbitrary sample drawn from $S$:

$$H(S) = -\sum_{k=1}^K p_k \log_2(p_k)$$

*(with the analytical limit convention $0 \log_2 0 \equiv 0$, justified by $\lim_{p \to 0^+} p \log_2 p = 0$)*.

When node $S$ is partitioned on candidate feature $A$ into disjoint subsets $\{S_v\}_{v \in \text{Val}(A)}$, the **Information Gain** is the expected reduction in entropy:

$$IG(S, A) = H(S) - \sum_{v \in \text{Val}(A)} \frac{|S_v|}{|S|} H(S_v) = H(S) - H(S \mid A)$$

Information gain equals the Kullback-Leibler divergence between the joint distribution of target and attribute and their product marginals.

### 2.2 Gain Ratio (C4.5 Paradigm)
Information Gain exhibits an intrinsic bias toward high-cardinality features (e.g., splitting on a unique "Transaction ID" yields pure 1-sample leaves with zero entropy, but fails to generalize). Quinlan's C4.5 algorithm resolves this via the **Gain Ratio**, normalizing by the intrinsic entropy of the split itself:

$$GR(S, A) = \frac{IG(S, A)}{\text{SplitInfo}(S, A)}, \quad \text{where } \text{SplitInfo}(S, A) = -\sum_{v \in \text{Val}(A)} \frac{|S_v|}{|S|} \log_2\left( \frac{|S_v|}{|S|} \right)$$

### 2.3 Gini Impurity & Impurity Reduction (CART Paradigm)
Breiman's Classification and Regression Trees (CART) formulate impurity as the expected probability of misclassification if an observation is randomly labeled according to the empirical class distribution:

$$I_G(S) = \sum_{k=1}^K p_k (1 - p_k) = \sum_{k=1}^K p_k - \sum_{k=1}^K p_k^2 = 1 - \sum_{k=1}^K p_k^2$$

For a binary split $s = (j, \tau)$ dividing parent node $S$ into left child $S_L$ and right child $S_R$, the **Gini Impurity Reduction** (Gini Gain) is:

$$\Delta I_G(S, s) = I_G(S) - \left[ \frac{|S_L|}{|S|} I_G(S_L) + \frac{|S_R|}{|S|} I_G(S_R) \right]$$

```
+---------------------------------------------------------------------------------------+
|                    IMPURITY METRIC COMPARISON FOR BINARY CLASSIFICATION                |
+---------------------------------------------------------------------------------------+
|   Impurity                                                                            |
|     1.0 +                      .-""-.  Shannon Entropy H(p)                           |
|         |                    .'      '.                                               |
|     0.8 +                   /          \                                              |
|         |                  /   .-""-.   \  Scaled Gini 2*I_G(p) = 4p(1-p)             |
|     0.5 + - - - - - - - - / - ' - - -' - \ - - - - - - - - - - - - - - - - - - - -    |
|         |                |   /        \   |  Gini Impurity I_G(p) = 2p(1-p)           |
|     0.0 +----------------+--+----------+--+------------------------> p (Class Prob)   |
|        0.0                 0.5                 1.0                                    |
+---------------------------------------------------------------------------------------+
```

### 2.4 Mathematical & Computational Comparison
- **Curvature**: For binary classification ($K=2$ with $p \in [0, 1]$):
  $$H(p) = -p \log_2 p - (1-p) \log_2(1-p), \quad I_G(p) = 2p(1-p)$$
  Both curves are strictly concave, symmetric about $p = 0.5$, and achieve zero at the pure boundaries $p \in \{0, 1\}$.
- **Computational Efficiency**: Calculating Gini impurity requires simple floating-point multiplications and subtractions: $1 - p_1^2 - p_2^2$. Shannon entropy requires transcendental logarithmic evaluations ($\log_2$). Consequently, CART achieves significantly higher throughput during exhaustive split searches over large datasets.

---

## 3. Continuous Feature Discretization Algorithm

Unlike categorical features with finite symbolic branches, continuous features $x_j \in \mathbb{R}$ require dynamic discretization into binary inequality conditions:

$$[x_j \le \tau] \quad \text{vs.} \quad [x_j > \tau]$$

The standard inductive search algorithm executes as follows:
1. **Sort**: Given node sample $S$, sort distinct observed values of feature $j$ in ascending order:
   $$u_{(1)} < u_{(2)} < \dots < u_{(m)}$$
2. **Generate Candidate Midpoints**: Construct split thresholds at adjacent midpoints:
   $$\tau_i = \frac{u_{(i)} + u_{(i+1)}}{2}, \quad \text{for } i \in \{1, 2, \dots, m-1\}$$
3. **Boundary Pruning (Efficiency Optimization)**: In CART, midpoint $\tau_i$ is evaluated if and only if the samples at $u_{(i)}$ and $u_{(i+1)}$ have different class labels. A split between samples of identical classes cannot yield a local maximum for impurity reduction.
4. **Optimal Coordinate Selection**: Select the feature coordinate $j^*$ and threshold $\tau^*$ that jointly maximize the impurity reduction:
   $$(j^*, \tau^*) = \arg\max_{j \in \{1, \dots, d\}} \max_{\tau \in \mathcal{T}_j} \Delta I(S, (j, \tau))$$

---

## 4. Regularization, Pruning & Bias-Variance Dynamics

An unconstrained decision tree recursively partitions data until every leaf is pure ($I=0$) or contains a single sample. This leads to the classical high-variance failure mode:
- **Empirical Bias $\approx 0$**: The tree achieves near-zero training error by memorizing noise.
- **Empirical Variance $\gg 0$**: A minor perturbation in a single data point can alter the root split, completely reconfiguring the downstream tree topology.

### 4.1 Pre-Pruning (Early Stopping)
Pre-pruning halts recursive expansion during construction if stopping criteria are met:
- Maximum tree depth reached (`max_depth`).
- Node sample size below minimum threshold (`min_samples_split`).
- Leaf sample size below threshold (`min_samples_leaf`).
- Impurity reduction below tolerance ($\Delta I < \epsilon$).

### 4.2 Post-Pruning: Minimal Cost-Complexity Pruning (Weakest Link)
Breiman's CART post-pruning constructs a fully grown tree $T_0$ and minimizes a penalized cost-complexity functional:

$$R_\alpha(T) = R(T) + \alpha |T|$$

where:
- $R(T) = \sum_{t \in \widetilde{T}} R(t) = \sum_{t \in \widetilde{T}} \frac{|S_t|}{|S|} I(S_t)$ is the empirical misclassification risk.
- $|T| = |\widetilde{T}|$ is the number of terminal leaf nodes.
- $\alpha \ge 0$ is the complexity penalty parameter.

For each internal node $t$, the cost of collapsing subtree $T_t$ into a single leaf node $t$ is:
- Risk of leaf $t$: $R(t)$
- Risk of subtree $T_t$: $R(T_t) = \sum_{l \in \widetilde{T}_t} R(l)$
- Number of leaves in subtree: $|T_t|$

The effective cost per leaf pruned is:

$$\alpha_{\text{eff}}(t) = \frac{R(t) - R(T_t)}{|T_t| - 1}$$

By systematically collapsing the node with the smallest $\alpha_{\text{eff}}$, CART generates a finite nested sequence of candidate subtrees:

$$T_0 \supset T_1 \supset T_2 \supset \dots \supset T_{\text{root}}$$

The optimal subtree $T^*$ is then selected via $K$-fold cross-validation, achieving optimal bias-variance equilibrium.

---

## 5. DeepTutor 5-Tier Socratic Diagnostic Suite

Trace your understanding through these diagnostic tiers:

### Tier 1: Phenomenological Observation
Consider a dataset containing 16 positive instances and 0 negative instances. What is the Shannon entropy of this dataset? What is its Gini impurity? If you split this dataset into two groups of 8 samples, does the split provide any information gain?

### Tier 2: Socratic Probing
Why is the Gini impurity of a binary classification problem bounded above by $0.5$, whereas Shannon entropy is bounded above by $1.0$? Does this numerical difference alter the optimal split selection when evaluating candidate thresholds?

### Tier 3: Minimal Counterexample
Consider the XOR classification problem in 2D space:
- $(0, 0) \to 0$
- $(0, 1) \to 1$
- $(1, 0) \to 1$
- $(1, 1) \to 0$

Evaluate the Information Gain of splitting on $X_1$ at $\tau = 0.5$. What is $IG(S, X_1)$? What does this reveal about the limitations of greedy top-down heuristic tree induction?

### Tier 4: Abstract Mathematical Pattern
Let parent node $S$ contain $n$ samples with class distribution $(p, 1-p)$. Suppose split $s$ divides $S$ into two equal-sized children ($n_L = n_R = n/2$), with left child having proportion $p_L = p + \delta$ and right child having proportion $p_R = p - \delta$.
Prove algebraically that the Gini impurity reduction is:

$$\Delta I_G(S, s) = 2 \delta^2$$

What does this prove about the relationship between split asymmetry $\delta$ and impurity reduction?

### Tier 5: Autonomous Mastery Prompt
Design an algorithm that converts an arbitrary trained decision tree into a set of mutually exclusive, collectively exhaustive propositional logic rules in Disjunctive Normal Form (DNF). Prove that the rule set contains zero contradictory predictions.

---

## 6. Self-Study Keywords: Topic 2

- Recursive Binary Splitting
- Axis-Aligned Hyper-Rectangles
- Shannon Entropy & Information Theory Axioms
- Information Gain (Mutual Information $I(Y; X_j)$)
- C4.5 Gain Ratio & Split Information
- Gini Impurity (Multinomial Variance)
- Misclassification Error Rate
- Continuous Feature Discretization & Midpoint Scanning
- Hunt's Algorithm
- Breiman's CART (Classification and Regression Trees)
- Quinlan's ID3 and C4.5
- Pre-Pruning (Early Stopping Criteria)
- Minimal Cost-Complexity Pruning ($R_\alpha(T) = R(T) + \alpha |T|$)
- Effective Alpha Sequence ($\alpha_{\text{eff}}$)
- High Variance / Instability of Single Trees
- Bagging (Bootstrap Aggregating) & Out-of-Bag (OOB) Error
- Random Forests & Feature Subsampling ($\sqrt{d}$)
- Gradient Boosted Decision Trees (GBDT / XGBoost)
- Mean Decrease in Impurity (MDI) vs. Permutation Feature Importance
- Surrogate Splits for Handling Missing Telemetry
