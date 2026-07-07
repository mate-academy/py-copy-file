import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, target = parts

    if source == target or not os.path.exists(source):
        return

    with open(source, "r") as file_in:
        with open(target, "w") as file_out:
              file_out.write(file_in.read())
