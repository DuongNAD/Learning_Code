import os
import re
from pathlib import Path

patterns = [
    (r"Step 2 and Step 6", "Problem A learning steps"),
    (r"KEEP CLOSED", "Problem B query answer"),
    (r"1250\s*ppm", "Problem B threshold"),
    (r"9\.26", "Problem C J(M1)"),
    (r"4\.08", "Problem C J(M2)"),
    (r"-rt\s*\+\s*(\\beta|beta)\s*t\^2", "Problem D scalar loss"),
    (r"r\s*/\s*\(?2\s*(\\beta|beta)\)?", "Problem D optimal t*"),
    (r"(\\beta|beta)\s*\\ge\s*.*r.*2T", "Problem D safety bound"),
    (r"SENIOR-2026-VN-0428", "Contest candidate ID"),
    (r"Qualification Round Formal Solutions", "Contest solution header"),
]

scan_dirs = ["docs", "latex", "README.md"]
results = []
for target in scan_dirs:
    p_target = Path(target)
    if p_target.is_file():
        files_to_scan = [p_target]
    else:
        files_to_scan = [p for p in p_target.rglob("*") if p.is_file()]

    for p in files_to_scan:
        if p.suffix in [".aux", ".log", ".out", ".toc", ".blg", ".bbl"]:
            continue
        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
            for pat, desc in patterns:
                matches = list(re.finditer(pat, content, re.IGNORECASE))
                if matches:
                    results.append((str(p), desc, len(matches)))
        except Exception as e:
            pass

print(f"{len(results)} pattern leak matches found:")
for path, desc, count in sorted(results):
    print(f"  [{count} matches] {path} -> {desc}")
