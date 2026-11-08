import heapq


class MinHeap:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"MinHeap: {self._data}"

    def is_empty(self):
        return not self._data

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._data[0]

    def push(self, value):
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def _sift_up(self, index):
        while index:
            parent = (index - 1) // 2
            if self._data[index] >= self._data[parent]:
                break
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            index = parent

    def pop(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        smallest = self._data.pop()
        if self._data:
            self._sift_down(0)
        return smallest

    def _sift_down(self, index):
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            smallest = index
            if left < len(self._data) and self._data[left] < self._data[smallest]:
                smallest = left
            if right < len(self._data) and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == index:
                return
            self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
            index = smallest


class PriorityQueue:
    def __init__(self):
        self._heap = MinHeap()
        self._sequence = 0

    def push(self, priority, item):
        self._heap.push((priority, self._sequence, item))
        self._sequence += 1

    def pop(self):
        return self._heap.pop()[2]

    def peek(self):
        return self._heap.peek()[2]

    def is_empty(self):
        return self._heap.is_empty()


def triage_demo():
    er = PriorityQueue()
    for priority, patient in [(1, "Cardiac arrest"), (3, "Sprained ankle"),
                              (2, "Broken arm"), (1, "Severe bleeding"),
                              (3, "Mild headache"), (2, "Possible fracture")]:
        er.push(priority, patient)
    print("=== Emergency Room Triage ===")
    while not er.is_empty():
        print(f"Treating next: {er.pop()}")


def verify_heap():
    values = [9, 4, 7, 1, 8, 3, 6, 2, 5]
    mine, reference = MinHeap(), []
    for value in values:
        mine.push(value)
        heapq.heappush(reference, value)
    my_result = [mine.pop() for _ in values]
    ref_result = [heapq.heappop(reference) for _ in values]
    assert my_result == ref_result, f"Mismatch!\nMine: {my_result}\nRef: {ref_result}"
    print("Heap verified:", my_result)


if __name__ == "__main__":
    verify_heap()
    triage_demo()
