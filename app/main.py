def copy_file(command: str) -> None:
    command_tuple = tuple(command.split(" "))
    if ((len(command_tuple) != 3
        or command_tuple[1] == command_tuple[2])
            or command_tuple[0] != "cp"):
        return
    with (open(command_tuple[1], "r") as file_in,
          open(command_tuple[2], "w") as file_out):
        file_out.write(file_in.read())
