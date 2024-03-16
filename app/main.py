from os import path, chdir
from sys import argv


def copy_file(command: str) -> None:
    chdir(path.dirname(argv[0]))
    cm = command.split(" ")
    return None if (len(cm) == 1) or (cm[1] == cm[2]) \
        else open(cm[2], "w").write(open(cm[1], "r").read())
