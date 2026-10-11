"""Module 1 Assignment: Tu viet vong lap ReAct Agent tu file trong.

Khoa hoc: AMD AI Academy - AI Agents 101
Muc tieu: Hieu sau co che van hanh cot loi cua ReAct Agent (Thought -> Action -> Observation -> Final Answer)
khong phu thuoc vao framework cap cao.

Quy tac bat bien:
1. Nguoi hoc tu viet ma nguon tu dau, khong sao chep hay mo lai Lab 1 cu.
2. Su dung Orion CLI / MCP de kiem tra va leo thang goi y (ladder hints).
3. Starter file nay chi chua khung giao dien va TODO, tuyet doi khong chua loi giai.
"""

from typing import Dict, Any, Tuple, Optional, Callable


def parse(text: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    """Phan tich cu phap phan hoi tu LLM de boc tach Thought, Action, Action Argument, va Final Answer.

    Args:
        text: Chuoi van ban phan hoi sinh ra boi LLM trong luot hien tai.

    Returns:
        Tuple 4 phan tu gom:
        - thought: Doan suy nghi (Thought: ...) cua mo hinh, hoac chuoi rong / None neu khong co.
        - tool_name: Ten cong cu can goi (Action: tool_name[...]), hoac None neu khong co Action.
        - tool_arg: Tham so truyen vao cong cu, ho tro day du ngoac don/vuong long nhau.
        - final_answer: Cau tra loi cuoi cung (Final Answer: ...). Luu y: neu phan hoi chua Action
          chua qua thuc thi, gia tri nay bat buoc phai la None de ngan chan Observation tu bia dat.
    """
    # TODO: Kiem tra su xuat hien cua Action va Final Answer
    # TODO: Xu ly truong hop ngoac long nhau nhu calculate[(2+3)*4]
    # TODO: Khong chap nhan Final Answer neu truoc do co mot Action chua thuc thi
    raise NotImplementedError("TODO: Implement parse(text)")


class ReActAgent:
    """Agent dieu phoi vong lap suy luan va hanh dong ReAct."""

    def __init__(self, llm: Any, tools: Dict[str, Callable[[str], str]], max_steps: int = 6) -> None:
        """Khoi tao ReAct Agent.

        Args:
            llm: Doi tuong dong co ngon ngu, cung cap phuong thuc generate(prompt: str) -> str.
            tools: Tu dien anh xa ten cong cu -> ham thuc thi nhan vao mot chuoi tham so.
            max_steps: Gioi han ngan sach so buoc lap toi da (mac dinh: 6).
        """
        # TODO: Luu tru cac thanh phan: llm, tools, max_steps
        raise NotImplementedError("TODO: Implement ReActAgent.__init__")

    def run(self, question: str) -> Dict[str, Any]:
        """Thuc thi vong lap ReAct de tra loi cau hoi cua nguoi dung.

        Vong lap qua tung buoc (step tu 1 den max_steps):
        1. Xay dung prompt tong hop tu question va lich su Thought/Action/Observation.
        2. Goi llm.generate(prompt) de nhan phan hoi.
        3. Dung ham parse(text) de boc tach cac truong du lieu.
        4. Neu co final_answer: ket thuc thanh cong va tra ve ket qua.
        5. Neu co Action:
           - Neu ten tool hop le trong tools: thuc thi va nhan ket qua observation that.
           - Neu ten tool khong ton tai: tra ve observation bao loi co cau truc, khong lam sap chuong trinh.
           - Ghi nhan Thought, Action, Observation vao lich su.
        6. Neu het max_steps ma chua co ket qua: dung va bao that bai.

        Args:
            question: Cau hoi can giai quyet.

        Returns:
            Dictionary chua ket qua:
            - success (bool): True neu tim duoc Final Answer hop le, False neu qua so buoc.
            - final_answer (str): Noi dung cau tra loi cuoi cung hoac thong bao het buoc.
            - steps (int): So buoc agent da thuc hien.
            - tools_executed (list[str]): Danh sach ten cac cong cu da duoc goi thanh cong.
        """
        # TODO: Khoi tao lich su buoc chay va danh sach cong cu da thuc thi
        # TODO: Lap qua cac buoc tu 1 toi max_steps
        # TODO: Xay dung prompt va goi self.llm.generate(prompt)
        # TODO: Phan tich phan hoi va xu ly re nhanh Final Answer / Action / Unknown Tool
        # TODO: Tra ve dictionary theo dung cau truc dac ta
        raise NotImplementedError("TODO: Implement ReActAgent.run")
