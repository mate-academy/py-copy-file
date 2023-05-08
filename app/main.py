def copy_file(command: str) -> None:
    _, start, end = command.split()
    if start == end:
        return
    with open(start, "r") as f_start, open(end, "w") as f_end:
        f_end.write(f_start.read())
