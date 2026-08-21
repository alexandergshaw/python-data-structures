# Week 13 — Graphs

A **graph** is a collection of **nodes** (vertices) connected by **edges**. Graphs are the most general data structure you've seen — trees, linked lists, and even simple key-value maps are all special cases. They model networks, maps, social connections, dependencies, and much more.

---

## Concepts Covered

### 1. Graph Representations

#### Adjacency List

Each node maps to a list of its neighbors. This is the most common representation.

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
```

- Space: O(V + E) where V = vertices, E = edges.
- Best for **sparse** graphs (few edges relative to nodes).

#### Adjacency Matrix

A 2D array where `matrix[i][j] = 1` if there is an edge from node `i` to node `j`.

```python
# 0-indexed, 4 nodes
matrix = [
    [0, 1, 1, 0],  # node 0 connects to 1 and 2
    [1, 0, 0, 1],  # node 1 connects to 0 and 3
    [1, 0, 0, 1],  # node 2 connects to 0 and 3
    [0, 1, 1, 0],  # node 3 connects to 1 and 2
]
```

- Space: O(V²).
- Best for **dense** graphs and when you need O(1) edge lookup.

---

### 2. Breadth-First Search (BFS)

Explore all neighbors of the current node before going deeper. Uses a **queue** (FIFO).

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

- Finds the **shortest path** (fewest edges) in an unweighted graph.
- Time complexity: **O(V + E)**.

---

### 3. Depth-First Search (DFS)

Go as deep as possible along one path before backtracking. Uses a **stack** (or recursion).

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

- Useful for detecting cycles, topological sorting, and maze solving.
- Time complexity: **O(V + E)**.

---

### 4. Connected Components

A **connected component** is a group of nodes where every node is reachable from every other node in the group.

```python
def connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = dfs(graph, node, visited)
            components.append(component)

    return components
```

---

### 5. Weighted Graphs

Edges can carry **weights** (distances, costs, times). Represent with a list of `(neighbor, weight)` tuples:

```python
weighted_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 5)],
    'C': [('A', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
```

---

### 6. Dijkstra's Shortest-Path Algorithm

Find the shortest path from a source node to all other nodes in a weighted graph.

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]   # (distance, node)

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue    # Already found a shorter path
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances
```

- Time complexity: **O((V + E) log V)** with a min-heap.
- Does **not** work with negative edge weights.

---

### 7. Prim's Minimum Spanning Tree

Find the minimum set of edges that connects all nodes with the smallest total weight.

```python
def prims(graph, start):
    visited = {start}
    edges = [(weight, start, neighbor)
             for neighbor, weight in graph[start]]
    heapq.heapify(edges)
    mst = []

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst
```

---

## Hints for This Week's Assignment

- **Always track visited nodes** in BFS and DFS — without a `visited` set, you'll loop forever in graphs with cycles.
- BFS uses a **queue** (FIFO); DFS uses a **stack** or recursion. Mix these up and your traversal order will be wrong.
- Draw small graphs by hand and trace through BFS/DFS manually before running your code.
- Dijkstra's algorithm processes nodes in order of their current known distance — the min-heap takes care of this automatically.
- For Prim's MST, the number of edges in the result is always V − 1 (where V is the number of nodes). Use this to verify your result.
- Start with the adjacency list representation — it's easier to read and write than matrices.

---

## Assignment Instructions

**File to create:** `module_13/graph.py`

You will implement a `Graph` class with BFS, DFS, connected components, and Dijkstra's shortest path. Work through each step in order.

---

### Step 1 — `Graph` class skeleton

Create a `Graph` class with:
- `self.adjacency_list = {}` — dictionary mapping each node to a list of `(neighbor, weight)` tuples.
- `add_vertex(v)` — add `v` as a key with an empty list if it doesn't already exist.
- `add_edge(u, v, weight=1)` — add an undirected edge between `u` and `v` with the given weight. Call `add_vertex` for both nodes first.
- `__str__()` — print each vertex and its neighbors.

```python
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 1)
g.add_edge("D", "E", 3)
print(g)
# A → [('B', 4), ('C', 2)]
# B → [('A', 4), ('D', 5)]
# C → [('A', 2), ('D', 1)]
# D → [('B', 5), ('C', 1), ('E', 3)]
# E → [('D', 3)]
```

---

### Step 2 — `bfs(start)`

Implement BFS starting from `start`. Return a list of vertices in the order they were visited.

```python
print(g.bfs("A"))   # ['A', 'B', 'C', 'D', 'E']  (neighbor order may vary)
```

Use a `collections.deque` as your queue. Add neighbors to the queue only if they haven't been visited.

---

### Step 3 — `dfs(start)`

Implement DFS starting from `start`. Use **recursion** (not an explicit stack). Return a list of vertices in visit order.

```python
print(g.dfs("A"))   # ['A', 'B', 'D', 'C', 'E']  (order depends on neighbor order)
```

---

### Step 4 — `has_path(start, end)`

Return `True` if there is any path from `start` to `end`, `False` otherwise. Use BFS or DFS internally.

```python
print(g.has_path("A", "E"))   # True
print(g.has_path("A", "Z"))   # False  (Z doesn't exist)
```

---

### Step 5 — `connected_components()`

Return a list of sets, where each set is one connected component (group of nodes that can all reach each other).

Build a disconnected graph to test this:
```python
g2 = Graph()
g2.add_edge("A", "B")
g2.add_edge("B", "C")
g2.add_edge("D", "E")
g2.add_vertex("F")
print(g2.connected_components())
# [{'A', 'B', 'C'}, {'D', 'E'}, {'F'}]  (set order may vary)
```

---

### Step 6 — `dijkstra(start)`

Implement Dijkstra's algorithm. Return a dictionary mapping every reachable vertex to its shortest distance from `start`.

```python
distances = g.dijkstra("A")
print(distances)
# {'A': 0, 'C': 2, 'B': 4, 'D': 3, 'E': 6}
```

Verify by tracing the shortest paths by hand:
- A→C = 2
- A→C→D = 3
- A→B = 4
- A→C→D→E = 6

---

### Step 7 — `shortest_path(start, end)`

Extend Dijkstra to also track the **actual path** (not just the distance). Return a tuple `(distance, path)` where `path` is a list of vertices.

```python
dist, path = g.shortest_path("A", "E")
print(dist)   # 6
print(path)   # ['A', 'C', 'D', 'E']
```

**Hint:** Track a `previous` dictionary in your Dijkstra implementation. After finding shortest distances, walk backward from `end` through `previous` to reconstruct the path, then reverse it.

---

### Step 8 — Campus map demo

At the bottom of your file, build a mini campus map and demonstrate all features:

```python
campus = Graph()
campus.add_edge("Library", "Science Hall", 5)
campus.add_edge("Library", "Student Union", 3)
campus.add_edge("Science Hall", "Engineering", 2)
campus.add_edge("Student Union", "Engineering", 7)
campus.add_edge("Engineering", "Dorms", 4)

print("All buildings (BFS from Library):", campus.bfs("Library"))
dist, path = campus.shortest_path("Library", "Dorms")
print(f"Shortest path to Dorms: {' → '.join(path)} ({dist} min)")
```

---

### Checklist Before Submitting

- [ ] `add_vertex()` and `add_edge()` work correctly; `__str__()` shows the adjacency list.
- [ ] `bfs()` visits all reachable nodes in breadth-first order.
- [ ] `dfs()` visits all reachable nodes in depth-first order using recursion.
- [ ] `has_path()` returns `True`/`False` correctly, including for non-existent vertices.
- [ ] `connected_components()` identifies all components including isolated vertices.
- [ ] `dijkstra()` returns correct shortest distances (verified by hand for the example graph).
- [ ] `shortest_path()` returns both the distance and the actual path as a list.
- [ ] The campus map demo runs and prints meaningful output.
