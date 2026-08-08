def copy_file(command: str) -> None:

    if command:
        separate_command = command.split(" ")
        if len(separate_command) == 3 and separate_command[0] == "cp":
            source_file = separate_command[1]
            destination_file = separate_command[2]
            if source_file == destination_file:
                return
            if len(source_file) > 0:
                try:
                    with (open(source_file, "r") as file_out,
                          open(destination_file, "w") as file_in):
                        file_in.write(file_out.read())
                except FileNotFoundError:
                    pass
