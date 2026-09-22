import re

with open(".agents/explorer_survey_2/prelecture_cells.txt", "r", encoding="utf-8") as f:
    text = f.read()

cells = text.split("--- Cell ")
print(f"Total cells in prelecture: {len(cells)}")

for c in cells[1:]:
    header_match = re.search(r"^(#+ .*)$", c, re.MULTILINE)
    if header_match:
        cell_id = c.split(" ")[0]
        ctype = c.split("[")[1].split("]")[0] if "[" in c else ""
        print(f"Cell {cell_id} [{ctype}]: {header_match.group(1)}")
