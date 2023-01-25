def copy_file(command: str) -> None:
    command_ls = command.split(" ")
    command_cp = command_ls[0]
    file_name = command_ls[1]
    file_copy_name = command_ls[2]
    if command_cp != "cp":
        return None
    if file_name != file_copy_name:
        with open(file_name, "r") as file_in, open(file_copy_name, "w") as file_out:
            file_out.write(file_in.read())
