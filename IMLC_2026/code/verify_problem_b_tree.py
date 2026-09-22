"""
IMLC 2026 Qualification Round (Senior Division) - Problem B Verification
Module: verify_problem_b_tree.py

Focus:
    - Full Decision Tree implementation from first principles (no sklearn / black box).
    - Shannon Entropy, Gini Impurity, Information Gain, and Gini Gain calculations.
    - Evaluation of initial greenhouse tree on query (T=26 C, H=68%) -> KEEP CLOSED.
    - Testing 6 logged sensor observations; identifying misclassifications on rows 5 & 6.
    - Evaluation of candidate splits on CO2; proving CO2 > 1250 ppm yields IG = 1.0 bit, Gini = 0.0.
    - Refined tree architecture achieving 100% accuracy on all 6 observations.
    - Exporting tree structure (JSON, ASCII) and asserting all invariants.
"""

from __future__ import annotations
import math
import json
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple


# =====================================================================
# 1. Information-Theoretic Metric Implementations
# =====================================================================

def shannon_entropy(labels: Sequence[Any]) -> float:
    """
    Computes Shannon Entropy H(S) = -sum(p_i * log2(p_i)) for a given label sequence.
    
    Properties:
        - H(S) >= 0.
        - H(S) = 0 when all labels are identical (pure node).
        - H(S) = log2(K) for K equally distributed classes (maximal impurity).
    """
    n = len(labels)
    if n == 0:
        return 0.0
    
    counts: Dict[Any, int] = {}
    for y in labels:
        counts[y] = counts.get(y, 0) + 1
        
    entropy = 0.0
    for count in counts.values():
        if count > 0:
            p = count / n
            entropy -= p * math.log2(p)
            
    # Clean floating point inaccuracies near zero
    return 0.0 if abs(entropy) < 1e-12 else entropy


def gini_impurity(labels: Sequence[Any]) -> float:
    """
    Computes Gini Impurity G(S) = 1 - sum(p_i^2) for a given label sequence.
    
    Properties:
        - G(S) >= 0.
        - G(S) = 0 when all labels are identical.
        - G(S) = 1 - 1/K for K equally distributed classes.
    """
    n = len(labels)
    if n == 0:
        return 0.0
    
    counts: Dict[Any, int] = {}
    for y in labels:
        counts[y] = counts.get(y, 0) + 1
        
    sum_p_sq = sum((c / n) ** 2 for c in counts.values())
    gini = 1.0 - sum_p_sq
    return 0.0 if abs(gini) < 1e-12 else gini


def information_gain(parent_labels: Sequence[Any],
                     left_labels: Sequence[Any],
                     right_labels: Sequence[Any]) -> float:
    """
    Calculates Information Gain:
        IG(S, A) = H(S) - (|S_L| / |S|) * H(S_L) - (|S_R| / |S|) * H(S_R)
    """
    n_total = len(parent_labels)
    if n_total == 0:
        return 0.0
    
    n_left = len(left_labels)
    n_right = len(right_labels)
    
    if n_left + n_right != n_total:
        raise ValueError(f"Partition size mismatch: {n_left} + {n_right} != {n_total}")
        
    h_parent = shannon_entropy(parent_labels)
    h_left = shannon_entropy(left_labels)
    h_right = shannon_entropy(right_labels)
    
    weighted_child_entropy = (n_left / n_total) * h_left + (n_right / n_total) * h_right
    ig = h_parent - weighted_child_entropy
    return 0.0 if abs(ig) < 1e-12 else ig


def gini_gain(parent_labels: Sequence[Any],
              left_labels: Sequence[Any],
              right_labels: Sequence[Any]) -> float:
    """
    Calculates Gini Gain (Impurity Reduction):
        Delta G = G(S) - (|S_L| / |S|) * G(S_L) - (|S_R| / |S|) * G(S_R)
    """
    n_total = len(parent_labels)
    if n_total == 0:
        return 0.0
    
    n_left = len(left_labels)
    n_right = len(right_labels)
    
    if n_left + n_right != n_total:
        raise ValueError(f"Partition size mismatch: {n_left} + {n_right} != {n_total}")
        
    g_parent = gini_impurity(parent_labels)
    g_left = gini_impurity(left_labels)
    g_right = gini_impurity(right_labels)
    
    weighted_child_gini = (n_left / n_total) * g_left + (n_right / n_total) * g_right
    gain = g_parent - weighted_child_gini
    return 0.0 if abs(gain) < 1e-12 else gain


# =====================================================================
# 2. Decision Tree Data Structures & Engine
# =====================================================================

class DecisionTreeNode:
    """
    A single node in a decision tree representing either a split decision
    or a terminal leaf action.
    """
    def __init__(self,
                 feature: Optional[str] = None,
                 threshold: Optional[float] = None,
                 operator: str = ">",
                 action: Optional[str] = None,
                 left: Optional[DecisionTreeNode] = None,
                 right: Optional[DecisionTreeNode] = None,
                 name: Optional[str] = None):
        self.feature = feature
        self.threshold = threshold
        self.operator = operator  # Typically ">" for numeric splits
        self.action = action      # Present if this is a leaf node
        self.left = left          # Branch taken when condition evaluates to True
        self.right = right        # Branch taken when condition evaluates to False
        self.name = name

    @property
    def is_leaf(self) -> bool:
        return self.action is not None

    def predict(self, sample: Dict[str, float]) -> str:
        """Evaluates a single sample recursively down the tree."""
        if self.is_leaf:
            assert self.action is not None
            return self.action
        
        assert self.feature is not None
        assert self.threshold is not None
        
        val = sample.get(self.feature)
        if val is None:
            raise KeyError(f"Sample missing required feature: '{self.feature}'")
            
        if self.operator == ">":
            condition = (val > self.threshold)
        elif self.operator == "<=":
            condition = (val <= self.threshold)
        elif self.operator == ">=":
            condition = (val >= self.threshold)
        elif self.operator == "<":
            condition = (val < self.threshold)
        else:
            raise ValueError(f"Unsupported operator: {self.operator}")
            
        if condition:
            if self.left is None:
                raise RuntimeError(f"Node {self.name} True-branch is None")
            return self.left.predict(sample)
        else:
            if self.right is None:
                raise RuntimeError(f"Node {self.name} False-branch is None")
            return self.right.predict(sample)

    def to_dict(self) -> Dict[str, Any]:
        """Serializes node to recursive dictionary."""
        if self.is_leaf:
            return {"type": "leaf", "action": self.action}
        return {
            "type": "decision",
            "name": self.name,
            "feature": self.feature,
            "threshold": self.threshold,
            "operator": self.operator,
            "true_branch": self.left.to_dict() if self.left else None,
            "false_branch": self.right.to_dict() if self.right else None,
        }

    def to_ascii(self, depth: int = 0, prefix: str = "") -> str:
        """Renders tree as human-readable ASCII hierarchy."""
        indent = "  " * depth
        if self.is_leaf:
            return f"{indent}{prefix}-> Action: [{self.action}]\n"
        
        cond_str = f"{self.feature} {self.operator} {self.threshold}"
        res = f"{indent}{prefix}[Is {cond_str}?]\n"
        if self.left:
            res += self.left.to_ascii(depth + 1, prefix="True:  ")
        if self.right:
            res += self.right.to_ascii(depth + 1, prefix="False: ")
        return res


class GreenhouseDecisionTree:
    """Encapsulates a decision tree model with batch evaluation and diagnostic methods."""
    def __init__(self, root: DecisionTreeNode, name: str = "GreenhouseTree"):
        self.root = root
        self.name = name

    def predict(self, sample: Dict[str, float]) -> str:
        return self.root.predict(sample)

    def evaluate(self, dataset: List[Dict[str, Any]], target_key: str = "action") -> Dict[str, Any]:
        correct = 0
        total = len(dataset)
        predictions = []
        mismatches = []
        
        for i, row in enumerate(dataset):
            pred = self.predict(row)
            actual = row[target_key]
            is_match = (pred == actual)
            if is_match:
                correct += 1
            else:
                mismatches.append({
                    "row_index": i + 1,
                    "sample": {k: v for k, v in row.items() if k != target_key},
                    "expected": actual,
                    "predicted": pred,
                })
            predictions.append(pred)
            
        accuracy = correct / total if total > 0 else 0.0
        return {
            "total": total,
            "correct": correct,
            "accuracy": accuracy,
            "predictions": predictions,
            "mismatches": mismatches,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.root.to_dict(), indent=indent)

    def print_tree(self) -> str:
        return self.root.to_ascii()


# =====================================================================
# 3. Model Factories: Baseline and Refined Trees
# =====================================================================

def build_baseline_tree() -> GreenhouseDecisionTree:
    """
    Constructs the original baseline greenhouse tree from Problem B:
        - Root: Temperature > 28 C
            - Yes -> OPEN ROOF
            - No -> Humidity > 70%
                - Yes -> OPEN ROOF
                - No -> KEEP CLOSED
    """
    leaf_open_1 = DecisionTreeNode(action="OPEN", name="Leaf_Open_T")
    leaf_open_2 = DecisionTreeNode(action="OPEN", name="Leaf_Open_H")
    leaf_closed = DecisionTreeNode(action="KEEP CLOSED", name="Leaf_Keep_Closed")
    
    node_humidity = DecisionTreeNode(
        feature="humidity",
        threshold=70.0,
        operator=">",
        left=leaf_open_2,
        right=leaf_closed,
        name="Check_Humidity"
    )
    
    root = DecisionTreeNode(
        feature="temperature",
        threshold=28.0,
        operator=">",
        left=leaf_open_1,
        right=node_humidity,
        name="Root_Temperature"
    )
    
    return GreenhouseDecisionTree(root=root, name="Baseline_Greenhouse_Tree")


def build_refined_tree(co2_threshold: float = 1250.0) -> GreenhouseDecisionTree:
    """
    Constructs the refined decision tree incorporating the optimal CO2 split:
        - Root: Temperature > 28 C
            - Yes -> OPEN ROOF
            - No -> Humidity > 70%
                - Yes -> OPEN ROOF
                - No -> CO2 > co2_threshold (default 1250 ppm)
                    - Yes -> OPEN ROOF
                    - No -> KEEP CLOSED
    """
    leaf_open_1 = DecisionTreeNode(action="OPEN", name="Leaf_Open_T")
    leaf_open_2 = DecisionTreeNode(action="OPEN", name="Leaf_Open_H")
    leaf_open_3 = DecisionTreeNode(action="OPEN", name="Leaf_Open_CO2")
    leaf_closed = DecisionTreeNode(action="KEEP CLOSED", name="Leaf_Keep_Closed")
    
    node_co2 = DecisionTreeNode(
        feature="co2",
        threshold=co2_threshold,
        operator=">",
        left=leaf_open_3,
        right=leaf_closed,
        name="Check_CO2"
    )
    
    node_humidity = DecisionTreeNode(
        feature="humidity",
        threshold=70.0,
        operator=">",
        left=leaf_open_2,
        right=node_co2,
        name="Check_Humidity"
    )
    
    root = DecisionTreeNode(
        feature="temperature",
        threshold=28.0,
        operator=">",
        left=leaf_open_1,
        right=node_humidity,
        name="Root_Temperature"
    )
    
    return GreenhouseDecisionTree(root=root, name="Refined_Greenhouse_Tree")


# =====================================================================
# 4. Canonical Dataset from Problem B
# =====================================================================

CANONICAL_LOGGED_OBSERVATIONS: List[Dict[str, Any]] = [
    {"row": 1, "temperature": 31.0, "humidity": 60.0, "co2": 700.0,  "action": "OPEN"},
    {"row": 2, "temperature": 26.0, "humidity": 75.0, "co2": 650.0,  "action": "OPEN"},
    {"row": 3, "temperature": 25.0, "humidity": 60.0, "co2": 800.0,  "action": "KEEP CLOSED"},
    {"row": 4, "temperature": 27.0, "humidity": 68.0, "co2": 1100.0, "action": "KEEP CLOSED"},
    {"row": 5, "temperature": 24.0, "humidity": 55.0, "co2": 1400.0, "action": "OPEN"},
    {"row": 6, "temperature": 22.0, "humidity": 50.0, "co2": 1550.0, "action": "OPEN"},
]


# =====================================================================
# 5. Exhaustive Candidate Split Optimization on CO2
# =====================================================================

def evaluate_co2_splits(sub_dataset: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Evaluates all midpoints between distinct sorted CO2 values in the sub-dataset.
    Computes Shannon Entropy, Gini Impurity, Information Gain, and Gini Gain for each.
    """
    sorted_samples = sorted(sub_dataset, key=lambda s: s["co2"])
    co2_values = [s["co2"] for s in sorted_samples]
    parent_labels = [s["action"] for s in sorted_samples]
    
    h_parent = shannon_entropy(parent_labels)
    g_parent = gini_impurity(parent_labels)
    
    candidates = []
    # Evaluate midpoints between consecutive distinct values
    for i in range(len(co2_values) - 1):
        c1, c2 = co2_values[i], co2_values[i + 1]
        if c1 == c2:
            continue
        threshold = (c1 + c2) / 2.0
        
        # Partition into left (CO2 > threshold) and right (CO2 <= threshold)
        left_labels = [s["action"] for s in sorted_samples if s["co2"] > threshold]
        right_labels = [s["action"] for s in sorted_samples if s["co2"] <= threshold]
        
        h_left = shannon_entropy(left_labels)
        h_right = shannon_entropy(right_labels)
        g_left = gini_impurity(left_labels)
        g_right = gini_impurity(right_labels)
        
        ig = information_gain(parent_labels, left_labels, right_labels)
        gg = gini_gain(parent_labels, left_labels, right_labels)
        
        candidates.append({
            "threshold": threshold,
            "c_between": (c1, c2),
            "left_size": len(left_labels),
            "right_size": len(right_labels),
            "left_labels": left_labels,
            "right_labels": right_labels,
            "entropy_left": h_left,
            "entropy_right": h_right,
            "gini_left": g_left,
            "gini_right": g_right,
            "information_gain": ig,
            "gini_gain": gg,
            "is_pure": (h_left == 0.0 and h_right == 0.0),
        })
        
    return candidates


# =====================================================================
# 6. Comprehensive Verification Suite & Assertions
# =====================================================================

def verify_problem_b() -> Dict[str, Any]:
    """
    Executes the full formal verification pipeline for Problem B:
        1. Query (T=26, H=68) evaluation on initial tree -> asserts 'KEEP CLOSED'.
        2. Evaluates all 6 logged observations on initial tree:
           - Rows 1-4 correct, Rows 5-6 fail (accuracy = 4/6 = 66.67%).
        3. Sub-dataset analysis at (T <= 28 and H <= 70):
           - Initial entropy H = 1.0 bit, Gini = 0.5.
        4. Evaluates all candidate CO2 splits:
           - Midpoint (1100 + 1400)/2 = 1250 ppm achieves IG = 1.0000 bit, Gini Gain = 0.5000.
           - Child nodes are perfectly pure (H_L = 0, H_R = 0, G_L = 0, G_R = 0).
        5. Refined tree evaluation:
           - 100% accuracy on all 6 rows (0 misclassifications).
    """
    results: Dict[str, Any] = {}
    
    # -------------------------------------------------------------
    # Step 1: Query (T=26, H=68) on Initial Tree
    # -------------------------------------------------------------
    baseline_tree = build_baseline_tree()
    query_sample = {"temperature": 26.0, "humidity": 68.0, "co2": 800.0}
    query_pred = baseline_tree.predict(query_sample)
    
    assert query_pred == "KEEP CLOSED", (
        f"Assertion Failed: Query (T=26, H=68) must predict 'KEEP CLOSED', got '{query_pred}'"
    )
    results["query_prediction"] = query_pred
    
    # -------------------------------------------------------------
    # Step 2: Evaluation of 6 Logged Observations on Initial Tree
    # -------------------------------------------------------------
    eval_baseline = baseline_tree.evaluate(CANONICAL_LOGGED_OBSERVATIONS)
    assert eval_baseline["correct"] == 4, f"Expected 4 correct rows, got {eval_baseline['correct']}"
    assert eval_baseline["total"] == 6, f"Expected 6 total rows, got {eval_baseline['total']}"
    assert math.isclose(eval_baseline["accuracy"], 4.0 / 6.0, rel_tol=1e-5)
    
    # Check exact failure on rows 5 and 6
    mismatch_rows = [m["row_index"] for m in eval_baseline["mismatches"]]
    assert mismatch_rows == [5, 6], f"Expected mismatches on rows [5, 6], got {mismatch_rows}"
    for m in eval_baseline["mismatches"]:
        assert m["expected"] == "OPEN"
        assert m["predicted"] == "KEEP CLOSED"
        
    results["baseline_evaluation"] = eval_baseline
    
    # -------------------------------------------------------------
    # Step 3: Sub-dataset Impurity Prior to Split
    # Samples reaching (T <= 28 and H <= 70) are Rows 3, 4, 5, 6
    # -------------------------------------------------------------
    sub_dataset = [s for s in CANONICAL_LOGGED_OBSERVATIONS if s["row"] in (3, 4, 5, 6)]
    sub_labels = [s["action"] for s in sub_dataset]
    
    h_sub = shannon_entropy(sub_labels)
    g_sub = gini_impurity(sub_labels)
    
    assert math.isclose(h_sub, 1.0, abs_tol=1e-9), f"Sub-dataset entropy must be 1.0, got {h_sub}"
    assert math.isclose(g_sub, 0.5, abs_tol=1e-9), f"Sub-dataset Gini must be 0.5, got {g_sub}"
    
    results["sub_node_impurity"] = {"entropy": h_sub, "gini": g_sub}
    
    # -------------------------------------------------------------
    # Step 4: Candidate CO2 Splits Evaluation
    # -------------------------------------------------------------
    candidates = evaluate_co2_splits(sub_dataset)
    results["candidate_splits"] = candidates
    
    # Find the split at 1250 ppm
    split_1250 = next((c for c in candidates if math.isclose(c["threshold"], 1250.0)), None)
    assert split_1250 is not None, "Candidate split at 1250 ppm not found!"
    assert split_1250["is_pure"] is True, "Split at 1250 ppm must yield 100% pure child nodes"
    assert math.isclose(split_1250["information_gain"], 1.0, abs_tol=1e-9), (
        f"Information gain at 1250 ppm must be 1.0, got {split_1250['information_gain']}"
    )
    assert math.isclose(split_1250["gini_gain"], 0.5, abs_tol=1e-9), (
        f"Gini gain at 1250 ppm must be 0.5, got {split_1250['gini_gain']}"
    )
    assert split_1250["entropy_left"] == 0.0 and split_1250["entropy_right"] == 0.0
    assert split_1250["gini_left"] == 0.0 and split_1250["gini_right"] == 0.0
    
    # -------------------------------------------------------------
    # Step 5: Refined Tree Evaluation on Full Dataset
    # -------------------------------------------------------------
    refined_tree = build_refined_tree(co2_threshold=1250.0)
    eval_refined = refined_tree.evaluate(CANONICAL_LOGGED_OBSERVATIONS)
    
    assert eval_refined["correct"] == 6, f"Refined tree must classify 6/6 correct, got {eval_refined['correct']}"
    assert eval_refined["accuracy"] == 1.0, f"Refined tree accuracy must be 1.0, got {eval_refined['accuracy']}"
    assert len(eval_refined["mismatches"]) == 0, f"Mismatches must be empty, got {eval_refined['mismatches']}"
    
    # Assert query (T=26, H=68, CO2=800) still predicts KEEP CLOSED
    query_refined_pred = refined_tree.predict({"temperature": 26.0, "humidity": 68.0, "co2": 800.0})
    assert query_refined_pred == "KEEP CLOSED"
    
    # But query with elevated CO2 (T=26, H=68, CO2=1300) now predicts OPEN
    query_elevated_pred = refined_tree.predict({"temperature": 26.0, "humidity": 68.0, "co2": 1300.0})
    assert query_elevated_pred == "OPEN"
    
    results["refined_evaluation"] = eval_refined
    results["refined_tree_ascii"] = refined_tree.print_tree()
    results["all_assertions_passed"] = True
    
    return results


# =====================================================================
# 7. Standalone CLI Output Formatter
# =====================================================================

def main() -> None:
    print("=" * 80)
    print(" IMLC 2026 QUALIFICATION ROUND - PROBLEM B VERIFICATION")
    print(" The Greenhouse Tree: Information Theory & Optimal Splitting")
    print("=" * 80)
    
    res = verify_problem_b()
    
    print("\n[1] Query Verification:")
    print("    Input: Temperature = 26 C, Humidity = 68%")
    print(f"    Baseline Tree Output: {res['query_prediction']} [CONFIRMED]")
    
    print("\n[2] Baseline Tree Diagnostic on 6 Logged Observations:")
    base_eval = res["baseline_evaluation"]
    print(f"    Accuracy: {base_eval['correct']}/{base_eval['total']} ({base_eval['accuracy'] * 100:.2f}%)")
    for m in base_eval["mismatches"]:
        row_idx = m["row_index"]
        print(f"    - MISCLASSIFICATION on Row {row_idx}: "
              f"Actual='{m['expected']}', Pred='{m['predicted']}' | Sample={m['sample']}")
        
    print("\n[3] Information Theory Analysis at Sub-Node (T <= 28 and H <= 70):")
    sub_imp = res["sub_node_impurity"]
    print(f"    Parent Entropy H(S): {sub_imp['entropy']:.4f} bit (Maximal Uncertainty)")
    print(f"    Parent Gini Impurity G(S): {sub_imp['gini']:.4f}")
    
    print("\n[4] Candidate CO2 Split Search:")
    print("    Threshold (ppm) | Information Gain | Gini Gain | Left Purity | Right Purity")
    print("    " + "-" * 70)
    for c in res["candidate_splits"]:
        print(f"    {c['threshold']:15.1f} | {c['information_gain']:16.4f} | {c['gini_gain']:9.4f} | "
              f"H_L={c['entropy_left']:.2f} G_L={c['gini_left']:.2f} | "
              f"H_R={c['entropy_right']:.2f} G_R={c['gini_right']:.2f}")
        
    print("\n[5] Refined Decision Tree Architecture:")
    print(res["refined_tree_ascii"])
    
    ref_eval = res["refined_evaluation"]
    print(f"[6] Refined Tree Performance:")
    print(f"    Accuracy: {ref_eval['correct']}/{ref_eval['total']} ({ref_eval['accuracy'] * 100:.1f}%)")
    print("    All 6 observations correctly classified.")
    print("\n" + "=" * 80)
    print(" [OK] Problem B Verification Suite: ALL ASSERTIONS PASSED (100%)")
    print("=" * 80)


def test_verify_problem_b() -> None:
    """Entry point for automated pytest discovery."""
    res = verify_problem_b()
    assert res["all_assertions_passed"] is True


if __name__ == "__main__":
    main()

