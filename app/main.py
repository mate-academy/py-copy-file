import os


def copy_file(command: str) -> None:
    """Copy a file similar to Linux cp command.

    Args:
        command: A string like "cp source_file dest_file"
    """
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    dest_file = parts[2]

    if source_file == dest_file:
        return

    if not os.path.exists(source_file):
        return

    with open(source_file, "r") as file_in, open(dest_file, "w") as file_out:
        file_out.write(file_in.read())
