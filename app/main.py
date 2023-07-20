def copy_file(command: str) -> None:
    info = command.split()
    file1 = info[1]
    file2 = info[2]
    if file1 != file2:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
