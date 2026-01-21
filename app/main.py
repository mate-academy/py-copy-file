def copy_file(command: str) -> None:
    if (command and command[:2] == "cp"):
        commands = command.split(" ")
        if len(commands) == 3 and commands[1] != commands[2]:
            command1 = commands[1][len(commands[1]) - 4:] == ".txt"
            command2 = commands[2][len(commands[2]) - 4:] == ".txt"
            if (command1 and command2):
                try:
                    with (
                        open(commands[1], "r") as file,
                        open(commands[2], "w") as copy_file
                    ):
                        copy_file.write(file.read())
                except FileNotFoundError:
                    return None
