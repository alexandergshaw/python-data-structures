# Week 4 — Complexity Analysis
### Big O Notation, Time, Space, and Recognizing Common Patterns

---

## Welcome!

This week you're not writing new types of programs — you're learning to **think about** the programs you already write. Specifically: how fast are they? How do they hold up when the data gets huge? This is one of the most important skills a software developer has, and it's simpler than it sounds.

---

## Why Does This Matter?

Imagine you wrote a program to find a name in a list of 10 people. It works fine! Then your company grows and the list has 10 million people. Does your program still work? Is it fast enough?

The answer depends on *how* your program searches. Some approaches that work fine on small data become impossibly slow on big data. Big O notation gives you a way to predict this *before* you run the code.

---

## Concept 1: What is Big O?

**Big O notation** describes how the amount of work your program does **grows** as the input gets bigger.

We call the input size **n**. So when we say "O(n)," we're saying: "as n grows, the work grows at roughly the same rate."

**Analogy:** Imagine reading names from a list:
- Reading 1 name takes 1 second
- Reading 100 names takes 100 seconds
- Reading 1,000 names takes 1,000 seconds

That's O(n) — the time grows *linearly* with the input.

**Important:** Big O ignores small details. We don't care if it takes 2 seconds per name vs. 3 seconds — we care about the *shape* of the growth. O(3n) simplifies to O(n) because the "3" stops mattering once n is huge.

---

## Concept 2: Time vs. Space Complexity

- **Time complexity** — how many *operations* your code does as input grows
- **Space complexity** — how much extra *memory* your code uses as input grows

Both are described with Big O. "Complexity" by itself usually means time complexity.

---

## Concept 3: Best, Average, and Worst Cases

The same algorithm can behave very differently depending on the input:

**Example:** Searching for a name in a list by scanning from left to right.
- **Best case:** The name is the very first item. Done in 1 step. → O(1)
- **Average case:** The name is somewhere in the middle. → O(n/2), which simplifies to O(n)
- **Worst case:** The name is last, or isn't there at all. → O(n)

When people say an algorithm is "O(n)," they almost always mean the **worst case**. It's a guarantee: "it can't get worse than this."

---

## Concept 4: The Four You Need to Know

### O(1) — Constant Time

The same amount of work, no matter how big the input is.

**Analogy:** Looking up someone's name by their employee ID number in a company database. Whether there are 10 employees or 10 million, you go straight to ID #4872 and get their name. Instant.

```python
def get_first(items):
    return items[0]   # Always exactly one operation, regardless of list size
```

Examples: accessing a list by index (`items[5]`), looking up a key in a dictionary (`data["name"]`), doing math (`x + y`).

---

### O(log n) — Logarithmic Time

The work grows very slowly — much slower than the input. Each step cuts the problem roughly in half.

**Analogy:** Finding a word in a physical dictionary. You open to the middle. If the word comes before that page, you flip to the middle of the first half. You keep halving until you find it. Even in a dictionary with 100,000 words, you find any word in about 17 steps (because 2^17 ≈ 131,000).

```python
# Binary search — cuts the list in half each step
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

1,000,000 items → at most 20 steps.

---

### O(n) — Linear Time

Work grows directly with input size. Double the input → double the work.

**Analogy:** Reading every page in a book to find a specific sentence. More pages = more reading, at the same rate.

```python
def find_max(items):
    max_val = items[0]
    for item in items:     # Visit every item once
        if item > max_val:
            max_val = item
    return max_val
```

---

### O(n²) — Quadratic Time

Work grows with the *square* of the input size. A loop inside a loop, both running over the input.

**Analogy:** You're at a party and want to introduce every person to every other person. If there are 5 people, that's 5×5 = 25 introductions. If there are 100 people, that's 10,000 introductions. It explodes fast.

```python
def has_duplicate(items):
    for i in range(len(items)):
        for j in range(len(items)):       # Loop inside a loop = O(n²)
            if i != j and items[i] == items[j]:
                return True
    return False
```

With 1,000 items: up to 1,000,000 operations. With 10,000 items: up to 100,000,000 operations. Quickly becomes too slow.

---

## Concept 5: Spotting Complexity at a Glance

You don't need to count every operation. Just look at the structure:

| What you see in the code | Complexity |
|--------------------------|------------|
| No loops, just a statement | O(1) |
| One loop over the input | O(n) |
| Two separate loops (one after the other) | O(n) — not O(2n) |
| A loop inside a loop, both over the input | O(n²) |
| Cutting the input in half each step | O(log n) |

---

## Assignment Instructions

**File to create:** `module_04/complexity.py`

You will implement five functions and analyze every one of them with a complexity label. The analysis is just as important as the code — your instructor will look at both.

---

### Step 1 — `find_first(lst, target)`

Write a function that scans through `lst` from left to right and returns the **index** of the first place `target` appears. Return `-1` if it's not found.

```python
print(find_first([5, 3, 8, 1, 9], 8))    # 2
print(find_first([5, 3, 8, 1, 9], 7))    # -1
print(find_first([1, 2, 3, 2, 1], 2))    # 1  (first occurrence)
```

Above the function, add a comment block:
```python
# Time: O(1) best case (target is first), O(n) average/worst case
# Space: O(1) — no extra memory used
```

---

### Step 2 — `has_duplicates_slow(lst)`

Write a function that checks whether any value appears more than once. Use **two nested loops** to compare every pair of items.

```python
print(has_duplicates_slow([1, 2, 3, 4]))     # False
print(has_duplicates_slow([1, 2, 3, 1]))     # True
```

Add the complexity comment. (Hint: two nested loops over the same list = ?)

---

### Step 3 — `has_duplicates_fast(lst)`

Write a **second version** of duplicate detection. This time, use a Python `set`. As you go through the list, add each item to the set. If an item is already in the set before you add it, you found a duplicate.

```python
def has_duplicates_fast(lst):
    seen = set()
    for item in lst:
        if item in seen:    # Checking a set is O(1)!
            return True
        seen.add(item)
    return False
```

Add the complexity comment. This should be much better than the slow version.

Verify they give the same answers:
```python
test = [3, 1, 4, 1, 5, 9]
assert has_duplicates_slow(test) == has_duplicates_fast(test)
print("Both agree!")
```

---

### Step 4 — `binary_search(sorted_lst, target)`

Write a binary search function. It requires a **sorted** list to work correctly.

The logic: look at the middle item. If it's the target, you're done. If the target is smaller, it must be in the left half — ignore the right. If the target is bigger, it must be in the right half — ignore the left. Repeat.

```python
nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))     # 3
print(binary_search(nums, 6))     # -1
print(binary_search(nums, 1))     # 0
print(binary_search(nums, 15))    # 7
```

Add the complexity comment. (Hint: you cut the search space in half each time = ?)

---

### Step 5 — `sum_pairs(lst)`

Return a list of all pairs `(a, b)` from `lst` where `a + b == 0`. Use nested loops (every combination of two elements).

```python
print(sum_pairs([-3, 1, 3, -1, 2]))   # [(-3, 3), (1, -1)]
print(sum_pairs([1, 2, 3]))            # []
```

To avoid duplicates like `(-3, 3)` AND `(3, -3)`, only include a pair when the first index is less than the second: `for i in range(len(lst)): for j in range(i+1, len(lst)):`.

Add the complexity comment.

---

### Step 6 — Benchmark slow vs. fast duplicate detection

Time both functions on a large list. The difference should be dramatic.

```python
import time

big_list = list(range(5000))    # 5000 unique numbers — worst case (no duplicates)

start = time.time()
has_duplicates_slow(big_list)
print(f"Slow (O(n²)): {time.time() - start:.4f} seconds")

start = time.time()
has_duplicates_fast(big_list)
print(f"Fast (O(n)):  {time.time() - start:.4f} seconds")
```

Add a comment after the benchmark stating which was faster and roughly how many times faster.

---

### Step 7 — Written summary at the top of your file

At the very top of your file, add this table filled in with your own answers:

```python
"""
Function               | Time Complexity (worst) | Space  | Why?
-----------------------|-------------------------|--------|---------------------------
find_first             |                         |        |
has_duplicates_slow    |                         |        |
has_duplicates_fast    |                         |        |
binary_search          |                         |        |
sum_pairs              |                         |        |
"""
```

---

### Checklist Before Submitting

- [ ] All five functions are implemented and return correct results
- [ ] Every function has a complexity comment (time and space)
- [ ] `has_duplicates_fast` uses a set, not nested loops
- [ ] `binary_search` only works on a sorted list (state this in a comment)
- [ ] `sum_pairs` doesn't produce duplicate pairs like `(-3,3)` and `(3,-3)`
- [ ] The benchmark runs and prints times for both duplicate functions
- [ ] A comment states which was faster
- [ ] The summary table at the top is filled in for all five functions
