def copy_file(command: str) -> None:
    if len(command) > 0:
        tokens = command.split(" ")
        if len(tokens) == 3:
            needed_command = tokens[0]
            file_name = tokens[1]
            new_file_name = tokens[2]
            if needed_command == "cp" and file_name != new_file_name:
                try:
                    with open(file_name, "r") as file_in, \
                            open(new_file_name, "w") as file_out:
                        data = file_in.read()
                        file_out.write(data)
                except FileNotFoundError:
                    pass
