def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "cp":
        if command_list[-1] == command_list[-2]:
            pass
        else:
            with open(command_list[-2],
                      "r") as file_in, open(command_list[-1],
                                            "w") as file_out:
                file_out.write(file_in.read())


copy_file("cp file.txt new_file.txt")
