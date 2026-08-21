# Week 2 — Python Basics II
### Conditionals, Loops, Input Validation, break, and continue

---

## Welcome Back!

Last week your programs ran straight through from top to bottom — one step, then the next, then the next. This week you learn to make decisions (run some code only sometimes) and repeat things automatically (run code many times without copying and pasting). These two ideas — decision-making and repetition — are at the heart of almost every program ever written.

---

## Concept 1: Conditionals (`if` / `elif` / `else`)

An `if` statement is a **fork in the road**. Your program checks a condition, and depending on whether it's true or false, it takes one path or the other.

**Real life analogy:** Imagine you're deciding what to wear.
- *If* it's raining → wear a raincoat
- *Otherwise, if* it's cold → wear a jacket
- *Otherwise* → wear a t-shirt

In Python:

```python
weather = "raining"

if weather == "raining":
    print("Wear a raincoat")
elif weather == "cold":
    print("Wear a jacket")
else:
    print("Wear a t-shirt")
```

**Things to notice:**
- The condition is always followed by a colon `:`
- The code *inside* the if block is **indented** (pushed in with 4 spaces). Python uses indentation to know what's "inside" the block. If you forget the indent, you get an error.
- `elif` means "else if" — it only runs if all previous conditions were false.
- `else` is the fallback — it runs if nothing above matched.

---

## Concept 2: Comparison Operators

These are the tools you use to build conditions. They all produce either `True` or `False`:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Is equal to? | `5 == 5` | `True` |
| `!=` | Is NOT equal to? | `5 != 3` | `True` |
| `>` | Greater than? | `7 > 3` | `True` |
| `<` | Less than? | `2 < 9` | `True` |
| `>=` | Greater than or equal? | `5 >= 5` | `True` |
| `<=` | Less than or equal? | `4 <= 3` | `False` |

⚠️ **The most common beginner mistake:** Using `=` (which *assigns* a value) instead of `==` (which *compares* values).

```python
# WRONG — this tries to assign 5 inside an if, which is an error:
if x = 5:

# CORRECT — this checks whether x equals 5:
if x == 5:
```

---

## Concept 3: Logical Operators (Combining Conditions)

Sometimes you need to check two things at once:

- `and` — BOTH conditions must be true
- `or` — AT LEAST ONE condition must be true
- `not` — flips true to false, and vice versa

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")

if age < 13 or age > 65:
    print("Discounted ticket!")

if not has_ticket:
    print("You need a ticket first.")
```

**Analogy for `and`:** A car needs BOTH the key turned AND the gas pedal pressed to move. One without the other doesn't work.

**Analogy for `or`:** A vending machine accepts coins OR bills. Either one works.

---

## Concept 4: `for` Loops — Repeating a Fixed Number of Times

A `for` loop runs a block of code once for each item in a sequence. Think of it as a checklist — it goes through every item, one at a time.

**Analogy:** You have a shopping list with 5 items. You go through each item on the list, pick it up, and check it off. The `for` loop does the same thing with code.

```python
# Print numbers 0 through 4:
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Go through every item in a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

`range(5)` generates the numbers 0, 1, 2, 3, 4. Think of it as a numbered list of 5 items.

- `range(1, 6)` → 1, 2, 3, 4, 5 (start at 1, stop before 6)
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (start at 0, stop before 10, count by 2s)

---

## Concept 5: `while` Loops — Repeating Until Something Changes

A `while` loop keeps running as long as a condition is true. It checks the condition before each repetition, and stops when the condition becomes false.

**Analogy:** You keep hitting the snooze button on your alarm *while* you're tired. As soon as you feel awake (condition becomes false), you stop hitting snooze.

```python
count = 0
while count < 5:
    print(count)
    count += 1    # This is CRUCIAL — without it, count never changes and you loop forever
```

⚠️ **Danger — the infinite loop:** If the condition in your `while` loop never becomes false, your program runs forever. Always make sure something inside the loop moves you closer to the condition being false.

---

## Concept 6: Input Validation — Demanding Correct Input

This is a classic use of `while` loops: keep asking the user until they give you something valid.

**Analogy:** A hotel check-in desk won't give you a key until you show ID. They keep asking until you produce it.

```python
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("That doesn't look right. Try again.")
    age = int(input("Enter your age: "))

print(f"Got it — you are {age} years old.")
```

---

## Concept 7: `break` — Emergency Exit from a Loop

`break` immediately quits the loop, no matter what. Think of it as a fire exit — you use it when you need to get out right now.

```python
for i in range(10):
    if i == 5:
        break        # Stop the loop immediately
    print(i)
# Prints: 0, 1, 2, 3, 4  (never reaches 5 or beyond)
```

---

## Concept 8: `continue` — Skip This Round

`continue` skips the rest of the current loop iteration and jumps straight to the next one. Think of it as a "skip" button — you skip this item but keep going through the rest of the list.

```python
for i in range(10):
    if i % 2 == 0:
        continue       # Skip even numbers
    print(i)
# Prints: 1, 3, 5, 7, 9  (odd numbers only)
```

---

## Assignment Instructions

**File to create:** `module_02/control_flow.py`

You're going to build a grade-report program. It collects scores from the user, validates them, grades them, and prints stats. Follow each step — don't skip ahead.

---

### Step 1 — Ask how many students there are

Ask the user to enter the number of students. Store it in a variable called `count`.

Validate it: the number must be between 1 and 50. If they enter something outside that range, print an error message and ask again. Keep asking until the number is valid.

```
How many students? -3
Invalid. Enter a number between 1 and 50: 0
Invalid. Enter a number between 1 and 50: 5
```

Use a `while` loop for the validation.

---

### Step 2 — Collect a score for each student

Use a `for` loop that runs exactly `count` times. On each loop, ask the user for that student's score (0–100). Validate each score with an inner `while` loop before accepting it.

```
Enter score for student 1 (0-100): 150
Invalid score. Try again: 85
Enter score for student 2 (0-100): 92
```

Store all valid scores in a list. Start with `scores = []` before the loop, and use `scores.append(score)` inside to add each valid score.

---

### Step 3 — Handle the "skip" case with `continue`

Before accepting a score, check if it equals `-1`. A score of `-1` means the student was absent. If it is:
- Print `"Skipping student X"` (where X is the student number)
- Use `continue` to move to the next student without adding anything to `scores`

So `-1` bypasses the 0–100 validation — check for it first, before the validation loop.

---

### Step 4 — Handle the "stop early" case with `break`

Also before the validation loop, check if the score is `999`. If it is:
- Print `"Early exit triggered."`
- Use `break` to stop collecting scores immediately

---

### Step 5 — Print a letter grade for each score

After the loop, go through every score in `scores` and print a line like this for each one:

```
Student 1: 85 → B
Student 2: 92 → A
Student 3: 74 → C
```

Use this grading scale:
- 90–100 → `A`
- 80–89 → `B`
- 70–79 → `C`
- 60–69 → `D`
- Below 60 → `F`

Use `if / elif / else` to pick the right letter.

---

### Step 6 — Print class statistics

After the grade list, print a statistics block. Use Python's built-in `max()`, `min()`, `sum()`, and `len()` functions — no loops needed for this step.

```
--- Class Statistics ---
Highest: 95
Lowest: 42
Average: 76.40
Passed: 8 | Failed: 2
```

To count passed (≥ 60) and failed (< 60), loop through `scores` and count:

```python
passed = 0
failed = 0
for score in scores:
    if score >= 60:
        passed += 1
    else:
        failed += 1
```

Format the average to 2 decimal places with `:.2f`.

---

### Things to Watch Out For

- If no scores were collected (all students were skipped or user hit 999 immediately), `scores` will be empty. Python's `max()` and `min()` crash on an empty list. Add a check: `if len(scores) > 0:` before printing statistics.
- Test the `-1` skip and the `999` early exit to make sure they actually work.

---

### Checklist Before Submitting

- [ ] Student count is validated (must be 1–50, keeps asking until valid)
- [ ] Each score is validated (must be 0–100, unless `-1` or `999`)
- [ ] `-1` skips the student using `continue`
- [ ] `999` exits the input loop early using `break`
- [ ] Letter grades are printed for each collected score using `if / elif / else`
- [ ] Statistics (highest, lowest, average, pass/fail) print correctly
- [ ] Average is formatted to 2 decimal places
- [ ] Program doesn't crash if `scores` is empty
