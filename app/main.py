import os


def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    if parts[1] == parts[2]:
        return
    source, dest = parts[1], parts[2]
    if not os.path.exists(source):
        return
    with open(source, "r") as src, open(dest, "w") as dst:
        dst.write(src.read())
