import argparse
import shlex

parser = argparse.ArgumentParser(
    prog="cp",
    description="Copy file from source to destination",
)

parser.add_argument("source")
parser.add_argument("destination")


def copy_file(user_input: str) -> None:
    cmd, *args = shlex.split(user_input)

    if cmd != "cp":
        parser.print_usage()
        return

    parsed_args = parser.parse_args(args)

    if parsed_args.source == parsed_args.destination:
        return

    with open(parsed_args.source, "r") as source_file, open(
        parsed_args.destination, "w"
    ) as destination_file:
        destination_file.write(source_file.read())
