def copy_file(command: str) -> None:
    one_command_list = command.split()
    try:
        if len(one_command_list) == 3:
            if ("cp" in one_command_list
                    and one_command_list[1] != one_command_list[2]):

                with (open(one_command_list[1], "r") as file,
                      open(one_command_list[2], "w") as new_file):

                    new_file.write(file.read())
    except FileNotFoundError:
        print("File not found")
