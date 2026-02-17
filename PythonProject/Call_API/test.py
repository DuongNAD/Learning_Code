from google import genai
from google.genai import types
import sys

MY_API_KEY = "AIzaSyClajyeMtMUT_eGQw6OaMRoPQDnUZLO-sw"

sys_instruct = """
Bạn là một trợ lý AI ân cần, tinh tế và luôn truyền cảm hứng.
Người dùng của bạn là "Dương" (Nguyễn Anh Dương).

Phong cách giao tiếp:
- Luôn trả lời với giọng điệu nhẹ nhàng, quan tâm và thân thiện.
- Khi phù hợp, hãy đưa ra những lời động viên giúp Anh giảm bớt căng thẳng.
"""

def start_conversation():
    client = genai.Client(api_key=MY_API_KEY)

    model_id = "gemini-2.5-flash"

    try:
        chat = client.chats.create(
        model = model_id,
        config = types.GenerateContentConfig(
            system_instruction=sys_instruct,
            temperature=0.7
        )
        )
        print(f"--- Đã kết nối với API ---")
        print("Gõ 'exit' để thoát.\n")

        while True:
            user_input = input("Me: ")

            if user_input.lower() in ['exit', 'quit']:
                print("End")
                break

            if not user_input.strip():
                continue

            response = chat.send_message(user_input)
            print(f"API: {response.text}")
            print("-" * 50)

    except Exception as e:
        print(f"❌ Lỗi: {e}")


if __name__ == "__main__":
    start_conversation()