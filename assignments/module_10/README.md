# Week 10 — Trees

Trees are hierarchical data structures — perfect for representing relationships where things branch. A **binary search tree (BST)** keeps data sorted automatically, making search very fast. This week you build one from scratch.

---

## Concepts Covered

### 1. Tree Terminology

```
          8          ← root
        /   \
       3     10
      / \      \
     1   6      14
        / \
       4   7
```

| Term      | Definition                                                     |
|-----------|----------------------------------------------------------------|
| Root      | The topmost node (no parent)                                   |
| Leaf      | A node with no children                                        |
| Parent    | A node that has children                                       |
| Child     | A node directly below another                                  |
| Height    | The number of edges on the longest path from root to a leaf    |
| Subtree   | A node and all its descendants                                 |

---

### 2. Binary Search Tree Property

In a **BST**, for every node:
- All values in the **left subtree** are **less than** the node's value.
- All values in the **right subtree** are **greater than** the node's value.

This property holds for **every** node, not just the root.

---

### 3. Node and BST Classes

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
```

---

### 4. Insertion

Insert by following the BST property: go left if smaller, right if larger.

```python
def insert(self, value):
    if self.root is None:
        self.root = TreeNode(value)
        return
    self._insert_recursive(self.root, value)

def _insert_recursive(self, node, value):
    if value < node.value:
        if node.left is None:
            node.left = TreeNode(value)
        else:
            self._insert_recursive(node.left, value)
    else:
        if node.right is None:
            node.right = TreeNode(value)
        else:
            self._insert_recursive(node.right, value)
```

---

### 5. Search

Follow the same logic as insertion — go left or right until you find the value or reach `None`.

```python
def search(self, value):
    return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
    if node is None:
        return False
    if value == node.value:
        return True
    elif value < node.value:
        return self._search_recursive(node.left, value)
    else:
        return self._search_recursive(node.right, value)
```

Time complexity: **O(h)** where `h` is the tree height. In a balanced tree, h = log n.

---

### 6. Height, Minimum, and Maximum

```python
def height(self, node):
    if node is None:
        return -1    # empty tree height = -1, single node = 0
    return 1 + max(self.height(node.left), self.height(node.right))

def minimum(self, node):
    while node.left is not None:
        node = node.left    # Go as far left as possible
    return node.value

def maximum(self, node):
    while node.right is not None:
        node = node.right   # Go as far right as possible
    return node.value
```

---

### 7. Depth-First Traversals

Traversal means visiting every node in a specific order.

**In-order (Left → Root → Right):** Visits nodes in *sorted* order for a BST.

```python
def inorder(self, node, result=[]):
    if node:
        self.inorder(node.left, result)
        result.append(node.value)
        self.inorder(node.right, result)
    return result
```

**Pre-order (Root → Left → Right):** Root is visited first — useful for copying a tree.

**Post-order (Left → Right → Root):** Root is visited last — useful for deletion.

---

### 8. Breadth-First Traversal (Level Order)

Visit nodes level by level using a **queue**:

```python
from collections import deque

def level_order(self):
    if self.root is None:
        return []
    result = []
    queue = deque([self.root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

---

### 9. Tree Balancing (Concept)

A BST is **balanced** when its height is O(log n). In the worst case (inserting already-sorted values), a BST degenerates into a linked list with O(n) height and O(n) search time. Balanced BST variants (AVL trees, Red-Black trees) automatically maintain balance — you don't need to implement these, just understand why balance matters.

---

## Hints for This Week's Assignment

- **Draw the tree** as you insert values. Trace through insertions by hand before writing code.
- Almost every tree operation is naturally recursive — think: "what should I do at this node, and then recurse left/right."
- Always handle `node is None` first in recursive functions — this is the base case.
- In-order traversal of a BST produces a **sorted list**. Use this to verify your tree is correct.
- Height of a single node is 0, and height of an empty tree is -1 (or -∞). Be consistent in your choice.
- For deletion, the trickiest case is deleting a node with **two children** — replace it with its **in-order successor** (smallest node in its right subtree).
