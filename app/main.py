def copy_file(command: str) -> None:
    command_list = command.split()
    file_name = command_list[1]
    new_file_name = command_list[-1]
    if file_name == new_file_name:
        return
    if command_list[0] == "cp":
        with open(file_name, "r") as f_in, open(new_file_name, "w") as f_out:
            for line in f_in:
                f_out.write(line)
