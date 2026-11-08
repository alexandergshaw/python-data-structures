import random
import time


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def bubble_sort(arr):
    result = arr[:]
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(arr):
    result = arr[:]
    for i in range(len(result)):
        smallest = min(range(i, len(result)), key=result.__getitem__, default=i)
        result[i], result[smallest] = result[smallest], result[i]
    return result


def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    return (quick_sort([x for x in arr if x < pivot])
            + [x for x in arr if x == pivot]
            + quick_sort([x for x in arr if x > pivot]))


def main():
    test_list = random.sample(range(1000), 20)
    b, s, m, q = (sort(test_list) for sort in
                  (bubble_sort, selection_sort, merge_sort, quick_sort))
    assert b == s == m == q == sorted(test_list)
    print("All four sorts agree:", b)
    big = random.sample(range(100_000), 2000)
    start = time.time()
    bubble_sort(big)
    bubble = time.time() - start
    start = time.time()
    merge_sort(big)
    merged = time.time() - start
    print(f"Bubble sort: {bubble:.4f}s")
    print(f"Merge sort:  {merged:.4f}s")
    print(f"Merge sort was about {bubble / merged:.0f}x faster.")
    # Merge sort is faster by roughly the measured factor because O(n log n) beats O(n²).
    nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(linear_search(nums, 23), linear_search(nums, 99))
    print(binary_search(nums, 23), binary_search(nums, 99))
    # Binary search is faster on sorted data because it halves the range each step.


if __name__ == "__main__":
    main()
