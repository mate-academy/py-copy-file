def copy_file(command: str):
    command_list = command.split()
    if command_list[0] == "cp" and command_list[1] != command_list[2]:
        with open(command_list[1], "r") as old_file:
            with open(command_list[2], "w") as new_file:
                new_file.write(old_file.read())
