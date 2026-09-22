import os
import json
import glob
import re

workspace = r"d:\02_Learning_Knowledge\GCI_World_2026_September"
notebooks = glob.glob(os.path.join(workspace, "**", "*.ipynb"), recursive=True)

report_data = {}

for nb_path in sorted(notebooks):
    rel_path = os.path.relpath(nb_path, workspace).replace("\\", "/")
    filename = os.path.basename(nb_path)
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    cells = nb.get('cells', [])
    md_cells = [c for c in cells if c.get('cell_type') == 'markdown']
    code_cells = [c for c in cells if c.get('cell_type') == 'code']
    
    # 1. Headers
    headers = []
    for c in md_cells:
        src = "".join(c.get('source', []))
        for line in src.split('\n'):
            line = line.strip()
            if line.startswith('#'):
                headers.append(line)
                
    # 2. Code analysis
    all_code = "\n".join(["".join(c.get('source', [])) for c in code_cells])
    
    # Imports
    imports = []
    for line in all_code.split('\n'):
        sline = line.strip()
        if sline.startswith('import ') or sline.startswith('from '):
            if sline not in imports:
                imports.append(sline)
                
    # Datasets
    datasets = re.findall(r'[\'"][^\'"]+\.(?:csv|tsv|data|txt)[\'"]', all_code)
    
    # Functions defined
    functions_defined = re.findall(r'def\s+([a-zA-Z0-9_]+)\s*\(', all_code)
    
    # Key ML models & sklearn methods
    ml_keywords = ['LinearRegression', 'Ridge', 'Lasso', 'LogisticRegression', 'DecisionTreeClassifier',
                   'RandomForestClassifier', 'RandomForestRegressor', 'KNeighborsClassifier', 'SVC', 'SVR',
                   'KMeans', 'PCA', 'train_test_split', 'StandardScaler', 'MinMaxScaler', 'OneHotEncoder',
                   'mean_squared_error', 'r2_score', 'accuracy_score', 'confusion_matrix', 'classification_report',
                   'roc_auc_score', 'cross_val_score', 'GridSearchCV']
    detected_ml = [kw for kw in ml_keywords if kw in all_code]
    
    # Pandas & numpy methods
    pd_np_methods = ['read_csv', 'head', 'info', 'describe', 'isnull', 'fillna', 'dropna', 'get_dummies',
                     'corr', 'plot', 'hist', 'scatter', 'groupby', 'merge', 'concat', 'iloc', 'loc',
                     'np.array', 'np.arange', 'np.zeros', 'np.ones', 'np.dot', 'np.linalg', 'np.random']
    detected_pd_np = [m for m in pd_np_methods if m in all_code]
    
    # Markdown content overview (first 2 markdown cells text)
    intro_md = ""
    for c in md_cells[:3]:
        intro_md += "".join(c.get('source', [])) + "\n"
        
    report_data[rel_path] = {
        "filename": filename,
        "total_cells": len(cells),
        "md_cells": len(md_cells),
        "code_cells": len(code_cells),
        "headers": headers,
        "imports": imports,
        "datasets": list(set(datasets)),
        "functions_defined": list(set(functions_defined)),
        "detected_ml": detected_ml,
        "detected_pd_np": detected_pd_np,
        "intro_preview": intro_md[:800]
    }

out_path = os.path.join(workspace, ".agents", "explorer_survey_2", "detailed_analysis.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Detailed analysis completed for {len(report_data)} notebooks.")
