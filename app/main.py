def copy_file(command: str) -> None:
    commands = command.split(" ")
    try:
        if commands[0] == "cp" and commands[1] != commands[2]:
            with (
                open(commands[1], "r") as file,
                open(commands[2], "w") as new_file
            ):
                new_file.write(file.read())
    except (FileNotFoundError, IndexError):
        pass
    return
