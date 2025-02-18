import argparse


def copy_file(command: str) -> None:
    parser = argparse.ArgumentParser(
        description="Copy the content of one file to another."
    )
    parser.add_argument("source", help="Path to the source file")
    parser.add_argument("destination", help="Path to the destination file")

    args = parser.parse_args(command.split())

    if args.source == args.destination:
        return

    try:
        with (open(args.source, "r") as source_file,
              open(args.destination, "w") as destination_file):
            destination_file.write(source_file.read())
    except FileNotFoundError:
        print(f"Error: {args.source} not found.")
    except PermissionError:
        print("Error: Permission denied to read/write files.")
