def copy_file(command: str) -> None:
    command_list = command.split()
    with open(f"{command_list[1]}", "r") as file_in,\
            open(f"{command_list[2]}", "w") as file_out:
        if command_list[1] != command_list[2]:
            file_out.write(file_in.read())
