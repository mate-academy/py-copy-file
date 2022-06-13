def copy_file(command: str):
    if command.split()[1] != command.split()[2]:
        with open(command.split()[1], "r") as file, \
                open(command.split()[2], "w") as new_file:
            new_file.write(file.read())
