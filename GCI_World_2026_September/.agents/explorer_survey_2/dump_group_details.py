import os
import json
import glob

workspace = r"d:\02_Learning_Knowledge\GCI_World_2026_September"

def dump_notebook(nb_rel_path, out_txt):
    nb_full_path = os.path.join(workspace, nb_rel_path)
    with open(nb_full_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    cells = nb.get('cells', [])
    with open(out_txt, 'w', encoding='utf-8') as out:
        out.write(f"# Notebook: {nb_rel_path}\n\n")
        for i, c in enumerate(cells):
            ctype = c.get('cell_type')
            src = "".join(c.get('source', []))
            out.write(f"--- Cell {i} [{ctype}] ---\n")
            out.write(src.strip() + "\n\n")

# Dump summaries for key notebooks
dump_notebook("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/PreLecture_Python1&2/prelecture_notebook.ipynb",
              os.path.join(workspace, ".agents", "explorer_survey_2", "prelecture_cells.txt"))

dump_notebook("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/Session2/lec2_notebook.ipynb",
              os.path.join(workspace, ".agents", "explorer_survey_2", "lec2_cells.txt"))

dump_notebook("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/Session2/HW1 for Session2.ipynb",
              os.path.join(workspace, ".agents", "explorer_survey_2", "hw1_cells.txt"))

dump_notebook("extracted_gci_world/GCI World_202609/02. Preparatory Materials/6. Exercise_ Regression/Exercise_Regression_Level_0.ipynb",
              os.path.join(workspace, ".agents", "explorer_survey_2", "regression_lv0_cells.txt"))

dump_notebook("extracted_gci_world/GCI World_202609/02. Preparatory Materials/7. Exercise_ Classification/Exercise_Classification_Level_0.ipynb",
              os.path.join(workspace, ".agents", "explorer_survey_2", "classification_lv0_cells.txt"))

print("Dump completed for key notebooks.")
