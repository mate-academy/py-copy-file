import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_name = parts[1]
    destination_name = parts[2]

    if not os.path.isfile(source_name):
        return

    if source_name == destination_name:
        return

    with (open(source_name, "r") as source,
            open(destination_name, "w") as destination):
        destination.write(source.read())
