"""
Ex2: NumPy Arrays Manipulation & NLP Text Corpus Frequency Analysis
===================================================================
Module provides clean, vectorized implementations for NumPy array manipulations
and statistical text token frequency counting on raw corpora.
"""

import os
import re
from collections import Counter
import numpy as np


def reverse_array(arr: np.ndarray) -> np.ndarray:
    """
    Ex1: Reverses a 1D NumPy array so that the first element becomes last.

    Args:
        arr: 1D NumPy array or array-like.

    Returns:
        Reversed NumPy array.
    """
    arr_np = np.asarray(arr)
    return arr_np[::-1]


def elements_in_second(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    """
    Ex2: Tests whether each element of a 1-D array is also present in a second array.

    Args:
        arr1: First 1D array.
        arr2: Second 1D array to test presence against.

    Returns:
        Boolean NumPy array of the same shape as arr1.
    """
    return np.isin(arr1, arr2)


def find_min_max_indices(arr: np.ndarray, axis: int | None = None) -> tuple[int | np.ndarray, int | np.ndarray]:
    """
    Ex3: Finds the indices of the minimum and maximum values along a given axis.

    Args:
        arr: NumPy array of any dimension.
        axis: Axis along which to find min/max (None for flattened index).

    Returns:
        Tuple of (min_index, max_index).
    """
    arr_np = np.asarray(arr)
    min_idx = np.argmin(arr_np, axis=axis)
    max_idx = np.argmax(arr_np, axis=axis)
    return min_idx, max_idx


def top_frequent_words(file_path: str, top_k: int = 100) -> list[tuple[str, int]]:
    """
    Ex4: Reads a text file, strips punctuation, normalizes case,
    and returns the top-K most frequently occurring words with their counts.

    Args:
        file_path: Relative or absolute path to the text file.
        top_k: Number of most frequent words to retrieve.

    Returns:
        List of (word, count) tuples sorted in descending order.
    """
    if not os.path.isabs(file_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        candidate = os.path.join(current_dir, file_path)
        if os.path.exists(candidate):
            file_path = candidate

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Corpus file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read().lower()

    # Match alphanumeric words, ignoring punctuation
    words = re.findall(r"\b[a-z0-9_']+\b", text)
    # Strip any leading/trailing single quotes from contractions
    words = [w.strip("'") for w in words if w.strip("'")]

    counter = Counter(words)
    return counter.most_common(top_k)


def main():
    print("=" * 60)
    print("Ex2: NumPy Arrays Manipulation & NLP Text Analysis")
    print("=" * 60)

    # Ex1 Demo
    input_ex1 = np.arange(12, 38)
    print(f"\n[Ex1] Đảo ngược mảng 1D:")
    print(f"Input:    {input_ex1}")
    print(f"Reversed: {reverse_array(input_ex1)}")

    # Ex2 Demo
    arr1 = np.array([0, 10, 20, 40, 60])
    arr2 = np.array([10, 30, 40])
    present = elements_in_second(arr1, arr2)
    print(f"\n[Ex2] Kiểm tra phần tử mảng 1 có thuộc mảng 2 không:")
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Kết quả (isin): {present}")

    # Ex3 Demo
    arr3 = np.array([1, 6, 4, 8, 9, -4, -2, 11])
    min_i, max_i = find_min_max_indices(arr3)
    print(f"\n[Ex3] Chỉ số Min & Max:")
    print(f"Array: {arr3}")
    print(f"Min index: {min_i} (Giá trị = {arr3[min_i]})")
    print(f"Max index: {max_i} (Giá trị = {arr3[max_i]})")

    # Ex4 Demo
    story_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "story.txt")
    print(f"\n[Ex4] Top 20 từ xuất hiện nhiều nhất trong 'story.txt':")
    top20 = top_frequent_words(story_path, top_k=20)
    for rank, (w, count) in enumerate(top20, start=1):
        print(f"  {rank:2d}. {w:<12} : {count} lần")


if __name__ == "__main__":
    main()