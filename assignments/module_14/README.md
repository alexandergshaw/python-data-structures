# Week 14 — Algorithmic Paradigms
### Greedy Algorithms, Divide and Conquer, and Maximum Subarray

---

## Welcome!

Up to now you've learned specific algorithms for specific problems. This week you zoom out and learn **general strategies** — ways of thinking about whole *families* of problems. Once you know these patterns, you'll recognize them in new problems you've never seen before.

---

## Concept 1: What Is an Algorithmic Paradigm?

A **paradigm** is a general approach or philosophy for solving problems.

**Analogy:** In cooking, there are general strategies: "sauté then deglaze," "low and slow," "mise en place." Once you know these strategies, you can apply them to many different recipes. Algorithmic paradigms are the same thing — general strategies you apply to many different coding problems.

The three you'll learn this week:

1. **Greedy** — always make the locally best choice right now
2. **Divide and Conquer** — split the problem, solve the parts, combine
3. **Dynamic Programming** (preview) — like divide and conquer, but cache repeated work

---

## Concept 2: Greedy Algorithms

A **greedy algorithm** makes the decision that looks best *at this moment*, without looking ahead. It never goes back and reconsiders.

**Analogy:** Imagine you're hiking and want to reach the highest peak. A greedy hiker always takes the steepest step available right now. Sometimes this works perfectly. Sometimes you end up on a small hill and the actual peak is in the other direction — because the greedy choice now led you wrong.

**The key question:** Does always choosing the locally best option guarantee the globally best result?

If yes → greedy works! ✅
If no → you need Dynamic Programming ❌

### Activity Selection (Greedy Works Here)

**Problem:** You have a list of events, each with a start and end time. You can only attend one event at a time. What's the maximum number of events you can attend?

**Greedy strategy:** Always pick the event that ends soonest — it leaves the most time available for future events.

```
Events: (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11)
Sorted by end time:
  (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11)

Pick (1,4)   — first to end
Skip (3,5)   — starts at 3, but (1,4) ends at 4; 3 < 4, conflict
Skip (0,6)   — starts at 0 < 4, conflict
Pick (5,7)   — starts at 5 ≥ 4, no conflict ✅
Skip (3,9)   — starts at 3 < 7, conflict
Skip (5,9)   — starts at 5 < 7, conflict
Skip (6,10)  — starts at 6 < 7, conflict
Pick (8,11)  — starts at 8 ≥ 7 ✅

Result: 3 events: (1,4), (5,7), (8,11)
```

```python
def activity_selection(activities):
    sorted_acts = sorted(activities, key=lambda x: x[1])   # Sort by END time
    selected = [sorted_acts[0]]

    for start, end in sorted_acts[1:]:
        if start >= selected[-1][1]:    # Starts after last selected one ends?
            selected.append((start, end))

    return selected
```

### When Greedy Fails

Greedy doesn't always work. Consider making change with coins [10, 6, 1] for a target of 12:
- Greedy (take the biggest coin first): 10 + 1 + 1 = **3 coins**
- Optimal: 6 + 6 = **2 coins**

Greedy fails here because picking 10 traps you into needing two 1s.

---

## Concept 3: Divide and Conquer

**Divide and Conquer** splits a big problem into smaller independent pieces, solves each piece (often recursively), and combines the results.

**Analogy:** You're cleaning a messy house. It's overwhelming as one task. But split it: one person does the kitchen, one does the living room, one does the bedrooms. Each smaller task is easier, and when everyone finishes, the whole house is clean.

You've already used divide and conquer:
- **Merge sort**: split list in half, sort each half, merge
- **Binary search**: cut the search space in half each step

The key: **the sub-problems must be independent** (solving one doesn't affect the other). If they overlap (same sub-problem appears multiple times), you need Dynamic Programming.

### Maximum Subarray — Kadane's Algorithm

**Problem:** Given a list of numbers (including negatives), find the contiguous subarray with the largest sum.

```
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
              ^^^^^^^^^
The subarray [4, -1, 2, 1] has sum 6 — the maximum possible.
```

**Kadane's Algorithm** solves this with a clever greedy/DP hybrid in O(n):

At each position, ask: "Am I better off **extending** the current running total, or **starting fresh** from just this number?"

```python
def max_subarray_kadane(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)  # Extend or start fresh?
        max_sum = max(max_sum, current_sum)         # Is this a new maximum?

    return max_sum
```

Trace through `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:
```
num=-2: current=-2, max=-2
num= 1: current=max(1, -2+1)=max(1,-1)=1,  max=1
num=-3: current=max(-3, 1-3)=max(-3,-2)=-2, max=1
num= 4: current=max(4, -2+4)=max(4,2)=4,   max=4
num=-1: current=max(-1, 4-1)=max(-1,3)=3,  max=4
num= 2: current=max(2, 3+2)=max(2,5)=5,    max=5
num= 1: current=max(1, 5+1)=max(1,6)=6,    max=6
num=-5: current=max(-5, 6-5)=max(-5,1)=1,  max=6
num= 4: current=max(4, 1+4)=max(4,5)=5,    max=6
```
Answer: 6 ✅

---

## Assignment Instructions

**File to create:** `module_14/paradigms.py`

---

### Step 1 — `activity_selection(activities)`

Implement the greedy activity selector described above. Return the list of selected `(start, end)` tuples.

```python
activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11)]
print(activity_selection(activities))
# [(1, 4), (5, 7), (8, 11)]
```

Verify: make sure no two selected activities overlap.

---

### Step 2 — `coin_change_greedy(coins, amount)`

Given coins sorted largest-first, always take the biggest coin that fits. Return the list of coins used.

```python
print(coin_change_greedy([25, 10, 5, 1], 41))
# [25, 10, 5, 1]  — 4 coins

print(coin_change_greedy([25, 10, 5, 1], 30))
# [25, 5]  — 2 coins
```

Now show the failure case. Add a comment explaining why greedy fails:

```python
result = coin_change_greedy([10, 6, 1], 12)
print(result)   # [10, 1, 1]  — 3 coins (WRONG — optimal is [6, 6] = 2 coins)
# COMMENT: Greedy fails here because choosing 10 makes it impossible to use 6+6.
# Dynamic Programming (Week 15) handles this correctly.
```

---

### Step 3 — `max_subarray_kadane(nums)`

Implement Kadane's algorithm. Return only the **sum** (not the subarray itself).

```python
print(max_subarray_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_kadane([1, 2, 3, 4, 5]))                   # 15
print(max_subarray_kadane([-3, -1, -4, -2]))                  # -1 (all negative!)
print(max_subarray_kadane([0, 0, 0]))                         # 0
```

For all-negative arrays: the maximum subarray is the single largest (least negative) number. Your code should handle this correctly without any special case, because `max(num, current_sum + num)` naturally picks the larger option.

---

### Step 4 — `max_subarray_indices(nums)`

Extend Kadane's to also return the **start and end indices** of the best subarray.

```python
total, start, end = max_subarray_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(total, start, end)    # 6 3 6
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(nums[start:end+1])    # [4, -1, 2, 1]
```

**Hint:** Track `current_start` (the start of the current running total). When you start fresh (`current_sum = num`), update `current_start = current_index`. When you update `max_sum`, save `best_start = current_start` and `best_end = current_index`.

---

### Step 5 — Classroom scheduler

Use `activity_selection` to solve a real scheduling problem:

```python
def schedule_classes(requests):
    # requests is a list of (student_name, start_hour, end_hour)
    # Schedule the maximum number of non-overlapping classes
    # Print a readable schedule

    activities = [(start, end, name) for name, start, end in requests]
    # Hint: sort by end time (index 1), then apply greedy selection

requests = [
    ("Alice",  9, 10),
    ("Bob",    9, 11),
    ("Carol",  10, 11),
    ("David",  11, 13),
    ("Eve",    12, 14),
    ("Frank",  13, 15),
]
schedule_classes(requests)
```

Expected output:
```
Selected 4 classes:
  Alice  : 9:00 - 10:00
  Carol  : 10:00 - 11:00
  David  : 11:00 - 13:00
  Frank  : 13:00 - 15:00
```

---

### Step 6 — Paradigm summary at the top of your file

```python
"""
Algorithmic Paradigm Cheat Sheet
---------------------------------
GREEDY:
  - Make the locally best choice at each step, never look back.
  - Works when: local optimality = global optimality (activity selection, Huffman).
  - Fails when: local optimality misleads (coin change with weird coins, knapsack).

DIVIDE AND CONQUER:
  - Split → solve independently → combine.
  - Sub-problems are INDEPENDENT (no overlap).
  - Examples: merge sort, binary search, max subarray (divide-and-conquer version).

DYNAMIC PROGRAMMING (Week 15 preview):
  - Like divide and conquer, but sub-problems OVERLAP.
  - Cache results so you never solve the same sub-problem twice.
  - Examples: coin change, knapsack, Fibonacci, LCS.
"""
```

---

### Checklist Before Submitting

- [ ] `activity_selection()` returns the correct non-overlapping set
- [ ] `coin_change_greedy()` works correctly with standard coins
- [ ] `coin_change_greedy([10,6,1], 12)` shows the greedy failure (returns 3 coins, not 2)
- [ ] A comment explains why greedy fails for that case
- [ ] `max_subarray_kadane()` handles all-negative arrays without a special case
- [ ] `max_subarray_indices()` returns correct sum, start, and end index
- [ ] `schedule_classes()` prints a readable schedule with correct selections
- [ ] The paradigm summary docstring is present at the top of the file
