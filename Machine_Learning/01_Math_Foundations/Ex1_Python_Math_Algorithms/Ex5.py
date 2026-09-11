"""
Bài tập 5: Gộp các danh sách con tương ứng và loại bỏ trùng lặp.
Mở rộng: Kỹ thuật khử trùng giữ nguyên thứ tự (Ordered Deduplication) trong làm sạch dữ liệu (Data Cleaning).
"""

from typing import List, Any


def merge_sublists_unique(list1: List[List[Any]], list2: List[List[Any]]) -> List[List[Any]]:
    """
    Gộp từng cặp danh sách con tương ứng tại chỉ số i: list1[i] + list2[i],
    sau đó loại bỏ các phần tử trùng lặp nhưng bảo toàn thứ tự xuất hiện ban đầu.
    
    Args:
        list1 (List[List[Any]]): Danh sách các list con thứ nhất.
        list2 (List[List[Any]]): Danh sách các list con thứ hai.
        
    Returns:
        List[List[Any]]: Danh sách các list con đã gộp và khử trùng.
        
    Edge cases handled:
        - Độ dài khác nhau: lấy theo độ dài tối thiểu của 2 danh sách.
        - Danh sách rỗng: trả về [].
    """
    result = []
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        merged = list(dict.fromkeys(list1[i] + list2[i]))
        result.append(merged)
    return result


# Dữ liệu gốc
data5_list1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]
result = merge_sublists_unique(data5_list1, data5_list2)

if __name__ == "__main__":
    print(result)