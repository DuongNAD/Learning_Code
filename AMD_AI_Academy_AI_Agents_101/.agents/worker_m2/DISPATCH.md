# Dispatch: Worker M2 (Curriculum & In-depth Architecture Specialist)

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT
hardcode test results, create dummy/facade implementations, or
circumvent the intended task. A teamwork_preview_auditor will independently
verify your work. Integrity violations WILL be detected and your
work WILL be rejected.

## Task Objective
You are Worker M2 (`teamwork_preview_worker`), the Curriculum & In-depth Architecture Specialist.

Your working directory is:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m2`

Read the authoritative requirements at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md`
and Explorer 2's comprehensive blueprint at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_2/handoff.md`
and the full transcript at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md`

### Write Ownership
You exclusively own:
- `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/01_foundations_and_agent_architecture.md`
- `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/02_core_pillars_and_design_patterns.md`
- `/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/03_amd_hardware_and_rocm_ecosystem.md`

### Detailed Instructions:
1. Author the three comprehensive, highly technical lecture modules in `02_Notes_Summaries/`:

   - Module 1: `01_foundations_and_agent_architecture.md`:
     * Paradigmatic shift: Traditional LLMs (one-shot, stateless, feed-forward text completers) vs Autonomous AI Agents (stateful, closed-loop cybernetic entities with perception, planning, tool usage, memory).
     * The Cybernetic Agency Loop: Environment -> Perception -> Internal World Model -> Action -> Environmental Change -> Feedback.
     * The motivating case from the lecture: WebUI / Browser-Use automated cooking chili workflow (interpreting UI DOM trees, interacting with web elements, dynamic error handling).
     * High-level architectural overview of the 4 Pillars.
     * Includes Diagram 1: Full 4-Pillars Cognitive Architecture Mermaid diagram.

   - Module 2: `02_core_pillars_and_design_patterns.md`:
     * Pillar 1: Perception (Multimodal ingest, vision-language grounding, Accessibility/DOM tree parsing).
     * Pillar 2: Planning & Reasoning (Chain-of-Thought, Tree-of-Thoughts, Plan-and-Solve, Backtracking & Self-Correction).
     * Pillar 3: Tool Use & Action (JSON Schema function declaration, API dispatching, sandboxed execution, error feedback trapping).
     * Pillar 4: Memory Architecture (Working memory buffer, sliding window, rolling summarization, episodic trajectory archive, vector semantic search).
     * Design Pattern A: ReAct (Reasoning + Acting) loop state machine (Yao et al., 2022).
     * Design Pattern B: Self-Reflection / Evaluator-Optimizer loop (Reflexion, Shinn et al., 2023).
     * Design Pattern C: Multi-Agent Collaboration (Hierarchical supervisor, peer swarm, specialized network).
     * Includes Diagram 2: ReAct & Self-Reflection Iterative Execution Loop Mermaid diagram.
     * Includes Diagram 3: Multi-Tier Memory Lifecycle & Compaction Mermaid diagram.

   - Module 3: `03_amd_hardware_and_rocm_ecosystem.md`:
     * The Agentic Compute Challenge: Latency compounding across iterative tool loops, KV-cache explosion during multi-turn ReAct trajectories.
     * AMD ROCm™ 6.x Software Stack: Open compute architecture, HIP portability, PyTorch ROCm backend, vLLM engine with PagedAttention and FP8 support.
     * AMD Ryzen™ AI NPU (XDNA™ 2): Spatial dataflow architecture, 50+ TOPS, <28W power envelope, edge local agent perception & guardrails on Copilot+ AI PCs.
     * AMD Radeon™ GPUs (RDNA™ 3 / RDNA™ 3.5): Workstation local agent inference (e.g. RX 7900 XTX 24GB VRAM, 960 GB/s bandwidth for running 14B-32B parameter agent backbones).
     * AMD Instinct™ MI300X/MI325X/MI350 Accelerators: CDNA™ 3 architecture, 192GB-256GB HBM3e, 5.3-6.0 TB/s memory bandwidth, 1.5TB unified node memory for hosting massive 70B/405B agent swarms without multi-node pipeline bottlenecks.
     * Optimization techniques: Quantization (FP8, AWQ, GGUF), Speculative Decoding, Vitis AI execution provider for ONNX Runtime.
     * Includes Diagram 4: Multi-Agent Collaborative Mesh mapped across AMD Hardware Acceleration Tiers Mermaid diagram.

2. Verify all Mermaid diagrams are syntactically valid and render clean ASCII/Markdown structure.
3. Cross-reference with the Python labs in `03_Materials_Code/`.
4. Write your completion report in `handoff.md` in your working directory.

## 2026-09-22T12:13:16Z
You are Worker M2 (teamwork_preview_worker), the Curriculum & In-depth Architecture Specialist.
Your working directory is: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m2
Read your instructions in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/worker_m2/DISPATCH.md
and the authoritative request in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md
and the lecture transcript in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md
and Explorer 2's blueprint in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_2/handoff.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Author the 3 comprehensive lecture modules in 02_Notes_Summaries/:
- 01_foundations_and_agent_architecture.md (includes Diagram 1: 4-Pillars Cognitive Architecture)
- 02_core_pillars_and_design_patterns.md (includes Diagram 2: ReAct/Reflection Loop, Diagram 3: Memory Lifecycle)
- 03_amd_hardware_and_rocm_ecosystem.md (includes Diagram 4: AMD Acceleration Mesh)
Ensure >=3 valid Mermaid diagrams, thorough explanations, mathematical formulation where appropriate, and full coverage of the AMD ecosystem. Write your completion report in handoff.md and notify via send_message when done.
