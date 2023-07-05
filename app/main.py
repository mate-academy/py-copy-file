def copy_file(command: str) -> None:
    words = command.split()
    file1 = words[1]
    file2 = words[2]

    if file1 == file2:
        return

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
