# Week 8 — Recursion
### Base Cases, Recursive Cases, the Call Stack, and Classic Problems

---

## Welcome!

Recursion is one of those ideas that feels impossible at first and then clicks all at once. Be patient with yourself this week. Read slowly, try the examples yourself, and trust the process.

---

## Concept 1: What Is Recursion?

**Recursion** is when a function calls *itself* as part of solving a problem.

**Analogy:** Have you ever stood between two mirrors facing each other? Each mirror reflects a reflection of a reflection of a reflection — and so on. That's recursion visually.

A more practical analogy: Russian nesting dolls (Matryoshka). You open the big doll, find a smaller one. Open that, find an even smaller one. You keep going until you reach the tiniest doll that doesn't open. That tiny doll is the **base case** — the thing that stops the recursion.

---

## Concept 2: The Two Rules — Every Recursive Function Has Both

### Rule 1: Base Case — Know When to Stop

The **base case** is the situation where the function does NOT call itself. It just returns an answer directly. Without a base case, the function would call itself forever (causing a `RecursionError`).

### Rule 2: Recursive Case — Make the Problem Smaller

The **recursive case** is where the function calls itself with a *smaller or simpler* version of the problem. Each call must get closer to the base case.

---

## Concept 3: Factorial — The Hello World of Recursion

Factorial: `5! = 5 × 4 × 3 × 2 × 1 = 120`

Notice: `5! = 5 × 4!` — the answer to the big problem contains the answer to a smaller version of the same problem. That's the heart of recursion.

```python
def factorial(n):
    if n == 0:               # BASE CASE — stop here
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE — smaller problem
```

Tracing `factorial(4)`:
```
factorial(4)
  = 4 * factorial(3)
  = 4 * 3 * factorial(2)
  = 4 * 3 * 2 * factorial(1)
  = 4 * 3 * 2 * 1 * factorial(0)
  = 4 * 3 * 2 * 1 * 1        ← base case returns 1
  = 4 * 3 * 2 * 1
  = 4 * 3 * 2
  = 4 * 6
  = 24
```

The answers "bubble back up" once the base case is reached.

---

## Concept 4: The Call Stack

When a function calls itself, Python doesn't forget where it was. It keeps a **stack** (literally — from last week!) of all the places it needs to come back to.

**Analogy:** You're reading a book and see a footnote. You jump to the footnote (the recursive call), and you put a bookmark on the original page. The footnote has another footnote — you bookmark that page too, and jump again. Eventually you reach a footnote with no more references. You read it and then follow your bookmarks back to where you started.

Python has a limit on how deep this can go (about 1000 levels). If your recursion goes deeper than that — usually because the base case is missing — you get:
```
RecursionError: maximum recursion depth exceeded
```

---

## Concept 5: Fibonacci

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Each number is the sum of the two before it: `fib(n) = fib(n-1) + fib(n-2)`

```python
def fibonacci(n):
    if n <= 1:                           # BASE CASE — two bases!
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # RECURSIVE CASE
```

`fibonacci(0)` = 0, `fibonacci(1)` = 1, `fibonacci(2)` = 1, `fibonacci(7)` = 13

⚠️ This version is very slow for large `n` because it recalculates the same subproblems over and over. You'll fix this in Week 15 with a technique called memoization.

---

## Concept 6: Recursive List Sum

**Problem:** Add up all numbers in a list using recursion (no loops allowed).

**Insight:** The sum of `[1, 2, 3, 4]` is `1 + sum of [2, 3, 4]`. The problem gets one item smaller each time.

```python
def recursive_sum(numbers):
    if len(numbers) == 0:   # BASE CASE — empty list sums to 0
        return 0
    return numbers[0] + recursive_sum(numbers[1:])
    # numbers[1:] is "all items except the first" — one item smaller
```

---

## Concept 7: String Reversal

**Problem:** Reverse a string using recursion.

**Insight:** The reverse of `"hello"` is the reverse of `"ello"` plus `"h"` at the end.

```python
def reverse_string(s):
    if len(s) <= 1:           # BASE CASE — empty or single character
        return s
    return reverse_string(s[1:]) + s[0]
```

---

## Concept 8: Exponentiation

**Problem:** Calculate `base` raised to the power `exp`.

**Insight:** `2^10 = 2 × 2^9`. The exponent shrinks by 1 each time.

```python
def power(base, exp):
    if exp == 0:              # BASE CASE — anything^0 = 1
        return 1
    return base * power(base, exp - 1)
```

---

## How to Approach Any Recursive Problem (Three Steps)

1. **Identify the base case.** What is the *simplest possible input* that has an obvious answer?
2. **Identify the recursive case.** How does the answer to the big problem depend on the answer to a *smaller* version?
3. **Trust the recursion.** Assume the recursive call works perfectly for the smaller input. Your only job is to combine it with the current step.

This third step is where most students get stuck. You don't need to trace every level — just trust that it works for the smaller case, the same way it worked for the previous cases.

---

## Assignment Instructions

**File to create:** `module_08/recursion.py`

**Rule: No loops (`for`, `while`) inside any of these functions.** Recursion only.

---

### Step 1 — `factorial(n)`

Return `n!`. Base case: `factorial(0) = 1`.

```python
print(factorial(0))    # 1
print(factorial(1))    # 1
print(factorial(5))    # 120
print(factorial(10))   # 3628800
```

---

### Step 2 — `fibonacci(n)`

Return the nth Fibonacci number (0-indexed). Two base cases: `fib(0) = 0`, `fib(1) = 1`.

```python
print(fibonacci(0))    # 0
print(fibonacci(1))    # 1
print(fibonacci(7))    # 13
print(fibonacci(10))   # 55
```

---

### Step 3 — `recursive_sum(numbers)`

Return the sum of all numbers in a list. Base case: empty list → return 0.

```python
print(recursive_sum([]))             # 0
print(recursive_sum([5]))            # 5
print(recursive_sum([1, 2, 3, 4]))   # 10
print(recursive_sum([10, -3, 7]))    # 14
```

---

### Step 4 — `reverse_string(s)`

Return the string reversed. Base case: empty string or single character → return as-is.

```python
print(reverse_string(""))         # ""
print(reverse_string("a"))        # "a"
print(reverse_string("hello"))    # "olleh"
print(reverse_string("Python"))   # "nohtyP"
```

---

### Step 5 — `power(base, exp)`

Return `base` to the power of `exp`. Base case: `exp == 0` → return 1. Assume `exp >= 0`.

```python
print(power(2, 0))     # 1
print(power(2, 10))    # 1024
print(power(3, 4))     # 81
print(power(5, 3))     # 125
```

---

### Step 6 — `count_occurrences(lst, target)`

Return how many times `target` appears in `lst`. Use recursion.

```python
print(count_occurrences([], 5))                  # 0
print(count_occurrences([1, 2, 3, 2, 2], 2))     # 3
print(count_occurrences(["a", "b", "a"], "a"))   # 2
print(count_occurrences([1, 2, 3], 9))           # 0
```

Hint: check the first item. If it matches, `return 1 + count_occurrences(lst[1:], target)`. If not, `return 0 + count_occurrences(lst[1:], target)`.

---

### Step 7 — `flatten(nested)`

Given a list that may contain both integers and other lists (nested to any depth), return a single flat list of all integers.

```python
print(flatten([1, [2, 3], [4, [5, 6]]]))    # [1, 2, 3, 4, 5, 6]
print(flatten([]))                           # []
print(flatten([1, [2, [3, [4]]]]))           # [1, 2, 3, 4]
print(flatten([5]))                          # [5]
```

Hint: For each element — if it's a list, recursively flatten it. If it's not, put it in `[element]`. Concatenate all results.

---

### Step 8 — Add a call trace comment

Pick any one of your functions and add a comment showing the full call trace for a small input. This forces you to actually understand the recursion. Example for `factorial(4)`:

```python
# factorial(4)
#   → 4 * factorial(3)
#       → 3 * factorial(2)
#           → 2 * factorial(1)
#               → 1 * factorial(0)
#                   → returns 1   (base case)
#               ← 1 * 1 = 1
#           ← 2 * 1 = 2
#       ← 3 * 2 = 6
#   ← 4 * 6 = 24
```

---

### Checklist Before Submitting

- [ ] No loops inside any function — recursion only
- [ ] `factorial(0)` returns 1
- [ ] `fibonacci(0)` returns 0 and `fibonacci(1)` returns 1
- [ ] `recursive_sum([])` returns 0 without crashing
- [ ] `reverse_string("")` returns `""`
- [ ] `power(n, 0)` returns 1 for any n
- [ ] `count_occurrences([], anything)` returns 0
- [ ] `flatten` handles arbitrarily deep nesting
- [ ] A call trace comment exists above at least one function
- [ ] All test calls shown above are present and produce correct output
