"""Unit tests cho bai thuc hanh Orion: Vong lap ReAct Agent tu file trong.

Kiem tra 4 tieu chi Definition of Done (DoD) cua Module 1:
1. test_max_steps: Co max_steps de ngat vong lap khi vuot qua so luot cho phep.
2. test_unknown_tool: Tool khong xac dinh tra ve observation bao loi thay vi lam sap chuong trinh.
3. test_final_answer_after_action: Khong chap nhan Final Answer di sau mot Action chua qua thuc thi.
4. test_nested_brackets: Phan tich cu phap chinh xac tham so chua cap ngoac long nhau nhu calculate[(2+3)*4].
"""

import sys
from pathlib import Path
from typing import Dict, Any, Callable

# Dam bao import duoc module my_react tu thu muc goc cua lab
lab_root = str(Path(__file__).resolve().parent.parent)
if lab_root not in sys.path:
    sys.path.insert(0, lab_root)

from my_react import parse, ReActAgent


# =====================================================================
# MOCK LLM ENGINES DUNG CHO KIEM THU
# =====================================================================

class LoopingMockLLM:
    """Mock LLM lien tuc sinh Action ma khong bao gio tra ve Final Answer."""

    def __init__(self):
        self.call_count = 0

    def generate(self, prompt: str) -> str:
        self.call_count += 1
        return (
            f"Thought: Buoc lap {self.call_count}\n"
            f"Action: loop_tool[{self.call_count}]"
        )


class UnknownToolMockLLM:
    """Mock LLM goi tool khong ton tai o luot 1, roi ket luan hop le o luot 2."""

    def __init__(self):
        self.prompts: list[str] = []

    def generate(self, prompt: str) -> str:
        self.prompts.append(prompt)
        if len(self.prompts) == 1:
            return (
                "Thought: Thu nghiem goi mot cong cu chua tung dang ky\n"
                "Action: missing_tool[param_test]"
            )
        return (
            "Thought: Observation da thong bao loi cong cu, toi dua ra ket luan\n"
            "Final Answer: Da tiep nhan va xu ly loi cong cu khong ton tai"
        )


class HallucinatingMockLLM:
    """Mock LLM sinh ca Action va Final Answer tu bia trong cung mot luot."""

    def __init__(self):
        self.call_count = 0

    def generate(self, prompt: str) -> str:
        self.call_count += 1
        if self.call_count == 1:
            return (
                "Thought: Toi muon tu bia ket qua ma khong cho moi truong chay\n"
                "Action: real_tool[hello]\n"
                "Observation: hello bia dat\n"
                "Final Answer: cau tra loi bia dat"
            )
        return (
            "Thought: Bay gio toi da co observation that su tu cong cu\n"
            "Final Answer: cau tra loi hop le sau khi chay tool"
        )


class NestedBracketMockLLM:
    """Mock LLM sinh Action chua bieu thuc toan voi nhieu cap ngoac long nhau."""

    def __init__(self):
        self.call_count = 0

    def generate(self, prompt: str) -> str:
        self.call_count += 1
        if self.call_count == 1:
            return (
                "Thought: Can tinh toan bieu thuc phuc tap co ngoac long\n"
                "Action: calculate[(2+3)*4]"
            )
        return (
            "Thought: Da nhan duoc ket qua tinh toan chinh xac\n"
            "Final Answer: 20"
        )


# =====================================================================
# 4 BAI KIEM THU TUONG UNG 4 CHECK DOD
# =====================================================================

def test_max_steps():
    """DoD 1: Co max_steps de ngat vong lap khi vuot qua so luot cho phep."""
    llm = LoopingMockLLM()
    tools: Dict[str, Callable[[str], str]] = {
        "loop_tool": lambda arg: f"Gia tri {arg}"
    }
    max_steps = 4
    agent = ReActAgent(llm=llm, tools=tools, max_steps=max_steps)
    result = agent.run("Thu nghiem gioi han so buoc")

    assert isinstance(result, dict), "Ket qua tra ve tu run() phai la kieu dict"
    assert result.get("success") is False, (
        "Agent phai tra ve success=False khi cham nguong max_steps ma chua co Final Answer"
    )
    assert result.get("steps") == max_steps, (
        f"So buoc da chay phai dung bang max_steps={max_steps}, thuc te nhan {result.get('steps')}"
    )
    assert llm.call_count == max_steps, (
        f"LLM chi duoc phep goi dung {max_steps} lan, thuc te da goi {llm.call_count} lan"
    )
    assert isinstance(result.get("tools_executed"), list), (
        "Truong tools_executed phai la mot danh sach"
    )


def test_unknown_tool():
    """DoD 2: Tool khong xac dinh tra ve observation bao loi thay vi lam sap chuong trinh."""
    llm = UnknownToolMockLLM()
    tools: Dict[str, Callable[[str], str]] = {
        "known_tool": lambda arg: "Ket qua hop le"
    }
    agent = ReActAgent(llm=llm, tools=tools, max_steps=5)
    result = agent.run("Goi tool khong ton tai trong danh sach")

    assert isinstance(result, dict), "Ket qua tra ve tu run() phai la kieu dict"
    assert result.get("success") is True, (
        "Agent phai tiep tuc vong lap va ket thuc thanh cong sau khi nhan observation bao loi"
    )
    assert len(llm.prompts) == 2, (
        "Agent phai thuc hien luot goi LLM thu hai de tiep nhan observation loi"
    )

    second_turn_prompt = llm.prompts[1]
    assert (
        "missing_tool" in second_turn_prompt
        or "Error" in second_turn_prompt
        or "error" in second_turn_prompt
    ), "Prompt gui den LLM o luot tiep theo phai chua thong bao loi ve tool khong hop le trong Observation"

    assert "missing_tool" not in result.get("tools_executed", []), (
        "Tool khong ton tai khong duoc ghi nhan vao danh sach tools_executed thanh cong"
    )


def test_final_answer_after_action():
    """DoD 3: Khong chap nhan Final Answer di sau mot Action chua qua thuc thi."""
    # 1. Kiem tra truc tiep tren ham parse:
    fabricated_output = (
        "Thought: Suy nghi truoc hanh dong\n"
        "Action: real_tool[hello]\n"
        "Observation: ket qua bia dat\n"
        "Final Answer: cau tra loi bia dat"
    )
    thought, tool_name, tool_arg, final_answer = parse(fabricated_output)
    assert tool_name == "real_tool", "Ham parse phai trich xuat dung ten cong cu can thuc thi"
    assert tool_arg == "hello", "Ham parse phai trich xuat dung tham so cua cong cu"
    assert final_answer is None, (
        "Ham parse khong duoc phep tra ve final_answer khi trong luot do con Action chua duoc moi truong thuc thi"
    )

    # 2. Kiem tra qua vong lap ReActAgent:
    executed_calls = []
    def real_tool(arg: str) -> str:
        executed_calls.append(arg)
        return f"Thuc thi thuc te: {arg}"

    llm = HallucinatingMockLLM()
    agent = ReActAgent(llm=llm, tools={"real_tool": real_tool}, max_steps=5)
    result = agent.run("Kiem tra bao ve action chua thuc thi")

    assert len(executed_calls) == 1 and executed_calls[0] == "hello", (
        "Cong cu real_tool bat buoc phai duoc thuc thi boi moi truong code truoc khi chap nhan Final Answer"
    )
    assert result.get("success") is True, (
        "Agent phai hoan thanh thanh cong sau khi chay tool that"
    )
    assert result.get("final_answer") == "cau tra loi hop le sau khi chay tool", (
        "Final Answer cuoi cung phai den tu luot suy luan hop le sau khi nhan observation that"
    )
    assert "real_tool" in result.get("tools_executed", []), (
        "Danh sach tools_executed phai ghi nhan cong cu da chay thuc te"
    )


def test_nested_brackets():
    """DoD 4: Phan tich cu phap chinh xac tham so chua cap ngoac long nhau nhu calculate[(2+3)*4]."""
    # 1. Kiem tra truc tiep ham parse voi ngoac long don gian va ngoac long phuc tap:
    output_nested = "Thought: Tinh toan\nAction: calculate[(2+3)*4]"
    thought, tool_name, tool_arg, final_answer = parse(output_nested)
    assert tool_name == "calculate", "Ham parse phai trich xuat dung ten tool la 'calculate'"
    assert tool_arg == "(2+3)*4", (
        f"Tham so tool phai giu nguyen toan bo bieu thuc '(2+3)*4', khong bi ngat cut o dau ngoac dau tien. Thuc te nhan '{tool_arg}'"
    )

    output_deep = "Action: evaluate[((10 + 5) * (2 + 1))]"
    _, deep_name, deep_arg, _ = parse(output_deep)
    assert deep_name == "evaluate", "Ham parse phai trich xuat dung ten tool la 'evaluate'"
    assert deep_arg == "((10 + 5) * (2 + 1))", (
        f"Tham so tool phai giu nguyen bieu thuc long sau '((10 + 5) * (2 + 1))', thuc te nhan '{deep_arg}'"
    )

    # 2. Kiem tra qua ReActAgent loop:
    def safe_calc(expr: str) -> str:
        try:
            return str(eval(expr, {"__builtins__": None}, {}))
        except Exception as err:
            return f"Calc Error: {err}"

    llm = NestedBracketMockLLM()
    agent = ReActAgent(llm=llm, tools={"calculate": safe_calc}, max_steps=4)
    result = agent.run("Tinh bieu thuc co ngoac long")

    assert result.get("success") is True, (
        "Agent phai hoan thanh thanh cong khi tinh toan bieu thuc ngoac long"
    )
    assert result.get("final_answer") == "20", "Ket qua cuoi cung phai la '20'"
    assert "calculate" in result.get("tools_executed", [])
