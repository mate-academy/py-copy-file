def copy_file(command: str) -> None:
    command = command.split()
    if command[0] == "cp" and command[1] != command[2]:
        with open(command[1], "r") as file, open(command[2], "w") as new_file:
            new_file.write(file.read())
