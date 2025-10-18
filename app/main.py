import os


def copy_file(command: str) -> None:
    tokens = command.split()
    if len(tokens) != 3:
        return

    cmd, source, destination = tokens

    if cmd != "cp":
        return

    if source == destination:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
