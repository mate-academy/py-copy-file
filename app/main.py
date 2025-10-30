import os


def copy_file(command: str) -> None:
    """Copy a file in the current directory like the Linux `cp` command.

    Args:
        command (str): A string containing the copy command in the format
            "cp source_file destination_file".

    The function does nothing if:
        - The source and destination filenames are the same.
        - The command format is invalid.
        - The source file does not exist.
    """
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dest = parts

    if src == dest:
        return

    if not os.path.exists(src):
        # Gracefully exit if source file does not exist
        return

    try:
        with open(src, "r", encoding="utf-8") as file_in, open(
            dest, "w", encoding="utf-8"
        ) as file_out:
            file_out.write(file_in.read())
    except OSError:
        # Handles file permission or I/O errors silently
        return
