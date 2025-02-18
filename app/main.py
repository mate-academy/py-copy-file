def copy_file(command: str) -> None:
    command, file, copy = command.split()
    if command == "cp" and file != copy:
        with open(file, "r") as source, open(copy, "w") as result:
            result.write(source.read())
