# Week 1 — Python Basics I

Welcome to your first week of Python! This module covers the fundamental building blocks every Python program is made of. By the end of the week you will be able to write programs that receive input from a user, perform calculations, and display formatted results.

---

## Concepts Covered

### 1. Environment Setup

Before writing any code you need a place to run it. In this course you will use **GitHub Codespaces** — a full Python environment that runs in your browser. No installation required.

- Open your Codespace from the `<> Code → Codespaces` menu on GitHub.
- Python 3 is already installed. You can verify this by typing `python3 --version` in the terminal.
- To run a Python file called `hello.py`, type `python3 hello.py` in the terminal and press Enter.

---

### 2. Variables

A **variable** is a named container that holds a value. You create one with the assignment operator `=`.

```python
name = "Alex"
age = 20
gpa = 3.75
is_enrolled = True
```

- Variable names should be lowercase with underscores (`student_name`, not `StudentName`).
- You can reassign a variable at any time — the old value is simply replaced.

---

### 3. Primitive Data Types

Python has four core (primitive) types:

| Type    | Example         | Description                          |
|---------|-----------------|--------------------------------------|
| `int`   | `42`, `-7`      | Whole numbers                        |
| `float` | `3.14`, `-0.5`  | Decimal numbers                      |
| `str`   | `"hello"`       | Text, wrapped in quotes              |
| `bool`  | `True`, `False` | Logical true/false (capital T and F) |

Check a variable's type with `type()`:

```python
x = 10
print(type(x))   # <class 'int'>
```

---

### 4. Operators

**Arithmetic operators** perform math:

```python
5 + 3    # 8  — addition
5 - 3    # 2  — subtraction
5 * 3    # 15 — multiplication
5 / 3    # 1.666... — division (always returns float)
5 // 3   # 1  — floor division (drops remainder)
5 % 3    # 2  — modulo (remainder only)
5 ** 3   # 125 — exponentiation (5 to the power of 3)
```

**Assignment shorthand** updates a variable in place:

```python
score = 10
score += 5   # same as: score = score + 5  →  15
score -= 2   # 13
score *= 2   # 26
```

---

### 5. Input and Output

`print()` displays text or values to the screen:

```python
print("Hello, world!")
print(42)
print(3.14)
```

`input()` pauses the program and waits for the user to type something. It **always returns a string**, so convert it when you need a number:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))    # convert to int
height = float(input("Your height (m)? "))  # convert to float
```

> **Common mistake:** Forgetting to convert `input()` to a number before doing math on it will raise a `TypeError`.

---

### 6. f-Strings (Formatted String Literals)

f-strings let you embed variable values directly inside a string. Prefix the string with `f` and wrap variable names in `{}`:

```python
name = "Alex"
age = 20
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alex and I am 20 years old.
```

You can put expressions inside the braces too:

```python
a = 7
b = 3
print(f"{a} divided by {b} is {a / b:.2f}")
# Output: 7 divided by 3 is 2.33
```

The `:.2f` format specifier rounds to 2 decimal places.

---

## Hints for This Week's Assignment

- **Start small.** Get the input working first, then add the calculation, then format the output.
- **Print often.** Add `print()` statements to check your variables as you go — delete them when you're done.
- **Read error messages.** Python tells you the line number and what went wrong. `TypeError` usually means a type mismatch; `NameError` means you used a variable before creating it.
- **Test with different inputs.** Try zero, negative numbers, and very large numbers to make sure your program handles them.
- Remember: `input()` returns a **string**. If your program does math, you must wrap it in `int()` or `float()`.
