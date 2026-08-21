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
