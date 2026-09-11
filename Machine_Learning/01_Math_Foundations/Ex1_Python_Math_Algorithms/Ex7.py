"""
Bài tập 7: Tìm các số chẵn trong đoạn [2000, 3000].
Mở rộng: Cung cấp cả 2 biến thể:
  1. Số chẵn thông thường: i % 2 == 0
  2. Mọi chữ số đều chẵn (All digits even): ví dụ 2000, 2002, 2024, 2888,...
"""

from typing import List


def find_even_numbers(start: int = 2000, end: int = 3000) -> List[int]:
    """
    Tìm tất cả các số chẵn trong khoảng [start, end] (bao gồm 2 đầu mút).
    
    Args:
        start (int): Điểm bắt đầu (mặc định 2000).
        end (int): Điểm kết thúc (mặc định 3000).
        
    Returns:
        List[int]: Danh sách các số chẵn.
    """
    if start > end:
        return []
    return [i for i in range(start, end + 1) if (i % 2 == 0)]


def find_numbers_all_even_digits(start: int = 2000, end: int = 3000) -> List[int]:
    """
    Biến thể phỏng vấn thường gặp:
    Tìm tất cả các số trong khoảng [start, end] mà MỌI chữ số của nó đều là số chẵn.
    Ví dụ: 2002 (chữ số: 2, 0, 0, 2 đều chẵn) -> Thỏa mãn.
           2001 (chữ số 1 lẻ) -> Loại bỏ.
    """
    if start > end:
        return []
    even_digits = {'0', '2', '4', '6', '8'}
    return [i for i in range(start, end + 1) if all(ch in even_digits for ch in str(abs(i)))]


# Dữ liệu gốc theo đề bài Ex7
_matched = find_even_numbers(2000, 3000)
result = [str(x) for x in _matched]

if __name__ == "__main__":
    print(', '.join(result))