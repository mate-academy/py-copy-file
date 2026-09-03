import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    _, source_file_name, destination_file_name = parts

    if source_file_name == destination_file_name:
        return

    if not os.path.exists(source_file_name):
        return

    with open(source_file_name, "r") as source_file, open(
        destination_file_name, "w"
    ) as destination_file:
        destination_file.write(source_file.read())
