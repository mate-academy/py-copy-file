def copy_file(command: str) -> None:
    command_ls = command.split()
    file_old, file_new = command_ls[1], command_ls[2]
    if file_old != file_new and command_ls[0] == "cp":
        with open(file_old, "r") as file_in, open(file_new, "w") as file_out:
            file_out.write(file_in.read())
