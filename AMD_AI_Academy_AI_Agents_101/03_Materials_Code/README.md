# 💻 AMD AI Academy: AI Agents 101 — Code Labs & Hands-on Materials

Bộ tài liệu và mã nguồn thực hành chuyên sâu mô phỏng 4 trụ cột kiến trúc cốt lõi và các mô hình thiết kế AI Agent hiện đại, tối ưu hóa cho hệ sinh thái phần cứng AMD (AMD ROCm, Ryzen AI NPU XDNA 2, Instinct MI300X, Radeon RX 7000).

---

## 📑 Mục lục & Danh mục Bài thực hành

| Tệp mã nguồn | Chủ đề / Kiến trúc | Công nghệ & Thư viện | Khái niệm then chốt |
| :--- | :--- | :--- | :--- |
| **`01_pure_react_agent.py`** | Vòng lặp Agent thuần (ReAct Loop from Scratch) | Python 3.10+ Standard Library | Thought $\rightarrow$ Action $\rightarrow$ Observation $\rightarrow$ Final Answer, Tra cứu phần cứng AMD, Tính toán an toàn |
| **`02_tool_calling_agent.py`** | Tác tử gọi công cụ & Tự phục hồi lỗi (Tool Calling & Self-Reflection) | JSON Schema, Pydantic v2 / Type Dispatcher | Khai báo schema chuẩn, Điều phối thực thi, Bắt lỗi tham số và Tự phản tỉnh (Self-Reflection) |
| **`03_memory_state_agent.py`** | Quản lý trạng thái & Bộ nhớ hội thoại 4 tầng (Memory & State Management) | Sliding Buffer, Entity Store, TF-IDF Episodic Search | Short-term Buffer Window, Rolling Summary, Structured Entity Store, Semantic Episodic Recall |
| **`04_framework_agent_langgraph.py`** | Đa tác tử cộng tác theo đồ thị trạng thái (Multi-Agent StateGraph Workflow) | Dual-Engine: Official LangGraph + Native Fallback | Supervisor-Worker Pattern, Điều hướng có điều kiện, Kiểm soát chất lượng (Quality Gate Reflection) |
| **`verify_labs.py`** | Bộ kiểm thử tự động toàn diện (Zero-Defect Verification Suite) | `py_compile`, Subprocess Test Runner, Semantic Assertions | Kiểm tra cú pháp 100%, chạy end-to-end độc lập, đối soát token ngữ nghĩa |
| **`requirements.txt`** | Danh mục thư viện phụ thuộc & Hướng dẫn cài đặt ROCm | Pip requirements & PyTorch ROCm Index | Cấu hình môi trường phát triển cục bộ và trên máy chủ AMD GPU/NPU |

---

## 🛠️ Yêu cầu môi trường & Cài đặt (Prerequisites)

Tất cả các bài lab được thiết kế theo nguyên tắc **Zero-Dependency First**: mã nguồn có thể chạy trực tiếp bằng Python 3.10+ tiêu chuẩn (Standard Library) mà không bắt buộc phải cài thêm bất kỳ thư viện bên thứ ba nào.

Nếu bạn muốn cài đặt môi trường đầy đủ để hỗ trợ định dạng Rich và kiểm thử mở rộng:

```bash
# 1. Tạo và kích hoạt môi trường ảo (khuyến nghị)
python3 -m venv .venv
source .venv/bin/activate  # Trên Linux/macOS
# .venv\Scripts\activate   # Trên Windows

# 2. Cài đặt các gói hỗ trợ
pip install -r requirements.txt
```

### ⚡ Dành cho người dùng GPU/APU AMD (ROCm & Ryzen AI):
- **Cài đặt PyTorch hỗ trợ AMD ROCm 6.x (Radeon / Instinct MI300X):**
  ```bash
  pip install torch --index-url https://download.pytorch.org/whl/rocm6.1
  ```
- **Sử dụng NPU Ryzen AI (XDNA / XDNA 2):** Sử dụng gói `onnxruntime-vitisai` và `ryzenai-sw` để suy luận mô hình ngôn ngữ nhỏ (SLM) với năng lượng siêu tiết kiệm (<15W).

---

## 🚀 Hướng dẫn Kiểm tra Tự động (Automated Verification)

Để đảm bảo toàn bộ mã nguồn không có bất kỳ lỗi cú pháp hoặc lỗi runtime nào, hãy thực thi suite kiểm tra tự động:

```bash
# Chạy bộ xác minh tự động tích hợp
python3 verify_labs.py
```

Quy trình `verify_labs.py` thực hiện:
1. **Kiểm tra biên dịch cú pháp (`py_compile`)**: Xác nhận tất cả các tệp `.py` không có lỗi cú pháp Python 3.
2. **Chạy kiểm thử độc lập (`--test-mode`)**: Thực thi lần lượt từng lab, kiểm tra mã thoát (exit code 0).
3. **Đối soát token ngữ nghĩa (Semantic Token Assertions)**: Đảm bảo luồng suy luận, công cụ, bộ nhớ và đồ thị trạng thái sinh ra kết quả chính xác theo yêu cầu kiến trúc.

Bạn cũng có thể kiểm tra cú pháp nhanh bằng lệnh chuẩn của Python:
```bash
python3 -m py_compile *.py
```

---

## 📖 Chi tiết từng Bài Lab Thực hành

### Lab 1: `01_pure_react_agent.py` — ReAct Loop from Scratch
- **Ý tưởng cốt lõi**: Hiện thực hóa thuật toán ReAct (Reasoning and Acting - Yao et al., 2022) từ số 0 mà không sử dụng bất kỳ framework ngoài nào.
- **Cơ chế hoạt động**:
  - Tác tử phân tích câu hỏi người dùng thành chuỗi suy nghĩ (`Thought:`).
  - Tác tử quyết định hành động (`Action: tool_name[arguments]`).
  - Hệ thống thực thi công cụ và trả về kết quả quan sát (`Observation:`).
  - Tác tử lặp lại cho đến khi đủ dữ liệu để đưa ra kết luận (`Final Answer:`).
- **Công cụ tích hợp**:
  - `lookup_hardware`: Tra cứu thông số APU AMD Ryzen AI 9 HX 370 (50 NPU TOPS, Strix Point), máy gia tốc Instinct MI300X (192GB HBM3, 5.3 TB/s), card đồ họa Radeon RX 7900 XTX, Apple M3, Intel Core Ultra.
  - `calculate`: Máy tính số học an toàn không cho phép mã độc.
  - `search_knowledge_base`: Tra cứu kiến thức AMD ROCm, XDNA và 4 trụ cột Agent.
- **Cách chạy**:
  ```bash
  # Chế độ tương tác mặc định:
  python3 01_pure_react_agent.py

  # Chế độ kiểm thử tự động:
  python3 01_pure_react_agent.py --test-mode

  # Tùy chỉnh câu hỏi:
  python3 01_pure_react_agent.py --query "Tra cứu thông số Instinct MI300X và ROCm"
  ```

---

### Lab 2: `02_tool_calling_agent.py` — Tool Calling & Self-Reflection
- **Ý tưởng cốt lõi**: Mô phỏng cơ chế gọi hàm (Function Calling / Tool Calling) theo định dạng JSON Schema hiện đại (tương thích chuẩn OpenAI / Anthropic) kết hợp khả năng **Tự sửa sai (Self-Correction / Reflection)**.
- **Cơ chế hoạt động**:
  - Sử dụng `ToolRegistry` để quản lý siêu dữ liệu công cụ và điều phối tham số.
  - Mô phỏng tình huống tác tử gửi tham số sai (`camera_megapixels` không có trong catalog).
  - Bộ điều phối bắt lỗi `ValueError`, trả về thông báo lỗi chi tiết cho tác tử.
  - Tác tử "tự suy ngẫm" (Self-Reflection), nhận diện danh sách thuộc tính hợp lệ (`npu_tops`, `vram_gb`, `tdp_w`), điều chỉnh lại tham số chính xác và hoàn thành phép tính tổng TOPS cho 4 node cụm edge.
- **Cách chạy**:
  ```bash
  # Chế độ chạy thông thường:
  python3 02_tool_calling_agent.py

  # Chế độ kiểm thử xác nhận lỗi và tự sửa:
  python3 02_tool_calling_agent.py --test-mode
  ```

---

### Lab 3: `03_memory_state_agent.py` — Multi-Tier Memory & State Management
- **Ý tưởng cốt lõi**: Hiện thực hóa kiến trúc quản lý bộ nhớ 4 tầng nhằm giải quyết bài toán giới hạn cửa sổ ngữ cảnh (Context Window) và chi phí token của LLM:
  1. **Working Memory (Buffer ngắn hạn)**: Giữ lại $K$ lượt hội thoại gần nhất trong sliding window.
  2. **Rolling Summary (Bộ nhớ tóm tắt liên tục)**: Khi hội thoại vượt quá kích thước buffer, các lượt cũ được nén thành bản tóm tắt súc tích.
  3. **Structured Entity Store (Bộ nhớ thực thể cấu trúc)**: Trích xuất và lưu giữ các thông tin cốt lõi dưới dạng key-value (`user_name`, `target_hardware`, `npu_tops`, `project_domain`).
  4. **Episodic Recall (Truy hồi ký ức theo ngữ nghĩa)**: Lưu trữ các đoạn hội thoại quá khứ vào kho lưu trữ và dùng thuật toán tương đồng Cosine TF-IDF (100% Python stdlib) để tìm kiếm khi cần.
- **Kịch bản thực nghiệm**: Trải qua 3 lượt hội thoại với nhiều thông số kỹ thuật (Alex, Drone surveillance, Ryzen AI 9 HX 370, INT8 Vitis AI, Instinct MI300X). Ở lượt thứ 4, khi dữ liệu lượt 1 đã bị đẩy ra khỏi working buffer, tác tử vẫn truy hồi chính xác 100% tên người dùng, tên dự án và phần cứng AMD đã chọn.
- **Cách chạy**:
  ```bash
  python3 03_memory_state_agent.py
  python3 03_memory_state_agent.py --test-mode
  ```

---

### Lab 4: `04_framework_agent_langgraph.py` — Multi-Agent StateGraph Workflow
- **Ý tưởng cốt lõi**: Xây dựng hệ thống Đa tác tử cộng tác (Multi-Agent Collaboration) quản lý theo Đồ thị trạng thái có chu trình (Cyclic State Graph) dựa trên mẫu thiết kế LangGraph.
- **Động cơ kép (Dual-Engine Architecture)**:
  - Nếu môi trường đã cài đặt `langgraph`, tệp sẽ tự động kích hoạt `langgraph.graph.StateGraph`.
  - Nếu môi trường chưa cài `langgraph` (môi trường học tập tiêu chuẩn), tệp kích hoạt `NativeStateGraph` — một engine nội tại viết bằng Python thuần (~60 dòng) triển khai chính xác các phương thức `add_node`, `add_edge`, `add_conditional_edges`, `compile`, và `invoke`.
- **Cấu trúc đồ thị cộng tác**:
  - `Supervisor`: Nhận nhiệm vụ, điều phối yêu cầu đến các chuyên gia.
  - `Hardware Specialist`: Phân tích kiến trúc CDNA 3 (Instinct MI300X) và XDNA 2 (Ryzen AI).
  - `Benchmark Analyst`: Đo lường thông lượng TFLOPS, băng thông bộ nhớ (5.3 TB/s vs 3.35 TB/s của H100) và hiệu năng suy luận on-device.
  - `Synthesizer & Reviewer`: Tổng hợp báo cáo điều hành và thực hiện cổng kiểm soát chất lượng (Quality Gate). Nếu chưa đạt, điều hướng trở lại Supervisor; nếu đã chuẩn xác (`APPROVED`), kết thúc quy trình tại `__END__`.
- **Cách chạy**:
  ```bash
  python3 04_framework_agent_langgraph.py
  python3 04_framework_agent_langgraph.py --test-mode
  ```

---

## 🎯 Kết luận & Chuẩn đầu ra

Sau khi hoàn thành 4 bài thực hành này, học viên sẽ nắm vững:
1. Bản chất thuật toán đằng sau các framework agentic phổ biến (LangChain, LangGraph, CrewAI, AutoGen).
2. Kỹ năng thiết kế công cụ, validation schema và xử lý ngoại lệ cho agent tự phục hồi.
3. Kỹ thuật tối ưu hóa chi phí token và quản lý ngữ cảnh thông qua bộ nhớ đa tầng.
4. Nắm bắt sâu sắc lợi thế cạnh tranh của hệ sinh thái phần cứng AMD (từ datacenter MI300X chạy ROCm đến laptop Copilot+ PC chạy NPU Ryzen AI 50 TOPS).
