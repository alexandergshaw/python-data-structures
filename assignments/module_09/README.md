# Week 9 — Searching and Sorting

Searching and sorting are among the most studied problems in computer science. This week you implement the classic algorithms, understand *why* they have their complexities, and measure how they perform in practice.

---

## Concepts Covered

### 1. Linear Search

Scan every element from left to right until you find the target or exhaust the list.

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i    # Return index of found item
    return -1           # Not found
```

- Works on **unsorted** lists.
- Time complexity: **O(n)** worst case (target at end or absent).
- Best case: **O(1)** (target is first).

---

### 2. Binary Search

Divide the sorted list in half repeatedly until you find the target or the search space is empty.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1    # Target is in the right half
        else:
            high = mid - 1   # Target is in the left half
    return -1
```

- **Requires a sorted list.**
- Time complexity: **O(log n)** — each step eliminates half the remaining elements.

> **Key insight:** With 1,000,000 elements, binary search takes at most 20 comparisons. Linear search could take 1,000,000.

---

### 3. Bubble Sort

Repeatedly compare adjacent elements and swap them if they're in the wrong order. The largest unsorted element "bubbles" to its correct position each pass.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

- Time complexity: **O(n²)** average and worst case.
- Simple to understand, but inefficient for large lists.

---

### 4. Selection Sort

Find the minimum element in the unsorted portion and move it to its correct position.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]   # Swap
    return arr
```

- Time complexity: **O(n²)** — always performs n²/2 comparisons.
- Makes fewer swaps than bubble sort, which can matter when swaps are expensive.

---

### 5. Merge Sort — Divide and Conquer

Split the list in half, sort each half recursively, then merge the two sorted halves.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

- Time complexity: **O(n log n)** — the most efficient you can achieve for comparison-based sorting.
- Space complexity: **O(n)** — requires extra memory for merging.

---

### 6. Quick Sort — Divide and Conquer

Choose a **pivot**, partition elements into "less than pivot" and "greater than pivot," then sort each partition recursively.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

- Average time complexity: **O(n log n)**.
- Worst case: **O(n²)** (rare with good pivot choice).
- Often faster than merge sort in practice due to lower overhead.

---

### 7. Performance Comparison

| Algorithm      | Best      | Average   | Worst     | Space  |
|----------------|-----------|-----------|-----------|--------|
| Linear search  | O(1)      | O(n)      | O(n)      | O(1)   |
| Binary search  | O(1)      | O(log n)  | O(log n)  | O(1)   |
| Bubble sort    | O(n)      | O(n²)     | O(n²)     | O(1)   |
| Selection sort | O(n²)     | O(n²)     | O(n²)     | O(1)   |
| Merge sort     | O(n log n)| O(n log n)| O(n log n)| O(n)   |
| Quick sort     | O(n log n)| O(n log n)| O(n²)     | O(log n)|

---

## Hints for This Week's Assignment

- **Never use binary search on an unsorted list** — the results will be wrong.
- To measure real performance, use Python's `time` module: `import time; start = time.time(); ...; print(time.time() - start)`.
- For merge sort, implement and test `merge()` first by itself before adding the recursive part.
- For quick sort, the simple version (shown above) creates new lists at each step. This is slightly less memory-efficient but much easier to understand — start here.
- When comparing algorithms, test with sorted, reverse-sorted, and random inputs — performance can vary dramatically.
- Python's built-in `sorted()` and `.sort()` use **Timsort**, which is O(n log n) and extremely optimized. In real code, always prefer the built-in — implement sorting algorithms to understand them, not to use them in production.

---

## Assignment Instructions

**File to create:** `module_09/searching_sorting.py`

You will implement two search algorithms and four sort algorithms, then benchmark them against each other. Follow each step in order.

---

### Step 1 — `linear_search(arr, target)`

Return the **index** of `target` in `arr`, or `-1` if not found. Scan from left to right.

```python
print(linear_search([5, 3, 8, 1, 9], 8))   # 2
print(linear_search([5, 3, 8, 1, 9], 7))   # -1
```

---

### Step 2 — `binary_search(arr, target)`

Return the **index** of `target` in the **sorted** list `arr`, or `-1` if not found.

```python
sorted_arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(sorted_arr, 7))    # 3
print(binary_search(sorted_arr, 6))    # -1
print(binary_search(sorted_arr, 1))    # 0
print(binary_search(sorted_arr, 13))   # 6
```

---

### Step 3 — `bubble_sort(arr)`

Return a **sorted copy** of `arr` using bubble sort. Do not modify the original list.

```python
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# [11, 12, 22, 25, 34, 64, 90]
```

---

### Step 4 — `selection_sort(arr)`

Return a **sorted copy** of `arr` using selection sort.

```python
print(selection_sort([29, 10, 14, 37, 13]))
# [10, 13, 14, 29, 37]
```

---

### Step 5 — `merge_sort(arr)`

Return a **sorted copy** of `arr` using merge sort. You need two functions: `merge_sort()` (recursive) and a helper `merge(left, right)`.

```python
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]
```

Test `merge()` separately first:
```python
print(merge([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
```

---

### Step 6 — `quick_sort(arr)`

Return a **sorted copy** of `arr` using quick sort. Use the middle element as the pivot.

```python
print(quick_sort([10, 80, 30, 90, 40, 50, 70]))
# [10, 30, 40, 50, 70, 80, 90]
```

---

### Step 7 — Verify all sorts produce the same result

Add a block at the bottom of your file that verifies all four sort functions produce identical output:

```python
import random
test_list = random.sample(range(1000), 20)   # 20 random numbers

b = bubble_sort(test_list)
s = selection_sort(test_list)
m = merge_sort(test_list)
q = quick_sort(test_list)

assert b == s == m == q == sorted(test_list), "Sorting mismatch!"
print("All four sorts agree:", b)
```

---

### Step 8 — Benchmark bubble sort vs. merge sort

Time both algorithms on a list of 2000 random integers and print the results:

```python
import time, random

big = random.sample(range(100_000), 2000)

start = time.time()
bubble_sort(big)
print(f"Bubble sort:  {time.time() - start:.4f}s")

start = time.time()
merge_sort(big)
print(f"Merge sort:   {time.time() - start:.4f}s")
```

In a comment, write one sentence explaining the speed difference you observe.

---

### Step 9 — Search demo

Using the list `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`:

1. Use `linear_search` to find `23` and `99`. Print the results.
2. Use `binary_search` to find `23` and `99`. Print the results.
3. In a comment, state which search is faster for this list and why.

---

### Checklist Before Submitting

- [ ] `linear_search` returns the correct index or `-1`.
- [ ] `binary_search` returns the correct index or `-1`; works only on sorted input.
- [ ] `bubble_sort`, `selection_sort`, `merge_sort`, `quick_sort` all return sorted copies without modifying the input.
- [ ] The `merge()` helper is implemented and tested separately.
- [ ] The assertion block passes (all four sorts agree with `sorted()`).
- [ ] The benchmark prints times for both bubble sort and merge sort.
- [ ] A comment explains the observed speed difference.
- [ ] The search demo prints results for both algorithms.
