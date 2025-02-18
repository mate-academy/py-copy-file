def copy_file(command: str) -> None:
    arg_command, source_file, copy_name = command.split()
    if arg_command == "cp" and source_file != copy_name:
        with open(source_file, "r") as source, open(copy_name, "w") as copy:
            copy.write(source.read())
