def copy_file(command: str) -> None:
    list_of_command = command.split()
    if list_of_command[1] != list_of_command[2] and list_of_command[0] == "cp":
        with open(list_of_command[1], "r") as source_file, \
                open(list_of_command[2], "w") as destination_file:
            content = source_file.read()
            destination_file.write(content)
