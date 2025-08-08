def copy_file(command: str) -> None:
    command_line = command.split()
    if (
        len(command_line) != 3
        or command_line[0] != "cp"
        or command_line[1] == command_line[2]
    ):
        return
    try:
        open(command_line[1], "r")
    except FileNotFoundError:
        return
    with open(command_line[1], "r") as file_in, open(
        command_line[2], "w"
    ) as file_out:
        file_out.write(file_in.read())
