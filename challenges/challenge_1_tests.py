"""
    Tests for challenge 1
"""
import unittest

from challenge_1 import DiGraph, Graph, Vertex


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
