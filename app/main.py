def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[1] == command_list[2] or command_list[0] != "cp":
        return
    else:
        with open(command_list[1], "r") as file_in:
            with open(command_list[2], "w") as file_out:
                file_out.writelines(file_in.readlines())
