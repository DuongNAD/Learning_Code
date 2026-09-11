"""
================================================================================
   TRUNG TÂM BÀI TẬP THỰC HÀNH PYTHON & MACHINE LEARNING (PRACTICE LAB)
================================================================================
Chào bạn! Đây là file thực hành chuyên sâu nâng cấp từ bộ bài tập Ex1 -> Ex8.
Gồm 16 bài tập từ cơ bản đến ứng dụng Machine Learning thực tế.

CÁCH HỌC VÀ LÀM BÀI:
1. Đọc yêu cầu và gợi ý (HINTS) trong từng hàm bên dưới.
2. Viết code của bạn thay thế dòng `raise NotImplementedError(...)`.
3. Chạy kiểm tra kết quả ngay trong terminal:
     py practice_exercises.py          # Kiểm tra toàn bộ 16 bài
     py practice_exercises.py 1        # Chỉ kiểm tra Bài 1
     py practice_exercises.py 8        # Chỉ kiểm tra Bài 8
4. Nếu gặp khó khăn, bạn có thể tham khảo file 'solutions_practice.py'
   hoặc mở ứng dụng trực quan 'launch_hub.py' trên trình duyệt!
================================================================================
"""

import sys
from typing import List, Tuple, Dict, Any, Optional, Callable, Set, Union

# Đảm bảo in tiếng Việt không bị lỗi font trên Windows PowerShell / CMD
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# MẸO: Đặt cờ này thành True nếu bạn muốn chạy thử bộ lời giải mẫu hoàn chỉnh
USE_SOLUTIONS_FOR_TESTING = False

try:
    import solutions_practice as sol
except ImportError:
    sol = None


# ==============================================================================
# CHỦ ĐỀ 1: PHÂN LOẠI DỮ LIỆU & HÀM KÍCH HOẠT (EX1)
# ==============================================================================

def practice_1_1_sign_and_zero_classifier(numbers: List[float]) -> Dict[str, Any]:
    """
    [BÀI 1.1] Phân loại 3 nhóm: Dương (>0), Số Không (==0), Âm (<0).
    
    Yêu cầu:
    - Trả về dictionary có 3 keys: 'positive', 'zero', 'negative'.
    - 'positive': dict gồm {'values': list_số_dương, 'count': số_lượng, 'sum': tổng, 'mean': trung_bình (làm tròn 4 chữ số)}
    - 'zero': dict gồm {'count': số_lượng_số_0}
    - 'negative': dict gồm {'values': list_số_âm, 'count': số_lượng, 'sum': tổng, 'mean': trung_bình (làm tròn 4 chữ số)}
    - Nếu danh sách con rỗng, sum = 0.0 và mean = 0.0.
    
    Gợi ý:
    - Duyệt qua từng số x trong numbers, kiểm tra x > 0, x < 0, và x == 0.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_1_1_sign_and_zero_classifier(numbers)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 1.1!")


def practice_1_2_relu_and_leaky_relu(features: List[float], alpha: float = 0.01) -> Dict[str, Any]:
    """
    [BÀI 1.2 - Ứng dụng Machine Learning] Cài đặt hàm kích hoạt ReLU & Leaky ReLU.
    
    Yêu cầu:
    - ReLU: f(x) = max(0.0, x)
    - Leaky ReLU: f(x) = x nếu x >= 0 else round(alpha * x, 4)
    - Đếm số lượng 'dead_neuron_count' (các giá trị x <= 0)
    - Tính tỷ lệ phần trăm nơ-ron chết: 'dead_neuron_rate' = (dead_count / total) * 100 (làm tròn 2 chữ số)
    
    Trả về Dict:
    {
        'relu_output': List[float],
        'leaky_relu_output': List[float],
        'dead_neuron_count': int,
        'dead_neuron_rate': float
    }
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_1_2_relu_and_leaky_relu(features, alpha)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 1.2!")


# ==============================================================================
# CHỦ ĐỀ 2: TẦN SUẤT & LỌC TỪ VỰNG NLP (EX2)
# ==============================================================================

def practice_2_1_top_k_frequent_words(text: str, k: int, min_len: int = 3) -> List[Tuple[str, int]]:
    """
    [BÀI 2.1] Tìm Top K từ xuất hiện nhiều nhất trong văn bản.
    
    Yêu cầu:
    - Làm sạch văn bản: chuyển thành chữ thường, dấu câu biến thành khoảng trắng.
    - Lọc các từ có độ dài >= min_len.
    - Trả về danh sách k tuples [(word, count), ...] xếp theo số lần xuất hiện giảm dần.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_2_1_top_k_frequent_words(text, k, min_len)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 2.1!")


def practice_2_2_nlp_vocabulary_pruner(
    corpus: List[List[str]], 
    min_freq: int = 2, 
    max_freq: int = 10
) -> List[str]:
    """
    [BÀI 2.2 - Ứng dụng NLP] Cắt tỉa tập từ vựng (Vocabulary Pruning).
    
    Yêu cầu:
    - Cho danh sách các câu đã tách từ: corpus = [['hello', 'world'], ['world', 'machine', 'learning']]
    - Tính tổng số lần xuất hiện của từng từ (chuẩn hóa chữ thường).
    - Chỉ giữ lại các từ có tần suất thỏa mãn: min_freq <= freq <= max_freq.
    - Sắp xếp kết quả theo tần suất giảm dần, nếu bằng nhau thì theo thứ tự bảng chữ cái.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_2_2_nlp_vocabulary_pruner(corpus, min_freq, max_freq)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 2.2!")


# ==============================================================================
# CHỦ ĐỀ 3: CỬA SỔ TRƯỢT & 1D MAX POOLING (EX3)
# ==============================================================================

def practice_3_1_moving_average_1d(signal: List[float], window_size: int) -> List[float]:
    """
    [BÀI 3.1] Tính trung bình trượt (Moving Average) làm mịn chuỗi tín hiệu.
    
    Yêu cầu:
    - Với mỗi cửa sổ độ dài window_size, tính giá trị trung bình (làm tròn 4 chữ số).
    - Kết quả có độ dài = len(signal) - window_size + 1.
    - Nếu len(signal) < window_size hoặc window_size <= 0: trả về [].
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_3_1_moving_average_1d(signal, window_size)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 3.1!")


def practice_3_2_max_pooling_1d(
    signal: List[float], 
    pool_size: int = 2, 
    stride: int = 2
) -> List[float]:
    """
    [BÀI 3.2 - Ứng dụng Deep Learning] Mô phỏng 1D Max Pooling Layer.
    
    Yêu cầu:
    - Trượt cửa sổ kích thước pool_size qua signal, mỗi bước nhảy cách stride phần tử.
    - Lấy giá trị lớn nhất trong mỗi cửa sổ.
    - Dừng lại khi không đủ pool_size phần tử tiếp theo.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_3_2_max_pooling_1d(signal, pool_size, stride)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 3.2!")


# ==============================================================================
# CHỦ ĐỀ 4: HOÁN VỊ & GRID SEARCH HYPERPARAMETERS (EX4)
# ==============================================================================

def practice_4_1_recursive_permutations(
    elements: List[Any], 
    r: Optional[int] = None
) -> List[Tuple[Any, ...]]:
    """
    [BÀI 4.1] Tự cài đặt thuật toán đệ quy quay lui (Backtracking) để sinh hoán vị chập r.
    
    Yêu cầu:
    - Không dùng thư viện itertools.
    - Trả về danh sách tất cả các tuple hoán vị chập r. Nếu r là None, mặc định r = len(elements).
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_4_1_recursive_permutations(elements, r)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 4.1!")


def practice_4_2_grid_search_combinations(param_grid: Dict[str, List[Any]]) -> List[Dict[str, Any]]:
    """
    [BÀI 4.2 - Ứng dụng Machine Learning] Sinh không gian siêu tham số GridSearchCV.
    
    Ví dụ:
        param_grid = {
            'lr': [0.01, 0.1],
            'batch_size': [16, 32]
        }
    Trả về 4 dictionary cấu hình tương ứng với tích Descartes (Cartesian product).
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_4_2_grid_search_combinations(param_grid)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 4.2!")


# ==============================================================================
# CHỦ ĐỀ 5: KHỬ TRÙNG GIỮ THỨ TỰ & GỘP BẢN GHI (EX5)
# ==============================================================================

def practice_5_1_ordered_deduplication(
    items: List[Any], 
    key_func: Optional[Callable[[Any], Any]] = None
) -> List[Any]:
    """
    [BÀI 5.1] Khử trùng lặp danh sách giữ nguyên thứ tự xuất hiện ban đầu.
    
    Yêu cầu:
    - Hỗ trợ tham số key_func tùy chọn (ví dụ: key_func=str.lower để khử trùng không phân biệt hoa thường).
    - Độ phức tạp thời gian đạt O(N) nhờ sử dụng tập băm (hash set).
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_5_1_ordered_deduplication(items, key_func)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 5.1!")


def practice_5_2_merge_feature_dictionaries(
    dataset_a: List[Dict[str, Any]], 
    dataset_b: List[Dict[str, Any]], 
    id_key: str = "id"
) -> List[Dict[str, Any]]:
    """
    [BÀI 5.2 - Ứng dụng Làm sạch Dữ liệu] Hợp nhất 2 bảng bản ghi theo khóa định danh.
    
    Yêu cầu:
    - Nối các bản ghi có cùng id_key.
    - Nếu trường dữ liệu là danh sách (list), gộp 2 danh sách và khử trùng giữ thứ tự.
    - Nếu không phải list, bản ghi sau (dataset_b) ghi đè bản ghi trước.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_5_2_merge_feature_dictionaries(dataset_a, dataset_b, id_key)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 5.2!")


# ==============================================================================
# CHỦ ĐỀ 6: LỌC CHIA HẾT & PHÂN TÁCH K-FOLD (EX6)
# ==============================================================================

def practice_6_1_custom_filter_range(
    start: int, 
    end: int, 
    divisors: List[int], 
    exclude_divisors: List[int]
) -> List[int]:
    """
    [BÀI 6.1] Lọc các số trong [start, end] thỏa mãn:
    - Chia hết cho TẤT CẢ các số trong divisors.
    - KHÔNG chia hết cho BẤT KỲ số nào trong exclude_divisors.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_6_1_custom_filter_range(start, end, divisors, exclude_divisors)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 6.1!")


def practice_6_2_kfold_split_indices(
    n_samples: int, 
    n_splits: int = 5, 
    shuffle: bool = False, 
    seed: int = 42
) -> List[Tuple[List[int], List[int]]]:
    """
    [BÀI 6.2 - Ứng dụng Đánh giá Mô hình ML] Tự cài đặt K-Fold Cross Validation.
    
    Yêu cầu:
    - Chia n_samples chỉ số [0, 1, ..., n_samples - 1] thành n_splits phần bằng nhau
      (hoặc chênh lệch tối đa 1 phần tử nếu không chia hết).
    - Trả về danh sách gồm n_splits tuple: (train_indices, val_indices).
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_6_2_kfold_split_indices(n_samples, n_splits, shuffle, seed)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 6.2!")


# ==============================================================================
# CHỦ ĐỀ 7: CHỮ SỐ CHẴN & PHÂN LOẠI BIT PARITY (EX7)
# ==============================================================================

def practice_7_1_all_even_digits(start: int, end: int) -> List[int]:
    """
    [BÀI 7.1] Tìm các số trong [start, end] mà MỌI chữ số đều là số chẵn.
    
    Ví dụ:
    - 2000, 2002, 2024, 2888 -> Thỏa mãn
    - 2001, 2023 -> Loại bỏ vì chứa chữ số lẻ 1, 3
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_7_1_all_even_digits(start, end)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 7.1!")


def practice_7_2_binary_parity_and_hamming(numbers: List[int]) -> Dict[str, Any]:
    """
    [BÀI 7.2 - Xử lý Nhị phân / Feature Hashing] Phân loại Parity bit nhị phân.
    
    Yêu cầu:
    - Đếm số lượng bit 1 trong biểu diễn nhị phân của từng số (Hamming weight).
    - Phân loại:
      + even_parity_numbers: danh sách các số có số bit 1 là số chẵn.
      + odd_parity_numbers: danh sách các số có số bit 1 là số lẻ.
      + hamming_weights: dict ánh xạ {số: số_lượng_bit_1}.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_7_2_binary_parity_and_hamming(numbers)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 7.2!")


# ==============================================================================
# CHỦ ĐỀ 8: WORD LADDER & BI-DIRECTIONAL BFS (EX8)
# ==============================================================================

def practice_8_1_word_ladder_one_letter_diff(
    begin_word: str, 
    end_word: str, 
    word_list: List[str]
) -> List[str]:
    """
    [BÀI 8.1] Word Ladder kinh điển (LeetCode 127):
    Mỗi bước biến đổi đúng 1 chữ cái sang một từ có trong word_list.
    Tìm đường đi ngắn nhất bằng thuật toán BFS.
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_8_1_word_ladder_one_letter_diff(begin_word, end_word, word_list)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 8.1!")


def practice_8_2_bidirectional_bfs_chain(
    start_word: str, 
    end_word: str, 
    filename: str = "wordsEn.txt"
) -> Any:
    """
    [BÀI 8.2 - Tối ưu Đồ thị] Bi-directional BFS cho chuỗi từ Suffix(2) == Prefix(2).
    
    Tìm kiếm 2 chiều: 1 đầu đi từ start_word tiến tới, 1 đầu đi từ end_word lùi lại.
    Khi 2 hướng gặp nhau tại cùng 1 từ, lập tức kết nối và trả về kết quả!
    """
    if USE_SOLUTIONS_FOR_TESTING:
        return sol.solution_8_2_bidirectional_bfs_chain(start_word, end_word, filename)
        
    # TODO: Viết code thực hành của bạn tại đây
    raise NotImplementedError("Hãy tự viết code cho bài 8.2!")


# ==============================================================================
# BỘ KIỂM THỬ TỰ ĐỘNG (INTERACTIVE TEST RUNNER)
# ==============================================================================

def get_test_suites() -> Dict[int, List[Tuple[str, Callable, Callable]]]:
    """Trả về định nghĩa toàn bộ 16 bài test kiểm thử tự động."""
    return {
        1: [
            (
                "Bài 1.1: Phân loại số âm/dương/0",
                lambda: practice_1_1_sign_and_zero_classifier([-5, 0, 10, -2, 0, 7]),
                lambda res: (
                    res["positive"]["count"] == 2 and 
                    res["positive"]["sum"] == 17.0 and 
                    res["zero"]["count"] == 2 and 
                    res["negative"]["count"] == 2 and
                    res["negative"]["sum"] == -7.0
                )
            ),
            (
                "Bài 1.2: ReLU & Leaky ReLU & Dead Neurons",
                lambda: practice_1_2_relu_and_leaky_relu([-2.0, 0.0, 3.0, -1.0], alpha=0.1),
                lambda res: (
                    res["relu_output"] == [0.0, 0.0, 3.0, 0.0] and
                    res["leaky_relu_output"] == [-0.2, 0.0, 3.0, -0.1] and
                    res["dead_neuron_count"] == 3 and
                    res["dead_neuron_rate"] == 75.0
                )
            )
        ],
        2: [
            (
                "Bài 2.1: Top K từ xuất hiện nhiều nhất",
                lambda: practice_2_1_top_k_frequent_words("Machine learning is fun. Learning machine models is great!", k=2, min_len=3),
                lambda res: [w for w, c in res] == ["learning", "machine"] and res[0][1] == 2
            ),
            (
                "Bài 2.2: Cắt tỉa từ vựng NLP (Pruning)",
                lambda: practice_2_2_nlp_vocabulary_pruner(
                    [["ai", "data", "model"], ["data", "model", "model"], ["noise"]],
                    min_freq=2, max_freq=2
                ),
                lambda res: res == ["data"]
            )
        ],
        3: [
            (
                "Bài 3.1: Trung bình trượt 1D (Moving Average)",
                lambda: practice_3_1_moving_average_1d([10, 20, 30, 40, 50], window_size=3),
                lambda res: res == [20.0, 30.0, 40.0]
            ),
            (
                "Bài 3.2: 1D Max Pooling",
                lambda: practice_3_2_max_pooling_1d([1, 5, 2, 8, 3, 9, 4, 6], pool_size=2, stride=2),
                lambda res: res == [5, 8, 9, 6]
            )
        ],
        4: [
            (
                "Bài 4.1: Hoán vị đệ quy (Recursive Permutations)",
                lambda: practice_4_1_recursive_permutations([1, 2, 3]),
                lambda res: len(res) == 6 and (1, 2, 3) in res and (3, 2, 1) in res
            ),
            (
                "Bài 4.2: Tổ hợp siêu tham số GridSearchCV",
                lambda: practice_4_2_grid_search_combinations({"lr": [0.01, 0.1], "batch": [16, 32]}),
                lambda res: len(res) == 4 and {"lr": 0.01, "batch": 16} in res
            )
        ],
        5: [
            (
                "Bài 5.1: Khử trùng lặp giữ thứ tự kèm hàm key",
                lambda: practice_5_1_ordered_deduplication(["Apple", "banana", "APPLE", "orange", "BANANA"], key_func=str.lower),
                lambda res: res == ["Apple", "banana", "orange"]
            ),
            (
                "Bài 5.2: Gộp danh sách bản ghi Feature Store",
                lambda: practice_5_2_merge_feature_dictionaries(
                    [{"id": 1, "tags": ["nlp", "ai"]}, {"id": 2, "tags": ["cv"]}],
                    [{"id": 1, "tags": ["ai", "ml"], "score": 9.5}],
                    id_key="id"
                ),
                lambda res: res[0]["tags"] == ["nlp", "ai", "ml"] and res[0]["score"] == 9.5
            )
        ],
        6: [
            (
                "Bài 6.1: Bộ lọc chia hết tùy biến",
                lambda: practice_6_1_custom_filter_range(1, 40, divisors=[3], exclude_divisors=[2]),
                lambda res: res == [3, 9, 15, 21, 27, 33, 39]
            ),
            (
                "Bài 6.2: Chia K-Fold Cross Validation",
                lambda: practice_6_2_kfold_split_indices(10, n_splits=5, shuffle=False),
                lambda res: len(res) == 5 and res[0][1] == [0, 1] and len(res[0][0]) == 8
            )
        ],
        7: [
            (
                "Bài 7.1: Số có toàn bộ chữ số chẵn",
                lambda: practice_7_1_all_even_digits(2000, 2025),
                lambda res: 2000 in res and 2002 in res and 2020 in res and 2024 in res and 2001 not in res
            ),
            (
                "Bài 7.2: Parity Bit nhị phân & Hamming weight",
                lambda: practice_7_2_binary_parity_and_hamming([3, 4, 7, 8]),
                lambda res: (
                    3 in res["even_parity_numbers"] and   # bin(3)='11' (2 bits -> chẵn)
                    4 in res["odd_parity_numbers"] and    # bin(4)='100' (1 bit -> lẻ)
                    res["hamming_weights"][7] == 3
                )
            )
        ],
        8: [
            (
                "Bài 8.1: Word Ladder khác đúng 1 ký tự",
                lambda: practice_8_1_word_ladder_one_letter_diff("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
                lambda res: len(res) == 5 and res[0] == "hit" and res[-1] == "cog"
            ),
            (
                "Bài 8.2: Bi-directional BFS Word Chain",
                lambda: (
                    practice_8_2_bidirectional_bfs_chain("head", "tail"),
                    practice_8_2_bidirectional_bfs_chain("apple", "lemon")
                ),
                lambda res_tuple: (
                    isinstance(res_tuple[0], list) and 
                    len(res_tuple[0]) >= 2 and 
                    res_tuple[0][0] == "head" and 
                    res_tuple[0][-1] == "tail" and
                    all(res_tuple[0][i][-2:] == res_tuple[0][i+1][:2] for i in range(len(res_tuple[0]) - 1)) and
                    res_tuple[1] == ["apple", "lemon"]
                )
            )
        ]
    }


def run_single_test(topic_num: int, sub_idx: int) -> Tuple[bool, str, Any]:
    """
    Chạy kiểm thử cho đúng 1 bài tập (sub_idx: 0 hoặc 1).
    Trả về (passed: bool, message: str, raw_output: Any).
    """
    tests = get_test_suites()
    if topic_num not in tests or sub_idx >= len(tests[topic_num]):
        return False, f"Không tìm thấy bài tập {topic_num}.{sub_idx + 1}", None
        
    name, run_fn, verify_fn = tests[topic_num][sub_idx]
    try:
        output = run_fn()
        if verify_fn(output):
            return True, f"[PASS] {name}", output
        else:
            return False, f"[FAIL] {name} -> Kết quả chưa đúng: {output}", output
    except NotImplementedError:
        return False, f"[TODO] {name} -> Chưa cài đặt code (NotImplementedError). Hãy tự viết code thay thế!", None
    except Exception as e:
        return False, f"[ERR]  {name} -> Lỗi ngoại lệ: {e}", None


def run_tests_for_topic(topic_num: int) -> Tuple[int, int]:
    """Chạy kiểm thử cho 1 chủ đề bài tập cụ thể. Trả về (passed, total)."""
    tests = get_test_suites()
    if topic_num not in tests:
        print(f"Chủ đề {topic_num} không hợp lệ (chỉ từ 1 đến 8).")
        return 0, 0
        
    passed = 0
    total = len(tests[topic_num])
    print(f"\n--- ĐANG KIỂM TRA CHỦ ĐỀ {topic_num} ---")
    for i in range(total):
        ok, msg, _ = run_single_test(topic_num, i)
        if ok:
            passed += 1
            print(f"  {msg}")
        else:
            print(f"  {msg}")
            
    return passed, total


def main():
    print("=" * 65)
    print("  TRÌNH CHẤM ĐIỂM BÀI TẬP THỰC HÀNH PYTHON & MACHINE LEARNING")
    print("=" * 65)
    
    if USE_SOLUTIONS_FOR_TESTING:
        print("[LƯU Ý] Đang bật chế độ kiểm tra bằng LỜI GIẢI MẪU (USE_SOLUTIONS_FOR_TESTING=True)")
    else:
        print("[LƯU Ý] Đang chấm code do BẠN tự viết trong file này!")
        print("        (Nếu muốn xem toàn bộ test pass mẫu, đổi biến USE_SOLUTIONS_FOR_TESTING = True)")
        
    topics = list(range(1, 9))
    if len(sys.argv) > 1:
        try:
            chosen = int(sys.argv[1])
            topics = [chosen]
        except ValueError:
            pass
            
    total_passed = 0
    total_tests = 0
    
    for t in topics:
        p, t_cnt = run_tests_for_topic(t)
        total_passed += p
        total_tests += t_cnt
        
    print("\n" + "=" * 65)
    print(f"  KẾT QUẢ TỔNG KẾT: {total_passed}/{total_tests} bài kiểm thử thành công (PASS)")
    if total_passed == total_tests and total_tests > 0:
        print("  XUẤT SẮC! Bạn đã hoàn thành toàn bộ các bài tập thực hành!")
    elif total_passed > 0:
        print("  Rất tốt! Hãy tiếp tục hoàn thiện các bài tập còn lại nhé!")
    else:
        print("  Bắt đầu làm bài nào! Mở file practice_exercises.py và viết code nhé!")
    print("=" * 65)


if __name__ == "__main__":
    main()
