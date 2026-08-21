# Week 12 — Hash Tables

A **hash table** (also called a hash map or dictionary) is one of the most powerful and widely used data structures. It achieves near-instant lookup, insertion, and deletion — on average O(1) — by using a **hash function** to convert keys into array indices.

---

## Concepts Covered

### 1. Hash Functions

A **hash function** takes a key and returns an integer (the hash value). You use that integer as an index into an array.

```python
def hash_function(key, size):
    return hash(key) % size   # Python's built-in hash(), mod table size
```

Properties of a good hash function:
- **Deterministic:** Same key always produces the same hash.
- **Uniform distribution:** Hashes spread evenly across the table to minimize clustering.
- **Fast:** Computing the hash should be O(1).

---

### 2. Basic Structure

A hash table is backed by a fixed-size array. Each slot in the array is called a **bucket**.

```python
class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [None] * size   # Array of buckets

    def _hash(self, key):
        return hash(key) % self.size
```

---

### 3. Collisions

A **collision** occurs when two different keys hash to the same index. Collisions are inevitable (pigeonhole principle) — the key is handling them gracefully.

---

### 4. Separate Chaining

Each bucket holds a **list** (chain) of all key-value pairs that hash to that index:

```python
class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]   # List of lists

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value   # Update existing key
                return
        self.buckets[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)
```

---

### 5. Linear Probing (Open Addressing)

Instead of chaining, store all entries in the array itself. If a bucket is occupied, scan forward until you find an empty slot:

```python
def put(self, key, value):
    index = self._hash(key)
    while self.buckets[index] is not None:
        if self.buckets[index][0] == key:
            self.buckets[index] = (key, value)   # Update
            return
        index = (index + 1) % self.size          # Probe next slot
    self.buckets[index] = (key, value)
```

---

### 6. Tombstones

When you **delete** an entry in an open-addressing table, you cannot simply set the slot to `None` — that would break probe chains for other keys. Instead, mark it with a **tombstone** sentinel:

```python
DELETED = object()   # Unique sentinel

def delete(self, key):
    index = self._hash(key)
    while self.buckets[index] is not None:
        if self.buckets[index] is not DELETED and \
           self.buckets[index][0] == key:
            self.buckets[index] = DELETED
            return
        index = (index + 1) % self.size
```

During a `get`, skip tombstone slots (keep probing); during a `put`, you can reuse them.

---

### 7. Load Factor and Resizing

The **load factor** is `n / size` (number of entries ÷ table size).

- A high load factor (> 0.7) means more collisions and slower performance.
- When the load factor exceeds a threshold, **resize** the table (typically double its size) and **rehash** all existing entries.

```python
def _load_factor(self):
    return self.count / self.size

def put(self, key, value):
    if self._load_factor() > 0.7:
        self._resize()
    # ... rest of put logic
```

---

## Hints for This Week's Assignment

- **Python's `dict` is a hash table.** When your assignment asks you to build one, implement it yourself — don't wrap `dict`. But do use `dict` to verify your results.
- Start with **separate chaining** — it's simpler. Move to linear probing after you have chaining working.
- For chaining, iterate the list in a bucket to check if the key already exists before appending — otherwise you'll end up with duplicate keys.
- For linear probing, be careful to handle the case where the table is full (all slots occupied) — add a guard or resize before inserting.
- Test thoroughly: insert duplicate keys (should update, not add), retrieve missing keys (should raise `KeyError` or return a default), and delete then re-insert.
- Python's built-in `hash()` function can return negative numbers — always `% self.size` to get a valid positive index.

---

## Assignment Instructions

**File to create:** `module_12/hash_table.py`

You will implement two versions of a hash table — one using separate chaining and one using linear probing — and compare them. Work through each step in order.

---

### Step 1 — `HashTableChaining` skeleton

Create a class `HashTableChaining` with:
- `self.size = 16` (default bucket count)
- `self.buckets = [[] for _ in range(self.size)]` — list of empty lists
- `self.count = 0` — number of stored key-value pairs
- `_hash(key)` — returns `hash(key) % self.size`

---

### Step 2 — `put(key, value)`

Insert or update a key-value pair:
1. Hash the key to find the bucket index.
2. Search the bucket list for an existing pair with the same key.
   - If found, **update** its value.
   - If not found, **append** `[key, value]` to the bucket and increment `self.count`.

```python
t = HashTableChaining()
t.put("name", "Alice")
t.put("age", 20)
t.put("name", "Bob")   # Update existing key
```

---

### Step 3 — `get(key)`

Search the correct bucket for a pair whose first element equals `key`. Return its value. Raise `KeyError(key)` if not found.

```python
print(t.get("name"))   # Bob
print(t.get("age"))    # 20
# t.get("gpa") → KeyError: 'gpa'
```

---

### Step 4 — `delete(key)`

Remove the pair with the given key from its bucket. Decrement `self.count`. Do nothing if the key is not found.

```python
t.delete("age")
# t.get("age") → KeyError
```

---

### Step 5 — `__str__()` and `load_factor()`

Add:
- `load_factor()` returning `self.count / self.size` (as a float)
- `__str__()` returning a readable summary showing non-empty buckets:

```
HashTable (16 buckets, 3 items, load=0.19):
  Bucket 2: [['city', 'NYC']]
  Bucket 7: [['name', 'Bob']]
  Bucket 11: [['score', 95]]
```

---

### Step 6 — `HashTableProbing` with linear probing

Create a **second class** `HashTableProbing` that stores entries in a flat array using linear probing.

Use a sentinel object `_EMPTY = object()` and `_DELETED = object()` to distinguish empty slots from deleted ones.

Implement:
- `put(key, value)` — find the slot (probe forward on collision), insert or update.
- `get(key)` — probe forward; skip `_DELETED` slots; raise `KeyError` if an `_EMPTY` slot is hit.
- `delete(key)` — find the slot and mark it `_DELETED` (tombstone).

```python
p = HashTableProbing(size=8)
p.put("a", 1)
p.put("b", 2)
p.put("c", 3)
print(p.get("b"))   # 2
p.delete("b")
# p.get("b") → KeyError
print(p.get("c"))   # 3  — probing still finds c correctly after b is deleted
```

---

### Step 7 — Collision demonstration

Show that your chaining implementation handles collisions gracefully:

1. Find two strings that hash to the same bucket in a size-8 table (trial-and-error is fine).
2. Insert both. Print the table to show both are stored in the same bucket.
3. Retrieve both and verify the correct values come back.

```python
# Example — find two keys that collide:
size = 8
keys = ["cat", "dog", "ant", "bee", "emu", "gnu", "hen", "jay", "koi"]
for k in keys:
    print(f"{k!r:8} → bucket {hash(k) % size}")
```

---

### Step 8 — Functional comparison

Run both hash table implementations with the same data and verify they return identical results:

```python
data = [("apple", 1), ("banana", 2), ("cherry", 3), ("date", 4), ("elderberry", 5)]

chain = HashTableChaining()
probe = HashTableProbing()
for k, v in data:
    chain.put(k, v)
    probe.put(k, v)

for k, _ in data:
    assert chain.get(k) == probe.get(k), f"Mismatch on key {k!r}"

print("Both implementations agree on all keys.")
```

---

### Checklist Before Submitting

- [ ] `HashTableChaining.put()` inserts new keys and updates existing ones.
- [ ] `HashTableChaining.get()` raises `KeyError` for missing keys.
- [ ] `HashTableChaining.delete()` removes the key; subsequent `get()` raises `KeyError`.
- [ ] `load_factor()` returns the correct float.
- [ ] `__str__()` shows non-empty buckets with their contents.
- [ ] `HashTableProbing` handles tombstone deletion correctly (`get()` still finds later keys).
- [ ] The collision demonstration shows two keys sharing a bucket.
- [ ] The comparison assertion passes for both implementations.
