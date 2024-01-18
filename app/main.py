import os
import sys


def copy_file(command: str) -> None:
    os.chdir(os.path.dirname(sys.argv[0]))
    items = command.split(" ")
    reference_name, copy_name = items[1], items[2]

    if reference_name == copy_name:
        return
    if copy_name in os.listdir(os.getcwd()):
        return
    else:
        open(copy_name, "x").write(open(reference_name, "r").read())
