def copy_file(command: str) -> None:
    command_name, file_name1, file_name2 = command.split()
    if command_name == "cp" and file_name1 != file_name2:
        with open(file_name1, "r") as file_in,\
                open(file_name2, "w") as file_out:
            file_out.write(file_in.read())
