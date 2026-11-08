from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self._data[-1]

    def is_empty(self):
        return not self._data

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Stack (top → bottom): {list(reversed(self._data))}"


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._data.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self._data[0]

    def is_empty(self):
        return not self._data

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Queue (front → back): [{', '.join(map(str, self._data))}]"


def is_balanced(text):
    stack = Stack()
    matching = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in matching:
            if stack.is_empty() or stack.peek() != matching[char]:
                return False
            stack.pop()
    return stack.is_empty()


def print_queue_demo():
    queue = Queue()
    for job in ["Report.pdf", "Photo.png", "Letter.docx", "Invoice.pdf", "Notes.txt"]:
        queue.enqueue(job)
    print(queue)
    while not queue.is_empty():
        print(f"Printing: {queue.dequeue()}")
    print(f"All jobs done. Queue empty: {queue.is_empty()}")


def do_action(action, undo_stack, redo_stack):
    undo_stack.push(action)
    redo_stack._data.clear()


def undo(undo_stack, redo_stack):
    if undo_stack.is_empty():
        return None
    action = undo_stack.pop()
    redo_stack.push(action)
    return action


def redo(undo_stack, redo_stack):
    if redo_stack.is_empty():
        return None
    action = redo_stack.pop()
    undo_stack.push(action)
    return action


def undo_redo_demo():
    undo_stack, redo_stack = Stack(), Stack()
    for action in ["Type 'Hello'", "Bold text", "Insert image"]:
        do_action(action, undo_stack, redo_stack)
    print("Undo:", undo(undo_stack, redo_stack))
    print("Undo:", undo(undo_stack, redo_stack))
    print("Redo:", redo(undo_stack, redo_stack))
    print("Undo:", undo(undo_stack, redo_stack))


if __name__ == "__main__":
    print_queue_demo()
    undo_redo_demo()
