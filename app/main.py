def copy_file(command: str) -> None:
    cp, file, file_copy = command.split()
    if cp != "cp" and file == file_copy:
        return
    with open(file, "r") as old_file, open(file, "w") as new_file:
        for line in old_file:
            new_file.write(line)
