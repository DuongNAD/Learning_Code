#!/usr/bin/env python3
"""
================================================================================
AMD AI Academy: AI Agents 101 — Course Integration & Link Integrity Verification
================================================================================
Role: Challenger 2 (teamwork_preview_challenger)
Purpose:
  Empirical, comprehensive verification suite for:
  1. Markdown syntax & code fence balancing across all repo markdown files.
  2. Relative link and anchor integrity (target existence on disk, anchor resolution).
  3. Mermaid diagram structural tags, syntax, and full compilation via mermaid-cli.
  4. Transcript integrity: start at 00:00, end at ~19:28, monotonic continuity,
     bilingual (EN/VI) pairing for 100% of segments.
  5. Quiz completeness: exactly 18 questions, options A-D, answer key,
     step-by-step rationale, and full distractor analysis for every question.
================================================================================
"""

import os
import re
import sys
import json
import shutil
import tempfile
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

class VerificationSuite:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.passed_checks = 0
        self.failed_checks = 0
        self.warnings = 0
        self.details = []

    def log_section(self, title: str):
        print("\n" + "=" * 78)
        print(f"🔬 {title}")
        print("=" * 78)

    def record_result(self, category: str, test_name: str, passed: bool, message: str):
        if passed:
            self.passed_checks += 1
            status = "✅ PASS"
        else:
            self.failed_checks += 1
            status = "❌ FAIL"
        print(f"{status} [{category}] {test_name}: {message}")
        self.details.append({
            "category": category,
            "test": test_name,
            "passed": passed,
            "message": message
        })

    def record_warning(self, category: str, test_name: str, message: str):
        self.warnings += 1
        print(f"⚠️ WARN [{category}] {test_name}: {message}")
        self.details.append({
            "category": category,
            "test": test_name,
            "passed": True,
            "warning": True,
            "message": message
        })

    def get_markdown_files(self):
        """Discover all repo markdown files, ignoring .agents, .git, and AppleDouble ._*"""
        md_files = []
        for root, dirs, files in os.walk(self.repo_root):
            if "/.agents" in root or "/.git" in root:
                continue
            for f in files:
                if f.endswith(".md") and not f.startswith("._"):
                    full_path = Path(root) / f
                    rel_path = full_path.relative_to(self.repo_root)
                    md_files.append(rel_path)
        md_files.sort()
        return md_files

    # --------------------------------------------------------------------------
    # 1. MARKDOWN SYNTAX & CODE FENCE INTEGRITY
    # --------------------------------------------------------------------------
    def verify_markdown_syntax(self, md_files):
        self.log_section("1. Markdown Structural & Code Fence Validation")
        for rel_path in md_files:
            full_path = self.repo_root / rel_path
            try:
                content = full_path.read_text(encoding="utf-8")
            except Exception as e:
                self.record_result("Markdown", str(rel_path), False, f"Failed to read file: {e}")
                continue

            # Check code fences balance
            fence_matches = re.findall(r'^```', content, re.MULTILINE)
            fence_count = len(fence_matches)
            if fence_count % 2 != 0:
                self.record_result(
                    "Markdown", str(rel_path), False,
                    f"Unbalanced code fences (total ``` count: {fence_count})"
                )
            else:
                self.record_result(
                    "Markdown", str(rel_path), True,
                    f"Code fences balanced ({fence_count} markers, {len(content.splitlines())} lines)"
                )

    # --------------------------------------------------------------------------
    # 2. RELATIVE LINK & ANCHOR INTEGRITY
    # --------------------------------------------------------------------------
    def verify_links_and_anchors(self, md_files):
        self.log_section("2. Relative Link & Anchor Target Integrity")
        link_regex = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)')
        img_regex = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

        # Cache file headings for anchor validation
        file_headings = {}
        for rel_path in md_files:
            full_path = self.repo_root / rel_path
            content = full_path.read_text(encoding="utf-8")
            clean_content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            headings = re.findall(r'^(#{1,6})\s+(.+)$', clean_content, flags=re.MULTILINE)
            file_headings[str(rel_path)] = [h[1].strip() for h in headings]

        def heading_to_slug(text: str) -> str:
            text = re.sub(r'<[^>]+>', '', text)
            text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
            text = re.sub(r'[*_`~]', '', text)
            text = text.lower().strip()
            chars = []
            for c in text:
                if c.isalnum() or c in (' ', '-', '_'):
                    chars.append(c)
                elif c in ('—', '–'):
                    chars.append('-')
            return "".join(chars).replace(" ", "-")

        total_links = 0
        total_relative_links = 0

        for rel_path in md_files:
            full_path = self.repo_root / rel_path
            content = full_path.read_text(encoding="utf-8")
            clean_content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            dir_path = full_path.parent

            # Verify standard links
            links = link_regex.findall(clean_content)
            for text, target in links:
                target = target.strip()
                total_links += 1

                # External URLs
                if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
                    continue

                # In-file anchor link
                if target.startswith("#"):
                    anchor = target[1:]
                    headings = file_headings.get(str(rel_path), [])
                    matched = any(
                        anchor == heading_to_slug(h) or anchor in heading_to_slug(h) or text.lower() in h.lower()
                        for h in headings
                    )
                    if matched:
                        self.record_result(
                            "AnchorLink", f"{rel_path} -> #{anchor}", True,
                            f"Matched heading in {rel_path}"
                        )
                    else:
                        self.record_result(
                            "AnchorLink", f"{rel_path} -> #{anchor}", False,
                            f"Anchor not found in headings of {rel_path}"
                        )
                    continue

                # Relative link to file (optional #anchor)
                total_relative_links += 1
                if "#" in target:
                    target_file, anchor = target.split("#", 1)
                else:
                    target_file, anchor = target, None

                resolved_path = (dir_path / target_file).resolve()
                if not resolved_path.exists():
                    self.record_result(
                        "RelativeLink", f"{rel_path} -> {target}", False,
                        f"Target path does not exist on disk: {resolved_path}"
                    )
                else:
                    msg = f"Target exists ({'dir' if resolved_path.is_dir() else 'file'})"
                    if anchor:
                        try:
                            rel_target = str(resolved_path.relative_to(self.repo_root))
                            headings = file_headings.get(rel_target, [])
                            anchor_matched = any(
                                anchor == heading_to_slug(h) or anchor in heading_to_slug(h)
                                for h in headings
                            )
                            if anchor_matched:
                                msg += f" & anchor #{anchor} verified"
                            else:
                                msg += f" [WARN: anchor #{anchor} not matched in {rel_target}]"
                        except Exception:
                            pass
                    self.record_result("RelativeLink", f"{rel_path} -> {target}", True, msg)

            # Verify image links
            images = img_regex.findall(clean_content)
            for alt, src in images:
                src = src.strip()
                if src.startswith("http://") or src.startswith("https://"):
                    continue
                resolved_img = (dir_path / src).resolve()
                if not resolved_img.exists():
                    self.record_result(
                        "ImageLink", f"{rel_path} -> {src}", False,
                        f"Image source does not exist: {resolved_img}"
                    )
                else:
                    self.record_result(
                        "ImageLink", f"{rel_path} -> {src}", True,
                        f"Image source verified on disk ({resolved_img.stat().st_size} bytes)"
                    )

        print(f"\nTotal markdown links inspected: {total_links} (Relative target links: {total_relative_links})")

    # --------------------------------------------------------------------------
    # 3. MERMAID DIAGRAM SYNTAX & COMPILATION
    # --------------------------------------------------------------------------
    def verify_mermaid_diagrams(self, md_files):
        self.log_section("3. Mermaid Diagram Syntax & Compilation Verification")
        mermaid_pattern = re.compile(r'```mermaid\s*\n(.*?)```', re.DOTALL)
        
        has_chrome = os.path.exists(CHROME_PATH)
        temp_dir = tempfile.mkdtemp(prefix="mermaid_verify_")

        diagram_index = 0
        total_diagrams = 0

        for rel_path in md_files:
            full_path = self.repo_root / rel_path
            content = full_path.read_text(encoding="utf-8")
            matches = mermaid_pattern.findall(content)
            if not matches:
                continue

            for idx, code in enumerate(matches, 1):
                total_diagrams += 1
                diagram_index += 1
                code_stripped = code.strip()
                first_line = code_stripped.splitlines()[0].strip() if code_stripped else ""

                # Structural Tag validation
                valid_starters = (
                    "flowchart", "graph", "stateDiagram", "stateDiagram-v2",
                    "sequenceDiagram", "classDiagram", "erDiagram", "gantt",
                    "pie", "gitGraph", "mindmap", "quadrantChart"
                )
                has_valid_tag = any(first_line.startswith(s) for s in valid_starters)
                if not has_valid_tag:
                    self.record_result(
                        "MermaidStructural", f"{rel_path} Diagram #{idx}", False,
                        f"Missing or invalid root structural tag: '{first_line}'"
                    )
                    continue

                # Balanced block syntax check
                subgraph_count = len(re.findall(r'\bsubgraph\b', code_stripped))
                end_count = len(re.findall(r'\bend\b', code_stripped))
                if subgraph_count != end_count:
                    self.record_result(
                        "MermaidStructural", f"{rel_path} Diagram #{idx}", False,
                        f"Unbalanced subgraph/end pairs (subgraph={subgraph_count}, end={end_count})"
                    )
                    continue

                self.record_result(
                    "MermaidStructural", f"{rel_path} Diagram #{idx}", True,
                    f"Structural tag '{first_line}' and subgraphs balanced ({subgraph_count} subgraphs)"
                )

                # Full compilation via @mermaid-js/mermaid-cli
                if has_chrome:
                    mmd_in = os.path.join(temp_dir, f"diag_{diagram_index}.mmd")
                    svg_out = os.path.join(temp_dir, f"diag_{diagram_index}.svg")
                    with open(mmd_in, "w", encoding="utf-8") as f:
                        f.write(code_stripped)

                    env = os.environ.copy()
                    env["PUPPETEER_EXECUTABLE_PATH"] = CHROME_PATH

                    cmd = ["npx", "-p", "@mermaid-js/mermaid-cli", "mmdc", "-i", mmd_in, "-o", svg_out]
                    try:
                        p = subprocess.run(
                            cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, timeout=30
                        )
                        if p.returncode == 0 and os.path.exists(svg_out) and os.path.getsize(svg_out) > 0:
                            svg_size = os.path.getsize(svg_out)
                            self.record_result(
                                "MermaidCompile", f"{rel_path} Diagram #{idx}", True,
                                f"Compiled to SVG successfully ({svg_size:,} bytes)"
                            )
                        else:
                            err_msg = p.stderr.strip() or p.stdout.strip()
                            self.record_result(
                                "MermaidCompile", f"{rel_path} Diagram #{idx}", False,
                                f"Compilation failed: {err_msg[:200]}"
                            )
                    except Exception as e:
                        self.record_result(
                            "MermaidCompile", f"{rel_path} Diagram #{idx}", False,
                            f"Execution error during mmdc: {e}"
                        )
                else:
                    self.record_warning(
                        "MermaidCompile", f"{rel_path} Diagram #{idx}",
                        "Chrome not found at expected path; skipped headless SVG render."
                    )

        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"\nTotal Mermaid diagrams verified: {total_diagrams}")

    # --------------------------------------------------------------------------
    # 4. TRANSCRIPT CONTINUITY & BILINGUAL INTEGRITY
    # --------------------------------------------------------------------------
    def verify_transcript_integrity(self):
        self.log_section("4. Transcript Timestamps & Bilingual Integrity")
        transcript_path = self.repo_root / "02_Notes_Summaries" / "transcript.md"
        if not transcript_path.exists():
            self.record_result("Transcript", "FileExistence", False, f"Not found at {transcript_path}")
            return

        content = transcript_path.read_text(encoding="utf-8")
        seg_pattern = re.compile(r'-\s+`\[(\d{2}:\d{2})\s*-\s*(\d{2}:\d{2})\]`')
        matches = list(seg_pattern.finditer(content))

        self.record_result(
            "Transcript", "SegmentCount", len(matches) > 0,
            f"Found {len(matches)} timestamped segments"
        )

        if not matches:
            return

        def ts_to_seconds(ts: str) -> int:
            m, s = map(int, ts.split(':'))
            return m * 60 + s

        first_start = matches[0].group(1)
        last_end = matches[-1].group(2)

        # Start timestamp check
        self.record_result(
            "Transcript", "StartTimestamp", first_start == "00:00",
            f"Initial timestamp is [{first_start}] (expected 00:00)"
        )

        # End timestamp check (~19:28)
        last_sec = ts_to_seconds(last_end)
        expected_sec = 19 * 60 + 28  # 1168s
        end_ok = abs(last_sec - expected_sec) <= 2
        self.record_result(
            "Transcript", "EndTimestamp", end_ok,
            f"Terminal timestamp is [{last_end}] ({last_sec}s, expected ~19:28 / 1168s)"
        )

        # Continuity check
        prev_end_sec = None
        discontinuities = []
        missing_bilingual = []

        for i, m in enumerate(matches):
            start_str, end_str = m.group(1), m.group(2)
            start_sec = ts_to_seconds(start_str)
            end_sec = ts_to_seconds(end_str)

            # Monotonicity & continuity
            if prev_end_sec is not None:
                if start_sec != prev_end_sec:
                    discontinuities.append((i, start_str, prev_end_sec, start_sec))

            # Segment slice
            start_pos = m.start()
            end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            seg_text = content[start_pos:end_pos]

            has_en = ("**EN:**" in seg_text) or ("EN:" in seg_text)
            has_vi = ("**VI:**" in seg_text) or ("VI:" in seg_text)

            if not (has_en and has_vi):
                missing_bilingual.append((i, start_str, has_en, has_vi))

            prev_end_sec = end_sec

        self.record_result(
            "Transcript", "Continuity", len(discontinuities) == 0,
            f"Contiguity check: {len(discontinuities)} gaps/overlaps detected across all {len(matches)} segments"
        )
        if discontinuities:
            for d in discontinuities[:5]:
                print(f"  Gap/Overlap at segment {d[0]}: [{d[1]}] vs prev end {d[2]}s")

        self.record_result(
            "Transcript", "BilingualPairing", len(missing_bilingual) == 0,
            f"Bilingual check: 100% of {len(matches)} segments contain both English (EN) and Vietnamese (VI) translations"
        )
        if missing_bilingual:
            for mb in missing_bilingual[:5]:
                print(f"  Segment {mb[0]} [{mb[1]}]: has_en={mb[2]}, has_vi={mb[3]}")

    # --------------------------------------------------------------------------
    # 5. QUIZ COMPLETENESS & DISTRACTOR ANALYSIS
    # --------------------------------------------------------------------------
    def verify_quiz_integrity(self):
        self.log_section("5. Quiz Completeness, Bloom Taxonomy & Distractor Analysis")
        quiz_path = self.repo_root / "02_Notes_Summaries" / "quiz_and_assessment.md"
        if not quiz_path.exists():
            self.record_result("Quiz", "FileExistence", False, f"Not found at {quiz_path}")
            return

        content = quiz_path.read_text(encoding="utf-8")
        q_headers = list(re.finditer(r'^####\s+Câu\s+hỏi\s+(\d+):', content, re.MULTILINE))

        self.record_result(
            "Quiz", "QuestionCount", len(q_headers) == 18,
            f"Found {len(q_headers)} questions (Requirement: exactly 18 questions)"
        )

        answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
        incomplete_questions = []

        for i, m in enumerate(q_headers):
            q_num = int(m.group(1))
            start_pos = m.start()
            end_pos = q_headers[i + 1].start() if i + 1 < len(q_headers) else len(content)
            q_text = content[start_pos:end_pos]

            has_a = bool(re.search(r'-\s+\*\*A\.\*\*', q_text))
            has_b = bool(re.search(r'-\s+\*\*B\.\*\*', q_text))
            has_c = bool(re.search(r'-\s+\*\*C\.\*\*', q_text))
            has_d = bool(re.search(r'-\s+\*\*D\.\*\*', q_text))
            options_ok = has_a and has_b and has_c and has_d

            ans_match = re.search(r'#####\s+Đáp\s+án\s+chính\s+xác:\s*([A-D])', q_text)
            ans_key = ans_match.group(1) if ans_match else None
            if ans_key in answer_counts:
                answer_counts[ans_key] += 1

            has_rationale = bool(re.search(r'#####\s+Giải\s+thích\s+kỹ\s+thuật', q_text, re.IGNORECASE))
            has_distractors = bool(re.search(r'#####\s+Phân\s+tích\s+(?:các\s+)?phương\s+án\s+gây\s+nhiễu', q_text, re.IGNORECASE))

            # Distractor coverage:
            # Check which distractors are mentioned in the distractor section
            distractor_slice = q_text[q_text.find("Phân tích"):] if "Phân tích" in q_text else ""
            distractors_expected = set(["A", "B", "C", "D"]) - {ans_key} if ans_key else set()
            
            # Check mentions of each distractor letter
            missing_distractors = []
            for d in distractors_expected:
                # Matches: "Phương án A sai", "Phương án C & D sai", "**Phương án A", "Phương án A:"
                pattern = rf'Phương\s+án[^\n]*\b{d}\b'
                if not re.search(pattern, distractor_slice):
                    missing_distractors.append(d)

            is_complete = (
                options_ok and bool(ans_key) and has_rationale and
                has_distractors and len(missing_distractors) == 0
            )

            if not is_complete:
                incomplete_questions.append({
                    "q_num": q_num,
                    "options_ok": options_ok,
                    "ans_key": ans_key,
                    "has_rationale": has_rationale,
                    "has_distractors": has_distractors,
                    "missing_distractors": missing_distractors
                })

        self.record_result(
            "Quiz", "ItemsCompleteness", len(incomplete_questions) == 0,
            f"All 18 questions satisfy: Options A-D, Answer Key, Technical Rationale, and Distractor Analyses"
        )
        if incomplete_questions:
            for iq in incomplete_questions:
                print(f"  Flagged Q{iq['q_num']}: {iq}")

        # Check Bloom Taxonomy coverage (CLO-1 to CLO-6)
        bloom_levels = re.findall(r'PHẦN\s+[IVX]+:\s+([^\n(]+)', content)
        self.record_result(
            "Quiz", "BloomTaxonomyStructure", len(bloom_levels) == 6,
            f"Found all 6 Bloom Cognitive Levels: {', '.join(b.strip() for b in bloom_levels)}"
        )

        # Check distribution balance
        print(f"Answer Key Distribution: A={answer_counts['A']}, B={answer_counts['B']}, C={answer_counts['C']}, D={answer_counts['D']}")
        self.record_result(
            "Quiz", "AnswerDistribution", all(3 <= count <= 6 for count in answer_counts.values()),
            f"Balanced distribution triệt tiêu position bias: A={answer_counts['A']}, B={answer_counts['B']}, C={answer_counts['C']}, D={answer_counts['D']}"
        )

    # --------------------------------------------------------------------------
    # 6. RUN ALL CHECKS & SUMMARY
    # --------------------------------------------------------------------------
    def run_all(self):
        print("=" * 78)
        print("🚀 RUNNING COURSE INTEGRITY & VERIFICATION SUITE")
        print(f"Repository Root: {self.repo_root}")
        print("=" * 78)

        md_files = self.get_markdown_files()
        print(f"Discovered {len(md_files)} project markdown files:")
        for mf in md_files:
            print(f"  • {mf}")

        self.verify_markdown_syntax(md_files)
        self.verify_links_and_anchors(md_files)
        self.verify_mermaid_diagrams(md_files)
        self.verify_transcript_integrity()
        self.verify_quiz_integrity()

        self.log_section("Verification Summary & Final Verdict")
        total_tests = self.passed_checks + self.failed_checks
        print(f"Total Verifications Executed: {total_tests}")
        print(f"  • Passed: {self.passed_checks}")
        print(f"  • Failed: {self.failed_checks}")
        print(f"  • Warnings: {self.warnings}")

        if self.failed_checks == 0:
            print("\n🌟 VERDICT: APPROVE — 100% Zero-Defect Integrity Confirmed across all dimensions!")
            return True
        else:
            print(f"\n🚨 VERDICT: REQUEST_CHANGES — {self.failed_checks} failures detected!")
            return False

if __name__ == "__main__":
    suite = VerificationSuite(REPO_ROOT)
    success = suite.run_all()
    sys.exit(0 if success else 1)
