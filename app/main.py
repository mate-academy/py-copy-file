def copy_file(command: str) -> None:
    command_list = command.split(" ")
    file_part = str(command_list[1])
    file_out_part = str(command_list[2])
    if file_part != file_out_part:
        with open(file_part, "r") as file_in,\
                open(file_out_part, "w") as file_out:
            file_out.write(file_in.read())
