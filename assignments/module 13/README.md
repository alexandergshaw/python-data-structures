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
