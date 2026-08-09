import os


def copy_file(command: str) -> None:
    """
    Copy a file to a new file, similar to the Linux 'cp' command.

    Does nothing (no exception raised) if:
    - the command is empty or has the wrong number of arguments,
    - the command does not start with 'cp',
    - the source file does not exist,
    - the source and destination file names are the same.

    :param command: str, a command string in the form
        "cp <source_file> <destination_file>".
    """
    parts = command.split()

    if len(parts) != 3:
        return

    action, source_file, destination_file = parts

    if action != "cp":
        return

    if source_file == destination_file:
        return

    if not os.path.exists(source_file):
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
