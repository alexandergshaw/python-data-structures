# Week 11 — Heaps and Priority Queues

A **heap** is a specialized tree structure that always keeps its smallest (or largest) element instantly accessible. It's the engine behind priority queues, efficient sorting, and scheduling systems. This week you build one using a plain Python list.

---

## Concepts Covered

### 1. What Is a Heap?

A **min-heap** is a binary tree with two properties:

1. **Shape property:** The tree is a **complete binary tree** — every level is fully filled except possibly the last, which fills left to right.
2. **Heap property:** Every node's value is **less than or equal to** its children's values.

Result: the **smallest element is always at the root**.

A **max-heap** reverses the rule — every node is greater than or equal to its children, so the largest is at the root.

```
Min-heap example:
        1
       / \
      3   5
     / \ /
    7  4 6
```

---

### 2. Array-Based Heap Representation

Because heaps are always complete binary trees, you can store them efficiently in a plain list (no pointers needed):

```
Index:  0  1  2  3  4  5
Array: [1, 3, 5, 7, 4, 6]
```

For a node at index `i`:
- **Left child:** `2 * i + 1`
- **Right child:** `2 * i + 2`
- **Parent:** `(i - 1) // 2`

This is how Python's built-in `heapq` module works internally.

---

### 3. Sift-Up (After Insertion)

When you add a new element, append it to the end of the list, then "sift up" to restore the heap property:

```python
def push(self, value):
    self._data.append(value)
    self._sift_up(len(self._data) - 1)

def _sift_up(self, index):
    while index > 0:
        parent = (index - 1) // 2
        if self._data[index] < self._data[parent]:
            self._data[index], self._data[parent] = \
                self._data[parent], self._data[index]
            index = parent
        else:
            break
```

---

### 4. Sift-Down (After Extraction)

When you remove the minimum (the root), replace it with the last element, then "sift down":

```python
def pop(self):
    if len(self._data) == 0:
        raise IndexError("Heap is empty")
    # Swap root with last, remove last
    self._data[0] = self._data[-1]
    self._data.pop()
    self._sift_down(0)

def _sift_down(self, index):
    n = len(self._data)
    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < n and self._data[left] < self._data[smallest]:
            smallest = left
        if right < n and self._data[right] < self._data[smallest]:
            smallest = right

        if smallest != index:
            self._data[index], self._data[smallest] = \
                self._data[smallest], self._data[index]
            index = smallest
        else:
            break
```

Both sift-up and sift-down are **O(log n)** because the tree height is log n.

---

### 5. Priority Queues

A **priority queue** is an ADT where each item has a priority and the item with the highest priority (lowest number, usually) is always served first — regardless of insertion order.

Implemented with a min-heap:

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []

    def push(self, priority, item):
        heapq.heappush(self._heap, (priority, item))

    def pop(self):
        priority, item = heapq.heappop(self._heap)
        return item

    def is_empty(self):
        return len(self._heap) == 0
```

**Real-world uses:** hospital triage, CPU scheduling, Dijkstra's shortest-path algorithm.

---

### 6. Task Scheduling Example

```python
pq = PriorityQueue()
pq.push(3, "Low priority task")
pq.push(1, "Urgent task")
pq.push(2, "Medium task")

while not pq.is_empty():
    print(pq.pop())
# Urgent task
# Medium task
# Low priority task
```

---

## Hints for This Week's Assignment

- **Index arithmetic is your friend.** Write out the parent/child formulas and verify them manually on a small array before coding.
- Always check for the empty case in `pop()` and `peek()`.
- Sift-up stops when the node is in the right place (heap property holds) or when it reaches the root.
- Sift-down stops when both children are larger than the current node (for a min-heap) or when there are no children.
- Python's `heapq` module gives you a min-heap for free: `heapq.heappush(h, val)` and `heapq.heappop(h)`. Use it to verify your implementation produces the same results.
- Tuples in a heap are compared element by element — `(priority, item)` lets you use the tuple directly with `heapq` without extra configuration.

---

## Assignment Instructions

**File to create:** `module_11/heap.py`

You will implement a `MinHeap` class from scratch using a plain Python list, then build a `PriorityQueue` on top of it. Work through each step in order.

---

### Step 1 — `MinHeap` class skeleton

Create a `MinHeap` class with:
- `self._data = []` — the backing list
- `__len__` returning `len(self._data)`
- `__str__` returning `f"MinHeap: {self._data}"`
- `is_empty()` returning `True` when the heap is empty
- `peek()` returning `self._data[0]`; raise `IndexError` if empty

---

### Step 2 — `push(value)`

Append `value` to the end of `_data`, then call `_sift_up()` to restore the heap property.

Implement `_sift_up(index)` using the parent formula `(index - 1) // 2`.

```python
h = MinHeap()
h.push(5)
h.push(3)
h.push(8)
h.push(1)
print(h)     # MinHeap: [1, 3, 8, 5]  (exact order may vary, but 1 must be first)
print(h.peek())   # 1
```

---

### Step 3 — `pop()`

Swap the root with the last element, remove the last element (the old root), then call `_sift_down(0)` to restore the heap property.

Implement `_sift_down(index)` using the left-child formula `2 * index + 1` and right-child formula `2 * index + 2`.

```python
print(h.pop())   # 1  — smallest element
print(h.pop())   # 3
print(h.pop())   # 5
print(h.pop())   # 8
```

---

### Step 4 — Verify against `heapq`

Add a block that pushes the same values into both your `MinHeap` and Python's `heapq`, then pops everything from both and compares:

```python
import heapq

values = [9, 4, 7, 1, 8, 3, 6, 2, 5]

my_heap = MinHeap()
for v in values:
    my_heap.push(v)

reference = []
for v in values:
    heapq.heappush(reference, v)

my_result  = [my_heap.pop() for _ in range(len(values))]
ref_result = [heapq.heappop(reference) for _ in range(len(values))]

assert my_result == ref_result, f"Mismatch!\nMine: {my_result}\nRef:  {ref_result}"
print("Heap verified:", my_result)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### Step 5 — `PriorityQueue` class

Build a `PriorityQueue` class on top of your `MinHeap`. Lower priority number = higher urgency (served first).

| Method                    | Behavior                                                   |
|---------------------------|------------------------------------------------------------|
| `push(priority, item)`    | Insert `(priority, item)` as a tuple into the heap        |
| `pop()`                   | Remove and return the `item` with the lowest priority number |
| `peek()`                  | Return the `item` with the lowest priority without removing it |
| `is_empty()`              | Return `True` if the queue is empty                        |

```python
pq = PriorityQueue()
pq.push(3, "Low priority report")
pq.push(1, "Urgent bug fix")
pq.push(2, "Medium task")
pq.push(1, "Another urgent item")

while not pq.is_empty():
    print(pq.pop())
# Urgent bug fix
# Another urgent item
# Medium task
# Low priority report
```

> **Hint:** Store tuples `(priority, item)` in the heap. Python compares tuples element by element, so the heap will order by priority automatically.

---

### Step 6 — Hospital triage demo

Write a `triage_demo()` function that simulates a hospital emergency room:

1. Create a `PriorityQueue`.
2. Add at least 6 patients, each with a triage priority (1 = critical, 2 = urgent, 3 = stable) and a name.
3. Process all patients in priority order, printing `"Treating: <name> (priority <n>)"` for each.

```
Treating: Cardiac arrest patient (priority 1)
Treating: Severe trauma patient (priority 1)
Treating: Broken arm patient (priority 2)
Treating: Sprained ankle patient (priority 3)
...
```

---

### Checklist Before Submitting

- [ ] `MinHeap.push()` correctly sifts up and maintains the heap property.
- [ ] `MinHeap.pop()` correctly sifts down; raises `IndexError` on empty heap.
- [ ] `MinHeap.peek()` raises `IndexError` on empty heap.
- [ ] The `heapq` verification block passes the assertion.
- [ ] `PriorityQueue.push()` and `.pop()` work correctly (items come out lowest-priority-number first).
- [ ] Two items with the same priority can both be stored (no crash).
- [ ] `triage_demo()` runs and prints patients in priority order.
