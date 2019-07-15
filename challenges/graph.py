class Vertex:
    def __init__(self, key: str):
        self.key = key
        self.__neighbors: list = []

    def __eq__(self, otherVert):
        return self.key == otherVert.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return "V-" + str(self.key)

    def __inNeighbors(self, vert):
        """
            Check if the vertex is already a neighbor to this current one 
        """
        if not self.__neighbors:
            return False

        for storedVert, _ in self.__neighbors:
            if vert == storedVert:
                return True

        return False

    @property
    def neighbors(self):
        """
            Get the keys of the neighbors of the vertex
        """
        return [vertKey for vertKey, _ in self.__neighbors]

    def addNeighbor(self, vert: tuple):
        """
            Add a neighbor to this vertex
        """
        if not self.__inNeighbors(vert):
            self.__neighbors.append(vert)


class Graph:
    def __init__(self):
        self.graph = {}
        self.verticies = 0
        self.edges = 0

    def addVertex(self, vertex: Vertex):
        """
            Add a vertex to the graph

            Args:
                vertex - The vertex object that we would like to be adding.
        """
        if vertex not in self.graph:
            self.graph[vertex] = vertex
            self.verticies += 1

        raise KeyError("The Vertex you're trying to add already exists")

    def getVertex(self, vertKey: int):
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

    def getVerticies(self):
        """
            Return a list of all the vertex keys

            Returns:
                a list of all verticies objects within the graph
        """
        return self.graph.keys()

    def addEdge(self, fromVert: Vertex, toVert: Vertex, weight: float = 0):
        """
           Add an edge to the graph 

           Args:
               fromVert - The vertex object we're connecting the toVert to
               toVert - The vertex object we're connecting the fromVert to
               weight - (0) - The weight of the edge 
        """
        if fromVert not in self.graph or toVert not in self.graph:
            raise ValueError("One of the verticies is not currently in the graph.")
        elif fromVert == toVert:
            raise ValueError("You cannot have a vertex connect to itself.")

        self.graph[fromVert].addNeighbor((toVert, weight))
        self.graph[toVert].addNeighbor((fromVert, weight))

        self.edges += 1

    def getNeighbors(self, vert: Vertex):
        """
            Get the neighbors of a vertex stored within the graph.

            Args:
                vert: The vertex we're trying to get the neighbors of.
        """
        if vert not in self.graph:
            raise KeyError("The vertex is not in the graph")

        return self.graph[vert].neighbors


import argparse


def main(filename):
    graph = None
    verts = []
    edges = []
    with open(filename, "r") as file:
        counter = 0
        for line in file:
            if line == "G" and not graph:
                graph = Graph()
            else:
                if counter == 1:
                    for key in line.strip().split(","):
                        verts.append(Vertex(key))
                elif counter > 1:
                    edge = line.strip(["(", ")"]).split(",")
                    if len(edge) > 3:
                        raise Exception(
                            f"You specified way too many arguments for the edge: {line}"
                        )
                    edges.append(edge)

    print(verts)
    print(edges)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")

    main(args.filename)
