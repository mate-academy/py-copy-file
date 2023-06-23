def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        if command[0] == "cp" and command[1] != command[2]:
            with open(command[1], "r") as file_in, \
                    open(command[2], "w") as file_out:
                content_file = file_in.read()
                file_out.write(content_file)
