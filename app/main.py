import shutil
import os


def copy_file(command: str) -> int:

    args = command.split(" ")

    if len(args) < 3:
        return 1

    cm = args[0]
    file1 = os.path.abspath(args[1])
    file2 = os.path.abspath(args[2])

    if cm == "cp":
        try:
            shutil.copyfile(file1, file2)
        except OSError:
            return 1
        else:
            return 0

    return 1
