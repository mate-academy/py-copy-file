import os


def copy_file(command: str) -> None:

    if not command:
        return

    splitted = command.split()

    if splitted[0] != "cp":
        return

    if len(splitted) > 3 or len(splitted) < 3:
        return

    if not os.path.exists(splitted[1]):
        return

    if splitted[1] == splitted[2]:
        return

    with open(splitted[1], "r") as file:
        with open(splitted[2], "w") as file2:
            content = file.read()
            file2.write(content)
