def copy_file(command: str) -> None:
    command_as_list = command.split()
    if command_as_list[1] == command_as_list[2]:
        return
    with open(f"{command_as_list[1]}", "r") as input_file,\
            open(f"{command_as_list[2]}", "w") as output_file:
        output_file.write(input_file.read())
