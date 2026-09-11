"""
Bài tập 4: Sinh các hoán vị của 3 phần tử khác nhau.
Mở rộng: Kỹ thuật quay lui (Backtracking), tìm kiếm không gian siêu tham số (Grid Search).
"""

from typing import List, Any


def generate_permutations_3(data: List[Any]) -> List[List[Any]]:
    """
    Sinh tất cả các hoán vị 3 phần tử phân biệt từ danh sách data (giả sử có ít nhất 3 phần tử).
    
    Args:
        data (List[Any]): Danh sách phần tử.
        
    Returns:
        List[List[Any]]: Danh sách các bộ 3 [i, j, k] với i != j, j != k, i != k.
        
    Edge cases handled:
        - len(data) < 3: trả về [] vì không thể chọn 3 phần tử khác nhau.
    """
    if len(data) < 3:
        return []
        
    permutations = []
    for i in data:
        for j in data:
            for k in data:
                if i != j and j != k and i != k:
                    permutations.append([i, j, k])
    return permutations


# Dữ liệu gốc
data4 = [1, 2, 3]
result = generate_permutations_3(data4)

if __name__ == "__main__":
    for perm in result:
        print(f"[{perm[0]}, {perm[1]}, {perm[2]}]")