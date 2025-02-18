def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        cmd = command_list[0]
        src_path = command_list[1]
        dst_path = command_list[2]

        if src_path != dst_path and cmd == "cp":
            with open(src_path, "r") as file1, open(dst_path, "w") as fin_file:
                fin_file.write(file1.read())
