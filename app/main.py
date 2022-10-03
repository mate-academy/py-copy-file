def copy_file(command: str) -> None:
    cp, file, file_copy = command.split(" ")

    if file == file_copy or cp != "cp":
        with open(file, "r") as line, open(file, "w") as copy:
            copy.write(line.read())
