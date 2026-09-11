"""
Bộ kiểm thử tự động toàn diện (Comprehensive Test Suite) cho:
- Bài tập gốc Ex1.py đến Ex8.py
- Bộ lời giải thực hành nâng cao solutions_practice.py
Kiểm thử bao phủ cả Happy Paths và Edge Cases (biên, rỗng, ngoại lệ).

Chạy bằng một trong các lệnh sau:
    py test_all.py
    py -m pytest test_all.py -v
"""

import sys
import os
import pytest

# Đảm bảo in tiếng Việt chuẩn trên Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Import các hàm từ bài tập gốc
from Ex1 import separate_positive_negative
from Ex2 import find_elements_greater_than_k
from Ex3 import pairwise_max
from Ex4 import generate_permutations_3
from Ex5 import merge_sublists_unique
from Ex6 import find_numbers_div7_not5
from Ex7 import find_even_numbers, find_numbers_all_even_digits
from Ex8 import find_shortest_word_chain, load_dictionary

# Import bộ lời giải thực hành
import solutions_practice as sol


# ==============================================================================
# 1. KIỂM THỬ EX1: PHÂN LOẠI SỐ ÂM/DƯƠNG
# ==============================================================================

class TestEx1:
    def test_original_data(self):
        data = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
        res = separate_positive_negative(data)
        assert res["pos_num"] == [93, 11, 12, 11, 4]
        assert res["pos_count"] == 5
        assert res["neg_num"] == [-10, -21, -4, -45, -66, -4, -6]
        assert res["neg_count"] == 7

    def test_empty_list(self):
        res = separate_positive_negative([])
        assert res["pos_num"] == []
        assert res["pos_count"] == 0
        assert res["neg_num"] == []
        assert res["neg_count"] == 0

    def test_all_positive(self):
        res = separate_positive_negative([1, 2, 3, 100])
        assert res["pos_count"] == 4
        assert res["neg_count"] == 0

    def test_all_negative(self):
        res = separate_positive_negative([-1, -5, -99])
        assert res["pos_count"] == 0
        assert res["neg_count"] == 3


# ==============================================================================
# 2. KIỂM THỬ EX2: TẦN SUẤT > K
# ==============================================================================

class TestEx2:
    def test_original_data(self):
        data = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
        res = find_elements_greater_than_k(data, 3)
        assert res == [4, 3]

    def test_empty_list(self):
        assert find_elements_greater_than_k([], 2) == []

    def test_k_larger_than_max_frequency(self):
        data = [1, 2, 3, 1, 2]
        assert find_elements_greater_than_k(data, 10) == []

    def test_negative_k(self):
        data = [1, 2, 3]
        # Mọi phần tử đều xuất hiện 1 lần > -1
        assert find_elements_greater_than_k(data, -1) == [1, 2, 3]

    def test_strings(self):
        data = ["apple", "banana", "apple", "cherry", "apple"]
        assert find_elements_greater_than_k(data, 2) == ["apple"]


# ==============================================================================
# 3. KIỂM THỬ EX3: CẶP SỐ LIỀN KỀ (PAIRWISE MAX)
# ==============================================================================

class TestEx3:
    def test_original_data(self):
        data = [4, 5, 6, 7, 3, 9, 11, 2, 10]
        assert pairwise_max(data) == [5, 6, 7, 7, 9, 11, 11, 10]

    def test_single_element(self):
        assert pairwise_max([5]) == []

    def test_empty_list(self):
        assert pairwise_max([]) == []

    def test_two_elements(self):
        assert pairwise_max([10, -5]) == [10]

    def test_all_equal(self):
        assert pairwise_max([7, 7, 7]) == [7, 7]


# ==============================================================================
# 4. KIỂM THỬ EX4: HOÁN VỊ 3 PHẦN TỬ
# ==============================================================================

class TestEx4:
    def test_original_data(self):
        res = generate_permutations_3([1, 2, 3])
        assert len(res) == 6
        expected = [
            [1, 2, 3], [1, 3, 2],
            [2, 1, 3], [2, 3, 1],
            [3, 1, 2], [3, 2, 1]
        ]
        assert res == expected

    def test_less_than_3_elements(self):
        assert generate_permutations_3([1, 2]) == []
        assert generate_permutations_3([]) == []


# ==============================================================================
# 5. KIỂM THỬ EX5: GỘP DANH SÁCH CON KHỬ TRÙNG
# ==============================================================================

class TestEx5:
    def test_original_data(self):
        l1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
        l2 = [[1, 3], [9, 3, 5, 7], [8]]
        res = merge_sublists_unique(l1, l2)
        assert res == [[4, 3, 5, 1], [1, 2, 3, 9, 5, 7], [3, 7, 4, 8]]

    def test_empty_lists(self):
        assert merge_sublists_unique([], []) == []

    def test_different_lengths(self):
        l1 = [[1, 2], [3]]
        l2 = [[4]]
        assert merge_sublists_unique(l1, l2) == [[1, 2, 4]]


# ==============================================================================
# 6. KIỂM THỬ EX6: CHIA HẾT CHO 7 NHƯNG KHÔNG CHIA HẾT CHO 5
# ==============================================================================

class TestEx6:
    def test_original_range(self):
        res = find_numbers_div7_not5(2000, 3200)
        assert len(res) == 138
        assert 2002 in res
        assert 2009 in res
        # Bội số của 35 (chia hết cho cả 7 và 5) phải bị loại
        assert 2030 not in res
        assert 2100 not in res
        for num in res:
            assert num % 7 == 0
            assert num % 5 != 0

    def test_invalid_range(self):
        assert find_numbers_div7_not5(100, 50) == []


# ==============================================================================
# 7. KIỂM THỬ EX7: SỐ CHẴN & CHỮ SỐ TOÀN CHẴN
# ==============================================================================

class TestEx7:
    def test_even_numbers(self):
        res = find_even_numbers(2000, 3000)
        assert len(res) == 501
        assert res[0] == 2000
        assert res[-1] == 3000
        for x in res:
            assert x % 2 == 0

    def test_all_even_digits(self):
        res = find_numbers_all_even_digits(2000, 2025)
        # Các số thỏa: 2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024
        assert 2000 in res
        assert 2002 in res
        assert 2024 in res
        assert 2001 not in res
        assert 2010 not in res  # Chứa số 1 là lẻ


# ==============================================================================
# 8. KIỂM THỬ EX8: WORD CHAIN BFS
# ==============================================================================

class TestEx8:
    def test_head_to_tail(self):
        chain = find_shortest_word_chain("head", "tail")
        assert isinstance(chain, list)
        assert chain[0] == "head"
        assert chain[-1] == "tail"
        # Kiểm tra tính hợp lệ của từng bước nối
        for i in range(len(chain) - 1):
            assert chain[i][-2:] == chain[i + 1][:2]

    def test_cat_to_dog(self):
        chain = find_shortest_word_chain("cat", "dog")
        assert isinstance(chain, list)
        assert chain[0] == "cat"
        assert chain[-1] == "dog"

    def test_same_word(self):
        assert find_shortest_word_chain("head", "head") == ["head"]

    def test_invalid_word(self):
        res = find_shortest_word_chain("zzzzzxyz", "head")
        assert "phải có ít nhất 3 chữ cái" in res or "Lỗi" in res


# ==============================================================================
# 9. KIỂM THỬ 16 BÀI THỰC HÀNH (SOLUTIONS PRACTICE)
# ==============================================================================

class TestPracticeSolutions:
    def test_prob_1_1_empty(self):
        res = sol.solution_1_1_sign_and_zero_classifier([])
        assert res["positive"]["count"] == 0
        assert res["zero"]["count"] == 0
        assert res["negative"]["count"] == 0

    def test_prob_1_2_all_negative(self):
        res = sol.solution_1_2_relu_and_leaky_relu([-5, -10], alpha=0.1)
        assert res["relu_output"] == [0.0, 0.0]
        assert res["leaky_relu_output"] == [-0.5, -1.0]
        assert res["dead_neuron_rate"] == 100.0

    def test_prob_2_1_top_k(self):
        res = sol.solution_2_1_top_k_frequent_words("one two two three three three", k=2, min_len=3)
        assert res[0] == ("three", 3)
        assert res[1] == ("two", 2)

    def test_prob_2_2_pruner(self):
        docs = [["python", "code"], ["python", "learning"], ["code"], ["   "]]
        vocab = sol.solution_2_2_nlp_vocabulary_pruner(docs, min_freq=2, max_freq=2)
        assert vocab == ["code", "python"]
        assert "" not in vocab

    def test_prob_3_1_moving_average(self):
        assert sol.solution_3_1_moving_average_1d([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
        assert sol.solution_3_1_moving_average_1d([1, 2], 5) == []

    def test_prob_3_2_max_pooling_1d(self):
        res = sol.solution_3_2_max_pooling_1d([2, 8, 4, 1], pool_size=2, stride=2)
        assert res == [8, 4]

    def test_prob_4_1_permutations(self):
        res = sol.solution_4_1_recursive_permutations(["A", "B"])
        assert set(res) == {("A", "B"), ("B", "A")}

    def test_prob_4_2_grid_search(self):
        grid = {"a": [1, 2], "b": ["x"]}
        configs = sol.solution_4_2_grid_search_combinations(grid)
        assert len(configs) == 2
        assert {"a": 1, "b": "x"} in configs
        assert {"a": 2, "b": "x"} in configs

    def test_prob_5_1_dedup(self):
        res = sol.solution_5_1_ordered_deduplication(["A", "b", "a"], key_func=str.lower)
        assert res == ["A", "b"]
        # Kiểm tra tính an toàn với unhashable types (list)
        res_lists = sol.solution_5_1_ordered_deduplication([[1, 2], [3], [1, 2]])
        assert res_lists == [[1, 2], [3]]

    def test_prob_5_2_merge_records(self):
        da = [{"id": 10, "tags": ["ml"]}]
        db = [{"id": 10, "tags": ["ml", "ai"]}]
        res = sol.solution_5_2_merge_feature_dictionaries(da, db)
        assert res[0]["tags"] == ["ml", "ai"]

        # Kiểm tra trùng id ngay trong dataset_a
        da_dup = [{"id": 1, "v": "a"}, {"id": 1, "v": "b"}]
        res_dup = sol.solution_5_2_merge_feature_dictionaries(da_dup, [])
        assert len(res_dup) == 1
        assert res_dup[0]["id"] == 1

    def test_prob_6_1_custom_filter(self):
        res = sol.solution_6_1_custom_filter_range(1, 20, divisors=[2, 3], exclude_divisors=[4])
        # Bội của 6 (2*3): 6, 12, 18. Trong đó 12 chia hết cho 4 nên bị loại -> còn [6, 18]
        assert res == [6, 18]
        # Kiểm tra an toàn khi divisors chứa 0
        assert sol.solution_6_1_custom_filter_range(1, 10, divisors=[2, 0], exclude_divisors=[0]) == [2, 4, 6, 8, 10]

    def test_prob_6_2_kfold(self):
        folds = sol.solution_6_2_kfold_split_indices(10, n_splits=5)
        assert len(folds) == 5
        # Kiểm tra không bị trùng val_indices giữa các fold
        all_val = []
        for train, val in folds:
            assert len(train) == 8
            assert len(val) == 2
            all_val.extend(val)
        assert sorted(all_val) == list(range(10))

    def test_prob_7_1_all_even_digits(self):
        res = sol.solution_7_1_all_even_digits(19, 31)
        # Các số từ 19..31 có mọi chữ số chẵn: 20, 22, 24, 26, 28
        assert res == [20, 22, 24, 26, 28]
        # Kiểm tra số âm
        neg_res = sol.solution_7_1_all_even_digits(-24, -20)
        assert neg_res == [-24, -22, -20]

    def test_prob_7_2_parity(self):
        res = sol.solution_7_2_binary_parity_and_hamming([0, 1, 2, 3])
        # 0: 0 bit (chẵn), 1: 1 bit (lẻ), 2: 1 bit (lẻ), 3: 2 bit (chẵn)
        assert 0 in res["even_parity_numbers"]
        assert 3 in res["even_parity_numbers"]
        assert 1 in res["odd_parity_numbers"]
        assert 2 in res["odd_parity_numbers"]

    def test_prob_8_1_word_ladder(self):
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        res = sol.solution_8_1_word_ladder_one_letter_diff("hit", "cog", words)
        assert res == ["hit", "hot", "dot", "dog", "cog"] or res == ["hit", "hot", "lot", "log", "cog"]

    def test_prob_8_2_bidirectional_bfs(self):
        res = sol.solution_8_2_bidirectional_bfs_chain("head", "tail")
        assert isinstance(res, list)
        assert res[0] == "head"
        assert res[-1] == "tail"
        for i in range(len(res) - 1):
            assert res[i][-2:] == res[i + 1][:2], f"Bước không khớp tại {i}: {res[i]} -> {res[i+1]}"

        # Test trực tiếp liên kết 1 bước (trước đây bị bug trả về ['apple'])
        direct_res = sol.solution_8_2_bidirectional_bfs_chain("apple", "lemon")
        assert direct_res == ["apple", "lemon"]

        # Test chuỗi cat -> dog
        cat_dog = sol.solution_8_2_bidirectional_bfs_chain("cat", "dog")
        assert isinstance(cat_dog, list)
        assert cat_dog[0] == "cat" and cat_dog[-1] == "dog"
        for i in range(len(cat_dog) - 1):
            assert cat_dog[i][-2:] == cat_dog[i + 1][:2]


if __name__ == "__main__":
    # Tự động chạy pytest khi execute trực tiếp
    import pytest
    sys.exit(pytest.main(["-v", __file__]))
