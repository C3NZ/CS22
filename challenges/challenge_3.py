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
    parser.add_argument("from_vert", help="The vertex you'd like to start at", type=str)
    parser.add_argument("to_vert", help="The vertex you'd like to end up at", type=str)

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

    if not args.from_vert:
        raise ValueError("You didn't specify a from vertex to start at!")

    if not args.to_vert:
        raise ValueError("You didn't specify a to vertex to start at!")

    # Obtain the graph properties and then fill out the graph.
    graph, vertex, edges = read_graph_file(args.filename)
    fill_graph(graph, vertex, edges)

    path = graph.find_path(args.from_vert, args.to_vert)

    if path:
        print(f"There exists a path between {args.from_vert} and {args.to_vert}: TRUE")
        print("Vertices in path: ", end="")
        for vert in path:
            if vert.key != args.to_vert:
                print(f"{vert},", end="")
            else:
                print(f"{vert}")
    else:
        print(f"There exists a path between {args.from_vert} and {args.to_vert}: FALSE")


if __name__ == "__main__":
    ARGS = process_args()
    main(ARGS)
