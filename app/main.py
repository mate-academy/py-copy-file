def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[1] != command_list[2]\
            and command_list[0] == "cp":
        with (open(command_list[1], "r") as main_file,
              open(command_list[2], "w") as file_copy):
            file_copy.write(main_file.read())
