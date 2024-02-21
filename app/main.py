from os import path, listdir, chdir
from sys import argv


def copy_file(command: str) -> None:
    chdir(path.dirname(argv[0]))
    if command \
        and len(command.split(" ")) == 3 \
        and command[1] != command[2] \
        and command[2] not in listdir():
        ref, copy = command[1], command[2]
        with open(command[2]) as new:
            with open(command[1]) as ref:
                new.write(ref.read())
                ref.close()
            new.close()
    else:
        return
