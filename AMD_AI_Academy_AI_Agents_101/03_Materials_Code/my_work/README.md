# Bai thuc hanh Module 1: Tu viet ReAct Agent tu file trong

> Mon hoc: AI Agents 101 · Module: M1 · Thoi gian uoc tinh: 45-90 phut

## 1. Muc tieu (Objectives)
- Xay dung hoan chinh vong lap ReAct (Reason + Act: Thought -> Action -> Observation -> Final Answer) tu tap tin trang ma khong dua vao cac framework agent cap cao nhu LangChain hay LlamaIndex.
- Hieu ro co che phan dinh trach nhiem: LLM dong vai tro bo nao suy luan (de xuat Action hoac Final Answer), con ma nguon Python dong vai tro moi truong thuc thi (chay Tool, bat loi va tra ve Observation).
- Nhan dien va tu tay khac phuc cac loi thiet ke kinh dien trong he thong agent: mat kiem soat ngan sach so buoc (max_steps), sap chuong trinh khi LLM bia ten tool, bi qua mat boi Final Answer ao tu observation bia dat, va loi cat cut bieu thuc tham so co ngoac long nhau.

## 2. Giao dien bat buoc (Required Interface)
Tap tin bai lam cua nguoi hoc la `my_react.py`, can xuat ban (export) dung cac giao dien va chu ky ham sau:

### 2.1. Ham boc tach phan hoi `parse(text: str)`
```python
def parse(text: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    """Phan tich cu phap phan hoi van ban tu LLM.

    Tra ve tuple 4 phan tu:
    (thought, tool_name, tool_arg, final_answer)
    """
```
- `thought`: Chuoi suy nghi cua mo hinh (nam sau `Thought:`).
- `tool_name`: Ten cong cu duoc yeu cau goi (vi du tu `Action: calculate[...]`), hoac `None`.
- `tool_arg`: Tham so truyen vao cong cu. Bat buoc phan tich dung toan bo bieu thuc ben trong, ke ca khi tham so chua cac cap ngoac don hoac ngoac vuong long nhau (vi du: `calculate[(2+3)*4]` phai lay ra duoc `(2+3)*4`).
- `final_answer`: Cau tra loi cuoi cung cua agent (nam sau `Final Answer:`).
- **Rao chan an toan bat bien:** Neu trong cung mot phan hoi xuat hien ca `Action:` va `Final Answer:` (mo hinh tu bia ca hanh dong lan quan sat va ket luan), ham `parse` hoac agent **khong duoc phep** chap nhan `final_answer` ngay. Truong `final_answer` phai tra ve `None` de buoc vong lap agent phai thuc thi Action that tren moi truong code truoc.

### 2.2. Lop dieu phoi `ReActAgent`
```python
class ReActAgent:
    def __init__(self, llm: Any, tools: Dict[str, Callable[[str], str]], max_steps: int = 6) -> None:
        """Khoi tao agent voi doi tuong LLM, tu dien cong cu, va gioi han so buoc."""
        ...

    def run(self, question: str) -> Dict[str, Any]:
        """Thuc thi vong lap ReAct cho den khi hoan tat hoac cham nguong max_steps."""
        ...
```

Ket qua tra ve tu phuong thuc `run(question)` phai la mot `dict` voi dung 4 truong sau:
- `success` (bool): `True` neu tim ra Final Answer hop le truoc khi het so buoc; `False` neu da dung het ngan sach `max_steps`.
- `final_answer` (str): Noi dung cau tra loi cuoi cung, hoac thong bao da cham gioi han buoc.
- `steps` (int): So buoc (turn) ma agent da thuc te thuc hien.
- `tools_executed` (list[str]): Danh sach ten cac cong cu da duoc goi thuc te tren moi truong Python.

### 2.3. Giao dien dong co ngon ngu `llm.generate(prompt: str) -> str`
Doi tuong `llm` truyen vao `ReActAgent` luon cung cap phuong thuc:
```python
llm.generate(prompt: str) -> str
```
Moi luot goi, agent phai truyen toan bo ngu canh (prompt) gom cau hoi goc va lich su cac buoc `Thought`, `Action`, `Observation` truoc do vao tham so `prompt`.

## 3. Cong cu va moi truong kiem thu (Tools & Data)
- Ngon ngu: Python 3.11+.
- Trinh kiem thu tu dong: `pytest`.
- Bo test nam tai: `tests/test_my_react.py`.
- Quy tac: Nguoi hoc tuyet doi khong sua cac file kiem thu trong thu muc `tests/`. Mọi logic can hoan thien nam trong `my_react.py`.

## 4. Cach chay va luyen tap voi Orion
Orion duoc thiet ke theo phuong phap "Predict -> Run -> Hint -> Recalibrate":

### 4.1. Du doan truoc khi chay (Predict)
Truoc khi chay test, hay du doan xem ma nguon cua ban hien tai se vuot qua bao nhieu test va gap loi o dau:
- Qua CLI: `node D:/03_Development_Projects/ai_agents/orion_mcp/dist/orion.mjs predict 03_Materials_Code/my_work "Du doan 0/4 vi chua implement"`
- Qua MCP: goi cong cu `orion_predict` voi duong dan lab va loi du doan.

### 4.2. Chay kiem thu (Run)
Thuc thi bo kiem thu va xem bao cao khoang cach (gap):
- Qua CLI: `node D:/03_Development_Projects/ai_agents/orion_mcp/dist/orion.mjs run 03_Materials_Code/my_work`
- Qua MCP: goi cong cu `orion_run` voi `lab: "03_Materials_Code/my_work"`.

### 4.3. Xem goi y theo thang tro giup (Hint)
Khi mot check bi FAIL, Orion mac dinh se hien thi goi y Level 1 (chi vao trieu chung). Neu gap kho khan sau 15 phut suy nghi doc lap, ban co the yeu cau leo len cac bac tiep theo:
- Level 1: Chi vao trieu chung hoac trang thai loi (symptom / state).
- Level 2: Cau hoi dinh huong ve bat bien kien truc va luong du lieu (boundaries, invariants).
- Level 3: Phan vi du toi thieu lam sup do gia dinh ban dau (minimal counter-example).
- Level 4: Chu ky ham hoac khung ma gia (pseudocode / signatures).
- Level 5: Ma nguon hoan chinh (Orion khong bao gio tu dong sinh Level 5).
Lenh goi y:
- Qua CLI: `node D:/03_Development_Projects/ai_agents/orion_mcp/dist/orion.mjs hint 03_Materials_Code/my_work test_nested_brackets`
- Qua MCP: goi cong cu `orion_hint` voi ten bai lab va ten check can giup do.

## 5. Cac bay thuong gap (Common Pitfalls)
1. **Bay ngoac lồng khi dung regex non-greedy:** Bieu thuc `re.search(r"Action:\s*(\w+)\[(.*?)\]", text)` se ngat ngay khi gap dau `)` dau tien ben trong bieu thuc toan hoc, bien `calculate[(2+3)*4]` thanh `(2+3`.
2. **Bay quan sat bia dat (Hallucinated Observation):** LLM tu dong sinh tiep cac dong `Observation: ...` va `Final Answer: ...` trong cung mot luot. Neu agent khong kiem tra va uu tien chay Action truoc ma voi va tra ve Final Answer, agent tro thanh bo sinh van ban thuan tuy chu khong phai tac tu hanh dong.
3. **Bay ngoai le KeyError voi tool la:** Khi mo hinh ao giac sinh ra ten cong cu khong co trong `tools`, viec truy cap truc tiep `self.tools[tool_name]` se lam chuong trinh vang loi va ket thuc dot ngot. Agent thuc te can bat truong hop nay va tra ve mot observation thong bao loi de mo hinh tu dieu chinh o buoc sau.
4. **Bay vong lap vo han:** Khong kiem soat bien dem buoc hoac dieu kien thoat `step >= max_steps`, dan den tieu ton tai nguyen tinh toan hoac treo he thong.

## 6. Tieu chuan hoan thanh (Definition of Done - DoD)
Bai lab chi duoc cong nhan hoan thanh khi ca 4 tieu chi sau dat 4/4 PASS:
- [ ] Co `max_steps` de ngat vong lap va tra ve `success=False` khi vuot qua so luot cho phep.
- [ ] Tool khong xac dinh tra ve observation bao loi co cau truc vao prompt tiep theo thay vi lam sap chuong trinh.
- [ ] Khong chap nhan Final Answer di sau mot Action chua qua thuc thi boi moi truong code.
- [ ] Phan tich cu phap chinh xac tham so chua cap ngoac long nhau nhu `calculate[(2+3)*4]`.

## 7. Quy tac vang (Golden Rule)
Nguoi hoc bat dau viet tu tap tin khoi tao `my_react.py` (chua `NotImplementedError`). **Tuyet doi khong mo hay sao chep ma nguon tu Lab 1 cu (`03_Materials_Code/01_pure_react_agent.py`)**. Tu minh vuot qua ca 4 loi thiet ke tren se giup ban hieu sau ve ReAct loop hon bat ky bai giang ly thuyet nao!
