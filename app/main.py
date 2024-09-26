def copy_file(command: str) -> None:
    cp, file, file_copy = command.split()
    if cp != "cp":
        return
    if file == file_copy:
        return
    with open(file, "r") as file_in, open(file, "w") as file_out:
        for line in file_in:
            file_out.write(line)
