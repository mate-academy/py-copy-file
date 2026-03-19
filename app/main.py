def copy_file(command: str) -> None:
    command_list = command.split(" ")
    cmd = command_list[0]
    if cmd == "cp" and len(command_list) == 3:
        source_file = command_list[1]
        destination_file = command_list[2]
        if source_file and destination_file:
            if source_file != destination_file:
                try:
                    with (open(source_file, "r") as source_file_obj,
                          open(destination_file, "w") as dest_file_obj):
                        dest_file_obj.write(source_file_obj.read())
                except FileNotFoundError:
                    pass
