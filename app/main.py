def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[1] != command_list[2] and command_list[0] == "cp":
        with open(command_list[1], "r") as \
                file_in, open(command_list[2], "w") as file_out:
            file_out.write(file_in.read())
