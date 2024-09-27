def copy_file(command: str) -> None:
    commands = command.split()
    if commands[1] != commands[2]:
        with open(commands[1], "r") as f, open(commands[2], "w") as new_file:
            new_file.write(f.read())
