def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if command_parts[0] == "cp" and len(command_parts) == 3:
        file_in = command_parts[1]
        file_out = command_parts[2]
        if file_in != file_out:
            try:
                with open(file_in) as read, open(file_out, "w") as write:
                    write.write(read.read())
            except FileNotFoundError:
                pass
