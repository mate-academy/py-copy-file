def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] == "cp" and len(command_list) == 3:
        if command_list[1] and command_list[2]:
            if command_list[1] != command_list[2]:
                try:
                    with (open(command_list[1], "r") as file_source_obj,
                          open(command_list[2], "w") as file_dest_obj):
                        file_dest_obj.write(file_source_obj.read())
                except FileNotFoundError:
                    pass
