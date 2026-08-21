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
