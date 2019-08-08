import argparse

from graphs.graph import fill_graph
from graphs.utils.file_reader import read_graph_file


def process_args():
    """
        Process the arguments for challenge 2
    """
    parser = argparse.ArgumentParser(
        description="Find the shortest path between two verticies"
    )
    parser.add_argument(
        "filename", help="The name of the graph file to parse", type=str
    )

    return parser.parse_args()


def main(args: argparse.Namespace):
    """
        Check if a path exists between two vertices.

        Args:
        * args - The parsed argument namespace from argparse
    """
    # Input checks
    if not args.filename:
        raise ValueError("There was no graph file path specified!")

    # Obtain the graph properties and then fill out the graph.
    graph, vertex, edges = read_graph_file(args.filename)
    fill_graph(graph, vertex, edges)

    is_eulerian = graph.is_eulerian_cycle()
    print(f"This graph is Eulerian: {is_eulerian}")


if __name__ == "__main__":
    ARGS = process_args()
    main(ARGS)
