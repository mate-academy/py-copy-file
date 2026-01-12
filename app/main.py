import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_filename = parts[1]
    target_filename = parts[2]

    if source_filename == target_filename:
        return

    if not os.path.isfile(source_filename):
        return

    with open(source_filename, "r") as src, open(target_filename, "w") as dst:
        content = src.read()
        dst.write(content)
