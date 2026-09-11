"""
Bài tập 3: Tìm giá trị lớn nhất của từng cặp 2 phần tử liền kề.
Mở rộng: Kỹ thuật cửa sổ trượt (Sliding Window) & Tương đồng với 1D Max Pooling trong Deep Learning.
"""

from typing import List


def pairwise_max(data: List[int]) -> List[int]:
    """
    Tìm giá trị lớn nhất của từng cặp 2 phần tử liền kề [data[i], data[i+1]].
    
    Args:
        data (List[int]): Danh sách số đầu vào.
        
    Returns:
        List[int]: Danh sách gồm len(data) - 1 phần tử lớn nhất của từng cặp.
        
    Edge cases handled:
        - Danh sách có ít hơn 2 phần tử: trả về [] vì không thể tạo cặp.
    """
    if len(data) < 2:
        return []
        
    result = []
    for i in range(len(data) - 1):
        num = data[i]
        num_next = data[i + 1]
        result.append(max(num, num_next))
        
    return result


# Dữ liệu gốc
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
result = pairwise_max(data3)

if __name__ == "__main__":
    print(result)