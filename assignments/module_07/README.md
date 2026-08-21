# Week 7 — Stacks and Queues

Stacks and queues are **abstract data types** — they define *what* you can do with data, not *how* the data is stored. This week you implement both and use them to solve real problems.

---

## Concepts Covered

### 1. Abstract Data Types (ADTs)

An **ADT** is a mathematical model for a data structure defined by its behavior (the operations it supports), not its implementation. Think of it like a contract:

- A stack says: "I will let you push, pop, and peek."
- It doesn't say whether it uses a list, a linked list, or something else internally.

This separation lets you swap implementations without changing the code that uses them.

---

### 2. Stacks — LIFO (Last In, First Out)

A **stack** works like a stack of plates:
- You add to the **top** (`push`)
- You remove from the **top** (`pop`)
- The last item added is the first one removed — **LIFO**

```
Push 1 → [1]
Push 2 → [1, 2]
Push 3 → [1, 2, 3]
Pop   → returns 3, stack is [1, 2]
```

**Real-world uses:** undo/redo, function call management (the call stack), browser back button.

**Implementation using a Python list:**

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)      # Add to top (end of list)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()       # Remove from top (end of list)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]         # Look at top without removing

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
```

All stack operations are **O(1)**.

---

### 3. Queues — FIFO (First In, First Out)

A **queue** works like a line of people waiting:
- You add to the **back** (`enqueue`)
- You remove from the **front** (`dequeue`)
- The first item added is the first one removed — **FIFO**

```
Enqueue 1 → [1]
Enqueue 2 → [1, 2]
Enqueue 3 → [1, 2, 3]
Dequeue   → returns 1, queue is [2, 3]
```

**Real-world uses:** print queues, task scheduling, breadth-first search.

**Implementation using `collections.deque` (efficient for both ends):**

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, value):
        self._data.append(value)          # Add to back

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.popleft()       # Remove from front — O(1)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
```

> **Why not use a regular list for a queue?** `list.pop(0)` is O(n) because every element must shift. `deque.popleft()` is O(1).

---

### 4. Balanced Bracket Checking

A classic stack application: verifying that brackets in a string are properly balanced and nested.

**Algorithm:**
1. Scan each character left to right.
2. If you see an **opening** bracket (`(`, `[`, `{`), push it onto the stack.
3. If you see a **closing** bracket (`)`, `]`, `}`):
   - If the stack is empty → unbalanced (no matching opener).
   - Pop the stack and check if the opener matches the closer.
   - If they don't match → unbalanced.
4. After scanning all characters, if the stack is empty → balanced. Otherwise → unbalanced.

```python
def is_balanced(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced("({[]})"))   # True
print(is_balanced("({[})"))    # False
```

---

## Hints for This Week's Assignment

- **Always check `is_empty()` before `pop()` or `dequeue()`** — removing from an empty structure raises an error.
- Use Python's built-in `list` for a stack (append/pop from the end are both O(1)).
- Use `collections.deque` for a queue — it gives you O(1) at both ends.
- For balanced brackets, trace through a small example by hand before coding: `"([)]"` should return `False` because the close order is wrong.
- The difference between LIFO and FIFO is the whole point — draw a diagram if you're confused about which end to add/remove from.
