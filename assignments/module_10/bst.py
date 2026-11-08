from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def add(node):
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    add(node.left)
            elif value > node.value:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    add(node.right)
        if self.root is None:
            self.root = TreeNode(value)
        else:
            add(self.root)

    def search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def _traverse(self, order):
        result = []
        def walk(node):
            if node is None:
                return
            if order == "pre":
                result.append(node.value)
            walk(node.left)
            if order == "in":
                result.append(node.value)
            walk(node.right)
            if order == "post":
                result.append(node.value)
        walk(self.root)
        return result

    def inorder(self):
        return self._traverse("in")

    def preorder(self):
        return self._traverse("pre")

    def postorder(self):
        return self._traverse("post")

    def level_order(self):
        if self.root is None:
            return []
        queue, result = deque([self.root]), []
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def height(self):
        def get_height(node):
            return -1 if node is None else 1 + max(get_height(node.left), get_height(node.right))
        return get_height(self.root)

    def minimum(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def maximum(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def delete(self, value):
        def remove(node, target):
            if node is None:
                return None
            if target < node.value:
                node.left = remove(node.left, target)
            elif target > node.value:
                node.right = remove(node.right, target)
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.value = successor.value
                node.right = remove(node.right, successor.value)
            return node
        self.root = remove(self.root, value)

    def __str__(self):
        lines = []
        def display(node, depth):
            if node:
                display(node.right, depth + 1)
                lines.append("    " * depth + str(node.value))
                display(node.left, depth + 1)
        display(self.root, 0)
        return "\n".join(lines)


def main():
    bst = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14, 4, 7]:
        bst.insert(value)
    print(bst.inorder(), bst.preorder(), bst.postorder(), bst.level_order())
    print(bst.height(), bst.minimum(), bst.maximum())
    bst.delete(3)
    bst.delete(8)
    print(bst)
    empty = BinarySearchTree()
    print(empty.search(5))
    single = BinarySearchTree()
    single.insert(42)
    print(single.height(), single.minimum(), single.maximum())
    single.delete(42)
    print(single.search(42))


if __name__ == "__main__":
    main()
