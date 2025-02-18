def copy_file(command: str) -> None:
    command, file1, file2 = command.split()
    if file1 != file2 and command == "cp":
        with open(file1) as file1, open(file2, "w") as file2:
            file2.write(file1.read())
