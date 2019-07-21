import argparse


def process_args():
    parser = argparse.ArgumentParser(
        description="Find the shortest path between two verticies"
    )
    parser.add_argument(
        "filename", help="The name of the graph file to parse", type=str
    )
    parser.add_argument("from_vert", help="The vertex you'd like to start at", type=int)
    parser.add_argument("to_vert", help="The vertex you'd like to end up at", type=int)

    return parser.parse_args()


def main(args: argparse.Namespace):
    """
        Process the arguments and find the shortest path
    """
    if not args.filename:
        raise ValueError("There was no graph file path specified!")

    if not args.from_vert:
        raise ValueError("You didn't specify a from vertex to start at!")

    if not args.to_vert:
        raise ValueError("You didn't specify a to vertex to start at!")


if __name__ == "__main__":
    ARGS = process_args()
    main(ARGS)
