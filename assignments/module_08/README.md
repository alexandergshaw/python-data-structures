# Week 8 — Recursion

Recursion is a technique where a function **calls itself** to solve a smaller version of the same problem. It feels magical at first, but it follows simple rules. Master those rules and recursion becomes one of the most elegant tools in your toolkit.

---

## Concepts Covered

### 1. The Two Essential Parts of Every Recursive Function

Every recursive function must have:

1. **Base case** — a condition that stops the recursion and returns a result directly (no more self-calls).
2. **Recursive case** — the function calls itself with a *smaller* or *simpler* input, moving toward the base case.

If you forget the base case, the function calls itself forever until Python raises a `RecursionError` (stack overflow).

---

### 2. The Call Stack

When a function calls itself, Python does not overwrite the current function — it creates a **new call frame** on the call stack. Each call gets its own copy of all local variables.

```
factorial(4)
  → factorial(3)
      → factorial(2)
          → factorial(1)   # base case: returns 1
        ← 2 * 1 = 2
      ← 3 * 2 = 6
    ← 4 * 6 = 24
```

Results bubble back up through the stack once the base case is reached.

---

### 3. Factorial

`n! = n × (n-1) × (n-2) × ... × 1`, and `0! = 1`.

```python
def factorial(n):
    if n == 0:          # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

print(factorial(5))  # 120
```

Notice: the problem gets smaller each call (`n - 1`), and eventually reaches the base case (`n == 0`).

---

### 4. Fibonacci

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...  
Each number is the sum of the two before it.

```python
def fibonacci(n):
    if n <= 1:                           # Base cases
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # Recursive case

print(fibonacci(7))  # 13
```

> **Warning:** This naive version is very slow for large `n` because it recalculates the same values repeatedly. (You'll fix this in Week 15 with memoization.)

---

### 5. Recursive List Sum

```python
def list_sum(numbers):
    if len(numbers) == 0:   # Base case: empty list sums to 0
        return 0
    return numbers[0] + list_sum(numbers[1:])   # First item + sum of rest
```

`numbers[1:]` is a slice — it returns all items except the first, making the list one item shorter each call.

---

### 6. String Reversal

```python
def reverse(s):
    if len(s) <= 1:         # Base case: empty or single-char string
        return s
    return reverse(s[1:]) + s[0]   # Reverse rest + add first char at end

print(reverse("hello"))  # "olleh"
```

---

### 7. Exponentiation

```python
def power(base, exp):
    if exp == 0:            # Base case: anything to the power 0 is 1
        return 1
    return base * power(base, exp - 1)

print(power(2, 10))  # 1024
```

---

## How to Approach Any Recursive Problem

Follow this three-step process:

1. **Identify the base case.** What is the simplest possible input? What does it return directly?
2. **Identify the recursive case.** How can you express the answer in terms of a *smaller* version of the same problem?
3. **Trust the recursion.** Assume the recursive call works correctly for the smaller input — your job is just to combine its result with the current step.

---

## Hints for This Week's Assignment

- **Always define the base case first.** Write the `if` for the base case before writing the recursive call. This forces you to think about when to stop.
- If you get a `RecursionError: maximum recursion depth exceeded`, your base case is missing or never being reached.
- **Print the argument** at the top of the function to trace what's happening: `print(f"Called with n={n}")`. Remove it when you're done.
- Recursive functions look like they do nothing useful — until the base case is hit and results start flowing back. Trust the process!
- Don't use a loop *inside* a recursive function — if you need a loop, it's a sign you haven't broken the problem down recursively yet.
- For list problems, `list[1:]` (all but the first) or `list[:-1]` (all but the last) are your best friends for reducing the problem size.

---

## Assignment Instructions

**File to create:** `module_08/recursion.py`

You will implement six recursive functions and one recursive problem of your choosing. **You may not use any loops (`for`, `while`) inside any of these functions** — recursion only.

---

### Step 1 — `factorial(n)`

Return `n!` (n factorial). Recall: `0! = 1`, `1! = 1`, `5! = 120`.

```python
print(factorial(0))   # 1
print(factorial(5))   # 120
print(factorial(10))  # 3628800
```

---

### Step 2 — `fibonacci(n)`

Return the nth Fibonacci number (0-indexed). Recall: 0, 1, 1, 2, 3, 5, 8, 13, 21 …

```python
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(7))   # 13
print(fibonacci(10))  # 55
```

---

### Step 3 — `recursive_sum(numbers)`

Return the sum of all numbers in a list using recursion.

```python
print(recursive_sum([]))           # 0
print(recursive_sum([5]))          # 5
print(recursive_sum([1, 2, 3, 4])) # 10
```

**Hint:** The sum of a list is the first element plus the sum of the rest.

---

### Step 4 — `reverse_string(s)`

Return the string `s` reversed, using recursion.

```python
print(reverse_string(""))        # ""
print(reverse_string("a"))       # "a"
print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```

**Hint:** The reverse of a string is the last character followed by the reverse of everything before it. Or: reverse of `s` = reverse of `s[1:]` + `s[0]`.

---

### Step 5 — `power(base, exp)`

Return `base` raised to the power `exp`. Assume `exp >= 0`.

```python
print(power(2, 0))    # 1
print(power(2, 10))   # 1024
print(power(3, 4))    # 81
```

---

### Step 6 — `count_occurrences(lst, target)`

Return how many times `target` appears in `lst`, using recursion.

```python
print(count_occurrences([], 5))                    # 0
print(count_occurrences([1, 2, 3, 2, 2], 2))       # 3
print(count_occurrences(["a", "b", "a"], "a"))     # 2
```

**Hint:** Check the first element; if it matches, return `1 + recurse on the rest`; otherwise return `0 + recurse on the rest`.

---

### Step 7 — `flatten(nested)`

Given a list that may contain integers or other lists (nested arbitrarily deep), return a single flat list of all integers.

```python
print(flatten([1, [2, 3], [4, [5, 6]]]))   # [1, 2, 3, 4, 5, 6]
print(flatten([]))                          # []
print(flatten([1, [2, [3, [4]]]]))          # [1, 2, 3, 4]
```

**Hint:** For each element in the list — if it's a list, recursively flatten it; if it's not, wrap it in `[element]`. Concatenate all results.

---

### Step 8 — Call trace comment

Pick **one** of your functions and add a detailed comment block above it showing the full call trace for a small example. For example, for `factorial(4)`:

```python
# factorial(4)
#   → 4 * factorial(3)
#       → 3 * factorial(2)
#           → 2 * factorial(1)
#               → 1 * factorial(0)
#                   → 1          (base case)
#               ← 1 * 1 = 1
#           ← 2 * 1 = 2
#       ← 3 * 2 = 6
#   ← 4 * 6 = 24
```

---

### Checklist Before Submitting

- [ ] All six functions are implemented with **no loops** inside them.
- [ ] `factorial(0)` returns `1`.
- [ ] `fibonacci(0)` returns `0` and `fibonacci(1)` returns `1`.
- [ ] `recursive_sum([])` returns `0` (empty list base case).
- [ ] `reverse_string("")` returns `""`.
- [ ] `power(n, 0)` returns `1` for any `n`.
- [ ] `flatten` handles arbitrarily nested lists.
- [ ] A call trace comment is present above at least one function.
- [ ] All test calls shown above are included at the bottom of the file and produce the expected output.
