def copy_file(command: str) -> None:
    command_list = command.split()
    file_name = command_list[1]
    file_copy_name = command_list[2]

    if file_name == file_copy_name:
        return

    with (open(file_copy_name, "r") as file_in,
            open(file_name, "w") as file_out):
        file_in.write(file_out.read())
