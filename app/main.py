import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source, destination = command_parts

    if not os.path.exists(source):
        return

    directories, _, filename = destination.rpartition("/")

    if not filename:
        filename = os.path.basename(source)

    if directories:
        os.makedirs(directories, exist_ok=True)

    destination_path = os.path.join(directories, filename)

    if os.path.abspath(source) == os.path.abspath(destination):
        return

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)
