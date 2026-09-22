======================================================================
PART: PHẦN 5 - Nhập môn Agentic AI (Zero to Hero Concept)
Desc: Nắm vững lý thuyết nền tảng về AI Agent, phân biệt bản chất với Chatbot và giải mã vòng lặp tự chủ Autonomous Loop.
--------------------------------------------------
SLIDE: [s5_1] Sự Tiến hóa của AI: Từ Rule-based đến Agentic AI
Analogy: Hành trình phát triển của trí tuệ nhân tạo đi từ những cỗ máy tuân thủ luật lệ cứng nhắc đến những thực thể số có khả năng tự chủ ra quyết định và hành động trong môi trường phức tạp.
Points:
  * <strong>Giai đoạn 1 (Rule-based & Expert Systems):</strong> Lập trình viên viết hàng nghìn câu lệnh `if-else`. Cứng nhắc, không thể mở rộng khi gặp tình huống mới.
  * <strong>Giai đoạn 2 (Traditional Machine Learning):</strong> Học từ dữ liệu (Hồi quy, Cây quyết định, SVM, Random Forest). Giải quyết bài toán phân loại và dự báo có cấu trúc.
  * <strong>Giai đoạn 3 (Deep Learning & GenAI Chatbot):</strong> Mạng nơ-ron sâu và LLM (ChatGPT, Claude, Gemini). Tạo sinh văn bản, hình ảnh, mã nguồn mượt mà nhưng mang tính <em>bị động (Passive)</em> — chỉ trả lời khi người dùng ra lệnh.
  * <strong>Giai đoạn 4 (HIỆN TẠI — AGENTIC AI):</strong> AI có mục tiêu (Goal-driven), chủ động hành động, lập kế hoạch, sử dụng công cụ và tự sửa sai để hoàn thành nhiệm vụ mà không cần người dùng can thiệp từng bước.
Formula: $$\text{Tiến Hóa: } \text{If-Else} \longrightarrow \text{Machine Learning} \longrightarrow \text{Passive GenAI} \longrightarrow \mathbf{\text{Autonomous Agentic AI}}$$
Code:
# SO SÁNH CÁCH THỰC THI:
# 1. Passive LLM (Chatbot):
response = llm.generate("Lập danh sách các khách hàng nợ thuế.")
# Kết quả: Chỉ in ra văn bản tư vấn chung chung.

# 2. Agentic AI:
agent.run(goal="Thu hồi nợ thuế quý 3")
# Tự động: Đọc database -> Lọc nợ xấu -> Tra cứu biểu thuế -> Gọi API gửi email nhắc nợ -> Báo cáo
Tip: Đừng bao giờ nói với Giám khảo 'Tôi dùng ChatGPT để làm dự án'. Hãy nói: 'Tôi xây dựng một hệ thống Agentic AI có khả năng tự chủ phân tách mục tiêu và tương tác với môi trường bên ngoài'!
--------------------------------------------------
SLIDE: [s5_2] Bảng So sánh Bản chất: Chatbot vs. Agentic AI
Analogy: Chatbot giống như một nhà thông thái bị nhốt trong phòng kín chỉ biết nói chuyện; còn Agentic AI là người trợ lý đắc lực được trao chìa khóa, máy tính và quyền thực thi công việc ngoài đời thực.
Points:
  * <strong>Tính Tự chủ (Autonomy):</strong> Chatbot trả lời câu hỏi đơn lẻ (1-turn); Agent tự đặt ra chuỗi hành động để đạt mục tiêu cuối cùng.
  * <strong>Lập kế hoạch (Planning):</strong> Chatbot không có kế hoạch; Agent tự chia bài toán lớn thành các bước con (Sub-tasks) và sắp xếp thứ tự thực thi.
  * <strong>Gọi công cụ (Tool Use):</strong> Chatbot bị cô lập; Agent kết nối API, chạy mã Python, đọc ghi Database, gọi dịch vụ đám mây.
  * <strong>Cơ chế Phản tỉnh (Reflection):</strong> Chatbot không biết mình nói sai trừ khi người dùng nhắc; Agent tự chạy code kiểm thử, thấy lỗi tự quay lại sửa prompt.
  * <strong>Khả năng Phối hợp (Multi-Agent):</strong> Agent có thể chia việc cho các Agent chuyên trách khác trong một hệ sinh thái phối hợp nhịp nhàng.
Formula: $$\text{Agent} = \text{LLM Core} + \text{Planning} + \text{Tools} + \text{Memory} + \text{Execution Loop}$$
Code:
+----------------------+---------------------------------+---------------------------------+
| Tiêu Chí             | Chatbot Thông Thường (RAG)      | Agentic AI Tự Chủ               |
+----------------------+---------------------------------+---------------------------------+
| Mục tiêu             | Trả lời câu hỏi                 | Hoàn thành mục tiêu phức tạp    |
| Hành động            | Xuất văn bản / Markdown         | Gọi API, ghi DB, chạy Code      |
| Kiểm soát lỗi        | Phụ thuộc người dùng            | Tự phản ánh (Self-Correction)   |
| Cấu trúc tương tác   | Tuyến tính (Linear)             | Đồ thị trạng thái (State Graph) |
+----------------------+---------------------------------+---------------------------------+
Tip: Khi trình bày slide dự thi, bảng so sánh này sẽ giúp Giám khảo lập tức nhận ra sản phẩm của bạn vượt trội thế nào so với các ứng dụng AI thông thường trên thị trường!
--------------------------------------------------
SLIDE: [s5_3] Vòng lặp Tự chủ (The Autonomous Loop)
Analogy: Mọi Agent thông minh đều hoạt động dựa trên một vòng lặp khép kín liên tục tương tác với môi trường bên ngoài: Nhận thức -> Suy luận -> Hành động -> Quan sát -> Phản tỉnh.
Points:
  * <strong>1. Perceive (Nhận thức):</strong> Tiếp nhận trạng thái hiện tại của thế giới thông qua dữ liệu đầu vào (Prompt người dùng, kết quả API, cảm biến, file tài liệu).
  * <strong>2. Reason & Plan (Suy luận & Lập kế hoạch):</strong> Phân tích mục tiêu, tra cứu trí nhớ, quyết định bước tiếp theo cần làm gì và cần dùng công cụ nào.
  * <strong>3. Act (Hành động):</strong> Phát lệnh gọi công cụ (Function Calling) như gửi yêu cầu HTTP, truy vấn SQL, tính toán toán học.
  * <strong>4. Observe (Quan sát):</strong> Đọc kết quả trả về từ công cụ vừa gọi (Observation).
  * <strong>5. Reflect & Terminate (Phản ánh & Hoàn tất):</strong> Đánh giá xem kết quả đã thỏa mãn mục tiêu chưa. Nếu chưa hoặc bị lỗi -> lặp lại bước 2; Nếu xong -> xuất kết quả cho người dùng.
Formula: $$\text{Loop: } S_t \xrightarrow{\text{Perceive}} A_t \xrightarrow{\text{Act (Tool)}} O_{t+1} \xrightarrow{\text{Reflect}} S_{t+1}$$
Code:
WHILE mục_tiêu_chưa_hoàn_thành:
    1. Nhận thức trạng thái hiện tại (State)
    2. Suy luận (Thought) & Chọn công cụ (Action)
    3. Thực thi công cụ -> Thu nhận kết quả (Observation)
    4. Đánh giá (Self-Reflect):
       - Nếu thành công -> Cập nhật Memory
       - Nếu gặp lỗi -> Điều chỉnh kế hoạch và thử lại
TRẢ VỀ KẾT QUẢ CUỐI CÙNG (Final Answer)
Tip: Luôn đặt ra 'Max Iterations' (số vòng lặp tối đa, ví dụ 10 lần) trong code của bạn. Nếu Agent bị kẹt trong vòng lặp vô tận do tool bị lỗi, hệ thống phải biết dừng lại an toàn và báo lỗi cho người dùng!
--------------------------------------------------
SLIDE: [s5_4] 5 Trụ cột Kỹ thuật của một AI Agent Hoàn chỉnh
Analogy: Giống như con người có ngũ giác, não bộ, trí nhớ, đôi bàn tay và khả năng nói, một AI Agent hoàn chỉnh được cấu thành từ 5 khối kiến trúc không thể thiếu.
Points:
  * <strong>1. Perception (Giác quan tiếp nhận):</strong> Khả năng đọc đa phương thức (Văn bản, File Excel/PDF, Hình ảnh y tế, Dữ liệu IoT).
  * <strong>2. Brain / LLM (Bộ não suy luận):</strong> Mô hình ngôn ngữ lớn đóng vai trò hạt nhân điều khiển (Reasoning Engine), đưa ra quyết định dựa trên ngữ cảnh.
  * <strong>3. Memory (Bộ nhớ đa tầng):</strong> Short-term memory (Cửa sổ ngữ cảnh hội thoại) + Long-term memory (Vector Database lưu trữ kiến thức chuyên sâu và lịch sử bài học).
  * <strong>4. Toolset (Đôi bàn tay thực thi):</strong> Danh mục các API, hàm Python, công cụ tra cứu web được định nghĩa bằng chuẩn OpenAPI hoặc JSON Schema.
  * <strong>5. Communication & Action (Giao tiếp & Hành động):</strong> Khả năng xuất kết quả, vẽ biểu đồ, gửi thông báo hoặc bàn giao nhiệm vụ cho Agent khác.
Formula: $$\text{Architecture} = \langle \text{Perception}, \text{Brain}, \text{Memory}, \text{Tools}, \text{Action} \rangle$$
Code:
# KHUNG ĐỊNH NGHĨA 1 AGENT CHUẨN PYTHON:
class AIAgent:
    def __init__(self, name, role, tools, memory, llm):
        self.name = name          # Danh tính
        self.role = role          # Vai trò chuyên môn
        self.tools = tools        # Danh sách công cụ được phép dùng
        self.memory = memory      # Bộ nhớ Vector Store + Buffer
        self.llm = llm            # Bộ não suy luận (Claude / Gemini)
Tip: Đừng nhồi nhét quá nhiều công cụ cho 1 Agent duy nhất (Tool Overload). Nếu có hơn 10 công cụ, hãy chia nhỏ thành nhiều Agent chuyên biệt và dùng mô hình Supervisor để điều phối!
======================================================================
PART: PHẦN 6 - Kiến trúc Kỹ thuật Agentic AI Toàn diện
Desc: Đi sâu vào các kỹ thuật lập trình Agent nâng cao: ReAct pattern, Tool Calling, Quản lý bộ nhớ và Cơ chế tự phản ánh.
--------------------------------------------------
SLIDE: [s6_1] Mẫu Thiết kế Suy luận ReAct (Reasoning + Acting)
Analogy: Mẫu thiết kế ReAct kết hợp sức mạnh suy luận logic (Reasoning) và hành vi thực thi (Acting). Thay vì đoán mò, Agent sẽ 'nghĩ thành tiếng' trước khi quyết định làm bất cứ điều gì.
Points:
  * <strong>Khái niệm ReAct (Yao et al., 2022):</strong> Kỹ thuật kết hợp đan xen giữa chuỗi suy nghĩ (Thought), hành động (Action) và quan sát kết quả (Observation).
  * <strong>Thought (Suy nghĩ):</strong> Agent tự phân tích: 'Tôi cần tìm doanh thu quý 2 của công ty X. Tôi chưa có dữ liệu này trong trí nhớ, vậy tôi cần gọi tool tìm kiếm báo cáo tài chính.'
  * <strong>Action (Hành động):</strong> Agent phát sinh lệnh gọi hàm: `search_financial_report(company='X', quarter='Q2')`.
  * <strong>Observation (Quan sát):</strong> Hệ thống thực thi hàm và trả về kết quả: 'Doanh thu Q2 đạt 50 triệu USD.'
  * <strong>Thought tiếp theo:</strong> 'Đã có doanh thu Q2. Bây giờ tôi cần gọi tool tính tỷ lệ tăng trưởng so với Q1.'
  * <strong>Ưu điểm vượt trội:</strong> Giảm thiểu ảo giác (Hallucination), tăng khả năng giải thích được (Explainability) cho Ban Giám khảo.
Formula: $$\text{ReAct Cycle:} \quad \text{Thought}_t \longrightarrow \text{Action}_t \longrightarrow \text{Observation}_t \longrightarrow \text{Thought}_{t+1}$$
Code:
PROMPT TEMPLATE REACT CHUẨN:
Trả lời câu hỏi theo cấu trúc sau:
Question: [Câu hỏi của người dùng]
Thought: Bạn nên nghĩ về việc cần làm gì
Action: [Tên công cụ cần gọi, phải là một trong các công cụ: search, calculator, sql]
Action Input: [Tham số truyền vào cho công cụ]
Observation: [Kết quả công cụ trả về]
... (Lặp lại Thought/Action/Observation N lần)
Thought: Tôi đã biết câu trả lời cuối cùng
Final Answer: [Câu trả lời hoàn chỉnh]
Tip: Khi demo cho Ban Giám khảo, hãy để giao diện hiển thị hộp 'Thinking Process' (các bước Thought -> Action -> Observation). Giám khảo công nghệ sẽ đánh giá rất cao việc bạn cho họ thấy được tư duy nội tại của Agent!
--------------------------------------------------
SLIDE: [s6_2] Cơ chế Gọi Công cụ (Tool Calling & Function Calling)
Analogy: Tool Calling là cầu nối giữa trí tuệ nhân tạo và thế giới thực. Thông qua việc khai báo chuẩn JSON Schema, LLM có thể gọi bất kỳ hàm Python hoặc API RESTful nào với tham số chính xác tuyệt đối.
Points:
  * <strong>Khai báo Tool bằng Decorator:</strong> Các framework hiện đại như LangChain/LangGraph cho phép biến hàm Python thông thường thành Tool của Agent chỉ với một cú pháp đơn giản.
  * <strong>Docstring là System Prompt của Tool:</strong> LLM đọc phần mô tả (Docstring) và kiểu dữ liệu (Type hints) của hàm để biết KHI NÀO NÊN DÙNG CÔNG CỤ NÀY.
  * <strong>Xử lý lỗi Tool an toàn:</strong> Mọi Tool gọi ra ngoài phải được bọc trong khối `try-except`. Nếu API bên ngoài bị lỗi (500, Timeout), hàm phải trả về thông báo lỗi dạng chuỗi để Agent biết đường chuyển sang giải pháp dự phòng.
  * <strong>Xu hướng mới - Model Context Protocol (MCP):</strong> Giao thức chuẩn hóa của Anthropic giúp kết nối Agent với các server dữ liệu và công cụ dùng chung một cách bảo mật.
Formula: $$\text{Tool Schema} = \{\text{name}: \text{string}, \text{description}: \text{string}, \text{parameters}: \text{JSON Schema}\}$$
Code:
from langchain_core.tools import tool

@tool
def get_weather_forecast(city: str) -> str:
    """Tra cứu dự báo thời tiết thời gian thực cho một thành phố cụ thể.
    Sử dụng công cụ này khi cần biết nhiệt độ, khả năng mưa để tưới tiêu."""
    try:
        # Gọi API OpenWeatherMap hoặc dịch vụ nội bộ
        data = call_weather_api(city)
        return f"Nhiệt độ tại {city}: {data['temp']}°C, Mưa: {data['rain_prob']}%"
    except Exception as e:
        return f"Lỗi khi tra cứu thời tiết: {str(e)}"
Tip: Hãy viết Docstring của Tool thật chi tiết và nêu rõ ví dụ input hợp lệ! 80% lỗi Agent gọi sai công cụ bắt nguồn từ việc lập trình viên viết mô tả công cụ quá sơ sài hoặc mơ hồ.
--------------------------------------------------
SLIDE: [s6_3] Kiến trúc Trí nhớ Đa tầng (Memory Architecture)
Analogy: Nếu không có trí nhớ, Agent sẽ trở thành một 'kẻ mất trí' quên sạch những gì vừa làm sau mỗi lượt gọi API. Bộ nhớ đa tầng giúp Agent tích lũy kinh nghiệm và duy trì ngữ cảnh dài hạn.
Points:
  * <strong>1. Short-term Memory (Bộ nhớ ngắn hạn):</strong> Lưu trữ chuỗi các tin nhắn (User, AI, Tool Output) trong phiên làm việc hiện tại. Dùng kỹ thuật Buffer Window hoặc tóm tắt (Summarization) để không bị tràn cửa sổ ngữ cảnh (Context Window).
  * <strong>2. Long-term Episodic Memory (Bộ nhớ tình huống):</strong> Lưu trữ các sự kiện, hành động thành công hoặc thất bại trong quá khứ vào Vector Database (Milvus, Pinecone, FAISS, PGVector).
  * <strong>3. Semantic Memory (Bộ nhớ ngữ nghĩa / RAG):</strong> Kho tri thức nghiệp vụ chuyên ngành (Luật pháp, tài liệu hướng dẫn y tế, sổ tay kỹ thuật). Khi cần, Agent dùng kỹ thuật Hybrid Search (Dense + Sparse/BM25) để truy xuất.
  * <strong>4. Procedural Memory (Bộ nhớ quy trình):</strong> Lưu các mẫu quy trình công việc chuẩn (SOPs) vào System Prompt hoặc file cấu hình để Agent tuân thủ nghiêm ngặt.
Formula: $$\text{Total Memory} = \underbrace{\text{Context Buffer}}_{\text{Short-term}} + \underbrace{\text{Vector DB (RAG)}}_{\text{Semantic}} + \underbrace{\text{Past Experiences}}_{\text{Episodic}}$$
Code:
# MÔ HÌNH TRUY XUẤT BỘ NHỚ VECTOR (LANGGRAPH + CHROMA):
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vector_store = Chroma(
    collection_name="hackathon_memory",
    embedding_function=OpenAIEmbeddings(),
    persist_directory="./chroma_db"
)
# Khi Agent gặp tình huống mới, truy vấn các bài học tương tự trong quá khứ
past_solutions = vector_store.similarity_search("Sự cố rò rỉ van tưới", k=2)
Tip: Trong môi trường Hackathon, đừng dùng các dịch vụ Vector Cloud phức tạp cần trả phí. Hãy dùng SQLite-VSS, ChromaDB hoặc FAISS lưu cục bộ trong máy/container Docker để khởi động nhanh và không phụ thuộc mạng!
--------------------------------------------------
SLIDE: [s6_4] Cơ chế Tự Phản tỉnh & Kiểm soát An toàn (Self-Reflection)
Analogy: Một kỹ sư giỏi là người biết tự viết Unit Test để kiểm tra code của chính mình. Agentic AI cũng cần một cơ chế tự soi chiếu (Critic / Evaluator) để bắt lỗi trước khi gửi kết quả cho người dùng.
Points:
  * <strong>Cơ chế Reflection (Shinn et al., Reflexion):</strong> Agent tạo ra bản nháp (Draft) -> Một Agent phản biện (Critic) kiểm tra đối chiếu với tiêu chí an toàn -> Nếu chưa đạt, trả về phản hồi để Agent chính viết lại.
  * <strong>Kiểm soát Ảo giác (Hallucination Guardrails):</strong> Bắt buộc Agent phải trích dẫn nguồn (Citations) từ các tài liệu RAG hoặc output của Tool, không được tự bịa số liệu.
  * <strong>Human-in-the-Loop (Con người giám sát):</strong> Đối với các hành động nhạy cảm (Xóa dữ liệu, gửi email chính thức, chuyển tiền), hệ thống phải tạm dừng (Interrupt) để con người bấm phê duyệt trước khi thực thi.
  * <strong>Circuit Breakers:</strong> Giới hạn số lần thử lại (Retry count <= 3), giới hạn tổng số token tiêu thụ cho 1 nhiệm vụ để tránh phát sinh chi phí ngoài ý muốn.
Formula: $$\text{Output Final} = \text{Reflect}(\text{Draft}, \text{Critique Rules}) \implies \text{Pass} \ge 95\%$$
Code:
# VÒNG LẶP REFLECTION TRONG LANGGRAPH:
def evaluator_node(state):
    draft = state["draft_report"]
    # Kiểm tra xem báo cáo có chứa số liệu nguồn không
    if "Nguồn:" not in draft or len(draft) < 100:
        return {"is_approved": False, "feedback": "Thiếu trích dẫn nguồn số liệu!"}
    return {"is_approved": True, "feedback": "Đạt chuẩn."}

# Điều hướng có điều kiện (Conditional Edge)
def route_after_eval(state):
    return "export_pdf" if state["is_approved"] else "research_agent"
Tip: Đây chính là 'vũ khí bí mật' giúp dự án của bạn đè bẹp các đối thủ chỉ làm Chatbot thông thường. Ban Giám khảo sẽ cực kỳ ấn tượng nếu bạn trình diễn được cơ chế Agent tự phát hiện lỗi và tự sửa sai trên màn hình demo!
======================================================================
PART: PHẦN 7 - Mô hình Đa Tác nhân (Multi-Agent Swarms & Supervisor)
Desc: Làm chủ kiến trúc nhiều Agent phối hợp: Supervisor Pattern, Mạng lưới phân tán và so sánh các Framework hàng đầu.
--------------------------------------------------
SLIDE: [s7_1] Vì sao 1 Agent Đơn lẻ là Chưa Đủ? (Sức mạnh Đa Tác nhân)
Analogy: Một công ty không thể chỉ có một người vừa làm Giám đốc, vừa viết code, vừa kế toán, vừa bán hàng. Việc chia nhỏ thành các phòng ban chuyên môn hóa là chìa khóa để xử lý bài toán lớn.
Points:
  * <strong>Vấn đề của Single Agent (Quá tải ngữ cảnh):</strong> Khi một Agent phải gánh quá nhiều mục tiêu và quá nhiều công cụ, prompt sẽ bị loãng, tỷ lệ chọn sai công cụ và sinh ảo giác tăng vọt.
  * <strong>Nguyên lý Chuyên môn hóa (Specialization):</strong> Mỗi Agent chỉ đảm nhận một vai trò cụ thể với bộ công cụ thu gọn (Ví dụ: Researcher Agent chỉ tìm kiếm; Coder Agent chỉ viết mã; Reviewer Agent chỉ kiểm tra lỗi).
  * <strong>Tách biệt Trạng thái (State Isolation):</strong> Mỗi Agent có thể sử dụng mô hình LLM khác nhau để tối ưu chi phí (Agent phân tích dùng Claude 3.5 Sonnet, Agent dịch thuật dùng Gemini Flash hoặc Haiku).
  * <strong>Dễ dàng kiểm thử & mở rộng:</strong> Bạn có thể kiểm thử riêng từng Agent trước khi tích hợp vào đồ thị luồng chung.
Formula: $$\text{Hiệu Quả Multi-Agent} > \sum_{i=1}^N \text{Hiệu Quả Single Agent} \quad (\text{Nhờ giảm thiểu Tool Interference})$$
Code:
# PHÂN CHIA VAI TRÒ ĐỘI HÌNH ĐA TÁC NHÂN (SPECIALIZED AGENTS):
[Orchestrator Agent]  : Nhận mục tiêu lớn, lập lộ trình và giao việc
  ├── [Data Agent]     : Gọi API SQL, cào dữ liệu web, làm sạch số liệu
  ├── [Analytics Agent]: Chạy phân tích thống kê, vẽ biểu đồ qua Python
  └── [Writer Agent]   : Tổng hợp kết quả, viết báo cáo executive summary
Tip: Tại Hackathon, mô hình 3 - 4 Agent chuyên biệt là tỷ lệ vàng lý tưởng. Đừng thiết kế hệ thống 20 Agent quá cồng kềnh; việc quản lý giao tiếp giữa chúng sẽ khiến độ trễ (latency) tăng cao và dễ lỗi!
--------------------------------------------------
SLIDE: [s7_2] Mô hình Điều phối Giám sát (Supervisor Pattern)
Analogy: Mô hình Supervisor giống như một người Quản lý Dự án (Project Manager) giàu kinh nghiệm. Người này không trực tiếp làm việc chi tiết mà lắng nghe yêu cầu, phân công cho cấp dưới và nghiệm thu sản phẩm.
Points:
  * <strong>Cấu trúc Phân cấp (Hierarchical Structure):</strong> Supervisor Agent đứng ở đỉnh, có quyền quyết định Agent chuyên môn nào sẽ thực thi bước tiếp theo.
  * <strong>Luồng truyền trạng thái (State Passing):</strong> Các Agent chia sẻ chung một cấu trúc trạng thái (State). Khi một Agent hoàn thành, nó cập nhật kết quả vào State và trả quyền kiểm soát về cho Supervisor.
  * <strong>Điều kiện Dừng (Termination):</strong> Khi tất cả các nhiệm vụ con đã hoàn thành và đạt chất lượng, Supervisor sẽ phát tín hiệu kết thúc (ví dụ: chuyển sang trạng thái `FINISH`).
  * <strong>Khả năng linh hoạt:</strong> Nếu Agent A làm sai, Supervisor có thể điều hướng lại để Agent B sửa chữa hoặc yêu cầu Agent A làm lại với chỉ dẫn cụ thể hơn.
Formula: $$\text{Supervisor}(\text{Current State}) \longrightarrow \text{Next Node} \in \{\text{Agent}_1, \text{Agent}_2, \dots, \text{FINISH}\}$$
Code:
# CODE MÔ HÌNH SUPERVISOR VỚI LANGGRAPH:
from typing import Literal
from pydantic import BaseModel

class RouterOutput(BaseModel):
    next_agent: Literal["researcher", "coder", "FINISH"]
    instruction: str

def supervisor_node(state):
    prompt = f"Trạng thái công việc hiện tại: {state['messages']}. Chọn người tiếp theo:"
    decision = llm_with_structured_output(RouterOutput).invoke(prompt)
    return {"next": decision.next_agent, "task": decision.instruction}
Tip: Mô hình Supervisor là kiến trúc dễ kiểm soát và đáng tin cậy nhất để đem đi thi hackathon. Luồng chạy rất trực quan, dễ vẽ sơ đồ kiến trúc đưa vào slide pitch deck!
--------------------------------------------------
SLIDE: [s7_3] So sánh Các Frameworks: LangGraph vs. CrewAI vs. AutoGen
Analogy: Việc chọn đúng 'vũ khí' lập trình sẽ giúp đội thi tiết kiệm được 50% thời gian phát triển và tránh được những đêm thức trắng vô ích vì lỗi thư viện.
Points:
  * <strong>LangGraph (Khuyên dùng số 1 cho Hackathon):</strong> Xây dựng trên nền tảng LangChain nhưng mô hình hóa luồng dưới dạng Đồ thị có trạng thái (State Graph). Cực kỳ mạnh về kiểm soát rẽ nhánh, hỗ trợ Human-in-the-loop, lưu vết trạng thái và tích hợp production.
  * <strong>CrewAI:</strong> Cực kỳ dễ học và thiết lập nhanh. Dựa trên tư duy phân vai (Role-playing: Role, Goal, Backstory). Rất thích hợp cho các bài toán mô phỏng đội ngũ văn phòng, nghiên cứu tài liệu.
  * <strong>AutoGen (Microsoft):</strong> Tập trung vào hội thoại đa tác nhân (Conversational Agents). Mạnh về khả năng tương tác tự do và giải quyết bài toán cần tranh luận nhiều góc nhìn.
  * <strong>LlamaIndex Workflows:</strong> Sự lựa chọn số 1 nếu bài toán của bạn xoay quanh việc cào tài liệu, phân tích PDF phức tạp và trích xuất tri thức.
Formula: $$\text{Độ Linh Hoạt: } \text{LangGraph} > \text{LlamaIndex} > \text{CrewAI} > \text{AutoGen}$$
Code:
+---------------+---------------------+--------------------+---------------------+
| Tiêu Chí      | LangGraph           | CrewAI             | AutoGen             |
+---------------+---------------------+--------------------+---------------------+
| Đường cong học| Trung bình (Đồ thị) | Rất dễ (Role-play) | Trung bình          |
| Kiểm soát luồng| Cực kỳ chặt chẽ     | Tuyến tính / Hier  | Tự do (Hội thoại)   |
| Production    | Rất cao (LangServe) | Trung bình         | Trung bình          |
| Phù hợp nhất  | Hệ thống phức tạp   | Prototype 24-48h   | Thảo luận chuyên sâu|
+---------------+---------------------+--------------------+---------------------+
Tip: Nếu bạn muốn làm nhanh trong 1 ngày: Chọn CrewAI. Nếu bạn muốn hệ thống vận hành chắc chắn, không bị chạy lung tung và dễ tích hợp API vào backend FastAPI: Hãy chọn LangGraph!
======================================================================
PART: PHẦN 8 - Tech Stack Thực chiến & Starter Kit (AWS Cloud + Code)
Desc: Bộ khung mã nguồn hoàn chỉnh, cấu hình AWS Bedrock / Groq và hướng dẫn đóng gói Docker sẵn sàng chiến đấu.
--------------------------------------------------
SLIDE: [s8_1] Kiến trúc Fullstack Hoàn chỉnh của một Dự án Hackathon
Analogy: Một sản phẩm dự thi chuyên nghiệp cần có giao diện trực quan cho người dùng, API trung gian ổn định và hạt nhân AI mạnh mẽ phía sau.
Points:
  * <strong>Tầng Giao diện (Frontend Layer):</strong> Dùng <em>Streamlit</em> (nếu đội mạnh Python, muốn dựng UI trong 2 giờ) hoặc <em>Next.js / React + Tailwind CSS</em> (nếu muốn giao diện bóng bẩy, hiện đại, trải nghiệm như sản phẩm SaaS thương mại).
  * <strong>Tầng Dịch vụ (Backend API Layer):</strong> <em>FastAPI</em> (Python) là sự lựa chọn số 1 nhờ tốc độ cao, hỗ trợ bất đồng bộ (Asynchronous `async/await`), tài liệu tự động Swagger UI `/docs` và dễ dàng stream token về client.
  * <strong>Tầng Hạt nhân Tác nhân (Agentic Orchestration):</strong> <em>LangGraph / CrewAI</em> quản lý logic điều phối các Agent, kết nối công cụ và quản lý bộ nhớ.
  * <strong>Tầng Dữ liệu & Vector DB:</strong> <em>ChromaDB</em> hoặc <em>PGVector</em> lưu trữ embeddings; <em>SQLite / PostgreSQL</em> lưu trữ thông tin người dùng và lịch sử tác vụ.
  * <strong>Tầng Hạ tầng Đám mây:</strong> AWS Bedrock (Claude 3.5 Sonnet / Llama 3.3) hoặc API Groq / OpenAI.
Formula: $$\text{Fullstack} = \text{React / Streamlit} \xleftrightarrow{\text{REST / SSE}} \text{FastAPI} \xleftrightarrow{\text{State Graph}} \text{LangGraph Core} \xleftrightarrow{\text{API}} \text{AWS Bedrock}$$
Code:
CẤU TRÚC THƯ MỤC DỰ ÁN MẪU (PROJECT STRUCTURE):
my_vjai_project/
├── backend/
│   ├── agents/            # Các Agent chuyên môn (Supervisor, Researcher, Coder)
│   ├── tools/             # Các công cụ Python (Search, DB, Calculator, API)
│   ├── core/config.py     # Cấu hình API keys, AWS Bedrock credentials
│   ├── main.py            # FastAPI entrypoint & REST endpoints
│   └── requirements.txt   # Danh sách thư viện Python
├── frontend/              # Mã nguồn React / Next.js hoặc Streamlit app.py
├── docker-compose.yml     # Khởi chạy toàn bộ hệ thống bằng 1 lệnh
└── README.md              # Hướng dẫn cài đặt & kịch bản demo
Tip: Luôn triển khai tính năng Server-Sent Events (SSE) hoặc WebSocket để truyền luồng token (Streaming text) từ Agent về UI. Đừng để người dùng nhìn màn hình trắng xóa chờ đợi 30 giây!
--------------------------------------------------
SLIDE: [s8_2] Tận dụng Tài nguyên AWS Cloud & Lựa chọn Mô hình
Analogy: Ban Tổ chức và Đối tác Công nghệ hỗ trợ hạ tầng AWS. Việc biết cách khai thác đúng dịch vụ sẽ giúp giải pháp của bạn vừa nhanh, vừa rẻ, vừa đạt chuẩn doanh nghiệp.
Points:
  * <strong>Chính sách của BTC:</strong> Hỗ trợ tài nguyên điện toán đám mây AWS (AWS Bedrock, EC2, Lambda, S3, ECS) và mentor kỹ thuật.
  * <strong>Không ép buộc sử dụng AWS:</strong> Theo FAQs chính thức, bạn hoàn toàn có thể dùng thêm OpenAI, Gemini, Groq hoặc Open Source nếu phù hợp bài toán.
  * <strong>AWS Bedrock (Vũ khí tối thượng):</strong> Cho phép gọi các mô hình hàng đầu thế giới thông qua một API thống nhất an toàn: Claude 3.5 Sonnet (Tư duy siêu việt), Llama 3.3 70B (Mạnh mẽ, giá rẻ), Amazon Titan (Embeddings).
  * <strong>Tối ưu hóa Chi phí Token (Token Economics):</strong> Áp dụng chiến thuật 'Model Tiering' — Dùng model lớn (Claude 3.5 Sonnet) cho Supervisor Agent lập kế hoạch; dùng model nhỏ siêu tốc (Claude 3.5 Haiku / Groq Llama 3.1 8B) cho các Worker Agent gọi tool phụ trợ.
  * <strong>AWS Lambda & S3:</strong> Lưu trữ tài liệu người dùng tải lên vào S3; chạy các tác vụ trích xuất PDF qua Lambda serverless.
Formula: $$\text{Chi Phí Tối Ưu} = (N_{\text{Plan}} \times \text{Cost}_{\text{Sonnet}}) + (N_{\text{Workers}} \times \text{Cost}_{\text{Haiku}}) \ll \text{Pure Sonnet}$$
Code:
# GỌI CLAUDE 3.5 SONNET QUA AWS BEDROCK VỚI PYTHON:
from langchain_aws import ChatBedrock
import boto3

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

llm = ChatBedrock(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    client=bedrock_client,
    model_kwargs={"temperature": 0.2, "max_tokens": 2000}
)
Tip: Hãy nhắc đến việc bạn đã tối ưu hóa chi phí token và độ trễ như thế nào khi thuyết trình kỹ thuật. Ban Giám khảo là các chuyên gia kiến trúc đám mây sẽ đánh giá cực kỳ cao sự trưởng thành trong tư duy kỹ thuật này!
--------------------------------------------------
SLIDE: [s8_3] Starter Kit: Mẫu Code LangGraph Multi-Agent Chạy Ngay
Analogy: Dưới đây là khung sườn code hoàn chỉnh thiết lập một hệ thống 2 tác nhân có Supervisor điều phối bằng LangGraph mà bạn có thể mang vào dự án ngay lập tức.
Points:
  * <strong>Định nghĩa State:</strong> Sử dụng `MessagesState` để lưu trữ lịch sử hội thoại và danh sách các thông điệp giữa các Agent.
  * <strong>Tạo Worker Nodes:</strong> Mỗi Node là một hàm Python nhận vào State và trả về thông điệp cập nhật.
  * <strong>Xây dựng Graph:</strong> Thêm các Node vào `StateGraph`, thiết lập các cạnh điều kiện (Conditional Edges) và chỉ định điểm bắt đầu (Entry Point).
  * <strong>Biên dịch (Compile):</strong> `graph = workflow.compile()` tạo ra một đồ thị có thể chạy độc lập hoặc tích hợp vào API endpoint của FastAPI.
Formula: $$\text{Graph} = \langle V = \{\text{Supervisor}, \text{WorkerA}, \text{WorkerB}\}, E = \{\text{Conditional Edges}\} \rangle$$
Code:
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, SystemMessage

# 1. Định nghĩa các Node tác nhân
def researcher_agent(state: MessagesState):
    # Giả lập nghiên cứu dữ liệu
    return {"messages": [SystemMessage(content="Đã thu thập số liệu phát thải từ 5 nhà máy.")]}

def analyst_agent(state: MessagesState):
    # Giả lập phân tích và đề xuất
    return {"messages": [SystemMessage(content="Khuyến nghị: Thay đổi lịch vận hành tiết kiệm 25% điện.")]}

# 2. Xây dựng đồ thị làm việc
workflow = StateGraph(MessagesState)
workflow.add_node("researcher", researcher_agent)
workflow.add_node("analyst", analyst_agent)

workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "analyst")
workflow.add_edge("analyst", END)

app = workflow.compile()
# 3. Chạy thử nghiệm
result = app.invoke({"messages": [HumanMessage(content="Tối ưu năng lượng cho nhà máy A")]})
Tip: Sao chép khung sườn này và phát triển thêm các Tool thực tế (gọi API thời tiết, đọc database, xuất PDF) là bạn đã có một bộ khung Agentic AI chuẩn chỉnh cho Hackathon!