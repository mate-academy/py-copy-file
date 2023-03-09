def copy_file(command: str) -> None:
    file1, file2 = command.lstrip("cp").split()
    if file1 != file2:
        with open(file1, "r") as file1, \
                open(file2, "w") as file2:
            file2.write(file1.read())
