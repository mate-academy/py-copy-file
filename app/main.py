import os


def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3:
        return

    cmd, source, goal = parts

    if cmd != "cp" or source == goal:
        return

    if not os.path.isfile(source):
        return

    with open(source, "r") as file_in, open(goal, "w") as file_out:
        file_out.write(file_in.read())
