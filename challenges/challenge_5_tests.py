import unittest

from graphs.digraph import Digraph
from graphs.graph import Graph, Vertex, fill_graph
from graphs.utils.file_reader import read_graph_file


class TestEulerian(unittest.TestCase):
    def test_true_eulerian(self):
        """
            Test a true eulerian path
        """
        # Obtain the graph properties and then fill out the graph.
        graph, vertex, edges = read_graph_file("inputs/eularian.txt")
        fill_graph(graph, vertex, edges)

        self.assertEqual(graph.is_eulerian_cycle(), True)

    def test_empty_graph(self):
        """
            Test an empty graph
        """
        graph = Graph()
        self.assertEqual(graph.is_eulerian_cycle(), False)

    def test_edgeless_graph(self):
        graph = Graph()
        vertices = [Vertex("a"), Vertex("b"), Vertex("c")]

        for vert in vertices:
            graph.add_vertex(vert)

        self.assertEqual(graph.is_eulerian_cycle(), False)

    def test_false_eulerian(self):
        graph = Digraph()
        vertices = [Vertex("a"), Vertex("b"), Vertex("c")]

        # b has only one neighbor
        edges = [
            ("a", "b", 1),
            ("a", "c", 1),
            ("b", "c", 1),
            ("c", "b", 1),
            ("c", "a", 1),
        ]

        for vert in vertices:
            graph.add_vertex(vert)

        for edge in edges:
            graph.add_edge(edge[0], edge[1])

        self.assertEqual(graph.is_eulerian_cycle(), False)

    def test_fixed_eulerian(self):
        graph = Digraph()
        vertices = [Vertex("a"), Vertex("b"), Vertex("c")]

        # b has only one neighbor
        edges = [
            ("a", "b", 1),
            ("a", "c", 1),
            ("b", "c", 1),
            ("b", "a", 1),
            ("c", "b", 1),
            ("c", "a", 1),
        ]

        for vert in vertices:
            graph.add_vertex(vert)

        for edge in edges:
            graph.add_edge(edge[0], edge[1])

        self.assertEqual(graph.is_eulerian_cycle(), True)
