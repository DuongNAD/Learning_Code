import os
import json

workspace = r"d:\02_Learning_Knowledge\GCI_World_2026_September"

def compare_levels(folder, prefix, levels):
    print(f"\n=================== Comparison for {folder} ===================")
    for lvl in levels:
        nb_name = f"{prefix}_Level_{lvl}.ipynb"
        nb_path = os.path.join(workspace, "extracted_gci_world", "GCI World_202609", "02. Preparatory Materials", folder, nb_name)
        if not os.path.exists(nb_path):
            continue
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        cells = nb.get('cells', [])
        md_cells = [c for c in cells if c.get('cell_type') == 'markdown']
        code_cells = [c for c in cells if c.get('cell_type') == 'code']
        empty_code_cells = [c for c in code_cells if len("".join(c.get('source', [])).strip()) == 0 or '# Write your code' in "".join(c.get('source', [])) or '# Please write' in "".join(c.get('source', []))]
        
        # Read the first markdown cell to see level description
        first_md = "".join(md_cells[0].get('source', [])) if md_cells else ""
        second_md = "".join(md_cells[1].get('source', [])) if len(md_cells) > 1 else ""
        
        print(f"\nLevel {lvl} ({nb_name}):")
        print(f"  Total cells: {len(cells)}, MD: {len(md_cells)}, Code: {len(code_cells)}, Scaffolded/Empty: {len(empty_code_cells)}")
        for line in (first_md + "\n" + second_md).split('\n')[:8]:
            if line.strip():
                print(f"    {line.strip()[:100]}")

compare_levels("6. Exercise_ Regression", "Exercise_Regression", [0, 1, 2, 3, 4])
compare_levels("7. Exercise_ Classification", "Exercise_Classification", [0, 1, 2, 3])
