def copy_file(command: str) -> None:
    command, file, directory = command.split()
    if file != directory and command == "cp":
        with open(file, "r") as old_file, open(directory, "w") as copy:
            copy.write(old_file.read())
