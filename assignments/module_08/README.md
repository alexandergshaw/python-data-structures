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
