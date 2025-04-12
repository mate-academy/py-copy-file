def copy_file(command: str) -> None:
    command_list = command.split()
    if (len(command_list) == 3
            and command.count(" ") == 2
            and command_list[0] == "cp"):
        if command_list[1] != command_list[2]:
            try:
                with (open(command_list[1]) as file,
                      open(command_list[2], "w") as file_copy):
                    file_copy.write(file.read())
            except FileNotFoundError:
                print()
