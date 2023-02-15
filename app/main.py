def copy_file(command: str) -> None:
    func, file_1, directory = command.split()
    if file_1 != directory and func == "cp":
        with open(file_1, "r") as old_file, open(directory, "w") as copy:
            copy.write(old_file.read())
