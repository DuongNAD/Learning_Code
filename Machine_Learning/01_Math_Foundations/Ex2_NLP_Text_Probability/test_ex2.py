"""
Unit tests for Ex2 NumPy manipulations and NLP frequency analysis.
"""

import os
import tempfile
import numpy as np
import pytest
from ex2 import reverse_array, elements_in_second, find_min_max_indices, top_frequent_words


class TestEx2NumPyAndNLP:
    def test_reverse_array_basic(self):
        arr = np.array([1, 2, 3, 4, 5])
        rev = reverse_array(arr)
        np.testing.assert_array_equal(rev, np.array([5, 4, 3, 2, 1]))

    def test_reverse_array_empty(self):
        arr = np.array([])
        rev = reverse_array(arr)
        np.testing.assert_array_equal(rev, np.array([]))

    def test_reverse_array_single(self):
        arr = np.array([42])
        rev = reverse_array(arr)
        np.testing.assert_array_equal(rev, np.array([42]))

    def test_elements_in_second(self):
        arr1 = np.array([0, 10, 20, 40, 60])
        arr2 = np.array([10, 30, 40])
        res = elements_in_second(arr1, arr2)
        np.testing.assert_array_equal(res, np.array([False, True, False, True, False]))

    def test_elements_in_second_none_present(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        res = elements_in_second(arr1, arr2)
        assert not np.any(res)

    def test_find_min_max_indices_1d(self):
        arr = np.array([1, 6, 4, 8, 9, -4, -2, 11])
        min_i, max_i = find_min_max_indices(arr)
        assert min_i == 5
        assert max_i == 7
        assert arr[min_i] == -4
        assert arr[max_i] == 11

    def test_find_min_max_indices_2d(self):
        arr = np.array([[10, 20, 5], [30, 2, 15]])
        min_col, max_col = find_min_max_indices(arr, axis=0)
        np.testing.assert_array_equal(min_col, np.array([0, 1, 0]))
        np.testing.assert_array_equal(max_col, np.array([1, 0, 1]))

    def test_top_frequent_words_story(self):
        story_path = os.path.join(os.path.dirname(__file__), "story.txt")
        top10 = top_frequent_words(story_path, top_k=10)
        assert len(top10) == 10
        # Check that 'the' and 'alice' are in the top words
        words = [w for w, _ in top10]
        assert "the" in words
        assert "alice" in words
        # Counts should be in descending order
        counts = [c for _, c in top10]
        assert counts == sorted(counts, reverse=True)

    def test_top_frequent_words_synthetic(self):
        with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
            tmp.write("Data science, machine learning! Deep learning is science and data.")
            tmp.flush()
            top = top_frequent_words(tmp.name, top_k=3)
            counts_dict = dict(top)
            assert counts_dict["data"] == 2
            assert counts_dict["learning"] == 2
            assert counts_dict["science"] == 2
        os.remove(tmp.name)

    def test_top_frequent_words_missing_file(self):
        with pytest.raises(FileNotFoundError):
            top_frequent_words("non_existent_file_path_xyz.txt")
