import os
import json
import glob
import sys

workspace = r"d:\02_Learning_Knowledge\GCI_World_2026_September"
notebooks = glob.glob(os.path.join(workspace, "**", "*.ipynb"), recursive=True)

results = []

for nb_path in sorted(notebooks):
    rel_path = os.path.relpath(nb_path, workspace).replace("\\", "/")
    nb_info = {
        "file_path": rel_path,
        "filename": os.path.basename(nb_path),
        "folder": os.path.dirname(rel_path),
    }
    
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        cells = nb.get('cells', [])
        nb_info["total_cells"] = len(cells)
        nb_info["markdown_cells_count"] = sum(1 for c in cells if c.get('cell_type') == 'markdown')
        nb_info["code_cells_count"] = sum(1 for c in cells if c.get('cell_type') == 'code')
        
        headers = []
        code_snippets = []
        imports = set()
        
        for idx, c in enumerate(cells):
            cell_type = c.get('cell_type')
            src = "".join(c.get('source', []))
            if cell_type == 'markdown':
                for line in src.split('\n'):
                    sline = line.strip()
                    if sline.startswith('#'):
                        headers.append({"cell_idx": idx, "header": sline})
            elif cell_type == 'code':
                for line in src.split('\n'):
                    sline = line.strip()
                    if sline.startswith('import ') or sline.startswith('from '):
                        imports.add(sline)
                # Store sample code or function definitions
                if any(kw in src for kw in ['def ', 'class ', 'fit(', 'predict(', 'read_csv', 'train_test_split', 'StandardScaler', 'LinearRegression', 'LogisticRegression', 'DecisionTreeClassifier', 'homework(']):
                    code_snippets.append({
                        "cell_idx": idx,
                        "code": src[:500] # preview
                    })

        nb_info["headers"] = headers
        nb_info["imports"] = sorted(list(imports))
        nb_info["key_code_snippets_count"] = len(code_snippets)
        nb_info["sample_snippets"] = code_snippets[:10]
        results.append(nb_info)
    except Exception as e:
        nb_info["error"] = str(e)
        results.append(nb_info)

out_path = os.path.join(workspace, ".agents", "explorer_survey_2", "notebooks_summary.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Successfully analyzed {len(results)} notebooks. Saved to {out_path}")
