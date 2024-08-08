def copy_file(command: str) -> None:
    data = command.split()
    file1, file2 = data[1], data[2]
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
