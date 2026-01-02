def copy_file(command: str) -> None:
    commands = command.split(" ")
    if (
            len(commands) == 3
            and commands[0] == "cp"
            and commands[1] != commands[2]
    ):
        with (
            open(commands[1], "r") as file,
            open(commands[2], "w") as copied_file
        ):
            copied_file.write(file.read())
