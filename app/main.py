def copy_file(command: str) -> None:
    if len(command.split(" ")) == 3:
        command, file, copy = command.split(" ")
    if command == "cp" and file != copy:
        with open(file, "r") as old_file, open(copy, "w") as new_file:
            new_file.write(old_file.read())
