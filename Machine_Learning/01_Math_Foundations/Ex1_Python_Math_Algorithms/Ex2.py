"""
Bài tập 2: Tìm các phần tử xuất hiện nhiều hơn k lần.
Mở rộng: Kết nối tư duy NLP (Vocabulary pruning, loại bỏ từ hiếm / Stop words).
"""

from collections import Counter
from typing import List, Any


def find_elements_greater_than_k(data: List[Any], k: int) -> List[Any]:
    """
    Tìm các phần tử có tần suất xuất hiện > k trong danh sách data.
    Giữ thứ tự xuất hiện đầu tiên của các phần tử trong kết quả.
    
    Args:
        data (List[Any]): Danh sách phần tử (số, chuỗi, v.v.).
        k (int): Ngưỡng số lần xuất hiện tối thiểu (phải lớn hơn k).
        
    Returns:
        List[Any]: Danh sách các phần tử thỏa mãn tần suất > k.
        
    Edge cases handled:
        - Danh sách rỗng: trả về [].
        - k âm: trả về tất cả phần tử duy nhất (tần suất >= 1 > k).
        - k lớn hơn độ dài danh sách: trả về [].
    """
    if not data:
        return []
        
    counts = Counter(data)
    result = []
    for item in counts:
        if counts[item] > k:
            result.append(item)
            
    return result


# Dữ liệu gốc
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
counts = Counter(data2)
result = find_elements_greater_than_k(data2, k)

if __name__ == "__main__":
    print(result)