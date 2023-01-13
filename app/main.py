def copy_file(command: str) -> None:
    list_command = command.split()
    command_name = list_command[0]
    file_name1 = list_command[1]
    file_name2 = list_command[2]
    if command_name == "cp" and file_name1 != file_name2:
        with open(file_name1, "r") as file_in,\
                open(file_name2, "w") as file_out:
            file_out.write(file_in.read())
