# Week 9 — Searching and Sorting
### Linear Search, Binary Search, Bubble/Selection/Merge/Quick Sort

---

## Welcome!

Searching and sorting are things computers do billions of times a day. Every time you search for something on Google or scroll through a sorted playlist, an algorithm like the ones in this module is running. This week you build them yourself so you understand why some approaches are fast and others crawl.

---

## Concept 1: Linear Search — The Obvious Way

Walk through the list from the beginning and check each item until you find what you're looking for — or reach the end.

**Analogy:** You lost your keys. You check the kitchen counter, then the coffee table, then your coat pocket, one spot at a time, until you find them or give up. That's linear search.

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i      # Found it — return the index
    return -1             # Not found
```

- Works on **any** list — sorted or not
- Time: O(n) worst case (check every item)
- Best case: O(1) (it's the first item)

---

## Concept 2: Binary Search — The Smart Way (for Sorted Lists Only!)

Binary search uses the fact that the list is **sorted** to eliminate half the remaining items with every single check.

**Analogy:** Guessing a number between 1 and 100. Someone tells you "higher" or "lower" after each guess. A smart player always guesses the middle (50 first, then 25 or 75, etc.). With this strategy you can find any number in at most 7 guesses. That's binary search.

```
List: [1, 3, 5, 7, 9, 11, 13]
Find: 7

Step 1: Middle is 7 (index 3). Found it!

Find: 11
Step 1: Middle is 7 (index 3). 11 > 7, so search right half [9, 11, 13]
Step 2: Middle is 11 (index 5). Found it!

Find: 4
Step 1: Middle is 7. 4 < 7, search left half [1, 3, 5]
Step 2: Middle is 3. 4 > 3, search right half [5]
Step 3: Only one item: 5 ≠ 4. Not found. Return -1.
```

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1      # Target is in the right half
        else:
            high = mid - 1     # Target is in the left half
    return -1
```

- **Requires a sorted list — wrong results on unsorted data!**
- Time: O(log n) — 1 million items → at most 20 checks

---

## Concept 3: Bubble Sort — The Simple (Slow) One

Go through the list over and over, comparing neighboring pairs. Swap them if they're in the wrong order. The biggest item "bubbles" to the end each pass.

**Analogy:** Imagine you're sorting a line of people by height, but you can only see two neighbors at a time. You walk the line comparing pairs. The tallest person slowly moves to the end through a series of swaps. Then you go again, and the second tallest reaches its spot. You repeat until no more swaps happen.

```python
def bubble_sort(arr):
    arr = arr[:]          # Make a copy so we don't modify the original
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # Swap
    return arr
```

- Time: O(n²) — very slow on large lists
- Simple to understand — good for learning, not for real use

---

## Concept 4: Selection Sort — Pick the Smallest Each Time

Find the smallest item in the unsorted portion, and move it to the front. Repeat.

**Analogy:** Sorting a hand of playing cards. You look at all your cards, pick out the lowest, put it first. Then look at the rest, pick the lowest of those, put it second. Repeat until done.

```python
def selection_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]   # Swap smallest to front
    return arr
```

- Time: O(n²) — also slow, but makes fewer swaps than bubble sort

---

## Concept 5: Merge Sort — Divide and Conquer

Split the list in half. Sort each half. Merge the two sorted halves back together.

**Analogy:** You and a friend each get half a shuffled deck of cards. You each sort your half (by using this same trick recursively). Then you merge your two sorted piles into one: look at the top card of each pile, take the smaller one, repeat until done.

```python
def merge_sort(arr):
    if len(arr) <= 1:              # BASE CASE — a list of 0 or 1 items is already sorted
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half
    return merge(left, right)      # Merge sorted halves

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
    result.extend(left[i:])     # Add any remaining items
    result.extend(right[j:])
    return result
```

- Time: O(n log n) — much faster than O(n²) on large inputs
- Space: O(n) — needs extra memory for merging

---

## Concept 6: Quick Sort — Another Divide and Conquer

Choose a **pivot** value. Put everything smaller than the pivot on the left. Put everything larger on the right. Sort the left and right sides recursively.

**Analogy:** You're sorting a pile of mail. You pick one letter (the pivot). Anything that comes before it alphabetically goes in a left pile. Anything that comes after goes in a right pile. Now sort each pile the same way.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]            # Pick the middle element as pivot
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

- Average time: O(n log n)
- Worst case: O(n²) — rare in practice with good pivot selection

---

## Comparison Table

| Algorithm | Speed (worst case) | Speed (best case) | Works on unsorted? |
|-----------|--------------------|--------------------|----------------------|
| Linear search | O(n) | O(1) | ✅ Yes |
| Binary search | O(log n) | O(1) | ❌ Sorted only |
| Bubble sort | O(n²) | O(n) | ✅ |
| Selection sort | O(n²) | O(n²) | ✅ |
| Merge sort | O(n log n) | O(n log n) | ✅ |
| Quick sort | O(n²) | O(n log n) | ✅ |

---

## Assignment Instructions

**File to create:** `module_09/searching_sorting.py`

You'll implement both search algorithms and all four sort algorithms, verify they agree, and benchmark them.

---

### Step 1 — `linear_search(arr, target)`

Return the index of the first occurrence of `target`, or `-1` if not found.

```python
print(linear_search([5, 3, 8, 1, 9], 8))   # 2
print(linear_search([5, 3, 8, 1, 9], 7))   # -1
```

---

### Step 2 — `binary_search(arr, target)`

Return the index of `target` in the **sorted** list, or `-1`.

```python
sorted_nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(sorted_nums, 7))    # 3
print(binary_search(sorted_nums, 6))    # -1
print(binary_search(sorted_nums, 1))    # 0
```

---

### Step 3 — `bubble_sort(arr)`

Return a sorted copy. Don't modify the original list.

```python
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# [11, 12, 22, 25, 34, 64, 90]
```

---

### Step 4 — `selection_sort(arr)`

Return a sorted copy. Don't modify the original list.

```python
print(selection_sort([29, 10, 14, 37, 13]))
# [10, 13, 14, 29, 37]
```

---

### Step 5 — `merge(left, right)` then `merge_sort(arr)`

Implement `merge()` first and test it:
```python
print(merge([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
```

Then implement `merge_sort()`:
```python
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]
```

---

### Step 6 — `quick_sort(arr)`

```python
print(quick_sort([10, 80, 30, 90, 40, 50, 70]))
# [10, 30, 40, 50, 70, 80, 90]
```

---

### Step 7 — Verify all four sorts agree

```python
import random
test_list = random.sample(range(1000), 20)

b = bubble_sort(test_list)
s = selection_sort(test_list)
m = merge_sort(test_list)
q = quick_sort(test_list)

assert b == s == m == q == sorted(test_list), "Mismatch detected!"
print("All four sorts agree:", b)
```

---

### Step 8 — Benchmark bubble sort vs. merge sort

```python
import time, random
big = random.sample(range(100_000), 2000)

start = time.time()
bubble_sort(big)
print(f"Bubble sort: {time.time() - start:.4f}s")

start = time.time()
merge_sort(big)
print(f"Merge sort:  {time.time() - start:.4f}s")

# Add a comment: which was faster, and roughly by how many times?
```

---

### Step 9 — Search demo

Using the list `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`:
- Use `linear_search` to find `23` and `99`. Print the results.
- Use `binary_search` to find `23` and `99`. Print the results.
- In a comment, state which is faster and why.

---

### Checklist Before Submitting

- [ ] `linear_search` returns correct index or `-1`
- [ ] `binary_search` returns correct index or `-1`; only use it on sorted lists
- [ ] All four sort functions return sorted copies and leave the original unchanged
- [ ] `merge()` helper works correctly on its own
- [ ] The assertion block passes (all four sorts agree with `sorted()`)
- [ ] Benchmark prints times for both algorithms with a comment on the difference
- [ ] Search demo is present and prints results for both algorithms
