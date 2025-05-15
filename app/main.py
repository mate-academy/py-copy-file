import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    file, file_copy = parts[1], parts[2]

    if file == file_copy:
        return

    if not os.path.isfile(file):
        return

    with open(file, "r") as file_in, open(file_copy, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
