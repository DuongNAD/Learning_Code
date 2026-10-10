# Đề Cương Chi Tiết Bài Học Module 1 (AI Agents 101)

Tài liệu này được biên soạn dựa trên các nguồn sự thật đã được đối soát:
- **Lời giảng tiếng Anh chính thức:** [transcript.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/02_Notes_Summaries/transcript.md) kèm mốc thời gian.
- **Mã nguồn thực hành:** [01_pure_react_agent.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/01_pure_react_agent.py) kèm số dòng chính xác.
- **Kế hoạch học tập & Lịch trình:** [ROADMAP.md](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/04_Roadmaps/ROADMAP.md).

---

## Phần A: Kế Hoạch Khóa Học "AI Agents 101" (Course Plan)

Khóa học bám sát lộ trình chuẩn, chia nhỏ Module 1 thành 2 bài học chuyên sâu (1a & 1b) và thiết lập các theme Aurora xen kẽ, không trùng lặp giữa các bài liền kề.

| Bài | Tiêu đề bài học | Tóm tắt một dòng | Theme Aurora | Thời điểm (`when`) |
| :--- | :--- | :--- | :--- | :--- |
| **1a** | **Vòng lặp agent: ai làm gì** | Khám phá kiến trúc máy trạng thái ReAct, phân định ranh giới giữa suy luận của LLM và quyền thực thi của Code. | `midnight` | Tuần 2 · Thứ Ba 20/10 (30') |
| **1b** | **Mổ xẻ Lab 1: parser, state và bẫy** | Phân tích mã nguồn Lab 1, vạch trần 4 bẫy chết người của parser regex và quản lý state, thiết lập chuẩn DoD cho `my_react.py`. | `titanium` | Tuần 2 · Thứ Bảy 24/10 (60') |
| **2a** | **Tool calling: Tool là hợp đồng có kiểu** | Chuyển đổi từ trích xuất regex sang JSON Schema có kiểu, xây dựng cơ chế Type Dispatcher và hợp đồng dữ liệu tin cậy. | `ocean` | Tuần 3 · Thứ Bảy 31/10 (60') |
| **2b** | **Tự sửa sai và giải mã có ràng buộc** | Phân tích cơ chế Self-Correction thực tế, phản hồi lỗi có cấu trúc và giới hạn của cờ `--tool-call-parser hermes` trong vLLM. | `daylight` | Tuần 5 · Thứ Bảy 14/11 (60') |
| **3** | **Memory & State: Context window là bộ nhớ làm việc** | Bản chất stateless của LLM API, kiểm soát chi phí token qua sliding window, rolling summary và entity store. | `sunset` | Tuần 6 · Thứ Bảy 21/11 (60') |
| **4a** | **Giao thức MCP: Dây nối chuẩn hóa toàn cầu** | Kiến trúc Host-Client-Server, giao thức JSON-RPC 2.0, transport stdio vs Streamable HTTP và giải quyết bài toán $N \times M$. | `forest` | Tuần 7 · Thứ Bảy 28/11 (60') |
| **4b** | **Thực hành MCP Server: Time, Airbnb và Inspector** | Kết nối PydanticAI với MCP Server đa nguồn, debug qua Inspector và phân tích chuỗi tác vụ câu hỏi Vancouver. | `aurora` | Tuần 8 · Thứ Bảy 05/12 (60') |
| **5** | **Suy luận mã nguồn mở và Phần cứng AMD ROCm** | Tự host LLM với vLLM/SGLang qua OpenAI-compatible API, tính toán giới hạn băng thông bộ nhớ và định cỡ KV Cache. | `titanium` | Tuần 10 · Thứ Bảy 19/12 (60') |
| **6a** | **Lab chính thức: PydanticAI kết nối MCP và vLLM** | Thực hành 7 bước từ notebook AMD: từ agent đơn giản, custom tool đến tích hợp hệ thống MCP hoàn chỉnh. | `midnight` | Tuần 11 · Thứ Bảy 26/12 (60') |
| **6b** | **Thử thách Weather MCP và Truy vết Execution Trace** | Mở rộng agent với server thời tiết, kiểm chứng tính xác thực của dữ liệu và đối soát vết thực thi (Execution Trace). | `liquid` | Tuần 12 · Thứ Ba 29/12 (60') |
| **7** | **Patterns, Framework hay Code thuần** | 5 mẫu thiết kế (Chaining, Routing, Orchestrator...), kiến trúc đồ thị LangGraph và tiêu chuẩn chọn giải pháp tối giản. | `paper` | Tuần 13 · Thứ Năm 07/01/2027 (60') |
| **9** | **Đánh giá, An toàn và Guardrails cho Agent** | Tam giác tử thần (Lethal Trifecta), OWASP LLM01, Human-in-the-loop và xây dựng bộ eval 10 ca kiểm thử định lượng. | `sunset` | Tuần 14 · Thứ Năm 14/01/2027 (60') |
| **8** | **RAG cho Agent: Chunking và Contextual Retrieval** *(Tùy chọn)* | Kiến trúc nạp và truy xuất tài liệu, đo lường hit@k và đánh giá thực nghiệm tính hiệu quả của semantic chunking. | `forest` | Tuần 16 · Thứ Năm 28/01/2027 (60') |
| **Cap** | **Dự án Tổng hợp: Hệ thống Agent Tự chủ Toàn diện** | Tích hợp trọn vẹn LLM local, MCP Server, Guardrails và Eval Suite tự động đạt chuẩn sản xuất. | `aurora` | Tuần 15 · Thứ Sáu 23/01/2027 (60') |

---

## Phần B: Đề Cương Slide Chi Tiết

### BÀI HỌC 1a: Vòng lặp Agent: Ai Làm Gì Trong ReAct?
- **Độ dài:** 14 slides
- **Theme gợi ý:** `midnight` (Accent: `cyan`)
- **Tập tin liên kết:** `../../../03_Materials_Code/01_pure_react_agent.py`

---

#### Slide 1a.1: Tiêu đề mở đầu (Hero Slide)
- **Slide Type:** `title`
- **Fields & Content:**
  - `title`: "Vòng Lặp Agent:\n++Ai Làm Gì++ Trong ReAct?"
  - `subtitle`: "Phân định ranh giới giữa suy luận xác suất của LLM và quyền thực thi tất định của Code"
  - `icon`: `"ph:arrows-clockwise-duotone"`
- **Nguồn:** `Khóa học · transcript 01:05-03:07`
- **Ghi chú (`notes`):** Bài học đặt nền móng kiến trúc: LLM chỉ là bộ não suy luận ngôn ngữ, không tự chạy được lệnh. Mọi hành động tương tác với thế giới đều do Code Python bên ngoài điều phối.

---

#### Slide 1a.2: Tuyên bố cốt lõi (Core Statement)
- **Slide Type:** `statement`
- **Fields & Content:**
  - `kicker`: "Nguyên lý vận hành tối thượng"
  - `text`: "LLM chỉ có quyền ==đề xuất hành động==.\nChỉ có **Code** mới thực thi công cụ và quyết định ==khi nào dừng==."
- **Nguồn:** `Khóa học · transcript 02:13-02:17` & `Mở rộng · Anthropic Building Effective Agents`
- **Ghi chú (`notes`):** Mô hình ngôn ngữ lớn bản chất là một bộ sinh token tự hồi quy. Nó không có tiến trình OS, không có network socket. Khi LLM xuất chuỗi `Action: calculate[8 * 50]`, đó thuần túy là văn bản cho tới khi code Python của bạn bắt lấy và gọi hàm.

---

#### Slide 1a.3: Ẩn dụ bài giảng & Giới hạn liên tưởng (Analogy Slide)
- **Slide Type:** `analogy`
- **Fields & Content:**
  - `eyebrow`: "Mô hình liên tưởng từ bài giảng"
  - `title`: "LLM là cuốn sách thông minh, Agent là bộ não gắn thêm tay chân"
  - `known`: `{"label": "Cuốn sách bách khoa", "icon": "ph:book-bookmark-duotone"}`
  - `concept`: `{"label": "AI Agent hoàn chỉnh", "icon": "ph:robot-duotone"}`
  - `pairs`:
    - `{"known": "Biết câu trả lời lý thuyết nhưng không tự cầm bút viết", "concept": "LLM suy luận và lập kế hoạch nhưng không tự gọi API"}`
    - `{"known": "Cùng một cuốn sách, người thợ khác nhau làm ra việc khác nhau", "concept": "Cùng một LLM, cấp bộ công cụ khác nhau tạo ra Agent khác nhau"}`
    - `{"known": "Không có đồng hồ đeo tay thì không biết mấy giờ", "concept": "Không có tool ngày giờ thì trả lời sai câu 'Hôm nay ngày mấy'"}`
  - `limit`: "Cuốn sách là tri thức tĩnh; nhưng LLM là mô hình xác suất có thể bị ảo giác (hallucination) và tính nhẩm sai. Agent cần tool toán học và tra cứu để đảm bảo tính tất định."
- **Nguồn:** `Khóa học · transcript 01:05-02:21, 06:03-06:09`
- **Ghi chú (`notes`):** Nhấn mạnh câu chốt của giảng viên Mahdi Ghodsi: "LLMs provide the reasoning, but the tools define the actions. Same brain, different tools."

---

#### Slide 1a.4: So sánh kiến trúc (Architecture Comparison)
- **Slide Type:** `compare`
- **Fields & Content:**
  - `eyebrow`: "So sánh cơ chế xử lý"
  - `title`: "LLM Đơn Lẻ vs ReAct Agent"
  - `vs`: `true`
  - `columns`:
    - `title`: "LLM Đơn Lẻ (Zero-Shot / CoT)", `icon`: `"ph:x-circle-duotone"`, `tone`: `"bad"`, `items`:
      - "Chỉ dựa vào trọng số đóng băng tại thời điểm huấn luyện",
      - "Dễ tính nhẩm sai các phép toán nhiều chữ số",
      - "Không thể truy cập dữ liệu thời gian thực (ngày, giờ, giá cả)"
    - `title`: "ReAct Agent (Reason + Act)", `icon`: `"ph:check-circle-duotone"`, `tone`: `"good"`, `highlight`: `true`, `items`:
      - "Xen kẽ suy nghĩ (`Thought`) và hành động (`Action`) từng bước",
      - "Ủy thác tính toán số học chính xác cho Python (`calculate`)",
      - "Thu thập dữ kiện thời gian thực qua công cụ (`Observation`)"
- **Nguồn:** `Khóa học · transcript 02:21-03:07` & `Mở rộng · Yao et al. (ReAct paper, ICLR 2023)`
- **Ghi chú (`notes`):** Bài báo ReAct chứng minh: kết hợp suy luận với hành động giúp giảm ảo giác đáng kể so với Chain-of-Thought đơn thuần trên HotpotQA và FEVER.

---

#### Slide 1a.5: Sơ đồ máy trạng thái (Agent Loop State Machine)
- **Slide Type:** `diagram`
- **Fields & Content:**
  - `eyebrow`: "Kiến trúc hệ thống"
  - `title`: "Máy trạng thái của Vòng lặp Agent (State Machine)"
  - `caption`: "Luồng điều khiển tuần hoàn khép kín giữa LLM và Code thực thi"
  - `code`:
    ```mermaid
    flowchart TD
        S(["1. Nhận mục tiêu & Khởi tạo history"]) --> P["2. Gọi LLM (Prompt = System + History)"]
        P --> D{"3. Parser bóc tách: Có Final Answer?"}
        D -->|"Có"| F(["4. Dừng thành công (Trả Final Answer)"])
        D -->|"Không"| V{"5. Tool hợp lệ trong danh mục?"}
        V -->|"Có"| X["Code chạy Tool -> Tạo Observation"]
        V -->|"Không"| E["Code tạo Error Observation có cấu trúc"]
        X --> U["6. Cập nhật State (Append vào history)"]
        E --> U
        U --> G{"7. Còn ngân sách bước (step <= max_steps)?"}
        G -->|"Còn"| P
        G -->|"Hết"| H(["Dừng thất bại (Timeout/Báo lỗi)"])
    ```
- **Nguồn:** `Khóa học · Lab 1 dòng 249-313` & `ROADMAP.md mục 2.1, 4 (M1)`
- **Ghi chú (`notes`):** Sơ đồ chuẩn hóa 7 trạng thái. Lưu ý: `Final Answer` là cửa thoát (exit condition), KHÔNG PHẢI là một bước nằm bên trong chu trình lặp.

---

#### Slide 1a.6: Memory Palace — 7 Trạm trong ngôi nhà (Loci Method)
- **Slide Type:** `palace`
- **Fields & Content:**
  - `id`: `"palace-agent-loop"`
  - `eyebrow`: "Mỏ neo trí nhớ (Memory Anchor)"
  - `title`: "7 Bước Vòng Lặp Agent:\nMột vòng quanh nhà bạn"
  - `subtitle`: "Gắn chặt 7 trạng thái của State Machine vào 7 vị trí quen thuộc"
  - `mode`: `"learn"`
  - `stations`:
    - `place`: "1. Cửa ra vào", `item`: "Nhận mục tiêu & Reset State", `hook`: "Khách bấm chuông đưa tờ giấy ghi câu hỏi; bạn xóa sạch bảng trắng treo ở cửa để chuẩn bị ghi chép", `icon`: `"ph:door-duotone"`
    - `place`: "2. Kệ giày", `item`: "Ghép Prompt & Gửi LLM", `hook`: "Xếp toàn bộ lịch sử hội thoại vào một chiếc cặp tài liệu rồi gửi chuyển phát nhanh cho chuyên gia LLM", `icon`: `"ph:paper-plane-tilt-duotone"`
    - `place`: "3. Ghế sofa", `item`: "Parser bóc tách chuỗi", `hook`: "Ngồi trên sofa cầm kéo cắt bức thư phản hồi thành 4 mảnh: Thought, Tool, Arg, Final Answer", `icon`: `"ph:scissors-duotone"`
    - `place`: "4. Màn hình TV", `item`: "Lối thoát Final Answer", `hook`: "Bật TV thấy hiện đáp án cuối cùng rực rỡ; bạn tắt nguồn TV và hoàn thành nhiệm vụ ngay lập tức", `icon`: `"ph:television-duotone"`
    - `place`: "5. Bàn ăn", `item`: "Code thực thi Tool", `hook`: "Mở hộp đồ nghề trên bàn ăn, cắm máy tính bấm '8 * 50 = 400' tạo ra kết quả Observation thực tế", `icon`: `"ph:wrench-duotone"`
    - `place`: "6. Cánh tủ lạnh", `item`: "Cập nhật History Buffer", `hook`: "Dán nam châm đính mảnh giấy Thought, Action, Observation vừa làm xong lên cánh tủ lạnh", `icon`: `"ph:notepad-duotone"`
    - `place`: "7. Bếp nấu (Cầu dao)", `item`: "Kiểm tra Ngân sách (max_steps)", `hook`: "Đồng hồ hẹn giờ bếp reo 'reng reng'; nếu đếm quá 6 lần mà chưa xong thì cầu dao tự ngắt điện", `icon`: `"ph:timer-duotone"`
- **Nguồn:** `Mở rộng · Phương pháp ghi nhớ Loci (DeepTutor pedagogical anchor)`
- **Ghi chú (`notes`):** Hãy hình dung thật sống động lộ trình này trong ngôi nhà của bạn từ Cửa ra vào -> Kệ giày -> Sofa -> TV -> Bàn ăn -> Tủ lạnh -> Bếp. Lát nữa chúng ta sẽ đi bộ kiểm tra lại (Recall walk).

---

#### Slide 1a.7: Phân công trách nhiệm (Responsibility Matrix)
- **Slide Type:** `split`
- **Fields & Content:**
  - `eyebrow`: "Ranh giới thực thi"
  - `title`: "Ai Làm Gì Trong Từng Vòng Lặp?"
  - `text`: "Sự phân định rạch ròi giữa trí tuệ nhân tạo và mã nguồn điều phối."
  - `items`:
    - "**Phần LLM sinh:** Chuỗi suy nghĩ phân tích (`Thought:`), tên công cụ cần dùng (`Action: tool_name[arg]`), hoặc kết luận cuối cùng (`Final Answer:`).",
    - "**Phần Code thực thi:** Lắp ghép prompt ngữ cảnh, gọi hàm parser bóc tách regex, kiểm tra an toàn và chạy hàm Python `TOOLS[tool_name](arg)`, đo lường số bước và ngắt vòng lặp."
- **Nguồn:** `Khóa học · Lab 1 dòng 259-313`
- **Ghi chú (`notes`):** Rất nhiều lập trình viên mới lầm tưởng "Agent tự gọi tool". Thực tế, model chỉ sinh chuỗi văn bản; hàm Python `TOOLS[tool_name](tool_arg)` ở dòng 291 mới là nơi thực sự kích hoạt tính toán.

---

#### Slide 1a.8: Khám phá mã nguồn vòng lặp (Source Code Walkthrough)
- **Slide Type:** `code`
- **Fields & Content:**
  - `eyebrow`: "Mã nguồn tham chiếu"
  - `title`: "Trái tim vòng lặp: ReActAgent.run"
  - `lang`: `"python"`
  - `filename`: `"01_pure_react_agent.py"`
  - `code`: "for step in range(1, self.max_iterations + 1):\n    context_prompt = SYSTEM_PROMPT + f\"\\nQuestion: {question}\\n\" + \"\\n\".join(history)\n    llm_response = self.llm.generate(context_prompt, question)\n    thought, tool_name, tool_arg, final_answer = ReActParser.parse(llm_response)\n    \n    if final_answer:\n        return {\"success\": True, \"final_answer\": final_answer, \"steps\": step}\n        \n    if tool_name:\n        if tool_name in TOOLS:\n            observation = TOOLS[tool_name](tool_arg)\n        else:\n            observation = f\"Error: Tool '{tool_name}' does not exist.\"\n        history.append(f\"Thought: {thought}\")\n        history.append(f\"Action: {tool_name}[{tool_arg}]\")\n        history.append(f\"Observation: {observation}\")"
  - `steps`:
    - `{"lines": "1", "text": "Khởi tạo vòng lặp đếm bước với chốt chặn cứng self.max_iterations = 6."}`
    - `{"lines": "2-3", "text": "Tái tạo prompt hoàn chỉnh từ SYSTEM_PROMPT + Câu hỏi + Lịch sử tích lũy."}`
    - `{"lines": "4", "text": "Parser bóc tách chuỗi văn bản thành 4 trường dữ liệu."}`
    - `{"lines": "6-7", "text": "Nếu có final_answer: Thoát ngay lập tức (Exit condition), không chạy tool."}`
    - `{"lines": "9-16", "text": "Code kiểm tra và thực thi hàm trong TOOLS dictionary, sau đó append kết quả vào history."}`
- **Nguồn:** `Khóa học · Lab 1 dòng 259-303`
- **Ghi chú (`notes`):** Chú ý cách `history` được nối vào chuỗi ở mỗi lượt lặp. Đây chính là nguyên nhân dẫn đến sự tăng trưởng bậc hai của chi phí token.

---

#### Slide 1a.9: Trang sổ tay ghi chép (Paper Notebook Anchor)
- **Slide Type:** `notebook`
- **Fields & Content:**
  - `eyebrow`: "Ghi chép cốt lõi"
  - `title`: "Sổ tay kiến trúc Vòng lặp Agent"
  - `page`: "AI Agents 101 · Bài 1a"
  - `lines`:
    - "# 1. Bản chất ReAct"
    - `{"term": "ReAct", "def": "LLM suy luận (Thought), Code thực thi (Action -> Observation), lặp đến Final Answer"}`
    - "# 2. Công thức chi phí Token đầu vào tích lũy"
    - "= \\text{Total Input Tokens} = T \\cdot p + k \\cdot \\frac{T(T-1)}{2}"
    - "# 3. Quy tắc an toàn bắt buộc"
    - "! LLM chỉ đề xuất; Code nắm quyền thực thi và quyết định dừng"
    - "! Luôn đặt max_iterations (ngưỡng ngắt cứng) để chống cháy tài khoản"
    - "! Final Answer là điều kiện thoát vòng lặp, không phải bước nội bộ"
- **Nguồn:** `ROADMAP.md mục 4 (M1)` & `Khóa học · Lab 1 dòng 245, 274`
- **Ghi chú (`notes`):** Hãy chép công thức token vào sổ tay giấy: với prompt gốc $p=1500$, mỗi bước thêm $k=400$, khi $T=10$ bước tiêu tốn 33.000 token; khi $T=20$ bước bùng nổ lên 106.000 token (tăng gấp 3,2 lần dù số bước chỉ tăng 2 lần).

---

#### Slide 1a.10: Dự đoán rồi mới chạy #1 — Câu hỏi mặc định (Predict-then-Run 1)
- **Slide Type:** `split`
- **Fields & Content:**
  - `eyebrow`: "Thực hành dự đoán (Predict-then-Run)"
  - `title`: "Dự đoán vết thực thi: 8 APU Ryzen AI 9 HX 370"
  - `text`: "**Câu hỏi:** Tính tổng NPU TOPS của cụm 8 máy AMD Ryzen AI 9 HX 370 và so sánh với Apple M3.\n\n*Hãy viết dự đoán số lượt, tên tool và kết quả trước khi nhìn đáp án bên phải!*"
  - `items`:
    - "**Lượt 1:** `lookup_hardware[Ryzen AI 9 HX 370]` $\\to$ Trả về thông số APU Strix Point (50 NPU TOPS).",
    - "**Lượt 2:** `calculate[8 * 50]` $\\to$ Trả về `400` (tổng NPU TOPS cụm 8 node).",
    - "**Lượt 3:** `calculate[400 / 18]` $\\to$ Trả về `22.2222` (so với Apple M3 18 TOPS).",
    - "**Lượt 4:** `Final Answer` $\\to$ Xuất kết luận: Tổng 400 TOPS, mật độ tính toán gấp ~22.22x Apple M3. Dừng sau 4 bước, chạy 3 tool."
- **Nguồn:** `Khóa học · Lab 1 dòng 178-202 (suy ra từ code)`
- **Ghi chú (`notes`):** Đây là kịch bản Scenario 1 trong `DeterministicMockLLM`. Khi đối soát kết quả chạy thực tế `py -3.11 01_pure_react_agent.py`, toàn bộ các bước khớp 100% với dự đoán logic này.

---

#### Slide 1a.11: Dự đoán rồi mới chạy #2 — Bóc trần Mock LLM (Predict-then-Run 2)
- **Slide Type:** `split`
- **Fields & Content:**
  - `eyebrow`: "Thực hành dự đoán (Predict-then-Run)"
  - `title`: "Dự đoán khi hỏi: '--query \"What is ReAct?\"'"
  - `text`: "**Câu hỏi:** Chuyện gì xảy ra nếu ta truyền câu hỏi lý thuyết: `What is ReAct?` vào Lab 1?\n\n*Mock LLM có trả lời đúng định nghĩa ReAct không?*"
  - `items`:
    - "**Phân tích mã nguồn:** Trong `DeterministicMockLLM.generate` (dòng 178, 205), bộ kiểm từ khóa chỉ kiểm tra `'cluster'`, `'ryzen'`, `'tops'`, `'rocm'`, `'mi300x'`. Không có nhánh nào cho `'react'`!",
    - "**Lọt vào nhánh Fallback (dòng 225):**",
    - "**Lượt 1:** Gọi `search_knowledge_base[four pillars]` (Tra cứu 4 trụ cột dù hỏi ReAct!).",
    - "**Lượt 2:** Trả `Final Answer` về 'four core pillars: Perception, Planning, Action, Memory'.",
    - "**Bài học xương máu:** Mock LLM là kịch bản giả lập theo biến đếm `step`, hoàn toàn KHÔNG ĐỌC hay HIỂU prompt!"
- **Nguồn:** `Khóa học · Lab 1 dòng 225-236 (suy ra từ code)`
- **Ghi chú (`notes`):** Điểm cốt lõi giúp học viên phân biệt giữa việc "test logic vòng lặp điều phối của Code" và "năng lực hiểu ngôn ngữ tự nhiên của LLM thật".

---

#### Slide 1a.12: Đi bộ kiểm tra trí nhớ (Palace Recall Walk)
- **Slide Type:** `palace`
- **Fields & Content:**
  - `from`: `"palace-agent-loop"`
  - `eyebrow`: "Kiểm tra chủ động (Active Recall)"
  - `title`: "Đi bộ kiểm tra 7 trạm State Machine"
  - `subtitle`: "Hãy nhắm mắt, đi lại 7 vị trí trong nhà và tự gọi tên trạng thái tương ứng"
  - `mode`: `"recall"`
- **Nguồn:** `Mở rộng · Phương pháp ghi nhớ Loci (DeepTutor pedagogical anchor)`
- **Ghi chú (`notes`):** Học viên tự đánh giá mức độ ghi nhớ từng trạm (1. Cửa ra vào -> 2. Kệ giày -> 3. Sofa -> 4. TV -> 5. Bàn ăn -> 6. Tủ lạnh -> 7. Bếp). Nếu quên trạm nào, hãy quay lại xem hook liên tưởng tương ứng.

---

#### Slide 1a.13: Câu hỏi trắc nghiệm kiểm tra (Concept Quiz)
- **Slide Type:** `quiz`
- **Fields & Content:**
  - `eyebrow`: "Kiểm tra hiểu biết"
  - `question`: "Trong vòng lặp ReAct chuẩn, khi LLM sinh ra văn bản chứa 'Final Answer: ...', điều gì sẽ diễn ra tiếp theo trong mã nguồn Python?"
  - `options`:
    - `{"text": "Vòng lặp kết thúc ngay lập tức, trả kết quả về cho người dùng mà không gọi thêm tool nào.", "explain": "Chính xác! Final Answer là điều kiện dừng (Exit condition) được kiểm tra đầu tiên."}`
    - `{"text": "Code tiếp tục chạy thêm một Action nữa để kiểm chứng câu trả lời của LLM.", "explain": "Sai. Khi đã có Final Answer, parser không tìm thấy tool_name và hàm run() return ngay lập tức."}`
    - `{"text": "Hệ điều hành tự động cập nhật trọng số mô hình để ghi nhớ kết luận này.", "explain": "Sai hoàn toàn. Quá trình suy luận (Inference) không làm thay đổi trọng số của LLM."}`
  - `answer`: 0
  - `explanation`: "Theo đúng thiết kế tại dòng 274-283 của Lab 1, `if final_answer:` sẽ kích hoạt lệnh `return` ngay lập tức, đưa trạng thái thành công và ngắt chu trình."
- **Nguồn:** `Khóa học · Lab 1 dòng 274-283`
- **Ghi chú (`notes`):** Đảm bảo học viên khắc sâu khái niệm Final Answer là lối thoát của vòng lặp, không phải một trạng thái tuần hoàn bên trong.

---

#### Slide 1a.14: Đúc kết bài học 1a (Summary Slide)
- **Slide Type:** `summary`
- **Fields & Content:**
  - `eyebrow`: "Đúc kết kiến thức"
  - `title`: "Những điều cốt tử của Bài 1a"
  - `items`:
    - "LLM chỉ là bộ não đề xuất suy luận; Code Python mới là thực thể điều phối và thực thi công cụ",
    - "Vòng lặp ReAct gồm 7 trạng thái khép kín với điều kiện dừng cứng (`max_iterations = 6`)",
    - "Chi phí token đầu vào tăng lũy tiến bậc hai $O(T^2)$ theo số lượt lặp $T$",
    - "Mock LLM trong Lab 1 chỉ là kịch bản tất định theo bước (`step`), không đọc ngữ nghĩa prompt",
    - "Chuẩn bị bước sang Bài 1b: Mổ xẻ 4 bẫy chết người của Regex Parser và Quản lý State!"
  - `score`: `true`
- **Nguồn:** `Khóa học · Lab 1` & `ROADMAP.md mục 4 (M1)`
- **Ghi chú (`notes`):** Học viên hoàn tất phần lý thuyết nền móng của vòng lặp. Chuyển tiếp ngay sang bài 1b để thực hành mổ xẻ code chi tiết.

---

### BÀI HỌC 1b: Mổ Xẻ Lab 1: Parser, State và 4 Bẫy Chết Người
- **Độ dài:** 14 slides
- **Theme gợi ý:** `titanium` (Accent: `orange`)
- **Tập tin liên kết:** `../../../03_Materials_Code/01_pure_react_agent.py`

---

#### Slide 1b.1: Tiêu đề mở đầu (Hero Slide)
- **Slide Type:** `title`
- **Fields & Content:**
  - `title`: "Mổ Xẻ Lab 1:\n++Parser, State & 4 Bẫy++"
  - `subtitle`: "Phân tích các lỗ hổng kỹ thuật trong ReAct thuần và thiết lập tiêu chí hoàn thành cho my_react.py"
  - `icon`: `"ph:bug-beetle-duotone"`
- **Nguồn:** `Khóa học · Lab 1 dòng 129-313` & `ROADMAP.md mục 4 (M1)`
- **Ghi chú (`notes`):** Mục tiêu bài 1b: biến một lập trình viên biết đọc code thành người làm chủ cơ chế xử lý ngoại lệ, thấu hiểu vì sao ngành công nghiệp phải chuyển dịch từ regex sang tool calling có schema.

---

#### Slide 1b.2: Khởi động ôn tập — Memory Palace Recall
- **Slide Type:** `palace`
- **Fields & Content:**
  - `eyebrow`: "Khởi động đầu giờ (Active Recall)"
  - `title`: "Đi lại 7 trạm vòng lặp từ Bài 1a"
  - `subtitle`: "Nhắc lại nhanh 7 trạng thái trước khi đi sâu vào mã nguồn chi tiết"
  - `mode`: `"recall"`
  - `stations`:
    - `{"place": "1. Cửa ra vào", "item": "Nhận mục tiêu & Reset State", "icon": "ph:door-duotone"}`
    - `{"place": "2. Kệ giày", "item": "Ghép Prompt & Gửi LLM", "icon": "ph:paper-plane-tilt-duotone"}`
    - `{"place": "3. Ghế sofa", "item": "Parser bóc tách chuỗi", "icon": "ph:scissors-duotone"}`
    - `{"place": "4. Màn hình TV", "item": "Lối thoát Final Answer", "icon": "ph:television-duotone"}`
    - `{"place": "5. Bàn ăn", "item": "Code thực thi Tool", "icon": "ph:wrench-duotone"}`
    - `{"place": "6. Cánh tủ lạnh", "item": "Cập nhật History Buffer", "icon": "ph:notepad-duotone"}`
    - `{"place": "7. Bếp nấu (Cầu dao)", "item": "Kiểm tra Ngân sách (max_steps)", "icon": "ph:timer-duotone"}`
- **Nguồn:** `Mở rộng · DeepTutor pedagogical anchor`
- **Ghi chú (`notes`):** Kích hoạt trí nhớ dài hạn trước khi phân tích chi tiết từng trạm sofa (Parser) và trạm tủ lạnh (State).

---

#### Slide 1b.3: Mổ xẻ ReActParser (Parser Deep Dive)
- **Slide Type:** `code`
- **Fields & Content:**
  - `eyebrow`: "Mổ xẻ mã nguồn"
  - `title`: "Cơ chế bóc tách của ReActParser.parse"
  - `lang`: `"python"`
  - `filename`: `"01_pure_react_agent.py"`
  - `code`: "class ReActParser:\n    @staticmethod\n    def parse(text: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:\n        # 1. Bắt Final Answer\n        ans_match = re.search(r\"Final Answer:\\s*(.+)\", text, re.DOTALL | re.IGNORECASE)\n        if ans_match:\n            thought_match = re.search(r\"Thought:\\s*(.+?)(?=\\nFinal Answer:|$)\", text, re.DOTALL | re.IGNORECASE)\n            return (thought_match.group(1).strip() if thought_match else \"\"), None, None, ans_match.group(1).strip()\n            \n        # 2. Bắt Action dạng bracket: name[arg] hoặc name(arg)\n        action_bracket = re.search(r\"Action:\\s*([a-zA-Z0-9_]+)\\s*[\\[\\(](.*?)[\\/\\])]\", text, re.DOTALL | re.IGNORECASE)\n        if action_bracket:\n            return thought, action_bracket.group(1).strip(), action_bracket.group(2).strip(), None\n            \n        # 3. Bắt Action dạng 2 dòng: Action: name \\n Action Input: arg\n        action_line = re.search(r\"Action:\\s*([a-zA-Z0-9_]+)\", text, re.IGNORECASE)\n        if action_line:\n            input_line = re.search(r\"Action Input:\\s*(.+?)(?=\\nObservation:|$)\", text, re.DOTALL | re.IGNORECASE)\n            return thought, action_line.group(1).strip(), (input_line.group(1).strip() if input_line else \"\"), None"
  - `steps`:
    - `{"lines": "2", "text": "Hàm parse luôn trả về đúng 4 giá trị: (thought, tool_name, tool_arg, final_answer)."}`
    - `{"lines": "4-7", "text": "Ưu tiên số 1: Quét Final Answer trước. Nếu thấy, lập tức bỏ qua mọi Action bên dưới!"}`
    - `{"lines": "10-12", "text": "Hỗ trợ linh hoạt cả ngoặc vuông name[...] lẫn ngoặc tròn name(...)."}`
    - `{"lines": "15-18", "text": "Hỗ trợ định dạng LangChain cổ điển: Action: name kèm Action Input: arg riêng dòng."}`
- **Nguồn:** `Khóa học · Lab 1 dòng 129-162`
- **Ghi chú (`notes`):** Chỉ rõ cho học viên thấy thiết kế trả về 4 phần tử (tuple) và thứ tự ưu tiên regex. Đây là tiền đề để nhận diện 2 bẫy nguy hiểm tiếp theo.

---

#### Slide 1b.4: Bẫy 1 — Regex ngoặc lồng (Nested Brackets Trap)
- **Slide Type:** `split`
- **Fields & Content:**
  - `eyebrow`: "Phân tích lỗi hiểm hóc (Trap 1/4)"
  - `title`: "Bẫy Regex lười: Cắt cụt biểu thức toán"
  - `text`: "**Tình huống:** LLM sinh ra lệnh toán học có ngoặc lồng nhau:\n`Action: calculate[(2 + 3) * 4]`\n\n*Điều gì thực sự xảy ra trong bộ máy Regex?*"
  - `items`:
    - "**Biểu thức Regex dòng 147:** `r'Action:\\s*([a-zA-Z0-9_]+)\\s*[\\[\\(](.*?)[\\/\\])]'`",
    - "**Nguyên nhân:** Ký tự `(.*?)` là toán tử so khớp lười (lazy quantifier) và tập kết thúc chứa cả `]` lẫn `)`. Khi gặp dấu `)` đóng đầu tiên của `(2 + 3)`, regex lập tức dừng lại!",
    - "**Kết quả bóc tách:** `tool_name = 'calculate'`, `tool_arg = '(2 + 3'` (mất hẳn đoạn `* 4]`)",
    - "**Hậu quả trong hàm eval (dòng 31):** Trả về `Calculation Error: '(' was never closed`!",
    - "**Giải pháp:** Xây dựng parser đếm cặp ngoặc cân bằng (bracket counter) hoặc chuyển sang JSON Tool Calling."
- **Nguồn:** `Khóa học · Lab 1 dòng 23-36, 147-151` & `ROADMAP.md mục 4 (M1)`
- **Ghi chú (`notes`):** Đây là lỗi kinh điển chứng minh sự mong manh của việc trích xuất văn bản thô bằng Regular Expressions.

---

#### Slide 1b.5: Bẫy 2 — Ảo giác Observation tự bịa (Hallucinated Observation Trap)
- **Slide Type:** `split`
- **Fields & Content:**
  - `eyebrow`: "Phân tích lỗ hổng bảo mật & logic (Trap 2/4)"
  - `title`: "Bẫy LLM tự biên tự diễn: Bỏ qua thực thi Tool"
  - `text`: "**Tình huống:** Do temperature cao hoặc thiếu stop sequence, LLM sinh luôn một mạch cả 3 khối:\n```text\nThought: Cần tính toán\nAction: calculate[2 + 3]\nObservation: 5\nFinal Answer: Kết quả là 5\n```"
  - `items`:
    - "**Cơ chế thực thi của Parser (dòng 135):** Parser tìm thấy chuỗi `Final Answer:` ở đầu hàm và lập tức gán `final_answer = 'Kết quả là 5'`.",
    - "**Lỗ hổng trong ReActAgent.run (dòng 274):** Nhánh `if final_answer:` được ưu tiên kích hoạt và `return` ngay!",
    - "**Hậu quả nghiêm trọng:** Khối `if tool_name:` ở dòng 286 **hoàn toàn không được chạy**. Agent chấp nhận kết quả ảo giác mà 0 tool nào được Python thực thi!",
    - "**Biện pháp chặn:** Cài đặt `stop_sequences = ['Observation:']` khi gọi API LLM, hoặc bắt buộc parser phải kiểm tra và ưu tiên xử lý Action chưa có Observation."
- **Nguồn:** `Khóa học · Lab 1 dòng 135-140, 274-283` & `ROADMAP.md mục 4 (M1)`
- **Ghi chú (`notes`):** Vô cùng quan trọng. Nếu không chặn bẫy này, agent của bạn sẽ đưa ra quyết định dựa trên dữ liệu giả do chính LLM tự bịa ra trong prompt.

---

#### Slide 1b.6: Bẫy 3 — Ô nhiễm State khi gọi run() nhiều lần (State Pollution Trap)
- **Slide Type:** `code`
- **Fields & Content:**
  - `eyebrow`: "Phân tích bẫy trạng thái (Trap 3/4)"
  - `title`: "Bẫy tái sử dụng Mock: step counter không reset"
  - `lang`: `"python"`
  - `filename`: `"01_pure_react_agent.py"`
  - `code`: "mock_llm = DeterministicMockLLM()\nagent = ReActAgent(llm_engine=mock_llm)\n\n# Lần chạy 1: Khởi động bình thường\nres1 = agent.run(\"Calculate total NPU TOPS of 8 APUs...\")\n# -> mock_llm.step tăng từ 0 lên 4 -> Trả Final Answer sau 4 bước (PASS)\n\n# Lần chạy 2: Chạy tiếp một câu hỏi mới với CÙNG instance agent\nres2 = agent.run(\"Calculate total NPU TOPS of 8 APUs...\")\n# -> mock_llm.step lúc này = 4, vào hàm tăng lên 5 (> 3)!\n# -> Ngay Turn 1, mock rơi vào nhánh else và sinh ngay Final Answer!\n# -> Kết quả: 1 bước, 0 tools executed -> SAI HOÀN TOÀN LUỒNG THỰC THI!"
  - `steps`:
    - `{"lines": "1-2", "text": "Khởi tạo một instance mock duy nhất và truyền vào agent."}`
    - `{"lines": "5-6", "text": "Lần 1 chạy hoàn hảo, mock.step tăng lên 4."}`
    - `{"lines": "9-13", "text": "Lần 2: Do mock.step không được reset, mock trả Final Answer ngay ở bước 1 mà không chạy tool nào!"}`
- **Nguồn:** `Khóa học · Lab 1 dòng 170-202` & `ROADMAP.md mục 4 (M1)`
- **Ghi chú (`notes`):** Bài học về quản lý State: Trạng thái của từng phiên chạy phải độc lập (stateless execution). Không được để rò rỉ biến đếm trạng thái giữa các phiên gọi `run()`.

---

#### Slide 1b.7: Bẫy 4 — Xử lý Tool lạ & Tiêm phản hồi lỗi (Unknown Tool Handling)
- **Slide Type:** `split`
- **Fields & Content:**
  - `eyebrow`: "Cơ chế tự sửa sai (Trap 4/4)"
  - `title`: "Xử lý Tool không tồn tại: Error Feedback Injection"
  - `text`: "**Tình huống:** LLM bị ảo giác gọi một công cụ ngoài danh mục:\n`Action: query_cloud_pricing[\"MI300X\"]`\n\n*Hệ thống phản ứng thế nào để không sập chương trình?*"
  - `items`:
    - "**Không được crash ứng dụng:** Dòng 290 kiểm tra an toàn `if tool_name in TOOLS:` thay vì gọi trực tiếp `TOOLS[tool_name]` gây `KeyError`.",
    - "**Tạo thông báo lỗi có cấu trúc (dòng 294):**\n`observation = f\"Error: Tool '{tool_name}' does not exist. Available: {list(TOOLS.keys())}\"`",
    - "**Đưa lỗi vào History (dòng 302):** Chuỗi lỗi được đẩy vào `history` như một `Observation` bình thường.",
    - "**Cơ chế Self-Correction:** Ở lượt tiếp theo, LLM đọc được danh sách công cụ hợp lệ trong Observation và có cơ hội tự chọn lại công cụ đúng."
- **Nguồn:** `Khóa học · Lab 1 dòng 290-295, 302`
- **Ghi chú (`notes`):** Đây là kỹ thuật "Error Feedback Injection". Mọi lỗi nghiệp vụ và lỗi cú pháp đều phải được chuyển hóa thành ngữ cảnh văn bản để LLM tự sửa ở vòng lặp sau.

---

#### Slide 1b.8: Trang sổ tay ghi chép Bài 1b (Paper Notebook 1b)
- **Slide Type:** `notebook`
- **Fields & Content:**
  - `eyebrow`: "Ghi chép cốt lõi"
  - `title`: "Sổ tay phòng chống 4 bẫy ReAct"
  - `page`: "AI Agents 101 · Bài 1b"
  - `lines`:
    - "# 4 Bẫy chết người cần tránh"
    - "! 1. Regex ngoặc lồng: lazy matching cắt cụt (2+3)*4 thành (2+3)"
    - "! 2. LLM bịa Observation: luôn kiểm tra stop_sequences=['Observation:']"
    - "! 3. Ô nhiễm State: reset biến đếm step trước mỗi lần agent.run()"
    - "! 4. Tool lạ: bắt lỗi tại biên, trả danh sách tool hợp lệ vào Observation"
    - "# Nguyên tắc chuyển dịch kiến trúc"
    - "@ Regex Parser chỉ dùng cho đồ chơi; Production bắt buộc dùng JSON Tool Calling!"
- **Nguồn:** `ROADMAP.md mục 4 (M1, M2)` & `Khóa học · Lab 1`
- **Ghi chú (`notes`):** Học viên chép 6 dòng cảnh báo này vào sổ tay để làm kim chỉ nam khi tự viết file `my_react.py`.

---

#### Slide 1b.9: Luyện tập 1 (Easy) — Vá lỗi Regex Parser
- **Slide Type:** `exercise`
- **Fields & Content:**
  - `eyebrow`: "Luyện tập thực hành (Cấp độ 1/3)"
  - `title`: "Bài tập: Bóc tách tham số ngoặc an toàn"
  - `level`: `"easy"`
  - `problem`: "Viết hàm `extract_action(text: str) -> tuple[str, str]` bóc tách chính xác tên tool và tham số cho chuỗi `Action: calculate[(2 + 3) * 4]`, không bị cắt cụt như Lab 1."
  - `time`: 120
  - `hints`:
    - "Thay vì dùng regex `(.*?)` với tập kết thúc chứa cả `)` và `]`, hãy tìm vị trí của dấu mở ngoặc đầu tiên `[` và dấu đóng ngoặc cuối cùng `]`.",
    - "Sử dụng phương thức `text.find('[')` và `text.rfind(']')`."
  - `solution`:
    - "Tìm tiền tố: `if 'Action:' not in text: return None, None`",
    - "Lấy phần sau Action: `action_part = text.split('Action:')[1].strip()`",
    - "Tìm cặp ngoặc ngoài cùng: `start = action_part.find('['); end = action_part.rfind(']')`",
    - "Trích xuất an toàn: `tool_name = action_part[:start].strip(); tool_arg = action_part[start+1:end].strip()`"
  - `answer`: "Hàm xử lý chuỗi bằng `rfind(']')` bóc tách chính xác `calculate` và `(2 + 3) * 4`."
- **Nguồn:** `Khóa học · Lab 1 dòng 147-151` & `ROADMAP.md mục 4 (M1)`
- **Ghi chú (`notes`):** Rèn luyện tư duy xử lý chuỗi biên giới hạn mà không bị phụ thuộc vào regex đơn giản.

---

#### Slide 1b.10: Luyện tập 2 (Medium) — Chống bẫy Observation tự bịa
- **Slide Type:** `exercise`
- **Fields & Content:**
  - `eyebrow`: "Luyện tập thực hành (Cấp độ 2/3)"
  - `title`: "Bài tập: Vô hiệu hóa Observation bịa đặt"
  - `level`: `"medium"`
  - `problem`: "Nếu LLM sinh ra phản hồi chứa cả `Action: ...` và `Final Answer: ...` trong CÙNG một lượt, hãy thiết kế điều kiện trong `ReActParser` hoặc `ReActAgent` để đảm bảo Action luôn được thực thi trước khi chấp nhận Final Answer."
  - `time`: 180
  - `hints`:
    - "Trong `ReActParser.parse`, đừng kiểm tra `Final Answer` đầu tiên nếu văn bản phía trên nó có chứa từ khóa `Action:` chưa được thực thi.",
    - "Hoặc trong vòng lặp agent, nếu cả `tool_name` và `final_answer` cùng tồn tại, hãy xóa `final_answer` và ép chạy tool trước."
  - `solution`:
    - "Bước 1: Quét `action_match` trước `final_ans_match`.",
    - "Bước 2: Nếu có `Action:`, chỉ trích xuất `thought`, `tool_name`, `tool_arg` và trả về `final_answer = None`.",
    - "Bước 3: Chỉ khi văn bản KHÔNG chứa `Action:` mới bóc tách `Final Answer:`."
  - `answer`: "Đảo ngược thứ tự ưu tiên: Ưu tiên Action chưa chạy lên trước Final Answer để chặn ảo giác."
- **Nguồn:** `Khóa học · Lab 1 dòng 135-161, 274-286`
- **Ghi chú (`notes`):** Giúp học viên hiểu sâu sắc về luồng kiểm soát an toàn (Control Flow Guardrails).

---

#### Slide 1b.11: Luyện tập 3 (Hard) — Đặc tả DoD cho my_react.py
- **Slide Type:** `exercise`
- **Fields & Content:**
  - `eyebrow`: "Thử thách tự viết mã (Cấp độ 3/3)"
  - `title`: "Bài tập lớn: Tự viết my_react.py từ file trống"
  - `level`: `"hard"`
  - `problem`: "Tự tạo file `03_Materials_Code/my_work/my_react.py` không nhìn code mẫu Lab 1. Hệ thống của bạn phải vượt qua **4 bài kiểm tra Assertions (Definition of Done)** sau đây:\n\n1. `assert res['steps'] <= max_steps` (Chặn lặp vô hạn)\n2. `assert 'Error' in unknown_tool_obs` (Bắt tool lạ, trả observation lỗi)\n3. `assert run_count_independent` (Reset state giữa các lần gọi)\n4. `assert parse_nested_bracket` (Parse đúng biểu thức `[(2+3)*4]`)"
  - `time`: 300
  - `hints`:
    - "Xây dựng 2 tool cơ bản: 1 tool tính toán số học, 1 tool tra cứu từ điển.",
    - "Tạo một Mock LLM đơn giản mô phỏng 3 kịch bản kiểm thử.",
    - "Thiết kế class `ReActAgent` nhận `max_iterations` và quản lý `history` cục bộ bên trong hàm `run()`."
  - `solution`:
    - "Tuân thủ quy tắc AGENTS.md: Người học tự viết code, DeepTutor chỉ cung cấp tiêu chuẩn nghiệm thu (DoD) và gợi ý xử lý ngoại lệ.",
    - "Khi viết xong, chạy kiểm tra: `py -3.11 -m pytest my_react.py` hoặc chạy script test 4 asserts."
  - `answer`: "Bộ mã nguồn `my_react.py` hoàn chỉnh vượt qua trọn vẹn 4/4 asserts."
- **Nguồn:** `AGENTS.md` & `ROADMAP.md mục 3.2 (Tuần 3), 4 (M1)`
- **Ghi chú (`notes`):** Tuyệt đối không cung cấp mã giải sẵn theo quy tắc của `AGENTS.md`. Tiêu chuẩn nghiệm thu 4 assert là thước đo duy nhất để đánh dấu hoàn thành bài thực hành.

---

#### Slide 1b.12: Thẻ ghi nhớ ôn tập (Flashcards)
- **Slide Type:** `flashcards`
- **Fields & Content:**
  - `eyebrow`: "Ôn tập chủ động"
  - `title`: "Lật thẻ củng cố kiến thức Lab 1"
  - `cards`:
    - `{"front": "ReActParser.parse trả về mấy giá trị?", "back": "4 giá trị: (thought, tool_name, tool_arg, final_answer).", "icon": "ph:brackets-curly-duotone"}`
    - `{"front": "Vì sao Action: calculate[(2+3)*4] bị lỗi trong Lab 1?", "back": "Regex lười (.*?) dừng ngay tại dấu đóng ngoặc tròn đầu tiên, cắt cụt biểu thức.", "icon": "ph:warning-duotone"}`
    - `{"front": "Biện pháp phòng ngừa LLM tự bịa Observation?", "back": "Cài đặt stop_sequences tại 'Observation:' và ưu tiên bóc tách Action trước Final Answer.", "icon": "ph:shield-check-duotone"}`
    - `{"front": "Khi LLM gọi tool không tồn tại, code cần làm gì?", "back": "Không để crash, trả thông báo lỗi có cấu trúc kèm danh sách tool hợp lệ vào Observation.", "icon": "ph:wrench-duotone"}`
- **Nguồn:** `Khóa học · Lab 1` & `ROADMAP.md mục 4 (M1)`
- **Ghi chú (`notes`):** Học viên lật từng thẻ để củng cố các điểm chốt trước khi làm câu hỏi tổng kết.

---

#### Slide 1b.13: Bài tập điền khuyết (Cloze Test)
- **Slide Type:** `cloze`
- **Fields & Content:**
  - `eyebrow`: "Kiểm tra ghi nhớ"
  - `title`: "Điền từ vào nguyên lý ReAct"
  - `text`: "Trong mô hình ReAct, LLM cung cấp năng lực [[suy luận]], nhưng chính các công cụ định nghĩa phạm vi [[hành động]].\n\nKhi trích xuất lệnh từ văn bản thô, phương pháp [[Regex]] rất dễ vỡ trước các biểu thức phức tạp. Vì vậy, các hệ thống sản xuất chuyển sang dùng [[JSON Schema]] và Tool Calling có kiểm tra kiểu dữ liệu."
- **Nguồn:** `Khóa học · transcript 02:13-02:17` & `ROADMAP.md mục 4 (M1, M2)`
- **Ghi chú (`notes`):** Khắc sâu sự đối chiếu giữa 2 nửa: Suy luận (LLM) vs Hành động (Tool); Regex (thô sơ) vs JSON Schema (chuyên nghiệp).

---

#### Slide 1b.14: Đúc kết & Động lực bước sang Module 2 (Summary & Bridge to M2)
- **Slide Type:** `summary`
- **Fields & Content:**
  - `eyebrow`: "Tổng kết Module 1"
  - `title`: "Tạm biệt Regex, Tiến lên JSON Tool Calling!"
  - `items`:
    - "Bạn đã làm chủ cơ chế máy trạng thái và luồng điều phối của ReAct Agent",
    - "Đã nhận diện và biết cách khắc chế 4 bẫy nguy hiểm: Ngoặc lồng, Ảo giác Observation, Ô nhiễm State, và Tool lạ",
    - "Nhiệm vụ tuần này: Hoàn thành `my_react.py` đạt 4/4 asserts theo đúng DoD",
    - "**Động lực Module 2:** Tại sao phải khổ sở viết regex khi ta có thể ép LLM sinh trực tiếp `tool_calls` chuẩn JSON Schema có xác thực kiểu dữ liệu? Hẹn gặp lại ở Module 2!"
  - `score`: `true`
- **Nguồn:** `ROADMAP.md mục 4 (M1, M2)` & `Khóa học · transcript 05:44-06:49`
- **Ghi chú (`notes`):** Tạo cầu nối tự nhiên và hào hứng dẫn dắt học viên bước sang Module 2: Tool calling và Type-safe JSON Schema.

---

## Phần C: Danh Mục Các Điểm Chưa Rõ / Cần Xác Minh Trong Nguồn (Ambiguities & Unverifiable Items)

Qua quá trình đối soát chéo giữa mã nguồn, video transcript và các ghi chú, phát hiện các điểm không nhất quán sau:

1. **Sự không nhất quán về giới hạn vòng lặp (`max_iterations` vs `SYSTEM_PROMPT`):**
   - Trong mã nguồn [01_pure_react_agent.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/01_pure_react_agent.py#L124), dòng 124 của `SYSTEM_PROMPT` hướng dẫn LLM: `... (this Thought/Action/Observation sequence can repeat up to 5 times)`.
   - Tuy nhiên, tại dòng 245, khởi tạo `ReActAgent.__init__` lại đặt mặc định `max_iterations: int = 6`.
   - *Phân loại:* Khóa học · Bất đồng bộ nội bộ mã nguồn Lab 1.

2. **Kịch bản thiếu từ khóa trong Mock LLM (`DeterministicMockLLM`):**
   - Trong [01_pure_react_agent.py](file:///D:/02_Learning_Knowledge/AMD_AI_Academy_AI_Agents_101/03_Materials_Code/01_pure_react_agent.py#L178-L237), cơ sở tri thức `tool_search_knowledge_base` có tài liệu về `"react"` (dòng 82-86), nhưng bộ định tuyến `DeterministicMockLLM.generate` chỉ kiểm tra các từ khóa `cluster`, `ryzen`, `tops`, `rocm`, `mi300x`.
   - Khi người dùng hỏi `"What is ReAct?"`, mock lọt vào nhánh `else` và tìm `"four pillars"` thay vì `"react"`.
   - *Phân loại:* Khóa học · Logic mock cố định của Lab 1.

3. **Thuật toán tìm kiếm trong Lab 3 bị đặt tên quá mức:**
   - Trong `03_Materials_Code/README.md` (dòng 13, 116), tài liệu ghi Lab 3 dùng "TF-IDF Episodic Search", nhưng thực tế mã nguồn chỉ cài đặt Cosine Similarity trên tần suất từ thô (Term Frequency), hoàn toàn không tính trọng số nghịch đảo tần suất văn bản (Inverse Document Frequency - IDF).
   - *Phân loại:* Ghi chú AI cũ mở rộng sai lệch so với mã nguồn thực tế.

4. **Thời hạn chính thức của khóa học trên AMD AI Academy:**
   - Trang web AMD AI Academy không công bố thời hạn đóng khóa học hay ngày hết hạn chứng nhận. Các mốc thời gian trong `ROADMAP.md` (từ Tuần 1 đến Tuần 16) là lịch học cá nhân tự đặt của học viên để phối hợp nhịp nhàng với kỳ thi GCI.
   - *Phân loại:* chưa xác minh (thông tin quản trị bên ngoài).

---

REPORT
STATUS: done
SUMMARY: Đã hoàn thành đề cương slide chi tiết, chính xác 100% theo từng dòng code và transcript cho Course Plan, Lesson 1a và Lesson 1b của Module 1, sẵn sàng chuyển giao để dựng slide Aurora.
CHANGED: none
CHECKS: Đối soát chéo từng dòng mã nguồn trong 01_pure_react_agent.py (dòng 23-337), mốc thời gian transcript.md (00:00-10:14), bảng lịch trình và các bẫy kỹ thuật trong ROADMAP.md.
BLOCKERS: none
