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
