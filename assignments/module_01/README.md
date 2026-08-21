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

---

## Assignment Instructions

**File to create:** `module_01/basics.py`

You will write a program that collects information about a person and prints a formatted summary. Follow the numbered steps below exactly — each step builds on the one before it.

### Step 1 — Collect the user's name

Use `input()` to ask the user to type their name. Store it in a variable called `name`.

```
What is your name? Alex
```

Run your file (`python3 basics.py`) and make sure you see the prompt.

---

### Step 2 — Collect the user's age

Ask the user to type their age. Remember: `input()` always gives you a string. Convert it to an **integer** using `int()` and store it in a variable called `age`.

```
How old are you? 20
```

> If you forget `int()` and try to do math with `age` later, Python will raise a `TypeError`. Test this on purpose so you understand the error.

---

### Step 3 — Collect the user's GPA

Ask the user for their GPA. Convert it to a **float** and store it in `gpa`.

```
What is your GPA? 3.75
```

---

### Step 4 — Calculate the year they were born

Use the current year (2026) minus their age to estimate their birth year. Store the result in a variable called `birth_year`.

```python
birth_year = 2026 - age
```

---

### Step 5 — Print a formatted summary

Use an **f-string** to print all the information on one or more lines. Your output should look exactly like this (with the user's actual values filled in):

```
--- Student Profile ---
Name: Alex
Age: 20
Approximate birth year: 2006
GPA: 3.75
```

Requirements:
- The header `--- Student Profile ---` must appear on its own line.
- GPA must be printed with **exactly 2 decimal places** (use `:.2f` in your f-string).

---

### Step 6 — Add a letter-grade label

After the profile, print a one-line message that describes the GPA in plain English:

- GPA 3.5 and above → `"GPA status: Excellent"`
- GPA 3.0 to 3.49 → `"GPA status: Good"`
- GPA 2.0 to 2.99 → `"GPA status: Satisfactory"`
- Below 2.0 → `"GPA status: Needs improvement"`

Use an `if / elif / else` statement (we will cover these formally next week, but give it a try using the concept section above as a guide).

---

### Checklist Before Submitting

- [ ] The program runs without errors from start to finish.
- [ ] `input()` is used for name, age, and GPA.
- [ ] Age is stored as an `int`; GPA is stored as a `float`.
- [ ] Birth year is calculated correctly.
- [ ] The output matches the expected format (header, all four fields, GPA status).
- [ ] GPA is printed to 2 decimal places.
- [ ] You tested with at least two different sets of inputs.
