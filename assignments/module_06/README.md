# Week 6 — Linked Lists

This week you build your first custom **data structure** from scratch. A linked list is a chain of objects (nodes) where each node holds a value and a pointer to the next node. It has very different strengths and weaknesses than a Python list, and understanding those differences is the point.

---

## Concepts Covered

### 1. Nodes

A **node** is the fundamental unit of a linked list. Each node stores:
1. A **value** (the data it holds)
2. A **next** pointer (a reference to the next node, or `None` if it's the last)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None   # Points to the next Node, or None
```

Nodes are just objects. They know nothing about the list they're in — that's the linked list's job.

---

### 2. Linked List Structure

A **linked list** object keeps track of the **head** (the first node). Everything else is reached by following `next` pointers.

```python
class LinkedList:
    def __init__(self):
        self.head = None   # Empty list — no nodes yet
```

A list with three elements looks like this in memory:

```
head → [10 | next] → [20 | next] → [30 | None]
```

---

### 3. Traversal

To visit every node, start at `head` and follow `next` until you reach `None`:

```python
def print_all(self):
    current = self.head
    while current is not None:
        print(current.value)
        current = current.next   # Move to the next node
```

> **Crucial:** Always save `current.next` before modifying `current.next`, or you will lose your place in the chain.

---

### 4. Append (Add to End)

```python
def append(self, value):
    new_node = Node(value)
    if self.head is None:          # Empty list — new node becomes head
        self.head = new_node
        return
    current = self.head
    while current.next is not None:  # Walk to the last node
        current = current.next
    current.next = new_node          # Link last node to the new one
```

---

### 5. Prepend (Add to Front)

Adding to the front is O(1) — no traversal needed!

```python
def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head   # New node points to old head
    self.head = new_node        # New node is now the head
```

---

### 6. Deletion

To delete a node, you must update the **previous** node's `next` to skip over the target:

```python
def delete(self, value):
    if self.head is None:
        return
    if self.head.value == value:   # Deleting the head
        self.head = self.head.next
        return
    current = self.head
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next   # Skip the target node
            return
        current = current.next
```

---

### 7. Edge Cases

Always handle these or your code will crash:
- **Empty list** — `self.head is None`. Check this at the start of every method.
- **Single-element list** — deleting the head should leave `head = None`.
- **Target not found** — searching or deleting a value that doesn't exist; decide whether to raise an error or do nothing.
- **Deleting the head** — requires special handling (shown above).

---

### 8. Array vs. Linked List Trade-offs

| Operation        | Python List (Array) | Linked List       |
|------------------|---------------------|-------------------|
| Access by index  | O(1)                | O(n)              |
| Prepend          | O(n) — shift all    | O(1)              |
| Append           | O(1) amortized      | O(n) without tail |
| Delete (middle)  | O(n) — shift all    | O(n) to find, O(1) to remove |
| Memory           | Contiguous block    | Scattered, extra pointer per node |

Use a linked list when you need fast insertions/deletions at the front and don't need random index access.

---

## Hints for This Week's Assignment

- **Draw it out.** Before writing a single line of code, draw boxes and arrows representing the nodes. Then trace through your algorithm on paper first.
- Every method that modifies the list must handle the **empty list** case — always check `self.head is None` first.
- When traversing, use a `current` variable — **never** advance `self.head` directly, or you'll lose the list.
- For deletion, you need the node **before** the one you want to remove. That's why you check `current.next.value` (the next node's value) while sitting on `current`.
- After every operation, print the full list to verify the result is what you expected.

---

## Assignment Instructions

**File to create:** `module_06/linked_list.py`

You will implement a complete `LinkedList` class from scratch, then demonstrate it with a real use case. Work through each step in order — each one adds a new method to the class.

---

### Step 1 — Implement the `Node` class

Create a `Node` class with:
- `value` — the data stored in this node
- `next` — initialized to `None`

---

### Step 2 — Implement the `LinkedList` class skeleton

Create a `LinkedList` class with:
- `__init__` that sets `self.head = None`
- A `__str__` method that returns a string representation of the list, like:  
  `"10 → 20 → 30 → None"`  
  **Hint:** Traverse the list, collect values into a list, then `" → ".join(...)` them and append `" → None"`.

Test it immediately:
```python
ll = LinkedList()
print(ll)   # None
```

---

### Step 3 — Implement `append(value)`

Add a new node to the **end** of the list. Handle the empty list case (new node becomes the head).

Test:
```python
ll.append(10)
ll.append(20)
ll.append(30)
print(ll)   # 10 → 20 → 30 → None
```

---

### Step 4 — Implement `prepend(value)`

Add a new node to the **front** of the list.

Test:
```python
ll.prepend(5)
print(ll)   # 5 → 10 → 20 → 30 → None
```

---

### Step 5 — Implement `delete(value)`

Remove the **first** node whose value matches the given value. Handle these cases:
1. Empty list — do nothing.
2. The head node matches — update `self.head`.
3. A middle or tail node matches — relink the previous node's `next`.
4. Value not found — do nothing.

Test:
```python
ll.delete(20)
print(ll)   # 5 → 10 → 30 → None
ll.delete(5)
print(ll)   # 10 → 30 → None
ll.delete(99)  # Not found — list unchanged
print(ll)   # 10 → 30 → None
```

---

### Step 6 — Implement `search(value)`

Return `True` if the value exists in the list, `False` otherwise.

```python
print(ll.search(10))   # True
print(ll.search(99))   # False
```

---

### Step 7 — Implement `length()`

Return the number of nodes in the list by traversing and counting.

```python
print(ll.length())   # 2
```

---

### Step 8 — Implement `reverse()`

Reverse the list **in place** (do not create a new list). After reversing, `self.head` should point to what was previously the tail.

**Hint:** Use three variables — `prev`, `current`, `next_node` — and re-link each node's `next` to point backward.

```python
ll.append(40)
ll.append(50)
print(ll)          # 10 → 30 → 40 → 50 → None
ll.reverse()
print(ll)          # 50 → 40 → 30 → 10 → None
```

---

### Step 9 — Real-world demo: browser history

At the bottom of your file (in a `main()` function), simulate a simple browser history using your linked list:

1. Prepend each URL as the user "visits" it (most recent at the front).
2. Print the full history.
3. Delete a URL (user clears it from history).
4. Print the updated history.

```python
history = LinkedList()
for url in ["google.com", "github.com", "stackoverflow.com", "python.org"]:
    history.prepend(url)
print("History:", history)
history.delete("github.com")
print("After removing github.com:", history)
print("Total pages:", history.length())
```

---

### Checklist Before Submitting

- [ ] `Node` class with `value` and `next` attributes.
- [ ] `LinkedList.__str__` produces the correct `"a → b → ... → None"` format.
- [ ] `append()` adds to the end; handles empty list.
- [ ] `prepend()` adds to the front.
- [ ] `delete()` handles all four edge cases (empty, head match, middle/tail match, not found).
- [ ] `search()` returns `True`/`False` correctly.
- [ ] `length()` returns the correct count.
- [ ] `reverse()` reverses in place without creating a new list.
- [ ] Browser history demo runs correctly in `main()`.
