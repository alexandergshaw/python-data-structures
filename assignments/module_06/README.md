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
