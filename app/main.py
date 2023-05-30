def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        cp = command_list[0]
        src_file = command_list[1]
        dst_file = command_list[2]

        if src_file != dst_file and cp == "cp":
            with open(src_file, "r") as file1, open(dst_file, "w") as fin_file:
                fin_file.write(file1.read())
