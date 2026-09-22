import os
import json
import sys

workspace = r"d:\02_Learning_Knowledge\GCI_World_2026_September"

def analyze_notebook_deep(rel_path, out_file):
    nb_full = os.path.join(workspace, rel_path)
    with open(nb_full, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write(f"===========================================================\n")
        out.write(f"Deep Analysis: {rel_path}\n")
        out.write(f"===========================================================\n\n")
        
        cells = nb.get('cells', [])
        for idx, cell in enumerate(cells):
            ctype = cell.get('cell_type')
            src = "".join(cell.get('source', [])).strip()
            if not src:
                continue
            
            if ctype == 'markdown':
                # Check for headers or question numbers
                for line in src.split('\n'):
                    sline = line.strip()
                    if sline.startswith('#') or sline.startswith('(') or 'Question' in sline or 'Exercise' in sline or 'Chapter' in sline or 'Section' in sline:
                        out.write(f"[Cell {idx:03d} MD] {sline}\n")
            elif ctype == 'code':
                # Print code summary or key lines
                code_lines = [l for l in src.split('\n') if l.strip() and not l.strip().startswith('#')]
                first_code = code_lines[0] if code_lines else ""
                comments = [l.strip() for l in src.split('\n') if l.strip().startswith('#')]
                out.write(f"  [Cell {idx:03d} Code ({len(src.splitlines())} lines)]")
                if comments:
                    out.write(f" Comment: {comments[0][:60]}")
                if first_code:
                    out.write(f" | Code: {first_code[:80]}")
                out.write("\n")

analyze_notebook_deep("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/PreLecture_Python1&2/prelecture_notebook.ipynb",
                      os.path.join(workspace, ".agents", "explorer_survey_2", "prelecture_deep.txt"))

analyze_notebook_deep("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/PreLecture_Python1&2/prelecture_notebook_answer.ipynb",
                      os.path.join(workspace, ".agents", "explorer_survey_2", "prelecture_answer_deep.txt"))

analyze_notebook_deep("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/Session2/lec2_notebook.ipynb",
                      os.path.join(workspace, ".agents", "explorer_survey_2", "lec2_deep.txt"))

analyze_notebook_deep("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/Session2/HW1 for Session2.ipynb",
                      os.path.join(workspace, ".agents", "explorer_survey_2", "hw1_deep.txt"))

print("Deep analysis completed for all lecture/homework notebooks.")
