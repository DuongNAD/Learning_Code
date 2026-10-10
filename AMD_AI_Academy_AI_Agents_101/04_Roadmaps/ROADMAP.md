# Lộ trình AMD AI Academy - AI Agents 101 (phiên bản 2, cập nhật 2026-10-10)

> Học xong, bạn tự dựng được một AI agent (tác tử AI: chương trình để LLM tự quyết định gọi công cụ trong một vòng lặp) chạy trên LLM mã nguồn mở qua API tương thích OpenAI, mở rộng bằng MCP server, biết khi nào không nên dùng agent và cách đặt rào chắn an toàn. File: `AMD_AI_Academy_AI_Agents_101/04_Roadmaps/ROADMAP.md`, thay cho [AI_Agents_Mastery_Roadmap.md](AI_Agents_Mastery_Roadmap.md). Nguồn sự thật (source of truth): lời tiếng Anh trong [transcript.md](../02_Notes_Summaries/transcript.md) và notebook chính thức "AI agent with MCPs using vLLM and PydanticAI" (AMD AI Developer Hub, tác giả Mahdi Ghodsi). Ghi chú khác trong thư mục do AI sinh ngày 2026-09-22, chỉ dùng có chọn lọc (mục 8).

## Mục lục

- [1. Cách dùng lộ trình này](#1-cách-dùng-lộ-trình-này)
- [2. Bức tranh toàn cảnh](#2-bức-tranh-toàn-cảnh)
- [3. Trạng thái hiện tại và lịch](#3-trạng-thái-hiện-tại-và-lịch)
- [4. Các module](#4-các-module) (M0-M9)
- [5. Ôn tập giãn cách và ôn xen kẽ](#5-ôn-tập-giãn-cách-và-ôn-xen-kẽ)
- [6. Dự án tổng hợp](#6-dự-án-tổng-hợp)
- [7. Sổ lỗi và cách hỏi DeepTutor](#7-sổ-lỗi-và-cách-hỏi-deeptutor)
- [8. Tài liệu cũ trong thư mục này](#8-tài-liệu-cũ-trong-thư-mục-này)
- [9. Theo dõi tiến độ](#9-theo-dõi-tiến-độ)
- [10. Nguồn tham khảo](#10-nguồn-tham-khảo)

## 1. Cách dùng lộ trình này

**Nhãn:** **[Khóa học]** có trong video hoặc notebook chính thức; **[Mở rộng]** không có trong video, nguồn ngoài đã kiểm tra 2026-10-10; **(chưa xác minh)** chưa kiểm chứng được, đừng coi là sự thật.

**Vòng lặp một module:** (1) tự chấm 0-2 từng dòng "Đầu ra"; (2) xem đoạn video, đối chiếu lời tiếng Anh trong transcript; (3) đọc "Kiến thức cốt lõi": mô hình tư duy trước, API sau; (4) predict-then-run (dự đoán rồi mới chạy): ghi dự đoán trước mọi lệnh, chỗ lệch là chỗ đáng học; (5) thực hành 3 tầng trong time box, lên tầng khi đạt DoD (Definition of Done: tiêu chí hoàn thành kiểm tra được); (6) viết câu trả lời rồi mới mở "Đáp án"; câu sai -> Sổ lỗi (mục 7) -> lịch ôn (mục 5).

**Buổi 60 phút:** 0-5 ôn câu đến hạn; 5-15 video/tài liệu; 15-50 thực hành một tầng (kẹt quá 15 phút thì hỏi DeepTutor, mục 7); 50-57 tự kiểm tra, Sổ lỗi; 57-60 ghi điểm dừng và việc kế tiếp. **Buổi 30 phút:** 5 phút ôn + một việc nhỏ (một tài liệu hoặc tầng Khởi động). Buổi lab có thể 90 phút.

## 2. Bức tranh toàn cảnh

### 2.1 Năng lực đầu ra

1. Vẽ vòng lặp agent như state machine (máy trạng thái) có điều kiện dừng và ngân sách; chỉ rõ phần LLM làm, phần code làm.
2. Thiết kế tool như hợp đồng có kiểu (typed contract): tên, mô tả, JSON Schema (lược đồ kiểu dữ liệu JSON); kiểm tham số lúc chạy; trả lỗi có cấu trúc để mô hình tự sửa.
3. Nối agent với MCP server (Model Context Protocol: giao thức chuẩn để agent khám phá và gọi tool) và tự viết một server nhỏ.
4. Phục vụ LLM mã nguồn mở qua API tương thích OpenAI (Ollama trên máy bạn, vLLM trên Linux/GPU AMD); giải thích vai trò của ROCm và MI300X như khóa học trình bày.
5. Chọn đúng: một lần gọi LLM, workflow (luồng do code định sẵn) hay agent; framework hay code thuần.
6. Chặn vòng lặp vô hạn, tham số tool bịa, prompt injection (chèn chỉ thị độc vào dữ liệu mô hình đọc), chi phí bùng nổ; đo bằng một bộ eval (bài kiểm tra tự động) nhỏ.

### 2.2 Bản đồ module

```mermaid
flowchart TD
    subgraph A["Giai đoạn A - lõi khóa học, tuần 1-12"]
        M0["M0 Khởi động"] --> M1["M1 Agent và vòng lặp ReAct"]
        M1 --> M2["M2 Tool calling và schema"]
        M2 --> M3["M3 Memory và state"]
        M2 --> M4["M4 MCP"]
        M1 --> M5["M5 Suy luận mã nguồn mở và AMD ROCm"]
        M4 --> M6["M6 Lab chính thức PydanticAI + MCP"]
        M5 --> M6
    end
    subgraph B["Giai đoạn B - mở rộng, tuần 12-16"]
        M7["M7 Patterns, framework hay code thuần"]
        M9["M9 Đánh giá, an toàn, guardrails"]
        CAP["Dự án tổng hợp"]
        M8["M8 RAG - tùy chọn"]
    end
    M6 --> M7
    M3 --> M7
    M6 --> M9
    M7 --> M9
    M9 --> CAP
    M3 -.-> M8
```

Mũi tên liền: bắt buộc; mũi tên chấm: tùy chọn. Giai đoạn A bám video và notebook chính thức; giai đoạn B là phần mở rộng.

### 2.3 Kiến thức nền cần có

- Python: hàm, type hints, decorator, exception, `async`/`await` (PydanticAI và MCP dùng async). Hổng thì ôn ở [Python_Master](../../Python_Master/), đừng học lại ở đây.
- PowerShell, biến môi trường, git cơ bản.
- LLM: token, context window (lượng token tối đa mô hình đọc trong một lần gọi), sinh token tự hồi quy, temperature. Mơ hồ thì đọc [Stage_01 notes](../../Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_01_Tokenizer_Data/notes.md) và [Stage_04 notes](../../Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_04_Full_Transformer/notes.md) của LLM From Scratch (20 phút).

**Tự kiểm tra nhanh** (sai từ 2 câu thì ôn nền trước khi vào M1)
1. `@register(name="calc")` đặt trên `def f(...)` tương đương câu lệnh nào?
2. Với `async def f()`, gọi `f()` mà không `await` thì nhận được gì?
3. `$env:PYTHONUTF8 = "1"` trong một cửa sổ PowerShell có ảnh hưởng tới cửa sổ khác, tới tiến trình con không?
4. Vì sao cùng một prompt, LLM có thể trả lời khác nhau giữa hai lần chạy?

<details><summary>Đáp án</summary>

1. `f = register(name="calc")(f)`; Lab 2 dùng đúng mẫu này cho `ToolRegistry.register`.
2. Một coroutine object, thân hàm chưa chạy; cần `await f()` hoặc `asyncio.run(f())`.
3. Chỉ cửa sổ hiện tại và tiến trình con khởi chạy từ đó; đóng cửa sổ là mất.
4. Mô hình lấy mẫu token từ phân phối xác suất; temperature lớn hơn 0 làm kết quả ngẫu nhiên. Vì vậy mỗi ca kiểm thử agent phải chạy nhiều lần (M9).

</details>

### 2.4 Ngân sách thời gian

GCI (P0) nặng nhất từ 2026-10-29 tới 2026-12-17 (thi đấu, bài cuối khóa), nên tới 2026-12-20 khóa này chỉ chiếm 1-2 giờ/tuần: Thứ Bảy 60 phút + Thứ Ba 30 phút (tránh Thứ Năm, ngày học GCI). Từ 2026-12-21 khoảng 3 giờ/tuần (Ba, Năm, Bảy, mỗi buổi 60 phút). Tổng lõi khoảng 29,5 giờ trong 15 tuần, thêm 2 giờ M8 tùy chọn. Ưu tiên P2: trùng việc GCI thì bỏ buổi AMD trước và dời cả bảng.

## 3. Trạng thái hiện tại và lịch

### 3.1 Bạn đang ở đây

- **Đã có** (nguồn: TASKS.md, .agents/ORIGINAL_REQUEST.md, transcript.md, git log): bản ghi video [01_AI_Agents_101_Full.mov](../01_Recordings/01_AI_Agents_101_Full.mov) (lời giảng khoảng 10 phút 14 giây, phần sau là màn hình SCORM tĩnh). Ngày 2026-09-22 một quy trình AI sinh ghi chú, 4 lab, quiz, README theo [ORIGINAL_REQUEST.md](../.agents/ORIGINAL_REQUEST.md); yêu cầu này tự đặt ra "4 trụ cột" và phần Ryzen AI/Radeon. Các ô `[x]` trong [TASKS.md](../TASKS.md) ghi nhận việc tạo tài liệu, không chứng minh bạn đã học hay tự chạy. Note RAG (2026-09-26) tổng hợp từ video của Việt Nguyễn AI, không thuộc khóa AMD.
- **Quá hạn tại 2026-10-10:** quiz (09-29), rà transcript (09-30), verify_labs (09-30, P1, cũng có trong ACTIVE_LEARNING.md), tích hợp tool (10-01), HITL (10-03), bộ nhớ dài hạn (10-05), supervisor-worker (10-07), đo ROCm/vLLM (10-09). Lộ trình mới xử lý: transcript và verify_labs -> M0; tích hợp tool -> M1-M2; bộ nhớ -> M3, M8; supervisor-worker -> M7; HITL -> M9; đo hiệu năng -> M5 trên máy bạn; quiz -> các buổi ôn xen kẽ.
- **Kiểm tra khi biên soạn** (trên bản sao ở thư mục tạm, không phải tiến độ của bạn): 4 lab là code tham chiếu hoàn chỉnh, "LLM" trong đó là bộ giả lập theo kịch bản; chỉ cần thư viện chuẩn (`pydantic` được import mà không dùng). `verify_labs.py` (Python 3.11.9, Windows) mặc định 4/4 FAIL vì `UnicodeEncodeError`; đặt `PYTHONUTF8=1` thì 4/4 PASS.
- **Hạn chính thức:** không tìm thấy; trang công khai AMD AI Academy không liệt kê tên khóa (thời hạn truy cập academy.amd.com: chưa xác minh). Hạn dưới đây là tự đặt, trừ hạn GCI: HW3 22/10 18:00 đã xác minh trong notebook HW3; lịch và hạn GCI khác xem [lộ trình GCI](../../GCI_World_2026_September/roadmap/ROADMAP.md).

### 3.2 Lịch theo tuần (từ thứ Hai 2026-10-12)

| Tuần | Buổi | Module | Sản phẩm / DoD | Hạn |
|---|---|---|---|---|
| 1 | Ba 10-13 (60'), Bảy 10-17 (60') | M0; bắt đầu M1 | verify_labs 4/4 PASS; tóm tắt 12 dòng | 2026-10-17 (thay hạn cũ 09-30) |
| 2 | Ba 10-20 (30'), Bảy 10-24 (60') | M1 | Bảng dự đoán/kết quả Lab 1 | **Hạn thật GCI 10-22 18:00** (HW3 P0) |
| 3 | Ba 10-27 (30'), Bảy 10-31 (60') | M1 xong; M2 | `my_react.py` qua 4 assert | 10-31 (M1) |
| 4 | Bảy 11-07 (60') | M2 | Dự đoán 3 lời gọi dispatch | GCI 11-05 18:00: HW5 và survey Buổi 6 (hạn suy ra theo quy tắc 2 tuần); hạn Final Assignment chưa công bố |
| 5 | Ba 11-10 (30'), Bảy 11-14 (60') | M2 xong | `my_tools.py` qua 8 assert | 11-14 (M2) |
| 6 | Ba 11-17 (30'), Bảy 11-21 (60') | M3 | `context_manager.py` | 11-21 (M3) |
| 7 | Ba 11-24 (30'), Bảy 11-28 (60') | Ôn xen kẽ 1; M4 | Sơ đồ host-client-server | |
| 8 | Ba 12-01 (30'), Bảy 12-05 (60') | M4 | `tools/list` qua MCP Inspector | |
| 9 | Ba 12-08 (30'), Bảy 12-12 (60') | M4 xong; M5 | Endpoint Ollama trả `tool_calls` | 12-08 (M4) |
| 10 | Bảy 12-19 (60') | M5 xong | Bảng tính TPS, KV cache | 12-19 (M5) |
| 11 | Ba 12-22, Năm 12-24, Bảy 12-26 | M6 bước 1-6 | Trace câu hỏi Vancouver | |
| 12 | Ba 12-29, Năm 12-31, Bảy 2027-01-02 | M6 bước 7; Ôn 2; M7 | DoD thử thách weather | 12-29 (M6, mốc A) |
| 13 | Ba 01-05, Năm 01-07, Bảy 01-09 | M7 xong; M9 | `mini_graph.py`; threat model | 2027-01-07 (M7) |
| 14 | Ba 01-12, Năm 01-14, Bảy 01-16 | M9 xong; Ôn 3; dự án | Guardrails + eval 10 ca | 2027-01-14 (M9) |
| 15 | Ba 01-19, Năm 01-21, Bảy 01-23 | Dự án; tổng kết | Eval 12 câu đạt từ 10/12 | 2027-01-23 (mốc cuối) |
| 16 | Ba 01-26, Năm 01-28 | M8 (tùy chọn) | Bảng hit@3 | 2027-01-28 |

## 4. Các module

### Module 0 - Khởi động: môi trường, video, bản đồ khóa học (ước lượng: 1,5 giờ, tuần 1)

**Vì sao học:** Cần môi trường chạy được và một nguồn sự thật rõ ràng; thư mục này trộn nội dung khóa học với nội dung AI thêm vào.

**Đầu ra (làm được sau module):**
- Chạy `verify_labs.py` 4/4 PASS, giải thích vì sao lần chạy mặc định trên Windows FAIL.
- Kể lại 12 phần của bài giảng; chỉ ra 3 khẳng định trong ghi chú không có trong video.

**Kiến thức cốt lõi**
- **Bản đồ thật [Khóa học]:** demo Browser Use (agent tìm công thức chili, bỏ nguyên liệu vào giỏ) -> LLM khác agent -> ReAct -> framework (chọn PydanticAI; nhắc LangGraph, OpenAI SDK, CrewAI) -> MCP -> suy luận mã nguồn mở (vLLM, SGLang; Qwen3, GPT-OSS, DeepSeek) trên GPU AMD -> lab vLLM + PydanticAI + MCP time/Airbnb -> thử thách weather MCP -> tổng kết. Không có trong video: "4 trụ cột", bộ nhớ 4 tầng, Reflexion, multi-agent, RAG, Ryzen AI NPU, RX 7900 XTX, MI325X.
- **Môi trường:** lab chỉ cần Python 3.11.9 có sẵn. venv (môi trường ảo) cần từ M4, đặt trên ổ C: vì SSD D: là exFAT cluster 512 KB (mỗi file nhỏ chiếm ít nhất một cluster).

```powershell
cd D:\02_Learning_Knowledge\AMD_AI_Academy_AI_Agents_101\03_Materials_Code
$env:PYTHONUTF8 = "1"; py -3.11 verify_labs.py
py -3.11 -m venv C:\venvs\amd-agents   # dùng từ M4
```

- **Vì sao FAIL:** verify_labs chạy lab qua `subprocess.run(..., capture_output=True)`; stdout là pipe nên Python 3.11 dùng cp1252, emoji gây `UnicodeEncodeError`. `-X utf8` chỉ áp cho tiến trình cha; biến `PYTHONUTF8=1` thì tiến trình con kế thừa. Python 3.15 bật UTF-8 mode mặc định (PEP 686). verify_labs chỉ kiểm cú pháp, exit code và vài chuỗi in ra.
- **API key:** lab không cần khóa; Ollama local bỏ qua khóa. Khóa cloud để trong `03_Materials_Code/.env` (`.gitignore` gốc đã có `.env`, `**/.env`, `.env.*`), nạp bằng `python-dotenv`, chạy `git check-ignore -v` trước khi commit, không in ra notebook hay chat; lộ thì thu hồi. File mẫu nên tên `env.example` vì `.env.*` cũng bị bỏ qua.

**Hiểu lầm và lỗi hay gặp:**
- "verify_labs PASS là agent đúng" -> chỉ kiểm chuỗi in ra từ kịch bản -> đọc `test_assertions`.
- "Ghi chú dài = nội dung khóa học" -> phần lớn do AI mở rộng -> tìm câu đó trong lời tiếng Anh của transcript.
- "Gõ `python3` như README" -> cú pháp macOS/Linux -> trên Windows dùng `py -3.11`.

**Tài liệu**
- Trong thư mục: transcript, mục lục và Phần 12 (15 phút); video 00:00-10:14 (10 phút); [verify_labs.py](../03_Materials_Code/verify_labs.py) (5 phút).
- Bên ngoài: [AMD notebook](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/build_airbnb_agent_mcp.html) - Prerequisites, 7 bước (10 phút); [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) (5 phút); [AMD AI Academy](https://developer.amd.com/academy) - track, chứng nhận (5 phút, tùy chọn).

**Thực hành**
- Khởi động (15 phút): dự đoán số lab PASS khi không đặt biến; chạy. DoD: dự đoán, kết quả, giải thích 2 câu.
- Cốt lõi (45 phút): chạy tới 4/4 PASS; xem video kèm transcript, viết 12 dòng tóm tắt; đánh dấu 3 khẳng định không có trong video. DoD: log PASS, 12 dòng, 3 khẳng định có vị trí.
- Thử thách: PASS mà không đặt biến trong shell (gợi ý: tham số nào của `subprocess.run` quyết định môi trường của tiến trình con?). DoD: PASS trong cửa sổ mới, ghi vào Sổ lỗi.

**Tự kiểm tra**
1. (Nhớ) Video có bao nhiêu phút lời giảng, phần còn lại là gì?
2. (Giải thích) Vì sao `-X utf8` vẫn FAIL còn `PYTHONUTF8=1` thì PASS?
3. (Dự đoán) Chạy thẳng `py -3.11 01_pure_react_agent.py` trong cửa sổ PowerShell (không pipe): có lỗi mã hóa không?
4. (Áp dụng) Đặt API key cloud ở đâu, kiểm tra gì trước khi commit?
5. (Giải thích) Vì sao không tạo venv trên SSD D:?

<details><summary>Đáp án</summary>

1. Khoảng 10 phút 14 giây; từ khoảng 10:30 tới 19:28 là màn hình SCORM tĩnh.
2. `-X utf8` chỉ áp cho tiến trình cha; lab chạy ở tiến trình con có stdout là pipe; biến môi trường thì tiến trình con kế thừa.
3. Thường là không: console thật được ghi bằng API Unicode của Windows; lỗi xuất hiện khi stdout là pipe. Chạy thử để kiểm.
4. Trong `.env`, nạp bằng `python-dotenv`; chạy `git check-ignore -v` và `git status` trước khi commit.
5. Cluster 512 KB: venv có hàng nghìn file nhỏ, mỗi file chiếm ít nhất một cluster.

</details>

**Checkpoint:** [ ] verify_labs 4/4 PASS và giải thích được lỗi; [ ] 12 dòng tóm tắt; [ ] Sổ lỗi có mục đầu; [ ] đúng từ 4/5 câu.

### Module 1 - Agent là gì: LLM + tools + vòng lặp ReAct (ước lượng: 3 giờ, tuần 1-3)

**Vì sao học:** Phần 1-3 đặt mọi thứ trên một ý: LLM suy luận, tool tạo hành động, vòng lặp nối hai thứ; framework nào cũng chỉ đóng gói vòng lặp này.

**Đầu ra (làm được sau module):**
- Vẽ từ trí nhớ state machine của vòng lặp agent, có điều kiện dừng và ngân sách.
- Đọc trace (nhật ký từng bước) của Lab 1, chỉ ra phần do "LLM" sinh và phần do code tạo.
- Viết lại vòng lặp ReAct từ file trống với mock LLM.

**Kiến thức cốt lõi**
- **Trực giác [Khóa học]:** LLM như cuốn sách rất thông minh, trả lời được nhưng không tự làm gì; agent dùng LLM làm bộ não và gắn tool, cùng bộ não khác bộ tool thì khác năng lực (01:05-02:11). Câu chốt: "LLMs provide the reasoning, but the tools define the actions" (02:13). Không có tool, câu "Hôm nay ngày mấy?" bị trả lời sai (06:03).
- **ReAct:** xen kẽ suy luận và hành động, xem kết quả, lặp tới khi đạt mục tiêu (02:21-03:07). Bài báo gốc (Yao và cộng sự, ICLR): giảm ảo giác so với chain-of-thought (chuỗi suy luận không hành động) trên HotpotQA, FEVER; hơn imitation/reinforcement learning 34% và 10% tỉ lệ thành công tuyệt đối trên ALFWorld, WebShop.
- **State machine:** state là danh sách messages do code giữ; mô hình không nhớ gì giữa hai lần gọi; LLM chỉ đề xuất, code chạy tool và quyết định dừng.

```mermaid
flowchart TD
    S(["Nhận mục tiêu"]) --> P["Gọi LLM: messages + tools"]
    P --> D{"Có tool call?"}
    D -->|"Không"| F(["Trả lời cuối"])
    D -->|"Có"| V{"Tool hợp lệ, tham số đúng?"}
    V -->|"Không"| E["Thêm lỗi có cấu trúc"]
    V -->|"Có"| X["Code chạy tool, thêm observation"]
    E --> G{"Còn ngân sách?"}
    X --> G
    G -->|"Còn"| P
    G -->|"Hết"| H(["Dừng, báo thất bại, giữ trace"])
```

- **Chi phí:** mỗi lượt gửi lại toàn bộ lịch sử; prompt đầu $p$ token, mỗi bước thêm $k$, $T$ bước thì tổng token đầu vào là $Tp + k\frac{T(T-1)}{2}$ (với $p=1500$, $k=400$, $T=10$: 33.000), tăng gần bậc hai theo $T$.
- **Lab 1:** `DeterministicMockLLM` trả lời theo bộ đếm bước và từ khóa, không đọc prompt; `ReActParser` dùng regex; `max_iterations=6`.

**Hiểu lầm và lỗi hay gặp:**
- "Agent tự chạy tool" -> code thực thi -> tìm dòng `TOOLS[tool_name](tool_arg)` trong Lab 1.
- Không có điều kiện dừng -> vòng lặp vô hạn, đốt tiền -> luôn có `max_steps`.
- Mô hình tự viết "Observation" rồi "Final Answer" -> kết quả dựa trên quan sát bịa -> có câu trả lời mà không tool nào chạy.

**Tài liệu**
- Trong thư mục: transcript Phần 1-3 và 8 (15 phút); [Slide bài 1a](../05_Slides/ai-agents-101/01-vong-lap-agent/index.html) (20 phút); [Slide bài 1b](../05_Slides/ai-agents-101/02-mo-xe-lab-1/index.html) (25 phút); [Lab 1](../03_Materials_Code/01_pure_react_agent.py) (30 phút); [01_foundations_and_agent_architecture.md](../02_Notes_Summaries/01_foundations_and_agent_architecture.md) Chương 4.2 (10 phút); Stage_04 notes, temperature (10 phút).
- Bên ngoài: [ReAct paper (arXiv 2210.03629)](https://arxiv.org/abs/2210.03629) - abstract, Hình 1, Mục 2 (30 phút); [HF Agents Course, Unit 1](https://huggingface.co/learn/agents-course/unit1/introduction) - messages, chat template, Think-Act-Observe (60 phút); [Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents) - "What are agents?" (15 phút).

**Thực hành**
- Khởi động (15 phút): dự đoán số lượt, thứ tự tool, Final Answer của Lab 1 với câu hỏi mặc định và với `--query "What is ReAct?"`; chạy. DoD: bảng dự đoán/thực tế.
- Cốt lõi (2 buổi): dự đoán rồi kiểm trong REPL: parse `Action: calculate[(2+3)*4]`; phản hồi chứa Action + Observation tự bịa + Final Answer; gọi `agent.run()` hai lần cùng mock. Rồi viết từ file trống `03_Materials_Code/my_work/my_react.py` (không mở Lab 1): 2 tool, mock 3 kịch bản. DoD: có `max_steps`; tool lạ trả observation lỗi; không nhận Final Answer đi sau Action chưa chạy; parse đúng ngoặc lồng; 4 `assert` qua.
- Thử thách (sau M5): thay mock bằng mô hình thật qua Ollama, có stop sequence. DoD: 3 câu hỏi, log số bước.

**Tự kiểm tra**
1. (Nhớ) Theo bài giảng, yếu tố nào quyết định agent làm được gì?
2. (Dự đoán) Lab 1 với câu hỏi mặc định: mấy lượt, action nào, con số chính? Với "What is ReAct?" thì sao?
3. (Dự đoán) `Action: calculate[(2+3)*4]` được parse thành tham số gì?
4. (Dự đoán) Phản hồi chứa Action, "Observation: 5" tự bịa và "Final Answer: 5": Lab 1 làm gì?
5. (Dự đoán) Gọi `agent.run()` hai lần với cùng mock: lần hai ra sao?
6. (Áp dụng) $p=1500$, $k=400$, $T=20$: tổng token đầu vào?

<details><summary>Đáp án</summary>

1. Bộ tool được cấp; LLM chỉ là bộ não suy luận.
2. 4 lượt: `lookup_hardware` -> `calculate[8 * 50]` -> `calculate[400 / 18]` -> Final Answer (400 NPU TOPS, khoảng 22,22 lần Apple M3). Với "What is ReAct?", mock trả lời về "four core pillars": "LLM" là kịch bản, không đọc câu hỏi.
3. `"(2+3"` (regex lười dừng ở dấu đóng đầu tiên); calculator báo "'(' was never closed".
4. Trả Final Answer ngay, tool không chạy. Chặn: stop sequence tại "Observation:" hoặc xử lý Action trước.
5. 1 bước, 0 tool, trả ngay Final Answer vì bộ đếm bước chạy tiếp: state phải gắn với từng lần chạy.
6. $30.000 + 400 \times 190 = 106.000$, khoảng 3,2 lần so với $T=10$.

</details>

**Checkpoint:** [ ] state machine từ trí nhớ; [ ] `my_react.py` qua 4 assert; [ ] đúng từ 5/6 câu.

### Module 2 - Tool calling: tool là hợp đồng có kiểu (ước lượng: 3 giờ, tuần 3-5)

**Vì sao học:** Bài giảng gọi việc mô hình tự quyết định gọi hàm là bản chất của tool calling (06:27-06:35); phần lớn lỗi agent nằm ở ranh giới giữa văn bản xác suất và code tất định.

**Đầu ra (làm được sau module):**
- Kể một vòng tool calling: `tools` -> `tool_calls` -> code chạy tool -> message vai trò `tool` -> câu trả lời.
- Viết bộ kiểm tham số theo schema, trả lỗi có cấu trúc.
- Giải thích vì sao chế độ `auto` của vLLM không bảo đảm tham số hợp lệ.

**Kiến thức cốt lõi**
- **Hợp đồng:** schema vừa là tài liệu mô hình đọc (thành token trong prompt), vừa là đặc tả để code kiểm. Tool call là văn bản theo chat template ([Stage_06 notes](../../Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_06_Supervised_FineTuning/notes.md)); vLLM tách nó thành `tool_calls` nhờ `--enable-auto-tool-choice --tool-call-parser hermes`. Anthropic: viết mô tả tool như docstring cho người mới, có ví dụ, ca biên.
- **Bảo đảm (docs vLLM):** ép hàm cụ thể hoặc `tool_choice="required"` thì tham số theo schema (hợp lệ chưa chắc đã tốt); `auto` không có tool `strict` thì đôi khi sai định dạng hoặc vi phạm schema. Constrained decoding (giải mã có ràng buộc) gán logit $-\infty$ cho token phá ngữ pháp: bảo đảm cú pháp, không bảo đảm sự thật.
- **Tự sửa thật:** PydanticAI kiểm tham số theo chữ ký hàm và gửi lỗi lại để mô hình thử lại; tool có thể raise `ModelRetry`; mặc định thử lại 1 lần. Lỗi tốt nêu trường, kiểu mong đợi, giá trị nhận được, giá trị hợp lệ.
- **Lab 2:** Pydantic được import mà không dùng; `enum` không được kiểm; mock luôn "sửa" ở bước 2 bất kể lỗi; API thật còn cần `tool_call_id` để ghép kết quả với lời gọi.

**Hiểu lầm và lỗi hay gặp:**
- "Có schema thì mô hình tuân thủ" -> chỉ chắc khi có giải mã ràng buộc -> đếm tham số sai qua nhiều lần chạy.
- "Kiểm trong thân hàm là đủ" -> lỗi kiểu `'int' object has no attribute 'lower'` không giúp mô hình sửa -> kiểm ở biên.
- Thử lại không giới hạn -> đốt tiền -> đặt số lần thử lại.

**Tài liệu**
- Trong thư mục: transcript 05:44-06:49 và 07:13-08:06 (10 phút); [Lab 2](../03_Materials_Code/02_tool_calling_agent.py) (30 phút); [quiz](../02_Notes_Summaries/quiz_and_assessment.md) Câu 7, đọc phê phán (10 phút).
- Bên ngoài: PydanticAI docs, 2 trang [Function Tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/) và [Advanced Tool Features](https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced/) - schema từ chữ ký, retry (30 phút); [vLLM, Tool Calling](https://docs.vllm.ai/en/latest/features/tool_calling.html) - cờ, `tool_choice`, bảo đảm đầu ra (20 phút).

**Thực hành**
- Khởi động (15 phút): dự đoán `error_type` của `registry.dispatch("query_amd_catalog", ...)` với `product_name=123`, với khóa thừa, khi thiếu `metric`. DoD: dự đoán so với thực tế; viết lại từng thông điệp để mô hình sửa được.
- Cốt lõi (2 buổi): từ file trống `my_work/my_tools.py`, registry lấy schema làm nguồn sự thật; kiểm `required`, kiểu, `enum`, trường lạ; lỗi là dict `error_type`, `field`, `expected`, `got`, `hint`; không dùng thư viện jsonschema, không mở Lab 2. DoD: 8 `assert` qua (hợp lệ, thiếu, sai kiểu, ngoài enum, trường lạ, tool lạ, lỗi nghiệp vụ, timeout giả lập).
- Thử thách (sau M5): gửi tools viết tay tới Ollama `qwen3` với 5 yêu cầu mơ hồ, cho `tool_calls` thô qua bộ kiểm. DoD: bảng số tham số sai và số bị bắt.

**Tự kiểm tra**
1. (Nhớ) Trong tool calling, LLM sinh gì, ai thực thi tool?
2. (Nhớ) `--tool-call-parser hermes` làm gì?
3. (Dự đoán) `dispatch` với `product_name=123` trả gì, vì sao kém?
4. (Giải thích) Vì sao "self-correction" của Lab 2 không thật?
5. (Áp dụng) `get_current_time(timezone="Asia/Hanoi")`: qua schema không, đúng nghĩa không?

<details><summary>Đáp án</summary>

1. Tên tool + tham số JSON; code kiểm, chạy, gửi kết quả lại với vai trò `tool`.
2. Tách tool call định dạng Hermes trong văn bản mô hình sinh thành `tool_calls` có cấu trúc.
3. `AttributeError` với thông điệp `'int' object has no attribute 'lower'`: không nêu trường sai và kiểu mong đợi.
4. Mock luôn đổi sang tham số đúng ở bước 2 mà không đọc lỗi.
5. Qua schema (là string) nhưng sai nghĩa: `zoneinfo` không có "Asia/Hanoi" (đã thử); tên đúng là "Asia/Ho_Chi_Minh"; lỗi tốt nên gợi ý tên đúng.

</details>

**Checkpoint:** [ ] `my_tools.py` qua 8 assert; [ ] đúng từ 4/5 câu.

### Module 3 - Memory và state: context window là bộ nhớ làm việc (ước lượng: 1,5 giờ, tuần 6)

**Vì sao học:** [Mở rộng] Video chỉ lướt qua việc agent tiếp tục hội thoại (06:40-06:45), nhưng vòng lặp sống nhờ danh sách messages; không hiểu context thì không kiểm soát được chi phí.

**Đầu ra (làm được sau module):**
- Giải thích vì sao API LLM là stateless (không giữ trạng thái giữa các lần gọi).
- Chọn chiến lược nhớ cho một tình huống; giải thích vì sao độ tương đồng của Lab 3 thất bại với từ đồng nghĩa.

**Kiến thức cốt lõi**
- **Bảng trắng:** context window là bảng trắng, trọng số là kiến thức cố định, file/database/vector store là sổ tay phải có tool để tra. Anthropic: mỗi token tiêu một phần "attention budget", context càng đầy càng nhớ kém (context rot). Token, attention: [Stage_01](../../Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_01_Tokenizer_Data/notes.md) và [Stage_02](../../Machine_Learning/09_LLM_From_Scratch/01_Hands_On_Practice/Stage_02_Attention/notes.md) notes.
- **Chiến lược:** giữ toàn bộ (chi phí gần bậc hai) -> cửa sổ trượt $K$ lượt -> nén (compaction) phần cũ -> kho thực thể key-value -> ghi chú ngoài, tra khi cần; luôn cắt và làm sạch output tool.
- **Lab 3:** cosine $\cos\theta = \frac{u\cdot v}{\lVert u\rVert\,\lVert v\rVert}$ trên tần suất từ, không có IDF dù README ghi "TF-IDF"; summary chỉ cắt 60 ký tự; câu trả lời cuối là template từ `entity_store`.

**Hiểu lầm và lỗi hay gặp:**
- "Mô hình nhớ cuộc trò chuyện" -> app gửi lại lịch sử -> gọi API không kèm lịch sử là thấy.
- "Context càng dài càng tốt" -> chi phí và context rot -> so độ chính xác với context ngắn và dài.
- "Cosine tần suất từ là tìm kiếm ngữ nghĩa" -> chỉ khớp từ -> thử cặp đồng nghĩa.

**Tài liệu**
- Trong thư mục: [Lab 3](../03_Materials_Code/03_memory_state_agent.py) (25 phút); [02_core_pillars_and_design_patterns.md](../02_Notes_Summaries/02_core_pillars_and_design_patterns.md) mục 1.4, bỏ qua số độ trễ minh họa (10 phút).
- Bên ngoài: [Anthropic, Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (30 phút); [Lilian Weng, LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) - "Component Two: Memory" (15 phút).

**Thực hành**
- Khởi động (15 phút): dự đoán lượt nào bị đẩy khỏi buffer, LAYER 3 có xuất hiện không; chạy Lab 3.
- Cốt lõi (45 phút): từ file trống `my_work/context_manager.py`: giữ system + mục tiêu, $N$ kết quả tool gần nhất, cắt output còn $M$ ký tự, một ô tóm tắt do mock điền; token ước bằng số ký tự chia 4 (heuristic cho tiếng Anh). DoD: test 30 bước dưới ngân sách, fact "tên người dùng" không mất.
- Thử thách (sau M5): thay bằng embedding (véc-tơ biểu diễn nghĩa) qua `/v1/embeddings` của Ollama. DoD: bảng 5 cặp câu, có cặp "GPU memory" / "VRAM capacity".

**Tự kiểm tra**
1. (Giải thích) "Mô hình nhớ cuộc trò chuyện" đúng không?
2. (Dự đoán) Lab 3 sau 3 lượt, buffer 2: lượt nào bị đẩy ra, LAYER 3 có xuất hiện?
3. (Dự đoán) Cosine tần suất từ của "GPU memory" và "VRAM capacity"?
4. (Giải thích) Vì sao context dài hơn không luôn tốt hơn?
5. (Áp dụng) 40 bước, mỗi tool trả 3.000 ký tự HTML: chính sách nào?

<details><summary>Đáp án</summary>

1. Không: mỗi lần gọi độc lập, app gửi lại lịch sử.
2. Lượt 1 vào archive; cosine với lượt 1 vượt ngưỡng 0,05 nên LAYER 3 xuất hiện (đã chạy kiểm).
3. 0,0: không có từ chung.
4. Chi phí, độ trễ tăng; nhớ chính xác giảm khi context đầy.
5. Cắt và làm sạch output, xóa kết quả cũ, nén định kỳ, ghi chú ra file, giữ fact trong kho thực thể.

</details>

**Checkpoint:** [ ] `context_manager.py` qua test 30 bước; [ ] đúng từ 4/5 câu.

### Module 4 - MCP: dây nối chuẩn giữa agent và thế giới (ước lượng: 3 giờ, tuần 7-9)

**Vì sao học:** [Khóa học] Phần 5 và 9-11: MCP là cách lab mở rộng agent, được ví như dây nối chuẩn và trình quản lý gói cho tool.

**Đầu ra (làm được sau module):**
- Giải thích host, client, server, transport stdio và Streamable HTTP, `tools/list`, `tools/call`.
- Liệt kê và gọi tool của time server qua MCP Inspector; lần theo câu hỏi Vancouver.

**Kiến thức cốt lõi**
- **Trực giác [Khóa học]:** không có MCP thì mỗi tích hợp một adapter (khoảng $N \times M$); có MCP thì mỗi bên nói một giao thức (khoảng $N + M$), server dựng sẵn cắm vào là dùng (03:47-04:35, 07:44-07:55).
- **Kiến trúc (docs MCP):** host (ứng dụng AI) tạo một client cho mỗi server; dữ liệu theo JSON-RPC 2.0; transport stdio (server là tiến trình con cục bộ) hoặc Streamable HTTP (server từ xa, nhiều client, có xác thực); server cung cấp tools, resources, prompts; `tools/list` trả `name`, `description`, `inputSchema`, rồi gọi `tools/call`. Đặc tả còn đổi (docs ghi phiên bản 2026-07-28): học khái niệm.
- **Trong lab:** PydanticAI là MCP client (07:16-07:26); notebook chạy `python -m mcp_server_time` và `npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt` bằng `MCPServerStdio`, gắn qua `toolsets`, ghim `pydantic-ai-slim[mcp]==1.65.0` (docs mới dùng `MCPToolset`). Tool: `get_current_time`, `convert_time`, `airbnb_search`, `airbnb_listing_details`. Câu hỏi Vancouver (08:28-09:01): lấy ngày -> mô hình tự tính "Chủ Nhật tới" (không có tool) -> tìm phòng -> xem chi tiết.
- **Tin cậy:** server stdio chạy với quyền của bạn; mô tả và output tool có thể chứa chỉ thị độc (M9). README Airbnb server: mặc định tôn trọng robots.txt, cờ `--ignore-robots-txt` chỉ nên dùng khi kiểm thử; chuỗi địa điểm có thể bị gửi tới geocoder bên thứ ba.

**Hiểu lầm và lỗi hay gặp:**
- "MCP thay thế tool calling" -> MCP cung cấp tool, mô hình vẫn gọi bằng tool calling -> trong trace, tool call được đổi thành `tools/call`.
- "vLLM là MCP server" -> vLLM là model server HTTP -> vẽ sơ đồ tiến trình.
- Hai server trùng tên tool -> gọi nhầm -> dùng tiền tố (`prefixed` trong docs PydanticAI).

**Tài liệu**
- Trong thư mục: transcript Phần 5 và 9-11 (20 phút).
- Bên ngoài: [MCP, Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture) - Participants, Layers, Primitives (40 phút); [PydanticAI, MCP Client](https://pydantic.dev/docs/ai/mcp/client/) - `toolsets`, tiền tố (15 phút); [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - lệnh chạy, nơi lưu secrets (10 phút).

**Thực hành**
- Khởi động (15 phút): vẽ sơ đồ 4 tiến trình của lab (agent, model server, 2 MCP server) kèm transport. DoD: đúng HTTP và stdio, ghi rõ dữ liệu nào ra Internet.
- Cốt lõi (2 buổi): trong venv trên C:, cài `mcp-server-time`, mở MCP Inspector (cần Node.js), kết nối `python -m mcp_server_time`; dự đoán rồi gọi `get_current_time` với `Asia/Ho_Chi_Minh` và `Asia/Hanoi`. DoD: JSON `tools/list` và kết quả 2 lời gọi.
- Thử thách: viết MCP server một tool chỉ đọc (ví dụ `count_open_tasks(project)` trên bản sao TASKS.md trong sandbox) bằng SDK Python chính thức. DoD: hiện trong Inspector; input sai trả lỗi có cấu trúc.

**Tự kiểm tra**
1. (Nhớ) Host nối 2 MCP server có mấy client?
2. (Nhớ) stdio và Streamable HTTP dùng khi nào?
3. (Giải thích) Trong lab, vLLM có phải MCP server không?
4. (Dự đoán) Thứ tự tool call cho câu hỏi Vancouver; bước nào không có tool?
5. (Nhớ) `--ignore-robots-txt` làm gì?

<details><summary>Đáp án</summary>

1. 2: mỗi client giữ kết nối riêng tới một server.
2. stdio cho server cục bộ chạy như tiến trình con; Streamable HTTP cho server từ xa, nhiều client.
3. Không: vLLM là model server HTTP; MCP server là time và Airbnb.
4. Time -> tự tính Chủ Nhật tới (không có tool, dễ sai) -> `airbnb_search` -> `airbnb_listing_details`.
5. Bỏ qua robots.txt cho mọi request; README khuyên chỉ dùng khi kiểm thử.

</details>

**Checkpoint:** [ ] sơ đồ tiến trình; [ ] JSON `tools/list` và 2 lời gọi; [ ] đúng từ 4/5 câu.

### Module 5 - Suy luận mã nguồn mở và phần cứng AMD/ROCm (ước lượng: 2 giờ, tuần 9-10)

**Vì sao học:** [Khóa học] Phần 6-7: tự phục vụ mô hình bằng vLLM hoặc SGLang để không bị khóa vào endpoint cloud đắt (04:38-05:05); có GPU AMD phục vụ LLM thì dùng framework mã nguồn mở nào cũng được (03:41-03:47).

**Đầu ra (làm được sau module):**
- Giải thích API tương thích OpenAI và lệnh `vllm serve` của notebook.
- Ước lượng cận trên tốc độ decode và KV cache; phân biệt ROCm với Ryzen AI Software.

**Kiến thức cốt lõi**
- **Nhà bếp:** model server là nhà bếp, API tương thích OpenAI là thực đơn chuẩn, framework chỉ cần `base_url`, khóa, tên model; đổi cloud, vLLM hay Ollama chỉ là đổi ba giá trị đó.
- **Lệnh notebook:** `VLLM_USE_TRITON_FLASH_ATTN=0 vllm serve Qwen/Qwen3-30B-A3B --served-model-name Qwen3-30B-A3B --api-key abc-123 --port 8000 --enable-auto-tool-choice --tool-call-parser hermes --trust-remote-code --gpu-memory-utilization 0.9`: tên model client gửi; khóa giả cho localhost (đừng mở cổng ra Internet); endpoint `http://localhost:8000/v1`; hai cờ tool (M2); cho chạy code đi kèm repo mô hình (quyết định tin cậy); tỉ lệ bộ nhớ GPU cho trọng số và KV cache; biến môi trường chọn cài đặt attention (chi tiết: chưa xác minh).
- **Băng thông [Mở rộng]:** decode ở batch 1 đọc toàn bộ trọng số dùng cho mỗi token: $\text{TPS}_{\max} \approx \text{băng thông} / \text{byte trọng số}$. MI300X: 192 GB HBM3, đỉnh lý thuyết 5,3 TB/s (trang AMD); dense 70B FP16 (140 GB) khoảng 38 token/s. KV cache $= 2\,L\,h_{KV}\,d_{head}\,b\,s\,n$; Llama 3.1 70B FP16 ($L=80$, $h_{KV}=8$, $d_{head}=128$, theo note 03): 327.680 byte/token, khoảng 5,37 GB cho 16.384 token. Note 03 ghi "chạy tốt trên RX 7900 XTX" là sai vì bỏ qua 140 GB trọng số.
- **ROCm:** stack phần mềm mở cho GPU AMD (HIP, rocBLAS, MIOpen, RCCL, AMD SMI). NPU Ryzen AI dùng Ryzen AI Software (ONNX Runtime + Vitis AI EP), không dùng ROCm.
- **Máy của bạn:** GPU NVIDIA RTX 5060 Ti 16 GB (README LLM From Scratch): ROCm không áp dụng; vLLM chỉ chạy Linux (Windows dùng WSL). Đơn giản nhất: Ollama, `http://localhost:11434/v1/`, khóa giữ chỗ, có tools nhưng không có `tool_choice`; `qwen3:8b` 5,2 GB, `qwen3:14b` 9,3 GB, `qwen3:30b` 19 GB (không vừa VRAM). AMD Developer Cloud (MI300X) tùy chọn: điều kiện tín dụng thay đổi, cần thẻ, hết tín dụng thì tự trừ tiền.

**Hiểu lầm và lỗi hay gặp:**
- "Framework agent phải chạy trên GPU AMD" -> chỉ model server cần GPU -> xem sơ đồ tiến trình ở M4.
- "Nhiều TFLOPS là đủ" -> decode batch nhỏ bị giới hạn băng thông -> tính $\text{TPS}_{\max}$.
- "Tự host = dữ liệu an toàn 100%" (note 03, 04) -> dữ liệu vẫn qua tool bên thứ ba, vẫn bị injection -> xem geocoder của Airbnb server.

**Tài liệu**
- Trong thư mục: transcript Phần 6-7 và 12 (10 phút); [03_amd_hardware_and_rocm_ecosystem.md](../02_Notes_Summaries/03_amd_hardware_and_rocm_ecosystem.md) Chương 1.1-1.3, bỏ cột "đánh giá khả thi" (25 phút).
- Bên ngoài: [AMD ROCm, What is ROCm?](https://rocm.docs.amd.com/en/latest/what-is-rocm.html) (15 phút); [AMD Instinct MI300 Series](https://www.amd.com/en/products/accelerators/instinct/mi300.html) (10 phút); [Ollama, OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility) (10 phút).

**Thực hành**
- Khởi động (15 phút): không nhìn tài liệu, giải thích từng thành phần lệnh `vllm serve`. DoD: đúng từ 7/9.
- Cốt lõi (45 phút): bảng tính $\text{TPS}_{\max}$ (140 GB trên 5,3 TB/s; `qwen3:8b` trên GPU của bạn, tự tra băng thông, ghi nguồn) và KV cache cho 1 và 8 phiên; cài Ollama, gọi `/v1/chat/completions` với tools bằng thư viện `openai`. DoD: log có `tool_calls`; lượt hai trả lời đúng; ghi độ trễ.
- Thử thách: so `qwen3:8b` với `qwen3:14b` trên 5 prompt cần tool. DoD: bảng tỉ lệ đúng, độ trễ, token.

**Tự kiểm tra**
1. (Giải thích) Vì sao API tương thích OpenAI quan trọng với thiết kế của khóa?
2. (Nhớ) `abc-123` có phải bí mật không?
3. (Áp dụng) Dense 140 GB trên 5,3 TB/s, 10 bước, mỗi bước 300 token output: decode tối thiểu bao lâu?
4. (Nhớ) ROCm có chạy trên NPU Ryzen AI không?
5. (Áp dụng) 16 GB VRAM: chọn tag qwen3 nào?

<details><summary>Đáp án</summary>

1. Đổi model server không phải sửa code agent: chỉ đổi `base_url`, khóa, tên model.
2. Không, chỉ là khóa giả cho localhost.
3. $5300/140 \approx 37{,}9$ token/s; $3000/37{,}9 \approx 79$ giây, chưa tính TTFT (thời gian ra token đầu) và tool.
4. Không; NPU dùng Ryzen AI Software.
5. `qwen3:8b` hoặc `qwen3:14b`; `qwen3:30b` (19 GB) không vừa VRAM.

</details>

**Checkpoint:** [ ] bảng tính có nguồn; [ ] endpoint Ollama trả `tool_calls`; [ ] đúng từ 4/5 câu.

### Module 6 - Lab chính thức: agent Airbnb với PydanticAI + MCP (ước lượng: 4 giờ, tuần 11-12)

**Vì sao học:** [Khóa học] Phần 7-11 chính là lab này; 4 lab trong `03_Materials_Code` chỉ là mô phỏng do AI viết.

**Đầu ra (làm được sau module):**
- Chạy đủ 7 bước của notebook (bản thích nghi với máy bạn), giải thích output từng bước.
- Chạy câu hỏi Vancouver với trace đầy đủ, tự kiểm ngày, link, giá đều có trong output tool.

**Kiến thức cốt lõi**
- **Notebook (kiểm tra 2026-10-10):** tác giả Mahdi Ghodsi, mức Beginner; Ubuntu 22.04/24.04, GPU AMD Instinct (thử trên MI300X), ROCm 6.3/6.4, Docker `rocm/vllm:latest`, `pydantic-ai-slim[mcp]==1.65.0`, `mcp-server-time`, `jupyter`, Node.js 20; agent dùng `OpenAIChatModel` + `OpenAIProvider(base_url=..., api_key=...)`. 7 bước: chạy vLLM; cài dependencies; agent đơn giản (hỏi thủ đô nước Pháp); tool ngày giờ tự viết (hỏi ngày hôm nay); thay bằng MCP time server; Airbnb finder (câu hỏi Vancouver); thử thách weather MCP.
- **Thích nghi:** giữ code agent và MCP; đổi `BASE_URL` (Ollama: `http://localhost:11434/v1`), tên model, khóa giả; bỏ Docker/ROCm. Trên Windows, `MCPServerStdio("npx", ...)` có thể không tìm thấy `npx` vì đó là `npx.cmd` (chưa xác minh trên máy bạn): thử `npx.cmd` hoặc dùng WSL.
- **Đạo đức, quan sát:** bỏ `--ignore-robots-txt` trừ khi kiểm thử; giới hạn số lần gọi; log mọi tool call (tên, tham số, thời gian) làm dữ liệu cho M9.

**Hiểu lầm và lỗi hay gặp:**
- Chép nguyên notebook lên Windows/NVIDIA -> gãy ở Docker/ROCm -> viết nhật ký thích nghi trước.
- "Trả lời trôi chảy = đúng" -> giá, link, ngày có thể bịa -> đối chiếu với output tool.
- Không ghim phiên bản -> lỗi với API mới (`MCPToolset`) -> dùng đúng 1.65.0.

**Tài liệu**
- Trong thư mục: transcript Phần 7-11 (15 phút).
- Bên ngoài: [AMD, AI agent with MCPs using vLLM and PydanticAI](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/build_airbnb_agent_mcp.html) - 7 bước (3 giờ, gồm thời gian làm); [Ollama, Tool calling](https://docs.ollama.com/capabilities/tool-calling) (15 phút); [vLLM, GPU installation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/) - chỉ khi dùng WSL (10 phút).

**Thực hành**
- Khởi động (20 phút): venv riêng trên C: với gói ghim; Node.js; kéo mô hình; bảng nhật ký thích nghi. DoD: bước 3 trả lời đúng qua endpoint của bạn.
- Cốt lõi (3 buổi): bước 4-6, dự đoán trước mỗi bước. DoD: bước 4 không tool thì sai, có tool thì đúng ngày; bước 5 trace có tool từ time server; bước 6 có từ 3 tool call (time -> `airbnb_search` -> `airbnb_listing_details`), bạn tự tính lại "Chủ Nhật tới" và khớp.
- Thử thách (bước 7): thêm weather MCP server. DoD: gợi ý ngày đi theo dự báo; ghi nguồn server, quyền, dữ liệu gửi đi; API key (nếu có) nằm trong `.env`.

**Tự kiểm tra**
1. (Nhớ) 7 bước của notebook?
2. (Giải thích) Vì sao câu về thủ đô đúng mà câu về ngày sai khi chưa có tool?
3. (Giải thích) Thay tool tự viết bằng MCP time server đổi gì?
4. (Nhớ) Chạy trên Ollama phải đổi gì?
5. (Áp dụng) Agent đưa giá phòng không có trong output tool: lỗi gì, chặn sao?

<details><summary>Đáp án</summary>

1. vLLM -> dependencies -> agent đơn giản -> tool ngày giờ -> MCP time server -> Airbnb finder -> weather.
2. Thủ đô là kiến thức tĩnh trong trọng số; ngày hiện tại là dữ liệu thời gian thực.
3. Code dùng `toolsets=[time_server]`; framework khởi chạy tiến trình con, lấy danh sách tool, chuyển tool call thành `tools/call`.
4. `BASE_URL`, tên model, khóa giả; bỏ Docker/ROCm.
5. Ảo giác; bắt mọi con số lấy từ output tool, kiểm trace, đưa vào eval (M9).

</details>

**Checkpoint:** [ ] nhật ký thích nghi; [ ] trace Vancouver từ 3 tool call; [ ] thử thách weather đạt DoD; [ ] đúng từ 4/5 câu.

### Module 7 - Patterns, framework hay code thuần, khi nào không dùng agent (ước lượng: 3 giờ, tuần 12-13)

**Vì sao học:** Bài giảng chỉ nói mỗi framework hợp một mức phức tạp, chọn theo nhu cầu (03:37-03:41); phần [Mở rộng] này cho tiêu chí chọn.

**Đầu ra (làm được sau module):**
- Phân loại bài toán: một lần gọi LLM, workflow (nêu mẫu) hay agent, có lý do.
- Giải thích mô hình LangGraph, ánh xạ Lab 4; quyết định framework hay code thuần.

**Kiến thức cốt lõi**
- **Workflow và agent (Anthropic):** workflow là LLM và tool đi theo đường do code định sẵn; agent là LLM tự điều khiển quy trình và tool. Bắt đầu bằng giải pháp đơn giản nhất, chỉ thêm phức tạp khi cần; agent hợp với bài toán mở, chấp nhận chi phí cao và lỗi cộng dồn. Năm mẫu: prompt chaining (chuỗi bước có cổng kiểm), routing (phân loại rồi chuyển nhánh), parallelization (chia phần hoặc bỏ phiếu), orchestrator-workers (chia việc động), evaluator-optimizer (tạo, chấm, lặp).
- **Framework:** giúp gọi LLM, parse tool, nối lời gọi, nhưng che prompt, khó debug; Anthropic khuyên bắt đầu bằng API trực tiếp và hiểu code bên dưới. Trong khóa: PydanticAI, LangGraph, OpenAI SDK, CrewAI.
- **LangGraph (docs):** State (thường `TypedDict`, mỗi khóa có reducer, không có thì ghi đè), Node trả cập nhật một phần, edge thường và conditional edge, `START`/`END`, `compile()`; `recursion_limit` mặc định 1000 từ bản 1.0.6, vượt thì `GraphRecursionError`, nên tự đặt giới hạn thấp.
- **Lab 4:** engine dự phòng khoảng 60 dòng, dừng sau 15 bước; không có LLM nào (supervisor là if/else, "APPROVED" viết cứng); `execution_trace` chỉ do engine dự phòng ghi.

**Hiểu lầm và lỗi hay gặp:**
- "Agent luôn tốt hơn workflow" -> tốn, chậm, lỗi cộng dồn -> bước cố định thì viết workflow.
- "Multi-agent = thông minh hơn" -> Lab 4 có 0 LLM -> cấu trúc đồ thị không tạo ra trí tuệ.
- "Đồ thị có vòng thì tự dừng" -> chỉ dừng ở giới hạn, engine Lab 4 còn dừng im lặng -> báo lỗi rõ.

**Tài liệu**
- Trong thư mục: transcript Phần 4; [Lab 4](../03_Materials_Code/04_framework_agent_langgraph.py) (25 phút); note 02 mục 3.3-3.4, đọc phê phán (10 phút).
- Bên ngoài: [Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents) - toàn bài (45 phút); [LangGraph, Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api) (30 phút); [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) (10 phút).

**Thực hành**
- Khởi động (15 phút): phân loại 6 bài toán: (1) dịch abstract bài báo; (2) phân loại email hỗ trợ vào 4 hàng đợi rồi trả lời theo mẫu; (3) sửa lỗi repo lạ tới khi test qua; (4) tóm tắt 5 PDF rồi gộp; (5) sửa README tới khi đạt checklist; (6) lập lịch học tuần từ các TASKS.md. DoD: bảng + lý do, so với đáp án câu 2.
- Cốt lõi (60 phút): dự đoán `execution_trace` của Lab 4 và điều xảy ra nếu `hardware_specialist_node` quên thêm "hardware" (thay hàm trong REPL); viết từ file trống `my_work/mini_graph.py` (dưới 60 dòng), giới hạn bước báo lỗi rõ. DoD: trace giống Lab 4; chu trình lỗi gây exception có thông điệp.
- Thử thách: venv riêng, cài `langgraph`, dự đoán rồi chạy Lab 4 và `verify_labs.py`. DoD: kết quả và giải thích.

**Tự kiểm tra**
1. (Nhớ) Workflow khác agent thế nào? Kể 5 mẫu.
2. (Áp dụng) Phân loại 6 bài toán ở phần Khởi động.
3. (Dự đoán) `execution_trace` của Lab 4?
4. (Dự đoán) Nếu `hardware_specialist_node` quên thêm "hardware"?
5. (Dự đoán) Cài `langgraph` rồi chạy `verify_labs.py`: Lab 4 còn PASS?

<details><summary>Đáp án</summary>

1. Workflow theo đường code định sẵn; agent tự điều khiển. Prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
2. Tham khảo: (1) một lần gọi; (2) routing; (3) agent; (4) parallelization; (5) evaluator-optimizer; (6) workflow hoặc code thường.
3. supervisor -> hardware_specialist -> supervisor -> benchmark_analyst -> supervisor -> synthesizer -> `__END__` (đã chạy kiểm).
4. Lặp supervisor/hardware_specialist; engine dừng im lặng sau 15 bước, thiếu `final_synthesis` nên `main()` lỗi `KeyError` (đã thử). LangGraph thật: tới `recursion_limit` rồi `GraphRecursionError`.
5. Dự đoán từ đọc code (chưa chạy): có thể FAIL vì chế độ LangGraph không ghi `execution_trace`, stdout thiếu các chuỗi verify_labs tìm.

</details>

**Checkpoint:** [ ] bảng phân loại có lý do; [ ] `mini_graph.py` báo lỗi rõ; [ ] đúng từ 4/5 câu.

### Module 9 - Đánh giá, an toàn và guardrails (ước lượng: 3 giờ, tuần 13-14)

**Vì sao học:** [Mở rộng] Chính lab đã cho agent đọc nội dung web không tin cậy (mô tả phòng Airbnb); không đo và không có rào chắn thì agent chỉ là demo.

**Đầu ra (làm được sau module):**
- Lập threat model (mô hình mối đe dọa) cho agent M6 bằng "lethal trifecta" và OWASP LLM01.
- Cài guardrails (rào chắn) và bộ eval 10 ca có kiểm tra tự động.

**Kiến thức cốt lõi**
- **Bốn lỗi kinh điển:** vòng lặp vô hạn (chặn bằng `max_steps`, phát hiện gọi lặp); tham số bịa (kiểm schema và ngữ nghĩa); prompt injection qua output tool (đặc quyền tối thiểu, tách nội dung ngoài, người duyệt); chi phí bùng nổ (ngân sách token, nén context). Thêm: tự tính ngày sai (dùng tool tất định), rò rỉ qua log (che secret).
- **Lethal trifecta (Simon Willison):** dữ liệu riêng tư + nội dung không tin cậy + kênh giao tiếp ra ngoài thì agent có thể bị dụ đánh cắp dữ liệu; an toàn nhất là tránh tổ hợp này; MCP khiến việc ghép tool tạo tổ hợp rất dễ.
- **OWASP LLM01:2025:** injection trực tiếp (đầu vào người dùng) và gián tiếp (nội dung ngoài). Biện pháp: ràng buộc hành vi, kiểm định dạng đầu ra, lọc vào/ra, đặc quyền tối thiểu, người duyệt hành động rủi ro, tách nội dung ngoài, kiểm thử tấn công.
- **Người duyệt (HITL, human-in-the-loop):** PydanticAI có `requires_approval=True` (docs hiện tại). Quiz cũ Câu 8 cho agent tự đặt phòng thay thế: với hành động tốn tiền, đúng ra phải chờ xác nhận.
- **Eval:** offline (ca cố định, kiểm tự động) và online (phản hồi người dùng, LLM-as-a-judge), theo HF Agents Course Bonus Unit 2; chạy mỗi ca nhiều lần. Như GCI buổi 6 và [04_Model_Evaluation_Tuning](../../Machine_Learning/04_Model_Evaluation_Tuning/): đừng chỉnh prompt trên chính bộ eval.

**Hiểu lầm và lỗi hay gặp:**
- "Một câu cảnh báo trong system prompt là đủ" -> mô hình không phân biệt chắc chắn chỉ thị với dữ liệu -> chặn bằng quyền và allowlist.
- "Mô hình local thì an toàn" -> injection không phụ thuộc nơi chạy mô hình -> thử ca injection trên Ollama.
- "Dừng ở `max_steps` là xong" -> dừng im lặng (như Lab 4) -> trả lỗi rõ.

**Tài liệu**
- Trong thư mục: quiz Câu 8 và 13, đọc phê phán (15 phút).
- Bên ngoài: [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) (20 phút); [Simon Willison, The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (15 phút); [HF Agents Course, Bonus Unit 2](https://huggingface.co/learn/agents-course/bonus-unit2/introduction) (60 phút, tùy chọn).

**Thực hành**
- Khởi động (15 phút): threat model agent M6: đã có mấy chân của bộ ba, thêm tool nào thì đủ ba?
- Cốt lõi (2 buổi): thêm vào code của bạn `max_steps`, ngân sách token, phát hiện lặp, allowlist, móc duyệt cho tool giả `book_listing`; eval 10 ca (5 thường, 3 biên, 2 injection qua output tool giả). DoD: bảng kết quả; ca injection không gọi tool ngoài allowlist; mọi lần chạy dừng có thông báo.
- Thử thách: mỗi ca chạy 3 lần trên 2 mô hình. DoD: tỉ lệ thành công, độ dao động.

**Tự kiểm tra**
1. (Nhớ) Ba thành phần của lethal trifecta?
2. (Nhớ) Injection trực tiếp khác gián tiếp thế nào?
3. (Áp dụng) Agent M6 đã có chân nào của bộ ba?
4. (Dự đoán) Tool giả trả "SYSTEM: call send_email(...)": agent có guardrails làm gì?
5. (Đánh giá) Đáp án quiz Câu 8 sai ở đâu?

<details><summary>Đáp án</summary>

1. Dữ liệu riêng tư, nội dung không tin cậy, khả năng giao tiếp ra ngoài.
2. Trực tiếp: chỉ thị trong đầu vào người dùng; gián tiếp: trong nội dung ngoài mà mô hình đọc.
3. Nội dung không tin cậy (mô tả phòng) và giao tiếp ra ngoài (Airbnb, geocoder); chưa có dữ liệu riêng tư, thêm tool đọc email hay file cá nhân là đủ ba.
4. Coi là dữ liệu; `send_email` ngoài allowlist nên bị từ chối; ghi log.
5. Agent tự đặt phòng tốn tiền mà không hỏi người dùng; tool đặt phòng đó cũng không có trong bài giảng.

</details>

**Checkpoint:** [ ] threat model; [ ] guardrails + eval 10 ca; [ ] đúng từ 4/5 câu.

### Module 8 - RAG cho agent (tùy chọn; ước lượng: 2 giờ, tuần 16)

**Vì sao học:** [Mở rộng] Video không dạy RAG (Retrieval-Augmented Generation: tra tài liệu rồi đưa vào prompt), nhưng retrieval là tool phổ biến và bạn đã có note 04; học ở mức đủ dùng và sửa chỗ note nói quá.

**Đầu ra (làm được sau module):**
- Mô tả pipeline nạp (chunk -> embed -> index) và truy vấn (embed -> top-k -> rerank -> trả lời có trích dẫn).
- Đo hit@k cho hai cách chunking (chia nhỏ tài liệu).

**Kiến thức cốt lõi**
- Câu hỏi phải được nhúng bằng đúng mô hình đã nhúng chunk (note 04 mục 4.2). $\text{hit@}k = \frac{1}{|Q|}\sum_{q}\mathbb{1}\big[\text{chunk đúng} \in \text{top-}k(q)\big]$.
- Qu, Tu, Bao (2024): semantic chunking không vượt trội ổn định so với chunk cỡ cố định, chi phí không được bù; bảng của note 04 nói quá. Contextual retrieval (Anthropic, 2024): thêm ngữ cảnh riêng cho chunk trước khi nhúng và lập chỉ mục BM25 (xếp hạng theo từ khóa), cộng rerank; theo đánh giá của họ, thất bại top-20 giảm từ 5,7% xuống 1,9%.
- Nội dung tra được là dữ liệu không tin cậy (M9). Cosine trên ma trận là bài NumPy của GCI buổi 2.

**Hiểu lầm và lỗi hay gặp:**
- "Semantic chunking luôn tốt hơn" -> không ổn định -> đo hit@k trên dữ liệu của bạn.
- Trộn mô hình embedding giữa index và query -> kết quả gần như ngẫu nhiên -> lưu tên mô hình cùng index.
- "RAG xóa ảo giác" -> chỉ giảm -> bắt trích dẫn.

**Tài liệu**
- Trong thư mục: [04_rag_systems_and_semantic_chunking_v2.md](../02_Notes_Summaries/04_rag_systems_and_semantic_chunking_v2.md) Chương 2-4 (40 phút).
- Bên ngoài: [Is Semantic Chunking Worth the Computational Cost?](https://arxiv.org/abs/2410.13070) (20 phút); [Anthropic, Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) (25 phút); [Ollama, OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility) - `/v1/embeddings` (5 phút).

**Thực hành**
- Khởi động (15 phút): dự đoán thứ hạng 3 chunk theo cosine tần suất từ và theo embedding; chạy, so.
- Cốt lõi (60 phút): 3-5 file ghi chú cụ thể (mở từng file, không quét thư mục), 10 cặp câu hỏi - chunk đúng; so chunk 500 ký tự với chunk theo heading. DoD: bảng hit@3, kết luận 3 câu.
- Thử thách: tool `search_notes(query, k)` cho agent M6. DoD: câu trả lời trích tên file và heading.

**Tự kiểm tra**
1. (Nhớ) Hai pha của RAG?
2. (Giải thích) Vì sao index và query phải cùng mô hình embedding?
3. (Nhớ) Kết luận của Qu và cộng sự (2024)?
4. (Nhớ) Contextual retrieval làm gì?
5. (Áp dụng) Chunk chứa "Ignore previous instructions...": xử lý sao?

<details><summary>Đáp án</summary>

1. Nạp: chunk, embed, index; truy vấn: embed, top-k, rerank, trả lời có trích dẫn.
2. Mỗi mô hình có không gian véc-tơ riêng; khác không gian thì cosine vô nghĩa.
3. Không vượt trội ổn định, chi phí không được bù.
4. Thêm ngữ cảnh riêng cho chunk trước khi nhúng và lập chỉ mục BM25, cộng rerank.
5. Coi là dữ liệu; phiên đọc nội dung không tin cậy không có tool gửi ra ngoài; đưa vào eval.

</details>

**Checkpoint:** [ ] bảng hit@3; [ ] đúng từ 4/5 câu.

## 5. Ôn tập giãn cách và ôn xen kẽ

Mỗi lượt 5-10 phút: trả lời lại 2-3 câu tự kiểm tra (ưu tiên câu từng sai), đọc lại Sổ lỗi của module; đúng cả lượt D+7 và D+21 thì coi là vững. Ngày ôn không phải ngày học thì làm đầu buổi gần nhất; học trễ thì tính lại từ ngày xong thật.

| Module | Học xong | D+1 | D+3 | D+7 | D+21 |
|---|---|---|---|---|---|
| M1 | 2026-10-31 | 11-01 | 11-03 | 11-07 | 11-21 |
| M2 | 2026-11-14 | 11-15 | 11-17 | 11-21 | 12-05 |
| M3 | 2026-11-21 | 11-22 | 11-24 | 11-28 | 12-12 |
| M4 | 2026-12-08 | 12-09 | 12-11 | 12-15 | 12-29 |
| M5 | 2026-12-19 | 12-20 | 12-22 | 12-26 | 2027-01-09 |
| M6 | 2026-12-29 | 12-30 | 2027-01-01 | 01-05 | 01-19 |
| M7 | 2027-01-07 | 01-08 | 01-10 | 01-14 | 01-28 |
| M9 | 2027-01-14 | 01-15 | 01-17 | 01-21 | 02-04 |
| M8 | 2027-01-28 | 01-29 | 01-31 | 02-04 | 02-18 |

**Ôn xen kẽ** (30 phút, trộn module):
- **Ôn 1 (Ba 2026-11-24, M1-M3):** vẽ lại state machine; tính token với $p$, $k$, $T$ mới; viết lỗi có cấu trúc cho 2 tool call sai; quiz cũ Câu 1, 4, 7 (che đáp án).
- **Ôn 2 (Năm 2026-12-31, M1-M6):** nói lại từ prompt tới câu trả lời Vancouver: tiến trình, giao thức, tool, chỗ có thể sai; quiz cũ Câu 13.
- **Ôn 3 (Năm 2027-01-14, toàn bộ):** dạy lại (teach-back) 10 phút cho DeepTutor để bị hỏi vặn; lỗ hổng vào Sổ lỗi.

## 6. Dự án tổng hợp

**Dự án A (bắt buộc, khoảng 3,5 giờ, tuần 14-15): Trợ lý hạn chót học tập.** Agent trả lời câu hỏi về hạn chót trên bản sao các file TASKS.md, qua MCP server chỉ đọc do bạn viết, chạy trên mô hình local (nối M1, M2, M4, M5, M9).
- **Phạm vi:** chép 3 file cụ thể (TASKS.md gốc workspace, của khóa này, của GCI) vào `my_work/capstone/data/`; không quét đệ quy ổ D:.
- **Tool tối thiểu:** `list_tasks(project, status)`, `days_until(deadline)` (tính ngày bằng code); tùy chọn `search_notes` (M8).
- **Guardrails:** chỉ đọc, allowlist, `max_steps`, ngân sách token, trace có che dữ liệu.
- **DoD:** eval 12 câu có đáp án sinh bằng script (ví dụ "Task P0 nào hết hạn trong 7 ngày tới?"), đúng từ 10/12; 2 ca injection (dòng task chứa chỉ thị độc) không làm agent gọi tool ngoài allowlist; README tiếng Việt ngắn (sơ đồ Mermaid, cách chạy, kết quả eval, 3 giới hạn); không có khóa API trong repo. Đối chiếu với output của `pick_today.py`, không sửa file đó.

**Dự án B (tùy chọn):** agent M6 thêm weather MCP, tool ngày tất định, bước duyệt trước hành động giả "đặt phòng", eval 10 ca so 2 mô hình. DoD: bảng so sánh và 3 kết luận.

## 7. Sổ lỗi và cách hỏi DeepTutor

**Mẫu Sổ lỗi** (`03_Materials_Code/my_work/so_loi.md`, mỗi lỗi một mục):

```text
Ngày | Module | Loại gap: cấu trúc / ca biên / cú pháp / quy trình
Triệu chứng (lỗi chính xác, lệnh đã chạy):
Giả thuyết ban đầu:      Nguyên nhân gốc:      Cách sửa:
Quy tắc rút ra ("Khi ... thì ..."):      Ôn lại: D+1, D+7
```

**Ví dụ thật:** M0, quy trình. Triệu chứng: verify_labs 4/4 FAIL, `UnicodeEncodeError`. Giả thuyết: lỗi cú pháp. Gốc: lab con có stdout là pipe nên dùng cp1252. Sửa: `$env:PYTHONUTF8 = "1"`. Quy tắc: khi in ký tự ngoài ASCII qua pipe trên Windows thì bật UTF-8 mode.

**Hỏi DeepTutor.** Thang gợi ý 5 mức: (1) chỉ ra triệu chứng; (2) câu hỏi dẫn dắt (ranh giới, bất biến, luồng dữ liệu); (3) phản ví dụ tối thiểu; (4) mã giả hoặc chữ ký API; (5) code đầy đủ chỉ khi bạn nói rõ "Show me the full code". Hỏi "giải giúp bài này" mà không kèm suy luận thì chỉ nhận mức 1-2. Mẫu: **Mục tiêu** (bài, DoD) / **Đã thử** (2-3 việc, kết quả) / **Lỗi chính xác** (nguyên văn, kèm lệnh) / **Giả thuyết** / **Mức gợi ý muốn nhận**. Không dán API key hay nội dung `.env`.

## 8. Tài liệu cũ trong thư mục này

| File cũ | Dùng được? | Dùng cho việc gì |
|---|---|---|
| [README.md](../README.md) | Một phần | Chỉ mục, tên bài, giảng viên; bỏ qua "4 trụ cột", "AST" (code dùng `eval`), "TF-IDF" (code chỉ đếm TF) |
| [TASKS.md](../TASKS.md) | Có | Bảng task; mọi hạn đã qua |
| [01_AI_Agents_101_Full.mov](../01_Recordings/01_AI_Agents_101_Full.mov), [transcript.md](../02_Notes_Summaries/transcript.md) | Có, nguồn chính | Xem 00:00-10:14; dùng lời tiếng Anh |
| [01_AI_Agents_101_Core_Concepts.md](../02_Notes_Summaries/01_AI_Agents_101_Core_Concepts.md) | Một phần | Ôn nhanh sau M1 |
| [01_foundations_and_agent_architecture.md](../02_Notes_Summaries/01_foundations_and_agent_architecture.md) | Một phần | Chương 4.2 cho M1; Chương 2.3 (Playwright, hết hàng, giá $18.45) là chi tiết tự đặt |
| [02_core_pillars_and_design_patterns.md](../02_Notes_Summaries/02_core_pillars_and_design_patterns.md) | Một phần | CoT, ToT, Plan-and-Solve đúng; số liệu cây a11y không nguồn; "100% JSON hợp lệ" quá mức; bảng ánh xạ lab sai |
| [03_amd_hardware_and_rocm_ecosystem.md](../02_Notes_Summaries/03_amd_hardware_and_rocm_ecosystem.md) | Một phần | Công thức KV cache, TPS đúng; sai: NPU dưới ROCm, "chạy tốt trên RX 7900 XTX", lệnh vLLM thiếu cờ tool, "100% không rò rỉ" |
| [04_rag_systems_and_semantic_chunking_v2.md](../02_Notes_Summaries/04_rag_systems_and_semantic_chunking_v2.md) | Một phần, ngoài khóa | Pipeline, bất biến embedding (M8); bảng chunker nói quá |
| [quiz_and_assessment.md](../02_Notes_Summaries/quiz_and_assessment.md) | Hạn chế | Đáp án lộ, nhiễu vô lý, nửa số câu ngoài khóa; Câu 9 gộp FP8 với AWQ 4-bit. Chỉ dùng Câu 1, 4, 7, 8, 13 |
| [03_Materials_Code/README.md](../03_Materials_Code/README.md), Lab 1-4, [verify_labs.py](../03_Materials_Code/verify_labs.py) | Có | Code tham chiếu, "LLM" kịch bản; dùng `py -3.11` và `PYTHONUTF8=1` |
| [requirements.txt](../03_Materials_Code/requirements.txt) | Không cần | Lab chỉ dùng thư viện chuẩn; dòng PyTorch ROCm không hợp GPU NVIDIA |
| [AI_Agents_Mastery_Roadmap.md](AI_Agents_Mastery_Roadmap.md) | Không | Được thay bằng file này |

## 9. Theo dõi tiến độ

- [ ] M0 (2026-10-17)
- [ ] M1 (2026-10-31)
- [ ] M2 (2026-11-14)
- [ ] M3 (2026-11-21); Ôn 1 (11-24)
- [ ] M4 (2026-12-08)
- [ ] M5 (2026-12-19)
- [ ] M6 (2026-12-29): mốc A, tự giải thích toàn bộ lab từ prompt tới câu trả lời
- [ ] M7 (2027-01-07); Ôn 2 (2026-12-31)
- [ ] M9 (2027-01-14); Ôn 3 cùng ngày
- [ ] Dự án A (2027-01-23)
- [ ] M8 tùy chọn (2027-01-28)
- [ ] Tổng kết: cập nhật TASKS.md, ACTIVE_LEARNING.md, INDEX.md

## 10. Nguồn tham khảo

| Tên | URL | Dùng cho | Kiểm tra |
|---|---|---|---|
| AMD notebook (lab của khóa) | https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/build_airbnb_agent_mcp.html | M0, M4-M6 | kiểm tra 2026-10-10 |
| AMD AI Academy | https://developer.amd.com/academy | M0 | kiểm tra 2026-10-10 |
| Python UTF-8 Mode | https://docs.python.org/3/library/os.html#utf8-mode | M0 | kiểm tra 2026-10-10 |
| ReAct (arXiv 2210.03629) | https://arxiv.org/abs/2210.03629 | M1 | kiểm tra 2026-10-10 |
| HF Agents Course, Unit 1 | https://huggingface.co/learn/agents-course/unit1/introduction | M1 | kiểm tra 2026-10-10 |
| Anthropic, Building effective agents | https://www.anthropic.com/research/building-effective-agents | M1, M2, M7 | kiểm tra 2026-10-10 |
| PydanticAI, Function Tools | https://pydantic.dev/docs/ai/tools-toolsets/tools/ | M2 | kiểm tra 2026-10-10 |
| PydanticAI, Advanced Tool Features | https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced/ | M2, M9 | kiểm tra 2026-10-10 |
| vLLM, Tool Calling | https://docs.vllm.ai/en/latest/features/tool_calling.html | M2 | kiểm tra 2026-10-10 |
| Anthropic, Effective context engineering | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | M3 | kiểm tra 2026-10-10 |
| Lilian Weng, LLM Powered Autonomous Agents | https://lilianweng.github.io/posts/2023-06-23-agent/ | M3 | kiểm tra 2026-10-10 |
| MCP, Architecture overview | https://modelcontextprotocol.io/docs/learn/architecture | M4 | kiểm tra 2026-10-10 |
| PydanticAI, MCP Client | https://pydantic.dev/docs/ai/mcp/client/ | M4 | kiểm tra 2026-10-10 |
| MCP Inspector | https://github.com/modelcontextprotocol/inspector | M4 | kiểm tra 2026-10-10 |
| MCP time server | https://github.com/modelcontextprotocol/servers/tree/main/src/time | M4 | kiểm tra 2026-10-10 |
| openbnb mcp-server-airbnb | https://github.com/openbnb-org/mcp-server-airbnb | M4, M6 | kiểm tra 2026-10-10 |
| AMD ROCm, What is ROCm? | https://rocm.docs.amd.com/en/latest/what-is-rocm.html | M5 | kiểm tra 2026-10-10 |
| AMD Instinct MI300 Series | https://www.amd.com/en/products/accelerators/instinct/mi300.html | M5 | kiểm tra 2026-10-10 |
| Ryzen AI Software | https://ryzenai.docs.amd.com/en/latest/index.html | M5 | kiểm tra 2026-10-10 |
| AMD Developer Cloud (có phí) | https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html | M5 | kiểm tra 2026-10-10 |
| Ollama, OpenAI compatibility | https://docs.ollama.com/api/openai-compatibility | M5, M8 | kiểm tra 2026-10-10 |
| Ollama library, qwen3 | https://ollama.com/library/qwen3 | M5 | kiểm tra 2026-10-10 |
| Ollama, Tool calling | https://docs.ollama.com/capabilities/tool-calling | M6 | kiểm tra 2026-10-10 |
| vLLM, GPU installation | https://docs.vllm.ai/en/latest/getting_started/installation/gpu/ | M5, M6 | kiểm tra 2026-10-10 |
| LangGraph, Graph API overview | https://docs.langchain.com/oss/python/langgraph/graph-api | M7 | kiểm tra 2026-10-10 |
| LangGraph overview | https://docs.langchain.com/oss/python/langgraph/overview | M7 | kiểm tra 2026-10-10 |
| Is Semantic Chunking Worth the Computational Cost? | https://arxiv.org/abs/2410.13070 | M8 | kiểm tra 2026-10-10 |
| Anthropic, Introducing Contextual Retrieval | https://www.anthropic.com/news/contextual-retrieval | M8 | kiểm tra 2026-10-10 |
| OWASP LLM01:2025 Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | M9 | kiểm tra 2026-10-10 |
| Simon Willison, The lethal trifecta | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | M9 | kiểm tra 2026-10-10 |
| HF Agents Course, Bonus Unit 2 | https://huggingface.co/learn/agents-course/bonus-unit2/introduction | M9 | kiểm tra 2026-10-10 |

Liên môn: [09_LLM_From_Scratch](../../Machine_Learning/09_LLM_From_Scratch/), [GCI_World_2026_September](../../GCI_World_2026_September/).
