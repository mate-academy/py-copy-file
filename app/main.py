def copy_file(command: str) -> None:
    """Copy a file like Linux cp command in the current directory."""
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return  # Invalid command format, do nothing

    src_file, dst_file = parts[1], parts[2]

    if src_file == dst_file:
        return  # Do nothing if source and destination are the same

    try:
        with open(src_file, "r", encoding="utf-8") as file_in, \
                open(dst_file, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass  # Do nothing if the source file does not exist
