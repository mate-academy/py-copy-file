def copy_file(command: str) -> None:
    command = command.split()
    command_order = command[0]
    origin_file = command[1]
    copy_file = command[2]
    if origin_file != copy_file and command_order == "cp":
        with open(origin_file, "r") as file_in, open(copy_file, "w") as file_out:
            file_out.write(file_in.read())
