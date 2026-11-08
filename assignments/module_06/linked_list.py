class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values, current = [], self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " → ".join(values + ["None"])

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def prepend(self, value):
        node = Node(value)
        node.next, self.head = self.head, node

    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def length(self):
        count, current = 0, self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node
        self.head = prev


def main():
    history = LinkedList()
    for page in ["google.com", "github.com", "stackoverflow.com", "python.org"]:
        history.prepend(page)
    print("History:", history)
    history.delete("github.com")
    print("After removing github.com:", history)
    print("Pages visited:", history.length())


if __name__ == "__main__":
    main()
