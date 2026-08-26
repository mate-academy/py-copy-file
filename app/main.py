import os
import shutil


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src_file, dest_file = parts

    if src_file == dest_file or not os.path.exists(src_file):
        return

    with open(src_file, "r") as file_in, open(dest_file, "w") as file_out:
        shutil.copyfileobj(file_in, file_out)
