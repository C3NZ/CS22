class Vertex:
    def __init__(self, key: str):
        self.key = key
        self.__neighbors: list = []

    def __eq__(self, other_vert):
        return self.key == other_vert.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return "V-" + str(self.key)

    def __in_neighbors(self, vert):
        """
            Check if the vertex is already a neighbor to this current one 

            Args:
                vert - The other vertex object we're checking
        """
        if not self.__neighbors:
            return False

        for stored_vert, _ in self.__neighbors:
            if vert == stored_vert:
                return True

        return False

    @property
    def neighbors(self):
        """
            Get the keys of the neighbors of the vertex
        """
        return self.__neighbors

    def add_neighbor(self, edge: tuple):
        """
            Add a neighbor to this vertex
        """
        vert, weight = edge
        if not self.__in_neighbors(vert):
            self.__neighbors.append((vert, float(weight)))
            return True
        return False


class Graph:
    """
        An undirected graph implementation
    """

    def __init__(self):
        self.graph = {}
        self.verticies = 0
        self.edges = 0

    def __hash_vert(self, vert: Vertex):
        return hash(vert)

    def add_vertex(self, vert: Vertex):
        """
            Add a vertex to the graph

            Args:
                vertex - The vertex object that we would like to be adding.
        """

        if vert.key not in self.graph:
            self.graph[vert.key] = vert
            self.verticies += 1
            return

        raise KeyError("The Vertex you're trying to add already exists")

    def get_vertex(self, vert_key: str):
        """
            Get a specific vertex from the set of verticies we have.

            Args:
                vertKey - the integer of the vert key we're looking for

            Returns:
                a vertex object if the vertkey is found
        """
        if vert_key in self.graph:
            return self.graph[vert_key]

        raise KeyError("The Vertex is not stored within this graph.")

    def get_verticies(self):
        """
            Return a list of all the vertex keys 

            Returns:
                a list of all verticies objects within the graph
        """
        return self.graph.keys()

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
        elif from_vert == to_vert:
            raise ValueError("You cannot have a vertex connect to itself.")

        # The from and to vertex objects within our graph
        from_vert_obj = self.graph[from_vert]
        to_vert_obj = self.graph[to_vert]

        # Add the neighbors to each vertex
        added_from = from_vert_obj.add_neighbor((to_vert_obj, weight))
        added_to = to_vert_obj.add_neighbor((from_vert_obj, weight))

        if added_from and added_to:
            self.edges += 1

    def get_neighbors(self, vert_key: str):
        """
            Get the neighbors of a vertex stored within the graph.

            Args:
                vert: The vertex we're trying to get the neighbors of.

            Returns:
                The neighbors of the vertex that we're looking for
        """
        if vert_key not in self.graph:
            raise KeyError("The vertex is not in the graph")

        return self.graph[vert_key].neighbors

    def get_edges(self):
        """
            Get all of the edges from the graph

            Returns:
                A list of the unique edges within the graph.
        """
        sorted_edges = set()
        unique_edges = set()

        for vert_key, vertex in self.graph.items():
            for neighbor_vert, weight in vertex.neighbors:
                edge = (vert_key, neighbor_vert.key, str(weight))
                sorted_edge = tuple(sorted(edge))
                if sorted_edge not in sorted_edges:
                    unique_edges.add(edge)

                sorted_edges.add(sorted_edge)

        return list(unique_edges)


import argparse


def fill_graph(graph: Graph, verts: list, edges: list):
    """
        Fill an undirected graph object with verticies and edges.

        Args:
            graph - the undirected graph object that is going to be filled
            verts - A list of vertex objects to add to the graph
            edges - A list of tuples that contain edge keys and weights.
    """
    # Iterate through the verticies.
    for vert in verts:
        graph.add_vertex(vert)

    # Iterate through the edges and add it.
    for from_vert, to_vert, weight in edges:
        graph.add_edge(from_vert, to_vert, weight)


def main(filename: str) -> Graph:
    """
        Main functionality of the app, opens the file and then
        parses it into a graph object

        Args:
            filename - The name of the file to open

        Returns:
            A graph object with the specified vertex and edges added
    """
    graph = Graph()
    verts = []
    edges = []

    # Open up the file and parse the graph from text
    with open(filename, "r") as file:
        counter = 0
        for line in file:
            if counter == 1:
                for key in line.strip().split(","):
                    verts.append(Vertex(key))
            elif counter > 1:
                edge = line.strip("()\n").split(",")
                if len(edge) != 3:
                    raise Exception(
                        f"You specified an incorrect amount of args for the edge: {line}"
                    )
                edges.append(edge)
            counter += 1

    # Fill the graph with the necessary items
    fill_graph(graph, verts, edges)

    print(f"Verticies: {graph.verticies}")
    print(f"Edges: {graph.edges}")
    print("Edge list:")

    # iterate through the fromVert, toVert, and weights and print them out.
    for from_vert, to_vert, weight in graph.get_edges():
        print(f"({from_vert}, {to_vert}, {weight})")

    return graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename)
