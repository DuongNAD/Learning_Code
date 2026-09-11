"""
File khởi chạy trung tâm học tập trực quan (Visual Learning Hub).
Tự động mở trình duyệt và phục vụ giao diện trực quan hóa động Ex1 -> Ex8.

Cách sử dụng:
    py launch_hub.py
"""

import os
import sys
import webbrowser
import http.server
import socketserver
import threading
import time

# Đảm bảo in tiếng Việt không bị lỗi font trên Windows PowerShell
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Mặc định chuyển hướng về interactive_hub.html nếu vào trang chủ /
        if self.path == "/" or self.path == "":
            self.path = "/interactive_hub.html"
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/run_code":
            self._handle_run_code()
        elif self.path == "/api/word_chain":
            self._handle_word_chain()
        elif self.path == "/api/run_practice":
            self._handle_run_practice()
        else:
            self.send_error(404, "Endpoint not found")

    def _send_json(self, data, status=200):
        import json
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _handle_run_code(self):
        import json, subprocess
        content_len = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(content_len).decode('utf-8')
        try:
            req = json.loads(raw_body)
            ex_id = req.get("exercise_id", "1.1")
            user_code = req.get("code", "")
            parts = ex_id.split('.')
            topic = int(parts[0])
            sub = int(parts[1])
            sub_idx = sub - 1

            func_map = {
                "1.1": "practice_1_1_sign_and_zero_classifier",
                "1.2": "practice_1_2_relu_and_leaky_relu",
                "2.1": "practice_2_1_top_k_frequent_words",
                "2.2": "practice_2_2_nlp_vocabulary_pruner",
                "3.1": "practice_3_1_moving_average_1d",
                "3.2": "practice_3_2_max_pooling_1d",
                "4.1": "practice_4_1_recursive_permutations",
                "4.2": "practice_4_2_grid_search_combinations",
                "5.1": "practice_5_1_ordered_deduplication",
                "5.2": "practice_5_2_merge_feature_dictionaries",
                "6.1": "practice_6_1_custom_filter_range",
                "6.2": "practice_6_2_kfold_split_indices",
                "7.1": "practice_7_1_all_even_digits",
                "7.2": "practice_7_2_binary_parity_and_hamming",
                "8.1": "practice_8_1_word_ladder_one_letter_diff",
                "8.2": "practice_8_2_bidirectional_bfs_chain",
            }
            target_func = func_map.get(ex_id, f"practice_{topic}_{sub}")

            runner_code = f"""
import sys, json
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import practice_exercises as pe

code_str = {json.dumps(user_code)}
ns = {{"__name__": "__practice__"}}

try:
    compiled = compile(code_str, "<practice_code>", "exec")
    exec(compiled, ns)
except SyntaxError as se:
    print(json.dumps({{"success": False, "error": f"Lỗi cú pháp (SyntaxError) dòng {{se.lineno}}: {{se.msg}}"}}))
    sys.exit(0)
except Exception as e:
    print(json.dumps({{"success": False, "error": f"Lỗi khi nạp code: {{e}}"}}))
    sys.exit(0)

user_fn = ns.get("{target_func}")
if user_fn is None:
    callables = [v for k, v in ns.items() if callable(v) and not k.startswith("_")]
    if callables:
        user_fn = callables[0]
    else:
        print(json.dumps({{"success": False, "error": "Không tìm thấy định nghĩa hàm nào trong code của bạn! Vui lòng giữ nguyên cấu trúc hàm mẫu."}}))
        sys.exit(0)

setattr(pe, "{target_func}", user_fn)
ok, msg, out = pe.run_single_test({topic}, {sub_idx})

print(json.dumps({{
    "success": ok,
    "message": msg,
    "output": str(out) if out is not None else None
}}, ensure_ascii=False))
"""
            proc = subprocess.run(
                [sys.executable, "-c", runner_code],
                cwd=DIRECTORY,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=8
            )

            if proc.stdout.strip():
                for line in reversed(proc.stdout.strip().split('\n')):
                    if line.strip().startswith('{') and line.strip().endswith('}'):
                        res_json = json.loads(line.strip())
                        self._send_json(res_json)
                        return
            
            if proc.stderr:
                self._send_json({"success": False, "error": proc.stderr.strip()})
            else:
                self._send_json({"success": False, "error": "Kiểm thử không phản hồi kết quả."})

        except subprocess.TimeoutExpired:
            self._send_json({"success": False, "error": "Hết thời gian chờ (Timeout > 8s)! Có thể code của bạn bị lặp vô tận (Infinite loop)."})
        except Exception as e:
            self._send_json({"success": False, "error": str(e)}, status=500)

    def _handle_word_chain(self):
        import json
        content_len = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(content_len).decode('utf-8')
        try:
            req = json.loads(raw_body)
            start_word = req.get("start", "").strip().lower()
            end_word = req.get("end", "").strip().lower()

            import Ex8
            res = Ex8.find_shortest_word_chain(start_word, end_word)
            if isinstance(res, list):
                self._send_json({"success": True, "path": res})
            else:
                self._send_json({"success": False, "error": res})
        except Exception as e:
            self._send_json({"success": False, "error": str(e)}, status=500)

    def _handle_run_practice(self):
        import json, subprocess
        content_len = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(content_len).decode('utf-8')
        try:
            req = json.loads(raw_body)
            topic = req.get("topic", "")
            cmd = [sys.executable, "practice_exercises.py"]
            if topic:
                cmd.append(str(topic))
            proc = subprocess.run(
                cmd,
                cwd=DIRECTORY,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=15
            )
            self._send_json({"success": proc.returncode == 0, "output": proc.stdout + proc.stderr})
        except Exception as e:
            self._send_json({"success": False, "error": str(e)}, status=500)

    def log_message(self, format, *args):
        # Giảm bớt log terminal
        pass


def find_available_port(start_port=8080, max_attempts=20):
    """Tìm cổng mạng còn trống để khởi chạy web server."""
    import socket
    for p in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', p)) != 0:
                return p
    return start_port


def main():
    port = find_available_port(PORT)
    url = f"http://localhost:{port}/interactive_hub.html"
    
    print("=" * 70)
    print("  🚀 PYTHON & MACHINE LEARNING INTERACTIVE VISUAL LAB")
    print("=" * 70)
    print(f"  Thư mục làm việc: {DIRECTORY}")
    print(f"  Đang phục vụ tại: {url}")
    print("  Đang tự động mở trình duyệt mặc định của bạn...")
    print("  Nhấn Ctrl+C trong cửa sổ này để dừng máy chủ bất kỳ lúc nào.")
    print("=" * 70)

    # Mở trình duyệt web sau 0.5s
    def open_browser():
        time.sleep(0.6)
        webbrowser.open(url)

    threading.Thread(target=open_browser, daemon=True).start()

    # Khởi chạy máy chủ HTTP
    with socketserver.TCPServer(("", port), CustomHTTPHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng máy chủ. Chúc bạn học tốt!")
            httpd.server_close()


if __name__ == "__main__":
    main()
