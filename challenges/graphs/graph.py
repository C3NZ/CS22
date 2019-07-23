"""
    Module that implements an undirected graph class
"""
from collections import deque

from graphs.vertex import Vertex


class Graph:
    """
        Class for representing an undirected graph
    """

    def __init__(self):
        self.graph = {}
        self.verticies = 0
        self.edges = 0

    def __repr__(self):
        return f"<Graph> - {self.verticies} verts - {self.edges} edges"

    def add_vertex(self, vert: Vertex):
        """
            Function for adding a vertex to the graph

            Args:
            * vertex - The vertex object that we would like to be adding.
        """

        if vert.key not in self.graph:
            self.graph[vert.key] = vert
            self.verticies += 1
            return

        raise KeyError("The Vertex you're trying to add already exists")

    def get_vertex(self, vert_key: str):
        """
            Function for getting a specific vertex from the set
            of verticies we have.

            Args:
            * vert_key - the integer of the vert key we're looking for

            Returns:
            * a vertex object if the vertkey is found
        """
        if vert_key in self.graph:
            return self.graph[vert_key]

        raise KeyError("The Vertex is not stored within this graph.")

    def get_verticies(self):
        """
            Function for getting a list of all the vertex keys

            Returns:
            * a list of all verticies objects within the graph
        """
        return list(self.graph.values())

    def add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0):
        """
           Function for adding an edge to the graph

           Args:
           * from_vert - The vertex object we're connecting the toVert to
           * to_vert - The vertex object we're connecting the fromVert to
           * weight - (1.0) - The weight of the edge
        """

        # Error handling before trying to add an edge
        if from_vert not in self.graph or to_vert not in self.graph:
            raise ValueError("One of the verticies is not currently in the graph.")
        if from_vert == to_vert:
            raise ValueError("You cannot have a vertex connect to itself.")

        # The from and to vertex objects within our graph
        from_vert_obj = self.graph[from_vert]
        to_vert_obj = self.graph[to_vert]

        # Add the neighbors to each vertex
        added_from = from_vert_obj.add_neighbor((to_vert_obj, weight))
        added_to = to_vert_obj.add_neighbor((from_vert_obj, weight))

        # Ensure that we had successful adds
        if added_from and added_to:
            self.edges += 1

    def get_neighbors(self, vert_key: str):
        """
            Function for getting the neighbors of a vertex
            stored within the graph.

            Args:
            * vert: The vertex we're trying to get the neighbors of.

            Returns:
            * The neighbors of the vertex that we're looking for
        """
        if vert_key not in self.graph:
            raise KeyError("The vertex is not in the graph")

        return self.graph[vert_key].neighbors

    def get_edges(self) -> [tuple]:
        """
            Function for getting all of the edges from the graph

            Returns:
            * A list of the unique edges within the graph.
        """
        sorted_edges: set = set()
        unique_edges: set = set()

        # Iterate through all of the edges within the graph
        for vert_key, vert in self.graph.items():

            # Iterate through all of the neighbors of the current vertex
            for neighbor_vert, weight in vert.neighbors:
                edge = [vert_key, neighbor_vert.key, str(weight)]
                sorted_edge = tuple(sorted(edge))

                # Check if the sorted edge has been seen before.
                if sorted_edge not in sorted_edges:
                    unique_edges.add((vert_key, neighbor_vert.key, int(weight)))

                sorted_edges.add(sorted_edge)

        return list(unique_edges)

    def find_shortest_path(self, from_vertex: str, to_vertex: str) -> [str]:
        """
            Finding the shortest path from one vertex to another using breadth first
            search. This algorithm attaches a parent property to all vertices that
            are neighbors to the vertex that we're traveling from, allowing us to
            traverse back up the tree to get the path at the end.

            Read more: https://en.wikipedia.org/wiki/Breadth-first_search

            Args:
            * from_vertex - The key of the vertex we're starting at
            * to_vertex - The key of the vertex we're going to

            Returns:
            * A list of vertex keys and the amount of edges if there is a valid
            path within the graph
            * An empty list and -1 indicating that there are no paths between the
            two vertices within the list
        """
        if from_vertex not in self.graph or to_vertex not in self.graph:
            raise KeyError("One of the verticies is not inside of the graph!")

        # If they are the same vertex, the path is itself and the # of edges
        # is 0!
        if from_vertex == to_vertex:
            vert_obj = self.graph[from_vertex]
            return [vert_obj], 0

        # Initialize the current vertex, the seen nodes, and the queue
        curr_vertex = self.graph[from_vertex]
        seen_nodes = set()
        queue = deque()

        # Start the traversal.
        queue.append(curr_vertex)
        seen_nodes.add(curr_vertex.key)

        # Start the path
        path = []
        path_found = False
        parent = None
        curr_vertex.parent = parent

        # Keep traversing while there are still items on the queue
        while queue:
            curr_vertex = queue.popleft()
            path.append(curr_vertex)

            # Check if we made it to our destination
            if curr_vertex.key == to_vertex:
                path_found = True
                break

            # Iterate through all of the neighbors
            for neighbor, _ in curr_vertex.neighbors:

                # Add the neighbor to the queue if it hasn't been seen
                if neighbor.key not in seen_nodes:
                    queue.append(neighbor)
                    seen_nodes.add(neighbor.key)
                    # Set the parent of the neighbor to the current node that we're on
                    neighbor.parent = curr_vertex

        # If there was a path found, we traverse the up the tree.
        if path_found:
            path = []

            # Traversal up the tree.
            while curr_vertex is not None:
                path.append(curr_vertex)
                curr_vertex = curr_vertex.parent

            # Return the list reversed, since we traverse the tree backwards.
            return path[::-1], len(path) - 1

        # No path was found, infinite amount of edges in between from vert and to vert.
        return [], -1


def fill_graph(graph: Graph, verts: list, edges: list):
    """
        Fill an undirected graph object with verticies and edges.

        Args:
        * graph - the graph object that is going to be filled\n
        * verts - A list of vertex objects to add to the graph\n
        * edges - A list of tuples that contain edge keys and weights.\n

        Returns:
        A reference to the graph, vertices, and edges.
    """
    # Iterate through the verticies.
    for vert in verts:
        graph.add_vertex(vert)

    # Iterate through the edges and add it to the graph.
    for edge in edges:
        from_vert, to_vert = edge[0], edge[1]

        # Check if the edge is already weighted
        if len(edge) == 2:
            graph.add_edge(from_vert, to_vert)
        else:
            weight = edge[2]
            graph.add_edge(from_vert, to_vert, weight)

    return graph, verts, edges
