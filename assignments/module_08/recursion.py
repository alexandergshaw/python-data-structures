def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# factorial(3) -> 3 * factorial(2) -> 3 * 2 * factorial(1)
# -> 3 * 2 * 1 * factorial(0) -> 3 * 2 * 1 * 1 = 6
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def recursive_sum(numbers):
    return 0 if not numbers else numbers[0] + recursive_sum(numbers[1:])


def reverse_string(text):
    return text if len(text) <= 1 else reverse_string(text[1:]) + text[0]


def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp - 1)


def count_occurrences(lst, target):
    if not lst:
        return 0
    return (lst[0] == target) + count_occurrences(lst[1:], target)


def flatten(nested):
    if not nested:
        return []
    first = nested[0]
    return (flatten(first) if isinstance(first, list) else [first]) + flatten(nested[1:])


if __name__ == "__main__":
    print(factorial(0), factorial(1), factorial(5), factorial(10))
    print(fibonacci(0), fibonacci(1), fibonacci(7), fibonacci(10))
    print(recursive_sum([]), recursive_sum([5]), recursive_sum([1, 2, 3, 4]))
    print(reverse_string(""), reverse_string("a"), reverse_string("hello"), reverse_string("Python"))
    print(power(2, 0), power(2, 10), power(3, 4), power(5, 3))
    print(count_occurrences([], 5), count_occurrences([1, 2, 3, 2, 2], 2))
    print(count_occurrences(["a", "b", "a"], "a"), count_occurrences([1, 2, 3], 9))
    print(flatten([1, [2, 3], [4, [5, 6]]]), flatten([]))
    print(flatten([1, [2, [3, [4]]]]), flatten([5]))
