def copy_file(command: str) -> None:
    part = command.split()
    if len(part) < 3:
        return
    if part[0] != "cp":
        return
    if part[1] == part[2]:
        return
    try:
        with open(part[1], "r") as file_in, open(part[2], "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
