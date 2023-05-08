def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    command_line, start, end = command_parts
    if start == end or command_line != "cp":
        return

    with open(start, "r") as f_start, open(end, "w") as f_end:
        f_end.write(f_start.read())
