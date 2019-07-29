import unittest

from graphs.digraph import Digraph
from graphs.graph import fill_graph
from graphs.vertex import Vertex


class DepthFirstSearch(unittest.TestCase):
    def test_dfs(self):
        graph = Digraph()

        vertices = [
            Vertex("4"),  # 0
            Vertex("2"),  # 1
            Vertex("3"),  # 2
            Vertex("7"),  # 3
            Vertex("8"),  # 4
            Vertex("1"),  # 5
            Vertex("9"),  # 6
            Vertex("12"),  # 7
            Vertex("13"),  # 8
            Vertex("10"),  # 9
            Vertex("11"),  # 10
            Vertex("14"),  # 11
        ]

        edges = [
            ("4", "2"),
            ("2", "1"),
            ("2", "3"),
            ("1", "9"),
            ("1", "12"),
            ("12", "13"),
            ("9", "10"),
            ("9", "8"),
            ("10", "11"),
            ("8", "7"),
            ("7", "3"),
            ("7", "4"),
        ]

        fill_graph(graph, vertices, edges)

        print(graph)

        # Testing a path to itself
        actual_path = [vertices[0]]
        pred_path = graph.find_path("4", "4")
        self.assertListEqual(pred_path, actual_path)

        # Testing a path that doesn't exist
        actual_path = []
        pred_path = graph.find_path("4", "14")
        self.assertEqual(pred_path, actual_path)

        # Testing a normal path
        # 4 -> 2 -> 1 -> 9 -> 8 -> 7
        actual_path = [
            vertices[0],
            vertices[1],
            vertices[5],
            vertices[6],
            vertices[4],
            vertices[3],
        ]

        pred_path = graph.find_path("4", "7")
        self.assertListEqual(pred_path, actual_path)

        actual_path = [
            vertices[0],
            vertices[1],
            vertices[5],
            vertices[6],
            vertices[9],
            vertices[10],
        ]

        pred_path = graph.find_path("4", "11")
        self.assertListEqual(pred_path, actual_path)
