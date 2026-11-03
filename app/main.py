import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    action, source, dest = parts

    if action != "cp" or source == dest:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(dest, "w") as file_out:
        file_out.write(file_in.read())
