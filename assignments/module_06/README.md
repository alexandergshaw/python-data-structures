# Week 6 — Linked Lists
### Nodes, Traversal, Append, Prepend, Deletion, and Trade-offs

---

## Welcome!

So far you've stored lists of data using Python's built-in list (`[]`). This week you build your own list from scratch — without using Python's built-in one. Why? Because building it yourself makes you understand what's happening under the hood, and because linked lists have real advantages in certain situations.

---

## Concept 1: What's Wrong With Regular Lists?

Python's built-in list stores all its items in a big block of memory, side by side. That makes looking up any item by number super fast (go to slot #5 → instant). But it has a cost:

- **Inserting at the front** of a Python list means every single item has to shift over one spot to make room. With 1 million items, that's 1 million moves.
- **Deleting from the front** has the same problem.

A linked list solves this by using a completely different structure.

---

## Concept 2: Nodes — The Building Block

A **node** is a tiny object that holds two things:
1. A **value** (the actual data — a number, a name, etc.)
2. A **next pointer** (a reference to the next node in the chain)

**Analogy:** Think of a scavenger hunt. Each clue (node) tells you the answer AND where to find the next clue. The last clue says "you're done" (that's `None`).

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # Points to the next Node, or None if last
```

---

## Concept 3: The Linked List

A **linked list** is a chain of nodes. The list object itself only needs to keep track of the **head** (the first node). Everything else you find by following the chain.

```python
class LinkedList:
    def __init__(self):
        self.head = None    # Empty list has no head
```

A list with three items looks like this in memory:

```
head → [10 | •]──→ [20 | •]──→ [30 | None]
```

Each arrow is the `next` pointer pointing to the next node. The last node's `next` is `None` — that's how you know you've reached the end.

---

## Concept 4: Traversal — Walking the Chain

To visit every node, start at `head` and follow the `next` pointers until you hit `None`:

```python
def print_all(self):
    current = self.head       # Start at the beginning
    while current is not None:
        print(current.value)
        current = current.next    # Move to the next node
```

**Critical rule:** Use a `current` variable to walk the list. **Never** move `self.head` forward — you'd lose track of where the list begins!

---

## Concept 5: Append — Adding to the End

1. Create a new node
2. If the list is empty, the new node becomes the head
3. Otherwise, walk to the last node (the one whose `next` is `None`)
4. Point that last node's `next` to the new node

```python
def append(self, value):
    new_node = Node(value)
    if self.head is None:              # Empty list
        self.head = new_node
        return
    current = self.head
    while current.next is not None:    # Walk to the last node
        current = current.next
    current.next = new_node            # Link the new node in
```

---

## Concept 6: Prepend — Adding to the Front (This is Fast!)

1. Create a new node
2. Point the new node's `next` to the current head
3. The new node becomes the new head

```python
def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head    # New node points to old head
    self.head = new_node         # New node IS the new head
```

**Analogy:** You're in a line at a theme park. Someone cuts to the front. They stand in front of the person who was first — they point to that person as the "next" — and now they ARE the new front of the line. O(1): no matter how long the line, this takes the same amount of time.

---

## Concept 7: Deletion — Removing a Node

To remove a node, you need to make the node **before** it skip over it:

```
Before: [A] → [B] → [C]
After:  [A] ────────→ [C]   (B is gone)
```

You don't need to destroy B — just make sure nobody points to it anymore.

```python
def delete(self, value):
    if self.head is None:
        return                           # Nothing to delete

    if self.head.value == value:
        self.head = self.head.next       # Skip the head
        return

    current = self.head
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next   # Skip the target
            return
        current = current.next
```

**Why check `current.next.value` instead of `current.value`?** Because to do the re-linking, you need to be sitting on the node *before* the one you're deleting. You need your hands on the previous node to update its `next`.

---

## Concept 8: Linked Lists vs. Python Lists — When to Use Which

| Operation | Python List | Linked List |
|-----------|-------------|-------------|
| Access item by index (e.g., `[5]`) | O(1) — instant | O(n) — must walk from head |
| Add to the front | O(n) — everything shifts | O(1) — just re-link head |
| Add to the end | O(1) — usually fast | O(n) — must walk to end |
| Delete from anywhere | O(n) | O(n) to find + O(1) to remove |

**Bottom line:** Use a linked list when you need fast additions/deletions at the front, and don't need random access by index.

---

## Assignment Instructions

**File to create:** `module_06/linked_list.py`

You'll build a complete `LinkedList` class from scratch. After each step, test your code before moving on.

---

### Step 1 — Build the `Node` class

`Node` should have two attributes: `value` and `next`. `next` starts as `None`.

---

### Step 2 — Build the `LinkedList` class

Start with just `__init__` (sets `self.head = None`) and `__str__`.

`__str__` should return the list as a readable string. Walk the chain and collect all values, then format them like:
```
10 → 20 → 30 → None
```

Test it:
```python
ll = LinkedList()
print(ll)    # None
```

---

### Step 3 — `append(value)`

Add a value to the end. Handle the empty list case.

```python
ll.append(10)
ll.append(20)
ll.append(30)
print(ll)    # 10 → 20 → 30 → None
```

---

### Step 4 — `prepend(value)`

Add a value to the front.

```python
ll.prepend(5)
print(ll)    # 5 → 10 → 20 → 30 → None
```

---

### Step 5 — `delete(value)`

Remove the first node that has the given value. Test all four cases:

```python
ll.delete(20)        # Delete middle node
print(ll)            # 5 → 10 → 30 → None

ll.delete(5)         # Delete head
print(ll)            # 10 → 30 → None

ll.delete(99)        # Value not in list — do nothing
print(ll)            # 10 → 30 → None

ll.delete(10)
ll.delete(30)
ll.delete(30)        # Delete from empty list — do nothing
print(ll)            # None
```

---

### Step 6 — `search(value)`

Return `True` if the value is anywhere in the list, `False` if not.

```python
ll.append(10)
ll.append(20)
print(ll.search(10))    # True
print(ll.search(99))    # False
```

---

### Step 7 — `length()`

Return the number of nodes. Walk the chain and count.

```python
print(ll.length())   # 2
```

---

### Step 8 — `reverse()`

Reverse the list **in place** — don't create a new list. After reversing, what was the tail becomes the new head.

This one is tricky. Use three variables: `prev` (starts as `None`), `current` (starts at head), and `next_node`. On each step:
1. Save `current.next` into `next_node` (so you don't lose it)
2. Point `current.next` backward to `prev`
3. Move `prev` and `current` one step forward

```python
ll.append(40)
ll.append(50)
print(ll)        # 10 → 20 → 40 → 50 → None
ll.reverse()
print(ll)        # 50 → 40 → 20 → 10 → None
```

---

### Step 9 — Browser history demo

In a `main()` function, simulate browser history. The most recently visited page goes to the front (use `prepend`):

```python
def main():
    history = LinkedList()
    pages = ["google.com", "github.com", "stackoverflow.com", "python.org"]
    for page in pages:
        history.prepend(page)    # Most recent at front

    print("History:", history)
    history.delete("github.com")
    print("After removing github.com:", history)
    print("Pages visited:", history.length())

main()
```

---

### Checklist Before Submitting

- [ ] `Node` has `value` and `next` (initialized to `None`)
- [ ] `__str__` produces the `"a → b → ... → None"` format
- [ ] `append()` works and handles empty list
- [ ] `prepend()` works and makes the new node the head
- [ ] `delete()` handles: empty list, delete head, delete middle/tail, value not found
- [ ] `search()` returns `True`/`False`
- [ ] `length()` returns the correct count
- [ ] `reverse()` reverses in place (no new list created)
- [ ] Browser history demo runs and produces correct output
