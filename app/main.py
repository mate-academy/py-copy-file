def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) != 3 or command_split[0] != "cp":
        return

    file_name = command_split[1]
    new_file_name = command_split[2]

    if file_name == new_file_name:
        return

    try:
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
