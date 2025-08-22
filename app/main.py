def copy_file(command: str) -> None:
    parts = command.strip().split()

    # Check for correct format: "cp source target"
    if len(parts) != 3 or parts[0] != "cp":
        return  # Invalid command format; do nothing

    _, src, dst = parts

    # Do nothing if source and destination are the same
    if src == dst:
        return

    # Try to copy the file content
    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        # Gracefully handle missing source file
        pass
