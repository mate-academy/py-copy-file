def copy_file(command: str) -> None:
    if not command:
        return
    split_command = command.split()
    if len(split_command) != 3:
        return
    cmd, source, dest = split_command
    if cmd != "cp":
        return
    if source == dest:
        return
    try:
        with open(source, "r") as file_src, open(dest, "w") as file_dest:
            file_dest.write(file_src.read())
    except FileNotFoundError:
        return
