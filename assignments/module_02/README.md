# Week 2 — Python Basics II

This week you move from storing values to **controlling the flow** of your program. You will decide what code runs (conditionals), repeat code automatically (loops), validate user input, and use `break` and `continue` to fine-tune loop behavior.

---

## Concepts Covered

### 1. Conditionals (`if` / `elif` / `else`)

A conditional runs a block of code only when a condition is `True`.

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Below C")
```

- **Indentation is required.** Python uses 4 spaces (or 1 tab) to define a block. Everything indented under an `if` only runs when that condition is met.
- `elif` means "else if" — you can have as many as you need.
- `else` is the catch-all that runs when no earlier condition matched.

---

### 2. Comparison Operators

These return `True` or `False` and are the building blocks of conditions:

| Operator | Meaning                  | Example          |
|----------|--------------------------|------------------|
| `==`     | Equal to                 | `5 == 5` → True  |
| `!=`     | Not equal to             | `5 != 3` → True  |
| `>`      | Greater than             | `7 > 3` → True   |
| `<`      | Less than                | `2 < 9` → True   |
| `>=`     | Greater than or equal to | `5 >= 5` → True  |
| `<=`     | Less than or equal to    | `4 <= 6` → True  |

> **Common mistake:** Using `=` (assignment) inside an `if` instead of `==` (comparison). `if x = 5:` is a `SyntaxError`.

---

### 3. Logical Operators

Combine multiple conditions:

| Operator | Meaning                            | Example                         |
|----------|------------------------------------|----------------------------------|
| `and`    | Both must be True                  | `age >= 18 and has_id == True`  |
| `or`     | At least one must be True          | `day == "Sat" or day == "Sun"`  |
| `not`    | Reverses True/False                | `not is_raining`                |

```python
temp = 75
is_sunny = True

if temp > 70 and is_sunny:
    print("Great day for a walk!")
```

---

### 4. `for` Loops

A `for` loop repeats code a fixed number of times or over every item in a sequence.

```python
# Count from 0 to 4
for i in range(5):
    print(i)

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

`range(start, stop, step)` generates a sequence of integers:
- `range(5)` → 0, 1, 2, 3, 4
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8

---

### 5. `while` Loops

A `while` loop keeps running as long as its condition remains `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1   # Don't forget to update the variable!
```

> **Danger — infinite loop:** If the condition never becomes `False`, the loop runs forever. Always make sure something inside the loop will eventually make the condition False, or use `break`.

---

### 6. Input Validation

Ask the user to re-enter data until they provide something valid:

```python
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Invalid age. Please try again.")
    age = int(input("Enter your age: "))
print(f"Your age is {age}.")
```

---

### 7. `break` and `continue`

`break` immediately **exits** the loop, no matter what:

```python
for i in range(10):
    if i == 5:
        break        # Stop the loop at 5
    print(i)         # Prints 0, 1, 2, 3, 4
```

`continue` **skips the rest of the current iteration** and jumps to the next one:

```python
for i in range(10):
    if i % 2 == 0:
        continue     # Skip even numbers
    print(i)         # Prints 1, 3, 5, 7, 9
```

---

## Hints for This Week's Assignment

- **Trace through your logic manually.** Before running the code, walk through it with a specific value and predict what each line will do.
- **Test boundary values.** If your condition is `>= 18`, test with 17, 18, and 19.
- **Avoid deeply nested `if` statements.** If you find yourself indenting 4+ levels, step back and think about whether `elif` or a different structure would be cleaner.
- For input validation loops, remember that the code inside the loop runs **after** the first attempt, so you often need to get the input once before the loop and again inside the loop — or use a `while True:` loop with a `break`.
- `break` and `continue` are powerful but can make code hard to follow — use them only when they make the logic clearer.
