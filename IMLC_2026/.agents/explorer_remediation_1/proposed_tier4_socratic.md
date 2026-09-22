### Tier 4: Abstract Mathematical Pattern (Replacement for Section 6)
Consider an idealized scalar approximation where reward gain is a concave function $g(t)$ of policy drift $t \ge 0$, and regularization is enforced via a strictly convex penalty $\Omega(t)$:
$$\mathcal{L}(t) = -g(t) + \beta \Omega(t), \quad \text{with } g'(t) > 0, \; g''(t) \le 0, \; \Omega'(t) > 0, \; \Omega''(t) > 0$$
1. Using the First-Order Condition $\frac{d\mathcal{L}}{dt} = 0$, express the relationship between marginal reward gain and marginal penalty cost at the optimal drift $t^*$.
2. Prove that the Second-Order Condition $\frac{d^2\mathcal{L}}{dt^2} > 0$ holds strictly for all $\beta > 0$, guaranteeing a unique global minimum.
3. If an engineering specification requires $t^* \le T_{\text{drift}}$ for all reward scales $r \le r_{\max}$, formulate how the worst-case supremum $\sup_{r \le r_{\max}} t^*(r, \beta) \le T_{\text{drift}}$ establishes a lower bound on alignment strength $\beta$.

### Keywords Replacement (Replacement for Section 7)
- Safe Policy Divergence & Governance Boundaries
- Trust-Region Policy Optimization (TRPO)
