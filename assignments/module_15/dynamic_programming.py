"""
Dynamic Programming Cheat Sheet
Use DP for overlapping sub-problems and optimal substructure.
Memoization caches recursive results; tabulation fills results bottom-up.
Fibonacci/stairs: dp[n] = dp[n-1] + dp[n-2]
Coin change: dp[a] = min(dp[a-c] + 1); LCS matches diagonally or takes max(skip).
Knapsack: choose the greater of skipping or taking each fitting item.
"""

import time


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n):
    if n <= 1:
        return n
    table = [0, 1]
    for _ in range(2, n + 1):
        table.append(table[-1] + table[-2])
    return table[n]


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


def climb_stairs(n):
    # Each step comes from n-1 or n-2, the same recurrence as Fibonacci.
    if n <= 2:
        return n
    one, two = 1, 2
    for _ in range(3, n + 1):
        one, two = two, one + two
    return two


def _lcs_table(s1, s2):
    table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i, char1 in enumerate(s1, 1):
        for j, char2 in enumerate(s2, 1):
            table[i][j] = (table[i - 1][j - 1] + 1 if char1 == char2
                           else max(table[i - 1][j], table[i][j - 1]))
    return table


def lcs(s1, s2):
    return _lcs_table(s1, s2)[len(s1)][len(s2)]


def lcs_sequence(s1, s2):
    table = _lcs_table(s1, s2)
    i, j, result = len(s1), len(s2), []
    while i and j:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i, j = i - 1, j - 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(result))


def knapsack(weights, values, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    for i, (weight, value) in enumerate(zip(weights, values), 1):
        for limit in range(capacity + 1):
            dp[i][limit] = dp[i - 1][limit]
            if weight <= limit:
                dp[i][limit] = max(dp[i][limit], dp[i - 1][limit - weight] + value)
    return dp[-1][-1]


def benchmark():
    start = time.time()
    for _ in range(1000):
        fib_memo(35)
    print(f"Memo: {time.time() - start:.4f}s")
    start = time.time()
    for _ in range(1000):
        fib_tab(35)
    print(f"Tab:  {time.time() - start:.4f}s")
    # Tabulation is generally faster here because it avoids recursive call overhead.


if __name__ == "__main__":
    benchmark()
