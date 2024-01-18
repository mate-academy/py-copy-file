from os import path, listdir, getcwd, chdir
from sys import argv


def copy_file(command: str) -> None:
    chdir(path.dirname(argv[0]))
    ref = command.split(" ")[1]
    new = command.split(" ")[2]
    if ref == new or new in listdir(getcwd()):
        return
    open(new, "x").write(open(ref, "r").read())
