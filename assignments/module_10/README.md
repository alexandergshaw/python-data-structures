# Week 10 — Trees
### Binary Search Trees, Traversals, Height, and Deletion

---

## Welcome!

All the data structures you've used so far have been linear — one thing after another in a row. Trees break that pattern. They're **hierarchical** — like a family tree, a company org chart, or the folder structure on your computer. This week you build a Binary Search Tree (BST), one of the most important structures in computer science.

---

## Concept 1: What Is a Tree?

A tree is made of **nodes** connected by **edges**, where one node is the **root** (the starting point at the top) and everything branches downward.

```
          8          ← root
        /   \
       3     10
      / \      \
     1   6      14
        / \
       4   7
```

**Key vocabulary:**
- **Root** — the top node (8 in this example). Has no parent.
- **Leaf** — a node with no children (1, 4, 7, 14 here)
- **Parent/Child** — 3 is the parent of 1 and 6. 1 and 6 are children of 3.
- **Height** — the number of edges on the longest path from root to a leaf. This tree has height 3.

**Analogy:** A family tree. The great-grandparent is the root. Each generation branches down. Leaves are people with no children in the tree.

---

## Concept 2: Binary Search Tree (BST) — The Magic Property

A **binary** tree means each node has at most **two** children (left and right).

A **binary search tree** adds one powerful rule:
- Everything in the **left subtree** of a node is **smaller** than that node
- Everything in the **right subtree** is **larger**

This rule applies to **every** node, not just the root.

**Why does this matter?** Because of this rule, you can search the tree efficiently. You never have to check the left side if the value you want is bigger than the current node. You eliminate half the tree with each step — just like binary search!

---

## Concept 3: Node and BST Setup

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None    # Smaller values go left
        self.right = None   # Larger values go right

class BinarySearchTree:
    def __init__(self):
        self.root = None    # Empty tree
```

---

## Concept 4: Inserting Values

When you insert a value, you follow the BST rule to find where it belongs:
- If value < current node → go left
- If value > current node → go right
- Keep going until you find an empty spot (`None`) → put it there

**Analogy:** You're filing papers alphabetically. You look at the divider in the middle. Your paper comes before it? Go left half. After it? Go right half. Keep dividing until you find the right empty slot.

```python
def insert(self, value):
    if self.root is None:
        self.root = TreeNode(value)
    else:
        self._insert_helper(self.root, value)

def _insert_helper(self, node, value):
    if value < node.value:
        if node.left is None:
            node.left = TreeNode(value)   # Found the spot
        else:
            self._insert_helper(node.left, value)   # Keep going left
    else:
        if node.right is None:
            node.right = TreeNode(value)
        else:
            self._insert_helper(node.right, value)
```

---

## Concept 5: Searching

Same idea as inserting — follow the BST property to navigate:

```python
def search(self, value):
    return self._search_helper(self.root, value)

def _search_helper(self, node, value):
    if node is None:
        return False              # Fell off the tree — not found
    if value == node.value:
        return True               # Found it!
    elif value < node.value:
        return self._search_helper(node.left, value)
    else:
        return self._search_helper(node.right, value)
```

---

## Concept 6: Three Ways to Visit Every Node (Traversals)

**In-order (Left → Node → Right):** Visits nodes in **sorted order** — this is the useful one for BSTs!

**Pre-order (Node → Left → Right):** Visit the root first.

**Post-order (Left → Right → Node):** Visit the root last.

```python
def inorder(self, node, result):
    if node:
        self.inorder(node.left, result)    # Go left first
        result.append(node.value)          # Visit this node
        self.inorder(node.right, result)   # Then go right
```

After in-order traversal of the example tree: `[1, 3, 4, 6, 7, 8, 10, 14]` — perfectly sorted!

**Level-order (Breadth-First):** Visit all nodes on the same level before going deeper. Uses a queue.

---

## Concept 7: Height, Minimum, Maximum

- **Height** = the longest path from root to any leaf. A single node has height 0. An empty tree has height -1.
- **Minimum** = always the **leftmost** node (follow left pointers until there's no more left)
- **Maximum** = always the **rightmost** node

---

## Concept 8: Deletion (The Tricky One)

Three cases:

1. **Deleting a leaf** — just remove it
2. **Deleting a node with one child** — replace it with its child
3. **Deleting a node with two children** — find the **in-order successor** (the smallest value in the right subtree), copy its value to the current node, then delete the successor

**Analogy for case 3:** You're removing someone from the middle of a sorted roster. You need someone to take their spot. The best candidate is the person who should come right after them alphabetically — that's the in-order successor.

---

## Assignment Instructions

**File to create:** `module_10/bst.py`

Build a complete BST step by step. Test after each step before moving on.

---

### Step 1 — Define `TreeNode` and `BinarySearchTree`

`TreeNode` has `value`, `left = None`, `right = None`.

`BinarySearchTree` has `self.root = None`.

---

### Step 2 — `insert(value)`

Insert values while respecting the BST property.

```python
bst = BinarySearchTree()
for v in [8, 3, 10, 1, 6, 14, 4, 7]:
    bst.insert(v)
```

After inserting all of these, the tree should look like the diagram at the top of this README.

---

### Step 3 — `search(value)`

Return `True` if the value exists, `False` if not.

```python
print(bst.search(6))     # True
print(bst.search(5))     # False
print(bst.search(14))    # True
print(bst.search(100))   # False
```

---

### Step 4 — `inorder()`, `preorder()`, `postorder()`

Each returns a list. Use `result = []` and pass it into a recursive helper.

```python
print(bst.inorder())    # [1, 3, 4, 6, 7, 8, 10, 14]  ← must be sorted!
print(bst.preorder())   # [8, 3, 1, 6, 4, 7, 10, 14]
print(bst.postorder())  # [1, 4, 7, 6, 3, 14, 10, 8]
```

If `inorder()` is not sorted, your `insert()` has a bug.

---

### Step 5 — `level_order()`

Use `collections.deque` as a queue. Start with the root. Dequeue a node, add its value to results, enqueue its children (if any). Repeat.

```python
print(bst.level_order())   # [8, 3, 10, 1, 6, 14, 4, 7]
```

---

### Step 6 — `height()`

Return the height of the tree. Write a recursive helper that returns `-1` for `None` nodes and `1 + max(left_height, right_height)` for any real node.

```python
print(bst.height())   # 3
```

---

### Step 7 — `minimum()` and `maximum()`

Walk left to find the minimum. Walk right for the maximum. Raise `ValueError` if the tree is empty.

```python
print(bst.minimum())   # 1
print(bst.maximum())   # 14
```

---

### Step 8 — `delete(value)`

Handle all three cases described above. The hardest case:

For a node with two children:
1. Find the smallest value in the **right subtree** (keep going left from the right child)
2. Copy that value into the current node
3. Delete that smallest node from the right subtree

```python
bst.delete(3)
print(bst.inorder())   # [1, 4, 6, 7, 8, 10, 14]  — 3 is gone, structure maintained

bst.delete(8)          # Deleting the root!
print(bst.inorder())   # [1, 4, 6, 7, 10, 14]
```

---

### Step 9 — `__str__()` sideways tree display

Implement a `__str__` that prints the tree sideways — right subtree at top, root in middle, left at bottom — with indentation showing depth. Each level adds 4 more spaces.

```
        14
    10
8
        7
    6
        4
    3
        1
```

Hint: do a reverse in-order traversal (right → node → left) and pass an `indent` counter that increases by 1 per level.

---

### Step 10 — Edge case tests

Add these to `main()`:
```python
empty_bst = BinarySearchTree()
print(empty_bst.search(5))    # False — not Found in empty tree

single = BinarySearchTree()
single.insert(42)
print(single.height())         # 0
print(single.minimum())        # 42
print(single.maximum())        # 42
single.delete(42)
print(single.search(42))       # False
```

---

### Checklist Before Submitting

- [ ] `insert()` maintains the BST property — in-order always returns sorted list
- [ ] `search()` returns `True`/`False` correctly
- [ ] `inorder()` returns values in sorted order
- [ ] `preorder()` and `postorder()` return values in correct order
- [ ] `level_order()` returns values level by level using a queue
- [ ] `height()` returns -1 for empty, 0 for single node
- [ ] `minimum()` and `maximum()` raise `ValueError` on empty tree
- [ ] `delete()` handles leaf, one-child, and two-children cases
- [ ] `__str__()` shows the tree sideways with correct indentation
- [ ] Edge case tests are present and pass
