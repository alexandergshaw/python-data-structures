# Week 3 — Functions and Collections

This week you learn to **organize** your code into reusable pieces (functions) and to **store groups of data** in lists and dictionaries. These two ideas — abstraction and data organization — are the backbone of almost every program you will ever write.

---

## Concepts Covered

### 1. Functions

A function is a named, reusable block of code. Define it once, call it as many times as you need.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")   # Hello, Alex!
greet("Jordan") # Hello, Jordan!
```

**Anatomy of a function:**
- `def` — keyword that starts the definition
- `greet` — the name you choose (use lowercase_underscores)
- `(name)` — the **parameter(s)** — placeholders for values passed in
- The indented body — the code that runs when the function is called
- `greet("Alex")` — calling the function with the **argument** `"Alex"`

---

### 2. Return Values

Functions can compute something and **hand it back** to the caller with `return`.

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # 7
```

- After `return` executes, the function stops immediately.
- If a function has no `return` statement, it implicitly returns `None`.

```python
def square(n):
    return n * n

print(square(5))        # 25
print(square(5) + 1)    # 26 — you can use the return value in expressions
```

---

### 3. Lists

A **list** is an ordered, mutable (changeable) collection of items.

```python
numbers = [10, 20, 30, 40, 50]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]
```

**Indexing** (zero-based — first item is index `0`):

```python
print(numbers[0])   # 10
print(numbers[-1])  # 50  (negative index counts from the end)
```

**Common list operations:**

```python
numbers.append(60)      # Add to the end
numbers.insert(0, 5)    # Insert 5 at index 0
numbers.remove(30)      # Remove first occurrence of 30
popped = numbers.pop()  # Remove and return last item
print(len(numbers))     # Number of items
```

**Iterating:**

```python
for num in numbers:
    print(num)
```

---

### 4. Dictionaries

A **dictionary** stores data as **key-value pairs**. Use it when each piece of data has a label.

```python
student = {
    "name": "Alex",
    "age": 20,
    "gpa": 3.75
}

print(student["name"])   # Alex
student["age"] = 21      # Update a value
student["major"] = "CS"  # Add a new key
```

**Iterating over a dictionary:**

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Check if a key exists before accessing it:

```python
if "gpa" in student:
    print(student["gpa"])
```

Use `.get()` to avoid a `KeyError` when the key might not exist:

```python
grade = student.get("grade", "N/A")  # Returns "N/A" if "grade" doesn't exist
```

---

### 5. Filtering Data

To collect items that match a condition, loop through the collection and append matches to a new list:

```python
grades = [88, 45, 92, 70, 55, 99]

passing = []
for grade in grades:
    if grade >= 60:
        passing.append(grade)

print(passing)   # [88, 92, 70, 99]
```

---

### 6. Counting Data

To count how many times each item appears, use a dictionary where keys are items and values are counts:

```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

---

## Hints for This Week's Assignment

- **One function, one job.** If a function is doing two different things, split it into two functions.
- **Return, don't print** (usually). Functions should `return` values so the caller can decide what to do with them. Printing inside a function makes it harder to reuse.
- **Test functions in isolation.** Call your function with known inputs and `print()` the result to verify it before using it in a larger program.
- When filtering a list, start with an empty list `[]` and `append()` items that pass your condition.
- When counting with a dictionary, the pattern `counts[word] = counts.get(word, 0) + 1` is a compact shorthand for the if/else shown above.
- List indices start at **0**, not 1. Accessing an index that doesn't exist causes an `IndexError` — check `len()` first if you're not sure.
