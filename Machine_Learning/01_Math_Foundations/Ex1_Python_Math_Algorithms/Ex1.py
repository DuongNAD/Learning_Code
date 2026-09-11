"""
Bài tập 1: Phân loại số âm và số dương trong danh sách.
Mở rộng: Hỗ trợ hàm tái sử dụng, phân loại số 0, và kết nối tư duy Machine Learning (ReLU / Chuẩn hóa dữ liệu).
"""

from typing import List, Dict, Any


def separate_positive_negative(numbers: List[int]) -> Dict[str, Any]:
    """
    Phân loại danh sách số thành số dương (>= 0) và số âm (< 0).
    
    Args:
        numbers (List[int]): Danh sách các số nguyên đầu vào.
        
    Returns:
        Dict[str, Any]: Dictionary gồm:
            - 'pos_num': danh sách số dương (hoặc không âm)
            - 'pos_count': số lượng số dương
            - 'neg_num': danh sách số âm
            - 'neg_count': số lượng số âm
            
    Edge cases handled:
        - Danh sách rỗng: trả về các danh sách rỗng và count = 0.
        - Toàn số âm hoặc toàn số dương: xử lý bình thường.
    """
    pos_num = []
    neg_num = []
    
    for i in numbers:
        if i < 0:
            neg_num.append(i)
        else:
            pos_num.append(i)
            
    return {
        "pos_num": pos_num,
        "pos_count": len(pos_num),
        "neg_num": neg_num,
        "neg_count": len(neg_num)
    }


# Dữ liệu gốc
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

# Thực thi logic chuẩn
_result = separate_positive_negative(data1)
pos_num = _result["pos_num"]
pos_count = _result["pos_count"]
neg_num = _result["neg_num"]
neg_count = _result["neg_count"]

if __name__ == "__main__":
    print("Positive numbers: ", pos_num)
    print("Positive count: ", pos_count)
    print("Negative numbers: ", neg_num)
    print("Negative count: ", neg_count)