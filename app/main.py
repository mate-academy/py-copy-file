def copy_file(command: str):
    command = command.split()
    if command[1] != command[2]:
        with open(command[2], "w") as new_file:
            new_file.write(open(command[0]).read())
