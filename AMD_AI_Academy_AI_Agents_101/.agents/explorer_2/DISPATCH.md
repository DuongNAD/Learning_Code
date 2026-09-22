# Dispatch: Explorer 2 (Curriculum & Knowledge Architecture Specialist)

## Task Objective
You are Explorer 2 (`teamwork_preview_explorer`), the Curriculum & Knowledge Architecture Specialist.

Your working directory is:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_2`

Read the authoritative requirements at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md`
and project layout at:
`/Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/orchestrator/PROJECT.md`

### Your Tasks:
1. Examine the course topic "AMD AI Academy: AI Agents 101" and map out the complete, deep educational curriculum in `02_Notes_Summaries/`.
2. Break down the theoretical foundation:
   - Defining AI Agents vs. Traditional Static LLMs (Autonomy, loop execution, environment perception, feedback reaction).
   - The 4 Core Architectural Pillars:
     * 1. Perception (Multimodal inputs, sensors, API ingest, prompt grounding).
     * 2. Planning & Reasoning (Task decomposition, Tree-of-Thoughts, Plan-and-Solve, Self-Reflection/Self-Correction).
     * 3. Tool Use & Action (Function calling, JSON schema tool definitions, API invocation, error recovery).
     * 4. Memory Architecture (Short-term context windows, Working memory buffers, Long-term episodic/semantic vector stores, Memory retrieval/pruning).
   - Agent Design Patterns:
     * ReAct Loop (Reasoning + Acting + Observing).
     * Reflection / Self-Critique loops.
     * Multi-Agent Collaboration (Hierarchical, Peer-to-Peer, Crew/Swarm architectures).
   - AMD Hardware Acceleration Ecosystem:
     * AMD ROCm (Radeon Open Compute) software stack, HIP, PyTorch/vLLM on ROCm.
     * AMD Ryzen AI NPU (XDNA architecture, low-latency local agent execution on AI PCs).
     * AMD Radeon GPUs (RDNA 3 / RDNA 3.5 for local workstation inference).
     * AMD Instinct MI300X/MI325X/MI350 GPUs for datacenter agentic swarm serving.
     * ONNX Runtime, Vitis AI Execution Provider, and quantized local deployment (GGUF, AWQ, FP8).
3. Design >=3 detailed, valid Mermaid diagrams representing:
   - Diagram 1: Overall 4-Pillars Agent Architecture (Perception -> Planning/Reasoning <-> Memory -> Action/Tools -> Environment feedback).
   - Diagram 2: ReAct & Self-Reflection Iteration Loop with tool execution.
   - Diagram 3: Multi-Agent Swarm / Collaboration Pattern (e.g. Orchestrator-Worker or Specialist Network) backed by AMD Hardware Acceleration tiers.
4. Design the quiz structure (15-20 questions across Bloom taxonomy levels) for `02_Notes_Summaries/quiz_and_assessment.md`.
5. Write your comprehensive analysis report in `handoff.md` in your working directory.

## 2026-09-22T11:45:00Z

<USER_REQUEST>
You are Explorer 2 (teamwork_preview_explorer), the Curriculum & Knowledge Architecture Specialist.
Your working directory is: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_2
Read your instructions in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/explorer_2/DISPATCH.md
and the authoritative request in: /Volumes/KINGSTON/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/.agents/ORIGINAL_REQUEST.md

Your tasks:
1. Break down the full course curriculum for "AMD AI Academy: AI Agents 101" to be authored in 02_Notes_Summaries/.
2. Detail the 4 core pillars (Perception, Planning & Reasoning, Tool Use & Action, Memory Short/Long-term), agent design patterns (ReAct, Reflection, Multi-Agent), and the AMD Hardware Acceleration ecosystem (AMD ROCm, Ryzen AI NPU XDNA, Radeon GPUs, Instinct MI300X/MI325X, inference optimization).
3. Design >=3 full, valid Mermaid architecture diagrams.
4. Outline the 15-20 question quiz structure for quiz_and_assessment.md.
5. Record your full analysis and curriculum blueprint in handoff.md in your working directory. Send a message to your parent when done.
</USER_REQUEST>
