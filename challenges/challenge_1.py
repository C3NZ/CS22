"""
    The implementation of a graph, digraph, and vertex within python!
"""
import argparse

from graphs.graph import Graph, fill_graph
from graphs.utils.file_reader import read_graph_file


def main(filename: str) -> Graph:
    """
        Main functionality of the app, opens the file and then
        parses it into a graph object

        Args:

            filename - The name of the file to open

        Returns:

            A graph object with the specified vertex and edges added
    """
    graph, verts, edges = read_graph_file(filename)

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
