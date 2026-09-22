# Module 4: Topic 3 — Polynomial Regression & Regularization Mechanics ($L_1$ vs. $L_2$)

**Document Reference**: `IMLC-2026-GUIDE-MOD4`  
**Topic Coverage**: Qualification Topic 3 (Overfitting, Polynomial Expansions, Ridge, Lasso & Bias-Variance)  
**Author**: Lead Educational Author & LaTeX Architect  
**Governing Standard**: DeepTutor Pedagogical Scaffolding & Strict R3 Non-Solution Compliance

---

## 1. Pedagogical Overview & Runge's Phenomenon

In empirical regression, the objective is to estimate an unknown target function $f^*(x)$ from noisy observations:

$$y = f^*(x) + \epsilon, \quad \text{where } \mathbb{E}[\epsilon] = 0, \quad \text{Var}(\epsilon) = \sigma^2$$

To approximate complex nonlinear relationships, linear models can be extended via a polynomial basis expansion:

$$\phi(x) = [1, x, x^2, \dots, x^p]^T \in \mathbb{R}^{p+1}$$

Under Weierstrass's Approximation Theorem, any continuous function on a closed interval can be approximated uniformly by a polynomial of sufficiently high degree. However, fitting high-degree polynomials to finite, noisy data via unconstrained Ordinary Least Squares (OLS) triggers **Runge's Phenomenon**: violent, uncontrolled oscillations between sample points, particularly near interval boundaries.

```
+---------------------------------------------------------------------------------------+
|                      RUNGE'S PHENOMENON & REGULARIZATION SMOOTHING                    |
+---------------------------------------------------------------------------------------+
|   y                                                                                   |
|   ^               _.-""-._                 Unconstrained High-Degree Polynomial       |
|   |             .'   *    '.               (Overfitting: Zero training loss,          |
|   |            /            \               exploding boundary oscillation)           |
|   |      *    /              \    *                                                   |
|   |     .    /                \    .           True Signal / Regularized Model        |
|   |    . \  /                  \  / .          (Smooth, Low Variance, Generalizes)    |
|   |   .   *'                    '*   .                                                |
|   |  *                                *                                               |
|   +----------------------------------------> x                                        |
|      0                                 1                                              |
+---------------------------------------------------------------------------------------+
```

As the polynomial degree $p$ increases, empirical training error monotonically decreases to zero, but expected test error explodes. Regularization introduces an inductive bias that penalizes excessively complex hypotheses, restoring numerical stability and generalization.

---

## 2. Ordinary Least Squares (OLS) & Its Breakdown

Let the design matrix $\Phi \in \mathbb{R}^{n \times (p+1)}$ have rows $\phi(x_i)^T = [1, x_i, x_i^2, \dots, x_i^p]$, and target vector $y \in \mathbb{R}^n$. The parameter vector is $w = [w_0, w_1, \dots, w_p]^T \in \mathbb{R}^{p+1}$.

### 2.1 The OLS Loss Function & Normal Equations
The Residual Sum of Squares (RSS) objective is:

$$\text{RSS}(w) = \frac{1}{2n} \|y - \Phi w\|_2^2 = \frac{1}{2n} (y - \Phi w)^T (y - \Phi w)$$

Taking the vector gradient with respect to $w$:

$$\nabla_w \text{RSS}(w) = -\frac{1}{n} \Phi^T (y - \Phi w)$$

Setting $\nabla_w \text{RSS}(w) = \mathbf{0}$ yields the classical **Normal Equations**:

$$\Phi^T \Phi w = \Phi^T y \implies w_{\text{OLS}} = (\Phi^T \Phi)^{-1} \Phi^T y$$

### 2.2 Pathological Breakdown Modes
1. **Underdetermined Regime ($p+1 > n$)**: When the number of features exceeds the sample size, $\text{rank}(\Phi^T \Phi) \le n < p+1$. The Gram matrix $\Phi^T \Phi$ is singular, yielding infinitely many interpolating solutions with arbitrarily large weight norms.
2. **Multicollinearity & Condition Number Collapse**: Even when $n > p+1$, polynomial powers $\{x, x^2, \dots, x^p\}$ are strongly correlated over positive domains. The condition number $\kappa(\Phi^T \Phi) = \frac{\sigma_{\max}^2}{\sigma_{\min}^2}$ explodes exponentially with degree $p$. Inversion inverts near-zero singular values, amplifying infinitesimal observation noise into massive coefficient swings of alternating signs.

---

## 3. Ridge Regularization ($L_2$ Tikhonov Regularization)

### 3.1 Conceptual Explanation (Mandatory Acceptance Requirement)
Ridge regression prevents overfitting by augmenting the empirical prediction loss with an isotropic Euclidean penalty on parameter magnitudes. Conceptually, while the prediction loss pulls the parameters toward whatever values reproduce the training targets, the $L_2$ penalty acts as a multi-dimensional elastic anchor centered at the origin, exerting an inward restoring force proportional to weight magnitude. Large weights are penalized quadratically, which discourages high-frequency polynomial oscillations and Runge's phenomenon. Because the intercept represents the mean target offset and does not contribute to function curvature or sensitivity, it is excluded from penalization.

### 3.2 Mathematical Formulation (Mandatory Acceptance Requirement)
The regularized Ridge loss function is:

$$J_{\text{Ridge}}(w) = \frac{1}{2n} \|y - \Phi w\|_2^2 + \frac{\lambda}{2} \|w_{1:p}\|_2^2 = \frac{1}{2n} \sum_{i=1}^n \left( y_i - \sum_{j=0}^p w_j x_i^j \right)^2 + \frac{\lambda}{2} \sum_{j=1}^p w_j^2$$

where $\lambda \ge 0$ is the regularization hyperparameter governing the tradeoff between training fidelity and hypothesis simplicity.

Let $I^*$ denote the $(p+1) \times (p+1)$ diagonal selector matrix:

$$I^* = \begin{bmatrix} 0 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{bmatrix}$$

The penalty can be expressed compactly in matrix notation as $\frac{\lambda}{2} w^T I^* w$.

### 3.3 Exact Matrix Gradient & Closed-Form Normal Equations
Differentiating $J_{\text{Ridge}}(w)$ with respect to parameter vector $w$:

$$\nabla_w J_{\text{Ridge}}(w) = -\frac{1}{n} \Phi^T (y - \Phi w) + \lambda I^* w$$

Setting the gradient to zero to find the stationary point:

$$\left( \frac{1}{n} \Phi^T \Phi + \lambda I^* \right) w = \frac{1}{n} \Phi^T y$$

Multiplying through by $n$ yields the regularized normal equations:

$$(\Phi^T \Phi + n\lambda I^*) w = \Phi^T y \implies \mathbf{w_{\text{Ridge}} = (\Phi^T \Phi + n\lambda I^*)^{-1} \Phi^T y}$$

### 3.4 Guaranteed Invertibility Proof
The matrix $\Phi^T \Phi$ is symmetric positive semi-definite ($\mu_i \ge 0$ for all eigenvalues). For $\lambda > 0$, the regularized non-intercept sub-matrix is strictly shifted by $n\lambda$:

$$\lambda_i(\Phi^T \Phi + n\lambda I^*) = \mu_i + n\lambda > 0 \quad (\forall i \ge 1)$$

Consequently, $(\Phi^T \Phi + n\lambda I^*)$ is strictly positive definite, well-conditioned, and unconditionally invertible, completely curing the multicollinearity pathology of OLS.

### 3.5 Gradient Descent Dynamics & Weight Decay Equivalence
Applying gradient descent with learning rate $\eta$:

$$w^{(t+1)} = w^{(t)} - \eta \nabla_w J_{\text{Ridge}}(w^{(t)}) = w^{(t)} - \eta \left( -\frac{1}{n} \Phi^T (y - \Phi w^{(t)}) + \lambda I^* w^{(t)} \right)$$

For the penalized coefficients ($j \ge 1$):

$$w_j^{(t+1)} = (1 - \eta \lambda) w_j^{(t)} + \eta \left[ \frac{1}{n} \Phi^T (y - \Phi w^{(t)}) \right]_j$$

The factor $(1 - \eta \lambda) < 1$ directly executes **weight decay**: before receiving the error-correction gradient update, every coefficient is shrunk toward zero by a constant geometric discount.

---

## 4. Lasso Regularization ($L_1$ Norm) & Coordinate Sparsity

Lasso (Least Absolute Shrinkage and Selection Operator) penalizes the taxicab ($L_1$) norm:

$$J_{\text{Lasso}}(w) = \frac{1}{2n} \|y - \Phi w\|_2^2 + \lambda \|w_{1:p}\|_1 = \frac{1}{2n} \|y - \Phi w\|_2^2 + \lambda \sum_{j=1}^p |w_j|$$

### 4.1 Subgradient Calculus
Because the absolute value function $|w_j|$ has a sharp corner at zero, it is non-differentiable at $w_j = 0$. Its subdifferential is:

$$\partial |w_j| = \begin{cases} \{+1\} & \text{if } w_j > 0 \\ \{-1\} & \text{if } w_j < 0 \\ [-1, +1] & \text{if } w_j = 0 \end{cases}$$

### 4.2 Soft-Thresholding Operator $\mathcal{S}_\lambda$
Under orthogonal design ($\Phi^T \Phi = I$), the exact coordinate-wise solution is governed by the **soft-thresholding operator**:

$$\hat{w}_j^{\text{Lasso}} = \mathcal{S}_\lambda(\hat{w}_j^{\text{OLS}}) = \text{sign}(\hat{w}_j^{\text{OLS}}) \max\left(0, |\hat{w}_j^{\text{OLS}}| - \lambda\right)$$

```
+---------------------------------------------------------------------------------------+
|                    COEFFICIENT SHRINKAGE: RIDGE (L2) VS. LASSO (L1)                   |
+---------------------------------------------------------------------------------------+
|   w_hat (Estimated)                                                                   |
|         ^                                                                             |
|         |                                    OLS (Unconstrained): w_hat = w_ols       |
|         |                                 . '                                         |
|         |                              . '   Ridge (L2 Linear Shrinkage):             |
|         |                           . '      w_hat = w_ols / (1 + lambda)             |
|         |                        . '                                                  |
|         |                     .-'            Lasso (L1 Soft-Thresholding):            |
|         |                 _.-'               Exact zeros when |w_ols| <= lambda       |
|   ------+---------------+--------------------> w_ols                                   |
|        -lambda         0     +lambda                                                  |
|         |           _.-'                                                              |
|         |        .-'                                                                  |
|         |     . '                                                                     |
+---------------------------------------------------------------------------------------+
```

---

## 5. Geometric Duality & SVD Spectral Shrinkage

### 5.1 Geometric Constraint Topology: Diamond vs. Sphere
Under KKT duality, regularization is equivalent to constrained optimization:

$$\min_w \text{RSS}(w) \quad \text{subject to} \quad \|w_{1:p}\|_q^q \le C$$

```
+---------------------------------------------------------------------------------------+
|                    GEOMETRY OF REGULARIZATION CONSTRAINTS                             |
+---------------------------------------------------------------------------------------+
|       w2                                        w2                                    |
|        ^                                         ^                                    |
|        |      Loss Contours                      |      Loss Contours                 |
|        |        ( .---. )                        |        ( .---. )                   |
|      --+--    (  /     \ )                     --+--    (  /     \ )                  |
|     /  |  \  (  |   *   | )                   /  |  \  (  |   *   | )                 |
|    /   |   \  (  \     / )                   |   |   |  (  \     / )                  |
|   +----+----+---+-'---'---> w1              -+---+---+---+-'---'---> w1               |
|    \   |   /  Tangent contact at vertex:     |   |   |  Tangential contact:           |
|     \  |  /   w2 = 0 (Exact Sparsity!)        \  |  /   w1, w2 != 0 (Smooth Shrink)   |
|      --+--                                     --+--                                  |
|        |                                         |                                    |
|     LASSO (L1): Diamond Constraint            RIDGE (L2): Spherical Constraint        |
+---------------------------------------------------------------------------------------+
```

- **Lasso ($L_1$, Diamond)**: The constraint boundary features non-differentiable vertices aligned with coordinate axes. Elliptical RSS level sets make first contact at these sharp vertices, setting non-informative coefficients **identically to zero** (sparse feature selection).
- **Ridge ($L_2$, Sphere)**: The constraint boundary is a smooth hypersphere. Contact occurs tangentially at non-axis points, shrinking all coefficients smoothly toward zero without eliminating them completely.

### 5.2 SVD Spectral Shrinkage in Ridge Regression
Let the Singular Value Decomposition of the centered design matrix be $\Phi = U \Sigma V^T$, where $U \in \mathbb{R}^{n \times p}$ and $V \in \mathbb{R}^{p \times p}$ are orthonormal matrices, and $\Sigma = \text{diag}(\sigma_1, \dots, \sigma_p)$.

Substituting into the Ridge closed-form estimator yields:

$$w_{\text{Ridge}} = \sum_{j=1}^p \left( \frac{\sigma_j^2}{\sigma_j^2 + n\lambda} \right) \frac{u_j^T y}{\sigma_j} v_j$$

Here, $\frac{u_j^T y}{\sigma_j} v_j$ is the unconstrained OLS projection onto principal direction $v_j$. Ridge introduces coordinate-wise **spectral filter factors**:

$$f_j = \frac{\sigma_j^2}{\sigma_j^2 + n\lambda} \in (0, 1]$$

- High-variance principal directions ($\sigma_j^2 \gg n\lambda$): $f_j \approx 1$, preserving dominant underlying patterns.
- Low-variance directions ($\sigma_j^2 \ll n\lambda$, corresponding to high-frequency noise or multicollinear features): $f_j \to 0$, aggressively filtering out spurious oscillations.

---

## 6. Rigorous Proof of the Bias-Variance Tradeoff

Assume data generation process $y = \Phi w_{\text{true}} + \epsilon$ with $\mathbb{E}[\epsilon] = \mathbf{0}$ and $\text{Cov}(\epsilon) = \sigma^2 I_n$.
Consider the Ridge estimator $w^* = (\Phi^T \Phi + \lambda I)^{-1} \Phi^T y$.

### 6.1 Expectation & Squared Bias Derivation
$$\mathbb{E}[w^*] = (\Phi^T \Phi + \lambda I)^{-1} \Phi^T \Phi w_{\text{true}}$$

The estimation bias vector is:

$$\text{Bias}(w^*) = \mathbb{E}[w^*] - w_{\text{true}} = -\lambda (\Phi^T \Phi + \lambda I)^{-1} w_{\text{true}}$$

In SVD coordinates:

$$\|\text{Bias}(w^*)\|_2^2 = \sum_{j=1}^p \left( \frac{\lambda}{\sigma_j^2 + \lambda} \right)^2 (v_j^T w_{\text{true}})^2$$

Differentiating with respect to $\lambda$:

$$\frac{\partial}{\partial \lambda} \|\text{Bias}(w^*)\|_2^2 = \sum_{j=1}^p 2 \left( \frac{\lambda}{\sigma_j^2 + \lambda} \right) \frac{\sigma_j^2}{(\sigma_j^2 + \lambda)^2} (v_j^T w_{\text{true}})^2 > 0 \quad (\forall \lambda > 0)$$

**Theorem**: Squared bias is strictly monotonically increasing with regularization parameter $\lambda$.

### 6.2 Variance Derivation
$$\text{Cov}(w^*) = (\Phi^T \Phi + \lambda I)^{-1} \Phi^T [\sigma^2 I] \Phi (\Phi^T \Phi + \lambda I)^{-1}$$

Taking the matrix trace to measure total variance:

$$\text{Var}(w^*) = \text{Tr}(\text{Cov}(w^*)) = \sigma^2 \sum_{j=1}^p \frac{\sigma_j^2}{(\sigma_j^2 + \lambda)^2}$$

Differentiating with respect to $\lambda$:

$$\frac{\partial}{\partial \lambda} \text{Var}(w^*) = \sigma^2 \sum_{j=1}^p \left( -\frac{2\sigma_j^2}{(\sigma_j^2 + \lambda)^3} \right) < 0 \quad (\forall \lambda > 0)$$

**Theorem**: Total parameter variance is strictly monotonically decreasing with regularization parameter $\lambda$.

```
+---------------------------------------------------------------------------------------+
|                         THE BIAS-VARIANCE OPTIMIZATION ENVELOPE                       |
+---------------------------------------------------------------------------------------+
|   Error                                                                               |
|     ^                                                                                 |
|     |  \                                             /  Total MSE = Bias^2 + Var      |
|     |   \                                           /                                 |
|     |    \           Optimal lambda*               /                                  |
|     |     \                |                      /                                   |
|     |      ' .             v                   . '      Squared Bias                  |
|     |         '-._                    _..-'-'                                         |
|     |             `""--..________..--""                                               |
|     |   . - - - - - - - - - - - - - - - - - - - - - .                                 |
|     |  Variance                                                                       |
|     +----------------------------------------------------> Regularization lambda      |
|        0 (OLS: Zero Bias, Huge Var)                  infty (All weights -> 0)         |
+---------------------------------------------------------------------------------------+
```

### 6.3 Existence of Superior Regularized Solution
Evaluating the derivative of the Mean Squared Error $\text{MSE}(\lambda) = \|\text{Bias}(\lambda)\|_2^2 + \text{Var}(\lambda)$ at $\lambda = 0$:

$$\left. \frac{\partial \|\text{Bias}\|_2^2}{\partial \lambda} \right|_{\lambda = 0} = 0, \quad \left. \frac{\partial \text{Var}}{\partial \lambda} \right|_{\lambda = 0} = -2\sigma^2 \sum_{j=1}^p \frac{1}{\sigma_j^4} < 0$$

$$\left. \frac{\partial \text{MSE}}{\partial \lambda} \right|_{\lambda = 0} = 0 - 2\sigma^2 \sum_{j=1}^p \frac{1}{\sigma_j^4} < 0$$

Because the derivative of total error is strictly negative at $\lambda = 0$, there **always exists a strictly positive regularization parameter $\lambda^* > 0$ such that the regularized Ridge model achieves strictly lower total expected prediction error than unconstrained OLS**.

---

## 7. DeepTutor 5-Tier Socratic Diagnostic Suite

### Tier 1: Phenomenological Observation
If you fit a 9th-degree polynomial to 10 distinct empirical measurements, what is the training Residual Sum of Squares (RSS)? If you evaluate this polynomial at an unobserved intermediate point, why does the prediction often deviate violently from common sense?

### Tier 2: Socratic Probing
Why is the intercept term $w_0$ excluded from the regularization penalty? If we set $w_0$ under heavy shrinkage ($\lambda w_0^2$), what happens to predictions when the entire dataset is vertically translated by $+100$ units?

### Tier 3: Minimal Counterexample
Consider two features $x_1$ and $x_2$ that are perfectly identical ($x_1 = x_2$).
- How does Ridge regression distribute the weights across $w_1$ and $w_2$?
- How does Lasso regression distribute the weights across $w_1$ and $w_2$?
*(Hint: Analyze the strict convexity of the $L_2$ Euclidean norm vs. the piece-wise linearity of the $L_1$ norm).*

### Tier 4: Abstract Mathematical Pattern
From the Ridge matrix gradient $\nabla_w J = -\frac{1}{n} \Phi^T (y - \Phi w) + \lambda w$, derive the gradient descent update with step size $\eta$. Show algebraically why this corresponds to multiplying the existing weight vector by a scalar shrinkage factor $(1 - \eta \lambda)$ before applying the empirical prediction error update.

### Tier 5: Autonomous Mastery Prompt
Formulate the Elastic Net loss function combining $L_1$ and $L_2$ penalties. Prove geometrically why Elastic Net retains Lasso's ability to create sparse models while avoiding Lasso's tendency to arbitrarily select only one feature from a group of highly correlated variables.

---

## 8. Self-Study Keywords: Topic 3

- Ordinary Least Squares (OLS) & Gauss-Markov Theorem
- Normal Equations & Gram Matrix $\Phi^T \Phi$
- Multicollinearity & Condition Number $\kappa(A)$
- Runge's Phenomenon & Chebyshev Spaced Nodes
- Polynomial Basis Expansion & Vandermonde Matrix
- Tikhonov Regularization ($L_2$ Ridge Penalty)
- Lasso ($L_1$ Least Absolute Shrinkage and Selection Operator)
- Elastic Net Regularization ($L_1 + L_2$)
- Subdifferential Calculus & Clarke Subgradients
- Coordinate Descent & Soft-Thresholding Operator $\mathcal{S}_\lambda$
- Karush-Kuhn-Tucker (KKT) Dual Formulation
- Singular Value Decomposition (SVD)
- Spectral Filter Factors ($f_j = \frac{\sigma_j^2}{\sigma_j^2 + \lambda}$)
- Weight Decay Dynamics in First-Order Optimization
- Bias-Variance Decomposition & Tradeoff Curves
- Bayesian Maximum A Posteriori (MAP) Estimation
- Isotropic Gaussian Prior (Ridge Equivalence)
- Laplace Prior (Lasso Equivalence)
- Structural Risk Minimization (Vapnik) & Occam's Razor
- Generalized Cross-Validation (GCV) for Parameter Selection
