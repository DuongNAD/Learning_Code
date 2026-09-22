import ast
import os
import re
from pathlib import Path

TARGET_DIRS = [
    Path('core/agents'),
    Path('core/tools'),
    Path('core/memory'),
    Path('core/domain')
]

TEST_DIRS = [
    Path('tests')
]

def analyze_ast(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    tree = ast.parse(content, filename=str(filepath))

    functions = []
    classes = []
    dummy_funcs = []
    fake_asserts = []
    docstring_only = []


    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            body = [stmt for stmt in node.body if not (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str))]
            is_dummy = False

            if len(body) == 0:
                docstring_only.append((node.name, node.lineno))
            elif len(body) == 1:
                stmt = body[0]
                if isinstance(stmt, ast.Pass):
                    is_dummy = True
                elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant) and stmt.value.value is Ellipsis:
                    is_dummy = True
                elif isinstance(stmt, ast.Raise) and isinstance(getattr(stmt, 'exc', Nonf), ast.Name) and stmt.exc.id == 'NotImplementedError':
                    is_dummy = True
                elif isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Constant):
                    is_dummy = True

            functions.append((node.name, node.lineno, is_dummy, len(node.body)))
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
        'filepath': filepath,
        'functions': functions,
        'classes': classes,
        'dummy_funcs': dummy_funcs,
        'docstring_only': docstring_only,
        'fake_asserts': fake_asserts
    }

print('=== 1. AST ANALYSIS OF CORE PRODUCTION CODE ===')
core_files = []
for d in TARGET_DIRS:
    for p in d.rglob('*.py'):
        if '__pycache__' not in str(p):
            core_files.append(p)

total_funcs = 0
total_classes = 0
all_dummies = []
all_docstrings_only = []

for f in sorted(core_files):
    res = analyze_ast(f)
    total_funcs += len(res['functions'])
    total_classes += len(res['classes'])
    if res['dummy_funcs']:
        all_dummies.extend([(f, d) for d in res['dummy_funcs']])
    if res['docstring_only']:
        all_docstrings_only.extend([(f, d) for d in res['docstring_only']])
    status = 'OK' if not res['dummy_funcs'] and not res['docstring_only'] else 'FLAGGED'
    print(f"[{status}] {f}: {len(res['functions'])} funcs, {len(res['classes'])} classes | Dummies: {len(res['dummy_funcs'])} | Empty/DocOnly: {len(res['docstring_only'])}")

print(f'Core summary: {len(core_files)} files, {total_funcs} functions, {total_classes} classes.')
print(f'Total dummy/stub functions: {len(all_dummies)}')
print(f'Total empty/docstring-only functions: {len(all_docstrings_only)}')

print('\n=== 2. AST ANALYSIS OF TEST CODE ===')
test_files = []
for d in TEST_DIRS:
    for p in d.rglob('*.py'):
        if '__pycache__' not in str(p):
            test_files.append(p)

total_test_funcs = 0
total_fake_asserts = 0
for f in sorted(test_files):
    res = analyze_ast(f)
    total_test_funcs += len(res['functions'])
    if res['fake_asserts']:
        total_fake_asserts += len(res['fake_asserts'])
        print(f'[FLAGGED] {f}: Fake asserts at lines {res["fake_asserts"]}')
    else:
        print(f'[OK] {f}: {len(res["functions"])} test funcs, 0 fake asserts')

print(f'Test summary: {len(test_files)} files, {total_test_funcs} test funcs, {total_fake_asserts} fake asserts.')
