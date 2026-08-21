# Week 11 — Heaps and Priority Queues
### Min-Heaps, Array Representation, Sift-Up, Sift-Down, and Scheduling

---

## Welcome!

You've learned about queues — first in, first out. But what if the order shouldn't be based on arrival time? What if the most *urgent* item should always go first, regardless of when it arrived? That's what a **priority queue** does, and it's powered by a data structure called a **heap**.

---

## Concept 1: The Priority Queue Problem

Imagine a hospital emergency room. Patients don't get seen in the order they arrived — they get seen based on how critical their condition is. A patient with a heart attack goes before someone with a sprained ankle, even if the ankle patient arrived first.

A **priority queue** is the data structure that makes this possible: you insert items with a priority number, and you always get back the item with the highest priority (usually the lowest priority number — 1 = most urgent).

---

## Concept 2: What Is a Heap?

A **min-heap** is a special kind of binary tree where:
1. **It's always "complete"** — every level is full except possibly the last, and the last level fills from left to right
2. **The smallest value is always at the top** — every node's value is smaller than or equal to its children

This second property means you can always find the minimum in O(1) — it's right at the top.

```
Min-heap:
        1
       / \
      3   5
     / \ /
    7  4 6
```

Is `1` ≤ `3` and `5`? Yes. Is `3` ≤ `7` and `4`? Yes. Is `5` ≤ `6`? Yes. ✅ Valid min-heap.

A **max-heap** is the same idea but reversed — the largest value is always at the top.

---

## Concept 3: Storing the Heap in a List (No Pointers Needed!)

Because a heap is always a complete tree, you can store it in a plain Python list and calculate parent/child relationships with simple math:

```
Index:  0  1  2  3  4  5
Array: [1, 3, 5, 7, 4, 6]
```

For any node at index `i`:
- **Left child** is at index `2*i + 1`
- **Right child** is at index `2*i + 2`
- **Parent** is at index `(i - 1) // 2`

**Check:** The node at index 1 (value = 3) has left child at index 3 (value = 7) and right child at index 4 (value = 4). Parent at index 0 (value = 1). ✅

This is how Python's built-in `heapq` module works internally.

---

## Concept 4: Sift-Up — Restoring Order After Insertion

When you add a new item, you always append it to the end of the list first. But this might violate the heap property (the new item might be smaller than its parent). So you "sift up" — swap the item with its parent repeatedly until the heap property is restored.

**Analogy:** A new employee joins a company at the bottom (intern). But they're more capable than their direct manager. They get promoted (swapped) up one level. Still more capable than the next manager? Promoted again. Eventually they find their right level.

```python
def _sift_up(self, index):
    while index > 0:
        parent = (index - 1) // 2
        if self._data[index] < self._data[parent]:   # Child smaller than parent?
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            index = parent    # Move up and check again
        else:
            break             # Heap property restored — stop
```

---

## Concept 5: Sift-Down — Restoring Order After Removal

When you remove the minimum (the root), you:
1. Move the last item to the root position (to fill the gap)
2. "Sift down" — swap it with its smallest child repeatedly until the heap property is restored

**Analogy:** The best employee (root) leaves the company. You temporarily promote the newest intern to their role. The intern might not be the best fit, so you reassign them: they swap with the more capable of their two direct reports. Then check that level. Repeat until everyone is in a valid place.

```python
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
            self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
            index = smallest    # Move down and check again
        else:
            break               # Heap property restored
```

---

## Concept 6: Priority Queues Using Heaps

Now that you have a heap, building a priority queue is straightforward:
- `push(priority, item)` → insert a `(priority, item)` tuple. Python compares tuples from left to right, so the heap automatically orders by priority number.
- `pop()` → remove and return the item with the smallest priority number (highest urgency)

---

## Assignment Instructions

**File to create:** `module_11/heap.py`

---

### Step 1 — `MinHeap` skeleton

```python
class MinHeap:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"MinHeap: {self._data}"

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._data[0]
```

---

### Step 2 — `push(value)` with `_sift_up`

Append the value to the end of `_data`, then call `_sift_up` with its index.

```python
h = MinHeap()
h.push(5)
h.push(3)
h.push(8)
h.push(1)
print(h)           # MinHeap: [1, 3, 8, 5]  — 1 must be first
print(h.peek())    # 1
```

The exact internal order depends on insertion order, but the root must always be the minimum.

---

### Step 3 — `pop()` with `_sift_down`

1. If empty, raise `IndexError`
2. Swap the root with the last item
3. Remove the last item (old root) and save it
4. Call `_sift_down(0)` to fix the heap
5. Return the saved value

```python
print(h.pop())    # 1
print(h.pop())    # 3
print(h.pop())    # 5
print(h.pop())    # 8
```

Items must come out in sorted (ascending) order.

---

### Step 4 — Verify against Python's `heapq`

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

assert my_result == ref_result, f"Mismatch!\nMine: {my_result}\nRef: {ref_result}"
print("Heap verified:", my_result)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### Step 5 — `PriorityQueue` class

Build a `PriorityQueue` on top of `MinHeap`. Store `(priority, item)` tuples.

```python
class PriorityQueue:
    def __init__(self):
        self._heap = MinHeap()

    def push(self, priority, item):
        self._heap.push((priority, item))

    def pop(self):
        priority, item = self._heap.pop()
        return item

    def peek(self):
        priority, item = self._heap.peek()
        return item

    def is_empty(self):
        return self._heap.is_empty()
```

Test it:
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

---

### Step 6 — Hospital triage demo

```python
def triage_demo():
    er = PriorityQueue()
    er.push(1, "Cardiac arrest")
    er.push(3, "Sprained ankle")
    er.push(2, "Broken arm")
    er.push(1, "Severe bleeding")
    er.push(3, "Mild headache")
    er.push(2, "Possible fracture")

    print("=== Emergency Room Triage ===")
    while not er.is_empty():
        patient = er.pop()
        print(f"Treating next: {patient}")

triage_demo()
```

Expected: cardiac arrest and severe bleeding go first (priority 1), then broken arm and possible fracture (priority 2), then the others (priority 3).

---

### Checklist Before Submitting

- [ ] `MinHeap.push()` maintains the heap property (smallest at index 0)
- [ ] `MinHeap.pop()` always removes and returns the smallest item
- [ ] `MinHeap.peek()` and `pop()` raise `IndexError` on an empty heap
- [ ] The `heapq` verification assertion passes
- [ ] `PriorityQueue.push()` and `pop()` work correctly (lowest number = first out)
- [ ] Two items with the same priority can both be stored
- [ ] `triage_demo()` prints patients in priority order (1s before 2s before 3s)
