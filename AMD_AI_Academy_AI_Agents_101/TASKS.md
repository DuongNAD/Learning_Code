---
document_type: project_task_board
project: AMD AI Academy - AI Agents 101
version: 2.0.0
last_updated: 2026-09-23
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
focus_board: file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md
central_tasks: file:///D:/02_Learning_Knowledge/TASKS.md
rfc2119_compliance: strict
emoji_policy: none
---

# AMD AI Academy - AI Agents 101 - Task Board

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
Active Focus Board: [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md)
System Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md)
Project Overview: [README.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/README.md)
Notes & Summaries: [02_Notes_Summaries](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries)
Materials & Code: [03_Materials_Code](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code)

## Task Maintenance Rules (RFC 2119)
- Standardized Schema: All tasks MUST follow the tag format `- [ ] [Deadline: YYYY-MM-DD HH:mm] [Priority: P0/P1/P2] Description`.
- Task Preservation: AI agents MUST NEVER delete existing tasks.
- Status Transitions: Task status MUST ONLY be transitioned between `[ ]` and `[x]`, and status change to completed MUST occur ONLY IF verification criteria are met.
- Task Placement: Newly identified micro-tasks MUST be appended to the end of the appropriate section.
- Local Authority: Local operations within this project directory MUST update this file directly.

## 1. Curriculum & Notes Review
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Tổng hợp các khái niệm cốt lõi: [01_AI_Agents_101_Core_Concepts.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/01_AI_Agents_101_Core_Concepts.md).
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Hệ thống hóa nền tảng và kiến trúc Agent: [01_foundations_and_agent_architecture.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/01_foundations_and_agent_architecture.md).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Phân tích Core Pillars và Design Patterns (Planning, ReAct, Memory, Multi-agent): [02_core_pillars_and_design_patterns.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/02_core_pillars_and_design_patterns.md).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Đọc và tổng hợp kiến trúc tăng tốc phần cứng AMD Instinct và ngăn xếp ROCm: [03_amd_hardware_and_rocm_ecosystem.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/03_amd_hardware_and_rocm_ecosystem.md).
- [ ] [Deadline: 2026-09-29 23:59] [Priority: P2] Hoàn thành và tự đánh giá bài trắc nghiệm chuyên sâu trong [quiz_and_assessment.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/quiz_and_assessment.md).
- [ ] [Deadline: 2026-09-30 23:59] [Priority: P2] Rà soát transcript bài giảng gốc trong [transcript.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md).
- [x] [Deadline: 2026-09-26 23:59] [Priority: P1] Tổng hợp kiến trúc RAG nâng cao, kỹ thuật Semantic Chunking v2.0 và pipeline LangChain trong [04_rag_systems_and_semantic_chunking_v2.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/04_rag_systems_and_semantic_chunking_v2.md).

## 2. Tool-Use Labs & Core Agent Implementations
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Xây dựng mẫu Pure ReAct Agent từ scratch: [01_pure_react_agent.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/01_pure_react_agent.py).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Xây dựng mẫu Tool Calling Agent với JSON schema: [02_tool_calling_agent.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/02_tool_calling_agent.py).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Xây dựng Memory & Conversation State Agent: [03_memory_state_agent.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/03_memory_state_agent.py).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Xây dựng StateGraph Multi-agent với LangGraph: [04_framework_agent_langgraph.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/04_framework_agent_langgraph.py).
- [ ] [Deadline: 2026-09-30 23:59] [Priority: P1] Chạy bộ kiểm thử xác thực labs [verify_labs.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/verify_labs.py) sau khi thiết lập môi trường Python 3.11+.
- [ ] [Deadline: 2026-10-01 23:59] [Priority: P2] Tích hợp công cụ tính toán toán học và tìm kiếm dữ liệu tùy biến vào vòng lặp tool execution của ReAct Agent.

## 3. Advanced Agent Pipelines & Production Patterns
- [ ] [Deadline: 2026-10-03 23:59] [Priority: P2] Thiết kế Human-in-the-loop (HITL) checkpointing cho tác vụ nhạy cảm (ghi đè file, gọi API bên ngoài).
- [ ] [Deadline: 2026-10-05 23:59] [Priority: P2] Triển khai bộ nhớ dài hạn (Long-term Episodic Memory) sử dụng Vector Database nhúng cục bộ.
- [ ] [Deadline: 2026-10-07 23:59] [Priority: P2] Xây dựng mô hình Supervisor-Worker điều phối song song 3 sub-agents giải quyết bài toán phân tích mã nguồn.
- [ ] [Deadline: 2026-10-09 23:59] [Priority: P2] Đánh giá độ trễ và thông lượng suy luận mô hình Agentic trên môi trường tăng tốc ROCm/vLLM.

## 4. Roadmap v2 Milestones ([ROADMAP.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/04_Roadmaps/ROADMAP.md))
- [ ] [Deadline: 2026-10-17 23:59] [Priority: P2] M0: chạy verify_labs.py với PYTHONUTF8=1 đạt 4/4 PASS, tóm tắt 12 phần video, tạo Sổ lỗi.
- [ ] [Deadline: 2026-10-31 23:59] [Priority: P2] M1: my_react.py viết từ file trống qua 4 assert (có max_steps, tool lạ trả lỗi có cấu trúc).
- [ ] [Deadline: 2026-11-14 23:59] [Priority: P2] M2: my_tools.py, registry kiểm schema qua 8 assert.
- [ ] [Deadline: 2026-11-21 23:59] [Priority: P2] M3: context_manager.py qua test 30 bước dưới ngân sách token.
- [ ] [Deadline: 2026-12-08 23:59] [Priority: P2] M4: MCP time server qua MCP Inspector (JSON tools/list và 2 lời gọi).
- [ ] [Deadline: 2026-12-19 23:59] [Priority: P2] M5: endpoint Ollama qwen3 trả tool_calls; bảng tính TPS và KV cache có nguồn.
- [ ] [Deadline: 2026-12-29 23:59] [Priority: P2] M6: hoàn thành notebook chính thức (bản Ollama) kèm trace Vancouver và thử thách weather MCP.
- [ ] [Deadline: 2027-01-14 23:59] [Priority: P2] M7 + M9: mini_graph.py, guardrails và bộ eval 10 ca (2 ca prompt injection).
- [ ] [Deadline: 2027-01-23 23:59] [Priority: P2] Dự án tổng hợp: trợ lý hạn chót qua MCP server chỉ đọc, eval đạt từ 10/12.
