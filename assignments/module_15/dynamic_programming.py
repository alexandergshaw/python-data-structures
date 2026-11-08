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
    pass


def fib_tab(n):
    pass


def coin_change(coins, amount):
    pass


def climb_stairs(n):
    pass


def _lcs_table(s1, s2):
    pass


def lcs(s1, s2):
    pass


def lcs_sequence(s1, s2):
    pass


def knapsack(weights, values, capacity):
    pass


def benchmark():
    pass


if __name__ == "__main__":
    benchmark()
