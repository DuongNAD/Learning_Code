# 🗺️ Lộ trình Tinh thông AI Agents (Từ 101 đến Master)

Lộ trình học tập thực chiến giúp xây dựng các hệ thống AI Agent từ cơ bản đến quy mô doanh nghiệp.

---

## Giai đoạn 1: Nền tảng (Foundations)
- [x] **Hiểu bản chất:** Khái niệm AI Agent, vòng lặp ReAct (*Reason + Act*).
- [ ] **Prompt Engineering cho Agents:** System prompts, XML structuring, Few-shot demonstration.
- [ ] **Function Calling & Tool Calling:** Cách LLM xuất JSON có cấu trúc để gọi hàm trong Python.
- [ ] **Structured Outputs:** Pydantic validation, Instructor library.

## Giai đoạn 2: Single-Agent Systems
- [ ] **ReAct Loop thủ công:** Tự viết vòng lặp Agent bằng Python thuần mà không dùng framework.
- [ ] **Memory Management:** Quản lý hội thoại, Sliding Window, Semantic Search trên Vector DB.
- [ ] **Frameworks cốt lõi:**
  - `LangChain` / `LangGraph` (Graph-based deterministic control).
  - `LlamaIndex` (Data agents & Agentic RAG).

## Giai đoạn 3: Multi-Agent Collaboration
- [ ] **Kiến trúc Multi-Agent:**
  - **Supervisor Pattern:** 1 Agent điều phối quản lý các Agent chuyên môn.
  - **Hierarchical Teams:** Phân cấp đội ngũ.
  - **Joint Collaboration (Swarm):** Phối hợp ngang hàng.
- [ ] **Frameworks thực chiến:**
  - `AutoGen` / `AutoBuild` (Microsoft).
  - `CrewAI` (Role-playing agents).
  - `LangGraph Multi-Agent Workflows`.

## Giai đoạn 4: Đánh giá, Triển khai & Tối ưu Phần cứng
- [ ] **Evaluation & Observability:** LangSmith, Arize Phoenix, AgentOps.
- [ ] **Tối ưu suy luận phần cứng:**
  - Chạy mô hình Agentic (Llama 3, Qwen 2.5, Mistral) cục bộ với `Ollama` / `vLLM` / `SGLang`.
  - Khai thác phần cứng AMD (ROCm, Ryzen AI NPU) để tối ưu hoá chi phí và độ trễ.
