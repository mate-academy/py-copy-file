def copy_file(command: str) -> None:
    command_list = command.split()

    command_name = command_list[0]
    file_1_name = command_list[1]
    file_2_name = command_list[2]

    if file_1_name == file_2_name:
        return

    if command_name == "cp":
        with (
            open(file_1_name, "r") as file_1,
            open(file_2_name, "w") as file_2
        ):
            file_2.write(file_1.read())
