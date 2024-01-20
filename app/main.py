def copy_file(command_line: str) -> None:
    command_line_splited = command_line.split()
    if len(command_line_splited) == 3:
        command, source_file, new_file = command_line_splited
        if command == "cp" and source_file != new_file:
            with (
                open(source_file, "r") as source,
                open(new_file, "w") as receiver
            ):
                receiver.write(source.read())
