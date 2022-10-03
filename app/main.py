def copy_file(command: str) -> None:
    cp, file, file_copy = command.split(" ")

    if file == file_copy or cp != "cp":
        return

    with open(file, "r+") as line:
        line.write(line.read())
