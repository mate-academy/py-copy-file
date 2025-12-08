def copy_file(command: str) -> None:
    if command:
        parsed_command = command.split()
        if len(parsed_command) == 3:
            file_in, file_out = parsed_command[1], parsed_command[2]
            if parsed_command[0] == "cp":
                if file_in != file_out:
                    try:
                        with (open(file_in, "r") as source,
                              open(file_out, "w") as target):
                            target.write(source.read())
                    except FileNotFoundError:
                        pass
