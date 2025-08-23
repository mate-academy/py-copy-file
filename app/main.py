import os

def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dst = parts

    if src == dst:
        return

    if not os.path.exists(src):
        return

    with open(src, "r", encoding="utf-8") as file_in, \
         open(dst, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
