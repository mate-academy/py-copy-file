def copy_file(command: str) -> None:
    line = command.split(" ")
    file1 = line[1]
    file2 = line[2]
    if file1 == file2:
        return
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        for _ in file1:
            file_out.write(file_in.readline())
