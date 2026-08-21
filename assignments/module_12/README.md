# Week 12 — Hash Tables
### Hash Functions, Collisions, Chaining, Probing, and Resizing

---

## Welcome!

Python's `dict` is the most useful data structure in the language. This week you learn exactly how it works by building one yourself. The secret is a **hash table** — a structure that can store and retrieve data in O(1) time on average, no matter how big it gets.

---

## Concept 1: The Core Idea

Imagine you have 1,000 lockers numbered 0 to 999. Each person gets assigned a locker number based on their name using a formula. To find someone's stuff later, you just run the same formula on their name → get the locker number → open that locker. No searching required.

That formula is a **hash function**. The row of lockers is the **array** backing the hash table.

---

## Concept 2: Hash Functions

A hash function takes a **key** (like a string or number) and returns an integer that becomes the index into the array.

```python
def _hash(self, key):
    return hash(key) % self.size
    # hash() is Python's built-in — works on strings, numbers, tuples
    # % self.size keeps the result in range [0, size-1]
```

A good hash function:
- Always gives the **same output** for the same input (deterministic)
- Spreads keys **evenly** across all slots (avoids everything piling up in one place)
- Runs **fast** — O(1)

⚠️ Python's `hash()` can return negative numbers. Always `% self.size` to get a valid positive index.

---

## Concept 3: Collisions — When Two Keys Get the Same Locker

Even with a great hash function, two different keys will sometimes hash to the same index. This is called a **collision**.

**Analogy:** You and a classmate both get assigned locker #42. There's a conflict. You need a plan for handling it.

There are two main strategies:

---

## Concept 4: Strategy 1 — Separate Chaining

Each "locker" (bucket) doesn't hold just one item — it holds a **list** of items. If two keys hash to the same index, they both go in that list.

```
Bucket 0: []
Bucket 1: [["apple", 1]]
Bucket 2: [["name", "Alex"], ["city", "NYC"]]   ← two items in same bucket!
Bucket 3: [["score", 95]]
```

```python
class HashTableChaining:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]   # List of empty lists
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value    # Key exists — update it
                return
        self.buckets[index].append([key, value])   # New key — add it
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)        # Key not found
```

---

## Concept 5: Strategy 2 — Linear Probing (Open Addressing)

Instead of lists in each bucket, every item lives directly in the main array. If a slot is taken, you **probe** (try) the next slot, then the next, until you find an empty one.

**Analogy:** You arrive at a parking lot and your assigned spot is taken. You drive to the next spot. Taken again? Next one. Until you find an open space.

```python
def put(self, key, value):
    index = self._hash(key)
    while self.buckets[index] is not None:
        if self.buckets[index][0] == key:
            self.buckets[index] = (key, value)   # Update existing
            return
        index = (index + 1) % self.size          # Probe next slot
    self.buckets[index] = (key, value)
```

---

## Concept 6: Tombstones — The Deletion Problem

With linear probing, you can't just set a deleted slot to `None`. If you do, future lookups for keys that were inserted past that slot will stop too early and return "not found" incorrectly.

**Solution:** Mark deleted slots with a special **tombstone** value. During lookups, you skip tombstones (keep probing). During insertions, you can reuse tombstone slots.

**Analogy:** In that parking lot, a spot marked with an orange cone means "temporarily out of service — skip me but keep looking." It's different from an empty spot (stop and park here).

```python
_DELETED = object()    # A unique sentinel — nothing else equals this

def delete(self, key):
    index = self._hash(key)
    while self.buckets[index] is not None:
        if self.buckets[index] is not _DELETED and self.buckets[index][0] == key:
            self.buckets[index] = _DELETED    # Mark with tombstone
            self.count -= 1
            return
        index = (index + 1) % self.size
```

---

## Concept 7: Load Factor and Resizing

The **load factor** is `number of items / array size`. When it gets too high (usually above 0.7), the table becomes crowded and performance degrades.

The fix: **double the size** of the array and re-insert everything (rehash). This keeps the load factor low.

```python
def _load_factor(self):
    return self.count / self.size

def put(self, key, value):
    if self._load_factor() > 0.7:
        self._resize()     # Double the table before inserting
    # ... rest of put
```

---

## Assignment Instructions

**File to create:** `module_12/hash_table.py`

---

### Step 1 — `HashTableChaining` skeleton and `_hash`

```python
class HashTableChaining:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size
```

---

### Step 2 — `put(key, value)`

Search the bucket at `_hash(key)`. If the key already exists, update its value. Otherwise, append `[key, value]` to the bucket and increment `count`.

---

### Step 3 — `get(key)`

Search the bucket. Return the value if found. Raise `KeyError(key)` if not.

```python
t = HashTableChaining()
t.put("name", "Alice")
t.put("age", 20)
t.put("name", "Bob")     # Update existing key
print(t.get("name"))     # Bob
print(t.get("age"))      # 20
# t.get("gpa")  →  KeyError: 'gpa'
```

---

### Step 4 — `delete(key)`

Remove the pair from its bucket. Decrement `count`. Do nothing if key not found.

```python
t.delete("age")
# t.get("age")  →  KeyError
```

---

### Step 5 — `load_factor()` and `__str__()`

```python
def load_factor(self):
    return self.count / self.size
```

`__str__` should show non-empty buckets:
```
HashTable (16 buckets, 2 items, load=0.13):
  Bucket 7: [['name', 'Bob']]
  Bucket 11: [['score', 95]]
```

---

### Step 6 — `HashTableProbing` with linear probing

Create a second class that uses linear probing. Use `_EMPTY = None` and `_DELETED = object()` as sentinels.

Implement `put`, `get`, and `delete` using the probing logic described above.

```python
p = HashTableProbing(size=8)
p.put("a", 1)
p.put("b", 2)
p.put("c", 3)
print(p.get("b"))    # 2
p.delete("b")
print(p.get("c"))    # 3 — still works after tombstone!
# p.get("b")  →  KeyError
```

---

### Step 7 — Show a collision happening

Find two keys that hash to the same bucket in a size-8 table. This is easiest by brute force:

```python
size = 8
test_keys = ["cat", "dog", "ant", "bee", "emu", "gnu", "hen", "jay", "koi", "owl"]
for k in test_keys:
    print(f"{k!r:8} → bucket {hash(k) % size}")
```

Identify two that share a bucket. Insert both into `HashTableChaining`, then retrieve both and verify they're stored correctly.

---

### Step 8 — Compare both implementations

```python
data = [("apple", 1), ("banana", 2), ("cherry", 3), ("date", 4), ("elderberry", 5)]

chain = HashTableChaining()
probe = HashTableProbing()
for k, v in data:
    chain.put(k, v)
    probe.put(k, v)

for k, _ in data:
    assert chain.get(k) == probe.get(k), f"Mismatch on {k!r}"

print("Both implementations return the same values for all keys.")
```

---

### Checklist Before Submitting

- [ ] `HashTableChaining.put()` inserts new keys and updates existing ones
- [ ] `HashTableChaining.get()` raises `KeyError` for missing keys
- [ ] `HashTableChaining.delete()` removes keys; later `get()` raises `KeyError`
- [ ] `load_factor()` returns the correct float
- [ ] `__str__()` shows non-empty buckets with their contents
- [ ] `HashTableProbing` uses tombstones for deletion and still finds later keys
- [ ] Collision demonstration shows two keys in the same bucket
- [ ] Comparison assertion passes for both implementations
