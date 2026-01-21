def copy_file(command: str) -> None:
    command, file, new_file = command.split()
    if file != new_file and command == "cp":
        with open(file, "r") as old_file, open(new_file, "w") as copy:
            copy.write(old_file.read())
