import os


def copy_file(command: str) -> None:
    components = command.split()
    if len(components) != 3 or components[0] != "cp":
        raise ValueError("Invalid command format. "
                         "Usage: cp <source_file> <destination_file>")

    source_file = components[1]
    destination_file = components[2]

    if source_file == destination_file:
        return

    if not os.path.exists(source_file):
        raise ValueError(f"Source file '{source_file}' does not exist")

    with open(source_file, "rb") as sourcefile, \
            open(destination_file, "wb") as destin_file:
        destin_file.write(sourcefile.read())

