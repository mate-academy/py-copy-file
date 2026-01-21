import os


def copy_file(command: str) -> None:
    """Simulate Linux 'cp' command for files in the current directory.

    Args:
        command (str): Must be in format 'cp source_file target_file'.

    Does nothing if:
        - Command does not start with 'cp'.
        - Source and target filenames are the same.
        - Source file does not exist.
    """
    parts = command.strip().split()

    # Validate command structure
    if len(parts) != 3 or parts[0] != "cp":
        return

    src, dst = parts[1], parts[2]

    # Do nothing if same file
    if src == dst:
        return

    # Gracefully do nothing if source doesn't exist
    if not os.path.exists(src):
        return

    # Copy content
    with open(src, "r", encoding="utf-8") as file_in, open(
        dst, "w", encoding="utf-8"
    ) as file_out:
        file_out.write(file_in.read())
