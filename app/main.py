import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source, destination = command_parts

    if not os.path.exists(source):
        return

    destination_path = os.path.join(os.getcwd(), destination)

    if os.path.abspath(source) == os.path.abspath(destination_path):
        return

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)
