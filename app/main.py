def copy_file(command: str) -> None:
    """
    Copy a file in the current directory like the Linux `cp` command.

    Args:
        command (str): must be in the format "cp <src> <dst>".

    Behavior:
        - Does nothing if <src> and <dst> are the same.
        - Does nothing if the source file does not exist.
        - Copies the full content of <src> into <dst> otherwise.
    """
    parts = command.strip().split()

    # Expected: cp <src> <dst>
    if len(parts) != 3 or parts[0] != "cp":
        return

    src, dst = parts[1], parts[2]
    if src == dst:
        return

    try:
        with open(src, "r", encoding="utf-8") as file_in, \
                open(dst, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        # Handle missing source file gracefully
        return
