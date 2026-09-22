#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Independent verification script for 02_Notes_Summaries/transcript.md
"""

import os
import re

TRANSCRIPT_PATH = "/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md"

def test_transcript():
    assert os.path.exists(TRANSCRIPT_PATH), f"File missing: {TRANSCRIPT_PATH}"
    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Size and line counts
    lines = text.splitlines()
    assert len(lines) >= 600, f"Expected >= 600 lines, got {len(lines)}"
    assert len(text) >= 40000, f"Expected >= 40,000 chars, got {len(text)}"

    # 2. Metadata checks
    assert "Mahdi Ghodsi" in text, "Missing speaker name: Mahdi Ghodsi"
    assert "AMD AI Academy" in text, "Missing provider: AMD AI Academy"
    assert "19 phút 28.20 giây" in text or "19:28" in text, "Missing full duration metadata"
    assert "mlx-whisper" in text, "Missing ASR model metadata"

    # 3. Section checks
    for sec_num in range(1, 14):
        pattern = rf"### Phần {sec_num}:"
        assert re.search(pattern, text), f"Missing section header: Phần {sec_num}"

    # 4. Critical technical terminology checks
    assert "ReAct" in text, "Missing ReAct terminology"
    assert "PydanticAI" in text, "Missing PydanticAI terminology"
    assert "Model Context Protocol" in text, "Missing Model Context Protocol"
    assert "vLLM" in text, "Missing vLLM"
    assert "SGLang" in text, "Missing SGLang"
    assert "Qwen3" in text, "Missing Qwen3"
    assert "DeepSeek" in text, "Missing DeepSeek"
    assert "ROCm" in text, "Missing ROCm"
    assert "MI300X" in text, "Missing MI300X"
    assert "Browser Use" in text, "Missing Browser Use"

    # 5. Timestamp format check
    timestamps = re.findall(r"`\[(\d{2}:\d{2})\s*-\s*(\d{2}:\d{2})\]`", text)
    assert len(timestamps) >= 120, f"Expected >= 120 timestamped segments, got {len(timestamps)}"
    first_start = timestamps[0][0]
    last_end = timestamps[-1][1]
    assert first_start == "00:00", f"Expected first segment start 00:00, got {first_start}"
    assert last_end == "19:28", f"Expected last segment end 19:28, got {last_end}"

    # 6. Absence of Whisper hallucination loops
    assert "Let's go to the next video." not in text, "Found uncleaned Whisper hallucination loop!"

    print("ALL 6 TRANSCRIPT VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print(f"- Total lines: {len(lines)}")
    print(f"- Total characters: {len(text)}")
    print(f"- Total timestamp segments verified: {len(timestamps)}")
    print(f"- Duration coverage: [{first_start} -> {last_end}] (100% complete)")

if __name__ == "__main__":
    test_transcript()
