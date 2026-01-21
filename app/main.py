import os


def copy_file(command: str) -> None:
    try:
        cmd, source, target = command.strip().split()
    except ValueError:
        return

    if cmd != "cp":
        return

    if source == target:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
