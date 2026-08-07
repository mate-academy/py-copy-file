import os


def copy_file(command):
    """Copy a file using a Linux-style cp command string.

    Expected format: "cp source.txt destination.txt"
    """
    if not command:
        return

    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_name, target_name = parts[1], parts[2]

    if os.path.abspath(source_name) == os.path.abspath(target_name):
        return

    if not os.path.exists(source_name):
        return

    with open(source_name, "r") as file_in, open(target_name, "w") as file_out:
        file_out.write(file_in.read())
