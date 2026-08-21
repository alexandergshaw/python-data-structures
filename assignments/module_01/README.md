# Week 1 — Python Basics I
### Variables, Data Types, Math, Input, Output, and f-Strings

---

## Welcome!

You are writing your first real Python programs this week. Don't worry if you've never programmed before — that's exactly what this course is for. Every concept below is explained from scratch with everyday examples. Read through the whole thing before you start coding.

---

## What Even Is Python?

Think of Python as a language you use to give instructions to your computer — the same way a recipe gives instructions to a chef. The chef (your computer) will follow your instructions exactly, in order, one step at a time. If you write something unclear, the chef gets confused and tells you where the problem is. That error message is your friend, not your enemy.

---

## Concept 1: Variables

A **variable** is just a labeled box where you store information.

Imagine sticky notes on a whiteboard:

```
[ name  ] → "Alex"
[ age   ] → 20
[ score ] → 95.5
```

In Python, you create a variable by writing its name, an equals sign, and the value you want to store:

```python
name = "Alex"
age = 20
score = 95.5
```

That's it. Now whenever you write `name` in your program, Python knows you mean `"Alex"`.

**Rules for naming variables:**
- Use lowercase letters and underscores: `student_name`, not `StudentName`
- No spaces: `first name` is not allowed; use `first_name`
- Names can't start with a number: `1score` is wrong; `score1` is fine

---

## Concept 2: Data Types

Not all information is the same kind of thing. Python tracks what *type* of thing is stored in each variable. The four basic types are:

| Type | What it holds | Example |
|------|---------------|---------|
| `int` | Whole numbers | `42`, `-7`, `0` |
| `float` | Numbers with decimals | `3.14`, `-0.5`, `100.0` |
| `str` | Text (short for "string") | `"hello"`, `"Alex"`, `"42"` |
| `bool` | True or false — that's it | `True`, `False` |

**Analogy:** Think of data types like containers. An egg carton holds eggs (`int`), a measuring cup holds liquids (`float`), a notepad holds text (`str`), and a light switch is either on or off (`bool`).

Notice that `"42"` (with quotes) is *text*, not a number. You can't do math with text, even if the text looks like a number.

You can check what type a variable is with `type()`:

```python
x = 10
print(type(x))   # <class 'int'>

y = "hello"
print(type(y))   # <class 'str'>
```

---

## Concept 3: Math Operators

Python can do math just like a calculator:

```python
10 + 3    # 13  — addition
10 - 3    # 7   — subtraction
10 * 3    # 30  — multiplication
10 / 3    # 3.333...  — regular division (always gives a decimal)
10 // 3   # 3   — floor division (throws away the remainder, like integer division)
10 % 3    # 1   — modulo (gives you ONLY the remainder)
10 ** 3   # 1000 — exponent (10 to the power of 3)
```

**Analogy for `%` (modulo):** If you have 10 apples and 3 friends, each friend gets 3 apples (10 // 3 = 3) and you have **1 left over** (10 % 3 = 1). The `%` operator gives you that leftover.

**Shortcut operators** — updating a variable using its own value:

```python
score = 10
score += 5    # same as: score = score + 5  → now score is 15
score -= 2    # now score is 13
score *= 2    # now score is 26
```

---

## Concept 4: Getting Input from the User

`input()` pauses your program, shows a message, and waits for the user to type something and press Enter.

```python
name = input("What is your name? ")
```

**Critical rule:** `input()` ALWAYS gives you back a string — even if the user types a number.

```python
age = input("How old are you? ")
# age is "20" (the text "20"), NOT the number 20
```

If you need to do math with the user's answer, you must convert it:

```python
age = int(input("How old are you? "))       # Convert to whole number
height = float(input("Your height in m? ")) # Convert to decimal number
```

**Analogy:** `input()` is like your program asking a question out loud. The answer always comes back written on a piece of paper (a string). If you need to do math with it, you have to read the paper and convert the words to a number in your head first.

---

## Concept 5: Displaying Output

`print()` shows information on the screen:

```python
print("Hello, world!")   # Shows text
print(42)                # Shows a number
print(3.14 + 1)          # Shows the result of math: 4.140...
```

You can print multiple things by separating them with commas:

```python
name = "Alex"
age = 20
print("Name:", name, "Age:", age)
# Name: Alex Age: 20
```

---

## Concept 6: f-Strings (The Cool Way to Print)

An **f-string** lets you mix variables and text together cleanly. Put an `f` before the opening quote, then wrap any variable name in curly braces `{}`:

```python
name = "Alex"
age = 20
print(f"My name is {name} and I am {age} years old.")
# My name is Alex and I am 20 years old.
```

You can even do math inside the curly braces:

```python
price = 9.99
quantity = 3
print(f"Total: ${price * quantity:.2f}")
# Total: $29.97
```

The `:.2f` at the end of `price * quantity` means "show this as a decimal with exactly 2 places." Like a cash register receipt.

**Analogy:** An f-string is like a fill-in-the-blank sentence. You write the sentence with blank spaces `{}` and Python automatically fills in the right values.

---

## Common Beginner Mistakes (Read These Carefully!)

| Mistake | What happens | Fix |
|--------|--------------|-----|
| `age = input(...)` then `age + 1` | `TypeError` — can't add a string and a number | Wrap input in `int()` |
| Using `=` to compare (`if x = 5`) | `SyntaxError` | Use `==` to compare |
| Forgetting quotes around text (`name = Alex`) | `NameError` — Python thinks `Alex` is a variable | `name = "Alex"` |
| Mixing types (`"hello" + 5`) | `TypeError` | Convert: `"hello" + str(5)` |

---

## Assignment Instructions

**File to create:** `module_01/basics.py`

You are going to write a program that asks a user some questions, does some math, and prints a nicely formatted summary. Follow the steps below — read each one fully before you write the code for it.

---

### Step 1 — Ask for the user's name

Write one line that asks the user to type their name and stores it in a variable called `name`.

When you run the program, you should see:
```
What is your name? 
```
(The cursor should wait for you to type something.)

Test it: run `python3 basics.py`, type your name, and press Enter. Then add a `print(name)` on the next line to verify it was stored. Remove that print when done.

---

### Step 2 — Ask for the user's age

Ask the user how old they are. Store it as an **integer** (whole number) in a variable called `age`.

Remember: wrap `input(...)` in `int(...)` so you get a number, not text.

---

### Step 3 — Ask for the user's GPA

Ask the user for their GPA. Store it as a **float** (decimal number) in a variable called `gpa`.

---

### Step 4 — Calculate their approximate birth year

Using the year 2026 and the `age` variable, calculate what year they were likely born. Store it in a variable called `birth_year`.

This is just one line of subtraction.

---

### Step 5 — Print a formatted profile

Use f-strings to print a summary that looks exactly like this (with real values substituted in):

```
--- Student Profile ---
Name: Alex
Age: 20
Approximate birth year: 2006
GPA: 3.75
```

Requirements:
- Print the `--- Student Profile ---` header first.
- GPA must show **exactly 2 decimal places** (use `:.2f`).

---

### Step 6 — Add a GPA status message

After the profile, print one more line that describes the GPA:

- 3.5 or above → print `GPA status: Excellent`
- 3.0 to 3.49 → print `GPA status: Good`
- 2.0 to 2.99 → print `GPA status: Satisfactory`
- Below 2.0 → print `GPA status: Needs improvement`

Use an `if / elif / else` block. We will cover these in depth next week, but you can look at the pattern and try it now — it reads almost like English:

```python
if gpa >= 3.5:
    print("GPA status: Excellent")
elif gpa >= 3.0:
    print("GPA status: Good")
...
```

---

### Step 7 — Test your program with different inputs

Run your program at least three times with different answers and make sure:
- The math is correct each time
- The GPA prints with 2 decimal places (e.g., `3.50` not `3.5`)
- The GPA status changes when you enter different GPAs

---

### Checklist Before Submitting

- [ ] `input()` is used for name, age, and GPA (all three ask the user)
- [ ] Age is stored as an `int` (wrapped in `int()`)
- [ ] GPA is stored as a `float` (wrapped in `float()`)
- [ ] Birth year is calculated correctly using subtraction
- [ ] The `--- Student Profile ---` header prints first
- [ ] GPA is displayed to exactly 2 decimal places using `:.2f`
- [ ] The GPA status message prints correctly for all four ranges
- [ ] The program runs from top to bottom with no errors
