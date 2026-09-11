"""
Bài tập 6: Tìm các số chia hết cho 7 nhưng không phải bội số của 5 trong đoạn [2000, 3200].
Mở rộng: Kỹ thuật lọc và phân đoạn dữ liệu (Data Filtering, Stratification).
"""

from typing import List


def find_numbers_div7_not5(start: int = 2000, end: int = 3200) -> List[int]:
    """
    Tìm tất cả các số nguyên trong khoảng [start, end] (bao gồm 2 đầu mút)
    thỏa mãn điều kiện: chia hết cho 7 và không chia hết cho 5.
    
    Args:
        start (int): Điểm bắt đầu (mặc định 2000).
        end (int): Điểm kết thúc (mặc định 3200).
        
    Returns:
        List[int]: Danh sách các số thỏa mãn.
        
    Edge cases handled:
        - start > end: trả về [].
    """
    if start > end:
        return []
    return [i for i in range(start, end + 1) if (i % 7 == 0) and (i % 5 != 0)]


# Dữ liệu gốc
_matched = find_numbers_div7_not5(2000, 3200)
result = [str(x) for x in _matched]

if __name__ == "__main__":
    print(', '.join(result))