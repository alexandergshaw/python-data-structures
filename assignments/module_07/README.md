# Week 7 — Stacks and Queues
### Abstract Data Types, LIFO, FIFO, and Balanced Brackets

---

## Welcome!

This week you learn two of the most useful data structures in computer science: **stacks** and **queues**. You've already used both of them in real life today — you just didn't know it had a name.

---

## Concept 1: Abstract Data Types (ADTs)

An **abstract data type** is a description of what you can *do* with a data structure, without specifying exactly how it's built internally.

**Analogy:** Think of a TV remote. It's an abstract interface — you press "volume up" and the volume goes up. You don't know or care whether the remote uses infrared light, Bluetooth, or radio waves. The *what* (raise the volume) is separate from the *how* (the electronics).

A stack says: "I support push, pop, and peek." It doesn't say whether it uses a Python list, a linked list, or something else internally. The contract is the behavior, not the implementation.

---

## Concept 2: Stacks — Last In, First Out (LIFO)

A stack works like a **stack of plates**:
- You add plates to the **top** (push)
- You take plates from the **top** (pop)
- The most recently added plate is the first one you take off

**LIFO: Last In, First Out** — the last thing added is the first thing removed.

```
Push 1 → [1]
Push 2 → [1, 2]
Push 3 → [1, 2, 3]
Pop   → removes 3 → [1, 2]
Pop   → removes 2 → [1]
```

**Real-world examples of stacks:**
- Your browser's back button — each page you visit gets pushed. Back pops the most recent.
- Ctrl+Z undo — each action gets pushed. Undo pops the last action.
- The function call stack — when Python calls a function, it pushes the current location so it can come back when the function finishes.

**Implementation using a Python list:**

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)      # Add to the "top" (end of list)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._data.pop()       # Remove from the "top"

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self._data[-1]         # Look at top without removing

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
```

All operations are O(1) — instant, regardless of size.

---

## Concept 3: Queues — First In, First Out (FIFO)

A queue works like a **line at a coffee shop**:
- You join at the **back** (enqueue)
- You're served at the **front** (dequeue)
- The first person in line is the first person served

**FIFO: First In, First Out** — the first thing added is the first thing removed.

```
Enqueue "Alice" → [Alice]
Enqueue "Bob"   → [Alice, Bob]
Enqueue "Carol" → [Alice, Bob, Carol]
Dequeue → removes Alice → [Bob, Carol]
```

**Real-world examples of queues:**
- A printer queue — print jobs are printed in the order they were submitted
- Customer service — first caller gets helped first
- BFS graph traversal (you'll see this in Week 13)

**Implementation using `collections.deque`:**

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, value):
        self._data.append(value)         # Add to the back

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._data.popleft()      # Remove from the front

    def front(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
```

**Why `deque` and not a regular list?** Removing from the front of a Python list (`list.pop(0)`) is O(n) — every other item has to shift. `deque.popleft()` is O(1). Use the right tool.

---

## Concept 4: Balanced Bracket Checking (Classic Stack Problem)

Consider the string `"({[]})"`. The brackets are properly balanced and nested. But `"({[})"` is not — the `}` closes before the `[` does.

**How to check with a stack:**
- Scan each character left to right
- If you see an *opening* bracket (`(`, `[`, `{`) → push it onto the stack
- If you see a *closing* bracket (`)`, `]`, `}`) → check if the top of the stack is the matching opener. If yes, pop. If no (or stack is empty), it's unbalanced.
- After scanning everything: if the stack is empty → balanced. If not → unbalanced (some opener was never closed).

**Analogy:** Imagine stacking "open" cards face-up. Every time you see a "close" card, it must match the card on top. If it does, remove the top card. If it doesn't, something is wrong.

```python
def is_balanced(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)      # Push openers
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return False        # No matching opener
            stack.pop()             # Matched — pop it

    return len(stack) == 0          # True if no unmatched openers remain
```

---

## Assignment Instructions

**File to create:** `module_07/stacks_queues.py`

You'll implement both data structures and build three real-world applications.

---

### Step 1 — Implement `Stack`

Your stack must have:
- `push(value)` — add to top
- `pop()` — remove and return top; raise `IndexError` if empty
- `peek()` — return top without removing; raise `IndexError` if empty
- `is_empty()` — return `True` if empty
- `size()` — return count of items
- `__str__()` — return a string like `"Stack (top → bottom): [3, 2, 1]"`

Test:
```python
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)           # Stack (top → bottom): [3, 2, 1]
print(s.pop())     # 3
print(s.peek())    # 2
print(s.size())    # 2
print(s.is_empty())   # False
```

---

### Step 2 — Implement `Queue`

Your queue must have:
- `enqueue(value)` — add to back
- `dequeue()` — remove and return front; raise `IndexError` if empty
- `front()` — return front without removing; raise `IndexError` if empty
- `is_empty()` — return `True` if empty
- `size()` — return count
- `__str__()` — return `"Queue (front → back): [Alice, Bob, Carol]"`

Test:
```python
q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Carol")
print(q)                # Queue (front → back): [Alice, Bob, Carol]
print(q.dequeue())      # Alice
print(q.front())        # Bob
```

---

### Step 3 — `is_balanced(s)` using your Stack

Write the balanced bracket checker described above. Use your `Stack` class (not a plain Python list).

Test ALL of these:
```python
print(is_balanced("({[]})"))      # True
print(is_balanced("{[()]}"))      # True
print(is_balanced("({[})"))       # False
print(is_balanced("((())"))       # False — opener with no closer
print(is_balanced("hello()[]"))   # True — non-brackets ignored
print(is_balanced(""))            # True — empty string
```

---

### Step 4 — Print Queue Simulator

Write a `print_queue_demo()` function that:
1. Creates a `Queue`
2. Enqueues at least 5 print jobs (strings like `"Report.pdf"`, `"Photo.png"`, etc.)
3. Prints the full queue
4. Processes (dequeues) all jobs in a `while` loop, printing `"Printing: <job>"` for each
5. Confirms the queue is empty at the end

Expected output:
```
Queue (front → back): [Report.pdf, Photo.png, Letter.docx, Invoice.pdf, Notes.txt]
Printing: Report.pdf
Printing: Photo.png
Printing: Letter.docx
Printing: Invoice.pdf
Printing: Notes.txt
All jobs done. Queue empty: True
```

---

### Step 5 — Undo / Redo System

This is a classic stack-of-stacks problem. Write three functions that use **two** `Stack` objects: an `undo_stack` and a `redo_stack`.

- `do_action(action, undo_stack, redo_stack)`:
  - Push `action` onto `undo_stack`
  - Clear `redo_stack` (new actions cancel redo history — just like Word does)

- `undo(undo_stack, redo_stack)`:
  - Pop from `undo_stack`, push onto `redo_stack`
  - Return the undone action (or `None` if undo stack is empty)

- `redo(undo_stack, redo_stack)`:
  - Pop from `redo_stack`, push back onto `undo_stack`
  - Return the redone action (or `None` if redo stack is empty)

Demo it:
```python
undo_s = Stack()
redo_s = Stack()

do_action("Type 'Hello'", undo_s, redo_s)
do_action("Bold text", undo_s, redo_s)
do_action("Insert image", undo_s, redo_s)

print("Undo:", undo(undo_s, redo_s))    # Insert image
print("Undo:", undo(undo_s, redo_s))    # Bold text
print("Redo:", redo(undo_s, redo_s))    # Bold text
print("Undo:", undo(undo_s, redo_s))    # Bold text (re-undone)
```

---

### Checklist Before Submitting

- [ ] `Stack` with all six required methods; `pop()` and `peek()` raise `IndexError` on empty
- [ ] `Queue` with all six required methods; `dequeue()` and `front()` raise `IndexError` on empty
- [ ] `Queue` uses `collections.deque` internally (not a list)
- [ ] `is_balanced()` passes all six test cases above
- [ ] Print queue demo shows all jobs processed in FIFO order
- [ ] Undo/redo demo shows correct action names returned
- [ ] Redo stack is cleared when a new action is performed
