def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[1] != command[2]:
        with open(command[1]) as file1:
            file1 = file1.read()
            file_empty = len(file1)
            if file_empty != 0:
                with open(command[2], "w") as file2:
                    file2.write(file1)
