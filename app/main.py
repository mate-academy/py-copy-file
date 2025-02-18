def copy_file(command: str) -> None:
    part = command.split()
    if part[0] != "cp" or len(part) != 3:
        return
    file_first = part[1]
    file_second = part[2]
    if file_first == file_second:
        return
    try:
        with (open(file_first, "r") as file_in,
              open(file_second, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
