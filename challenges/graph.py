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
                vert
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

    def get_vertex(self, vertKey: str):
        """
            Get a specific vertex from the set of verticies we have.

            Args:
                vertKey - the integer of the vert key we're looking for

            Returns:
                a vertex object if the vertkey is found
        """
        if vertKey in self.graph:
            return self.graph[vertKey]

        raise KeyError("The Vertex is not stored within this graph.")

    def get_verticies(self):
        """
            Return a list of all the vertex keys

            Returns:
                a list of all verticies objects within the graph
        """
        return self.graph.keys()

    def add_edge(self, fromVert: str, toVert: str, weight: float = 1.0):
        """
           Add an edge to the graph 

           Args:
               fromVert - The vertex object we're connecting the toVert to
               toVert - The vertex object we're connecting the fromVert to
               weight - (0) - The weight of the edge 
        """

        # The hashed keys for the from and to verts

        if fromVert not in self.graph or toVert not in self.graph:
            raise ValueError("One of the verticies is not currently in the graph.")
        elif fromVert == toVert:
            raise ValueError("You cannot have a vertex connect to itself.")

        # The from and to vertex objects
        fromVertObj = self.graph[fromVert]
        toVertObj = self.graph[toVert]

        # Add the neighbors to each vertex
        self.graph[fromVert].addNeighbor((toVertObj, weight))

        self.edges += 1

    def get_neighbors(self, vert: Vertex):
        """
            Get the neighbors of a vertex stored within the graph.

            Args:
                vert: The vertex we're trying to get the neighbors of.
        """
        if vert not in self.graph:
            raise KeyError("The vertex is not in the graph")

        return self.graph[vert].neighbors

    def get_edges(self):
        """
            Get the edges of
        """
        sortedEdges = set()
        uniqueEdges = set()

        for vertKey, vertex in self.graph.items():
            for neighborVert, weight in vertex.neighbors:
                edge = (vertKey, neighborVert.key, str(weight))
                sortedEdge = tuple(sorted(edge))
                if sortedEdge not in sortedEdges:
                    uniqueEdges.add(edge)

                sortedEdges.add(sortedEdge)

        return list(uniqueEdges)


import argparse


def fill_graph(graph: Graph, verts: list, edges: list):
    for vert in verts:
        graph.add_vertex(vert)

    for fromVert, toVert, weight in edges:
        graph.add_edge(fromVert, toVert, weight)


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
    for fromVert, toVert, weight in graph.get_edges():
        print(f"({fromVert}, {toVert}, {weight})")

    return graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename)
