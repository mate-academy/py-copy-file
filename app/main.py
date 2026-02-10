import shutil
import os


def copy_file(command: str) -> int:

    args = command.split(" ")

    if len(args) != 3:
        return 1
    if args[0] != "cp":
        return 1

    source_path = os.path.abspath(args[1])
    dest_path = os.path.abspath(args[2])

    if source_path == dest_path:
        return 0

    try:
        shutil.copyfile(source_path, dest_path)
    except OSError:
        return 1
    else:
        return 0
