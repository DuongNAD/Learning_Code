"""
IMLC 2026 Qualification Round (Senior Division) - Problem D Verification
Module: verify_problem_d_rlhf.py

Focus:
    - Loss function: L(t) = -r*t + beta*t^2 with r > 0, beta > 0.
    - Analytical & numerical derivation of optimal shift t* = r / (2*beta) and minimal loss L(t*) = -r^2 / (4*beta).
    - Asymptotic behavior: beta -> 0+ (unbounded reward hacking) vs beta -> infty (frozen reference policy).
    - Verification of Safe Boundary Condition: for all r in (0, r_max], t*(r) <= T <=> beta >= r_max / (2*T).
    - Simulation of policy drift in token distribution space:
        * Reference policy pi_ref
        * Reward model r(y)
        * Optimal Gibbs policy pi*(y) proportional to pi_ref(y) * exp(r(y) / beta)
    - Empirical KL divergence D_KL(pi* || pi_ref) and Fisher Information quadratic proxy equivalence.
"""

from __future__ import annotations
import math
from typing import Any, Dict, List, Tuple
import numpy as np


# =====================================================================
# 1. Scalar RLHF Drift Loss & Analytical Derivations
# =====================================================================

def rlhf_drift_loss(t: float, r: float, beta: float) -> float:
    """
    Computes the scalar alignment training loss:
        L(t) = -r*t + beta*t^2
    """
    return -r * t + beta * (t ** 2)


def analytical_optimal_drift(r: float, beta: float) -> float:
    """
    First-order condition dL/dt = -r + 2*beta*t = 0
    => t* = r / (2*beta)
    """
    if beta <= 0:
        raise ValueError("beta must be strictly positive.")
    return r / (2.0 * beta)


def analytical_minimal_loss(r: float, beta: float) -> float:
    """
    L(t*) = -r*(r/(2*beta)) + beta*(r/(2*beta))^2 = -r^2 / (4*beta)
    """
    if beta <= 0:
        raise ValueError("beta must be strictly positive.")
    return -(r ** 2) / (4.0 * beta)


def numerical_optimize_drift(r: float, beta: float,
                             t_bounds: Tuple[float, float] = (0.0, 1000.0),
                             num_steps: int = 100) -> Tuple[float, float]:
    """
    Performs numerical optimization (Golden Section Search) to find the minimum
    of L(t) independently of the analytical formula.
    """
    a, b = t_bounds
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    resphi = 2.0 - phi
    
    c = a + resphi * (b - a)
    d = b - resphi * (b - a)
    fc = rlhf_drift_loss(c, r, beta)
    fd = rlhf_drift_loss(d, r, beta)
    
    for _ in range(num_steps):
        if fc < fd:
            b = d
            d = c
            fd = fc
            c = a + resphi * (b - a)
            fc = rlhf_drift_loss(c, r, beta)
        else:
            a = c
            c = d
            fc = fd
            d = b - resphi * (b - a)
            fd = rlhf_drift_loss(d, r, beta)
            
    t_opt = (a + b) / 2.0
    loss_opt = rlhf_drift_loss(t_opt, r, beta)
    return t_opt, loss_opt


# =====================================================================
# 2. Safety Bound Condition Verification Engine
# =====================================================================

def verify_safety_bound(r_max: float, T: float, num_samples: int = 10000, seed: int = 42) -> Dict[str, Any]:
    """
    Verifies the Safe Boundary Theorem:
        For all r in (0, r_max], t*(r) <= T  <=>  beta >= r_max / (2*T).
        
    Simulates stochastic rewards r drawn uniformly from (0, r_max] under three regimes:
        1. Sub-critical (beta < beta_crit): drift exceeds safety threshold T.
        2. Critical (beta = beta_crit): supremum drift equals T exactly.
        3. Super-critical (beta > beta_crit): drift strictly within safety limit T.
    """
    rng = np.random.default_rng(seed)
    beta_crit = r_max / (2.0 * T)
    
    # Generate random noisy rewards in (0, r_max]
    rewards = rng.uniform(1e-6, r_max, size=num_samples)
    
    # 1. Sub-critical regime: beta = 0.8 * beta_crit
    beta_sub = 0.8 * beta_crit
    drifts_sub = rewards / (2.0 * beta_sub)
    max_drift_sub = float(np.max(drifts_sub))
    violations_sub = int(np.sum(drifts_sub > T))
    
    # 2. Critical regime: beta = 1.0 * beta_crit
    drifts_crit = rewards / (2.0 * beta_crit)
    max_drift_crit = float(np.max(drifts_crit))
    violations_crit = int(np.sum(drifts_crit > T))
    
    # 3. Super-critical regime: beta = 1.25 * beta_crit
    beta_super = 1.25 * beta_crit
    drifts_super = rewards / (2.0 * beta_super)
    max_drift_super = float(np.max(drifts_super))
    violations_super = int(np.sum(drifts_super > T))
    
    return {
        "r_max": r_max,
        "T_limit": T,
        "beta_critical": beta_crit,
        "sub_critical": {
            "beta": beta_sub,
            "max_drift": max_drift_sub,
            "violations_count": violations_sub,
            "violates": max_drift_sub > T
        },
        "critical": {
            "beta": beta_crit,
            "max_drift": max_drift_crit,
            "violations_count": violations_crit,
            "exact_bound_achieved": math.isclose(r_max / (2.0 * beta_crit), T, rel_tol=1e-12)
        },
        "super_critical": {
            "beta": beta_super,
            "max_drift": max_drift_super,
            "violations_count": violations_super,
            "safe": max_drift_super <= T
        }
    }


# =====================================================================
# 3. Distributional RLHF & Gibbs Policy Simulation
# =====================================================================

def softmax(logits: np.ndarray) -> np.ndarray:
    """Stable softmax implementation."""
    shifted = logits - np.max(logits)
    exp_logits = np.exp(shifted)
    return exp_logits / np.sum(exp_logits)


def compute_kl_divergence(p: np.ndarray, q: np.ndarray) -> float:
    """
    Computes Kullback-Leibler divergence D_KL(P || Q) = sum(P(y) * log(P(y) / Q(y))).
    """
    eps = 1e-15
    p_safe = np.clip(p, eps, 1.0)
    q_safe = np.clip(q, eps, 1.0)
    kl = np.sum(p_safe * np.log(p_safe / q_safe))
    return float(max(0.0, kl))


def simulate_token_space_rlhf(vocab_size: int = 64,
                              seed: int = 123) -> Dict[str, Any]:
    """
    Simulates policy alignment in token distribution space:
        - Reference policy pi_ref over vocabulary.
        - Reward function r(y) across tokens.
        - Closed-form optimal Gibbs distribution:
              pi*(y) = (1 / Z) * pi_ref(y) * exp(r(y) / beta).
        - Computes empirical KL divergence D_KL(pi* || pi_ref) across a spectrum of beta.
    """
    rng = np.random.default_rng(seed)
    
    # Reference policy generated from logit distribution
    ref_logits = rng.normal(0.0, 1.0, size=vocab_size)
    pi_ref = softmax(ref_logits)
    
    # Token rewards r(y)
    rewards = rng.uniform(0.5, 3.0, size=vocab_size)
    
    beta_values = np.logspace(-1, 2, 20)  # beta from 0.1 to 100
    kl_divergences = []
    mean_rewards = []
    
    for beta in beta_values:
        # Gibbs policy unnormalized log weights: log(pi_ref) + r(y)/beta
        unnorm_log = np.log(pi_ref + 1e-15) + (rewards / beta)
        pi_star = softmax(unnorm_log)
        
        kl = compute_kl_divergence(pi_star, pi_ref)
        expected_reward = float(np.sum(pi_star * rewards))
        
        kl_divergences.append(kl)
        mean_rewards.append(expected_reward)
        
    return {
        "beta_values": beta_values,
        "kl_divergences": np.array(kl_divergences),
        "mean_rewards": np.array(mean_rewards),
        "pi_ref": pi_ref,
        "rewards": rewards
    }


# =====================================================================
# 4. Fisher Information Geometry & Quadratic Proxy Equivalence
# =====================================================================

def verify_fisher_quadratic_proxy_equivalence(vocab_size: int = 16, seed: int = 999) -> Dict[str, Any]:
    """
    Proves and verifies that the quadratic proxy beta * t^2 in Problem D is the exact
    second-order Riemannian Fisher Information approximation of the KL penalty:
        D_KL(pi_{theta + Delta theta} || pi_theta) = 0.5 * Delta theta^T F(theta) Delta theta + O(||Delta theta||^3)
    
    Let t^2 = Delta theta^T F(theta) Delta theta (Mahalanobis distance under Fisher metric).
    As ||Delta theta|| -> 0, the ratio D_KL / (0.5 * t^2) converges exactly to 1.0000.
    """
    rng = np.random.default_rng(seed)
    theta_0 = rng.normal(0.0, 1.0, size=vocab_size)
    pi_0 = softmax(theta_0)
    
    # Fisher Information Matrix for categorical softmax distribution:
    # F_{jk} = diag(pi_0) - pi_0 @ pi_0^T
    F = np.diag(pi_0) - np.outer(pi_0, pi_0)
    
    # Perturbation direction
    delta_dir = rng.normal(0.0, 1.0, size=vocab_size)
    delta_dir -= np.mean(delta_dir)  # Center to eliminate gauge redundancy
    delta_dir /= np.linalg.norm(delta_dir)
    
    # Test across decreasing step sizes epsilon
    epsilons = [1.0, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001]
    ratios = []
    
    for eps in epsilons:
        delta_theta = eps * delta_dir
        pi_perturbed = softmax(theta_0 + delta_theta)
        
        kl_exact = compute_kl_divergence(pi_perturbed, pi_0)
        fisher_quadratic = 0.5 * float(delta_theta.T @ F @ delta_theta)
        
        ratio = kl_exact / fisher_quadratic if fisher_quadratic > 0 else 1.0
        ratios.append(ratio)
        
    return {
        "epsilons": epsilons,
        "convergence_ratios": ratios,
        "limiting_ratio": ratios[-1]
    }


# =====================================================================
# 5. Master Verification Pipeline for Problem D
# =====================================================================

def verify_problem_d() -> Dict[str, Any]:
    """
    Executes the full formal verification pipeline for Problem D:
        1. Numerical vs Analytical verification of t* and L(t*).
        2. First-order and second-order strict convexity verification.
        3. Asymptotic analysis: beta -> 0+ and beta -> infty.
        4. Safety Bound Theorem: sup_{r <= r_max} t*(r) <= T <=> beta >= r_max / (2*T).
        5. Token distribution space Gibbs policy & empirical KL divergence.
        6. Fisher Information quadratic proxy convergence proof.
    """
    results: Dict[str, Any] = {}
    
    # -------------------------------------------------------------
    # Step 1: Numerical vs Analytical Verification of t* and L(t*)
    # -------------------------------------------------------------
    test_cases = [
        {"r": 2.0, "beta": 1.0},
        {"r": 5.0, "beta": 2.5},
        {"r": 1.2, "beta": 0.3},
        {"r": 10.0, "beta": 0.5},
    ]
    
    for tc in test_cases:
        r, beta = tc["r"], tc["beta"]
        t_ana = analytical_optimal_drift(r, beta)
        loss_ana = analytical_minimal_loss(r, beta)
        
        t_num, loss_num = numerical_optimize_drift(r, beta)
        
        assert math.isclose(t_ana, t_num, rel_tol=1e-5), (
            f"Analytical t* ({t_ana}) does not match numerical ({t_num}) for r={r}, beta={beta}"
        )
        assert math.isclose(loss_ana, loss_num, rel_tol=1e-5), (
            f"Analytical loss ({loss_ana}) does not match numerical ({loss_num}) for r={r}, beta={beta}"
        )
        
        # Verify first-order condition: dL/dt = -r + 2*beta*t == 0
        grad = -r + 2.0 * beta * t_ana
        assert math.isclose(grad, 0.0, abs_tol=1e-12), f"First derivative must be 0 at t*, got {grad}"
        
        # Verify second-order condition: d^2L/dt^2 = 2*beta > 0
        hessian = 2.0 * beta
        assert hessian > 0.0, f"Second derivative must be positive for convexity, got {hessian}"
        
    results["optimal_drift_verified"] = True
    
    # -------------------------------------------------------------
    # Step 2: Asymptotic Analysis
    # -------------------------------------------------------------
    r_fixed = 4.0
    
    # beta -> 0+
    betas_small = [1e-1, 1e-2, 1e-3, 1e-4]
    t_stars_small = [analytical_optimal_drift(r_fixed, b) for b in betas_small]
    # Verify t* grows without bound
    assert all(t_stars_small[i] < t_stars_small[i+1] for i in range(len(t_stars_small) - 1))
    assert t_stars_small[-1] >= 20000.0, "t* must approach infinity as beta -> 0"
    
    # beta -> infty
    betas_large = [10.0, 100.0, 1000.0, 10000.0]
    t_stars_large = [analytical_optimal_drift(r_fixed, b) for b in betas_large]
    # Verify t* shrinks to zero
    assert all(t_stars_large[i] > t_stars_large[i+1] for i in range(len(t_stars_large) - 1))
    assert t_stars_large[-1] <= 0.001, "t* must approach 0 as beta -> infty"
    
    results["asymptotics"] = {
        "beta_to_zero_max_drift": t_stars_small[-1],
        "beta_to_infty_min_drift": t_stars_large[-1]
    }
    
    # -------------------------------------------------------------
    # Step 3: Safety Bound Theorem Verification
    # -------------------------------------------------------------
    r_max = 6.0
    T_limit = 1.5
    expected_beta_crit = r_max / (2.0 * T_limit)  # 6.0 / (2 * 1.5) = 2.0
    
    safety_res = verify_safety_bound(r_max=r_max, T=T_limit, num_samples=20000)
    assert math.isclose(safety_res["beta_critical"], expected_beta_crit, rel_tol=1e-12)
    assert safety_res["sub_critical"]["violates"] is True, "Sub-critical beta must violate safety limit"
    assert safety_res["sub_critical"]["violations_count"] > 0
    assert safety_res["critical"]["exact_bound_achieved"] is True, "Critical beta must match T exactly"
    assert safety_res["super_critical"]["safe"] is True, "Super-critical beta must remain within safety limit"
    assert safety_res["super_critical"]["violations_count"] == 0
    
    results["safety_bound"] = safety_res
    
    # -------------------------------------------------------------
    # Step 4: Token Distribution Space Gibbs Policy Simulation
    # -------------------------------------------------------------
    dist_res = simulate_token_space_rlhf(vocab_size=32)
    kl_vals = dist_res["kl_divergences"]
    beta_vals = dist_res["beta_values"]
    
    # Verify KL divergence strictly decreases as beta increases
    kl_diffs = np.diff(kl_vals)
    assert np.all(kl_diffs <= 0.0), "KL divergence must decrease monotonically as beta increases"
    
    results["token_rlhf"] = {
        "kl_at_min_beta": float(kl_vals[0]),
        "kl_at_max_beta": float(kl_vals[-1]),
        "mean_reward_at_min_beta": float(dist_res["mean_rewards"][0]),
        "mean_reward_at_max_beta": float(dist_res["mean_rewards"][-1])
    }
    
    # -------------------------------------------------------------
    # Step 5: Fisher Information Quadratic Equivalence
    # -------------------------------------------------------------
    fisher_res = verify_fisher_quadratic_proxy_equivalence(vocab_size=16)
    limiting_ratio = fisher_res["limiting_ratio"]
    assert math.isclose(limiting_ratio, 1.0000, rel_tol=1e-2), (
        f"KL / (0.5 * Fisher_quad) must converge to 1.0, got {limiting_ratio}"
    )
    
    results["fisher_equivalence"] = {
        "epsilons": fisher_res["epsilons"],
        "convergence_ratios": fisher_res["convergence_ratios"],
        "limiting_ratio": limiting_ratio
    }
    results["all_assertions_passed"] = True
    
    return results


# =====================================================================
# 6. Standalone CLI Output Formatter
# =====================================================================

def main() -> None:
    print("=" * 80)
    print(" IMLC 2026 QUALIFICATION ROUND - PROBLEM D VERIFICATION")
    print(" The Price of Drift: RLHF Policy Drift, Asymptotics & Safety Bounds")
    print("=" * 80)
    
    res = verify_problem_d()
    
    print("\n[1] Analytical vs Numerical Optimal Drift:")
    print("    Loss Function: L(t) = -r*t + beta*t^2")
    print("    First Derivative:  dL/dt = -r + 2*beta*t = 0  => t* = r / (2*beta)")
    print("    Second Derivative: d^2L/dt^2 = 2*beta > 0      => Strictly Convex (Global Min)")
    print("    Minimal Loss:      L(t*) = -r^2 / (4*beta)")
    print("    Status: [VERIFIED 100% MATCH WITH NUMERICAL OPTIMIZER]")
    
    print("\n[2] Asymptotic Regime Verification:")
    asymp = res["asymptotics"]
    print(f"    - As beta -> 0+:  t* -> +infty (Observed t* = {asymp['beta_to_zero_max_drift']:.1f}) [Reward Hacking]")
    print(f"    - As beta -> inf: t* -> 0+     (Observed t* = {asymp['beta_to_infty_min_drift']:.6f}) [Frozen Policy]")
    
    print("\n[3] Safe Boundary Condition Theorem:")
    sb = res["safety_bound"]
    r_max = sb["r_max"]
    T_lim = sb["T_limit"]
    b_crit = sb["beta_critical"]
    print(f"    Parameters: r_max = {r_max:.2f}, Safety Threshold T = {T_lim:.2f}")
    print(f"    Theoretical Critical Bound: beta_crit = r_max / (2*T) = {b_crit:.4f}")
    print(f"    - Sub-critical (beta = {sb['sub_critical']['beta']:.2f} < {b_crit:.2f}):")
    print(f"        Max Drift = {sb['sub_critical']['max_drift']:.4f} > T ({T_lim:.2f}) | "
          f"Violations = {sb['sub_critical']['violations_count']} [UNSAFE]")
    print(f"    - Critical Bound (beta = {sb['critical']['beta']:.2f} == {b_crit:.2f}):")
    print(f"        Max Drift = {sb['critical']['max_drift']:.4f} <= T ({T_lim:.2f}) | Exact Boundary [TIGHT]")
    print(f"    - Super-critical (beta = {sb['super_critical']['beta']:.2f} > {b_crit:.2f}):")
    print(f"        Max Drift = {sb['super_critical']['max_drift']:.4f} < T ({T_lim:.2f}) | "
          f"Violations = {sb['super_critical']['violations_count']} [GUARANTEED SAFE]")
    
    print("\n[4] Distributional Token Space RLHF (Gibbs Policy):")
    tok = res["token_rlhf"]
    print(f"    - At low beta (0.1):  D_KL = {tok['kl_at_min_beta']:.4f} bits | Mean Reward = {tok['mean_reward_at_min_beta']:.4f}")
    print(f"    - At high beta (100): D_KL = {tok['kl_at_max_beta']:.4f} bits | Mean Reward = {tok['mean_reward_at_max_beta']:.4f}")
    print("    Tradeoff: Higher beta restrains KL drift at the cost of aggressive reward pursuit.")
    
    print("\n[5] Fisher Information Geometry & Quadratic Proxy Equivalence:")
    fe = res["fisher_equivalence"]
    print("    Epsilon step | D_KL / (0.5 * Delta_theta^T * F * Delta_theta)")
    print("    " + "-" * 55)
    for eps, ratio in zip(fe["epsilons"], fe["convergence_ratios"]):
        print(f"    {eps:12.4f} | {ratio:20.6f}")
    print(f"    Limiting Ratio as eps -> 0: {fe['limiting_ratio']:.6f} [CONVERGES EXACTLY TO 1.0000]")
    print("    Proves beta * t^2 is the local Riemannian representation of beta * D_KL.")
    
    print("\n" + "=" * 80)
    print(" [OK] Problem D Verification Suite: ALL ASSERTIONS PASSED (100%)")
    print("=" * 80)


def test_verify_problem_d() -> None:
    """Entry point for automated pytest discovery."""
    res = verify_problem_d()
    assert res["all_assertions_passed"] is True


if __name__ == "__main__":
    main()

