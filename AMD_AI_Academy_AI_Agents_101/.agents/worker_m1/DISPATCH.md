# Dispatch: Worker M1 (Transcript & Translation Specialist)

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT
hardcode test results, create dummy/facade implementations, or
circumvent the intended task. A teamwork_preview_auditor will independently
verify your work. Integrity violations WILL be detected and your
work WILL be rejected.

## Task Objective
You are Worker M1 (`teamwork_preview_worker`), the Speech-to-Text Transcription & Technical Translation Specialist.

Your working directory is:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m1`

Read the authoritative requirements at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md`
and Explorer 1's findings at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_1/handoff.md`

### Write Ownership
You exclusively own:
- `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md`
- Any temporary transcripts or intermediate files in `.agents/worker_m1/` or `02_Notes_Summaries/transcript_raw.*`

### Detailed Instructions:
1. Run full speech recognition on `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_1/audio.wav`:
   - Use the fast Apple Silicon Metal accelerated tool tested by Explorer 1:
     `mlx_whisper "/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_1/audio.wav" --model mlx-community/whisper-large-v3-turbo --output-dir "/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m1" --output-name "transcript_raw" --output-format all --language en`
2. Inspect the generated raw transcript (`transcript_raw.json` / `transcript_raw.srt` / `transcript_raw.txt`).
   - Verify that the transcript spans the entire lecture duration (~00:00 to ~19:28).
   - Check and polish any technical jargon that ASR might mishear (e.g., ensure "ReAct", "ROCm", "Ryzen AI", "XDNA", "NPU", "MI300X", "Vitis AI", "Browser Use", "LLMs" are accurately rendered).
3. Translate the entire lecture to technical Vietnamese (Bản dịch tiếng Việt chuẩn xác theo thuật ngữ AI):
   - Keep standard AI terms consistent: Agent / AI Agent, Reasoning (Suy luận/Lập luận), Planning (Lập kế hoạch), Tool Use (Sử dụng công cụ), Memory (Bộ nhớ: Short-term / Long-term), Perception (Tri giác/Nhận thức), State (Trạng thái).
4. Create the final authoritative transcript file at `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md`:
   - Structure into clear logical sections with headings matching video chapters/topics.
   - For every section/segment, include precise timestamps `[MM:SS - MM:SS]`, the English transcript, followed by the Vietnamese translation.
   - Include a metadata header (Video title, Speaker/Source: AMD AI Academy, Total duration: 19m 28s, Audio specs, Transcript specs).
5. Clean up any raw temporary files from `02_Notes_Summaries/` so only `transcript.md` remains in that directory.
6. Write your completion report in `handoff.md` in your working directory with word counts, duration coverage check, and sample excerpts.

## 2026-09-22T11:54:20Z
You are Worker M1 (teamwork_preview_worker), the Speech-to-Text Transcription & Technical Translation Specialist.
Your working directory is: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m1
Read your instructions in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m1/DISPATCH.md
and the authoritative request in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Execute speech-to-text on the extracted audio using mlx_whisper, verify complete duration coverage (~19m28s), format full timestamped English transcript, translate to technical Vietnamese with proper AI domain terminology, and produce /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md. Write your completion report to handoff.md in your working directory and notify via send_message when done.

