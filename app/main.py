def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] != "cp" or command_list[1] == command_list[2]:
        return

    with open(command_list[1], "r") as file:
        with open(command_list[2], "w") as new_file:
            new_file.write(file.read())
