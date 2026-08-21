# Week 3 — Functions and Collections
### Functions, Return Values, Lists, and Dictionaries

---

## Welcome!

So far, every program you've written has been a long sequence of steps from top to bottom. This week you learn two huge ideas that make real programs possible:

1. **Functions** — giving a name to a reusable set of steps, so you can call it whenever you need it without rewriting it.
2. **Collections** — storing many pieces of related data together (lists and dictionaries).

These two ideas show up in literally every program that has ever been written.

---

## Concept 1: Functions

Imagine you work at a coffee shop. Every time someone orders a latte, you do the same steps: pull espresso, steam milk, combine, add foam. Instead of thinking through all those steps every time, you just call it "making a latte."

A **function** is the programming version of that: a named set of steps you can run any time by using its name.

```python
def make_greeting(name):
    print(f"Hello, {name}! Welcome.")

make_greeting("Alex")    # Hello, Alex! Welcome.
make_greeting("Jordan")  # Hello, Jordan! Welcome.
```

**Breaking it down:**
- `def` tells Python "I'm defining a function"
- `make_greeting` is the name you chose (use lowercase with underscores)
- `(name)` is the **parameter** — a placeholder for whatever you pass in when you call the function
- The indented code below is the **body** — what runs when the function is called
- `make_greeting("Alex")` is the **function call** — `"Alex"` is the **argument** (the real value that fills the placeholder)

**Why bother?** Write the steps once, use them hundreds of times. If you need to change how greetings work, you change it in one place — not everywhere you used it.

---

## Concept 2: Return Values

Some functions just *do* something (like printing). Others *calculate* something and **give you back a result**. You bring that result back with `return`.

**Analogy:** A calculator is a function. You give it `3 + 4`, and it gives you back `7`. It *returns* an answer.

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)         # 7
print(add(10, 20))    # 30
print(add(5, 5) * 2)  # 20  — you can use the returned value in expressions
```

When Python hits `return`, the function stops immediately and sends the value back to whoever called it.

**What if there's no `return`?** The function implicitly returns `None` (Python's way of saying "nothing").

```python
def greet(name):
    print(f"Hi, {name}")   # This prints but doesn't return anything

result = greet("Alex")
print(result)              # None  — because greet() never returned a value
```

**Good rule of thumb:** If your function calculates something, `return` it. Let the caller decide what to print. This makes functions reusable in more situations.

---

## Concept 3: Lists

A **list** is an ordered collection of items — like a numbered shopping list.

```
[0] → "milk"
[1] → "eggs"
[2] → "bread"
```

In Python:
```python
shopping = ["milk", "eggs", "bread"]
grades = [85, 92, 78, 95, 60]
mixed = [1, "hello", 3.14, True]   # Lists can hold different types
```

**Accessing items** — counting starts at 0, not 1:
```python
print(shopping[0])    # "milk"    — first item
print(shopping[1])    # "eggs"    — second item
print(shopping[-1])   # "bread"   — last item (-1 always means last)
```

**Analogy:** A list is like a parking lot with numbered spaces. Space 0 is the first spot, space 1 is the second, and so on. You grab a car by its spot number.

**Modifying lists:**
```python
grades.append(88)        # Add to the end → [85, 92, 78, 95, 60, 88]
grades.insert(0, 100)    # Insert 100 at position 0 → [100, 85, ...]
grades.remove(60)        # Remove first occurrence of 60
removed = grades.pop()   # Remove AND return the last item
print(len(grades))       # How many items are in the list
```

**Looping through a list:**
```python
for grade in grades:
    print(grade)
```

---

## Concept 4: Dictionaries

A **dictionary** stores information as **labeled pairs** — each piece of data has a name (a "key") attached to it.

**Analogy:** Think of a real dictionary. You look up a word (the key) and get its definition (the value). Or think of a contact in your phone — you search by name and get back their number.

```python
student = {
    "name": "Alex",
    "age": 20,
    "gpa": 3.75
}

print(student["name"])   # Alex
print(student["gpa"])    # 3.75
```

**Adding and updating:**
```python
student["major"] = "CS"   # Add a new key
student["age"] = 21       # Update an existing key
```

**Looping through a dictionary:**
```python
for key, value in student.items():
    print(f"{key}: {value}")
# name: Alex
# age: 21
# gpa: 3.75
# major: CS
```

**Safe lookup with `.get()`** — use this when you're not sure if a key exists:
```python
grade = student.get("grade", "Not set")  # Returns "Not set" if "grade" doesn't exist
```

---

## Concept 5: Filtering a List

Filtering means going through a list and keeping only the items that match a condition — like sorting M&Ms by color.

```python
grades = [88, 45, 92, 70, 55, 99]

passing = []                    # Start with an empty list
for grade in grades:
    if grade >= 60:             # Check the condition
        passing.append(grade)   # If it passes, add it to the new list

print(passing)   # [88, 92, 70, 99]
```

---

## Concept 6: Counting with a Dictionary

You want to count how many times each item appears — like tallying votes.

```python
votes = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice"]

counts = {}
for vote in votes:
    counts[vote] = counts.get(vote, 0) + 1
    # If the name is already a key, get its count and add 1.
    # If not, start from 0 and add 1.

print(counts)   # {'Alice': 3, 'Bob': 2, 'Carol': 1}
```

---

## Assignment Instructions

**File to create:** `module_03/collections.py`

You're building a small student-record system. You'll use functions to organize your code and a list of dictionaries to store the data. Follow each step in order.

---

### Step 1 — Create your student data

At the top of your file (outside any function), create a list called `students`. It should contain at least **6 dictionaries**, each with these keys: `"name"`, `"grade"`, and `"major"`.

```python
students = [
    {"name": "Alice",  "grade": 91, "major": "CS"},
    {"name": "Bob",    "grade": 54, "major": "Math"},
    {"name": "Carol",  "grade": 78, "major": "CS"},
    {"name": "David",  "grade": 63, "major": "Art"},
    {"name": "Eve",    "grade": 45, "major": "Math"},
    {"name": "Frank",  "grade": 88, "major": "CS"},
]
```

Mix up the grades and majors so you can see filtering and counting work properly.

---

### Step 2 — Write `get_passing_students(students)`

Write a function that takes the student list and returns a new list containing only students with a grade of 60 or above.

```python
def get_passing_students(students):
    passing = []
    for student in students:
        if student["grade"] >= 60:
            passing.append(student)
    return passing
```

Test it by printing the result:
```python
passing = get_passing_students(students)
for s in passing:
    print(s["name"], s["grade"])
```

---

### Step 3 — Write `get_average_grade(students)`

Write a function that returns the **average grade** of all students as a float.

Steps inside the function:
1. If the list is empty, return `0` (to avoid dividing by zero).
2. Add up all the grades.
3. Divide by the number of students.
4. Return the result.

```python
def get_average_grade(students):
    if len(students) == 0:
        return 0
    total = 0
    for student in students:
        total += student["grade"]
    return total / len(students)
```

---

### Step 4 — Write `count_by_major(students)`

Write a function that returns a dictionary where each key is a major name and each value is how many students are in that major.

```python
def count_by_major(students):
    counts = {}
    for student in students:
        major = student["major"]
        counts[major] = counts.get(major, 0) + 1
    return counts
```

Expected output with the sample data: `{'CS': 3, 'Math': 2, 'Art': 1}`

---

### Step 5 — Write `get_top_student(students)`

Write a function that returns the student dictionary with the highest grade. If the list is empty, return `None`.

Start by assuming the first student is the top. Then loop through the rest. If you find someone with a higher grade, they become the new top.

---

### Step 6 — Write `filter_by_major(students, major)`

Write a function that takes the student list and a major name string, and returns a list of all students in that major.

```python
cs_students = filter_by_major(students, "CS")
# Should return Alice, Carol, Frank
```

---

### Step 7 — Call everything from `main()`

At the bottom of your file, write a `main()` function that calls all five functions and prints the results in a clean, readable format. Then call `main()` at the very bottom:

```python
def main():
    print("--- Student Report ---")
    print(f"Total students: {len(students)}")

    passing = get_passing_students(students)
    print(f"Passing students: {len(passing)}")

    avg = get_average_grade(students)
    print(f"Average grade: {avg:.2f}")

    print(f"Students by major: {count_by_major(students)}")

    top = get_top_student(students)
    print(f"Top student: {top['name']} ({top['grade']})")

    print("\nCS students:")
    for s in filter_by_major(students, "CS"):
        print(f"  {s['name']} — {s['grade']}")

main()
```

---

### Checklist Before Submitting

- [ ] At least 6 students defined as a list of dictionaries with `"name"`, `"grade"`, `"major"`
- [ ] `get_passing_students()` returns only students with grade ≥ 60
- [ ] `get_average_grade()` returns a float and handles an empty list without crashing
- [ ] `count_by_major()` returns a dictionary of major → student count
- [ ] `get_top_student()` returns the student with the highest grade
- [ ] `filter_by_major()` returns only students in the given major
- [ ] All logic lives inside named functions
- [ ] `main()` calls all functions and prints a readable report
- [ ] `main()` is called at the bottom of the file
