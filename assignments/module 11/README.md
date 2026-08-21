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
