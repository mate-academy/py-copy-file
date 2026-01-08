import os


def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dest = parts

    if src == dest:
        return

    if not os.path.exists(src):
        return

    with open(src, "r") as file_in, open(dest, "w") as file_out:
        file_out.write(file_in.read())
