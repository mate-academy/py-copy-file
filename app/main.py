def copy_file(command: str) -> None:
    list_of_commands = command.split()
    if list_of_commands[1] != list_of_commands[2] and list_of_commands[0] == "cp":
        with open(list_of_commands[1], "r") as origin_file,\
                open(list_of_commands[2], "w") as new_file:
            new_file.write(origin_file.read())
