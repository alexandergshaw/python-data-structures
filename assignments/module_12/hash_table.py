_EMPTY = None
_DELETED = object()


class HashTableChaining:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1

    def get(self, key):
        for stored_key, value in self.buckets[self._hash(key)]:
            if stored_key == key:
                return value
        raise KeyError(key)

    def delete(self, key):
        bucket = self.buckets[self._hash(key)]
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[index]
                self.count -= 1
                return

    def load_factor(self):
        return self.count / self.size

    def __str__(self):
        lines = [f"HashTable ({self.size} buckets, {self.count} items, load={self.load_factor():.2f}):"]
        lines.extend(f"  Bucket {i}: {bucket}" for i, bucket in enumerate(self.buckets) if bucket)
        return "\n".join(lines)


class HashTableProbing:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [_EMPTY] * size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index, first_deleted = self._hash(key), None
        for _ in range(self.size):
            pair = self.buckets[index]
            if pair is _EMPTY:
                slot = first_deleted if first_deleted is not None else index
                self.buckets[slot] = (key, value)
                self.count += 1
                return
            if pair is _DELETED:
                if first_deleted is None:
                    first_deleted = index
            elif pair[0] == key:
                self.buckets[index] = (key, value)
                return
            index = (index + 1) % self.size
        if first_deleted is not None:
            self.buckets[first_deleted] = (key, value)
            self.count += 1
            return
        raise OverflowError("Hash table is full")

    def get(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            pair = self.buckets[index]
            if pair is _EMPTY:
                break
            if pair is not _DELETED and pair[0] == key:
                return pair[1]
            index = (index + 1) % self.size
        raise KeyError(key)

    def delete(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            pair = self.buckets[index]
            if pair is _EMPTY:
                return
            if pair is not _DELETED and pair[0] == key:
                self.buckets[index] = _DELETED
                self.count -= 1
                return
            index = (index + 1) % self.size


def main():
    size = 8
    by_bucket = {}
    sample_keys = ["cat", "dog", "ant", "bee", "emu", "gnu", "hen", "jay", "koi", "owl"]
    for key in sample_keys:
        by_bucket.setdefault(hash(key) % size, []).append(key)
    collision = next((keys[:2] for keys in by_bucket.values() if len(keys) >= 2), None)
    if collision is None:
        for i in range(1000):
            key = f"key-{i}"
            bucket = by_bucket.setdefault(hash(key) % size, [])
            bucket.append(key)
            if len(bucket) >= 2:
                collision = bucket[:2]
                break
    first, second = collision
    chain = HashTableChaining(size)
    chain.put(first, 1)
    chain.put(second, 2)
    assert chain.get(first) == 1 and chain.get(second) == 2
    print(f"Collision: {first!r} and {second!r} share bucket {hash(first) % size}")

    data = [("apple", 1), ("banana", 2), ("cherry", 3), ("date", 4), ("elderberry", 5)]
    chain, probe = HashTableChaining(), HashTableProbing()
    for key, value in data:
        chain.put(key, value)
        probe.put(key, value)
    for key, _ in data:
        assert chain.get(key) == probe.get(key), f"Mismatch on {key!r}"
    print("Both implementations return the same values for all keys.")


if __name__ == "__main__":
    main()
