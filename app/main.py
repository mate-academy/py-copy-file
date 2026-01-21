def copy_file(command: str) -> None:
    command_line = command.split()
    if len(command_line) == 3:
        command, source_path, copy_path = command_line
        if source_path != copy_path and command == "cp":
            with open(source_path, "r") as source, \
                    open(copy_path, "w") as copy:
                date = source.read()
                copy.write(str(date))
