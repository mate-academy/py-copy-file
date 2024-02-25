def copy_file(command: str) -> None:
    list_of_commands = command.strip().split()

    if (
        len(list_of_commands) == 3
        and list_of_commands[0] == "cp"
        and list_of_commands[1] != list_of_commands[2]
    ):
        with open(list_of_commands[2], "w") as destination_file:
            with open(list_of_commands[1], "r") as source_file:
                destination_file.write(source_file.read())
    pass
