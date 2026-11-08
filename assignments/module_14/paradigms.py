"""
Algorithmic Paradigm Cheat Sheet
GREEDY: choose the local best; works for activity selection, fails for unusual coin systems.
DIVIDE AND CONQUER: split, solve independent parts, combine.
DYNAMIC PROGRAMMING: cache overlapping subproblems with optimal substructure.
"""


def activity_selection(activities):
    selected = []
    for start, end in sorted(activities, key=lambda activity: activity[1]):
        if not selected or start >= selected[-1][1]:
            selected.append((start, end))
    return selected


def coin_change_greedy(coins, amount):
    result = []
    for coin in coins:
        while coin <= amount:
            result.append(coin)
            amount -= coin
    return result if amount == 0 else []


def max_subarray_kadane(nums):
    if not nums:
        return 0
    current = best = nums[0]
    for value in nums[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best


def max_subarray_indices(nums):
    if not nums:
        return 0, -1, -1
    current = best = nums[0]
    current_start = best_start = best_end = 0
    for index, value in enumerate(nums[1:], 1):
        if value > current + value:
            current, current_start = value, index
        else:
            current += value
        if current > best:
            best, best_start, best_end = current, current_start, index
    return best, best_start, best_end


def schedule_classes(requests):
    selected = []
    for start, end, name in sorted(
            ((start, end, name) for name, start, end in requests), key=lambda item: item[1]):
        if not selected or start >= selected[-1][1]:
            selected.append((start, end, name))
    print(f"Selected {len(selected)} classes:")
    for start, end, name in selected:
        print(f"  {name:<7}: {start}:00 - {end}:00")
    return selected


if __name__ == "__main__":
    result = coin_change_greedy([10, 6, 1], 12)
    print(result)
    # Greedy fails because choosing 10 prevents the optimal 6 + 6; DP finds two coins.
    schedule_classes([("Alice", 9, 10), ("Bob", 9, 11), ("Carol", 10, 11),
                      ("David", 11, 13), ("Eve", 12, 14), ("Frank", 13, 15)])
