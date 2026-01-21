import os


def copy_file(command: str) -> None:
    command, source_file, destination_file = command.split()

    if command != "cp":
        raise ValueError("Invalid command format. "
                         "Usage: cp <source_file> <destination_file>")

    if not os.path.exists(source_file):
        raise ValueError(f"Source file '{source_file}' does not exist")

    if os.path.abspath(source_file) == os.path.abspath(destination_file):
        raise ValueError("Source and destination files are the same")

    with open(source_file, "rb") as sourcefile, (
            open(destination_file, "wb")
    ) as destinationfile:
        destinationfile.write(sourcefile.read())
