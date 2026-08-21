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

---

## Assignment Instructions

**File to create:** `module_03/collections.py`

You will build a small student-record system using functions, lists, and dictionaries. Follow each step in order and call each function in a `main()` function at the bottom of your file.

---

### Step 1 — Store student records

Create a **list of dictionaries** where each dictionary represents one student. Each student must have at least these four keys:

```python
students = [
    {"name": "Alice", "grade": 91, "major": "CS"},
    {"name": "Bob",   "grade": 54, "major": "Math"},
    {"name": "Carol", "grade": 78, "major": "CS"},
    {"name": "David", "grade": 63, "major": "Art"},
    {"name": "Eve",   "grade": 45, "major": "Math"},
    {"name": "Frank", "grade": 88, "major": "CS"},
]
```

You must have **at least 6 students** with a mix of grades and majors.

---

### Step 2 — Write `get_passing_students(students)`

Write a function that takes the student list and returns a **new list** containing only the students whose grade is 60 or above.

```python
def get_passing_students(students):
    # Your code here
```

Test it:
```python
passing = get_passing_students(students)
print(passing)  # Should show Alice, Carol, David, Frank
```

---

### Step 3 — Write `get_average_grade(students)`

Write a function that takes the student list and returns the **average grade** as a float. Use a `for` loop to sum all grades, then divide by the number of students.

Return `0` if the list is empty (avoid division by zero).

---

### Step 4 — Write `count_by_major(students)`

Write a function that returns a **dictionary** mapping each major to how many students are enrolled in it.

```python
{"CS": 3, "Math": 2, "Art": 1}
```

Use the counting pattern from the concept section: `counts[major] = counts.get(major, 0) + 1`.

---

### Step 5 — Write `get_top_student(students)`

Write a function that returns the **dictionary** of the student with the highest grade. If two students are tied, return either one.

**Hint:** Start by assuming the first student is the top, then loop through the rest and update if you find a higher grade.

---

### Step 6 — Write `filter_by_major(students, major)`

Write a function that takes the student list and a major name (string) and returns a list of all students in that major.

```python
cs_students = filter_by_major(students, "CS")
# → [Alice, Carol, Frank]
```

---

### Step 7 — Print a formatted report

In your `main()` function, call all five functions and print the results in a clean format:

```
--- Student Report ---
All students: 6
Passing students: 4
Average grade: 69.83
Students by major: {'CS': 3, 'Math': 2, 'Art': 1}
Top student: Alice (91)

CS students:
  Alice — 91
  Carol — 78
  Frank — 88
```

---

### Checklist Before Submitting

- [ ] You have at least 6 students defined as a list of dictionaries.
- [ ] `get_passing_students()` returns only students with grade ≥ 60.
- [ ] `get_average_grade()` returns a float and handles an empty list.
- [ ] `count_by_major()` returns a dictionary of major → count.
- [ ] `get_top_student()` returns the student dictionary with the highest grade.
- [ ] `filter_by_major()` returns students matching the given major.
- [ ] A `main()` function calls all five functions and prints a formatted report.
- [ ] All logic is inside functions — no bare code outside of `main()`.
