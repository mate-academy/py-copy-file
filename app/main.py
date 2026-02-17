import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    operation, source_file_name, destination_file_name = parts

    if operation != "cp":
        return

    if source_file_name == destination_file_name:
        return

    if not os.path.exists(source_file_name):
        return

    with open(source_file_name, "r") as source_file_object, \
         open(destination_file_name, "w") as destination_file_object:
        for line in source_file_object:
            destination_file_object.write(line)
