def copy_file(command: str) -> None:
    command = command.split()

    if command[0] != "cp" or command[1] == command[2]:
        return

    with open(command[1], "r") as file, open(command[2], "a") as copy:
        copy.write(file.read())
