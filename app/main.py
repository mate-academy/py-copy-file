import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source, target = parts[1], parts[2]

    if source == target or not os.path.exists(source):
        return

    with open(source, "r") as file_in:
        file_content = file_in.read()

    with open(target, "w") as file_out:
        file_out.write(file_content)
