import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source_file, target_file = command_parts

    if (
        source_file == target_file
        or not os.path.exists(source_file)
    ):
        return

    with open(source_file, "r") as source_file_object, open(
        target_file, "w"
    ) as target_file_object:
        target_file_object.write(source_file_object.read())
