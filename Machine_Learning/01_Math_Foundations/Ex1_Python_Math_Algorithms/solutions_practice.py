"""
File Lời Giải Chuẩn & Giải Thích Chi Tiết Cho 16 Bài Tập Thực Hành.
Mỗi bài tập đi kèm:
- Cách giải tối ưu
- Phân tích độ phức tạp thời gian O(N) và không gian O(1)/O(N)
- Ý nghĩa thực tiễn trong Machine Learning & Xử lý Dữ liệu.
"""

import os
import math
import random
from collections import Counter, defaultdict, deque
from typing import List, Tuple, Dict, Any, Optional, Callable, Set, Union


# ==============================================================================
# CHỦ ĐỀ 1: PHÂN LOẠI DỮ LIỆU & HÀM KÍCH HOẠT (EX1 EXPANDED)
# ==============================================================================

def solution_1_1_sign_and_zero_classifier(numbers: List[float]) -> Dict[str, Any]:
    """
    Phân loại danh sách số thành 3 nhóm: dương (>0), số 0 (==0), âm (<0)
    và tính các đại lượng thống kê (count, sum, mean) cho từng nhóm.
    
    Độ phức tạp: O(N) thời gian (duyệt 1 lần), O(N) không gian lưu trữ.
    """
    pos = []
    neg = []
    zero_count = 0
    
    for x in numbers:
        if x > 0:
            pos.append(x)
        elif x < 0:
            neg.append(x)
        else:
            zero_count += 1
            
    pos_sum = sum(pos) if pos else 0.0
    neg_sum = sum(neg) if neg else 0.0
    
    return {
        "positive": {
            "values": pos,
            "count": len(pos),
            "sum": round(pos_sum, 4),
            "mean": round(pos_sum / len(pos), 4) if pos else 0.0
        },
        "zero": {
            "count": zero_count
        },
        "negative": {
            "values": neg,
            "count": len(neg),
            "sum": round(neg_sum, 4),
            "mean": round(neg_sum / len(neg), 4) if neg else 0.0
        }
    }


def solution_1_2_relu_and_leaky_relu(features: List[float], alpha: float = 0.01) -> Dict[str, Any]:
    """
    Áp dụng hàm kích hoạt ReLU: f(x) = max(0, x)
    và Leaky ReLU: f(x) = x nếu x >= 0 else alpha * x.
    Tính tỷ lệ nơ-ron 'bị chết' (dying ReLU percentage: giá trị <= 0).
    
    Ý nghĩa ML: ReLU là activation function phổ biến nhất trong Deep Learning.
    """
    if not features:
        return {
            "relu_output": [],
            "leaky_relu_output": [],
            "dead_neuron_count": 0,
            "dead_neuron_rate": 0.0
        }
        
    relu_out = [max(0.0, float(x)) for x in features]
    leaky_out = [float(x) if x >= 0 else round(alpha * float(x), 4) for x in features]
    
    dead_count = sum(1 for x in features if x <= 0)
    dead_rate = round((dead_count / len(features)) * 100.0, 2)
    
    return {
        "relu_output": relu_out,
        "leaky_relu_output": leaky_out,
        "dead_neuron_count": dead_count,
        "dead_neuron_rate": dead_rate
    }


# ==============================================================================
# CHỦ ĐỀ 2: TẦN SUẤT & LỌC TỪ VỰNG NLP (EX2 EXPANDED)
# ==============================================================================

def solution_2_1_top_k_frequent_words(text: str, k: int, min_len: int = 3) -> List[Tuple[str, int]]:
    """
    Tách từ trong chuỗi văn bản, loại bỏ ký tự đặc biệt, chuyển chữ thường,
    lọc các từ có độ dài >= min_len và trả về top k từ có tần suất cao nhất.
    
    Độ phức tạp: O(N log k) với heap hoặc O(N log U) với Counter.most_common().
    """
    if not text.strip() or k <= 0:
        return []
        
    # Loại bỏ dấu câu đơn giản
    clean_chars = [ch.lower() if ch.isalnum() or ch.isspace() else ' ' for ch in text]
    clean_text = "".join(clean_chars)
    tokens = [w for w in clean_text.split() if len(w) >= min_len]
    
    counts = Counter(tokens)
    # Sắp xếp theo tần suất giảm dần, nếu bằng nhau thì theo thứ tự alphabet
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:k]


def solution_2_2_nlp_vocabulary_pruner(
    corpus: List[List[str]], 
    min_freq: int = 2, 
    max_freq: int = 10
) -> List[str]:
    """
    Lọc danh sách từ vựng từ tập văn bản (corpus):
    Chỉ giữ lại các từ có tần suất xuất hiện tổng cộng trong khoảng [min_freq, max_freq].
    Loại bỏ từ quá hiếm (noise) và từ quá phổ biến (stop words).
    
    Giữ thứ tự từ theo tần suất giảm dần, nếu bằng nhau thì theo thứ tự alphabet.
    """
    all_words = []
    for doc in corpus:
        for word in doc:
            w = word.lower().strip()
            if w:
                all_words.append(w)
            
    counts = Counter(all_words)
    filtered = [
        word for word, cnt in counts.items() 
        if min_freq <= cnt <= max_freq
    ]
    
    # Sắp xếp theo tần suất giảm dần, sau đó alphabet
    filtered.sort(key=lambda w: (-counts[w], w))
    return filtered


# ==============================================================================
# CHỦ ĐỀ 3: CỬA SỔ TRƯỢT & 1D MAX POOLING (EX3 EXPANDED)
# ==============================================================================

def solution_3_1_moving_average_1d(signal: List[float], window_size: int) -> List[float]:
    """
    Tính trung bình trượt (Moving Average) với kích thước cửa sổ window_size.
    Dùng kỹ thuật sliding window O(N): duy trì tổng cửa sổ thay vì sum lại.
    
    Ý nghĩa ML: Khử nhiễu tín hiệu chuỗi thời gian (time series smoothing).
    """
    if not signal or window_size <= 0 or window_size > len(signal):
        return []
        
    result = []
    window_sum = sum(signal[:window_size])
    result.append(round(window_sum / window_size, 4))
    
    for i in range(window_size, len(signal)):
        window_sum += signal[i] - signal[i - window_size]
        result.append(round(window_sum / window_size, 4))
        
    return result


def solution_3_2_max_pooling_1d(
    signal: List[float], 
    pool_size: int = 2, 
    stride: int = 2
) -> List[float]:
    """
    Mô phỏng phép toán 1D Max Pooling trong Convolutional Neural Networks (CNNs).
    Trượt cửa sổ kích thước pool_size qua mảng với bước nhảy stride,
    tại mỗi vị trí lấy giá trị lớn nhất.
    """
    if not signal or pool_size <= 0 or stride <= 0 or pool_size > len(signal):
        return []
        
    result = []
    idx = 0
    while idx + pool_size <= len(signal):
        window = signal[idx : idx + pool_size]
        result.append(max(window))
        idx += stride
        
    return result


# ==============================================================================
# CHỦ ĐỀ 4: HOÁN VỊ & GRID SEARCH HYPERPARAMETERS (EX4 EXPANDED)
# ==============================================================================

def solution_4_1_recursive_permutations(
    elements: List[Any], 
    r: Optional[int] = None
) -> List[Tuple[Any, ...]]:
    """
    Sinh tất cả hoán vị hoặc chỉnh hợp chập r từ danh sách elements
    bằng thuật toán đệ quy quay lui (Backtracking).
    """
    if r is None:
        r = len(elements)
    if r > len(elements) or r < 0:
        return []
    if r == 0:
        return [()]
        
    result = []
    
    def backtrack(current_perm: List[Any], used_indices: Set[int]):
        if len(current_perm) == r:
            result.append(tuple(current_perm))
            return
            
        for i in range(len(elements)):
            if i not in used_indices:
                used_indices.add(i)
                current_perm.append(elements[i])
                backtrack(current_perm, used_indices)
                current_perm.pop()
                used_indices.remove(i)
                
    backtrack([], set())
    return result


def solution_4_2_grid_search_combinations(param_grid: Dict[str, List[Any]]) -> List[Dict[str, Any]]:
    """
    Sinh tất cả tổ hợp tham số từ một không gian tìm kiếm siêu tham số (GridSearchCV).
    Ví dụ: {'lr': [0.01, 0.1], 'batch': [16, 32]}
    Trả về 4 cấu hình dict kết hợp.
    """
    if not param_grid:
        return []
        
    keys = list(param_grid.keys())
    combinations = []
    
    def backtrack(key_idx: int, current_config: Dict[str, Any]):
        if key_idx == len(keys):
            combinations.append(dict(current_config))
            return
            
        key = keys[key_idx]
        values = param_grid[key]
        for val in values:
            current_config[key] = val
            backtrack(key_idx + 1, current_config)
            del current_config[key]
            
    backtrack(0, {})
    return combinations


# ==============================================================================
# CHỦ ĐỀ 5: KHỬ TRÙNG GIỮ THỨ TỰ & GỘP BẢN GHI (EX5 EXPANDED)
# ==============================================================================

def solution_5_1_ordered_deduplication(
    items: List[Any], 
    key_func: Optional[Callable[[Any], Any]] = None
) -> List[Any]:
    """
    Khử trùng lặp danh sách các phần tử nhưng bảo toàn thứ tự xuất hiện đầu tiên.
    Hỗ trợ hàm key_func (ví dụ: str.lower để khử trùng không phân biệt hoa thường).
    
    Độ phức tạp: O(N) thời gian sử dụng hash set.
    """
    seen = set()
    unhashable_seen = []
    result = []
    
    for item in items:
        k = key_func(item) if key_func is not None else item
        try:
            if k not in seen:
                seen.add(k)
                result.append(item)
        except TypeError:
            if k not in unhashable_seen:
                unhashable_seen.append(k)
                result.append(item)
            
    return result


def solution_5_2_merge_feature_dictionaries(
    dataset_a: List[Dict[str, Any]], 
    dataset_b: List[Dict[str, Any]], 
    id_key: str = "id"
) -> List[Dict[str, Any]]:
    """
    Gộp 2 tập dữ liệu bảng/bản ghi theo khóa chính id_key.
    Nếu thuộc tính là danh sách (ví dụ danh sách nhãn, tags),
    thực hiện gộp và khử trùng lặp giữ nguyên thứ tự.
    """
    lookup: Dict[Any, Dict[str, Any]] = {}
    ordered_ids = []
    
    for row in dataset_a:
        row_id = row.get(id_key)
        if row_id is None:
            continue
        if row_id not in lookup:
            lookup[row_id] = dict(row)
            ordered_ids.append(row_id)
        else:
            merged_row = lookup[row_id]
            for field, val in row.items():
                if field == id_key:
                    continue
                if isinstance(val, list) and isinstance(merged_row.get(field), list):
                    merged_row[field] = solution_5_1_ordered_deduplication(merged_row[field] + val)
                else:
                    merged_row[field] = val
            
    for row in dataset_b:
        row_id = row.get(id_key)
        if row_id is None:
            continue
            
        if row_id not in lookup:
            lookup[row_id] = dict(row)
            ordered_ids.append(row_id)
        else:
            merged_row = lookup[row_id]
            for field, val in row.items():
                if field == id_key:
                    continue
                if isinstance(val, list) and isinstance(merged_row.get(field), list):
                    # Gộp list và khử trùng giữ thứ tự
                    merged_row[field] = solution_5_1_ordered_deduplication(merged_row[field] + val)
                else:
                    merged_row[field] = val
                    
    return [lookup[rid] for rid in ordered_ids]


# ==============================================================================
# CHỦ ĐỀ 6: LỌC CHIA HẾT & PHÂN TÁCH K-FOLD (EX6 EXPANDED)
# ==============================================================================

def solution_6_1_custom_filter_range(
    start: int, 
    end: int, 
    divisors: List[int], 
    exclude_divisors: List[int]
) -> List[int]:
    """
    Tìm các số trong khoảng [start, end] chia hết cho TẤT CẢ các số trong divisors
    và KHÔNG chia hết cho BẤT KỲ số nào trong exclude_divisors.
    """
    if start > end:
        return []
        
    divisors = [d for d in divisors if d != 0]
    exclude_divisors = [ed for ed in exclude_divisors if ed != 0]
        
    result = []
    for x in range(start, end + 1):
        # Kiểm tra chia hết cho tất cả divisors
        div_ok = all(x % d == 0 for d in divisors) if divisors else True
        if not div_ok:
            continue
            
        # Kiểm tra không chia hết cho bất kỳ số nào trong exclude_divisors
        ex_ok = all(x % ed != 0 for ed in exclude_divisors) if exclude_divisors else True
        if ex_ok:
            result.append(x)
            
    return result


def solution_6_2_kfold_split_indices(
    n_samples: int, 
    n_splits: int = 5, 
    shuffle: bool = False, 
    seed: int = 42
) -> List[Tuple[List[int], List[int]]]:
    """
    Tự cài đặt thuật toán chia tập dữ liệu thành K Folds (K-Fold Cross Validation).
    Trả về danh sách gồm n_splits cặp (train_indices, val_indices).
    """
    if n_samples < n_splits or n_splits <= 1:
        raise ValueError("n_samples phải >= n_splits và n_splits > 1")
        
    indices = list(range(n_samples))
    if shuffle:
        rng = random.Random(seed)
        rng.shuffle(indices)
        
    # Tính kích thước từng fold
    fold_sizes = [n_samples // n_splits] * n_splits
    for i in range(n_samples % n_splits):
        fold_sizes[i] += 1
        
    folds = []
    current = 0
    for fold_size in fold_sizes:
        val_idx = indices[current : current + fold_size]
        train_idx = indices[:current] + indices[current + fold_size :]
        folds.append((train_idx, val_idx))
        current += fold_size
        
    return folds


# ==============================================================================
# CHỦ ĐỀ 7: CHỮ SỐ CHẴN & PHÂN LOẠI BIT PARITY (EX7 EXPANDED)
# ==============================================================================

def solution_7_1_all_even_digits(start: int, end: int) -> List[int]:
    """
    Tìm tất cả các số trong khoảng [start, end] mà MỌI chữ số của nó đều chẵn (0, 2, 4, 6, 8).
    Ví dụ: 2000, 2002, 2024 thỏa mãn; 2001 loại vì có chữ số 1.
    """
    if start > end:
        return []
    even_digits = {'0', '2', '4', '6', '8'}
    return [i for i in range(start, end + 1) if all(ch in even_digits for ch in str(abs(i)))]


def solution_7_2_binary_parity_and_hamming(numbers: List[int]) -> Dict[str, Any]:
    """
    Phân loại các số nguyên theo tính Parity của biểu diễn nhị phân:
    - Hamming Weight: số lượng bit 1 trong biểu diễn nhị phân.
    - Even Parity: nếu số lượng bit 1 là số chẵn.
    - Odd Parity: nếu số lượng bit 1 là số lẻ.
    """
    even_parity = []
    odd_parity = []
    hamming_weights = {}
    
    for num in numbers:
        # Đếm số bit 1
        bits_count = bin(num).count('1')
        hamming_weights[num] = bits_count
        if bits_count % 2 == 0:
            even_parity.append(num)
        else:
            odd_parity.append(num)
            
    return {
        "even_parity_numbers": even_parity,
        "odd_parity_numbers": odd_parity,
        "hamming_weights": hamming_weights
    }


# ==============================================================================
# CHỦ ĐỀ 8: WORD LADDER & BI-DIRECTIONAL BFS GRAPH SEARCH (EX8 EXPANDED)
# ==============================================================================

def solution_8_1_word_ladder_one_letter_diff(
    begin_word: str, 
    end_word: str, 
    word_list: List[str]
) -> List[str]:
    """
    Bài toán kinh điển Word Ladder (LeetCode 127):
    Mỗi bước biến đổi đúng 1 chữ cái sang một từ có trong word_list.
    Tìm chuỗi từ ngắn nhất nối begin_word với end_word.
    """
    words = set(w.lower() for w in word_list)
    begin = begin_word.lower()
    end = end_word.lower()
    
    if end not in words:
        return []
    if begin == end:
        return [begin]
        
    # BFS
    queue = deque([[begin]])
    visited = {begin}
    
    while queue:
        path = queue.popleft()
        last_word = path[-1]
        
        if last_word == end:
            return path
            
        # Tìm các từ láng giềng khác 1 ký tự
        for i in range(len(last_word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == last_word[i]:
                    continue
                next_word = last_word[:i] + c + last_word[i+1:]
                if next_word in words and next_word not in visited:
                    visited.add(next_word)
                    queue.append(path + [next_word])
                    
    return []


def solution_8_2_bidirectional_bfs_chain(
    start_word: str, 
    end_word: str, 
    filename: str = "wordsEn.txt"
) -> Union[List[str], str]:
    """
    Tìm chuỗi từ nối theo quy tắc: từ sau có prefix(2) == suffix(2) của từ trước.
    Tối ưu hóa bằng tìm kiếm 2 chiều Bi-directional BFS giúp tăng tốc độ tìm kiếm.
    """
    # Tái sử dụng bộ nạp từ điển từ Ex8
    from Ex8 import load_dictionary
    try:
        valid_words, prefix_map = load_dictionary(filename)
    except Exception as e:
        return f"Lỗi đọc file từ điển: {e}"
        
    start = start_word.strip().lstrip('\ufeff').lstrip('ï»¿').lower()
    end = end_word.strip().lstrip('\ufeff').lstrip('ï»¿').lower()
    
    if start not in valid_words or end not in valid_words:
        return "Từ không hợp lệ hoặc không có trong từ điển."
    if start == end:
        return [start]
        
    # Tạo thêm suffix_map để hỗ trợ đi ngược từ end về start
    # suffix_map[prefix] -> danh sách các từ có suffix bằng prefix này
    suffix_map = defaultdict(list)
    for w in valid_words:
        suffix_map[w[-2:]].append(w)
        
    forward_queue = deque([[start]])
    forward_visited = {start: [start]}
    
    backward_queue = deque([[end]])
    backward_visited = {end: [end]}
    
    while forward_queue and backward_queue:
        # Mở rộng phía trước
        f_path = forward_queue.popleft()
        f_word = f_path[-1]
        f_suffix = f_word[-2:]
        
        for next_word in prefix_map.get(f_suffix, []):
            if next_word in backward_visited:
                # Giao nhau! Nối đường đi phía trước và phía sau
                b_path = backward_visited[next_word]
                # b_path đi từ end về next_word -> đảo ngược lại
                return f_path + b_path[::-1]
            if next_word not in forward_visited:
                new_path = f_path + [next_word]
                forward_visited[next_word] = new_path
                forward_queue.append(new_path)
                
        # Mở rộng phía sau
        b_path = backward_queue.popleft()
        b_word = b_path[-1]
        b_prefix = b_word[:2]
        
        for prev_word in suffix_map.get(b_prefix, []):
            if prev_word in forward_visited:
                # Giao nhau!
                f_path = forward_visited[prev_word]
                return f_path + b_path[::-1]
            if prev_word not in backward_visited:
                new_path = b_path + [prev_word]
                backward_visited[prev_word] = new_path
                backward_queue.append(new_path)
                
    return "Không tìm thấy chuỗi nào kết nối 2 từ"
