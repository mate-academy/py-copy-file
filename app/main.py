def copy_file(command: str) -> None:
    command_line, start, end = command.split()
    if start == end and command_line != "cp":
        return
    with open(start, "r") as f_start, open(end, "w") as f_end:
        f_end.write(f_start.read())
