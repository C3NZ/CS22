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
            Vertex("a"),
            Vertex("b"),
            Vertex("c"),
            Vertex("d"),
            Vertex("e"),
            Vertex("f"),
            Vertex("g"),
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

        with self.assertRaises(KeyError):
            graph.find_shortest_path("a", "3")
