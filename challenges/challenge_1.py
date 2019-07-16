"""
    The implementation of a graph, digraph, and vertex within python!
"""
import argparse

from digraph import Digraph
from graph import Graph
from vertex import Vertex


def fill_graph(graph: Graph, verts: list, edges: list):
    """
        Fill an undirected graph object with verticies and edges.

        Args:\n
            graph - the graph object that is going to be filled\n
            verts - A list of vertex objects to add to the graph\n
            edges - A list of tuples that contain edge keys and weights.\n
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

        # Iterate through the file
        for line in file:

            # Obtain the type of graph
            if counter == 0:
                graph_type = line.strip()
                if graph_type == "G":
                    graph = Graph()
                elif graph_type == "D":
                    graph = Digraph()
                else:
                    raise ValueError("Graph type not properly specified")

            # Obtain the verticies for the graph.
            elif counter == 1:
                for key in line.strip().split(","):
                    verts.append(Vertex(key))

            # Obtain all the edges.
            elif counter > 1:
                edge = line.strip("()\n").split(",")
                if len(edge) != 3 and len(edge) != 2:
                    raise ValueError(
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

    print(graph)
    return graph


def process_args() -> argparse.Namespace:
    """
        Process the command line arguments

        Returns:
            an argparser namespace for the parsed objects.
    """
    arg_parser = argparse.ArgumentParser(description="Create a graph from text files")
    arg_parser.add_argument("filename", help="The name of the file to read from")
    arguments = arg_parser.parse_args()

    return arguments


if __name__ == "__main__":
    ARGS = process_args()

    if not ARGS.filename:
        raise Exception("You didn't provide a file argument!")
    main(ARGS.filename)
