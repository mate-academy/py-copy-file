def copy_file(command: str) -> None:
    ls_command = command.split(" ")
    if len(ls_command) == 3 \
            and ls_command[1] != ls_command[2] \
            and ls_command[0] == "cp":
        try:
            with open(ls_command[1], "r") as file_in, \
                    open(ls_command[2], "w") as file_out:
                file_read_object = file_in.read()
                file_out.write(file_read_object)
        except FileNotFoundError:
            return
    else:
        return
