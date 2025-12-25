def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command, file_original, file_copy = command.split()
        if command == "cp" and file_original != file_copy:
            with (
                open(file_original, "r") as read,
                open(file_copy, "w") as write
            ):
                write.write(read.read())
