import os


def copy_file(command: str) -> None:
    parts = command.split()

    # Do nothing if the command isn't exactly: cp <source> <destination>
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, destination = parts

    # Do nothing if source and destination are the same file
    if source == destination:
        return

    # Do nothing if the source file doesn't exist
    if not os.path.isfile(source):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
