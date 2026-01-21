def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return None
    if command[0] != "cp":
        return None
    if command[1] == command[2]:
        return None
    try:
        with (open(command[1], "r") as file_in,
              open(command[-1], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
