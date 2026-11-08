from collections import deque
import heapq


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list.setdefault(vertex, [])

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def __str__(self):
        return "\n".join(f"{v} → {neighbors}" for v, neighbors in self.adjacency_list.items())

    def bfs(self, start):
        if start not in self.adjacency_list:
            return []
        seen, queue, order = {start}, deque([start]), []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adjacency_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        seen, order = set(), []
        def visit(node):
            seen.add(node)
            order.append(node)
            for neighbor, _ in self.adjacency_list[node]:
                if neighbor not in seen:
                    visit(neighbor)
        if start in self.adjacency_list:
            visit(start)
        return order

    def has_path(self, start, end):
        return end in self.bfs(start)

    def connected_components(self):
        unseen = set(self.adjacency_list)
        components = []
        while unseen:
            component = set(self.dfs(next(iter(unseen))))
            components.append(component)
            unseen -= component
        return components

    def dijkstra(self, start):
        if start not in self.adjacency_list:
            return {}
        distances = {start: 0}
        heap = [(0, start)]
        while heap:
            distance, node = heapq.heappop(heap)
            if distance != distances[node]:
                continue
            for neighbor, weight in self.adjacency_list[node]:
                candidate = distance + weight
                if candidate < distances.get(neighbor, float("inf")):
                    distances[neighbor] = candidate
                    heapq.heappush(heap, (candidate, neighbor))
        return distances

    def shortest_path(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return float("inf"), []
        distances, previous, heap = {start: 0}, {}, [(0, start)]
        while heap:
            distance, node = heapq.heappop(heap)
            if distance != distances[node]:
                continue
            if node == end:
                break
            for neighbor, weight in self.adjacency_list[node]:
                candidate = distance + weight
                if candidate < distances.get(neighbor, float("inf")):
                    distances[neighbor], previous[neighbor] = candidate, node
                    heapq.heappush(heap, (candidate, neighbor))
        if end not in distances:
            return float("inf"), []
        path, node = [], end
        while node != start:
            path.append(node)
            node = previous[node]
        path.append(start)
        return distances[end], path[::-1]


def campus_demo():
    campus = Graph()
    for a, b, weight in [("Library", "Science Hall", 5),
                         ("Library", "Student Union", 3),
                         ("Science Hall", "Engineering", 2),
                         ("Student Union", "Engineering", 7),
                         ("Engineering", "Dorms", 4)]:
        campus.add_edge(a, b, weight)
    print("Campus map:")
    print(campus)
    print("\nBFS from Library:", campus.bfs("Library"))
    distance, path = campus.shortest_path("Library", "Dorms")
    print(f"\nShortest path to Dorms: {' → '.join(path)} (total: {distance} min)")


if __name__ == "__main__":
    campus_demo()
