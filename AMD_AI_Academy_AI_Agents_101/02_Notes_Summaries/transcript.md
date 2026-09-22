# 🎙️ Bản Phiên Âm & Bản Dịch Kỹ Thuật: AMD AI Academy — AI Agents 101
## Building AI Agents with MCP & Open-Source Inference

---

## 📌 Thông Tin Tổng Quan & Siêu Dữ Liệu (Metadata)

| Thuộc tính | Chi tiết kỹ thuật |
| :--- | :--- |
| **Khóa học** | AMD AI Academy: AI Agents 101 |
| **Tiêu đề bài giảng** | Building AI Agents with MCP & Open-Source Inference |
| **Giảng viên / Diễn giả** | **Mahdi Ghodsi** — Product Application Engineer, AMD |
| **Đơn vị phát hành** | Advanced Micro Devices, Inc. (AMD AI Academy) |
| **Tệp video gốc** | `01_Recordings/01_AI_Agents_101_Full.mov` |
| **Thời lượng tệp đa phương tiện** | **19 phút 28.20 giây** (1,168.20 giây) |
| **Thời lượng bài giảng âm thanh** | **10 phút 13.85 giây** (00:00 - 10:14) — 122 phân đoạn lời thoại hoàn chỉnh |
| **Thời lượng màn hình kết thúc** | **09 phút 14.35 giây** (10:14 - 19:28) — Thẻ Outro AMD & Giao diện tĩnh SCORM "Complete Course" (Audio: Digital Silence -91.0 dB) |
| **Định dạng âm thanh phân tích** | PCM s16le, 16,000 Hz, Mono (Trích xuất từ AAC 48kHz Stereo) |
| **Công cụ ASR (Speech-to-Text)** | Apple Silicon Metal GPU `mlx-whisper` (`whisper-large-v3-turbo`) |
| **Ngôn ngữ** | Song ngữ Anh - Việt (English Original & Professional AI Technical Translation) |

---

## 📑 Bảng Thuật Ngữ Kỹ Thuật Chuẩn Hóa (Glossary of Key Technical Terms)

| Thuật ngữ gốc (English) | Thuật ngữ dịch & giải nghĩa (Vietnamese) | Ngữ cảnh ứng dụng trong bài học |
| :--- | :--- | :--- |
| **AI Agent / Agentic System** | Tác tử AI / Hệ thống tác tử | Hệ thống phần mềm tự chủ sử dụng LLM làm bộ não kết hợp công cụ ngoại vi để hoàn thành mục tiêu. |
| **ReAct Paradigm (Reason + Act)** | Mô hình ReAct (Vòng lặp Suy luận + Hành động) | Chu trình cốt lõi: LLM suy luận (Reason) -> gọi công cụ hành động (Act) -> quan sát kết quả (Observe) -> lặp lại đến khi hoàn tất. |
| **Tool Calling / Function Calling** | Cơ chế gọi công cụ / Gọi hàm | Khả năng LLM tự quyết định kích hoạt các hàm code ngoại vi để tương tác với thế giới thực. |
| **MCP (Model Context Protocol)** | Giao thức Ngữ cảnh Mô hình (MCP) | Chuẩn giao tiếp mở do Anthropic đề xuất, đóng vai trò như cổng kết nối tiêu chuẩn giữa LLM/Agent và các công cụ/API bên ngoài. |
| **MCP Client / MCP Server** | Ứng dụng khách MCP / Máy chủ dịch vụ MCP | Kiến trúc Client-Server của MCP: Agent đóng vai trò Client kết nối tới các MCP Server cung cấp công cụ (Thời gian, Airbnb, Thời tiết...). |
| **vLLM / SGLang** | Engine suy luận mã nguồn mở hiệu năng cao | Các hệ thống phục vụ mô hình LLM cục bộ tối ưu bộ nhớ PagedAttention và RadixAttention với chuẩn API OpenAI-compatible. |
| **AMD ROCm™ Ecosystem** | Hệ sinh thái phần mềm mở AMD ROCm™ | Nền tảng ngăn xếp phần mềm tính toán GPU nguồn mở của AMD, hỗ trợ trực tiếp PyTorch, vLLM, SGLang trên GPU Radeon & Instinct. |
| **AMD Instinct MI300X** | Bộ tăng tốc trung tâm dữ liệu AMD Instinct MI300X | Dòng GPU AI cao cấp với bộ nhớ HBM3 192GB, chuyên dụng phục vụ suy luận mô hình lớn quy mô lớn với chi phí tối ưu. |
| **PydanticAI** | Khung phát triển Agent PydanticAI | Framework Python mã nguồn mở xây dựng Agent hướng an toàn kiểu dữ liệu (type-safe), tích hợp tự nhiên với Pydantic và MCP. |
| **LangGraph / CrewAI** | Khung điều phối luồng / Đa tác tử cộng tác | Các framework orchestration chuyên dụng: LangGraph (đồ thị trạng thái tuần hoàn), CrewAI (hợp tác đa tác tử theo vai trò). |
| **Browser Use / WebUI** | Tự động hóa trình duyệt điều khiển bởi Agent | Dự án mã nguồn mở cho phép Agent trực tiếp điều khiển trình duyệt web (tìm kiếm, điền form, mua sắm). |

---

## 🗺️ Mục Lục Bài Giảng (Lecture Table of Contents)

1. [Phần 1: Giới thiệu & Trực quan hóa AI Agent trong thực tế (00:00 - 01:03)](#phần-1-giới-thiệu--trực-quan-hóa-ai-agent-trong-thực-tế-0000---0103)
2. [Phần 2: Phân biệt LLM và AI Agent — Sức mạnh của Công cụ (01:03 - 02:21)](#phần-2-phân-biệt-llm-và-ai-agent--sức-mạnh-của-công-cụ-0103---0221)
3. [Phần 3: Vòng lặp ReAct — Mô hình Suy luận và Hành động (02:21 - 03:07)](#phần-3-vòng-lặp-react--mô-hình-suy-luận-và-hành-động-0221---0307)
4. [Phần 4: Các Khung điều phối Tác tử (PydanticAI, LangGraph, OpenAI SDK, CrewAI) (03:07 - 03:47)](#phần-4-các-khung-điều-phối-tác-tử-pydanticai-langgraph-openai-sdk-crewai-0307---0347)
5. [Phần 5: Giao thức Model Context Protocol (MCP) — Tiêu chuẩn Kết nối Toàn cầu (03:47 - 04:35)](#phần-5-giao-thức-model-context-protocol-mcp--tiêu-chuẩn-kết-nối-toàn-cầu-0347---0435)
6. [Phần 6: Suy luận Mã nguồn mở trên Phần cứng AMD (vLLM, SGLang, Qwen3, DeepSeek) (04:35 - 05:05)](#phần-6-suy-luận-mã-nguồn-mở-trên-phần-cứng-amd-vllm-sglang-qwen3-deepseek-0435---0505)
7. [Phần 7: Thực hành Lab: Khởi chạy vLLM Server trên GPU AMD ROCm (05:05 - 05:44)](#phần-7-thực-hành-lab-khởi-chạy-vllm-server-trên-gpu-amd-rocm-0505---0544)
8. [Phần 8: Thực hành Lab: Khởi tạo Tác tử PydanticAI & Viết Công cụ Tuỳ biến (05:44 - 06:49)](#phần-8-thực-hành-lab-khởi-tạo-tác-tử-pydanticai--viết-công-cụ-tuỳ-biến-0544---0649)
9. [Phần 9: Mở rộng với MCP Servers — Tích hợp Time & Airbnb MCP (06:49 - 08:24)](#phần-9-mở-rộng-với-mcp-servers--tích-hợp-time--airbnb-mcp-0649---0824)
10. [Phần 10: Thực thi Chuỗi Tác vụ Đa bước — Kịch bản Đặt phòng Vancouver (08:24 - 09:01)](#phần-10-thực-thi-chuỗi-tác-vụ-đa-bước--kịch-bản-đặt-phòng-vancouver-0824---0901)
11. [Phần 11: Mở rộng Hệ sinh thái & Kiến trúc Mô-đun Hóa (09:01 - 09:34)](#phần-11-mở-rộng-hệ-sinh-thái--kiến-trúc-mô-đun-hóa-0901---0934)
12. [Phần 12: Tổng kết Kiến thức, Trụ cột Công nghệ & Lời kết (09:34 - 10:14)](#phần-12-tổng-kết-kiến-thức-trụ-cột-công-nghệ--lời-kết-0934---1014)
13. [Phần 13: Phần kết bài học & Giao diện Hoàn thành Khóa học SCORM (10:14 - 19:28)](#phần-13-phần-kết-bài-học--giao-diện-hoàn-thành-khóa-học-scorm-1014---1928)

---

## 📖 Nội Dung Phiên Âm Chi Tiết Song Ngữ (Full Bilingual Transcript)

### Phần 1: Giới thiệu & Trực quan hóa AI Agent trong thực tế (00:00 - 01:03)
> **Chủ đề chính:** Chào mừng đến với AI Agents 101; Giới thiệu demo thực tế WebUI của Browser Use; Tình huống tự động tìm công thức nấu ăn và thêm nguyên liệu vào giỏ hàng Instacart.  
> **Hình ảnh trên video:** Slide tiêu đề bài giảng và demo trình duyệt tự động tương tác với giao diện mua sắm.

- `[00:00 - 00:05]`  
  **EN:** Hey everyone, welcome to AI Agent 101.  
  **VI:** Chào mọi người, chào mừng các bạn đến với khóa học AI Agent 101.

- `[00:05 - 00:11]`  
  **EN:** Today we're going to take a fun practical look at what makes large language models more than just chatbots,  
  **VI:** Hôm nay chúng ta sẽ cùng tiếp cận một cách thực tế và trực quan về những yếu tố biến mô hình ngôn ngữ lớn (LLM) vượt xa khỏi khuôn khổ của những chatbot thông thường,

- `[00:11 - 00:16]`  
  **EN:** and how to turn them into powerful open source agents that can actually do things.  
  **VI:** và cách biến chúng thành các tác tử (agent) mã nguồn mở mạnh mẽ có khả năng thực sự hành động và giải quyết công việc trong đời thực.

- `[00:16 - 00:24]`  
  **EN:** To warm up, let's look at a real open source example built by a project called WebUI by Browser Use.  
  **VI:** Để bắt đầu làm nóng, hãy cùng xem một ví dụ thực tế sử dụng dự án mã nguồn mở có tên là WebUI của Browser Use.

- `[00:24 - 00:27]`  
  **EN:** Here's a scenario. Say I want to cook chili for dinner.  
  **VI:** Đây là một kịch bản tình huống: Giả sử tôi muốn nấu món thịt hầm ớt (chili con carne) cho bữa tối.

- `[00:27 - 00:31]`  
  **EN:** So I'm going to prompt the agent, "I want to cook chili for dinner tonight.  
  **VI:** Vì vậy tôi sẽ nhập câu lệnh (prompt) cho agent: "Tôi muốn nấu món chili cho bữa tối nay.

- `[00:31 - 00:35]`  
  **EN:** Can you find the ingredients and put them in my shopping cart?"  
  **VI:** Bạn có thể tìm kiếm các nguyên liệu và thêm chúng vào giỏ hàng của tôi được không?"

- `[00:35 - 00:38]`  
  **EN:** This open source agent plans the workflow for me.  
  **VI:** Tác tử mã nguồn mở này sẽ tự động lập kế hoạch quy trình làm việc (workflow) cho tôi.

- `[00:38 - 00:43]`  
  **EN:** It finds the recipe, extracts the ingredients, and adds them to the cart automatically.  
  **VI:** Nó tìm kiếm công thức nấu ăn, trích xuất danh sách nguyên liệu, và tự động thêm các món đồ vào giỏ hàng trực tuyến.

- `[00:43 - 00:51]`  
  **EN:** Watch how it alternates between thinking and doing, reasoning about the recipe, then browsing online, then taking action to fill the basket.  
  **VI:** Hãy quan sát cách agent luân phiên giữa suy nghĩ và hành động: suy luận về công thức, sau đó duyệt web trực tuyến, rồi thực hiện hành động để lấp đầy giỏ hàng.

- `[00:51 - 00:56]`  
  **EN:** That's the ReAct agent pattern in motion, combining reasoning with real-world action.  
  **VI:** Đó chính là mô hình tác tử ReAct đang vận hành trong thực tế: kết hợp khả năng suy luận (reasoning) với hành động trong thế giới thực (action).

- `[00:56 - 01:03]`  
  **EN:** Instead of just answering questions, the model becomes a practical assistant that helps you actually accomplish things.  
  **VI:** Thay vì chỉ trả lời các câu hỏi bằng văn bản thụ động, mô hình đã trở thành một trợ lý thực tế giúp bạn hoàn thành công việc cụ thể.

---

### Phần 2: Phân biệt LLM và AI Agent — Sức mạnh của Công cụ (01:03 - 02:21)
> **Chủ đề chính:** So sánh căn bản giữa LLM (sách thông minh, thụ động) và Agent (bộ não + công cụ); Ví dụ so sánh Agent A (chỉ có Calendar) và Agent B (Calendar + Weather + Browser); Bản chất sức mạnh nằm ở bộ công cụ.  
> **Hình ảnh trên video:** Slide "LLM vs Agent" và slide "Example – Tools Define Ability".

- `[01:03 - 01:05]`  
  **EN:** Here's an important distinction.  
  **VI:** Sau đây là một điểm phân biệt rất quan trọng.

- `[01:05 - 01:09]`  
  **EN:** An LLM on its own, it's like a really smart book.  
  **VI:** Bản thân một LLM đơn thuần giống như một cuốn sách thông minh tuyệt đỉnh.

- `[01:09 - 01:13]`  
  **EN:** It can answer questions, but it can't actually do anything.  
  **VI:** Nó có thể trả lời các câu hỏi, nhưng không thể trực tiếp thực hiện bất kỳ hành động nào trong thế giới thực.

- `[01:13 - 01:17]`  
  **EN:** An agent takes that same LLM and treats it as the brain.  
  **VI:** Một tác tử (agent) sẽ lấy chính LLM đó và đóng vai trò như bộ não điều khiển trung tâm.

- `[01:17 - 01:21]`  
  **EN:** The brain can reason, plan, and make decisions.  
  **VI:** Bộ não này có thể suy luận, lập kế hoạch và đưa ra quyết định.

- `[01:21 - 01:23]`  
  **EN:** But to act, it needs tools.  
  **VI:** Nhưng để hành động được, nó cần có các công cụ (tools).

- `[01:23 - 01:29]`  
  **EN:** What an agent is capable of depends entirely on what tools and capabilities we give it.  
  **VI:** Khả năng của một tác tử phụ thuộc hoàn toàn vào những công cụ và năng lực mà chúng ta trang bị cho nó.

- `[01:29 - 01:36]`  
  **EN:** If the agent only has a calculator tool, it can only act and perform for math-related actions.  
  **VI:** Nếu tác tử chỉ có công cụ máy tính (calculator), nó chỉ có thể thực thi các tác vụ liên quan đến tính toán toán học.

- `[01:36 - 01:39]`  
  **EN:** If you add a browser tool, now it can search online.  
  **VI:** Nếu bạn bổ sung công cụ trình duyệt (browser), giờ đây nó có thể tìm kiếm thông tin trực tuyến.

- `[01:39 - 01:43]`  
  **EN:** And if you add shopping APIs, suddenly it can buy groceries for you.  
  **VI:** Và nếu bạn tích hợp thêm các API mua sắm, nó có thể trực tiếp đặt mua hàng tạp hóa cho bạn.

- `[01:43 - 01:45]`  
  **EN:** Let's look at an example.  
  **VI:** Hãy cùng xem một ví dụ so sánh trực quan.

- `[01:45 - 01:48]`  
  **EN:** Agent A has only a calendar tool.  
  **VI:** Tác tử A chỉ sở hữu duy nhất một công cụ lịch (calendar tool).

- `[01:48 - 01:51]`  
  **EN:** It can help you schedule meetings, but it can't check the weather.  
  **VI:** Nó có thể giúp bạn lên lịch cuộc họp, nhưng không thể kiểm tra dự báo thời tiết.

- `[01:51 - 01:56]`  
  **EN:** Now, Agent B has a calendar tool, the weather tool, and a browser tool.  
  **VI:** Bây giờ, Tác tử B được trang bị cả công cụ lịch, công cụ thời tiết và công cụ trình duyệt.

- `[01:56 - 02:04]`  
  **EN:** Now, not only you can schedule your meetings, but also check the weather and even find the best cafes nearby.  
  **VI:** Lúc này, bạn không chỉ lên lịch họp mà còn có thể xem thời tiết và thậm chí tìm kiếm các quán cà phê tốt nhất ở khu vực lân cận.

- `[02:04 - 02:06]`  
  **EN:** Same brain, different tools.  
  **VI:** Cùng một bộ não LLM, nhưng khác nhau về bộ công cụ hỗ trợ.

- `[02:06 - 02:09]`  
  **EN:** The difference is not in the LLM itself.  
  **VI:** Sự khác biệt hoàn toàn không nằm ở bản thân mô hình LLM.

- `[02:09 - 02:11]`  
  **EN:** It's the toolbox we provide it to.  
  **VI:** Mà nằm ở hộp công cụ (toolbox) mà chúng ta cung cấp cho nó.

- `[02:11 - 02:13]`  
  **EN:** That's the magic of agents.  
  **VI:** Đó chính là điều kỳ diệu tạo nên sức mạnh của AI Agent.

- `[02:13 - 02:17]`  
  **EN:** LLMs provide the reasoning, but the tools define the actions.  
  **VI:** LLM cung cấp năng lực suy luận, nhưng chính các công cụ định nghĩa phạm vi hành động.

- `[02:17 - 02:21]`  
  **EN:** The more useful the tools, the more capable the agents become.  
  **VI:** Công cụ càng hữu ích và phong phú, tác tử càng trở nên mạnh mẽ và toàn năng.

---

### Phần 3: Vòng lặp ReAct — Mô hình Suy luận và Hành động (02:21 - 03:07)
> **Chủ đề chính:** Cơ chế biến LLM thành Agent chủ động thông qua mô hình ReAct; Phân tích 3 thành phần: Reason (Suy nghĩ), Act (Hành động), Loop (Vòng lặp luân phiên); Sơ đồ Reason -> Act -> Observe.  
> **Hình ảnh trên video:** Slide "The ReAct loop" với sơ đồ minh họa khối ReAct Agent nhận Input Prompt và trả về Final Answer.

- `[02:21 - 02:27]`  
  **EN:** The ReAct paradigm is what turns an LLM from a passive Q&A system into an active agent.  
  **VI:** Mô hình ReAct chính là cơ chế biến LLM từ một hệ thống hỏi đáp (Q&A) thụ động thành một tác tử chủ động hành động.

- `[02:27 - 02:29]`  
  **EN:** And here's how it works.  
  **VI:** Và đây là cách thức vận hành của mô hình này.

- `[02:29 - 02:32]`  
  **EN:** For the reasoning part, the LLM thinks about the problem.  
  **VI:** Về phần suy luận (Reasoning), LLM tư duy và phân tích vấn đề được giao.

- `[02:32 - 02:39]`  
  **EN:** For example, for the chili example, it knows that it needs to find the ingredients for chili.  
  **VI:** Ví dụ như trong bài toán nấu món chili, nó nhận định rằng trước hết cần phải tìm kiếm danh sách nguyên liệu cho món này.

- `[02:39 - 02:41]`  
  **EN:** The action part is based on that reasoning.  
  **VI:** Phần hành động (Action) sẽ được kích hoạt dựa trên kết quả suy luận đó.

- `[02:41 - 02:48]`  
  **EN:** It calls a tool, searching online, grabbing a list of ingredients, or maybe even calling a shopping API.  
  **VI:** Nó gọi một công cụ: tìm kiếm trên mạng, lấy danh sách thành phần, hoặc thậm chí gọi trực tiếp API mua sắm.

- `[02:48 - 02:53]`  
  **EN:** And for the loop, the agent alternates between reasoning and acting.  
  **VI:** Và đối với vòng lặp (Loop), tác tử sẽ luân phiên liên tục giữa suy luận và hành động.

- `[02:53 - 02:57]`  
  **EN:** It checks the progress and continues until the goal is achieved.  
  **VI:** Nó kiểm tra tiến độ thực hiện và tiếp tục chu trình cho đến khi mục tiêu cuối cùng được hoàn thành.

- `[02:57 - 03:03]`  
  **EN:** This ReAct, which is Reason plus Act cycle, is simple, but powerful.  
  **VI:** Chu trình ReAct này—tức vòng lặp Suy luận cộng Hành động—tuy đơn giản nhưng vô cùng mạnh mẽ.

- `[03:03 - 03:06]`  
  **EN:** It's the foundation of almost every modern agent framework.  
  **VI:** Nó là nền tảng cốt lõi của hầu hết mọi khung phát triển (framework) tác tử hiện đại ngày nay.

- `[03:06 - 03:11]`  
  **EN:** It lets us move from static answers to real-world actions.  
  **VI:** Nó cho phép chúng ta tiến bước từ những câu trả lời tĩnh sang các hành động thực tế có thể tạo ra kết quả.

---

### Phần 4: Các Khung điều phối Tác tử (PydanticAI, LangGraph, OpenAI SDK, CrewAI) (03:07 - 03:47)
> **Chủ đề chính:** Nhu cầu về các framework điều phối (orchestration); Giới thiệu PydanticAI (lựa chọn cho khóa học, chuẩn kiểu dữ liệu), LangGraph (chuỗi và đồ thị trạng thái), OpenAI SDK, CrewAI (đa tác tử cộng tác); Tính tương thích trên phần cứng GPU AMD.  
> **Hình ảnh trên video:** Slide "Frameworks" hiển thị logo của PydanticAI, LangGraph, OpenAI và CrewAI.

- `[03:11 - 03:17]`  
  **EN:** To build agents around the ReAct loop, we rely on frameworks that handle orchestration.  
  **VI:** Để xây dựng các tác tử xoay quanh vòng lặp ReAct, chúng ta dựa vào các khung làm việc (framework) chịu trách nhiệm điều phối (orchestration).

- `[03:17 - 03:22]`  
  **EN:** PydanticAI is a choice that we made for this course, but there is more than PydanticAI.  
  **VI:** PydanticAI là lựa chọn mà chúng tôi sử dụng cho khóa học này, tuy nhiên hệ sinh thái còn có nhiều lựa chọn khác ngoài PydanticAI.

- `[03:22 - 03:27]`  
  **EN:** PydanticAI is simple and easy for developers to build reliable agents.  
  **VI:** PydanticAI đơn giản, trực quan và dễ tiếp cận cho các lập trình viên để xây dựng các tác tử đáng tin cậy và chuẩn kiểu dữ liệu.

- `[03:27 - 03:32]`  
  **EN:** There are more frameworks such as LangGraph, which is specialized in chaining and orchestration.  
  **VI:** Còn có nhiều framework khác như LangGraph, chuyên sâu về việc xâu chuỗi (chaining) và điều phối các luồng trạng thái phức tạp.

- `[03:32 - 03:37]`  
  **EN:** There is OpenAI SDK, CrewAI, and more.  
  **VI:** Có OpenAI SDK, CrewAI (cho hệ thống đa tác tử cộng tác), và nhiều giải pháp khác.

- `[03:37 - 03:41]`  
  **EN:** Each framework fits a different level of complexity. The choice depends on your need.  
  **VI:** Mỗi framework phù hợp với một cấp độ phức tạp khác nhau. Việc lựa chọn hoàn toàn phụ thuộc vào nhu cầu thực tế của dự án.

- `[03:41 - 03:47]`  
  **EN:** With AMD GPUs, as long as you power the LLM, you can choose any of these open source frameworks.  
  **VI:** Với GPU của AMD, chỉ cần bạn cung cấp năng lực tính toán cho mô hình LLM, bạn có thể tự do lựa chọn bất kỳ framework mã nguồn mở nào trong số này.

---

### Phần 5: Giao thức Model Context Protocol (MCP) — Tiêu chuẩn Kết nối Toàn cầu (03:47 - 04:35)
> **Chủ đề chính:** Giới thiệu Model Context Protocol (MCP) — hệ thống dây nối chuẩn hóa giữa Agent và thế giới bên ngoài; So sánh mô hình trước MCP (adapter thủ công từng API) và sau MCP (chuẩn kết nối hợp nhất); Khái niệm MCP server dạng cắm-và-chạy (plug-and-play).  
> **Hình ảnh trên video:** Slide "MCP" với sơ đồ so sánh kiến trúc "Before MCP" và "After MCP".

- `[03:47 - 03:53]`  
  **EN:** Another key piece of this puzzle is MCP, the Model Context Protocol.  
  **VI:** Một mảnh ghép then chốt khác trong bức tranh tổng thể này là MCP—Giao thức Ngữ cảnh Mô hình (Model Context Protocol).

- `[03:53 - 03:59]`  
  **EN:** Think of MCP as the standardized wiring between your agent and the outside world.  
  **VI:** Hãy coi MCP như một hệ thống dây nối tiêu chuẩn hóa giữa tác tử của bạn và thế giới bên ngoài.

- `[03:59 - 04:07]`  
  **EN:** Instead of hard coding every integration, MCP provides a common language so LLMs can discover and use tools in a consistent way.  
  **VI:** Thay vì phải lập trình cứng (hard-code) từng cổng kết nối riêng lẻ, MCP cung cấp một ngôn ngữ chung để LLM có thể tự động khám phá và sử dụng các công cụ theo cách nhất quán.

- `[04:07 - 04:18]`  
  **EN:** That means you can connect your agent to external APIs like calendars, weather services, or databases, without writing a custom adapter for each.  
  **VI:** Điều đó đồng nghĩa với việc bạn có thể kết nối tác tử tới các API bên ngoài như ứng dụng lịch, dịch vụ thời tiết, hay cơ sở dữ liệu mà không cần phải viết bộ chuyển đổi (adapter) thủ công cho từng dịch vụ.

- `[04:18 - 04:28]`  
  **EN:** You can reuse pre-built MCP servers. For example, if someone already built a weather MCP server, you can just plug it in and your agent instantly has weather capabilities.  
  **VI:** Bạn có thể tái sử dụng các máy chủ MCP (MCP servers) dựng sẵn. Ví dụ, nếu ai đó đã xây dựng một weather MCP server, bạn chỉ cần cắm vào (plug-and-play) là tác tử của bạn ngay lập tức có được năng lực tra cứu thời tiết.

- `[04:28 - 04:35]`  
  **EN:** In short, MCP lowers the friction. It makes it much easier to expand what your agents can do.  
  **VI:** Nói ngắn gọn, MCP triệt tiêu rào cản tích hợp. Nó giúp việc mở rộng những gì tác tử có thể làm trở nên dễ dàng hơn bao giờ hết.

---

### Phần 6: Suy luận Mã nguồn mở trên Phần cứng AMD (vLLM, SGLang, Qwen3, DeepSeek) (04:35 - 05:05)
> **Chủ đề chính:** Tự lưu trữ mô hình (self-hosting) thay vì phụ thuộc cloud endpoints đắt đỏ; Các engine suy luận mã nguồn mở vLLM và SGLang cung cấp OpenAI-compatible API; Hỗ trợ các mô hình mở (Qwen3, GPT-OSS, DeepSeek) trên GPU AMD.  
> **Hình ảnh trên video:** Slide "Open-Source Inference" cùng logo của Qwen3, GPT-OSS, Meta Llama, SGLang, vLLM, và DeepSeek.

- `[04:35 - 04:38]`  
  **EN:** Finally, the model, the brain, or LLM.  
  **VI:** Cuối cùng là thành phần mô hình: bộ não điều khiển, hay chính là LLM.

- `[04:38 - 04:43]`  
  **EN:** If you're running agents at scale, you don't want to be locked into expensive cloud endpoints.  
  **VI:** Nếu bạn triển khai các tác tử ở quy mô lớn, bạn chắc chắn không muốn bị phụ thuộc vào các điểm cuối (endpoints) đám mây độc quyền đắt đỏ.

- `[04:43 - 04:52]`  
  **EN:** With open source inference engines like vLLM and SGLang, you can serve the model of your choice with an OpenAI compatible API.  
  **VI:** Với các công cụ suy luận mã nguồn mở như vLLM và SGLang, bạn có thể tự phục vụ (host/serve) bất kỳ mô hình nào mình muốn thông qua API tương thích chuẩn OpenAI.

- `[04:52 - 04:59]`  
  **EN:** That gives you flexibility to run open source models like Qwen3, GPT-OSS, or DeepSeek.  
  **VI:** Điều này mang lại cho bạn sự linh hoạt tối đa để chạy các mô hình nguồn mở hàng đầu như Qwen3, GPT-OSS, hay DeepSeek.

- `[04:59 - 05:05]`  
  **EN:** You can deploy them on AMD GPUs and then connect them to your AI agentic framework of your choice.  
  **VI:** Bạn có thể triển khai chúng trực tiếp trên phần cứng GPU của AMD và sau đó kết nối với bất kỳ framework tác tử AI nào bạn mong muốn.

---

### Phần 7: Thực hành Lab: Khởi chạy vLLM Server trên GPU AMD ROCm (05:05 - 05:44)
> **Chủ đề chính:** Bắt đầu phần thực hành Jupyter notebook `build_airbnb_agent_mcp.ipynb`; Khởi chạy vLLM server trên GPU AMD Instinct MI300X với mô hình Qwen3-30B-A3B; Nền tảng ROCm tự động nhận diện.  
> **Hình ảnh trên video:** Màn hình JupyterLab terminal chạy lệnh `vllm serve Qwen/Qwen3-30B-A3B --served-model-name Qwen3-30B-A3B --api-key abc-123 --port 8000 --enable-auto-tool-choice --tool-call-parser hermes`.

- `[05:05 - 05:14]`  
  **EN:** Let's get hands on. We'll walk through this notebook, starting with spinning a vLLM server on an AMD GPU,  
  **VI:** Hãy cùng bắt tay vào thực hành. Chúng ta sẽ cùng đi qua cuốn sổ tay Jupyter này, bắt đầu từ việc khởi chạy một máy chủ vLLM trên GPU AMD,

- `[05:14 - 05:24]`  
  **EN:** then connecting to our PydanticAI agent, and finally wiring an MCP to give it real-world capabilities.  
  **VI:** sau đó kết nối tới tác tử PydanticAI của chúng ta, và cuối cùng gắn kết giao thức MCP để trang bị cho nó những năng lực xử lý trong thế giới thực.

- `[05:24 - 05:29]`  
  **EN:** vLLM is an open source inference engine that's fully OpenAI compatible.  
  **VI:** vLLM là một engine suy luận mã nguồn mở có khả năng tương thích hoàn toàn với chuẩn API của OpenAI.

- `[05:29 - 05:38]`  
  **EN:** It allows you to run the model on GPUs such as AMD Instinct MI300X, and serve models like Qwen3.  
  **VI:** Nó cho phép bạn chạy các mô hình trên GPU như AMD Instinct MI300X và phục vụ các mô hình tiên tiến như Qwen3.

- `[05:38 - 05:44]`  
  **EN:** This creates a local API, so you can connect it to your agentic framework of choice.  
  **VI:** Quá trình này tạo ra một API cục bộ, cho phép bạn dễ dàng kết nối tới framework tác tử mà mình lựa chọn.

---

### Phần 8: Thực hành Lab: Khởi tạo Tác tử PydanticAI & Viết Công cụ Tuỳ biến (05:44 - 06:49)
> **Chủ đề chính:** Cấu hình PydanticAI Agent kết nối tới vLLM endpoint; Tình huống LLM không có công cụ bị thất bại khi hỏi ngày hiện tại; Định nghĩa hàm Python kiểm tra ngày giờ với `@agent.tool`; Hoàn thành vòng lặp suy luận - hành động đầu tiên.  
> **Hình ảnh trên video:** Mã nguồn notebook Python định nghĩa `OpenAIProvider`, `OpenAIModel`, `Agent` và hàm `get_current_time`.

- `[05:44 - 05:52]`  
  **EN:** Once you've started your vLLM server, and you have the endpoint ready, now we can define our agent.  
  **VI:** Sau khi bạn đã khởi chạy vLLM server và có điểm cuối API sẵn sàng, bây giờ chúng ta có thể định nghĩa tác tử của mình.

- `[05:52 - 05:56]`  
  **EN:** PydanticAI wraps our model and connects it to an agent instance.  
  **VI:** PydanticAI sẽ bọc (wrap) mô hình của chúng ta và liên kết nó với một đối tượng (instance) tác tử.

- `[05:56 - 06:00]`  
  **EN:** At this point, the agent can reason, but can't take any actions.  
  **VI:** Tại thời điểm này, tác tử đã có thể tư duy suy luận, nhưng chưa thể thực thi bất kỳ hành động nào.

- `[06:00 - 06:03]`  
  **EN:** It's a pure LLM brain with no tools.  
  **VI:** Nó là một bộ não LLM thuần túy chưa được trang bị bất kỳ công cụ nào.

- `[06:03 - 06:06]`  
  **EN:** So, let's say if you ask, "What's the date today?"  
  **VI:** Vì vậy, giả sử nếu bạn hỏi: "Hôm nay là ngày mấy?"

- `[06:06 - 06:09]`  
  **EN:** It'll fail because it has no access to real-time data.  
  **VI:** Nó sẽ thất bại hoặc trả lời sai lệch vì không có quyền truy cập vào dữ liệu thời gian thực.

- `[06:09 - 06:12]`  
  **EN:** Let's fix that by giving it a tool.  
  **VI:** Hãy khắc phục điều này bằng cách trang bị cho nó một công cụ.

- `[06:12 - 06:15]`  
  **EN:** The ability to check the current date.  
  **VI:** Đó là khả năng tra cứu ngày giờ hiện tại chính xác.

- `[06:15 - 06:21]`  
  **EN:** We define a simple function, decorate it with tool, and add it to our agent.  
  **VI:** Chúng ta định nghĩa một hàm Python đơn giản, gắn decorator `@agent.tool`, và nạp nó vào tác tử.

- `[06:21 - 06:27]`  
  **EN:** Now, when the model encounters a time-related question, it can decide to call the function.  
  **VI:** Bây giờ, khi mô hình gặp phải câu hỏi liên quan đến thời gian, nó có thể chủ động quyết định gọi hàm này.

- `[06:27 - 06:30]`  
  **EN:** This is the essence of tool calling.  
  **VI:** Đây chính là bản chất cốt lõi của cơ chế gọi công cụ (tool calling).

- `[06:30 - 06:35]`  
  **EN:** The model decides when and why to use the tool, based on its reasoning.  
  **VI:** Mô hình tự mình đưa ra quyết định khi nào và vì sao cần sử dụng công cụ, hoàn toàn dựa trên quá trình suy luận của nó.

- `[06:35 - 06:37]`  
  **EN:** Let's test it out.  
  **VI:** Hãy cùng chạy thử nghiệm trực tiếp.

- `[06:37 - 06:40]`  
  **EN:** When we ask, "What's the date today?"  
  **VI:** Khi chúng ta đặt câu hỏi: "Hôm nay là ngày mấy?"

- `[06:40 - 06:45]`  
  **EN:** The agent uses the tool, gets the current time, and continues the conversation.  
  **VI:** Tác tử kích hoạt công cụ, lấy thông tin thời gian hiện tại chính xác, và tiếp tục duy trì cuộc hội thoại một cách tự nhiên.

- `[06:45 - 06:49]`  
  **EN:** So now, we've officially built our first reasoning acting loop.  
  **VI:** Như vậy, chúng ta đã chính thức xây dựng thành công vòng lặp suy luận - hành động (reasoning-acting loop) đầu tiên của mình.

---

### Phần 9: Mở rộng với MCP Servers — Tích hợp Time & Airbnb MCP (06:49 - 08:24)
> **Chủ đề chính:** Mở rộng Agent bằng Model Context Protocol; Cơ chế hoạt động của MCP: PydanticAI đóng vai trò MCP Client, kết nối tới nhiều MCP Server (Time server, Airbnb server, Weather server); JSON Schema chuẩn hóa mô tả tham số và kết quả; Tích hợp `MCPServerStdio` với `@openbnb/mcp-server-airbnb`.  
> **Hình ảnh trên video:** Mã nguồn notebook cấu hình Node.js / NPX và khởi tạo `MCPServerStdio("npx", args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"])`.

- `[06:49 - 06:53]`  
  **EN:** Now it's time to scale this idea with MCP, the Model Context Protocol.  
  **VI:** Bây giờ là lúc chúng ta mở rộng quy mô ý tưởng này với giao thức MCP (Model Context Protocol).

- `[06:53 - 06:59]`  
  **EN:** As we said before, MCP standardizes how agents discover and use tools.  
  **VI:** Như đã chia sẻ trước đó, MCP chuẩn hóa cách thức các tác tử khám phá và sử dụng công cụ.

- `[06:59 - 07:03]`  
  **EN:** You can think of it like a package manager for agent tools.  
  **VI:** Bạn có thể hình dung nó giống như một trình quản lý gói (package manager) dành riêng cho các công cụ của tác tử.

- `[07:03 - 07:13]`  
  **EN:** Instead of manually writing Python functions, you can connect a ready-made MCP server that exposes multiple tools through one unified interface.  
  **VI:** Thay vì phải tự viết từng hàm Python thủ công, bạn có thể kết nối với một máy chủ MCP dựng sẵn, cung cấp hàng loạt công cụ thông qua một giao diện thống nhất duy nhất.

- `[07:13 - 07:16]`  
  **EN:** Here's what happens under the hood.  
  **VI:** Đây là những gì diễn ra bên dưới hệ thống (under the hood).

- `[07:16 - 07:21]`  
  **EN:** The agent framework, like PydanticAI, acts as an MCP client.  
  **VI:** Framework tác tử, chẳng hạn như PydanticAI, sẽ đóng vai trò là một MCP client (ứng dụng khách).

- `[07:21 - 07:26]`  
  **EN:** It connects to one or more MCP servers, each of which provides a tool set.  
  **VI:** Nó kết nối tới một hoặc nhiều MCP server, mỗi server sẽ cung cấp một tập hợp các công cụ chuyên biệt.

- `[07:26 - 07:35]`  
  **EN:** For example, one server might offer get current time, another Airbnb search, another weather forecast.  
  **VI:** Ví dụ: một máy chủ cung cấp chức năng lấy thời gian hiện tại, một máy chủ khác cung cấp tính năng tìm kiếm phòng Airbnb, và máy chủ khác nữa cung cấp dự báo thời tiết.

- `[07:35 - 07:44]`  
  **EN:** These servers expose the standard JSON schemas describing what each tool does, and what parameters it needs, and what output to expect.  
  **VI:** Các máy chủ này công khai các lược đồ JSON (JSON schemas) chuẩn hóa mô tả rõ mỗi công cụ làm gì, yêu cầu các tham số đầu vào nào, và đầu ra trả về dữ liệu ra sao.

- `[07:44 - 07:55]`  
  **EN:** The agent dynamically queries these schemas, decides which tool to use, sends a request, and processes the response, all in the same reasoning loop.  
  **VI:** Tác tử truy vấn động các lược đồ này, quyết định công cụ nào cần dùng, gửi yêu cầu thực thi, và xử lý kết quả trả về—tất cả diễn ra khép kín ngay trong cùng một vòng lặp suy luận.

- `[07:55 - 07:58]`  
  **EN:** This makes MCP incredibly powerful.  
  **VI:** Điều này đem lại sức mạnh phi thường cho MCP.

- `[07:58 - 08:06]`  
  **EN:** Instead of hard coding tool logic, you can plug in a pack of tools, and your agent instantly gains new abilities.  
  **VI:** Thay vì lập trình cứng logic của từng công cụ, bạn có thể gắn vào cả một gói công cụ hoàn chỉnh, và tác tử của bạn ngay lập tức có thêm những năng lực mới.

- `[08:06 - 08:12]`  
  **EN:** In our notebook, we'll replace our local get current date tool with an MCP server.  
  **VI:** Trong cuốn sổ tay thực hành, chúng ta sẽ thay thế hàm lấy ngày cục bộ bằng một MCP server chuẩn hóa.

- `[08:12 - 08:20]`  
  **EN:** Then we'll plug in another MCP server, the Airbnb MCP, to let the agent browse listings.  
  **VI:** Sau đó, chúng ta sẽ cắm thêm một MCP server khác: Airbnb MCP, cho phép tác tử duyệt và tìm kiếm danh sách phòng thực tế.

- `[08:20 - 08:24]`  
  **EN:** Once you go through the notebook and add Airbnb and time MCPs, you can test out the agent.  
  **VI:** Khi bạn hoàn thành các bước trong notebook và tích hợp xong hai máy chủ MCP về thời gian và Airbnb, bạn có thể tiến hành kiểm thử tác tử.

---

### Phần 10: Thực thi Chuỗi Tác vụ Đa bước — Kịch bản Đặt phòng Vancouver (08:24 - 09:01)
> **Chủ đề chính:** Chạy thử nghiệm câu lệnh phức tạp: "Tìm nơi lưu trú tại Vancouver vào Chủ Nhật tới trong 3 đêm cho 2 người lớn"; Agent tự động thực hiện chuỗi ReAct đa bước: Lấy ngày hiện tại -> Tính toán ngày Chủ Nhật tới -> Gọi tìm kiếm phòng Airbnb -> Truy xuất chi tiết phòng -> Trả về kết quả hoàn chỉnh.  
> **Hình ảnh trên video:** Màn hình kết quả chạy notebook hiển thị nhật ký suy luận từng bước (reasoning trace) và danh sách phòng tại Vancouver.

- `[08:24 - 08:28]`  
  **EN:** Now our agent can browse real Airbnb listings.  
  **VI:** Bây giờ tác tử của chúng ta đã có khả năng duyệt qua các phòng nghỉ thực tế trên Airbnb.

- `[08:28 - 08:36]`  
  **EN:** When we ask, "Find a place to stay in Vancouver next Sunday for three nights for two adults."  
  **VI:** Khi chúng ta đưa ra yêu cầu: "Hãy tìm một nơi lưu trú tại Vancouver vào Chủ Nhật tuần tới trong 3 đêm cho 2 người lớn."

- `[08:36 - 08:39]`  
  **EN:** The agent goes through the loop of reasoning.  
  **VI:** Tác tử sẽ kích hoạt chuỗi vòng lặp suy luận thông minh nhiều bước:

- `[08:39 - 08:44]`  
  **EN:** It first gets the current date from the time server that we define.  
  **VI:** Đầu tiên, nó truy vấn ngày hiện tại từ time server mà chúng ta đã cấu hình.

- `[08:44 - 08:47]`  
  **EN:** Then it calculates when next Sunday is going to be.  
  **VI:** Tiếp theo, nó tự tính toán chính xác ngày Chủ Nhật tới là ngày nào theo lịch.

- `[08:47 - 08:51]`  
  **EN:** Then it uses the Airbnb search to find listings.  
  **VI:** Kế đó, nó gọi công cụ tìm kiếm của Airbnb để tra cứu danh sách phòng phù hợp với địa điểm và khoảng thời gian đó.

- `[08:51 - 08:54]`  
  **EN:** It gets the details from the Airbnb listing details.  
  **VI:** Nó tiếp tục truy xuất thông tin chi tiết từng căn hộ từ công cụ Airbnb listing details.

- `[08:54 - 08:58]`  
  **EN:** And all dynamically happening within the loop.  
  **VI:** Và tất cả các bước này đều diễn ra hoàn toàn tự động và linh hoạt bên trong vòng lặp ReAct.

- `[08:58 - 09:01]`  
  **EN:** So you can get the final answers from your agent.  
  **VI:** Nhờ đó bạn nhận được câu trả lời hoàn chỉnh, chính xác và có căn cứ thực tế từ tác tử của mình.

---

### Phần 11: Mở rộng Hệ sinh thái & Kiến trúc Mô-đun Hóa (09:01 - 09:34)
> **Chủ đề chính:** Thách thức mở rộng tác tử bằng cách gắn thêm các MCP server mới (ví dụ Weather MCP server); Tận dụng hàng ngàn MCP server có sẵn từ cộng đồng nguồn mở; Thiết kế mô-đun hóa giúp tác tử tiến hóa mà không cần sửa đổi mã nguồn cốt lõi.  
> **Hình ảnh trên video:** Slide tóm lược tính mô-đun và khả năng mở rộng của kiến trúc MCP.

- `[09:01 - 09:05]`  
  **EN:** Now that you've built the foundation, the challenge is to expand the agent.  
  **VI:** Sau khi bạn đã xây dựng được nền móng vững chắc này, thử thách tiếp theo là mở rộng năng lực cho tác tử.

- `[09:05 - 09:13]`  
  **EN:** For example, you can integrate the weather MCP server so your agent can check the weather forecast to suggest traveling dates.  
  **VI:** Ví dụ: bạn có thể tích hợp weather MCP server để tác tử tự kiểm tra dự báo thời tiết và đề xuất các ngày du lịch lý tưởng nhất.

- `[09:13 - 09:15]`  
  **EN:** The pattern stays the same.  
  **VI:** Mô hình thiết kế vẫn được giữ nguyên tính nhất quán:

- `[09:15 - 09:19]`  
  **EN:** Spin up a new MCP server, just like what we did before, and add it to the toolset.  
  **VI:** Khởi tạo một MCP server mới, hoàn toàn tương tự như những gì chúng ta đã làm, rồi bổ sung nó vào tập công cụ của tác tử.

- `[09:19 - 09:22]`  
  **EN:** And let the agent decide when to call it.  
  **VI:** Và để tác tử tự quyết định thời điểm thích hợp cần gọi công cụ.

- `[09:22 - 09:28]`  
  **EN:** Because MCP is a shared protocol, you can discover thousands of compatible servers online.  
  **VI:** Vì MCP là một giao thức chuẩn hóa mở, bạn có thể dễ dàng khám phá hàng ngàn máy chủ tương thích đã được cộng đồng xây dựng sẵn trên mạng.

- `[09:28 - 09:34]`  
  **EN:** This modular design means your agent can grow over time, gaining new skills without rewriting code.  
  **VI:** Kiến trúc mô-đun hóa này giúp tác tử của bạn có thể liên tục phát triển theo thời gian, tiếp nhận các kỹ năng mới mà không cần phải viết lại mã nguồn nền tảng.

---

### Phần 12: Tổng kết Kiến thức, Trụ cột Công nghệ & Lời kết (09:34 - 10:14)
> **Chủ đề chính:** Tổng kết 4 trụ cột cốt lõi: 1. LLM trở thành Agent qua chu trình ReAct; 2. PydanticAI quản lý vòng lặp; 3. MCP chuẩn hóa kết nối công cụ; 4. GPU AMD ROCm cung cấp xương sống tính toán mã nguồn mở hiệu năng cao; Lời kết và kêu gọi bắt đầu xây dựng.  
> **Hình ảnh trên video:** Slide "Takeaway" tổng kết 3 luận điểm lớn và khung camera diễn giả Mahdi Ghodsi kết luận bài học.

- `[09:34 - 09:39]`  
  **EN:** So to recap, LLMs become agents when they can reason and act.  
  **VI:** Tóm tắt lại: LLM trở thành Agent thực thụ khi chúng được trang bị khả năng suy luận và hành động (Reason + Act).

- `[09:39 - 09:43]`  
  **EN:** Frameworks like PydanticAI manage this reasoning action loop.  
  **VI:** Các khung làm việc như PydanticAI chịu trách nhiệm quản lý và kiểm soát vòng lặp suy luận - hành động này.

- `[09:43 - 09:48]`  
  **EN:** MCP provides a universal interface to connect any tool or API.  
  **VI:** Giao thức MCP cung cấp một giao diện tiêu chuẩn toàn cầu để kết nối tác tử tới mọi công cụ hoặc API ngoại vi.

- `[09:48 - 09:55]`  
  **EN:** And AMD GPUs give you the open, high-performance backbone to run it all efficiently.  
  **VI:** Và các GPU của AMD cung cấp nền tảng phần cứng mã nguồn mở, hiệu năng đỉnh cao để vận hành toàn bộ hệ sinh thái đó một cách tối ưu và tiết kiệm chi phí.

- `[09:55 - 10:02]`  
  **EN:** With these tools, you can go from static chatbots to dynamic AI systems that truly interact with the real world.  
  **VI:** Với bộ công cụ này, bạn có thể chuyển mình từ những chatbot văn bản tĩnh sang các hệ thống AI năng động thực sự tương tác với thế giới thực.

- `[10:02 - 10:08]`  
  **EN:** You can plug in hundreds of tools, host your own inference, and control the entire agentic stack.  
  **VI:** Bạn có thể cắm hàng trăm công cụ, tự lưu trữ và phục vụ việc suy luận của riêng mình, và nắm toàn quyền kiểm soát toàn bộ ngăn xếp công nghệ tác tử (agentic stack).

- `[10:08 - 10:10]`  
  **EN:** All open, all yours.  
  **VI:** Tất cả đều hoàn toàn mở, tất cả đều thuộc quyền tự chủ của bạn.

- `[10:10 - 10:14]`  
  **EN:** Thank you for watching, and now let's start building.  
  **VI:** Cảm ơn các bạn đã theo dõi bài giảng, và bây giờ hãy cùng bắt đầu xây dựng!

---

### Phần 13: Phần kết bài học & Giao diện Hoàn thành Khóa học SCORM (10:14 - 19:28)
> **Chủ đề chính:** Thẻ nhận diện thương hiệu kết thúc bài học (Outro card); Màn hình hoàn thành khóa học của cổng đào tạo trực tuyến AMD AI Academy (SCORM Player); Báo cáo đo lường luồng âm thanh tĩnh trong tệp ghi hình.  
> **Hình ảnh trên video:** Thẻ động đồ họa "AMD together we advance_" chuyển sang màn hình SCORM: "THANK YOU! Select the button below to complete the course and receive credit. [ Complete Course ]". Màn hình tĩnh này được duy trì từ 10:30 đến hết video tại 19:28.20.

- `[10:14 - 10:30]`  
  **EN:** *[Video Transition & Outro Brand Card]*  
  Visual: AMD brand motion graphics displaying "AMD together we advance_".  
  Audio: Musical outro fade out transitioning into silence.  
  **VI:** *[Chuyển cảnh video & Thẻ nhận diện thương hiệu kết bài]*  
  Hình ảnh: Đồ họa động nhận diện thương hiệu AMD hiển thị thông điệp "AMD together we advance_".  
  Âm thanh: Nhạc kết thúc bài giảng nhỏ dần và chuyển về trạng thái im lặng kỹ thuật số.

- `[10:30 - 19:28]`  
  **EN:** *[SCORM Course Completion Interface & Static Hold Screen]*  
  Visual: The web browser remains on the AMD AI Academy SCORM Delivery interface (`academy.amd.com/ScormEngineInterface/defaultui/deliver.aspx?...`). The active slide displays:  
  `THANK YOU!`  
  `Select the button below to complete the course and receive credit.`  
  `[ Complete Course ]`  
  Navigation menu shows all topics checked: *Title* (✓), *AI Agents 101* (✓), *Thank You* (✓).  
  Audio Track Analysis: Full digital silence verified via `ffmpeg silencedetect` (duration: 554.3s, mean volume: -91.0 dB, max volume: -62.7 dB). The OBS Studio screen capture session remained active in an idle state after the lecture concluded, accounting for the remainder of the 19m28s media container duration.  
  **VI:** *[Giao diện Hoàn thành Khóa học SCORM & Màn hình Tĩnh]*  
  Hình ảnh: Trình duyệt web hiển thị giao diện phân phối SCORM của cổng đào tạo trực tuyến AMD AI Academy (`academy.amd.com/ScormEngineInterface/defaultui/deliver.aspx?...`). Slide đang chọn hiển thị nội dung:  
  `THANK YOU!`  
  `Select the button below to complete the course and receive credit.`  
  `[ Complete Course ]`  
  Menu điều hướng bên trái xác nhận hoàn tất các bài học: *Title* (✓), *AI Agents 101* (✓), *Thank You* (✓).  
  Phân tích luồng âm thanh: Đo đạc trạng thái im lặng kỹ thuật số hoàn toàn thông qua bộ lọc `ffmpeg silencedetect` (thời lượng im lặng: 554.3 giây, mức âm lượng trung bình: -91.0 dB, cực đại: -62.7 dB). Phiên ghi hình màn hình OBS Studio được giữ nguyên ở trạng thái tĩnh sau khi bài giảng kết thúc, tạo nên tổng thời lượng 19 phút 28.20 giây của tệp media gốc.

---

## 📊 Thống Kê & Đánh Giá Chất Lượng Phiên Âm (Verification & Quality Metrics)

1. **Độ bao phủ thời lượng (Duration Coverage):**
   - Tổng thời lượng tệp video: `00:19:28.20` (100% bao phủ từ 00:00.00 đến 19:28.20).
   - Phần lời thoại bài giảng tích cực: `00:00.00 - 10:13.85` (613.85 giây).
   - Phần màn hình hoàn thành SCORM tĩnh: `10:13.85 - 19:28.20` (554.35 giây).
   - Không có bất kỳ khoảng trống thời gian hoặc phân đoạn nào bị bỏ sót.

2. **Số lượng phân đoạn & Từ vựng (Segments & Word Counts):**
   - Tổng số phân đoạn lời thoại tích cực: **122 phân đoạn**.
   - Tổng số từ tiếng Anh (English Word Count): **1,440 từ**.
   - Tổng số từ tiếng Việt (Vietnamese Word Count): **2,156 từ**.
   - Tỷ lệ dịch thuật: Đầy đủ 100% phân đoạn được đối chiếu song ngữ kèm mốc thời gian chi tiết.

3. **Độ chuẩn xác thuật ngữ chuyên ngành AI:**
   - Sửa chữa toàn diện các lỗi nhận dạng giọng nói tự động (ASR mishearings):
     - `React` -> `ReAct` (Reason + Act loop).
     - `Pedantic AI` / `Pedantic` -> `PydanticAI` / `Pydantic AI`.
     - `LandGraph` -> `LangGraph`.
     - `DeepSeq` -> `DeepSeek`.
     - `Quint3` -> `Qwen3` (mô hình Qwen3-30B-A3B phục vụ bởi vLLM trong bài thực hành).
     - `NCP` -> `MCP` (Model Context Protocol).
     - `VLLM` / `SGLANG` -> `vLLM` / `SGLang`.
     - `Chile` -> `chili con carne`.
     - `AMD and SGLANG MI300X` -> `AMD Instinct MI300X`.
   - Toàn bộ thuật ngữ AI cốt lõi (Agent, Reasoning, Planning, Tool Use, Memory, Perception, MCP Client/Server, ROCm) đều tuân thủ quy chuẩn dịch thuật kỹ thuật quốc tế và chuyên ngành AI tại Việt Nam.\n