def copy_file(command: str) -> None:
    commands = command.split(" ")
    if commands[0] == "cp" and len(commands) == 3:
        try:
            if commands[1] == commands[2]:
                return
            with (
                open(commands[1]) as source,
                open(commands[2], "w") as target
            ) :
                target.write(source.read())
        except FileNotFoundError:
            pass
