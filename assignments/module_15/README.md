# Week 15 — Dynamic Programming

**Dynamic programming (DP)** solves problems by breaking them into overlapping subproblems, solving each subproblem only once, and storing the result to avoid redundant computation. It's not a single algorithm — it's a technique you can apply to a whole family of optimization and counting problems.

---

## Concepts Covered

### 1. When to Use Dynamic Programming

Two conditions must both be true:

1. **Optimal substructure:** The optimal solution to the problem contains optimal solutions to its subproblems.
2. **Overlapping subproblems:** The same subproblem is solved multiple times during a naive recursive solution.

If only the first condition holds (no overlapping subproblems), divide and conquer is sufficient. DP shines when you would otherwise redo the same work thousands of times.

---

### 2. Memoization (Top-Down DP)

Add a **cache** to a recursive solution so each subproblem is solved at most once:

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(50))  # Instant — no repeated work
```

Without memoization, `fibonacci(50)` makes ~2^50 calls. With it, exactly 50 unique subproblems are solved.

---

### 3. Tabulation (Bottom-Up DP)

Build a table starting from the smallest subproblems and fill it up to the answer — no recursion needed:

```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

Bottom-up avoids recursion stack overhead and is often faster in practice.

---

### 4. Coin Change

**Problem:** Given coin denominations and a target amount, find the minimum number of coins needed.

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0   # Base case: 0 coins needed to make $0

    for amt in range(1, amount + 1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 5, 10, 25], 36))  # 3  (25 + 10 + 1)
print(coin_change([10, 6, 1], 12))      # 2  (6 + 6)
```

**Key insight:** `dp[amt]` = the fewest coins needed to make exactly `amt`. For each amount, try every coin and take the best option.

---

### 5. Longest Common Subsequence (LCS)

**Problem:** Find the length of the longest subsequence common to two strings (characters don't need to be contiguous).

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1   # Characters match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Take best

    return dp[m][n]

print(lcs("ABCBDAB", "BDCAB"))  # 4  (BCAB or BDAB)
```

---

### 6. 0/1 Knapsack

**Problem:** Given items with weights and values, and a knapsack with capacity W, maximize value without exceeding weight. Each item can be taken at most once.

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            # Don't take item i
            dp[i][w] = dp[i - 1][w]
            # Take item i (if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][W]

weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
print(knapsack(weights, values, 7))  # 9  (items with weight 3 and 4)
```

---

### 7. Climbing Stairs

**Problem:** You can climb 1 or 2 steps at a time. How many distinct ways can you reach the top of an n-step staircase?

```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]   # Same recurrence as Fibonacci!
    return dp[n]

print(climb_stairs(5))  # 8
```

---

## Hints for This Week's Assignment

- **Start with the recurrence relation.** Before writing any code, express the solution as: "dp[i] depends on dp[smaller subproblems]". The code almost writes itself from there.
- For 2D DP (LCS, knapsack), draw the table on paper and fill in a few cells by hand — this makes the pattern obvious.
- `dp[0]` is almost always a base case: 0 coins to make $0, 0 ways to pick 0 items, 0 length with empty strings.
- Use `float('inf')` as the initial value when you want to minimize — it's larger than any real answer, so the first valid solution will always replace it.
- Memoization (top-down) is often easier to write first — add `@functools.lru_cache(maxsize=None)` above a recursive function to get automatic memoization.
- Once you understand the recursive solution, convert it to tabulation (bottom-up) for better performance and no recursion limits.

---

## Assignment Instructions

**File to create:** `module_15/dynamic_programming.py`

You will implement five classic DP problems in two styles each (memoization and tabulation), then compare them. Work through each step in order.

---

### Step 1 — Fibonacci: memoization version

Write `fib_memo(n, memo={})` that computes the nth Fibonacci number using top-down memoization. Do **not** use `@lru_cache` — implement the cache manually with a dictionary.

```python
print(fib_memo(0))    # 0
print(fib_memo(1))    # 1
print(fib_memo(10))   # 55
print(fib_memo(50))   # 12586269025  (instant)
```

---

### Step 2 — Fibonacci: tabulation version

Write `fib_tab(n)` that builds a list `dp` of size `n+1` and fills it bottom-up.

```python
print(fib_tab(10))   # 55
print(fib_tab(50))   # 12586269025
assert fib_memo(30) == fib_tab(30), "Mismatch!"
```

---

### Step 3 — Coin Change

Write `coin_change(coins, amount)` using **bottom-up tabulation**. Return the minimum number of coins to make `amount`, or `-1` if it's impossible.

```python
print(coin_change([1, 5, 10, 25], 36))   # 3  (25+10+1)
print(coin_change([10, 6, 1], 12))       # 2  (6+6) — greedy fails, DP wins!
print(coin_change([2], 3))               # -1  (impossible)
print(coin_change([1], 0))               # 0
```

**Hint:** Initialize `dp = [float('inf')] * (amount + 1)`, set `dp[0] = 0`, then for each amount from 1 to `amount`, try every coin.

---

### Step 4 — Climbing Stairs

Write `climb_stairs(n)` that returns the number of distinct ways to climb `n` stairs, taking 1 or 2 steps at a time.

```python
print(climb_stairs(1))    # 1
print(climb_stairs(2))    # 2
print(climb_stairs(5))    # 8
print(climb_stairs(10))   # 89
```

Add a comment explaining why the recurrence is the same as Fibonacci.

---

### Step 5 — Longest Common Subsequence

Write `lcs(s1, s2)` using a 2D DP table. Return the **length** of the longest common subsequence.

```python
print(lcs("ABCBDAB", "BDCAB"))      # 4
print(lcs("AGGTAB", "GXTXAYB"))     # 4
print(lcs("", "ABC"))               # 0
print(lcs("ABC", "ABC"))            # 3
```

Then write `lcs_sequence(s1, s2)` that returns the **actual subsequence string** (not just the length) by backtracking through the DP table.

```python
print(lcs_sequence("ABCBDAB", "BDCAB"))   # "BCAB" or "BDAB"
```

---

### Step 6 — 0/1 Knapsack

Write `knapsack(weights, values, capacity)` using a 2D DP table. Return the maximum total value achievable without exceeding `capacity`. Each item can be taken at most once.

```python
weights  = [1, 3, 4, 5]
values   = [1, 4, 5, 7]
print(knapsack(weights, values, 7))   # 9  (items 1 and 2: weight 3+4, value 4+5)
print(knapsack(weights, values, 0))   # 0
print(knapsack([], [], 10))           # 0
```

Also write `knapsack_items(weights, values, capacity)` that returns the **list of item indices** selected (backtracking through the table).

```python
print(knapsack_items(weights, values, 7))   # [1, 2]  (0-indexed)
```

---

### Step 7 — Performance: memoization vs. tabulation

Time both Fibonacci implementations for `n = 35` and print results:

```python
import time

start = time.time()
for _ in range(1000):
    fib_memo(35)
print(f"Memo (1000 calls, n=35): {time.time()-start:.4f}s")

start = time.time()
for _ in range(1000):
    fib_tab(35)
print(f"Tab  (1000 calls, n=35): {time.time()-start:.4f}s")
```

In a comment, explain which is faster and why. (Tabulation usually wins because it avoids function call overhead.)

---

### Step 8 — DP summary table

At the top of your file (as a docstring), add a summary of each problem's recurrence relation:

```python
"""
Problem            | Recurrence
-------------------|------------------------------------------------------------
Fibonacci          | fib(n) = fib(n-1) + fib(n-2)
Coin Change        | dp[a] = min(dp[a - c] + 1) for each coin c
Climbing Stairs    | dp[n] = dp[n-1] + dp[n-2]  (same as Fibonacci!)
LCS                | dp[i][j] = dp[i-1][j-1]+1 if match, else max(dp[i-1][j], dp[i][j-1])
Knapsack           | dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt]+val) if wt<=w
"""
```

---

### Checklist Before Submitting

- [ ] `fib_memo` and `fib_tab` return correct results and agree with each other.
- [ ] `fib_memo(50)` completes instantly (proves memoization is working).
- [ ] `coin_change` returns `-1` when the amount is impossible, and `0` for amount=0.
- [ ] `coin_change([10,6,1], 12)` returns `2` (demonstrating DP beats greedy).
- [ ] `climb_stairs` matches the Fibonacci sequence (offset by 1).
- [ ] `lcs` returns correct lengths for all test cases.
- [ ] `lcs_sequence` returns a valid common subsequence string.
- [ ] `knapsack` returns the correct maximum value.
- [ ] `knapsack_items` returns indices that, when selected, achieve the maximum value.
- [ ] Performance comparison is present and includes a comment.
- [ ] DP summary docstring is present at the top of the file.
