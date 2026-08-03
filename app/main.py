import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return

    _, source_file_name, destination_file = parts
    if source_file_name == destination_file:
        return

    if not os.path.exists(source_file_name):
        return

    with open(source_file_name, "r") as source_file_object, \
         open(destination_file, "w") as file_out:
        file_out.write(source_file_object.read())
