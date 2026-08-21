# Week 14 — Algorithmic Paradigms

An **algorithmic paradigm** is a high-level strategy for solving a class of problems. This week you study three of the most important: **greedy algorithms**, **divide and conquer**, and you see how they compare to **dynamic programming** (next week). Understanding which paradigm to apply — and why — is a key problem-solving skill.

---

## Concepts Covered

### 1. Greedy Algorithms

A **greedy algorithm** makes the locally optimal choice at each step, hoping that these local choices lead to a globally optimal solution.

**Key question to ask:** "Does choosing the best option right now always lead to the best overall answer?" If yes, a greedy approach works. If no, you need dynamic programming.

#### Activity Selection Problem

Given a set of activities with start and end times, select the maximum number of non-overlapping activities.

**Greedy strategy:** Always pick the activity that finishes earliest (leaves the most room for future activities).

```python
def activity_selection(activities):
    # Sort by finish time
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected = [sorted_acts[0]]

    for start, end in sorted_acts[1:]:
        # Only pick if this activity starts after the last selected one ends
        if start >= selected[-1][1]:
            selected.append((start, end))

    return selected

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
print(activity_selection(activities))
# [(1, 4), (5, 7), (8, 11)]  — 3 non-overlapping activities
```

Why greedy works here: finishing early is always at least as good as any other choice — it never prevents a future choice that would have been possible otherwise.

---

### 2. Greedy Does Not Always Work

Consider the coin change problem: make 30 cents with coins [25, 10, 5, 1].

Greedy (always pick the largest coin): 25 + 5 = 2 coins. ✓ Works here.

But with coins [10, 6, 1] and target 12:
- Greedy: 10 + 1 + 1 = 3 coins.
- Optimal: 6 + 6 = 2 coins. ✗ Greedy fails.

When greedy fails, use **dynamic programming** (Week 15).

---

### 3. Divide and Conquer

**Divide and conquer** splits a problem into smaller subproblems, solves each independently, and combines the results.

The three steps:
1. **Divide:** Split the problem into subproblems.
2. **Conquer:** Solve each subproblem (often recursively).
3. **Combine:** Merge the results.

You have already seen divide and conquer in:
- **Merge sort** (divide the list, sort each half, merge)
- **Binary search** (halve the search space each step)

---

### 4. Maximum Subarray Sum (Kadane's Algorithm)

Find the contiguous subarray within a list that has the largest sum.

**Divide and conquer approach** (O(n log n)):
- Recursively solve the left and right halves.
- Find the maximum subarray that crosses the midpoint.
- Return the maximum of the three.

**Kadane's Algorithm** — a simpler O(n) greedy/DP hybrid:

```python
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        # Either extend the current subarray or start fresh
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6  (subarray [4,-1,2,1])
```

The key decision at each step: "Is it better to add this number to the running sum, or start a new subarray from here?"

---

### 5. Greedy vs. Divide and Conquer vs. Dynamic Programming

| Paradigm              | Strategy                                          | When to use                                             |
|-----------------------|---------------------------------------------------|---------------------------------------------------------|
| Greedy                | Make the locally best choice at each step         | When local optimality guarantees global optimality      |
| Divide and conquer    | Split, solve independently, combine               | When subproblems are independent (no overlap)           |
| Dynamic Programming   | Split, solve, **cache** repeated subproblems      | When subproblems overlap (same sub-problem solved twice)|

---

## Hints for This Week's Assignment

- **Prove your greedy is correct (informally).** Ask: "Can I construct a counterexample where the greedy choice fails?" If you can, you need DP.
- For activity selection, sorting by finish time is the key insight. Try sorting by start time or duration — you'll see those give wrong answers.
- Kadane's algorithm has only two decisions per step: extend or restart. If you understand those two lines, you understand the algorithm.
- For divide and conquer problems, identify: (1) how to divide, (2) what the base case is, (3) how to combine results.
- The maximum subarray that **crosses the midpoint** in the divide-and-conquer approach is found by scanning outward from the midpoint in both directions — don't skip this step.
- Think about edge cases: all-negative arrays (the max subarray is the single largest value), single-element arrays, and arrays of all zeros.

---

## Assignment Instructions

**File to create:** `module_14/paradigms.py`

You will implement three greedy algorithms, Kadane's algorithm, and a divide-and-conquer maximum subarray — then compare paradigms. Work through each step in order.

---

### Step 1 — `activity_selection(activities)`

Given a list of `(start, end)` tuples, return the maximum set of non-overlapping activities.

```python
activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11)]
print(activity_selection(activities))
# [(1, 4), (5, 7), (8, 11)]
```

**Steps to implement:**
1. Sort `activities` by finish time (second element of each tuple).
2. Always pick the activity with the earliest finish time that starts at or after the last selected activity ended.

Test with your own set of activities and verify the result is truly non-overlapping.

---

### Step 2 — `coin_change_greedy(coins, amount)`

Given a **sorted (descending) list of coin denominations** and a target amount, return the minimum list of coins using a greedy approach (always take the largest coin that fits).

```python
print(coin_change_greedy([25, 10, 5, 1], 41))
# [25, 10, 5, 1]  → 4 coins

print(coin_change_greedy([25, 10, 5, 1], 30))
# [25, 5]  → 2 coins
```

Then show that greedy **fails** with non-standard coins:

```python
# With coins [10, 6, 1], target 12:
print(coin_change_greedy([10, 6, 1], 12))
# [10, 1, 1]  → 3 coins  ← WRONG (optimal is [6, 6] = 2 coins)
```

Add a comment: `# Greedy fails here — DP needed (see module 15)`

---

### Step 3 — `max_subarray_kadane(nums)`

Implement Kadane's algorithm. Return the **maximum subarray sum** (not the subarray itself — just the sum).

```python
print(max_subarray_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
print(max_subarray_kadane([1, 2, 3, 4, 5]))                    # 15
print(max_subarray_kadane([-3, -1, -4, -2]))                   # -1  (all negative)
print(max_subarray_kadane([0, 0, 0]))                          # 0
```

**Edge case:** When all numbers are negative, the maximum subarray is the single largest (least negative) number.

---

### Step 4 — `max_subarray_indices(nums)`

Extend Kadane's to also return the **start and end indices** of the maximum subarray (not just the sum).

```python
total, start, end = max_subarray_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(total, start, end)      # 6 3 6
print(nums[start:end+1])      # [4, -1, 2, 1]
```

**Hint:** Track `current_start` (resets when you start fresh), and update `best_start, best_end` whenever you find a new max.

---

### Step 5 — `max_subarray_divide_conquer(nums)`

Implement the divide-and-conquer version. This function must:
1. If `len(nums) == 1`, return `nums[0]` (base case).
2. Split the list in half.
3. Recursively find the max subarray sum in the **left half**.
4. Recursively find the max subarray sum in the **right half**.
5. Find the max subarray sum that **crosses the midpoint** (scan outward from the midpoint in both directions).
6. Return the maximum of the three.

```python
print(max_subarray_divide_conquer([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
```

Verify it matches Kadane's result.

---

### Step 6 — Greedy class scheduler

Write a function `schedule_classes(requests)` where `requests` is a list of `(student_name, start, end)` tuples. Use your activity selection algorithm to schedule the maximum number of classes in a single classroom, then print a schedule:

```python
requests = [
    ("Alice", 9, 10),
    ("Bob", 9, 11),
    ("Carol", 10, 11),
    ("David", 11, 13),
    ("Eve", 12, 14),
    ("Frank", 13, 15),
]
schedule_classes(requests)
# Selected 4 classes:
#   Alice    : 9:00 - 10:00
#   Carol    : 10:00 - 11:00
#   David    : 11:00 - 13:00
#   Frank    : 13:00 - 15:00
```

---

### Step 7 — Paradigm comparison comment block

At the top of your file, add a docstring summarizing when to use each paradigm:

```python
"""
Paradigm Comparison
-------------------
Greedy:
  - Makes locally optimal choice at each step.
  - Fast (usually O(n log n) due to sorting).
  - Works for: activity selection, fractional knapsack, Huffman coding.
  - Does NOT work for: coin change with arbitrary coins, 0/1 knapsack.

Divide and Conquer:
  - Split → solve independently → combine.
  - Works for: merge sort, binary search, max subarray.
  - Subproblems must be INDEPENDENT (no overlap).

Dynamic Programming:
  - Split → solve → CACHE repeated subproblems.
  - Use when greedy fails and subproblems overlap.
  - Works for: coin change, knapsack, LCS (see module 15).
"""
```

---

### Checklist Before Submitting

- [ ] `activity_selection()` returns the correct non-overlapping set sorted by finish time.
- [ ] `coin_change_greedy()` works correctly for standard coins and demonstrates failure for `[10, 6, 1]`.
- [ ] `max_subarray_kadane()` handles all-negative arrays and all-zero arrays.
- [ ] `max_subarray_indices()` returns correct sum, start index, and end index.
- [ ] `max_subarray_divide_conquer()` returns the same answer as Kadane's for all test cases.
- [ ] `schedule_classes()` prints a readable schedule.
- [ ] The paradigm comparison docstring is present at the top of the file.
