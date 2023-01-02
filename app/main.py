def copy_file(command: str) -> None:
    list_command = command.split()
    if list_command[0] == "cp":
        if list_command[1] != list_command[2]:
            with open(list_command[1], "r") as file_in,\
                    open(list_command[2], "w") as file_out:
                file_out.write(file_in.read())
