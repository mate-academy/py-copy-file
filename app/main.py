import os


def copy_file(command: str) -> None:
    names = command.split()
    if len(names) < 3:
        return
    cp, name1, name2 = names
    if name1 == name2 or cp != "cp":
        return
    if not os.path.exists(name1):
        return
    with open(name1, "r") as f1, open(name2, "w") as f2:
        f2.write(f1.read())
