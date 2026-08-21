# Week 13 — Graphs
### Representations, BFS, DFS, Shortest Path, and Minimum Spanning Trees

---

## Welcome!

Every data structure you've seen so far has been somewhat linear or tree-like. **Graphs** are the most general structure of all — they can model anything where things are connected to other things: social networks, road maps, airline routes, the internet, power grids, and more.

This is also one of the most exciting weeks because the algorithms you write here — BFS, DFS, Dijkstra's — are used in Google Maps, Facebook friend suggestions, and GPS systems.

---

## Concept 1: What Is a Graph?

A graph has:
- **Vertices (nodes)** — the things (cities, people, web pages, buildings)
- **Edges** — the connections between them (roads, friendships, links)

**Analogy:** A road map is a graph. Cities are vertices. Roads connecting them are edges. If a road goes both ways, it's an **undirected** edge. A one-way street is a **directed** edge.

```
    A ——4—— B
    |       |
    2       5
    |       |
    C ——1—— D ——3—— E
```

Here, edges have **weights** (the numbers) — think of them as distances or travel times.

---

## Concept 2: Representing a Graph in Code

### Adjacency List (Most Common)

Each node maps to a list of its neighbors (and optional weights):

```python
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 5)],
    "C": [("A", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1), ("E", 3)],
    "E": [("D", 3)]
}
```

Reading this: `"A": [("B", 4), ("C", 2)]` means A is connected to B (cost 4) and C (cost 2).

- Space: O(vertices + edges) — efficient for sparse graphs (few edges)
- Easy to iterate over neighbors

---

## Concept 3: BFS — Breadth-First Search

BFS explores the graph **level by level** — all neighbors of the starting point first, then their neighbors, then their neighbors' neighbors, etc.

**Analogy:** You drop a stone in a pond. The ripples spread outward in rings — the closest water moves first, then the next ring, then the next. BFS is like those ripples through a graph.

**What it's good for:** Finding the shortest path in an **unweighted** graph (fewest edges, not lowest total weight).

**How it works:**
1. Start at the source node. Mark it visited.
2. Add it to a queue (FIFO).
3. Dequeue a node. Visit all its unvisited neighbors. Mark them visited and add them to the queue.
4. Repeat until the queue is empty.

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
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

---

## Concept 4: DFS — Depth-First Search

DFS goes as **deep** as possible along one path before backtracking and trying another path.

**Analogy:** You're exploring a cave system. You pick one tunnel and follow it all the way to the end (or a dead end). Then you backtrack and try the next tunnel.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result
```

**BFS vs. DFS:**
- BFS finds the shortest path (by number of edges) — use a queue
- DFS is great for detecting cycles, exploring all paths — uses recursion (or a stack)

---

## Concept 5: Connected Components

A **connected component** is a group of nodes where you can get from any one to any other by following edges. If you can't get from A to B at all, they're in different components.

**Analogy:** Imagine islands. All the cities on one island form a connected component. You can't drive to a different island.

```python
def connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = dfs(graph, node, visited)
            components.append(set(component))
    return components
```

---

## Concept 6: Dijkstra's Shortest Path

What if edges have weights (distances, times, costs)? BFS no longer works because it counts edges, not total cost. **Dijkstra's algorithm** finds the path with the lowest total weight.

**Analogy:** Google Maps finding the fastest route. Not the route with fewest turns (BFS), but the one with the shortest total drive time (Dijkstra's).

**How it works:**
1. Start with distance 0 to the source, infinity to everywhere else
2. Use a min-heap (priority queue) ordered by current known distance
3. Each time you process a node, check if going through it gives a shorter path to any of its neighbors
4. If yes, update the distance and add the neighbor to the heap

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]   # (distance, node)

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue    # Already found a better path to this node
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances
```

For the example graph, starting at A:
- A→C = 2, A→C→D = 3, A→B = 4, A→C→D→E = 6

---

## Assignment Instructions

**File to create:** `module_13/graph.py`

---

### Step 1 — `Graph` class

```python
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))   # Undirected

    def __str__(self):
        lines = []
        for vertex, neighbors in self.adjacency_list.items():
            lines.append(f"{vertex} → {neighbors}")
        return "\n".join(lines)
```

Test:
```python
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 1)
g.add_edge("D", "E", 3)
print(g)
```

---

### Step 2 — `bfs(start)`

Return a list of vertices visited in breadth-first order.

```python
print(g.bfs("A"))   # ['A', 'B', 'C', 'D', 'E']  (exact order may vary by neighbor order)
```

---

### Step 3 — `dfs(start)`

Return a list in depth-first order (use recursion).

```python
print(g.dfs("A"))   # ['A', 'B', 'D', 'C', 'E']  (order depends on neighbor order)
```

---

### Step 4 — `has_path(start, end)`

Return `True` if any path exists from `start` to `end`. Return `False` if the vertex doesn't exist or there's no connection.

```python
print(g.has_path("A", "E"))    # True
print(g.has_path("A", "Z"))    # False  (Z doesn't exist)
```

---

### Step 5 — `connected_components()`

Build a disconnected graph and find all components:

```python
g2 = Graph()
g2.add_edge("A", "B")
g2.add_edge("B", "C")
g2.add_edge("D", "E")
g2.add_vertex("F")
print(g2.connected_components())
# [{'A', 'B', 'C'}, {'D', 'E'}, {'F'}]  — three separate groups
```

---

### Step 6 — `dijkstra(start)`

Return a dictionary of shortest distances from `start` to every reachable node.

```python
distances = g.dijkstra("A")
print(distances)
# {'A': 0, 'B': 4, 'C': 2, 'D': 3, 'E': 6}
```

Verify by hand: A→C = 2, A→C→D = 3, A→B = 4, A→C→D→E = 6. ✅

---

### Step 7 — `shortest_path(start, end)`

Extend Dijkstra to also track which node came before each node (a `previous` dictionary). After finding shortest distances, backtrack from `end` through `previous` to reconstruct the path.

```python
dist, path = g.shortest_path("A", "E")
print(dist)    # 6
print(path)    # ['A', 'C', 'D', 'E']
```

**Hint:** After Dijkstra, build the path by starting at `end` and following `previous[node]` backward until you reach `start`. Then reverse the result.

---

### Step 8 — Campus map demo

```python
def campus_demo():
    campus = Graph()
    campus.add_edge("Library", "Science Hall", 5)
    campus.add_edge("Library", "Student Union", 3)
    campus.add_edge("Science Hall", "Engineering", 2)
    campus.add_edge("Student Union", "Engineering", 7)
    campus.add_edge("Engineering", "Dorms", 4)

    print("Campus map:")
    print(campus)
    print("\nBFS from Library:", campus.bfs("Library"))

    dist, path = campus.shortest_path("Library", "Dorms")
    print(f"\nShortest path to Dorms: {' → '.join(path)} (total: {dist} min)")

campus_demo()
```

---

### Checklist Before Submitting

- [ ] `add_vertex()` and `add_edge()` work; `__str__()` shows adjacency list
- [ ] `bfs()` visits all reachable nodes in breadth-first order (uses a queue)
- [ ] `dfs()` visits all reachable nodes in depth-first order (uses recursion)
- [ ] `has_path()` returns correct result, including `False` for non-existent vertices
- [ ] `connected_components()` correctly finds all groups including isolated vertices
- [ ] `dijkstra()` returns correct shortest distances (verified by hand)
- [ ] `shortest_path()` returns both the distance and the actual path as a list
- [ ] Campus demo runs and prints meaningful output
