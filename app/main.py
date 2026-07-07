import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, target = parts

    if source == target or not os.path.exists(source):
        return

    with open(source, "r") as source_file_object:
        with open(target, "w") as target_file_object:
            target_file_object.write(source_file_object.read())
