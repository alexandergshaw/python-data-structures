# Week 16 — Final Capstone
### Bringing It All Together

---

## Welcome to the Final Week!

You've come a long way. You started with variables and print statements, and you now know linked lists, trees, graphs, heaps, hash tables, recursion, sorting, searching, and dynamic programming. The capstone project is your chance to prove you can combine these tools to build something real.

There is no single right answer this week. Your goal is to make smart design choices, implement them correctly, and explain your reasoning.

---

## What Makes This Different From Previous Assignments

Every previous assignment told you exactly what to build. This one gives you a **goal** and lets you decide how to get there. That's what real software development looks like.

You still have structure (the steps below), but there are decisions only you can make:
- Which data structure fits this need?
- Should I use BFS or DFS here?
- Is a hash table the right choice, or would a sorted list work better?

Start simple. Get something working. Then improve it.

---

## Choose Your Project

Pick **one** of the three options below. Read all three before deciding — pick the one that genuinely interests you.

---

## Option A — Campus Navigation System

**The idea:** Model a campus as a map. Buildings are nodes. Walking paths between them are edges with distances (in minutes). Your program lets a user find the fastest route between any two buildings.

**You must use:**
- A **Graph** (from Week 13) to store the campus map
- **Dijkstra's algorithm** (from Week 13) to find shortest paths
- **BFS** to list all buildings reachable from a starting point
- A **Priority Queue / Heap** (from Week 11) inside Dijkstra's

**Your program should:**

1. Build a campus graph with at least 8 buildings and realistic connections
2. Show the full map (print all buildings and their connections)
3. Ask the user for a start building and a destination
4. Find and display the shortest path:
   ```
   Shortest path from Library to Dorms:
   Library → Science Hall → Engineering → Dorms
   Total walking time: 11 minutes
   ```
5. List all buildings reachable from the starting point using BFS
6. Handle invalid building names gracefully (print an error, don't crash)

**Stretch goal:** Let the user add a new building or path interactively.

---

## Option B — Task Management System

**The idea:** A to-do list where tasks have priorities. The most urgent task is always served first. Users can add tasks, complete the top task, and search for tasks by name.

**You must use:**
- A **Min-Heap / Priority Queue** (from Week 11) to always serve the highest-priority task first
- A **Hash Table** (from Week 12) for O(1) lookup by task name
- **Sorting** (from Week 9) to display tasks in different orders

**Your program should:**

1. Let the user add a task with: name, priority (1=urgent, 2=normal, 3=low), and a short description
2. Show all tasks sorted by priority, then by name
3. Complete (pop) the highest-priority task and display it
4. Search for a task by name (use the hash table)
5. Count tasks by priority level
6. Handle edge cases: completing from an empty queue, searching for a task that doesn't exist

**Stretch goal:** Add task categories (e.g., "Work," "Personal"). Use a dictionary of queues — one per category.

---

## Option C — Text Analyzer

**The idea:** Feed your program a paragraph (or a few sentences) and it tells you interesting things about the text.

**You must use:**
- A **Hash Table / dict** (from Week 12) for word frequency counting
- **Sorting** (from Week 9) to rank words by frequency
- **Binary Search** (from Week 9) to search for a word in a sorted word list
- **LCS** (from Week 15) to compare two blocks of text

**Your program should:**

1. Accept a text string (hardcode a paragraph for demo purposes)
2. Count how many times each word appears (case-insensitive, ignoring punctuation)
3. Display the top 10 most common words
4. Display the 10 least common words
5. Count total words, unique words, and average word length
6. Search for a specific word using binary search on a sorted word list
7. Compare two paragraphs and output their longest common subsequence (LCS) length
8. Display a simple readability report

**Stretch goal:** Count 2-word phrases (bigrams) and display the top 5.

---

## Design Guidelines — Read These Carefully

### Choose Your Data Structures Deliberately

For every piece of data you store, ask yourself:

| Need | Use |
|------|-----|
| Fast lookup by name/key | Hash table / dict |
| Always need the min or max quickly | Heap / Priority Queue |
| Process items in arrival order | Queue |
| Process in reverse order / undo | Stack |
| Ordered traversal / range queries | BST |
| Connections between things | Graph |
| Many items, frequent search | Sorted list + binary search |

Write a comment above each data structure explaining why you chose it.

### State Your Complexity

For every major method, add a one-line comment stating its time complexity. Example:

```python
def add_task(self, task):
    # O(log n) — heap insertion
    self._heap.push(task.priority, task)
```

Your instructor **will** ask: "Why did you use a hash table here instead of a list?" Be ready with a Big O answer.

### Handle Bad Input Gracefully

Real programs don't crash on bad input — they explain what went wrong:

```
Enter a building name: cafeteria
Error: 'cafeteria' is not in the campus map.
Available buildings: Library, Science Hall, Engineering, Dorms, ...
```

### Organize Your Code

Use classes. Don't put everything in one giant `main()` function.

```
module_16/
├── main.py          ← entry point, menu, demo
├── graph.py         ← (Option A) Graph class
├── heap.py          ← (Option A/B) MinHeap, PriorityQueue
├── hash_table.py    ← (Option B/C) HashTable class
└── text_utils.py    ← (Option C) analysis functions
```

---

## Step-by-Step Approach

Don't try to build everything at once. Use this order:

**Phase 1 — Core data structure (Day 1)**
Build and test the main data structure your project depends on (Graph, Heap, or HashTable). Use your implementations from earlier weeks as a starting point.

**Phase 2 — Core algorithm (Day 2)**
Implement the main algorithm (Dijkstra's, priority-based dispatch, or frequency counting). Test it with small, known inputs where you can verify the answer by hand.

**Phase 3 — User interface (Day 3)**
Add the `main()` menu/demo that ties everything together. This is where you print results and handle user input.

**Phase 4 — Edge cases and polish (Day 4)**
What happens if the user inputs something invalid? What if a structure is empty? Handle all the error cases.

---

## What a Strong Submission Looks Like

- [ ] At least **3 different data structures** are used meaningfully (not just `list` everywhere)
- [ ] At least **2 algorithms** are implemented and applied (search, sort, graph traversal, DP, etc.)
- [ ] Every major method has a **time complexity comment**
- [ ] The program runs end-to-end with **no crashes** on valid input
- [ ] **Invalid input** is handled with a helpful error message
- [ ] Code is organized into **classes or separate functions** — no single 200-line function
- [ ] A short **design explanation** at the top of `main.py` describes your choices in plain English
- [ ] You can answer the question: "Why did you use a [data structure] for [this feature]?"

---

## A Note on Using Your Previous Work

You spent 15 weeks building data structures from scratch. **You may and should reuse your own implementations** from previous modules. Copy `MinHeap` from module 11, `Graph` from module 13, etc. This is not cheating — this is how real software is built. Code you write once should be reusable.

If you want to use Python's built-in `heapq` or `dict` for simplicity, that's also fine — but be ready to explain the trade-off compared to your custom implementation.

---

## Good Luck!

You've learned an enormous amount in 16 weeks. This capstone is your chance to show it. Build something you're proud of. Ask for help early if you're stuck — that's what your instructor is there for.
