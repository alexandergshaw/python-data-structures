# Week 16 — Final Capstone

Congratulations on reaching the final week! The capstone project asks you to apply **multiple data structures and algorithms together** to build a realistic, non-trivial system. There is no single right answer — your goal is to make thoughtful design decisions, implement them correctly, and explain your reasoning.

---

## Project Options

Choose **one** of the following projects (or propose your own, with instructor approval):

| Option | Project                     | Core concepts used                                                     |
|--------|-----------------------------|------------------------------------------------------------------------|
| A      | Campus Navigation System    | Graphs, BFS/DFS, Dijkstra's shortest path, priority queues             |
| B      | Task Management System      | Priority queues (heaps), hash tables, sorting, linked lists            |
| C      | Text Analyzer               | Hash tables, sorting, dynamic programming, searching                   |

---

## Option A — Campus Navigation System

Model a campus as a **weighted graph** where nodes are buildings and edges are paths with distances. Your system should:

1. **Store the campus map** using an adjacency list with edge weights.
2. **Find the shortest path** between any two buildings using Dijkstra's algorithm.
3. **List all reachable buildings** from a given starting point (BFS or DFS).
4. **Find the minimum spanning tree** of the campus (Prim's algorithm) — the cheapest way to connect all buildings with walkways.

**Stretch goal:** Let users add new buildings or paths interactively.

---

## Option B — Task Management System

Build a system for managing tasks with priorities and deadlines. Your system should:

1. **Add tasks** with a name, priority, and deadline. Store them in a **min-heap** (priority queue) so the most urgent task is always accessible in O(1).
2. **Look up tasks by name** using a **hash table** for O(1) average lookup.
3. **List all tasks** sorted by priority, then by deadline (use a stable sort).
4. **Complete (remove) the highest-priority task** and display it.
5. **Search for tasks** matching a keyword in their name (linear search or binary search on a sorted list).

**Stretch goal:** Support task categories; use a dictionary of heaps, one per category.

---

## Option C — Text Analyzer

Analyze a piece of text and extract insights. Your system should:

1. **Count word frequencies** using a hash table. Display the top 10 most common words.
2. **Detect repeated phrases** (n-grams) — find all 2-word or 3-word sequences and count their occurrences.
3. **Find the longest common subsequence** between two paragraphs (DP).
4. **Sort words** alphabetically and by frequency (demonstrate at least two sorting algorithms).
5. **Search** for a word in a sorted word list using binary search.

**Stretch goal:** Compute readability statistics (average sentence length, unique word count, etc.).

---

## Design Guidelines

### Choose Data Structures Intentionally

For each piece of data your system stores, ask:
- Do I need fast lookup by key? → **Hash table / dictionary**
- Do I always need the min or max? → **Heap / priority queue**
- Do I need to process items in order? → **Queue (BFS) or Stack (DFS)**
- Do I need ordered traversal? → **BST or sorted list**
- Do I need to track connections between items? → **Graph**

Document your choices in comments or a short design section at the top of your file.

### Complexity Matters

For each major operation, state its time complexity. Your instructor will ask: "Why did you choose this data structure over a simpler list?" Be ready to answer with Big O.

### Error Handling

Real systems handle bad input gracefully:
- What happens if the user searches for a building that doesn't exist?
- What happens if they try to complete a task from an empty queue?
- Handle these cases with clear error messages, not crashes.

---

## Suggested File Structure

```
module 16/
├── main.py          # Entry point / menu / demo
├── graph.py         # (Option A) Graph class with BFS, DFS, Dijkstra, Prim
├── heap.py          # (Option B) MinHeap / PriorityQueue class
├── hash_table.py    # (Option B/C) HashTable class
├── text_analysis.py # (Option C) Analysis functions
└── README.md        # This file
```

---

## Hints for the Capstone

- **Start simple, then expand.** Get a basic working version before adding features. A working MVP beats a half-finished ambitious design.
- **Test each component in isolation first.** Verify your graph, heap, or hash table works before connecting them.
- **Don't reinvent wheels unnecessarily.** Use Python's `heapq`, `collections.deque`, and `dict` where appropriate — you've already implemented them from scratch in earlier weeks.
- **Write a `main()` function** that demonstrates all features with example data. Your instructor should be able to run `python3 main.py` and see the system working without any setup.
- **Comment your Big O complexity** next to each method — this shows you understand the trade-offs, not just the implementation.
- **Think about edge cases:** empty inputs, single-node graphs, ties in priority, very long text files.
- Review Weeks 6–15 if you need a refresher on any data structure or algorithm — your implementation from those modules is a great starting point.

---

## What a Strong Submission Looks Like

- [ ] At least **3 different data structures** are used meaningfully (not just `list` everywhere).
- [ ] At least **2 algorithms** are implemented and applied (search, sort, graph traversal, DP, etc.).
- [ ] Every major method has a comment stating its **time complexity**.
- [ ] The program runs end-to-end with **no uncaught exceptions** on valid input.
- [ ] **Edge cases** are handled gracefully.
- [ ] The code is organized into **classes or modules** (not one giant function).
- [ ] A short design explanation (can be in comments at the top of `main.py`) describes your choices.
