def copy_file(command: str) -> None:
    command_split = command.split()
    file_name_1 = command_split[1]
    file_name_2 = command_split[2]

    if file_name_1 != file_name_2:
        with (
            open(file_name_1, "r") as file_in,
            open(file_name_2, "w") as file_out
        ):
            file_out.write(file_in.read())

