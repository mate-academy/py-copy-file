import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3 or parts[0] != "cp":
        return
    _, src, dest = parts[:3]
    if src == dest or not os.path.exists(src):
        return
    with open(src, "rb") as file_in, \
            open(dest, "wb") as file_out:
        file_out.write(file_in.read())
