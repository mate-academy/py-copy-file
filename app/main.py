import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source, target = parts[1], parts[2]

    if source == target:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as src, open(target, "w") as dst:
        dst.write(src.read())
