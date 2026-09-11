"""
Bài tập 8: Tìm chuỗi từ ngắn nhất nối 2 từ (Word Chain / Word Ladder).
Quy tắc: Từ tiếp theo có 2 chữ cái đầu (prefix) trùng với 2 chữ cái cuối (suffix) của từ trước.
Thuật toán: Breadth-First Search (BFS) tìm đường đi ngắn nhất trên đồ thị không trọng số.
"""

import os
import sys
from collections import defaultdict, deque
from typing import List, Union, Dict, Set, Tuple

# Đảm bảo tiếng Việt không bị lỗi mã hóa trên Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8-sig")
    except Exception:
        pass

# Bộ nhớ đệm tránh đọc lại file 1.15MB nhiều lần
_CACHE_FILENAME = None
_CACHE_VALID_WORDS = None
_CACHE_PREFIX_MAP = None


def load_dictionary(filename: str = "wordsEn.txt") -> Tuple[Set[str], Dict[str, List[str]]]:
    """
    Đọc từ điển từ file, lọc các từ có độ dài >= 3 và lập bảng tra prefix 2 ký tự.
    Tự động tìm kiếm cả ở thư mục hiện tại lẫn thư mục chứa file Ex8.py.
    """
    global _CACHE_FILENAME, _CACHE_VALID_WORDS, _CACHE_PREFIX_MAP
    
    # Tìm đường dẫn thực tế của file
    resolved_path = filename
    if not os.path.exists(resolved_path):
        alt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        if os.path.exists(alt_path):
            resolved_path = alt_path
            
    if not os.path.exists(resolved_path):
        raise FileNotFoundError(f"Không tìm thấy file '{filename}' (đã kiểm tra cả {resolved_path})")
        
    if _CACHE_FILENAME == resolved_path and _CACHE_VALID_WORDS is not None:
        return _CACHE_VALID_WORDS, _CACHE_PREFIX_MAP
        
    valid_words = set()
    prefix_map = defaultdict(list)
    
    with open(resolved_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            word = line.strip().lstrip('\ufeff').lower()
            if len(word) >= 3:
                valid_words.add(word)
                prefix = word[:2]
                prefix_map[prefix].append(word)
                
    _CACHE_FILENAME = resolved_path
    _CACHE_VALID_WORDS = valid_words
    _CACHE_PREFIX_MAP = prefix_map
    return valid_words, prefix_map


def find_shortest_word_chain(
    start_word: str, 
    end_word: str, 
    filename: str = "wordsEn.txt"
) -> Union[List[str], str]:
    """
    Tìm chuỗi từ ngắn nhất nối giữa start_word và end_word bằng thuật toán BFS.
    
    Args:
        start_word (str): Từ xuất phát.
        end_word (str): Từ đích đến.
        filename (str): Tên file từ điển.
        
    Returns:
        Union[List[str], str]: Danh sách các từ tạo thành chuỗi, hoặc thông báo lỗi / không tìm thấy.
    """
    try:
        valid_words, prefix_map = load_dictionary(filename)
    except Exception as e:
        return f"Lỗi khi đọc file: {e} (File reading error)"

    start_word = start_word.strip().lstrip('\ufeff').lstrip('ï»¿').lower()
    end_word = end_word.strip().lstrip('\ufeff').lstrip('ï»¿').lower()

    if start_word not in valid_words or end_word not in valid_words:
        return "Từ nhập vào phải có ít nhất 3 chữ cái và tồn tại trong file wordsEn.txt."

    if start_word == end_word:
        return [start_word]

    queue = deque([[start_word]])
    visited = {start_word}

    while queue:
        current_path = queue.popleft()
        last_word = current_path[-1]

        if last_word == end_word:
            return current_path

        suffix = last_word[-2:]

        for next_word in prefix_map.get(suffix, []):
            if next_word not in visited:
                visited.add(next_word)
                queue.append(current_path + [next_word])

    return "Không tìm thấy chuỗi nào kết nối 2 từ"


def main():
    start_word = input("Nhập từ 1: ")
    end_word = input("Nhập từ 2: ")

    result = find_shortest_word_chain(start_word, end_word)
    
    if isinstance(result, list):
        print("\nOutput:")
        print("\n".join(result))
    else:
        print("\n" + result)


if __name__ == "__main__":
    main()