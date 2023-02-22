def copy_file(command: str) -> None:
    copy_command, original, copy = command.split()
    if original != copy:
        with open(original, "r") as file_in, open(copy, "w") as copy:
            copy.write(file_in.read())
