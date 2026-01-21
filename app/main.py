import os


def copy_file(command: str) -> None:
    if not command:
        return
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    name1, name2 = parts[1], parts[2]
    if name1 == name2:
        return
    if not os.path.exists(name1):
        return
    with open(name1, "rb") as f1, open(name2, "wb") as f2:
        f2.write(f1.read())
