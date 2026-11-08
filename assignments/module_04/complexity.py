"""
Function               | Time Complexity (worst) | Space  | Why?
-----------------------|-------------------------|--------|---------------------------
find_first             | O(n)                    | O(1)   | scans once
has_duplicates_slow    | O(n^2)                  | O(1)   | compares all pairs
has_duplicates_fast    | O(n)                    | O(n)   | stores seen values
binary_search          | O(log n)                | O(1)   | halves the search range
sum_pairs              | O(n^2)                  | O(n^2) | stores matching pairs
"""

import time


# Time: O(1) best, O(n) average/worst; Space: O(1)
def find_first(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


# Time: O(n^2); Space: O(1)
def has_duplicates_slow(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False


# Time: O(n) average; Space: O(n)
def has_duplicates_fast(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False


# Time: O(log n); Space: O(1). Requires a sorted list.
def binary_search(sorted_lst, target):
    low, high = 0, len(sorted_lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return mid
        if sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Time: O(n^2); Space: O(n^2) for the returned pairs
def sum_pairs(lst):
    return [(lst[i], lst[j]) for i in range(len(lst))
            for j in range(i + 1, len(lst)) if lst[i] + lst[j] == 0]


def benchmark():
    test = [3, 1, 4, 1, 5, 9]
    assert has_duplicates_slow(test) == has_duplicates_fast(test)
    print("Both agree!")
    big_list = list(range(5000))
    start = time.time()
    has_duplicates_slow(big_list)
    slow = time.time() - start
    start = time.time()
    has_duplicates_fast(big_list)
    fast = time.time() - start
    print(f"Slow (O(n²)): {slow:.4f} seconds")
    print(f"Fast (O(n)):  {fast:.4f} seconds")
    print(f"Fast version was about {slow / fast:.0f}x faster.")
    # The set-based version is faster, by approximately the measured factor above.


if __name__ == "__main__":
    benchmark()
