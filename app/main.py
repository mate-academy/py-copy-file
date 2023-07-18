def copy_file(command: str) -> None:
    command = command.split()
    if command[1] == command[2]:
        pass
    with open(command[1], "r") as file_from:
        with open(command[2], "w") as file_to:
            file_to.write(file_from.read())



print(copy_file("cp file.txt new_file.txt"))