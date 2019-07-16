from graph import Graph


class Digraph(Graph):
    """
        A directed graph
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"<Digraph> - {self.verticies} verts - {self.edges} edges"

    def add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0):
        """
           Add an edge to the graph

           Args:
               fromVert - The vertex object we're connecting the toVert to
               toVert - The vertex object we're connecting the fromVert to
               weight - (1.0) - The weight of the edge
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

        if added_from:
            self.edges += 1
