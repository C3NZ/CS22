"""
    Tests for challenge 1
"""
import unittest

from graphs.digraph import Digraph
from graphs.graph import Graph
from graphs.vertex import Vertex


class VertexTest(unittest.TestCase):
    def test_instantation(self):
        # Test instantation properties of a vertex
        v1 = Vertex("k")

        self.assertEqual(v1.key, "k")
        self.assertListEqual(v1.neighbors, [])

    def test_equality(self):
        v1 = Vertex("k")
        v2 = Vertex("g")
        v3 = Vertex("k")

        # Assert that they're not equal based on keys
        self.assertNotEqual(v1, v2)

        # Assert that these verts are equal because of their keys
        self.assertEqual(v1, v3)


class GraphTest(unittest.TestCase):
    def test_instantation(self):
        graph = Graph()

        self.assertDictEqual(graph.graph, {})
        self.assertEqual(graph.verticies, 0)
        self.assertEqual(graph.edges, 0)

    def test_add_vertex(self):
        graph = Graph()

        # Create verticies
        v1, v2, v3 = Vertex("k"), Vertex("g"), Vertex("g")

        # Add vertex 3
        graph.add_vertex(v1)
        self.assertDictEqual(graph.graph, {"k": v1})
        self.assertEqual(graph.verticies, 1)
        self.assertEqual(graph.edges, 0)

        # Add vertex 2
        graph.add_vertex(v2)
        self.assertDictEqual(graph.graph, {"k": v1, "g": v2})
        self.assertEqual(graph.verticies, 2)
        self.assertEqual(graph.edges, 0)

        # Try adding a vertex with the same key
        with self.assertRaises(KeyError):
            graph.add_vertex(v3)

    def test_get_vertex(self):
        graph = Graph()

        # Create verticies
        v1, v2, v3 = Vertex("k"), Vertex("g"), Vertex("a")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        # Assert the count is equal
        self.assertEqual(graph.verticies, 3)

        # Assert that we can get all verts by keys
        self.assertEqual(v1, graph.get_vertex("k"))
        self.assertEqual(v2, graph.get_vertex("g"))
        self.assertEqual(v3, graph.get_vertex("a"))

        # Attempt to get a key that doesn't exist
        with self.assertRaises(KeyError):
            graph.get_vertex("j")

    def test_get_verticies(self):
        graph = Graph()

        # Create verticies
        v1, v2, v3 = Vertex("k"), Vertex("g"), Vertex("a")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        # Assert the count is equal
        self.assertEqual(graph.verticies, 3)

        self.assertListEqual(graph.get_verticies(), [v1, v2, v3])

    def test_add_edge(self):
        graph = Graph()

        # Create verticies
        v1, v2, v3, v4 = Vertex("k"), Vertex("g"), Vertex("a"), Vertex("b")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_vertex(v4)

        self.assertEqual(graph.verticies, 4)
        self.assertEqual(graph.edges, 0)

        # create edges (1 duplicate one to demonstrate how it handles duplicates)
        edges = [
            ("k", "g", 10),
            ("g", "k", 10),
            ("g", "a", 4),
            ("a", "k", 30),
            ("b", "k", 20),
        ]

        # Iterate over
        for edge in edges:
            from_vert, to_vert, weight = edge
            graph.add_edge(from_vert, to_vert, weight)

        self.assertEqual(graph.edges, 4)

    def test_get_edges(self):
        graph = Graph()

        # Create verticies
        v1, v2, v3, v4 = Vertex("k"), Vertex("g"), Vertex("a"), Vertex("b")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_vertex(v4)

        self.assertEqual(graph.verticies, 4)
        self.assertEqual(graph.edges, 0)

        # create edges (1 duplicate one to demonstrate how it handles duplicates)
        edges = [
            ("k", "g", 10),
            ("g", "k", 10),
            ("g", "a", 4),
            ("a", "k", 30),
            ("b", "k", 20),
            ("a", "b", 10),
        ]

        # Iterate over the edges and put them into the graph
        for edge in edges:
            from_vert, to_vert, weight = edge
            graph.add_edge(from_vert, to_vert, weight)

        self.assertEqual(graph.edges, 5)
        # create edges (1 duplicate one to demonstrate how it handles duplicates)
        unique_edges = [
            ("k", "g", 10),
            ("g", "a", 4),
            ("a", "k", 30),
            ("b", "k", 20),
            ("a", "b", 10),
        ]
        self.assertEqual(len(graph.get_edges()), len(unique_edges))

    def test_get_neighbors(self):
        graph = Graph()

        # Create verticies
        v1, v2, v3, v4 = Vertex("k"), Vertex("g"), Vertex("a"), Vertex("b")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_vertex(v4)

        self.assertEqual(graph.verticies, 4)
        self.assertEqual(graph.edges, 0)

        # create edges (1 duplicate one to demonstrate how it handles duplicates)
        edges = [
            ("k", "g", 10),
            ("g", "a", 4),
            ("a", "k", 30),
            ("b", "k", 20),
            ("a", "b", 10),
        ]

        # Iterate over the edges and put them into the graph
        for edge in edges:
            from_vert, to_vert, weight = edge
            graph.add_edge(from_vert, to_vert, weight)

        self.assertEqual(graph.edges, 5)


class DigraphTest(unittest.TestCase):
    def test_instantation(self):
        graph = Digraph()

        self.assertDictEqual(graph.graph, {})
        self.assertEqual(graph.verticies, 0)
        self.assertEqual(graph.edges, 0)

    def test_add_vertex(self):
        graph = Digraph()

        # Create verticies
        v1, v2, v3 = Vertex("k"), Vertex("g"), Vertex("g")

        # Add vertex 3
        graph.add_vertex(v1)
        self.assertDictEqual(graph.graph, {"k": v1})
        self.assertEqual(graph.verticies, 1)
        self.assertEqual(graph.edges, 0)

        # Add vertex 2
        graph.add_vertex(v2)
        self.assertDictEqual(graph.graph, {"k": v1, "g": v2})
        self.assertEqual(graph.verticies, 2)
        self.assertEqual(graph.edges, 0)

        # Try adding a vertex with the same key
        with self.assertRaises(KeyError):
            graph.add_vertex(v3)

    def test_get_vertex(self):
        graph = Digraph()

        # Create verticies
        v1, v2, v3 = Vertex("k"), Vertex("g"), Vertex("a")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        # Assert the count is equal
        self.assertEqual(graph.verticies, 3)

        # Assert that we can get all verts by keys
        self.assertEqual(v1, graph.get_vertex("k"))
        self.assertEqual(v2, graph.get_vertex("g"))
        self.assertEqual(v3, graph.get_vertex("a"))

        # Attempt to get a key that doesn't exist
        with self.assertRaises(KeyError):
            graph.get_vertex("j")

    def test_get_verticies(self):
        graph = Digraph()

        # Create verticies
        v1, v2, v3 = Vertex("k"), Vertex("g"), Vertex("a")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        # Assert the count is equal
        self.assertEqual(graph.verticies, 3)

        self.assertListEqual(graph.get_verticies(), [v1, v2, v3])

    def test_add_edge(self):
        graph = Digraph()

        # Create verticies
        v1, v2, v3, v4 = Vertex("k"), Vertex("g"), Vertex("a"), Vertex("b")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_vertex(v4)

        self.assertEqual(graph.verticies, 4)
        self.assertEqual(graph.edges, 0)

        # create edges (1 duplicate one to demonstrate how it handles duplicates)
        edges = [
            ("k", "g", 10),
            ("g", "k", 10),
            ("g", "a", 4),
            ("a", "k", 30),
            ("b", "k", 20),
        ]

        # Iterate over
        for edge in edges:
            from_vert, to_vert, weight = edge
            graph.add_edge(from_vert, to_vert, weight)

        self.assertEqual(graph.edges, 5)

    def test_get_edges(self):
        graph = Digraph()

        # Create verticies
        v1, v2, v3, v4 = Vertex("k"), Vertex("g"), Vertex("a"), Vertex("b")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_vertex(v4)

        self.assertEqual(graph.verticies, 4)
        self.assertEqual(graph.edges, 0)

        # create edges (1 duplicate one to demonstrate how it handles duplicates)
        edges = [
            ("k", "g", 10),
            ("g", "k", 10),
            ("g", "a", 4),
            ("a", "k", 30),
            ("b", "k", 20),
            ("a", "b", 10),
        ]

        # Iterate over the edges and put them into the graph
        for edge in edges:
            from_vert, to_vert, weight = edge
            graph.add_edge(from_vert, to_vert, weight)

        self.assertEqual(graph.edges, 6)
        # create edges (1 duplicate one to demonstrate how it handles duplicates)

        self.assertEqual(len(graph.get_edges()), len(edges))
        self.assertCountEqual(graph.get_edges(), edges)

    def test_get_neighbors(self):
        graph = Digraph()

        # Create verticies
        v1, v2, v3, v4 = Vertex("k"), Vertex("g"), Vertex("a"), Vertex("b")

        # Add verticies to the list
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_vertex(v4)

        self.assertEqual(graph.verticies, 4)
        self.assertEqual(graph.edges, 0)

        # create edges (1 duplicate one to demonstrate how it handles duplicates)
        edges = [
            ("k", "g", 10),
            ("g", "a", 4),
            ("a", "k", 30),
            ("b", "k", 20),
            ("a", "b", 10),
        ]

        # Iterate over the edges and put them into the graph
        for edge in edges:
            from_vert, to_vert, weight = edge
            graph.add_edge(from_vert, to_vert, weight)

        self.assertEqual(graph.edges, 5)

        # Testing vertex 1 neighbors
        self.assertIn((v2, 10), v1.neighbors)
