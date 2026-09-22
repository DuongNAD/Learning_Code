import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
workspace = r"d:\02_Learning_Knowledge\GCI_World_2026_September"

def compare_levels_to_file(folder, prefix, levels, out_file):
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write(f"=================== Comparison for {folder} ===================\n")
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
            
            out.write(f"\n--------------------------------------------------\n")
            out.write(f"Level {lvl}: {nb_name}\n")
            out.write(f"Total cells: {len(cells)} (Markdown: {len(md_cells)}, Code: {len(code_cells)})\n\n")
            
            for i, c in enumerate(cells):
                src = "".join(c.get('source', [])).strip()
                if c.get('cell_type') == 'markdown':
                    lines = [line.strip() for line in src.split('\n') if line.strip().startswith('#') or 'Level' in line or 'Goal' in line or 'Task' in line or 'Problem' in line]
                    if lines:
                        out.write(f"  Cell {i} [MD]: {'; '.join(lines[:3])}\n")
                elif c.get('cell_type') == 'code':
                    # Check if empty, scaffolded or full code
                    first_line = src.split('\n')[0] if src else "<EMPTY>"
                    out.write(f"  Cell {i} [Code, {len(src.splitlines())} lines]: {first_line[:80]}\n")

compare_levels_to_file("6. Exercise_ Regression", "Exercise_Regression", [0, 1, 2, 3, 4],
                       os.path.join(workspace, ".agents", "explorer_survey_2", "regression_levels_comparison.txt"))

compare_levels_to_file("7. Exercise_ Classification", "Exercise_Classification", [0, 1, 2, 3],
                       os.path.join(workspace, ".agents", "explorer_survey_2", "classification_levels_comparison.txt"))

print("Levels comparison written to files successfully.")
