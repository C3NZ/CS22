import unittest

from graphs.digraph import Digraph
from graphs.vertex import Vertex


class DepthFirstSearch(unittest.TestCase):
    def test_dfs(self):
        graph = Digraph()
