import unittest

from graphs.graph import Graph
from graphs.vertex import Vertex


class BreadthTest(unittest.TestCase):
    """
        Testing out the breadth first search algorithm
    """

    def test_bfs(self):
        """
            Test out our breadth first search algorithm
        """
        graph = Graph()
        vertices = [
            Vertex("a"),  # 0
            Vertex("b"),  # 1
            Vertex("c"),  # 2
            Vertex("d"),  # 3
            Vertex("e"),  # 4
            Vertex("f"),  # 5
            Vertex("g"),  # 6
        ]
        edges = [
            ("a", "b", 2),
            ("a", "c", 2),
            ("b", "c", 2),
            ("b", "e", 2),
            ("c", "d", 2),
            ("d", "g", 2),
        ]

        for vertex in vertices:
            graph.add_vertex(vertex)

        for edge in edges:
            from_vert, to_vert, weight = edge
            graph.add_edge(from_vert, to_vert, weight)

        # Should throw an error, there is no key 3!
        with self.assertRaises(KeyError):
            graph.find_shortest_path("a", "3")

        # Testing from vertex A -> A
        # Should have no edges and be connected to just itself.
        pred_path, pred_edges = graph.find_shortest_path("a", "a")
        actual_path = [vertices[0]]
        actual_edges = 0
        self.assertEqual((pred_path, pred_edges), (actual_path, actual_edges))

        # Testing from vertex A -> F
        # Should have no connection and infinite (-1) edges
        pred_path, pred_edges = graph.find_shortest_path("a", "f")
        actual_path = []
        actual_edges = -1
        self.assertEqual((pred_path, pred_edges), (actual_path, actual_edges))

        # Testing from vertex A -> E
        # Should have a path from a -> b -> e with 2 edges
        pred_path, pred_edges = graph.find_shortest_path("a", "e")
        actual_path = [vertices[0], vertices[1], vertices[4]]
        actual_edges = 2
        self.assertEqual((pred_path, pred_edges), (actual_path, actual_edges))

        # Testing from vertices A -> G
        # Should be connected from: a -> c -> d -> g
        pred_path, pred_edges = graph.find_shortest_path("a", "g")
        actual_path = [vertices[0], vertices[2], vertices[3], vertices[6]]
        actual_edges = 3
        self.assertEqual((pred_path, pred_edges), (actual_path, actual_edges))
