# Week 15 — Dynamic Programming
### Memoization, Tabulation, and Classic DP Problems

---

## Welcome!

Dynamic programming (DP) sounds intimidating, but the core idea is simple: **don't solve the same sub-problem twice**. Once you've computed an answer, store it. If you need it again, look it up instead of recomputing.

This one idea — caching repeated work — turns algorithms that would take billions of years into ones that finish in milliseconds.

---

## Concept 1: The Problem DP Solves

Remember `fibonacci` from Week 8?

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

This works, but it's catastrophically slow for large n. To compute `fib(40)`, it makes billions of function calls, recalculating `fib(2)`, `fib(3)`, etc. thousands of times each.

**Analogy:** You call customer service for a question. They put you on hold to find the answer. Ten minutes later you call again with the same question. They put you on hold again. And again. And again. Instead, they could just write the answer on a sticky note the first time and read it instantly every time after.

That sticky note is the **cache** (or **memo**).

---

## Concept 2: When to Use DP

Two conditions must both be true:

1. **Overlapping sub-problems:** The same smaller problem is solved multiple times (like `fib(5)` being needed by both `fib(7)` and `fib(6)`)
2. **Optimal substructure:** The best solution to the big problem is built from the best solutions to the smaller problems

If both conditions hold → DP will work (and dramatically speed things up).

---

## Concept 3: Memoization — Top-Down DP

Keep the recursive structure but add a dictionary to cache results:

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]        # Already computed — just look it up
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(50))   # Instant!  Without memoization: would take hours
```

**How it works:** The first time you compute `fibonacci(10)`, store the result. Every future call to `fibonacci(10)` returns the stored result immediately.

**Analogy:** You're studying for a history test. The first time you look up when the Civil War started, you write it on a flashcard. Every time after, you just read the flashcard — no more looking it up.

---

## Concept 4: Tabulation — Bottom-Up DP

Instead of starting from the top (the big problem) and working down recursively, start from the bottom (the smallest sub-problems) and build up:

```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)   # Create a table
    dp[0] = 0             # Base case
    dp[1] = 1             # Base case
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]   # Fill in from small to large
    return dp[n]
```

No recursion at all — just a loop filling in a table. This is often faster because there's no function call overhead.

**Analogy:** You're building a staircase. Instead of starting at the top and figuring out what needs to go below it, you build from the ground up — each step rests on the ones below it.

---

## Concept 5: Coin Change — DP vs. Greedy

**Problem:** What's the minimum number of coins to make a target amount?

Remember from Week 14 that greedy fails with coins `[10, 6, 1]` for amount `12`. DP gets it right:

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)   # Start assuming impossible
    dp[0] = 0    # 0 coins needed to make $0

    for amt in range(1, amount + 1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([10, 6, 1], 12))    # 2  (6 + 6)
print(coin_change([1, 5, 10, 25], 36)) # 3  (25 + 10 + 1)
print(coin_change([2], 3))            # -1  (impossible)
```

**Reading the recurrence:** `dp[amt]` = the fewest coins needed to make `amt`. For each amount, try subtracting each coin — if `dp[amt - coin] + 1` is better than what we have, update.

**Analogy:** You're building a Lego tower exactly N blocks tall. `dp[n]` = the fewest pieces needed. For each piece size you have, try adding it on top of the best tower of height `n - piece_size`.

---

## Concept 6: Longest Common Subsequence (LCS)

**Problem:** Given two strings, how long is the longest sequence of characters that appears in both (in order, but not necessarily contiguous)?

```
s1 = "ABCBDAB"
s2 = "BDCAB"
LCS = "BCAB" or "BDAB"  →  length 4
```

**2D table approach:**

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1   # Characters match: extend
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # Take the better of skipping either

    return dp[m][n]
```

---

## Concept 7: 0/1 Knapsack

**Problem:** You have items with weights and values. Your bag has a weight limit. Maximize the total value you can carry. Each item can only be taken once.

```
Items:    weight [1, 3, 4, 5], value [1, 4, 5, 7]
Capacity: 7
Best:     take items 1 and 2 (weight 3+4=7, value 4+5=9)
```

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            # Option 1: don't take item i
            dp[i][w] = dp[i-1][w]
            # Option 2: take item i (only if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][W]
```

---

## Concept 8: Climbing Stairs

**Problem:** You can climb 1 or 2 steps at a time. How many distinct ways can you reach step n?

```
n=1: 1 way (just: 1)
n=2: 2 ways (1+1, or 2)
n=3: 3 ways (1+1+1, 1+2, 2+1)
n=4: 5 ways
```

This is exactly the Fibonacci sequence! `ways(n) = ways(n-1) + ways(n-2)`.

---

## Assignment Instructions

**File to create:** `module_15/dynamic_programming.py`

---

### Step 1 — `fib_memo(n)` — memoization

Write Fibonacci using a dictionary cache. Do NOT use `@lru_cache` — implement it manually.

```python
def fib_memo(n, memo={}):
    ...

print(fib_memo(0))    # 0
print(fib_memo(1))    # 1
print(fib_memo(10))   # 55
print(fib_memo(50))   # 12586269025  ← must be instant
```

---

### Step 2 — `fib_tab(n)` — tabulation

Fill in a list from index 0 up to n.

```python
print(fib_tab(10))   # 55
assert fib_memo(30) == fib_tab(30), "They should agree!"
print("Both Fibonacci implementations agree.")
```

---

### Step 3 — `coin_change(coins, amount)`

Bottom-up tabulation. Initialize `dp` with `float('inf')`, set `dp[0] = 0`, fill in the rest.

```python
print(coin_change([1, 5, 10, 25], 36))  # 3
print(coin_change([10, 6, 1], 12))      # 2  ← DP beats greedy!
print(coin_change([2], 3))              # -1 (impossible)
print(coin_change([1], 0))             # 0
```

---

### Step 4 — `climb_stairs(n)`

Return the number of distinct ways to reach step n, taking 1 or 2 steps at a time.

```python
print(climb_stairs(1))    # 1
print(climb_stairs(2))    # 2
print(climb_stairs(5))    # 8
print(climb_stairs(10))   # 89
```

Add a comment noting that this is the same recurrence as Fibonacci. Why? Because each position `n` can be reached from `n-1` (one step) or `n-2` (two steps) — the same as Fibonacci's addition.

---

### Step 5 — `lcs(s1, s2)` — length only

Return the length of the longest common subsequence.

```python
print(lcs("ABCBDAB", "BDCAB"))      # 4
print(lcs("AGGTAB", "GXTXAYB"))     # 4
print(lcs("", "ABC"))               # 0
print(lcs("ABC", "ABC"))            # 3
```

---

### Step 6 — `lcs_sequence(s1, s2)` — actual string

Return the actual LCS string by backtracking through the DP table.

**How to backtrack:** Start at `dp[m][n]`. If `s1[i-1] == s2[j-1]`, that character is part of the LCS — prepend it and move diagonally (`i-1, j-1`). Otherwise, move in the direction of the larger value (`i-1` or `j-1`).

```python
print(lcs_sequence("ABCBDAB", "BDCAB"))   # "BCAB" or "BDAB"
```

---

### Step 7 — `knapsack(weights, values, capacity)`

Return the maximum total value.

```python
weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
print(knapsack(weights, values, 7))   # 9
print(knapsack(weights, values, 0))   # 0
print(knapsack([], [], 10))           # 0
```

---

### Step 8 — Benchmark

Time `fib_memo` and `fib_tab` each called 1000 times for `n=35`. Print the results and explain in a comment which is faster and why.

```python
import time

start = time.time()
for _ in range(1000):
    fib_memo(35)
print(f"Memo: {time.time()-start:.4f}s")

start = time.time()
for _ in range(1000):
    fib_tab(35)
print(f"Tab:  {time.time()-start:.4f}s")

# Comment: Which is faster? Tabulation is usually faster because it
# avoids the overhead of thousands of recursive function calls.
```

---

### Step 9 — Summary docstring at the top of your file

```python
"""
Dynamic Programming Cheat Sheet
---------------------------------
WHEN TO USE DP:
  1. Overlapping sub-problems: same sub-problem appears multiple times
  2. Optimal substructure: best big answer = built from best small answers

TWO STYLES:
  Memoization (top-down): Keep recursion, add a cache dictionary.
  Tabulation (bottom-up): Fill a table iteratively from smallest to largest.

RECURRENCES:
  Fibonacci:      dp[n] = dp[n-1] + dp[n-2]
  Coin change:    dp[a] = min(dp[a-c] + 1) for each coin c
  Climbing stairs: dp[n] = dp[n-1] + dp[n-2]   (same as Fibonacci!)
  LCS:            dp[i][j] = dp[i-1][j-1]+1 if chars match, else max(dp[i-1][j], dp[i][j-1])
  Knapsack:       dp[i][w] = max(skip item, take item if it fits)
"""
```

---

### Checklist Before Submitting

- [ ] `fib_memo(50)` completes instantly (memoization working)
- [ ] `fib_memo` and `fib_tab` agree for n=30
- [ ] `coin_change([10,6,1], 12)` returns 2 — DP beats greedy!
- [ ] `coin_change([2], 3)` returns -1 (impossible case handled)
- [ ] `climb_stairs` matches Fibonacci offset by one
- [ ] `lcs` returns correct lengths for all test cases
- [ ] `lcs_sequence` returns a valid common subsequence string
- [ ] `knapsack` handles empty items and zero capacity without crashing
- [ ] Benchmark is present with a comment explaining results
- [ ] Summary docstring is at the top of the file
