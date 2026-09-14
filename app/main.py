import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    action, source_file, target_file = parts

    if action != "cp":
        return

    if source_file == target_file:
        return

    if not os.path.exists(source_file):
        return

    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
