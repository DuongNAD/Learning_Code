import json

with open("extracted_gci_world/GCI World_202609/03. Lecture Materials & Homework/PreLecture_Python1&2/prelecture_notebook_answer.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb['cells']
print("--- Cell 28 (3-4 text) ---")
print("".join(cells[28]['source']))
print("--- Cell 29 (3-4 code) ---")
print("".join(cells[29]['source']))
print("--- Cell 38 (4-3 text) ---")
print("".join(cells[38]['source']))
print("--- Cell 40 (4-3 code) ---")
print("".join(cells[40]['source']))
