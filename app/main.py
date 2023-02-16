def copy_file(command: str) -> None:
    command = command.split()
    for i in range(2, len(command)):
        if command[1] != command[i]:
            with open(command[1]) as file1:
                file1 = file1.read()
                file_empty = len(file1)
                print(file_empty)
                if file_empty != 0:
                    with open(command[i], "w") as file2:
                        file2.write(file1)
