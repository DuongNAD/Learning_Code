import ast
import os
from pathlib import Path

def analyze_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=str(filepath))
    
    functions = []
    classes = []
    fake_asserts = []
    dummy_funcs = []
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            body = node.body
            is_dummy = False
            # Check if only pass or return constant
            if len(body) == 1:
                stmt = body[0]
                if isinstance(stmt, ast.Pass):
                    is_dummy = True
                elif isinstance(stmt, ast.Raise) and isinstance(getattr(stmt, "exc", None), ast.Name) and stmt.exc.id == "NotImplementedError":
                    is_dummy = True
                elif isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Constant):
                    is_dummy = True
            functions.append((node.name, node.lineno, is_dummy, len(body)))
            if is_dummy:
                dummy_funcs.append((node.name, node.lineno))
        elif isinstance(node, ast.ClassDef):
            classes.append((node.name, node.lineno))
        elif isinstance(node, ast.Assert):
            test = node.test
            if isinstance(test, ast.Constant) and test.value is True:
                fake_asserts.append(node.lineno)
            elif isinstance(test, ast.Compare) and isinstance(test.left, ast.Constant) and len(test.comparators) == 1 and isinstance(test.comparators[0], ast.Constant):
                if test.left.value == test.comparators[0].value:
                    fake_asserts.append(node.lineno)
                    
    return {
        "functions": functions,
        "classes": classes,
        "dummy_funcs": dummy_funcs,
        "fake_asserts": fake_asserts
    }

target_dirs = ["core/agents", "core/tools", "core/memory"]
all_files = []
for d in target_dirs:
    for p in Path(d).rglob("*.py"):
        if "__pycache__" not in str(p):
            all_files.append(p)

all_files.append(Path("tests/test_agent_core_m2.py"))

print(f"Auditing {len(all_files)} files...")
for p in all_files:
    res = analyze_file(p)
    dummy_str = f"DUMMIES: {res['dummy_funcs']}" if res["dummy_funcs"] else "No dummies"
    fake_str = f"FAKE ASSERTS: {res['fake_asserts']}" if res["fake_asserts"] else "No fake asserts"
    print(f"{p}: {len(res['functions'])} funcs, {len(res['classes'])} classes | {dummy_str} | {fake_str}")
