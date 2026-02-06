import os
import shutil


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    _, src, dst = parts
    if src == dst or not os.path.exists(src):
        return
    else:
        shutil.copy(src, dst)
