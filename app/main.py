def copy_file(command: str) -> None:
    command_items = command.split()

    if command_items[1] != command_items[2]:
        with open(command_items[1], "r") as input_file, \
             open(command_items[2], "w") as output_file:
            output_file.write(input_file.read())
