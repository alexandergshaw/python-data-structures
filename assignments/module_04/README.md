# Week 4 — Complexity Analysis

This week you step back from writing code and start **analyzing** it. How fast does your program run? How much memory does it use? These questions matter enormously when your input grows from 10 items to 10 million. Big O notation gives you a language to answer them precisely.

---

## Concepts Covered

### 1. What Is Big O Notation?

Big O notation describes how an algorithm's **resource usage** (time or memory) grows as the **input size** (`n`) grows. It expresses an upper bound on growth — the worst it can get.

Think of it as answering: *"If I double the input, what happens to the runtime?"*

Big O ignores constants and lower-order terms because they become insignificant for large inputs:
- `3n + 5` → O(n)
- `n² + n + 1` → O(n²)
- `5` → O(1)

---

### 2. Time Complexity vs. Space Complexity

- **Time complexity** — how the number of **operations** scales with input size.
- **Space complexity** — how the amount of **memory** (extra variables, lists, etc.) scales with input size.

Both are expressed in Big O. Unless otherwise noted, "complexity" usually refers to time complexity.

---

### 3. Best, Average, and Worst Cases

An algorithm can behave very differently depending on the input:

| Case    | Meaning                                          | Example (linear search)         |
|---------|--------------------------------------------------|---------------------------------|
| Best    | The luckiest possible input                      | Target is the very first item   |
| Average | A typical, random input                          | Target is somewhere in the middle |
| Worst   | The most difficult input                         | Target is last, or not present  |

Big O almost always describes the **worst case** — this gives you a guarantee: "no matter what, it won't be slower than this."

---

### 4. Common Complexities

#### O(1) — Constant Time

The algorithm always takes the same amount of time, regardless of input size.

```python
def get_first(items):
    return items[0]   # Always exactly one operation
```

Accessing any list index, dictionary lookup, and simple math are all O(1).

---

#### O(log n) — Logarithmic Time

The algorithm cuts the problem in half (or some fraction) each step. Extremely efficient for large inputs.

```python
# Binary search: each iteration halves the search space
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

If `n` = 1,000,000, binary search takes at most ~20 steps (log₂ 1,000,000 ≈ 20).

---

#### O(n) — Linear Time

The algorithm's work grows directly proportional to input size. Double the input → double the work.

```python
def find_max(items):
    max_val = items[0]
    for item in items:    # Visits every item once → n operations
        if item > max_val:
            max_val = item
    return max_val
```

---

#### O(n²) — Quadratic Time

The algorithm has a loop **inside** a loop, both iterating over the input. Usually acceptable for small inputs; slow for large ones.

```python
def has_duplicate(items):
    for i in range(len(items)):
        for j in range(len(items)):    # Nested loop → n * n operations
            if i != j and items[i] == items[j]:
                return True
    return False
```

If `n` = 1,000, this performs up to 1,000,000 operations.

---

### 5. How to Recognize Complexity at a Glance

| Code pattern                           | Typical complexity |
|----------------------------------------|--------------------|
| Single statement / index access        | O(1)               |
| One loop over n items                  | O(n)               |
| Two separate loops over n items        | O(n) — not O(2n)   |
| Loop inside a loop, both over n items  | O(n²)              |
| Halving the input each step            | O(log n)           |
| Sorting (comparison-based)             | O(n log n)         |

---

## Hints for This Week's Assignment

- **Count the loops, not the lines.** A function with 50 lines but only one loop is still O(n).
- When you see a loop inside a loop and both loop over the same input, that's almost always O(n²) — stop and ask yourself: is there a smarter way?
- **Drop constants and lower-order terms.** O(3n + 100) simplifies to O(n). Big O only cares about what dominates as n → ∞.
- Space complexity counts the **extra** memory your function allocates — not the input itself (usually). A function that creates a new list of size n has O(n) space complexity even if it does very little work.
- Practice by estimating the complexity of functions you wrote in previous modules before looking at the answer.

---

## Assignment Instructions

**File to create:** `module_04/complexity.py`

You will implement several functions and then **analyze and document the complexity** of each one. Read every step carefully — the analysis is just as important as the code.

---

### Step 1 — Implement and label `find_first(lst, target)`

Write a function that returns the **index** of the first occurrence of `target` in `lst`, or `-1` if it isn't there.

After writing it, add a comment above the function that states:
- Its **time complexity** (best, average, worst)
- Its **space complexity**
- A one-sentence explanation of why

Example comment format:
```python
# Time: O(1) best, O(n) average/worst — must scan up to n elements
# Space: O(1) — no extra memory proportional to input
def find_first(lst, target):
    ...
```

---

### Step 2 — Implement and label `has_duplicates_slow(lst)`

Write a function that checks whether any value appears more than once in `lst` using **two nested loops** (compare every pair of elements).

Label its complexity. This is the O(n²) approach.

---

### Step 3 — Implement and label `has_duplicates_fast(lst)`

Write a **second version** of duplicate detection using a Python `set`. Add each element to the set; if it's already there, return `True`.

Label its complexity. This is the O(n) approach.

---

### Step 4 — Implement and label `binary_search(sorted_lst, target)`

Write a binary search function (refer to the concept section for the algorithm). Label it with its time and space complexity.

---

### Step 5 — Implement and label `sum_pairs(lst)`

Write a function that returns all pairs `(a, b)` from `lst` where `a + b == 0`. Use nested loops.

```python
sum_pairs([-3, 1, 3, -1, 2])
# → [(-3, 3), (1, -1)]
```

Label its complexity.

---

### Step 6 — Time the two duplicate-detection functions

At the bottom of your file, use Python's `time` module to measure how long `has_duplicates_slow` and `has_duplicates_fast` take on a large list:

```python
import time
import random

big_list = list(range(5000))   # No duplicates — worst case for both

start = time.time()
has_duplicates_slow(big_list)
slow_time = time.time() - start

start = time.time()
has_duplicates_fast(big_list)
fast_time = time.time() - start

print(f"Slow (O(n²)): {slow_time:.4f}s")
print(f"Fast (O(n)):  {fast_time:.4f}s")
```

Run it and observe the difference. You don't need to submit the numbers, but you should see the O(n²) version is dramatically slower.

---

### Step 7 — Written complexity summary

At the **top** of your file (as a multi-line comment or docstring), write a table summarizing the complexity of all five functions:

```python
"""
Function                  | Time (worst) | Space | Notes
--------------------------|--------------|-------|-------------------------------
find_first                | O(n)         | O(1)  | Linear scan
has_duplicates_slow       | O(n²)        | O(1)  | Nested loops
has_duplicates_fast       | O(n)         | O(n)  | Set stores up to n elements
binary_search             | O(log n)     | O(1)  | Halves search space each step
sum_pairs                 | O(n²)        | O(n)  | Nested loops, result list
"""
```

---

### Checklist Before Submitting

- [ ] All five functions are implemented and return correct results.
- [ ] Every function has a comment stating its time complexity (best/average/worst) and space complexity.
- [ ] `has_duplicates_fast` uses a `set`, not nested loops.
- [ ] `binary_search` requires a sorted list and correctly returns `-1` when not found.
- [ ] The timing comparison at the bottom is present and runs without errors.
- [ ] The written summary table at the top is filled in for all five functions.
