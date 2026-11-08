import unittest

from tests.support import load_answer


class GraphTests(unittest.TestCase):
    def test_traversals_components_and_shortest_routes(self):
        module = load_answer("module_13", "graph.py")
        graph = module.Graph()
        for edge in [("A", "B", 4), ("A", "C", 2), ("B", "D", 5),
                     ("C", "D", 1), ("D", "E", 3)]:
            graph.add_edge(*edge)
        self.assertEqual(graph.bfs("A"), ["A", "B", "C", "D", "E"])
        self.assertEqual(graph.dfs("A"), ["A", "B", "D", "C", "E"])
        self.assertTrue(graph.has_path("A", "E"))
        self.assertFalse(graph.has_path("A", "Z"))
        self.assertEqual(graph.dijkstra("A"), {"A": 0, "B": 4, "C": 2, "D": 3, "E": 6})
        self.assertEqual(graph.shortest_path("A", "E"), (6, ["A", "C", "D", "E"]))
        graph.add_vertex("F")
        components = graph.connected_components()
        self.assertIn({"F"}, components)
        self.assertEqual(len(components), 2)


if __name__ == "__main__":
    unittest.main()
