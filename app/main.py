def copy_file(command: str) -> None:
    command = command.split()
    if command[1] != command[2]:
        with open(command[1]) as file1, open(command[2], "w") as file2:
            file2.write(file1.read())
