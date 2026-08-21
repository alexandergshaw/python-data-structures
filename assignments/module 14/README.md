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
