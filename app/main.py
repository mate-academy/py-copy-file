def copy_file(command: str) -> None:
    command = command.split()
    if command[0] == 'cp' and command[1] != command[2]:
        with open(command[2], 'r') as copied, open(command[2], 'w') as file:
            file.write(copied.read())
