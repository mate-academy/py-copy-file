def copy_file(command: str) -> None:
    commands = command.split(" ")
    if commands[2] != commands[1]:
        with (open(commands[2], "w") as new_file,
              open(commands[1], "r") as old_file):
            new_file.write(old_file.read())
